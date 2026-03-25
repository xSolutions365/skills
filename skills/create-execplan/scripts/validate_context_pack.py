"""Validate Context Pack completeness for create-execplan."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_HEADINGS = (
    "## Requirement Freeze (user-confirmed)",
    "## Evidence Inventory",
    "## Verification Baseline & Strategy",
    "## Dependency Preconditions",
    "## Execution Command Catalog",
    "## Code Map (line-numbered)",
    "## Requirement to Evidence Traceability",
    "## Risk Register",
)

TABLE_REQUIRED = (
    "## Evidence Inventory",
    "## Dependency Preconditions",
    "## Execution Command Catalog",
    "## Code Map (line-numbered)",
    "## Requirement to Evidence Traceability",
    "## Risk Register",
)

MODE_TABLES = {
    "greenfield": "## Established Library Comparison (required for greenfield; optional for brownfield)",
    "brownfield": "## Existing Change Surface (required for brownfield; optional for greenfield)",
}

VERIFICATION_SCENARIOS = {
    "greenfield-setup",
    "brownfield-existing",
    "brownfield-none",
}
VERIFICATION_DECISIONS = {
    "approved-change-scoped",
    "declined-blocked",
    "n/a-existing",
}
DEPENDENCY_OPTIONAL_VALUES = {"none", "n/a", "na", "not applicable"}

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ANCHOR_PATTERN = re.compile(r".+:\d+$")
TIMESTAMP_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T.+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate create-execplan Context Pack."
    )
    parser.add_argument("--context-pack", required=True, help="Path to context-pack.md")
    parser.add_argument(
        "--project-mode",
        choices=("greenfield", "brownfield"),
        default="",
        help="Override project mode from metadata in context pack.",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Validation output JSON path. Default: <context-pack-dir>/context-pack-validation.json",
    )
    return parser.parse_args()


def heading_exists(text: str, heading: str) -> bool:
    return heading in text


def parse_project_mode(text: str, mode_override: str) -> str:
    if mode_override:
        return mode_override
    match = re.search(
        r"^- Project mode:\s*`(greenfield|brownfield)`", text, re.MULTILINE
    )
    if not match:
        raise ValueError("Missing or invalid `- Project mode: ` metadata.")
    return match.group(1)


def extract_section_table(
    lines: list[str], heading: str
) -> tuple[list[str], list[dict[str, str]]]:
    start = find_heading_index(lines, heading)
    if start < 0:
        return [], []

    section_end = len(lines)
    for idx in range(start + 1, len(lines)):
        if lines[idx].startswith("## "):
            section_end = idx
            break

    table_lines = [
        line for line in lines[start + 1 : section_end] if line.startswith("|")
    ]
    if len(table_lines) < 3:
        return [], []

    headers = parse_row(table_lines[0])
    rows = [parse_row(line) for line in table_lines[2:] if line.strip()]
    dict_rows = [dict(zip(headers, row, strict=False)) for row in rows]
    return headers, dict_rows


def parse_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def strip_code_markers(value: str) -> str:
    stripped = value.strip()
    if stripped.startswith("`") and stripped.endswith("`") and len(stripped) >= 2:
        return stripped[1:-1].strip()
    return stripped


def find_heading_index(lines: list[str], heading: str) -> int:
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            return idx
    return -1


def validate_required_headings(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if not heading_exists(text, heading):
            errors.append(f"Missing required heading: {heading}")
    return errors


def validate_requirement_confirmation(text: str) -> list[str]:
    match = re.search(r"^- Confirmed by user at:\s*(.+)$", text, re.MULTILINE)
    if not match:
        return ["Missing `Confirmed by user at` entry in Requirement Freeze."]
    timestamp = match.group(1).strip()
    if not TIMESTAMP_PATTERN.match(timestamp):
        return ["Invalid requirement confirmation timestamp format."]
    return []


def validate_required_tables(lines: list[str]) -> list[str]:
    errors: list[str] = []
    for heading in TABLE_REQUIRED:
        headers, rows = extract_section_table(lines, heading)
        if not headers or not rows:
            errors.append(f"Missing or empty table for section: {heading}")
            continue
        if not any(not row_contains_placeholder(row) for row in rows):
            errors.append(f"Section table contains only placeholder rows: {heading}")
    return errors


def row_contains_placeholder(row: dict[str, str]) -> bool:
    return any("<" in value or ">" in value for value in row.values())


def value_is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped == "" or "<" in stripped or ">" in stripped


def validate_mode_table(lines: list[str], mode: str) -> list[str]:
    errors: list[str] = []
    heading = MODE_TABLES[mode]
    headers, rows = extract_section_table(lines, heading)
    if not headers or not rows:
        return [f"Missing or empty mode-specific table: {heading}"]
    if not any(not row_contains_placeholder(row) for row in rows):
        errors.append(f"Mode-specific table contains only placeholder rows: {heading}")
    return errors


def validate_code_anchors(lines: list[str], mode: str) -> list[str]:
    errors: list[str] = []
    _, code_rows = extract_section_table(lines, "## Code Map (line-numbered)")
    errors.extend(validate_anchor_rows(code_rows, "Code Map (line-numbered)"))
    if mode == "brownfield":
        _, surface_rows = extract_section_table(
            lines,
            "## Existing Change Surface (required for brownfield; optional for greenfield)",
        )
        errors.extend(validate_anchor_rows(surface_rows, "Existing Change Surface"))
    return errors


def validate_anchor_rows(rows: list[dict[str, str]], section_name: str) -> list[str]:
    errors: list[str] = []
    for row in rows:
        anchor = strip_code_markers(row.get("File anchor", ""))
        if not ANCHOR_PATTERN.match(anchor):
            errors.append(f"Invalid file anchor in {section_name}: {anchor}")
    return errors


def validate_evidence_dates(lines: list[str]) -> list[str]:
    errors: list[str] = []
    _, rows = extract_section_table(lines, "## Evidence Inventory")
    for row in rows:
        published = row.get("Published", "").strip()
        retrieved = row.get("Retrieved", "").strip()
        if not (
            DATE_PATTERN.match(published) or published.lower().startswith("undated:")
        ):
            errors.append(f"Invalid published date in Evidence Inventory: {published}")
        if not DATE_PATTERN.match(retrieved):
            errors.append(f"Invalid retrieved date in Evidence Inventory: {retrieved}")
    return errors


def validate_verification_strategy(text: str) -> list[str]:
    scenario = parse_verification_scenario(text)
    if scenario is None:
        return [
            "Missing `Verification scenario` entry in Verification Baseline & Strategy."
        ]
    if scenario not in VERIFICATION_SCENARIOS:
        return [
            "Invalid `Verification scenario`. Expected one of: "
            + ", ".join(sorted(VERIFICATION_SCENARIOS))
        ]
    decision = parse_verification_decision(text)
    if decision is None:
        return [
            "Missing `User decision when verification missing` entry in Verification Baseline & Strategy."
        ]
    if decision not in VERIFICATION_DECISIONS:
        return [
            "Invalid `User decision when verification missing`. Expected one of: "
            + ", ".join(sorted(VERIFICATION_DECISIONS))
        ]
    return []


def parse_verification_scenario(text: str) -> str | None:
    match = re.search(
        r"^- Verification scenario:\s*`?([A-Za-z0-9\-_/ ]+)`?$",
        text,
        re.MULTILINE,
    )
    if not match:
        return None
    return match.group(1).strip().lower()


def parse_verification_decision(text: str) -> str | None:
    match = re.search(
        r"^- User decision when verification missing:\s*`?([A-Za-z0-9\-/]+)`?$",
        text,
        re.MULTILINE,
    )
    if not match:
        return None
    return match.group(1).strip().lower()


def validate_verification_mode_alignment(text: str, mode: str) -> list[str]:
    scenario = parse_verification_scenario(text)
    if scenario is None:
        return []
    if mode == "greenfield" and scenario != "greenfield-setup":
        return [
            "Verification scenario must be `greenfield-setup` when project mode is greenfield."
        ]
    if mode == "brownfield" and scenario not in {
        "brownfield-existing",
        "brownfield-none",
    }:
        return [
            "Verification scenario must be `brownfield-existing` or "
            "`brownfield-none` when project mode is brownfield."
        ]
    return []


def validate_verification_decision_alignment(text: str) -> list[str]:
    scenario = parse_verification_scenario(text)
    decision = parse_verification_decision(text)
    if scenario is None or decision is None:
        return []
    if scenario == "brownfield-existing" and decision != "n/a-existing":
        return [
            "`brownfield-existing` requires `User decision when verification missing` to be `n/a-existing`."
        ]
    if scenario == "brownfield-none" and decision != "approved-change-scoped":
        return [
            "`brownfield-none` requires `User decision when verification missing` to be "
            "`approved-change-scoped`; `declined-blocked` must remain blocked and not handoff-ready."
        ]
    if scenario == "greenfield-setup" and decision == "declined-blocked":
        return [
            "`greenfield-setup` cannot use `declined-blocked` for verification decision."
        ]
    return []


def validate_dependency_preconditions(lines: list[str]) -> list[str]:
    errors: list[str] = []
    _, rows = extract_section_table(lines, "## Dependency Preconditions")
    if not rows:
        return ["Missing or empty table for section: ## Dependency Preconditions"]

    non_placeholder_rows = 0
    for row in rows:
        dependency = row.get("Dependency", "").strip()
        if value_is_placeholder(dependency):
            continue
        non_placeholder_rows += 1
        check_cmd = row.get("Check command", "").strip()
        install_cmd = row.get("Install command", "").strip()
        source = row.get("Source", "").strip()
        if dependency.lower() in DEPENDENCY_OPTIONAL_VALUES:
            continue
        if value_is_placeholder(check_cmd):
            errors.append(
                f"Dependency Preconditions missing check command for dependency: {dependency}"
            )
        if value_is_placeholder(install_cmd):
            errors.append(
                f"Dependency Preconditions missing install command for dependency: {dependency}"
            )
        if value_is_placeholder(source):
            errors.append(
                f"Dependency Preconditions missing source for dependency: {dependency}"
            )

    if non_placeholder_rows == 0:
        errors.append("Dependency Preconditions table contains only placeholder rows.")
    return errors


def validate_smoke_command(lines: list[str]) -> list[str]:
    errors: list[str] = []
    _, rows = extract_section_table(lines, "## Execution Command Catalog")
    if not rows:
        return []
    for row in rows:
        purpose = row.get("Purpose", "").strip().lower()
        if "smoke" not in purpose:
            continue
        command = row.get("Command", "").strip()
        signal = row.get("Expected success signal", "").strip()
        if value_is_placeholder(command):
            errors.append(
                "Smoke command row in Execution Command Catalog is missing a concrete command."
            )
        if value_is_placeholder(signal):
            errors.append(
                "Smoke command row in Execution Command Catalog is missing an expected success signal."
            )
        return errors
    errors.append(
        "Execution Command Catalog must include a mandatory smoke command row."
    )
    return errors


def validate_workspace_artifact_paths(text: str) -> list[str]:
    errors: list[str] = []
    expected_paths = {
        "Intake artifact": "workspace/context-discovery.md",
        "Evidence artifact": "workspace/context-evidence.json",
        "Codemap artifact": "workspace/context-codemap.md",
        "Requirements freeze artifact": "workspace/requirements-freeze.md",
    }
    for label, suffix in expected_paths.items():
        match = re.search(
            rf"^- {re.escape(label)}:\s*`([^`]+)`$",
            text,
            re.MULTILINE,
        )
        if not match:
            errors.append(f"Missing `{label}` path in Discovery Inputs.")
            continue
        value = match.group(1).strip()
        if not value.endswith(suffix):
            errors.append(
                f"`{label}` must end with `{suffix}` to enforce workspace artifact layout."
            )
    return errors


def output_report(
    output_path: Path,
    context_pack: Path,
    mode: str,
    errors: list[str],
) -> None:
    payload = {
        "status": "pass" if not errors else "fail",
        "context_pack": str(context_pack),
        "project_mode": mode,
        "errors": errors,
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    context_pack = Path(args.context_pack).resolve()
    text = context_pack.read_text(encoding="utf-8")
    mode = parse_project_mode(text, args.project_mode)
    lines = text.splitlines()

    errors: list[str] = []
    errors.extend(validate_required_headings(text))
    errors.extend(validate_requirement_confirmation(text))
    errors.extend(validate_required_tables(lines))
    errors.extend(validate_mode_table(lines, mode))
    errors.extend(validate_code_anchors(lines, mode))
    errors.extend(validate_evidence_dates(lines))
    errors.extend(validate_verification_strategy(text))
    errors.extend(validate_verification_mode_alignment(text, mode))
    errors.extend(validate_verification_decision_alignment(text))
    errors.extend(validate_dependency_preconditions(lines))
    errors.extend(validate_smoke_command(lines))
    errors.extend(validate_workspace_artifact_paths(text))

    output_path = (
        Path(args.output).resolve()
        if args.output
        else context_pack.parent / "context-pack-validation.json"
    )
    output_report(
        output_path=output_path, context_pack=context_pack, mode=mode, errors=errors
    )

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"Context pack validation passed: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
