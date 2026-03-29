"""Run one create-execplan phase with deterministic artifact handoff."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

from execplan_common import (
    PHASE_DEFINITIONS,
    PHASE_RESULT_STATUSES,
    build_phase_manifest,
    read_json_file,
    render_repo_relative_path,
    utc_now_iso,
    write_json_file,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a create-execplan phase.")
    parser.add_argument("--phase", required=True, choices=tuple(PHASE_DEFINITIONS.keys()))
    parser.add_argument("--artifact-root", required=True, help="Path to the plan artifact root.")
    parser.add_argument(
        "--runner",
        default="codex",
        choices=("codex",),
        help="Runner to use for codex-backed phases.",
    )
    parser.add_argument(
        "--codex-bin",
        default="",
        help="Optional Codex CLI override used by the phase wrapper.",
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


def required_scaffold_artifacts() -> list[str]:
    return [
        "context-pack.md",
        "execplan.md",
        "review-checklist.md",
        "workspace/context-discovery.md",
        "workspace/context-evidence.json",
        "workspace/context-codemap.md",
        "workspace/requirements-freeze.md",
        "workspace/draft-review.md",
        "workspace/research-questions.md",
        "workspace/research-findings.md",
        "workspace/design-options.md",
        "workspace/structure-outline.md",
        "workspace/phase-manifest.json",
        "workspace/phase-result.json",
    ]


def ensure_manifest(artifact_root: Path, runner: str) -> Path:
    manifest_path = artifact_root / "workspace" / "phase-manifest.json"
    if manifest_path.exists():
        return manifest_path
    write_json_file(
        manifest_path,
        build_phase_manifest(
            artifact_root=artifact_root,
            runner=runner,
            created_at=utc_now_iso(),
        ),
    )
    return manifest_path


def validate_phase_manifest(manifest: dict[str, object], phase_name: str) -> list[str]:
    errors: list[str] = []
    phases = manifest.get("phases")
    if not isinstance(phases, dict):
        return ["Phase manifest `phases` must be an object keyed by phase name."]

    phase_data = phases.get(phase_name)
    if not isinstance(phase_data, dict):
        return [f"Phase manifest is missing phase entry: {phase_name}"]

    definition = PHASE_DEFINITIONS[phase_name]
    for key, expected in (
        ("allowedInputArtifacts", definition["allowed_input_artifacts"]),
        ("expectedOutputArtifacts", definition["expected_output_artifacts"]),
    ):
        actual = phase_data.get(key)
        if actual != expected:
            errors.append(
                f"Phase manifest `{phase_name}` `{key}` drifted from the canonical contract."
            )

    expected_runner = "deterministic" if definition["kind"] == "deterministic" else "codex"
    if phase_data.get("runner") != expected_runner:
        errors.append(f"Phase manifest `{phase_name}` runner must be `{expected_runner}`.")
    return errors


def required_inputs_exist(artifact_root: Path, phase_name: str) -> list[str]:
    errors: list[str] = []
    for relative_path in PHASE_DEFINITIONS[phase_name]["allowed_input_artifacts"]:
        artifact_path = artifact_root / str(relative_path)
        if not artifact_path.exists():
            errors.append(
                f"Phase `{phase_name}` is missing required input artifact: {relative_path}"
            )
    return errors


def phase_workdir(artifact_root: Path, manifest: dict[str, object], phase_name: str) -> Path:
    phase_data = manifest["phases"][phase_name]
    workdir_value = str(phase_data["workdir"])
    workdir_path = Path(workdir_value)
    if workdir_path.is_absolute():
        return workdir_path
    return (artifact_root / workdir_path).resolve()


def stage_phase_workspace(artifact_root: Path, workdir: Path, phase_name: str) -> None:
    if workdir.exists():
        shutil.rmtree(workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    stage_paths = set(PHASE_DEFINITIONS[phase_name]["allowed_input_artifacts"]) | {
        path
        for path in PHASE_DEFINITIONS[phase_name]["expected_output_artifacts"]
        if path != "workspace/phase-result.json"
    }
    for relative_path in sorted(stage_paths):
        source = artifact_root / str(relative_path)
        destination = workdir / str(relative_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.exists():
            shutil.copy2(source, destination)


def build_phase_schema() -> dict[str, object]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "phase": {"type": "string"},
            "status": {
                "type": "string",
                "enum": sorted(PHASE_RESULT_STATUSES),
            },
            "message": {"type": "string"},
            "inputArtifacts": {"type": "array", "items": {"type": "string"}},
            "outputArtifacts": {"type": "array", "items": {"type": "string"}},
            "blockingIssues": {"type": "array", "items": {"type": "string"}},
        },
        "required": [
            "phase",
            "status",
            "message",
            "inputArtifacts",
            "outputArtifacts",
        ],
    }


def build_phase_prompt(phase_name: str) -> str:
    definition = PHASE_DEFINITIONS[phase_name]
    allowed_inputs = "\n".join(
        f"- {path}" for path in definition["allowed_input_artifacts"]
    )
    expected_outputs = "\n".join(
        f"- {path}"
        for path in definition["expected_output_artifacts"]
        if path != "workspace/phase-result.json"
    )
    checkpoint = str(definition["checkpoint"]).strip() or "none"
    return f"""You are executing the create-execplan `{phase_name}` phase.

