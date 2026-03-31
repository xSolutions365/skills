"""Validate create-execplan phase artifacts against the skeptical planning rubric."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

from execplan_common import (
    PHASE_DEFINITIONS,
    PHASE_RESULT_STATUSES,
    is_placeholder,
    lines,
    parse_table,
    read_json_file,
    read_section,
    write_json_file,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate create-execplan phase artifacts against the planning rubric."
    )
    parser.add_argument("--artifact-root", required=True, help="Path to the plan artifact root.")
    parser.add_argument(
        "--output",
        default="",
        help="Optional output JSON path for the rubric report.",
    )
    return parser.parse_args()


REQUIRED_WORKSPACE_ARTIFACTS = (
    "workspace/translation-validation.md",
    "workspace/planning-brief.md",
    "workspace/phase-manifest.json",
    "workspace/phase-result.json",
    "workspace/research-questions.md",
    "workspace/research-findings.md",
    "workspace/design-options.md",
    "workspace/structure-outline.md",
)


def missing_artifacts(artifact_root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_WORKSPACE_ARTIFACTS:
        if not (artifact_root / relative_path).exists():
            errors.append(f"Missing required intermediate artifact: {relative_path}")
    return errors


def validate_manifest_contract(artifact_root: Path) -> list[str]:
    manifest = read_json_file(artifact_root / "workspace" / "phase-manifest.json")
    errors: list[str] = []
    phase_order = manifest.get("phaseOrder")

    phases = manifest.get("phases")
    if not isinstance(phases, dict):
        return ["Phase manifest `phases` must be an object keyed by canonical phase name."]

    if phase_order != list(PHASE_DEFINITIONS.keys()):
        errors.append(
            "Phase manifest `phaseOrder` drifted from the canonical phase sequence."
        )
    for phase_name, definition in PHASE_DEFINITIONS.items():
        phase_data = phases.get(phase_name)
        if not isinstance(phase_data, dict):
            errors.append(f"Phase manifest is missing phase entry: {phase_name}")
            continue
        if phase_data.get("allowedInputArtifacts") != definition["allowed_input_artifacts"]:
            errors.append(
                f"Phase manifest `{phase_name}` allowed inputs drifted from the hard-separation contract."
            )
        if phase_data.get("expectedOutputArtifacts") != definition["expected_output_artifacts"]:
            errors.append(
                f"Phase manifest `{phase_name}` expected outputs drifted from the canonical contract."
            )
    return errors


def validate_latest_phase_result(artifact_root: Path) -> list[str]:
    payload = read_json_file(artifact_root / "workspace" / "phase-result.json")
    errors: list[str] = []
    if payload.get("status") not in PHASE_RESULT_STATUSES:
        errors.append("Latest phase result uses an invalid status.")
    if not payload.get("phase"):
        errors.append("Latest phase result must record the phase name.")
    return errors


def validate_requirements_freeze(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "requirements-freeze.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    for label in (
        "- Scope and user-visible outcomes:",
        "- Constraints and non-goals:",
        "- User-provided artifacts and starting views:",
        "- Confirmation prompt:",
        "- Confirmed by user at:",
        "- User approval response (verbatim excerpt):",
    ):
        match = re.search(rf"^{re.escape(label)}\s*(.+)$", text, re.MULTILINE)
        if not match or is_placeholder(match.group(1)):
            errors.append(f"Requirements freeze is missing concrete content for `{label}`")

    frozen_items = [
        line
        for line in lines(read_section(text, "## Frozen Requirements"))
        if line.strip().startswith("- R")
    ]
    if len(frozen_items) < 1 or any(is_placeholder(line) for line in frozen_items):
        errors.append("Requirements freeze must contain concrete frozen requirements.")
    return errors


def validate_planning_brief(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "planning-brief.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    for label in (
        "- User-visible outcome:",
        "- In-scope change surface:",
        "- Explicit non-goals:",
        "- Selected project mode (`greenfield`|`brownfield`):",
        "- Mode rationale:",
        "- Verification scenario to carry into planning:",
        "- Mandatory smoke gate command:",
        "- Online research policy carried forward:",
        "- Approval prompt:",
        "- Approved by user at:",
        "- User approval response (verbatim excerpt):",
    ):
        match = re.search(rf"^{re.escape(label)}\s*(.+)$", text, re.MULTILINE)
        if not match or is_placeholder(match.group(1)):
            errors.append(f"Planning brief is missing concrete content for `{label}`")
    return errors


def validate_translation_validation(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "translation-validation.md").read_text(
        encoding="utf-8"
    )
    headers, rows = parse_table(text)
    if not headers or not rows:
        return ["Translation validation log must contain the skeptical review table."]

    errors: list[str] = []
    required_steps = {"Step 1", "Step 2", "Step 4"}
    seen_steps: set[str] = set()
    for row in rows:
        step = row.get("Step", "").strip()
        if step not in required_steps:
            continue
        seen_steps.add(step)
        candidate = row.get("Candidate Artifact", "").strip()
        inputs = row.get("Authoritative Inputs Reviewed", "").strip()
        verdict = row.get("Verdict", "").strip()
        findings = row.get("Findings Summary", "").strip()
        resolution = row.get("Resolution Status", "").strip()
        timestamp = row.get("Timestamp", "").strip()
        if any(
            is_placeholder(value)
            for value in (candidate, inputs, verdict, findings, resolution, timestamp)
        ):
            errors.append(
                f"Translation validation row for {step} must be fully populated."
            )
            continue
        if verdict != "pass":
            errors.append(
                f"Translation validation row for {step} must be resolved to `pass` before approval."
            )
        if resolution != "resolved":
            errors.append(
                f"Translation validation row for {step} must be marked `resolved` before approval."
            )

    missing_steps = sorted(required_steps - seen_steps)
    for step in missing_steps:
        errors.append(f"Translation validation log is missing required row: {step}")
    return errors


def validate_research_findings(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "research-findings.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    for heading in ("## Facts", "## Assumptions", "## Unknowns", "## Risks"):
        section = read_section(text, heading)
        if not section:
            errors.append(f"Research findings are missing section: {heading}")
            continue
        bullets = [line.strip() for line in lines(section) if line.strip().startswith("- ")]
        if not bullets or all(is_placeholder(line) for line in bullets):
            errors.append(f"Research findings section lacks concrete content: {heading}")
    return errors


def validate_design_options(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "design-options.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    option_count = len(re.findall(r"^### Option \d+\s*$", text, re.MULTILINE))
    if option_count < 2 and "| Option |" not in text:
        errors.append("Design options must compare at least two candidate approaches.")

    selected = read_section(text, "## Selected Direction")
    if selected:
        for label in ("- Chosen option:", "- Rationale:", "- Rejected alternatives:"):
            match = re.search(rf"^{re.escape(label)}\s*(.+)$", selected, re.MULTILINE)
            if not match or is_placeholder(match.group(1)):
                errors.append(f"Design options are missing concrete content for `{label}`")
        return errors

    chosen = read_section(text, "## Chosen Direction")
    rejected = read_section(text, "## Rejected Alternatives")
    if not chosen:
        errors.append("Design options must include `## Selected Direction` or `## Chosen Direction`.")
    elif is_placeholder(chosen):
        errors.append("Design options must record a concrete chosen direction.")
    if not rejected:
        errors.append("Design options must include rejected alternatives.")
    elif is_placeholder(rejected):
        errors.append("Design options must record rejected alternatives.")
    return errors


def validate_structure_outline(artifact_root: Path) -> list[str]:
    text = (artifact_root / "workspace" / "structure-outline.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    for heading in ("## Interfaces", "## Boundaries", "## Data Flow"):
        section = read_section(text, heading)
        if not section:
            errors.append(f"Structure outline is missing section: {heading}")
            continue
        bullets = [line.strip() for line in lines(section) if line.strip().startswith("- ")]
        if not bullets or all(is_placeholder(line) for line in bullets):
            errors.append(f"Structure outline section lacks concrete content: {heading}")
    return errors


def resolve_execplan_path(artifact_root: Path) -> Path:
    return artifact_root / "execplan.md"


def validate_execplan_vertical_slices(artifact_root: Path) -> list[str]:
    text = resolve_execplan_path(artifact_root).read_text(encoding="utf-8")
    task_headers, task_rows = parse_table(read_section(text, "## Task Table (single source of truth)"))
    if not task_headers or not task_rows:
        return ["ExecPlan task table must exist before rubric validation."]

    errors: list[str] = []
    task_types = {row.get("Type", "").strip() for row in task_rows}
    if "Code" not in task_types:
        errors.append("ExecPlan must contain at least one Code task.")
    if not any(task_type in {"Test", "Gate"} for task_type in task_types):
        errors.append("ExecPlan must contain at least one Test or Gate task.")

    test_headers, test_rows = parse_table(read_section(text, "## Test Plan"))
    if not test_headers or not test_rows:
        errors.append("ExecPlan test plan must contain scenario rows.")
        return errors
    if not any(row.get("Priority", "").strip() == "P0" for row in test_rows):
        errors.append("ExecPlan test plan must include a P0 smoke scenario.")
    return errors


def validate_approval_trace(artifact_root: Path) -> list[str]:
    draft_review = (artifact_root / "workspace" / "draft-review.md").read_text(
        encoding="utf-8"
    )
    errors: list[str] = []
    for label in (
        "- Approval prompt:",
        "- Approved by user at:",
        "- User approval response (verbatim excerpt):",
    ):
        match = re.search(rf"^{re.escape(label)}\s*(.+)$", draft_review, re.MULTILINE)
        if not match or is_placeholder(match.group(1)):
            errors.append(f"Draft review is missing concrete approval evidence for `{label}`")
    return errors


def build_report(artifact_root: Path, errors: list[str]) -> dict[str, object]:
    return {
        "status": "pass" if not errors else "fail",
        "artifact_root": str(artifact_root),
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    artifact_root = Path(args.artifact_root).resolve()
    errors: list[str] = []
    errors.extend(missing_artifacts(artifact_root))

    if not errors:
        errors.extend(validate_manifest_contract(artifact_root))
        errors.extend(validate_latest_phase_result(artifact_root))
        errors.extend(validate_requirements_freeze(artifact_root))
        errors.extend(validate_translation_validation(artifact_root))
        errors.extend(validate_planning_brief(artifact_root))
        errors.extend(validate_research_findings(artifact_root))
        errors.extend(validate_design_options(artifact_root))
        errors.extend(validate_structure_outline(artifact_root))
        errors.extend(validate_execplan_vertical_slices(artifact_root))
        errors.extend(validate_approval_trace(artifact_root))

    report = build_report(artifact_root, errors)
    if args.output:
        write_json_file(Path(args.output).resolve(), report)

    if errors:
        for error in errors:
            print(error)
        return 1
    print("Plan rubric validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
