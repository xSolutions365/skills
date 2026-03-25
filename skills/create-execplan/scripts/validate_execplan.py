"""Validate finalized ExecPlan completeness for create-execplan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from execplan_common import (
    ANCHOR_PATTERN,
    REQ_ID_PATTERN,
    TASK_REF_PATTERN,
    is_na,
    is_placeholder,
    lines,
    normalize_cell,
    parse_requirements,
    parse_table,
    read_section,
    split_csv_tokens,
    task_ref,
)

REQUIRED_HEADINGS = (
    "## Requirements Freeze",
    "## Success Criteria (how to prove \"done\")",
    "## Constraints & Guardrails",
    "## Dependency Preconditions",
    "## Task Table (single source of truth)",
    "## Test Plan",
    "## Idempotence & Recovery",
)

FORBIDDEN_HEADINGS = (
    "## Executor Contract",
    "## Verification Strategy",
    "## Plan Overview (phases)",
    "## Quality Gates",
    "## Artifacts & Notes",
)

REQUIRED_TOP_METADATA = (
    "- Runtime Input artifact:",
)

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

TASK_TYPES = {"Code", "Read", "Action", "Test", "Gate", "Human"}
VALID_STATUS = {"", "@", "X"}
TEST_PRIORITIES = {"P0", "P1", "P2"}
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


def read_metadata_lines(text: str) -> list[str]:
    metadata: list[str] = []
    for line in lines(text):
        if line.startswith("## "):
            break
        metadata.append(line)
    return metadata


def validate_required_headings(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"Missing required heading: {heading}")
    return errors


def validate_forbidden_headings(text: str) -> list[str]:
    errors: list[str] = []
    for heading in FORBIDDEN_HEADINGS:
        if heading in text:
            errors.append(f"Legacy heading must not appear: {heading}")
    return errors


def validate_top_metadata(text: str) -> list[str]:
    metadata_lines = read_metadata_lines(text)
    metadata_text = "\n".join(metadata_lines)
    errors: list[str] = []
    for required_line in REQUIRED_TOP_METADATA:
        if required_line not in metadata_text:
            errors.append(
                f"Top metadata is missing required artifact reference: {required_line}"
            )
    if "execplan-task-packets.json" in metadata_text:
        errors.append("Top metadata must not reference `execplan-task-packets.json`.")
    for index, line in enumerate(metadata_lines, start=1):
        if not line.strip():
            continue
        if is_placeholder(line):
            errors.append(
                f"Top metadata still contains placeholder content at line {index}: {line.strip()}"
            )
    return errors


def validate_success_criteria(text: str) -> list[str]:
    section = read_section(text, "## Success Criteria (how to prove \"done\")")
    bullet_lines = [line.strip() for line in lines(section) if line.strip().startswith("-")]
    errors: list[str] = []
    if not bullet_lines:
        return ["Success Criteria must include checklist bullets and a Non-Goals line."]
    if "smoke" not in section.lower():
        errors.append("Success Criteria must include a smoke verification criterion.")
    if not any(line.startswith("- [ ]") and not is_placeholder(line) for line in bullet_lines):
        errors.append("Success Criteria must include at least one concrete checklist item.")
    non_goals_lines = [line for line in bullet_lines if line.startswith("- Non-Goals:")]
    if not non_goals_lines:
        errors.append("Success Criteria must include a `- Non-Goals:` line.")
    elif is_placeholder(non_goals_lines[0]):
        errors.append("Success Criteria `Non-Goals` must be concrete.")
    return errors


def validate_dependency_preconditions(text: str) -> list[str]:
    headers, rows = parse_table(read_section(text, "## Dependency Preconditions"))
    if not headers or not rows:
        return ["Missing or empty table for section: ## Dependency Preconditions"]
    errors: list[str] = []
    if not any(not all(is_placeholder(value) for value in row.values()) for row in rows):
        errors.append("Dependency Preconditions table contains only placeholder rows.")
    return errors


def validate_task_table(text: str) -> tuple[list[str], dict[str, set[str]]]:
    section = read_section(text, "## Task Table (single source of truth)")
    headers, rows = parse_table(section)
    errors: list[str] = []
    if headers != TASK_HEADERS:
        return (
            ["Task table columns must exactly match: " + ", ".join(TASK_HEADERS)],
            {},
        )
    if not rows:
        return (["Task table is missing rows."], {})

    requirement_ids = {item["id"] for item in parse_requirements(read_section(text, "## Requirements Freeze"))}
    task_requirements: dict[str, set[str]] = {}
    covered_requirements: set[str] = set()
    seen_task_refs: set[str] = set()

    for row in rows:
        status = row["Status"].strip()
        if status not in VALID_STATUS:
            errors.append(f"Invalid task status value: {status}")

        try:
            phase_number = int(row["Phase #"].strip())
            task_number = int(row["Task #"].strip())
        except ValueError:
            errors.append(
                f"Task row must include numeric `Phase #` and `Task #`: {row}"
            )
            continue

        row_task_ref = task_ref(phase_number, task_number)
        if row_task_ref in seen_task_refs:
            errors.append(f"Duplicate Task Ref detected: {row_task_ref}")
        seen_task_refs.add(row_task_ref)

        task_type = row["Type"].strip()
        if task_type not in TASK_TYPES:
            errors.append(f"Task `{row_task_ref}` has invalid Type: {task_type}")

        req_ids = split_csv_tokens(row["Req IDs"])
        if not req_ids:
            errors.append(f"Task `{row_task_ref}` must include at least one Req ID.")
        for req_id in req_ids:
            if not REQ_ID_PATTERN.fullmatch(req_id):
                errors.append(f"Task `{row_task_ref}` has invalid Req ID token: {req_id}")
            elif requirement_ids and req_id not in requirement_ids:
                errors.append(
                    f"Task `{row_task_ref}` references unknown requirement ID: {req_id}"
                )
        covered_requirements.update(req_ids)
        task_requirements[row_task_ref] = set(req_ids)

        file_anchors = split_csv_tokens(row["File Anchors"])
        for anchor in file_anchors:
            if not ANCHOR_PATTERN.fullmatch(anchor):
                errors.append(f"Task `{row_task_ref}` has invalid file anchor: {anchor}")

        command = normalize_cell(row["Command"])
        has_command = not is_na(command) and not is_placeholder(command)
        if not file_anchors and not has_command:
            errors.append(
                f"Task `{row_task_ref}` must include at least one concrete file anchor or command."
            )

        if is_placeholder(row["Expected Output"]):
            errors.append(f"Task `{row_task_ref}` is missing `Expected Output`.")
        if is_placeholder(row["Action"]):
            errors.append(f"Task `{row_task_ref}` is missing `Action`.")

    for requirement_id in sorted(requirement_ids - covered_requirements):
        errors.append(
            f"Requirement `{requirement_id}` is not covered by any task row."
        )

    return errors, task_requirements


def validate_test_plan(text: str, task_requirements: dict[str, set[str]]) -> list[str]:
    section = read_section(text, "## Test Plan")
    headers, rows = parse_table(section)
    errors: list[str] = []
    if headers != TEST_PLAN_HEADERS:
        return ["Test Plan columns must exactly match: " + ", ".join(TEST_PLAN_HEADERS)]
    if not rows:
        return ["Test Plan is missing rows."]

    covered_requirements: set[str] = set()
    smoke_p0_rows = 0

    for row in rows:
        scenario_id = row["Scenario ID"].strip()
        priority = row["Priority"].strip().upper()
        given = row["Given"].strip()
        when = row["When"].strip()
        then = row["Then"].strip()
        evidence_command = normalize_cell(row["Evidence Command"])
        task_refs = split_csv_tokens(row["Task Ref"])

        if not scenario_id.startswith("S") or not scenario_id[1:].isdigit():
            errors.append(
                f"Test Plan scenario must use a concrete `Scenario ID` like `S1`: {scenario_id}"
            )
        if priority not in TEST_PRIORITIES:
            errors.append(
                f"Test Plan scenario `{scenario_id or '<missing>'}` has invalid Priority: {priority}"
            )

        for field_name, field_value in (("Given", given), ("When", when), ("Then", then)):
            if is_placeholder(field_value):
                errors.append(
                    f"Test Plan scenario `{scenario_id or '<missing>'}` is missing `{field_name}`."
                )
            elif len(field_value) > MAX_BDD_STEP_LENGTH:
                errors.append(
                    f"Test Plan scenario `{scenario_id or '<missing>'}` `{field_name}` exceeds {MAX_BDD_STEP_LENGTH} characters."
                )

        if is_na(evidence_command) or is_placeholder(evidence_command):
            errors.append(
                f"Test Plan scenario `{scenario_id or '<missing>'}` must include a concrete Evidence Command."
            )

        if not task_refs:
            errors.append(
                f"Test Plan scenario `{scenario_id or '<missing>'}` is missing Task Ref mapping."
            )
        for row_task_ref in task_refs:
            if not TASK_REF_PATTERN.fullmatch(row_task_ref):
                errors.append(
                    f"Test Plan scenario `{scenario_id or '<missing>'}` has invalid Task Ref format: {row_task_ref}"
                )
                continue
            if row_task_ref not in task_requirements:
                errors.append(
                    f"Test Plan scenario `{scenario_id or '<missing>'}` references unknown Task Ref: {row_task_ref}"
                )
                continue
            covered_requirements.update(task_requirements[row_task_ref])

        if priority == "P0" and "smoke" in " ".join((scenario_id, given, when, then)).lower():
            smoke_p0_rows += 1

    all_requirement_ids = {
        item["id"] for item in parse_requirements(read_section(text, "## Requirements Freeze"))
    }
    for requirement_id in sorted(all_requirement_ids - covered_requirements):
        errors.append(
            f"Requirement `{requirement_id}` is not covered by any Test Plan scenario through Task Ref mapping."
        )

    if smoke_p0_rows == 0:
        errors.append(
            "Test Plan must include at least one `P0` smoke scenario with executable evidence."
        )

    return errors


def validate_runtime_input(execplan: Path) -> list[str]:
    runtime_input = execplan.parent / "workspace" / "execplan-runtime-input.json"
    if not runtime_input.exists():
        return [
            f"Missing runtime input artifact: {runtime_input}"
        ]

    try:
        payload = json.loads(runtime_input.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"Runtime input artifact is not valid JSON: {exc}"]

    errors: list[str] = []
    required_keys = {
        "schemaVersion",
        "generated",
        "editPolicy",
        "generatedAt",
        "sourceExecplan",
        "requirements",
        "tasks",
        "verificationScenarios",
    }
    missing = sorted(required_keys - payload.keys())
    if missing:
        errors.append(
            "Runtime input artifact is missing required keys: " + ", ".join(missing)
        )

    if "taskPackets" in payload:
        errors.append("Runtime input artifact must not use the legacy `taskPackets` key.")

    if not isinstance(payload.get("requirements"), list):
        errors.append("Runtime input artifact `requirements` must be a list.")
    if not isinstance(payload.get("tasks"), list):
        errors.append("Runtime input artifact `tasks` must be a list.")
    if not isinstance(payload.get("verificationScenarios"), list):
        errors.append("Runtime input artifact `verificationScenarios` must be a list.")

    for task in payload.get("tasks", []):
        if "adrThreshold" in task:
            errors.append("Runtime input tasks must not contain injected `adrThreshold` data.")

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

    errors: list[str] = []
    errors.extend(validate_required_headings(text))
    errors.extend(validate_forbidden_headings(text))
    errors.extend(validate_top_metadata(text))
    errors.extend(validate_success_criteria(text))
    errors.extend(validate_dependency_preconditions(text))
    task_errors, task_requirements = validate_task_table(text)
    errors.extend(task_errors)
    errors.extend(validate_test_plan(text, task_requirements))
    errors.extend(validate_runtime_input(execplan))

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
