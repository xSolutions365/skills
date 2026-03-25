"""Render the machine-readable runtime input artifact from execplan.md."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from execplan_common import (
    parse_requirements,
    parse_table,
    read_section,
    split_csv_tokens,
    strip_code_markers,
    task_ref,
    normalize_status,
    is_na,
)

TASK_TABLE_HEADING = "## Task Table (single source of truth)"
TEST_PLAN_HEADING = "## Test Plan"
REQUIREMENTS_HEADING = "## Requirements Freeze"

TASK_HEADERS = [
    "Status",
    "Phase #",
    "Task #",
    "Type",
    "Req IDs",
    "File Anchors",
    "Command",
    "Expected Output",
    "Action",
]

TEST_PLAN_HEADERS = [
    "Scenario ID",
    "Priority",
    "Given",
    "When",
    "Then",
    "Evidence Command",
    "Task Ref",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render create-execplan runtime input."
    )
    parser.add_argument("--execplan", required=True, help="Path to execplan.md")
    parser.add_argument(
        "--output",
        default="",
        help=(
            "Output JSON path. Default: <execplan-dir>/workspace/execplan-runtime-input.json"
        ),
    )
    parser.add_argument(
        "--generated-at",
        default="",
        help="Optional generatedAt override for deterministic tests.",
    )
    parser.add_argument(
        "--source-execplan-value",
        default="",
        help="Optional sourceExecplan override for deterministic tests.",
    )
    return parser.parse_args()


def parse_task_rows(source: str) -> list[dict[str, object]]:
    headers, rows = parse_table(read_section(source, TASK_TABLE_HEADING))
    if headers != TASK_HEADERS:
        raise ValueError(
            "Task table columns must exactly match: " + ", ".join(TASK_HEADERS)
        )

    tasks: list[dict[str, object]] = []
    for row in rows:
        phase_number = int(row["Phase #"].strip())
        task_number = int(row["Task #"].strip())
        command = strip_code_markers(row["Command"])
        tasks.append(
            {
                "taskRef": task_ref(phase_number, task_number),
                "status": normalize_status(row["Status"]),
                "phaseNumber": phase_number,
                "taskNumber": task_number,
                "type": row["Type"].strip(),
                "requirementIds": split_csv_tokens(row["Req IDs"]),
                "fileAnchors": split_csv_tokens(row["File Anchors"]),
                "command": "" if is_na(command) else command,
                "expectedOutput": row["Expected Output"].strip(),
                "action": row["Action"].strip(),
            }
        )
    return tasks


def parse_test_plan(source: str) -> list[dict[str, object]]:
    headers, rows = parse_table(read_section(source, TEST_PLAN_HEADING))
    if headers != TEST_PLAN_HEADERS:
        raise ValueError(
            "Test Plan columns must exactly match: " + ", ".join(TEST_PLAN_HEADERS)
        )

    scenarios: list[dict[str, object]] = []
    for row in rows:
        scenarios.append(
            {
                "scenarioId": row["Scenario ID"].strip(),
                "priority": row["Priority"].strip(),
                "given": row["Given"].strip(),
                "when": row["When"].strip(),
                "then": row["Then"].strip(),
                "evidenceCommand": strip_code_markers(row["Evidence Command"]),
                "taskRefs": split_csv_tokens(row["Task Ref"]),
            }
        )
    return scenarios


def render_runtime_input(
    execplan_path: Path, generated_at: str, source_execplan_value: str
) -> dict[str, object]:
    source = execplan_path.read_text(encoding="utf-8")
    requirements = parse_requirements(read_section(source, REQUIREMENTS_HEADING))
    tasks = parse_task_rows(source)
    scenarios = parse_test_plan(source)
    generated_value = generated_at or datetime.now(UTC).isoformat().replace("+00:00", "Z")
    source_execplan = source_execplan_value or str(execplan_path.resolve())
    return {
        "schemaVersion": "2.0",
        "generated": True,
        "editPolicy": "do-not-edit",
        "generatedAt": generated_value,
        "sourceExecplan": source_execplan,
        "requirements": requirements,
        "tasks": tasks,
        "verificationScenarios": scenarios,
    }


def main() -> int:
    args = parse_args()
    execplan_path = Path(args.execplan).resolve()
    output_path = (
        Path(args.output).resolve()
        if args.output
        else execplan_path.parent / "workspace" / "execplan-runtime-input.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = render_runtime_input(
        execplan_path=execplan_path,
        generated_at=args.generated_at,
        source_execplan_value=args.source_execplan_value,
    )
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered ExecPlan runtime input: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
