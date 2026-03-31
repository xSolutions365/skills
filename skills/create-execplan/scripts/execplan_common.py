"""Shared parsing helpers for create-execplan Python utilities."""

from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
import re
import json
import tempfile

HEADING_PATTERN = re.compile(r"^#{1,6}\s+")
PLACEHOLDER_PATTERN = re.compile(r"<[^>]+>")
REQ_ID_PATTERN = re.compile(r"^R\d+$")
TASK_REF_PATTERN = re.compile(r"^P\d+-T\d+$")
ANCHOR_PATTERN = re.compile(r"[^`\s]+:\d+$")

NA_VALUES = {"", "n/a", "na", "none", "not applicable"}
PHASE_RESULT_STATUSES = {
    "complete",
    "needs_user_input",
    "needs_approval",
    "blocked",
    "failed",
}

PHASE_DEFINITIONS: dict[str, dict[str, object]] = {
    "preflight": {
        "kind": "deterministic",
        "description": "Verify scaffolded artifacts exist before phase execution begins.",
        "allowed_input_artifacts": [
            "context-pack.md",
            "execplan.md",
            "review-checklist.md",
            "workspace/context-discovery.md",
            "workspace/context-evidence.json",
            "workspace/context-codemap.md",
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/draft-review.md",
            "workspace/research-questions.md",
            "workspace/research-findings.md",
            "workspace/design-options.md",
            "workspace/structure-outline.md",
        ],
        "expected_output_artifacts": [
            "workspace/phase-manifest.json",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "research-questions": {
        "kind": "subagent",
        "description": "Turn the frozen requirements into concrete research questions.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/context-discovery.md",
        ],
        "expected_output_artifacts": [
            "workspace/research-questions.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "research": {
        "kind": "subagent",
        "description": "Produce objective research findings from the approved questions.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/research-questions.md",
            "workspace/context-evidence.json",
            "workspace/context-codemap.md",
            "workspace/research-findings.md",
        ],
        "expected_output_artifacts": [
            "workspace/context-evidence.json",
            "workspace/context-codemap.md",
            "workspace/research-findings.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "design": {
        "kind": "subagent",
        "description": "Evaluate candidate approaches and record the chosen direction.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/research-findings.md",
            "workspace/design-options.md",
        ],
        "expected_output_artifacts": [
            "workspace/design-options.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "structure": {
        "kind": "subagent",
        "description": "Define interfaces, boundaries, and structural outline before planning.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/research-findings.md",
            "workspace/design-options.md",
            "workspace/structure-outline.md",
        ],
        "expected_output_artifacts": [
            "workspace/structure-outline.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "context-pack": {
        "kind": "subagent",
        "description": "Assemble the durable Context Pack from approved upstream artifacts.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/research-questions.md",
            "workspace/research-findings.md",
            "workspace/design-options.md",
            "workspace/structure-outline.md",
            "workspace/context-discovery.md",
            "workspace/context-evidence.json",
            "workspace/context-codemap.md",
            "context-pack.md",
        ],
        "expected_output_artifacts": [
            "context-pack.md",
            "workspace/context-evidence.json",
            "workspace/context-codemap.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "execplan-draft": {
        "kind": "subagent",
        "description": "Draft the ExecPlan from the approved context and structure outputs.",
        "allowed_input_artifacts": [
            "workspace/requirements-freeze.md",
            "workspace/planning-brief.md",
            "workspace/design-options.md",
            "workspace/structure-outline.md",
            "context-pack.md",
            "execplan.md",
            "workspace/draft-review.md",
        ],
        "expected_output_artifacts": [
            "execplan.md",
            "workspace/draft-review.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "execplan-draft-approval",
    },
    "finalization": {
        "kind": "subagent",
        "description": "Finalize the approved ExecPlan before readiness audit and handoff.",
        "allowed_input_artifacts": [
            "context-pack.md",
            "execplan.md",
            "workspace/requirements-freeze.md",
            "workspace/draft-review.md",
        ],
        "expected_output_artifacts": [
            "execplan.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "readiness-audit": {
        "kind": "deterministic",
        "description": "Run validators, refresh the derived runtime input, and enforce rubric checks.",
        "allowed_input_artifacts": [
            "context-pack.md",
            "execplan.md",
            "workspace/requirements-freeze.md",
            "workspace/draft-review.md",
            "workspace/research-questions.md",
            "workspace/research-findings.md",
            "workspace/design-options.md",
            "workspace/structure-outline.md",
        ],
        "expected_output_artifacts": [
            "context-pack-validation.json",
            "execplan-validation.json",
            "workspace/execplan-runtime-input.json",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
    "handoff-checklist": {
        "kind": "subagent",
        "description": "Complete the final checklist after readiness audit succeeds.",
        "allowed_input_artifacts": [
            "context-pack.md",
            "execplan.md",
            "review-checklist.md",
            "context-pack-validation.json",
            "execplan-validation.json",
            "workspace/requirements-freeze.md",
            "workspace/draft-review.md",
            "workspace/execplan-runtime-input.json",
        ],
        "expected_output_artifacts": [
            "review-checklist.md",
            "workspace/phase-result.json",
        ],
        "checkpoint": "",
    },
}


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
    return value.strip()


def strip_code_markers(value: str) -> str:
    stripped = value.strip()
    if stripped.startswith("`") and stripped.endswith("`") and len(stripped) >= 2:
        return stripped[1:-1].strip()
    return stripped


def parse_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    table_lines = [
        line.strip()
        for line in lines(section)
        if line.strip().startswith("|") and line.strip().endswith("|")
    ]
    if len(table_lines) < 3:
        return [], []

    headers = [normalize_cell(cell) for cell in table_lines[0][1:-1].split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[1:]:
        if re.fullmatch(r"(\|[\s:-]+)+\|", line):
            continue
        values = [normalize_cell(cell) for cell in line[1:-1].split("|")]
        while len(values) < len(headers):
            values.append("")
        rows.append(dict(zip(headers, values, strict=False)))
    return headers, rows


def is_na(value: str) -> bool:
    return strip_code_markers(value).lower() in NA_VALUES


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped == "" or bool(PLACEHOLDER_PATTERN.search(stripped))


def split_csv_tokens(raw: str) -> list[str]:
    if is_na(raw):
        return []
    tokens: list[str] = []
    for token in raw.split(","):
        normalized = strip_code_markers(token)
        if normalized and not is_na(normalized):
            tokens.append(normalized)
    return tokens


def parse_requirements(section: str) -> list[dict[str, str]]:
    requirements: list[dict[str, str]] = []
    for item in read_bullet_items(section):
        match = re.match(r"^(R\d+):\s*(.*)$", item)
        if match:
            requirements.append({"id": match.group(1), "text": match.group(2).strip()})
    return requirements


def task_ref(phase_number: int, task_number: int) -> str:
    return f"P{phase_number}-T{task_number}"


def normalize_status(raw: str) -> str:
    stripped = raw.strip()
    if stripped == "@":
        return "in_progress"
    if stripped == "X":
        return "complete"
    return "outstanding"


def utc_now_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def phase_sandbox_workdir(artifact_root: Path, phase_name: str) -> Path:
    digest = sha256(str(artifact_root.resolve()).encode("utf-8")).hexdigest()[:16]
    return Path(tempfile.gettempdir()) / "create-execplan-phases" / digest / phase_name


def build_phase_manifest(
    artifact_root: Path,
    created_at: str,
) -> dict[str, object]:
    phases: dict[str, dict[str, object]] = {}
    for phase_name, definition in PHASE_DEFINITIONS.items():
        workdir = phase_sandbox_workdir(artifact_root, phase_name)
        runner = "deterministic" if definition["kind"] == "deterministic" else "subagent"
        phases[phase_name] = {
            "kind": definition["kind"],
            "description": definition["description"],
            "status": "pending",
            "runner": runner,
            "workdir": str(workdir),
            "allowedInputArtifacts": deepcopy(definition["allowed_input_artifacts"]),
            "expectedOutputArtifacts": deepcopy(
                definition["expected_output_artifacts"]
            ),
            "checkpoint": definition["checkpoint"],
            "lastRunAt": "",
            "lastResultStatus": "",
        }

    return {
        "schemaVersion": "1.0",
        "createdAt": created_at,
        "updatedAt": created_at,
        "selectedRunner": "subagent",
        "currentPhase": "preflight",
        "phaseOrder": list(PHASE_DEFINITIONS.keys()),
        "phases": phases,
    }


def render_repo_relative_path(project_root: Path, path: Path) -> str:
    try:
        relative_path = path.resolve().relative_to(project_root.resolve())
    except ValueError:
        return path.resolve().as_posix()
    if str(relative_path) == ".":
        return "."
    return relative_path.as_posix()


def read_json_file(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json_file(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
