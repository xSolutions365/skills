"""Render the machine-readable runtime input artifact from execplan.md."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from execplan_common import (
    normalize_status,
    parse_requirements,
    parse_table,
    read_section,
    split_csv_tokens,
    task_ref,
)

TASK_TABLE_HEADING = "## Task Table (single source of truth)"
REQUIREMENTS_HEADING = "## Requirements Freeze"

TASK_HEADERS = [
    "Status",
    "Phase #",
    "Task #",
    "Type",
    "Req IDs",
    "Edit Targets",
    "Supporting Context Anchors",
    "Commands",
    "Expected Output",
    "Action",
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


def render_repo_relative_path(project_root: Path, path: Path) -> str:
    try:
        relative_path = path.resolve().relative_to(project_root.resolve())
    except ValueError:
        return path.resolve().as_posix()
    if str(relative_path) == ".":
        return "."
    return relative_path.as_posix()


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
        tasks.append(
            {
                "taskRef": task_ref(phase_number, task_number),
                "status": normalize_status(row["Status"]),
                "phaseNumber": phase_number,
                "taskNumber": task_number,
                "type": row["Type"].strip(),
                "requirementIds": split_csv_tokens(row["Req IDs"]),
                "editTargets": split_csv_tokens(row["Edit Targets"]),
                "supportingContextAnchors": split_csv_tokens(
                    row["Supporting Context Anchors"]
                ),
                "commands": split_csv_tokens(row["Commands"]),
                "expectedOutput": row["Expected Output"].strip(),
                "action": row["Action"].strip(),
            }
        )
    return tasks


def render_runtime_input(
    execplan_path: Path, generated_at: str, source_execplan_value: str
) -> dict[str, object]:
    source = execplan_path.read_text(encoding="utf-8")
    requirements = parse_requirements(read_section(source, REQUIREMENTS_HEADING))
    tasks = parse_task_rows(source)
    generated_value = generated_at or datetime.now(UTC).isoformat().replace("+00:00", "Z")
    project_root = discover_project_root(execplan_path.parent)
    source_execplan = source_execplan_value or render_repo_relative_path(
        project_root, execplan_path
    )
    return {
        "schemaVersion": "4.0",
        "generated": True,
        "editPolicy": "do-not-edit",
        "generatedAt": generated_value,
        "sourceExecplan": source_execplan,
        "requirements": requirements,
        "tasks": tasks,
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
