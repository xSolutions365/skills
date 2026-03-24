#!/usr/bin/env python3
"""Render a machine-readable runtime task packet artifact from execplan.md."""

from __future__ import annotations

import argparse
import json
import re
from datetime import UTC, datetime
from pathlib import Path

HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+)$")
REQ_ID_PATTERN = re.compile(r"R\d+")
ANCHOR_PATTERN = re.compile(r"[^`\s]+:\d+")
COMMAND_BACKTICK_PATTERN = re.compile(r"`([^`]+)`")
COMMAND_PREFIX_PATTERN = re.compile(
    r"^(?:pnpm|npm|node|git|bash|sh|python|python3|cargo|go|make|pytest|vitest|tsc|codex|pi)\b"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render create-execplan runtime task packets."
    )
    parser.add_argument("--execplan", required=True, help="Path to execplan.md")
    parser.add_argument(
        "--output",
        default="",
        help=(
            "Output JSON path. Default: <execplan-dir>/workspace/execplan-task-packets.json"
        ),
    )
    return parser.parse_args()


def lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").split("\n")


def read_section(source: str, heading: str) -> str:
    all_lines = lines(source)
    start_index = -1
    for index, line in enumerate(all_lines):
        if line.strip() == heading:
            start_index = index
            break
    if start_index == -1:
        return ""

    end_index = len(all_lines)
    for index in range(start_index + 1, len(all_lines)):
        if HEADING_PATTERN.match(all_lines[index].strip()):
            end_index = index
            break

    return "\n".join(all_lines[start_index + 1 : end_index]).strip()


def read_bullet_items(section: str) -> list[str]:
    items: list[str] = []
    for line in lines(section):
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def normalize_cell(value: str) -> str:
    return value.strip().removeprefix("`").removesuffix("`")


def parse_table(section: str) -> list[list[str]]:
    rows = [
        line.strip()
        for line in lines(section)
        if line.strip().startswith("|") and line.strip().endswith("|")
    ]
    if len(rows) < 2:
        return []

    header = rows[0]
    body = rows[1:]
    column_count = len(header.split("|")) - 2
    parsed_rows: list[list[str]] = []
    for row in body:
        if re.fullmatch(r"(\|[\s:-]+)+\|", row):
            continue
        values = [normalize_cell(cell) for cell in row[1:-1].split("|")]
        while len(values) < column_count:
            values.append("")
        parsed_rows.append(values)
    return parsed_rows


def read_requirements(section: str) -> list[dict[str, str]]:
    requirements: list[dict[str, str]] = []
    for item in read_bullet_items(section):
        match = re.match(r"^(R\d+):\s*(.*)$", item)
        if not match:
            continue
        requirements.append({"id": match.group(1), "text": match.group(2)})
    return requirements


def extract_backticked(text: str) -> list[str]:
    matches = [match.group(1) for match in COMMAND_BACKTICK_PATTERN.finditer(text)]
    unique = list(dict.fromkeys(item for item in matches if item))
    return unique


def extract_commands(description: str) -> list[str]:
    return [
        item for item in extract_backticked(description) if COMMAND_PREFIX_PATTERN.match(item)
    ]


def extract_expected_outputs(description: str) -> list[str]:
    outputs = [
        match.group(1).strip()
        for match in re.finditer(r"(?:confirm|expect|ensure)\s+([^.;]+)(?:[.;]|$)", description, re.IGNORECASE)
    ]
    fallback = [
        item
        for item in extract_backticked(description)
        if re.search(r"expected|success|pass|complete|blocked|error", item, re.IGNORECASE)
    ]
    combined = list(dict.fromkeys([*outputs, *fallback]))
    return [item for item in combined if item]


def task_ref(phase_number: int, task_number: int) -> str:
    return f"P{phase_number}-T{task_number}"


