"""Scaffold Context Pack, living ExecPlan, and related authoring artifacts."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from execplan_common import build_phase_manifest, render_repo_relative_path, write_json_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold create-execplan artifacts.")
    parser.add_argument("--title", required=True, help="ExecPlan title")
    parser.add_argument(
        "--artifact-root",
        default="",
        help="Artifact directory relative to the project root. Default: .plan/create-execplan/<timestamp>/",
    )
    parser.add_argument(
        "--timestamp",
        default="",
        help="Optional UTC timestamp (YYYYMMDDTHHMMSSZ) for deterministic reruns.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files in artifact root.",
    )
    parser.add_argument(
        "--project-mode",
        choices=("greenfield", "brownfield"),
        default="",
        help="Optional initial project mode. If omitted, keep template placeholder.",
    )
    return parser.parse_args()


def extract_template_block(reference_path: Path) -> str:
    content = reference_path.read_text(encoding="utf-8")
    match = re.search(r"```md\n(.*?)\n```", content, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Missing markdown template block in {reference_path}")
    return match.group(1).strip() + "\n"


def remove_markdown_section(template: str, heading: str) -> str:
    pattern = re.compile(
        rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)",
        flags=re.DOTALL,
    )
    return re.sub(pattern, "\n", template)


def resolve_timestamp(raw_timestamp: str) -> str:
    if raw_timestamp:
        return raw_timestamp
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def discover_project_root(start_path: Path) -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
            cwd=start_path,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return start_path.resolve()

    git_root = result.stdout.strip()
    if not git_root:
        return start_path.resolve()
    return Path(git_root).resolve()


def resolve_artifact_root(raw_root: str, timestamp: str, project_root: Path) -> Path:
    if raw_root:
        artifact_root = Path(raw_root)
        if artifact_root.is_absolute():
            return artifact_root.resolve()
        return (project_root / artifact_root).resolve()
    return project_root / ".plan" / "create-execplan" / timestamp


def resolve_target_path(project_root: Path, working_dir: Path) -> str:
    try:
        relative_path = working_dir.resolve().relative_to(project_root)
    except ValueError:
        return working_dir.resolve().as_posix()
    if str(relative_path) == ".":
        return "."
    return relative_path.as_posix()


def ensure_writable(path: Path, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing artifact root: {path}")
    path.mkdir(parents=True, exist_ok=True)


def render_context_template(
    template: str,
    project_root: Path,
    target_path: str,
    artifact_root: Path,
    workspace_root: Path,
    date_str: str,
    project_mode: str,
) -> str:
    if project_mode == "brownfield":
        template = remove_markdown_section(
            template,
            "Established Library Comparison (required for greenfield; optional for brownfield)",
        )
    elif project_mode == "greenfield":
        template = remove_markdown_section(
            template,
            "Existing Change Surface (required for brownfield; optional for greenfield)",
        )
    repo_root_value = render_repo_relative_path(project_root, project_root)
    artifact_root_value = render_repo_relative_path(project_root, artifact_root)
    workspace_root_value = render_repo_relative_path(project_root, workspace_root)
    rendered = template
    line_replacements = {
        "# Context Pack: <short title>": "# Context Pack: Context Pack",
        "- Created: <YYYY-MM-DD>": f"- Created: {date_str}",
        "- Repo root: `<repo-relative-path>`": f"- Repo root: `{repo_root_value}`",
        "- Target path: `<path-or-.>`": f"- Target path: `{target_path}`",
        "- Artifact root: `<artifact-root>`": f"- Artifact root: `{artifact_root_value}`",
        "- Workspace root: `<workspace-root>`": f"- Workspace root: `{workspace_root_value}`",
    }
    for placeholder, replacement in line_replacements.items():
        rendered = rendered.replace(placeholder, replacement)
    if project_mode:
        rendered = rendered.replace("<greenfield|brownfield>", project_mode)
    return rendered


def render_execplan_template(
    template: str,
    title: str,
    project_root: Path,
    artifact_root: Path,
    date_str: str,
    iso_ts: str,
) -> str:
    artifact_path = render_repo_relative_path(project_root, artifact_root)
    rendered = template
    line_replacements = {
        "# ExecPlan: <short, action-oriented title>": f"# ExecPlan: {title}",
        "- Status: <Proposed|In Progress|Blocked|Complete>": "- Status: Proposed",
        "- Start: <YYYY-MM-DD> • Last Updated: <ISO8601 UTC>": (
            f"- Start: {date_str} • Last Updated: {iso_ts}"
        ),
    }
    for placeholder, replacement in line_replacements.items():
        rendered = rendered.replace(placeholder, replacement)
    return (
        rendered.replace(
            ".plan/create-execplan/<timestamp>/",
            artifact_path.rstrip("/") + "/",
        ).replace(
            ".plan/create-execplan/<timestamp>/context-pack.md",
            artifact_path.rstrip("/") + "/context-pack.md",
        )
    )


def build_context_discovery_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Context Discovery\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Clarification Rounds\n\n"
        "- Round 1:\n"
        "- Round 2:\n\n"
        "## Approved Requirements (pre-freeze draft)\n\n"
        "- R1:\n"
        "- R2:\n"
        "- R3:\n\n"
        "## Provided Artifacts + Starting Views\n\n"
        "- User-provided artifacts:\n"
        "- User-provided constraints/views:\n"
        "- Assumptions inferred from provided artifacts:\n\n"
        "## Verification Baseline Capture\n\n"
        "- Existing verification present:\n"
        "- Existing verification commands and scope:\n"
        "- If missing, did user approve adding change-scoped verification:\n\n"
        "## Online Research Permissions\n\n"
        "- Online research allowed:\n"
        "- Approved domains/APIs:\n"
        "- Recency expectation:\n"
        "- Restricted domains/sources:\n"
    )


def build_context_evidence_content(iso_ts: str) -> str:
    payload = {
        "created_at": iso_ts,
        "requirements": [],
        "sources": [],
        "notes": [],
    }
    return json.dumps(payload, indent=2) + "\n"


def build_context_codemap_content(date_str: str) -> str:
    return (
        "# Context Code Map\n\n"
        f"- Created: {date_str}\n\n"
        "| Area | File anchor | Current behavior | Planned change |\n"
        "| ---- | ----------- | ---------------- | -------------- |\n"
    )


def build_draft_review_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Draft Review\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Draft Summary\n\n"
        "- Requirements coverage summary:\n"
        "- Key context findings:\n"
        "- Key risks:\n\n"
        "## Pre-draft Clarifications & Blockers\n\n"
        "- Status (`resolved`|`none`|`blocked`):\n"
        "- Item 1:\n"
        "- Resolution:\n\n"
        "## Initial Draft Generation\n\n"
        "- Initial execplan draft generated at:\n"
        "- Draft artifacts reviewed with user at:\n\n"
        "## Feedback Rounds\n\n"
        "| Round | User feedback summary | Files amended | Resolution status | Timestamp |\n"
        "| ----- | --------------------- | ------------- | ----------------- | --------- |\n"
        "| 1 | | | | |\n\n"
        "## Clarifying Questions From Context Gathering/Research\n\n"
        "- Q1:\n"
        "- Q2:\n\n"
        "## Requirement Deltas\n\n"
        "- Added:\n"
        "- Updated:\n"
        "- Removed:\n\n"
        "## Draft Approval\n\n"
        "- Approval prompt:\n"
        "- Approved by user at:\n"
        "- User approval response (verbatim excerpt):\n"
        "- Approval note:\n"
    )


def build_requirements_freeze_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Requirements Freeze\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Captured Inputs Playback\n\n"
        "- Scope and user-visible outcomes:\n"
        "- Constraints and non-goals:\n"
        "- User-provided artifacts and starting views:\n"
        "- Assumptions to validate with user:\n\n"
        "## Frozen Requirements\n\n"
        "- R1:\n"
        "- R2:\n"
        "- R3:\n\n"
        "## Verification Decision\n\n"
        "- Existing verification present:\n"
        "- If missing, user decision (`approved-change-scoped`|`declined-blocked`|`n/a-existing`):\n"
        "- Minimum smoke gate command:\n\n"
        "## Confirmation\n\n"
        "- Confirmation prompt:\n"
        "- Confirmed by user at:\n"
        "- User approval response (verbatim excerpt):\n"
        "- Confirmation note:\n"
    )


def build_translation_validation_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Translation Validation\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "Use this log for skeptical approval-gate validation before any Step 1, Step 2, or Step 4 artifact is surfaced to the user.\n\n"
        "| Step | Candidate Artifact | Authoritative Inputs Reviewed | Verdict | Findings Summary | Resolution Status | Timestamp |\n"
        "| ---- | ------------------ | ----------------------------- | ------- | ---------------- | ----------------- | --------- |\n"
        "| Step 1 | `workspace/requirements-freeze.md` | `user request`,`supplied artifacts` |  |  |  |  |\n"
        "| Step 2 | `workspace/planning-brief.md` | `workspace/requirements-freeze.md`,`workspace/context-discovery.md` |  |  |  |  |\n"
        "| Step 4 | `execplan.md` | `workspace/planning-brief.md`,`context-pack.md`,`workspace/draft-review.md` |  |  |  |  |\n"
    )


def build_planning_brief_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Planning Brief\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Objective Summary\n\n"
        "- User-visible outcome:\n"
        "- In-scope change surface:\n"
        "- Explicit non-goals:\n\n"
        "## Source of Truth Inputs\n\n"
        "- Requirements freeze artifact: `workspace/requirements-freeze.md`\n"
        "- Context discovery artifact: `workspace/context-discovery.md`\n"
        "- Source links or seed artifacts:\n\n"
        "## Planning Decisions\n\n"
        "- Selected project mode (`greenfield`|`brownfield`):\n"
        "- Mode rationale:\n"
        "- Verification scenario to carry into planning:\n"
        "- Mandatory smoke gate command:\n"
        "- Online research policy carried forward:\n\n"
        "## Phase Guidance\n\n"
        "- Research questions must answer:\n"
        "- Research must stay within these source boundaries:\n"
        "- Design options must compare these trade-offs:\n"
        "- Structure must anchor these edit surfaces or interfaces:\n\n"
        "## Approval\n\n"
        "- Approval prompt:\n"
        "- Approved by user at:\n"
        "- User approval response (verbatim excerpt):\n"
        "- Approval note:\n"
    )


def build_research_questions_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Research Questions\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Objective Research Questions\n\n"
        "1. \n"
        "2. \n"
        "3. \n\n"
        "## Scope Guardrails\n\n"
        "- Ask only codebase or approved-source questions tied to the frozen requirements.\n"
        "- Do not encode a preferred implementation before research completes.\n"
    )


def build_research_findings_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Research Findings\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Facts\n\n"
        "- F1:\n"
        "- F2:\n\n"
        "## Assumptions\n\n"
        "- A1:\n\n"
        "## Unknowns\n\n"
        "- U1:\n\n"
        "## Risks\n\n"
        "- R1:\n"
    )


def build_design_options_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Design Options\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Candidate Approaches\n\n"
        "### Option 1\n\n"
        "- Summary:\n"
        "- Pros:\n"
        "- Cons:\n\n"
        "### Option 2\n\n"
        "- Summary:\n"
        "- Pros:\n"
        "- Cons:\n\n"
        "## Selected Direction\n\n"
        "- Chosen option:\n"
        "- Rationale:\n"
        "- Rejected alternatives:\n"
    )


def build_structure_outline_content(date_str: str, iso_ts: str) -> str:
    return (
        "# Structure Outline\n\n"
        f"- Created: {date_str}\n"
        f"- Last updated: {iso_ts}\n\n"
        "## Interfaces\n\n"
        "- Interface 1:\n\n"
        "## Boundaries\n\n"
        "- Boundary 1:\n\n"
        "## Data Flow\n\n"
        "- Flow 1:\n"
    )


def build_phase_result_content(iso_ts: str) -> dict[str, object]:
    return {
        "phase": "preflight",
        "status": "complete",
        "message": "Scaffold created the plan package and initialized phase control artifacts.",
        "inputArtifacts": [],
        "outputArtifacts": [
            "workspace/phase-manifest.json",
            "workspace/phase-result.json",
        ],
        "blockingIssues": [],
        "updatedAt": iso_ts,
    }


def main() -> int:
    args = parse_args()
    working_dir = Path.cwd()
    project_root = discover_project_root(working_dir)
    timestamp = resolve_timestamp(args.timestamp)
    now = datetime.now(UTC)
    iso_ts = now.isoformat().replace("+00:00", "Z")
    date_str = now.strftime("%Y-%m-%d")

    artifact_root = resolve_artifact_root(args.artifact_root, timestamp, project_root)
    ensure_writable(artifact_root, args.overwrite)
    workspace_root = artifact_root / "workspace"
    workspace_root.mkdir(parents=True, exist_ok=True)
    target_path = resolve_target_path(project_root, working_dir)

    skill_root = Path(__file__).resolve().parents[1]
    references_root = skill_root / "references"
    context_template = extract_template_block(
        references_root / "context-pack-template.md"
    )
    execplan_template = extract_template_block(references_root / "execplan-template.md")
    review_content = (references_root / "review-checklist-template.md").read_text(
        encoding="utf-8"
    )

    context_content = render_context_template(
        template=context_template,
        project_root=project_root,
        target_path=target_path,
        artifact_root=artifact_root,
        workspace_root=workspace_root,
        date_str=date_str,
        project_mode=args.project_mode,
    )
    execplan_content = render_execplan_template(
        template=execplan_template,
        title=args.title,
        project_root=project_root,
        artifact_root=artifact_root,
        date_str=date_str,
        iso_ts=iso_ts,
    )

    context_path = artifact_root / "context-pack.md"
    execplan_path = artifact_root / "execplan.md"
    checklist_path = artifact_root / "review-checklist.md"
    draft_review_path = workspace_root / "draft-review.md"
    discovery_path = workspace_root / "context-discovery.md"
    evidence_path = workspace_root / "context-evidence.json"
    codemap_path = workspace_root / "context-codemap.md"
    freeze_path = workspace_root / "requirements-freeze.md"
    translation_validation_path = workspace_root / "translation-validation.md"
    planning_brief_path = workspace_root / "planning-brief.md"
    research_questions_path = workspace_root / "research-questions.md"
    research_findings_path = workspace_root / "research-findings.md"
    design_options_path = workspace_root / "design-options.md"
    structure_outline_path = workspace_root / "structure-outline.md"
    phase_manifest_path = workspace_root / "phase-manifest.json"
    phase_result_path = workspace_root / "phase-result.json"
    runtime_input_path = workspace_root / "execplan-runtime-input.json"

    context_path.write_text(context_content, encoding="utf-8")
    execplan_path.write_text(execplan_content, encoding="utf-8")
    checklist_path.write_text(review_content, encoding="utf-8")
    draft_review_path.write_text(
        build_draft_review_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    discovery_path.write_text(
        build_context_discovery_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    evidence_path.write_text(
        build_context_evidence_content(iso_ts=iso_ts), encoding="utf-8"
    )
    codemap_path.write_text(
        build_context_codemap_content(date_str=date_str), encoding="utf-8"
    )
    freeze_path.write_text(
        build_requirements_freeze_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    translation_validation_path.write_text(
        build_translation_validation_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    planning_brief_path.write_text(
        build_planning_brief_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    research_questions_path.write_text(
        build_research_questions_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    research_findings_path.write_text(
        build_research_findings_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    design_options_path.write_text(
        build_design_options_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    structure_outline_path.write_text(
        build_structure_outline_content(date_str=date_str, iso_ts=iso_ts),
        encoding="utf-8",
    )
    write_json_file(
        phase_manifest_path,
        build_phase_manifest(
            artifact_root=artifact_root,
            created_at=iso_ts,
        ),
    )
    write_json_file(phase_result_path, build_phase_result_content(iso_ts=iso_ts))

    print(
        json.dumps(
            {
                "artifact_root": str(artifact_root),
                "workspace_root": str(workspace_root),
                "context_pack": str(context_path),
                "execplan": str(execplan_path),
                "review_checklist": str(checklist_path),
                "draft_review": str(draft_review_path),
                "context_discovery": str(discovery_path),
                "context_evidence": str(evidence_path),
                "context_codemap": str(codemap_path),
                "requirements_freeze": str(freeze_path),
                "translation_validation": str(translation_validation_path),
                "planning_brief": str(planning_brief_path),
                "research_questions": str(research_questions_path),
                "research_findings": str(research_findings_path),
                "design_options": str(design_options_path),
                "structure_outline": str(structure_outline_path),
                "phase_manifest": str(phase_manifest_path),
                "phase_result": str(phase_result_path),
                "planned_runtime_input": str(runtime_input_path),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
