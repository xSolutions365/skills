"""Validate finalized ExecPlan completeness for create-execplan."""

from __future__ import annotations

import argparse
import json
import re
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
    '## Success Criteria (how to prove "done")',
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

REQUIRED_TOP_METADATA = ("- Runtime Input artifact:",)

RELATIVE_ARTIFACT_METADATA_LABELS = {
    "Artifact root",
    "Workspace root",
    "Context Pack",
    "Runtime Input artifact",
    "Requirements Freeze artifact",
    "Draft Review artifact",
}

TASK_HEADERS = [
    "Status",
    "Phase #",
    "Task #",
    "Type",
    "Req IDs",
    "Edit Targets",
    "Supporting Context Anchors",
    "Allowed Commands",
    "Verification Commands",
    "Evidence Commands",
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
TASK_LEVEL_EVIDENCE_EXEMPT_TYPES = {"Read", "Human"}
BROWNFIELD_REQUIRED_EDIT_TARGET_TYPES = {"Code"}
BROWNFIELD_REQUIRED_CONTEXT_TYPES = {"Read"}
BROWNFIELD_REQUIRED_COMMAND_TYPES = {"Action", "Test", "Gate"}

BROWNFIELD_VAGUE_TEXT_PATTERNS = (
    re.compile(
        r"\b(tbd|todo|placeholder|example only|fill in|somewhere|something|various|etc\.?)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(as needed|if needed|when needed|if appropriate|when appropriate|or similar|follow the pattern)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(relevant|canonical|appropriate|locate|identify|investigate|determine)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(done|updated|fixed|verified|complete|completed|pass|passed|success|okay|ok)\s*[.!]?\s*$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(change applied|code change applied|implementation complete|implementation done|task complete)\s*[.!]?\s*$",
        re.IGNORECASE,
    ),
)

DOC_ONLY_ACTION_PATTERN = re.compile(
    r"\b(doc|docs|documentation|readme|guide|comment|template|example)\b",
    re.IGNORECASE,
)


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


def read_context_pack_mode(execplan: Path) -> str | None:
    context_pack = execplan.parent / "context-pack.md"
    if not context_pack.exists():
        return None

    text = context_pack.read_text(encoding="utf-8")
    match = re.search(
        r"^- Project mode:\s*`(greenfield|brownfield)`",
        text,
        re.MULTILINE,
    )
    if not match:
        return None
    return match.group(1).strip().lower()


def extract_metadata_value(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped.startswith("- "):
        return None

    body = stripped[2:]
    separator = body.find(":")
    if separator == -1:
        return None

    key = body[:separator].strip()
    value = body[separator + 1 :].strip()
    value = re.sub(r"\s+\([^)]*\)\s*$", "", value).strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        value = value[1:-1].strip()
    return key, value


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

        metadata_item = extract_metadata_value(line)
        if metadata_item is None:
            continue
        key, value = metadata_item
        if key in RELATIVE_ARTIFACT_METADATA_LABELS and value.startswith("/"):
            errors.append(
                f"Top metadata `{key}` must use repo-relative in-repo paths, not absolute paths: {value}"
            )
    return errors


def validate_success_criteria(text: str) -> list[str]:
    section = read_section(text, '## Success Criteria (how to prove "done")')
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


def is_concrete_command(command: str) -> bool:
    return not is_na(command) and not is_placeholder(command)


def command_ignores_untracked_changes(command: str) -> bool:
    normalized = " ".join(command.split())
    return "git diff --name-only" in normalized and not any(
        marker in normalized
        for marker in (
            "git status --short",
            "git ls-files --others",
            "--others --exclude-standard",
        )
    )


def brownfield_vague_text_reason(value: str) -> str | None:
    text = value.strip()
    if not text:
        return "is empty"
    if is_placeholder(text):
        return "contains placeholder text"

    normalized = " ".join(text.split())
    for pattern in BROWNFIELD_VAGUE_TEXT_PATTERNS:
        if pattern.search(normalized):
            return "uses vague brownfield language"
    return None


def is_doc_or_plan_anchor(anchor: str) -> bool:
    anchor_path = anchor.rsplit(":", 1)[0]
    return "/.plan/" in anchor_path or anchor_path.startswith(".plan/") or anchor_path.endswith(
        ".md"
    )


def is_documentation_only_action(action: str) -> bool:
    return bool(DOC_ONLY_ACTION_PATTERN.search(action))


def validate_anchor_list(
    task_ref_value: str, field_name: str, anchors: list[str]
) -> list[str]:
    errors: list[str] = []
    for anchor in anchors:
        if not ANCHOR_PATTERN.fullmatch(anchor):
            errors.append(f"Task `{task_ref_value}` has invalid {field_name}: {anchor}")
    return errors


def validate_command_list(
    task_ref_value: str, field_name: str, commands: list[str]
) -> list[str]:
    errors: list[str] = []
    for command in commands:
        if is_placeholder(command):
            errors.append(
                f"Task `{task_ref_value}` {field_name} contains placeholder command text: {command}"
            )
            continue
        if command_ignores_untracked_changes(command):
            errors.append(
                f"Task `{task_ref_value}` {field_name} uses `git diff --name-only` without handling untracked files: {command}"
            )
    return errors


def validate_task_scope(
    task_ref_value: str,
    task_type: str,
    edit_targets: list[str],
    supporting_context_anchors: list[str],
    allowed_commands: list[str],
    action: str,
    expected_output: str,
    brownfield: bool,
) -> list[str]:
    errors: list[str] = []

    if task_type != "Human" and not any(
        (edit_targets, supporting_context_anchors, allowed_commands)
    ):
        errors.append(
            f"Task `{task_ref_value}` must include at least one concrete edit target, supporting context anchor, or allowed command."
        )

    if not brownfield:
        return errors

    if task_type in BROWNFIELD_REQUIRED_EDIT_TARGET_TYPES and not edit_targets:
        errors.append(
            f"Brownfield task `{task_ref_value}` of type {task_type} must include concrete `Edit Targets`."
        )

    if task_type in BROWNFIELD_REQUIRED_CONTEXT_TYPES and not supporting_context_anchors:
        errors.append(
            f"Brownfield task `{task_ref_value}` of type {task_type} must include concrete `Supporting Context Anchors`."
        )

    if task_type in BROWNFIELD_REQUIRED_COMMAND_TYPES and not allowed_commands:
        errors.append(
            f"Brownfield task `{task_ref_value}` of type {task_type} must include concrete `Allowed Commands`."
        )

    if (
        task_type == "Code"
        and edit_targets
        and all(is_doc_or_plan_anchor(anchor) for anchor in edit_targets)
        and not is_documentation_only_action(action)
    ):
        errors.append(
            f"Brownfield task `{task_ref_value}` must not use only policy/doc or `.plan` edit targets for executable code work."
        )

    for field_name, field_value in (("Action", action), ("Expected Output", expected_output)):
        reason = brownfield_vague_text_reason(field_value)
        if reason:
            errors.append(
                f"Brownfield task `{task_ref_value}` `{field_name}` {reason}: {field_value}"
            )

    return errors


def validate_task_table(
    text: str, project_mode: str | None
) -> tuple[list[str], dict[str, set[str]], dict[str, dict[str, object]]]:
    section = read_section(text, "## Task Table (single source of truth)")
    headers, rows = parse_table(section)
    errors: list[str] = []
    if headers != TASK_HEADERS:
        return (
            ["Task table columns must exactly match: " + ", ".join(TASK_HEADERS)],
            {},
            {},
        )
    if not rows:
        return (["Task table is missing rows."], {}, {})

    requirement_ids = {
        item["id"] for item in parse_requirements(read_section(text, "## Requirements Freeze"))
    }
    task_requirements: dict[str, set[str]] = {}
    task_index: dict[str, dict[str, object]] = {}
    covered_requirements: set[str] = set()
    seen_task_refs: set[str] = set()
    previous_task_ref: tuple[int, int] | None = None
    brownfield = project_mode == "brownfield"

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

        if previous_task_ref is not None and (phase_number, task_number) < previous_task_ref:
            errors.append(
                f"Task rows must be ordered by phase/task: {row_task_ref} appears before an earlier row."
            )
        previous_task_ref = (phase_number, task_number)

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

        edit_targets = split_csv_tokens(row["Edit Targets"])
        supporting_context_anchors = split_csv_tokens(row["Supporting Context Anchors"])
        allowed_commands = split_csv_tokens(row["Allowed Commands"])
        verification_commands = split_csv_tokens(row["Verification Commands"])
        evidence_commands = split_csv_tokens(row["Evidence Commands"])
        expected_output = row["Expected Output"].strip()
        action = row["Action"].strip()

        errors.extend(validate_anchor_list(row_task_ref, "edit target", edit_targets))
        errors.extend(
            validate_anchor_list(
                row_task_ref,
                "supporting context anchor",
                supporting_context_anchors,
            )
        )
        errors.extend(
            validate_command_list(row_task_ref, "`Allowed Commands`", allowed_commands)
        )
        errors.extend(
            validate_command_list(
                row_task_ref,
                "`Verification Commands`",
                verification_commands,
            )
        )
        errors.extend(
            validate_command_list(
                row_task_ref,
                "`Evidence Commands`",
                evidence_commands,
            )
        )

        if is_placeholder(expected_output):
            errors.append(f"Task `{row_task_ref}` is missing `Expected Output`.")
        if is_placeholder(action):
            errors.append(f"Task `{row_task_ref}` is missing `Action`.")

        errors.extend(
            validate_task_scope(
                task_ref_value=row_task_ref,
                task_type=task_type,
                edit_targets=edit_targets,
                supporting_context_anchors=supporting_context_anchors,
                allowed_commands=allowed_commands,
                action=action,
                expected_output=expected_output,
                brownfield=brownfield,
            )
        )

        task_index[row_task_ref] = {
            "type": task_type,
            "has_task_level_evidence": bool(
                verification_commands or evidence_commands
            ),
        }

    for requirement_id in sorted(requirement_ids - covered_requirements):
        errors.append(f"Requirement `{requirement_id}` is not covered by any task row.")

    return errors, task_requirements, task_index


def validate_test_plan(
    text: str,
    task_requirements: dict[str, set[str]],
    task_index: dict[str, dict[str, object]],
) -> list[str]:
    section = read_section(text, "## Test Plan")
    headers, rows = parse_table(section)
    errors: list[str] = []
    if headers != TEST_PLAN_HEADERS:
        return ["Test Plan columns must exactly match: " + ", ".join(TEST_PLAN_HEADERS)]
    if not rows:
        return ["Test Plan is missing rows."]

    covered_requirements: set[str] = set()
    referenced_task_refs: set[str] = set()
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
        elif command_ignores_untracked_changes(evidence_command):
            errors.append(
                f"Test Plan scenario `{scenario_id or '<missing>'}` uses `git diff --name-only` without handling untracked files: {evidence_command}"
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
            referenced_task_refs.add(row_task_ref)

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

    for row_task_ref, details in task_index.items():
        task_type = str(details["type"])
        has_task_level_evidence = bool(details["has_task_level_evidence"])
        if task_type in TASK_LEVEL_EVIDENCE_EXEMPT_TYPES:
            continue
        if has_task_level_evidence:
            continue
        if row_task_ref not in referenced_task_refs:
            errors.append(
                f"Task `{row_task_ref}` must map to executable evidence through `Verification Commands`, `Evidence Commands`, or a Test Plan scenario."
            )

    return errors


def validate_runtime_input(execplan: Path, project_mode: str | None) -> list[str]:
    runtime_input = execplan.parent / "workspace" / "execplan-runtime-input.json"
    if not runtime_input.exists():
        return [f"Missing runtime input artifact: {runtime_input}"]

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
    }
    missing = sorted(required_keys - payload.keys())
    if missing:
        errors.append(
            "Runtime input artifact is missing required keys: " + ", ".join(missing)
        )

    if payload.get("schemaVersion") != "3.0":
        errors.append("Runtime input artifact `schemaVersion` must be `3.0`.")

    for legacy_key in ("verificationScenarios", "taskPackets"):
        if legacy_key in payload:
            errors.append(
                f"Runtime input artifact must not use the legacy `{legacy_key}` key."
            )

    if not isinstance(payload.get("requirements"), list):
        errors.append("Runtime input artifact `requirements` must be a list.")
    if not isinstance(payload.get("tasks"), list):
        errors.append("Runtime input artifact `tasks` must be a list.")

    required_task_keys = {
        "taskRef",
        "status",
        "phaseNumber",
        "taskNumber",
        "type",
        "requirementIds",
        "editTargets",
        "supportingContextAnchors",
        "allowedCommands",
        "verificationCommands",
        "evidenceCommands",
        "expectedOutput",
        "action",
    }
    brownfield = project_mode == "brownfield"
    for task in payload.get("tasks", []):
        if not isinstance(task, dict):
            errors.append("Runtime input tasks must be JSON objects.")
            continue

        task_ref_value = str(task.get("taskRef", "")).strip() or "<missing>"
        missing_task_keys = sorted(required_task_keys - task.keys())
        if missing_task_keys:
            errors.append(
                f"Runtime input task `{task_ref_value}` is missing required keys: {', '.join(missing_task_keys)}"
            )

        for legacy_key in ("adrThreshold", "fileAnchors", "command"):
            if legacy_key in task:
                errors.append(
                    f"Runtime input task `{task_ref_value}` must not contain legacy field `{legacy_key}`."
                )

        task_type = str(task.get("type", "")).strip()
        edit_targets = task.get("editTargets", [])
        supporting_context_anchors = task.get("supportingContextAnchors", [])
        allowed_commands = task.get("allowedCommands", [])
        verification_commands = task.get("verificationCommands", [])
        evidence_commands = task.get("evidenceCommands", [])
        expected_output = str(task.get("expectedOutput", "")).strip()
        action = str(task.get("action", "")).strip()

        for field_name, value in (
            ("editTargets", edit_targets),
            ("supportingContextAnchors", supporting_context_anchors),
            ("allowedCommands", allowed_commands),
            ("verificationCommands", verification_commands),
            ("evidenceCommands", evidence_commands),
        ):
            if not isinstance(value, list):
                errors.append(
                    f"Runtime input task `{task_ref_value}` `{field_name}` must be a list."
                )

        edit_targets = edit_targets if isinstance(edit_targets, list) else []
        supporting_context_anchors = (
            supporting_context_anchors
            if isinstance(supporting_context_anchors, list)
            else []
        )
        allowed_commands = allowed_commands if isinstance(allowed_commands, list) else []
        verification_commands = (
            verification_commands if isinstance(verification_commands, list) else []
        )
        evidence_commands = evidence_commands if isinstance(evidence_commands, list) else []

        errors.extend(validate_anchor_list(task_ref_value, "edit target", edit_targets))
        errors.extend(
            validate_anchor_list(
                task_ref_value,
                "supporting context anchor",
                supporting_context_anchors,
            )
        )
        errors.extend(
            validate_command_list(task_ref_value, "`allowedCommands`", allowed_commands)
        )
        errors.extend(
            validate_command_list(
                task_ref_value,
                "`verificationCommands`",
                verification_commands,
            )
        )
        errors.extend(
            validate_command_list(task_ref_value, "`evidenceCommands`", evidence_commands)
        )

        if is_placeholder(expected_output):
            errors.append(
                f"Runtime input task `{task_ref_value}` is missing `expectedOutput`."
            )
        if is_placeholder(action):
            errors.append(f"Runtime input task `{task_ref_value}` is missing `action`.")

        errors.extend(
            validate_task_scope(
                task_ref_value=task_ref_value,
                task_type=task_type,
                edit_targets=edit_targets,
                supporting_context_anchors=supporting_context_anchors,
                allowed_commands=allowed_commands,
                action=action,
                expected_output=expected_output,
                brownfield=brownfield,
            )
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
    project_mode = read_context_pack_mode(execplan)

    errors: list[str] = []
    errors.extend(validate_required_headings(text))
    errors.extend(validate_forbidden_headings(text))
    errors.extend(validate_top_metadata(text))
    errors.extend(validate_success_criteria(text))
    errors.extend(validate_dependency_preconditions(text))
    task_errors, task_requirements, task_index = validate_task_table(text, project_mode)
    errors.extend(task_errors)
    errors.extend(validate_test_plan(text, task_requirements, task_index))
    errors.extend(validate_runtime_input(execplan, project_mode))

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