def parse_task_rows(source: str) -> list[dict[str, object]]:
    task_rows = parse_table(read_section(source, "## Task Table (single source of truth)"))
    parsed: list[dict[str, object]] = []
    for row in task_rows:
        phase_number = int((row[1] or "0").strip())
        task_number = int((row[2] or "0").strip())
        description = row[4].strip()
        parsed.append(
            {
                "taskRef": task_ref(phase_number, task_number),
                "phaseNumber": phase_number,
                "taskNumber": task_number,
                "type": row[3].strip() or "Action",
                "description": description,
                "requirementIds": list(dict.fromkeys(REQ_ID_PATTERN.findall(description))),
                "fileAnchors": list(dict.fromkeys(ANCHOR_PATTERN.findall(description))),
                "allowedCommands": extract_commands(description),
                "expectedOutputs": extract_expected_outputs(description),
            }
        )
    return parsed


def split_req_ids(raw: str) -> list[str]:
    tokens = [token.strip() for token in raw.split(",")]
    return [token for token in tokens if REQ_ID_PATTERN.fullmatch(token)]


def parse_test_plan(source: str) -> dict[str, list[dict[str, object]]]:
    test_rows = parse_table(read_section(source, "## Test Plan"))
    scenarios_by_task: dict[str, list[dict[str, object]]] = {}
    for row in test_rows:
        scenario = {
            "scenarioId": row[0] if len(row) > 0 else "",
            "requirementIds": split_req_ids(row[1] if len(row) > 1 else ""),
            "priority": row[2] if len(row) > 2 else "",
            "evidenceCommand": normalize_cell(row[6] if len(row) > 6 else ""),
            "taskRef": row[7] if len(row) > 7 else "",
        }
        task_key = str(scenario["taskRef"])
        scenarios_by_task.setdefault(task_key, []).append(scenario)
    return scenarios_by_task


def parse_quality_gates(source: str) -> list[str]:
    quality_rows = parse_table(read_section(source, "## Quality Gates"))
    commands: list[str] = []
    for row in quality_rows:
        if len(row) > 1 and row[1].strip():
            commands.append(normalize_cell(row[1]))
    return list(dict.fromkeys(commands))


def render_runtime_artifact(execplan_path: Path) -> dict[str, object]:
    source = execplan_path.read_text(encoding="utf-8")
    requirements = read_requirements(read_section(source, "## Requirements Freeze"))
    tasks = parse_task_rows(source)
    scenarios_by_task = parse_test_plan(source)
    quality_gate_commands = parse_quality_gates(source)

    task_packets: list[dict[str, object]] = []
    for task in tasks:
        task_ref_value = str(task["taskRef"])
        scenarios = scenarios_by_task.get(task_ref_value, [])
        scenario_requirement_ids: list[str] = []
        evidence_commands = list(quality_gate_commands)
        for scenario in scenarios:
            scenario_requirement_ids.extend(scenario["requirementIds"])  # type: ignore[arg-type]
            evidence_command = str(scenario["evidenceCommand"])
            if evidence_command:
                evidence_commands.append(evidence_command)

        task_packets.append(
            {
                "taskRef": task_ref_value,
                "phaseNumber": task["phaseNumber"],
                "taskNumber": task["taskNumber"],
                "type": task["type"],
                "description": task["description"],
                "requirementIds": list(
                    dict.fromkeys(
                        [
                            *task["requirementIds"],  # type: ignore[list-item]
                            *scenario_requirement_ids,
                        ]
                    )
                ),
                "fileAnchors": task["fileAnchors"],
                "allowedCommands": task["allowedCommands"],
                "evidenceCommands": list(dict.fromkeys(evidence_commands)),
                "expectedOutputs": task["expectedOutputs"],
                "adrThreshold": {
                    "requiresHumanApproval": True,
                    "triggerTerms": [
                        "architecture",
                        "interface",
                        "schema",
                        "data model",
                        "public API",
                        "ADR",
                    ],
                },
            }
        )

    return {
        "schemaVersion": "1.0",
        "generated": True,
        "editPolicy": "do-not-edit",
        "generatedAt": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "sourceExecplan": str(execplan_path.resolve()),
        "requirements": requirements,
        "taskPackets": task_packets,
    }


def main() -> int:
    args = parse_args()
    execplan_path = Path(args.execplan).resolve()
    output_path = (
        Path(args.output).resolve()
        if args.output
        else execplan_path.parent / "workspace" / "execplan-task-packets.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = render_runtime_artifact(execplan_path)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered ExecPlan runtime artifact: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