Phase purpose: {definition["description"]}
Current working directory contains only the staged artifacts for this phase.

Read-only/allowed phase inputs:
{allowed_inputs}

Files you may update for this phase:
{expected_outputs}

Hard rules:
- do not rely on any prior conversation or external memory
- do not read or write files outside the current working directory
- do not invent new requirements
- return only a JSON object matching the provided schema

Checkpoint for this phase: {checkpoint}
If the phase reaches an approval gate, use `needs_approval`.
If more user clarification is required before valid output exists, use `needs_user_input`.
If the phase is blocked by inconsistent artifacts or missing evidence, use `blocked`.
Otherwise use `complete`.
"""


def invoke_codex_phase(
    artifact_root: Path,
    workdir: Path,
    phase_name: str,
    codex_bin: str,
) -> dict[str, object]:
    control_dir = workdir / ".codex-phase"
    control_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = control_dir / "prompt.txt"
    schema_path = control_dir / "schema.json"
    last_message_path = control_dir / "last-message.json"
    stdout_path = control_dir / "stdout.jsonl"
    stderr_path = control_dir / "stderr.log"

    prompt_path.write_text(build_phase_prompt(phase_name), encoding="utf-8")
    schema_path.write_text(json.dumps(build_phase_schema(), indent=2) + "\n", encoding="utf-8")

    wrapper = Path(__file__).resolve().parent / "run_codex_phase.sh"
    command = [
        str(wrapper),
        "--workdir",
        str(workdir),
        "--prompt-file",
        str(prompt_path),
        "--schema-file",
        str(schema_path),
        "--result-file",
        str(last_message_path),
        "--stdout-file",
        str(stdout_path),
        "--stderr-file",
        str(stderr_path),
    ]
    if codex_bin:
        command.extend(["--codex-bin", codex_bin])

    subprocess.run(command, check=True, cwd=artifact_root)
    payload = json.loads(last_message_path.read_text(encoding="utf-8"))
    if payload.get("phase") != phase_name:
        raise ValueError(
            f"Runner returned mismatched phase `{payload.get('phase')}` for `{phase_name}`."
        )
    if payload.get("status") not in PHASE_RESULT_STATUSES:
        raise ValueError(f"Runner returned invalid phase status: {payload.get('status')}")
    return payload


def sync_phase_outputs(artifact_root: Path, workdir: Path, phase_name: str) -> None:
    for relative_path in PHASE_DEFINITIONS[phase_name]["expected_output_artifacts"]:
        if relative_path == "workspace/phase-result.json":
            continue
        staged = workdir / str(relative_path)
        destination = artifact_root / str(relative_path)
        if staged.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(staged, destination)


def resolve_python_cmd() -> str:
    resolver = Path(__file__).resolve().parent / "resolve_python.sh"
    result = subprocess.run(
        [str(resolver)],
        check=True,
        capture_output=True,
        text=True,
        cwd=resolver.parent,
    )
    return result.stdout.strip()


def run_readiness_audit(artifact_root: Path) -> dict[str, object]:
    python_cmd = resolve_python_cmd()
    script_root = Path(__file__).resolve().parent
    context_pack = artifact_root / "context-pack.md"
    execplan = artifact_root / "execplan.md"
    context_output = artifact_root / "context-pack-validation.json"
    execplan_output = artifact_root / "execplan-validation.json"
    runtime_output = artifact_root / "workspace" / "execplan-runtime-input.json"
    rubric_output = (
        artifact_root
        / "workspace"
        / "phases"
        / "readiness-audit"
        / "plan-rubric-validation.json"
    )
    project_root = discover_project_root(artifact_root)
    source_execplan_value = render_repo_relative_path(project_root, execplan)

    subprocess.run(
        [
            python_cmd,
            str(script_root / "validate_context_pack.py"),
            "--context-pack",
            str(context_pack),
            "--output",
            str(context_output),
        ],
        check=True,
        cwd=artifact_root,
    )
    subprocess.run(
        [
            python_cmd,
            str(script_root / "validate_execplan.py"),
            "--execplan",
            str(execplan),
            "--output",
            str(execplan_output),
        ],
        check=True,
        cwd=artifact_root,
    )
    subprocess.run(
        [
            python_cmd,
            str(script_root / "render_execplan_runtime_input.py"),
            "--execplan",
            str(execplan),
            "--output",
            str(runtime_output),
            "--generated-at",
            utc_now_iso(),
            "--source-execplan-value",
            source_execplan_value,
        ],
        check=True,
        cwd=artifact_root,
    )
    subprocess.run(
        [
            python_cmd,
            str(script_root / "validate_plan_rubric.py"),
            "--artifact-root",
            str(artifact_root),
            "--output",
            str(rubric_output),
        ],
        check=True,
        cwd=artifact_root,
    )
    return {
        "phase": "readiness-audit",
        "status": "complete",
        "message": "Readiness audit completed and validators passed.",
        "inputArtifacts": PHASE_DEFINITIONS["readiness-audit"]["allowed_input_artifacts"],
        "outputArtifacts": PHASE_DEFINITIONS["readiness-audit"]["expected_output_artifacts"],
        "blockingIssues": [],
    }


def run_preflight(artifact_root: Path) -> dict[str, object]:
    missing = [
        path
        for path in required_scaffold_artifacts()
        if not (artifact_root / path).exists()
    ]
    if missing:
        return {
            "phase": "preflight",
            "status": "failed",
            "message": "Scaffolded artifacts are incomplete.",
            "inputArtifacts": [],
            "outputArtifacts": ["workspace/phase-manifest.json", "workspace/phase-result.json"],
            "blockingIssues": missing,
        }
    return {
        "phase": "preflight",
        "status": "complete",
        "message": "Preflight confirmed the scaffolded plan package is ready.",
        "inputArtifacts": [],
        "outputArtifacts": ["workspace/phase-manifest.json", "workspace/phase-result.json"],
        "blockingIssues": [],
    }


def next_phase_name(current_phase: str) -> str:
    phase_names = list(PHASE_DEFINITIONS.keys())
    index = phase_names.index(current_phase)
    if index + 1 >= len(phase_names):
        return current_phase
    return phase_names[index + 1]


def persist_phase_result(
    artifact_root: Path,
    manifest_path: Path,
    phase_name: str,
    payload: dict[str, object],
) -> None:
    updated_at = utc_now_iso()
    normalized = {
        "phase": phase_name,
        "status": payload["status"],
        "message": payload["message"],
        "inputArtifacts": list(payload.get("inputArtifacts", [])),
        "outputArtifacts": list(payload.get("outputArtifacts", [])),
        "blockingIssues": list(payload.get("blockingIssues", [])),
        "updatedAt": updated_at,
    }
    phase_result_path = artifact_root / "workspace" / "phase-result.json"
    write_json_file(phase_result_path, normalized)

    manifest = read_json_file(manifest_path)
    manifest["updatedAt"] = updated_at
    manifest["currentPhase"] = (
        next_phase_name(phase_name) if payload["status"] == "complete" else phase_name
    )
    phase_state = manifest["phases"][phase_name]
    phase_state["status"] = payload["status"]
    phase_state["lastRunAt"] = updated_at
    phase_state["lastResultStatus"] = payload["status"]
    write_json_file(manifest_path, manifest)


def main() -> int:
    args = parse_args()
    artifact_root = Path(args.artifact_root).resolve()
    manifest_path = ensure_manifest(artifact_root, runner=args.runner)
    manifest = read_json_file(manifest_path)

    errors = validate_phase_manifest(manifest, args.phase)
    if args.phase != "preflight":
        errors.extend(required_inputs_exist(artifact_root, args.phase))
    if errors:
        payload = {
            "phase": args.phase,
            "status": "failed",
            "message": "Phase contract validation failed before execution.",
            "inputArtifacts": list(PHASE_DEFINITIONS[args.phase]["allowed_input_artifacts"]),
            "outputArtifacts": ["workspace/phase-result.json"],
            "blockingIssues": errors,
        }
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        for error in errors:
            print(error)
        return 1

    try:
        if args.phase == "preflight":
            payload = run_preflight(artifact_root)
        elif args.phase == "readiness-audit":
            payload = run_readiness_audit(artifact_root)
        else:
            workdir = phase_workdir(artifact_root, manifest, args.phase)
            stage_phase_workspace(artifact_root, workdir, args.phase)
            payload = invoke_codex_phase(
                artifact_root=artifact_root,
                workdir=workdir,
                phase_name=args.phase,
                codex_bin=args.codex_bin,
            )
            sync_phase_outputs(artifact_root, workdir, args.phase)
    except subprocess.CalledProcessError as exc:
        payload = {
            "phase": args.phase,
            "status": "failed",
            "message": "Phase execution failed.",
            "inputArtifacts": list(PHASE_DEFINITIONS[args.phase]["allowed_input_artifacts"]),
            "outputArtifacts": ["workspace/phase-result.json"],
            "blockingIssues": [f"Command failed with exit code {exc.returncode}."],
        }
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        return exc.returncode or 1
    except (json.JSONDecodeError, ValueError) as exc:
        payload = {
            "phase": args.phase,
            "status": "failed",
            "message": "Phase runner returned an invalid result payload.",
            "inputArtifacts": list(PHASE_DEFINITIONS[args.phase]["allowed_input_artifacts"]),
            "outputArtifacts": ["workspace/phase-result.json"],
            "blockingIssues": [str(exc)],
        }
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        return 1

    persist_phase_result(artifact_root, manifest_path, args.phase, payload)
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
