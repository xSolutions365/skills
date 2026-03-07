#!/usr/bin/env python3
"""Validate ExecPlan completeness for create-execplan."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_HEADINGS = (
    "## Requirements Freeze",
    "## Success Criteria",
    "## Verification Strategy",
    "## Dependency Preconditions",
    "## Task Table (single source of truth)",
    "## Test Plan",
    "## Quality Gates",
)

TABLE_REQUIRED = (
    "## Dependency Preconditions",
    "## Task Table (single source of truth)",
    "## Test Plan",
    "## Quality Gates",
)

ANCHOR_PATTERN = re.compile(r"[^`\s]+:\d+")
COMMAND_PATTERN = re.compile(r"`[^`]+`")
VAGUE_TASK_PATTERN = re.compile(
    r"\b(investigate|review|consider|look at|think about|explore)\b", re.IGNORECASE
)
PLACEHOLDER_PATTERN = re.compile(r"<[^>]+>")
REQ_ID_PATTERN = re.compile(r"^R\d+$")
SCENARIO_ID_PATTERN = re.compile(r"^S\d+$")
TASK_REF_PATTERN = re.compile(r"^P\d+-T\d+$")
TEST_PRIORITIES = {"P0", "P1", "P2"}
TEST_PLAN_REQUIRED_COLUMNS = (
    "Scenario ID",
    "Req IDs",
    "Priority",
    "Given",
    "When",
    "Then",
    "Evidence Command",
    "Task Ref",
)
MAX_BDD_STEP_LENGTH = 180


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate create-execplan ExecPlan.")
    parser.add_argument("--execplan", required=True, help="Path to execplan.md")
    parser.add_argument(
        "--output",
        default="",
        help="Validation output JSON path. Default: <execplan-dir>/execplan-validation.json",
    )
    return parser.parse_args()


def find_heading_index(lines: list[str], heading_prefix: str) -> int:
    for idx, line in enumerate(lines):
        if line.strip().startswith(heading_prefix):
            return idx
    return -1


def extract_section(lines: list[str], heading_prefix: str) -> list[str]:
    start = find_heading_index(lines, heading_prefix)
    if start < 0:
        return []
    end = len(lines)
    for idx in range(start + 1, len(lines)):
        if lines[idx].startswith("## "):
            end = idx
            break
    return lines[start:end]


def parse_table_rows(
    section_lines: list[str],
) -> tuple[list[str], list[dict[str, str]]]:
    table_lines = [line for line in section_lines if line.startswith("|")]
    if len(table_lines) < 3:
        return [], []
    headers = [part.strip() for part in table_lines[0].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        if not line.strip():
            continue
        values = [part.strip() for part in line.strip().strip("|").split("|")]
        rows.append(dict(zip(headers, values, strict=False)))
    return headers, rows


def value_is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped == "" or "<" in stripped or ">" in stripped


def validate_required_headings(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"Missing required heading: {heading}")
    return errors


def validate_required_tables(lines: list[str]) -> list[str]:
    errors: list[str] = []
    for heading in TABLE_REQUIRED:
        section = extract_section(lines, heading)
        headers, rows = parse_table_rows(section)
        if not headers or not rows:
            errors.append(f"Missing or empty table for section: {heading}")
            continue
        if not any(
            not any(value_is_placeholder(v) for v in row.values()) for row in rows
        ):
            errors.append(f"Section table contains only placeholder rows: {heading}")
    return errors


def validate_top_metadata_placeholders(lines: list[str]) -> list[str]:
    errors: list[str] = []
    top_slice = lines[:24]
    for idx, line in enumerate(top_slice, start=1):
        if PLACEHOLDER_PATTERN.search(line):
            errors.append(
                f"Top metadata still contains placeholder at line {idx}: {line.strip()}"
            )
        if "<timestamp>" in line:
            errors.append(
                f"Top metadata still contains <timestamp> token at line {idx}: {line.strip()}"
            )
    return errors


def validate_task_table(lines: list[str]) -> list[str]:
    errors: list[str] = []
    section = extract_section(lines, "## Task Table (single source of truth)")
    _, rows = parse_table_rows(section)
    if not rows:
        return ["Task table is missing rows."]

    for row in rows:
        description = row.get("Description", "").strip()
        if value_is_placeholder(description):
            errors.append("Task row has placeholder or empty description.")
            continue

        has_anchor = bool(ANCHOR_PATTERN.search(description))
        has_command = bool(COMMAND_PATTERN.search(description))
        if not has_anchor and not has_command:
            errors.append(
                f"Task description lacks explicit file anchor or command: {description}"
            )

        if VAGUE_TASK_PATTERN.search(description) and not (has_anchor or has_command):
            errors.append(
                f"Task uses vague action without concrete execution cues: {description}"
            )

    return errors


def parse_requirement_ids(lines: list[str]) -> set[str]:
    requirement_section = extract_section(lines, "## Requirements Freeze")
    requirement_ids: set[str] = set()
    for line in requirement_section:
        match = re.match(r"^\s*-\s*(R\d+)\s*:", line)
        if match:
            requirement_ids.add(match.group(1))
    return requirement_ids


def parse_task_refs(lines: list[str]) -> set[str]:
    task_section = extract_section(lines, "## Task Table (single source of truth)")
    _, rows = parse_table_rows(task_section)
    refs: set[str] = set()
    for row in rows:
        phase = row.get("Phase #", "").strip()
        task = row.get("Task #", "").strip()
        if value_is_placeholder(phase) or value_is_placeholder(task):
            continue
        refs.add(f"P{phase}-T{task}")
    return refs


def split_csv_tokens(raw: str) -> list[str]:
    return [token for token in re.split(r"[\s,]+", raw.strip()) if token]


def format_scenario_label(scenario_id: str) -> str:
    return scenario_id or "<missing>"


def validate_test_plan_columns(headers: list[str]) -> list[str]:
    missing_columns = [
        name for name in TEST_PLAN_REQUIRED_COLUMNS if name not in headers
    ]
    if not missing_columns:
        return []
    return [
        "Test Plan table is missing required column(s): " + ", ".join(missing_columns)
    ]


def validate_test_plan_req_ids(
    scenario_label: str, req_ids_value: str, requirement_ids: set[str]
) -> list[str]:
    errors: list[str] = []
    req_ids = split_csv_tokens(req_ids_value)
    if not req_ids:
        return [f"Test Plan scenario `{scenario_label}` is missing Req IDs."]

    for req_id in req_ids:
        if not REQ_ID_PATTERN.match(req_id):
            errors.append(
                f"Test Plan scenario `{scenario_label}` has invalid Req ID token: {req_id}"
            )
            continue
        if requirement_ids and req_id not in requirement_ids:
            errors.append(
                f"Test Plan scenario `{scenario_label}` references unknown requirement ID: {req_id}"
            )
    return errors


def validate_test_plan_bdd_steps(
    scenario_label: str, given: str, when: str, then: str
) -> list[str]:
    errors: list[str] = []
    for field_name, field_value in (("Given", given), ("When", when), ("Then", then)):
        if value_is_placeholder(field_value):
            errors.append(
                f"Test Plan scenario `{scenario_label}` is missing `{field_name}`."
            )
            continue
        if len(field_value) > MAX_BDD_STEP_LENGTH:
            errors.append(
                f"Test Plan scenario `{scenario_label}` `{field_name}` exceeds {MAX_BDD_STEP_LENGTH} characters."
            )
    return errors


def validate_test_plan_evidence_command(
    scenario_label: str, evidence_cmd: str
) -> list[str]:
    if not value_is_placeholder(evidence_cmd) and COMMAND_PATTERN.search(evidence_cmd):
        return []
    return [
        f"Test Plan scenario `{scenario_label}` must include a concrete backticked Evidence Command."
    ]


def validate_test_plan_task_refs(
    scenario_label: str, task_ref_value: str, task_refs: set[str]
) -> list[str]:
    errors: list[str] = []
    task_refs_for_row = split_csv_tokens(task_ref_value)
    if not task_refs_for_row:
        return [f"Test Plan scenario `{scenario_label}` is missing Task Ref mapping."]

    for task_ref in task_refs_for_row:
        if not TASK_REF_PATTERN.match(task_ref):
            errors.append(
                f"Test Plan scenario `{scenario_label}` has invalid Task Ref format: {task_ref}"
            )
            continue
        if task_refs and task_ref not in task_refs:
            errors.append(
                f"Test Plan scenario `{scenario_label}` references unknown Task Ref: {task_ref}"
            )
    return errors


def is_smoke_p0(
    priority: str, scenario_id: str, given: str, when: str, then: str
) -> bool:
    if priority != "P0":
        return False
    row_text = " ".join((scenario_id, given, when, then)).lower()
    return "smoke" in row_text


def validate_test_plan(lines: list[str]) -> list[str]:
    errors: list[str] = []
    section = extract_section(lines, "## Test Plan")
    headers, rows = parse_table_rows(section)
    if not headers or not rows:
        return []

    errors.extend(validate_test_plan_columns(headers))
    if errors:
        return errors

    requirement_ids = parse_requirement_ids(lines)
    if not requirement_ids:
        errors.append(
            "Requirements Freeze must define requirement IDs using bullet keys like `- R1:`."
        )

    task_refs = parse_task_refs(lines)
    if not task_refs:
        errors.append(
            "Task Table must include concrete phase/task rows for Test Plan mapping."
        )

    smoke_p0_rows = 0
    for row in rows:
        scenario_id = row.get("Scenario ID", "").strip()
        scenario_label = format_scenario_label(scenario_id)
        priority = row.get("Priority", "").strip().upper()
        given = row.get("Given", "").strip()
        when = row.get("When", "").strip()
        then = row.get("Then", "").strip()
        req_ids_value = row.get("Req IDs", "").strip()

        if value_is_placeholder(scenario_id) or not SCENARIO_ID_PATTERN.match(
            scenario_id
        ):
            errors.append(
                f"Test Plan scenario must use a concrete `Scenario ID` like `S1`: {scenario_id}"
            )

        errors.extend(
            validate_test_plan_req_ids(scenario_label, req_ids_value, requirement_ids)
        )

        if priority not in TEST_PRIORITIES:
            errors.append(
                f"Test Plan scenario `{scenario_label}` has invalid Priority: {priority}"
            )

        errors.extend(validate_test_plan_bdd_steps(scenario_label, given, when, then))
        errors.extend(
            validate_test_plan_evidence_command(
                scenario_label, row.get("Evidence Command", "").strip()
            )
        )
        errors.extend(
            validate_test_plan_task_refs(
                scenario_label, row.get("Task Ref", "").strip(), task_refs
            )
        )

        if is_smoke_p0(priority, scenario_id, given, when, then):
            smoke_p0_rows += 1

    if smoke_p0_rows == 0:
        errors.append(
            "Test Plan must include at least one `P0` smoke scenario with executable evidence."
        )

    return errors


def validate_smoke_gate(lines: list[str]) -> list[str]:
    errors: list[str] = []

    success_section = extract_section(lines, "## Success Criteria")
    success_text = "\n".join(success_section).lower()
    if "smoke" not in success_text:
        errors.append(
            "Success Criteria section must include a smoke command criterion."
        )

    quality_section = extract_section(lines, "## Quality Gates")
    _, rows = parse_table_rows(quality_section)
    smoke_rows = [row for row in rows if row.get("Gate", "").strip().lower() == "smoke"]
    if not smoke_rows:
        errors.append("Quality Gates table must include a Smoke row.")
    else:
        for row in smoke_rows:
            command = row.get("Command", "").strip()
            if value_is_placeholder(command):
                errors.append(
                    "Quality Gates Smoke row must include a concrete command."
                )

    return errors


def output_report(output_path: Path, execplan: Path, errors: list[str]) -> None:
    payload = {
        "status": "pass" if not errors else "fail",
        "execplan": str(execplan),
        "errors": errors,
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    execplan = Path(args.execplan).resolve()
    text = execplan.read_text(encoding="utf-8")
    lines = text.splitlines()

    errors: list[str] = []
    errors.extend(validate_required_headings(text))
    errors.extend(validate_required_tables(lines))
    errors.extend(validate_top_metadata_placeholders(lines))
    errors.extend(validate_task_table(lines))
    errors.extend(validate_test_plan(lines))
    errors.extend(validate_smoke_gate(lines))

    output_path = (
        Path(args.output).resolve()
        if args.output
        else execplan.parent / "execplan-validation.json"
    )
    output_report(output_path=output_path, execplan=execplan, errors=errors)

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"ExecPlan validation passed: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
