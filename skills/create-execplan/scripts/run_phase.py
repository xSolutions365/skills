"""Prepare and apply create-execplan phases with staged worker packets."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from hashlib import sha256
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

CHECKPOINT_STATUSES = {"needs_approval", "needs_user_input"}
RESULT_REQUIRED_KEYS = {
    "phase",
    "status",
    "message",
    "inputArtifacts",
    "outputArtifacts",
    "blockingIssues",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare or apply a create-execplan phase.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command_name in ("prepare", "apply"):
        command = subparsers.add_parser(command_name)
        command.add_argument("--phase", required=True, choices=tuple(PHASE_DEFINITIONS.keys()))
        command.add_argument(
            "--artifact-root",
            required=True,
            help="Path to the plan artifact root.",
        )

    apply_command = subparsers.choices["apply"]
    apply_command.add_argument(
        "--result-file",
        default="",
        help="Optional phase worker result JSON path. Defaults to the canonical control artifact.",
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
        "workspace/translation-validation.md",
        "workspace/planning-brief.md",
        "workspace/draft-review.md",
        "workspace/research-questions.md",
        "workspace/research-findings.md",
        "workspace/design-options.md",
        "workspace/structure-outline.md",
        "workspace/phase-manifest.json",
        "workspace/phase-result.json",
    ]


def ensure_manifest(artifact_root: Path) -> Path:
    manifest_path = artifact_root / "workspace" / "phase-manifest.json"
    if manifest_path.exists():
        return manifest_path
    write_json_file(
        manifest_path,
        build_phase_manifest(
            artifact_root=artifact_root,
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

    expected_runner = "deterministic" if definition["kind"] == "deterministic" else "subagent"
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


def phase_control_dir(artifact_root: Path, phase_name: str) -> Path:
    return artifact_root / "workspace" / "phases" / phase_name


def worker_input_path(control_dir: Path) -> Path:
    return control_dir / "phase-worker-input.json"


def worker_result_path(control_dir: Path) -> Path:
    return control_dir / "phase-worker-result.json"


def stage_paths_for_phase(phase_name: str) -> set[str]:
    return set(PHASE_DEFINITIONS[phase_name]["allowed_input_artifacts"]) | {
        path
        for path in PHASE_DEFINITIONS[phase_name]["expected_output_artifacts"]
        if path != "workspace/phase-result.json"
    }


def writable_paths_for_phase(phase_name: str) -> set[str]:
    return {
        path
        for path in PHASE_DEFINITIONS[phase_name]["expected_output_artifacts"]
        if path != "workspace/phase-result.json"
    }


def stage_phase_workspace(artifact_root: Path, workdir: Path, phase_name: str) -> None:
    if workdir.exists():
        shutil.rmtree(workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    for relative_path in sorted(stage_paths_for_phase(phase_name)):
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
        "required": sorted(RESULT_REQUIRED_KEYS),
    }


def build_phase_prompt(phase_name: str) -> str:
    definition = PHASE_DEFINITIONS[phase_name]
    allowed_inputs = "\n".join(
        f"- {path}" for path in definition["allowed_input_artifacts"]
    )
    writable_outputs = "\n".join(
        f"- {path}"
        for path in definition["expected_output_artifacts"]
        if path != "workspace/phase-result.json"
    )
    checkpoint = str(definition["checkpoint"]).strip() or "none"
    return f"""You are the isolated planning worker for phase `{phase_name}` in the `create-execplan` workflow.

Phase purpose: {definition["description"]}
The parent orchestrator already staged the only files you may inspect into the current working directory.

Allowed phase inputs:
{allowed_inputs}

Files you may update:
{writable_outputs}

Hard rules:
- treat this as a fresh context with no prior conversation or memory
- read and write only inside the current working directory
- do not inspect the repo root, git history, ancestor directories, or external files
- do not invent new requirements or widen scope
- do not load or invoke skills
- do not ask the user questions directly
- do not use agent-management tools (`spawn_agent`, `send_input`, `wait_agent`, `resume_agent`, `close_agent`)
- do not delegate to other agents or subprocess workers
- update the required phase artifacts before you return a checkpoint status
- if approval or clarification is needed, return the matching status and let the parent orchestrator handle the conversation
- return only one JSON object that matches the provided schema

Checkpoint for this phase: {checkpoint}
Use `needs_approval` when the phase reaches an approval gate.
Use `needs_user_input` when the staged evidence is insufficient and the parent must clarify something.
Use `blocked` for inconsistent or broken artifacts.
Use `complete` otherwise.
"""


def hash_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(65536)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def snapshot_workdir(workdir: Path) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for path in sorted(workdir.rglob("*")):
        if path.is_file():
            snapshot[path.relative_to(workdir).as_posix()] = hash_file(path)
    return snapshot


def build_phase_worker_input(
    artifact_root: Path,
    workdir: Path,
    control_dir: Path,
    phase_name: str,
) -> dict[str, object]:
    definition = PHASE_DEFINITIONS[phase_name]
    staged_artifacts = sorted(stage_paths_for_phase(phase_name))
    writable_artifacts = sorted(writable_paths_for_phase(phase_name))
    read_only_artifacts = sorted(set(staged_artifacts) - set(writable_artifacts))
    return {
        "schemaVersion": "1.0",
        "phase": phase_name,
        "runner": "subagent",
        "artifactRoot": str(artifact_root),
        "controlDir": str(control_dir),
        "phaseWorkdir": str(workdir),
        "allowedInputArtifacts": list(definition["allowed_input_artifacts"]),
        "expectedOutputArtifacts": list(definition["expected_output_artifacts"]),
        "writableArtifacts": writable_artifacts,
        "readOnlyArtifacts": read_only_artifacts,
        "checkpoint": definition["checkpoint"],
        "workerPrompt": build_phase_prompt(phase_name),
        "resultSchema": build_phase_schema(),
        "stagedArtifacts": staged_artifacts,
        "stagedSnapshot": snapshot_workdir(workdir),
    }


def ensure_string_list(name: str, payload: object) -> list[str]:
    if not isinstance(payload, list) or any(not isinstance(item, str) for item in payload):
        raise ValueError(f"Phase result `{name}` must be an array of strings.")
    return list(payload)


def normalize_result_payload(phase_name: str, raw_payload: dict[str, object]) -> dict[str, object]:
    if set(raw_payload.keys()) != RESULT_REQUIRED_KEYS:
        missing = sorted(RESULT_REQUIRED_KEYS - set(raw_payload.keys()))
        extra = sorted(set(raw_payload.keys()) - RESULT_REQUIRED_KEYS)
        details: list[str] = []
        if missing:
            details.append(f"missing keys: {', '.join(missing)}")
        if extra:
            details.append(f"unexpected keys: {', '.join(extra)}")
        raise ValueError("Phase result payload shape is invalid (" + "; ".join(details) + ").")

    phase_value = raw_payload["phase"]
    status_value = raw_payload["status"]
    message_value = raw_payload["message"]
    if not isinstance(phase_value, str) or phase_value != phase_name:
        raise ValueError(
            f"Phase result must record phase `{phase_name}`, got `{phase_value}`."
        )
    if not isinstance(status_value, str) or status_value not in PHASE_RESULT_STATUSES:
        raise ValueError(f"Phase result uses invalid status `{status_value}`.")
    if not isinstance(message_value, str) or not message_value.strip():
        raise ValueError("Phase result `message` must be a non-empty string.")

    input_artifacts = ensure_string_list("inputArtifacts", raw_payload["inputArtifacts"])
    output_artifacts = ensure_string_list("outputArtifacts", raw_payload["outputArtifacts"])
    blocking_issues = ensure_string_list("blockingIssues", raw_payload["blockingIssues"])
    if input_artifacts != list(PHASE_DEFINITIONS[phase_name]["allowed_input_artifacts"]):
        raise ValueError("Phase result `inputArtifacts` drifted from the manifest contract.")
    if output_artifacts != list(PHASE_DEFINITIONS[phase_name]["expected_output_artifacts"]):
        raise ValueError("Phase result `outputArtifacts` drifted from the manifest contract.")

    return {
        "phase": phase_value,
        "status": status_value,
        "message": message_value,
        "inputArtifacts": input_artifacts,
        "outputArtifacts": output_artifacts,
        "blockingIssues": blocking_issues,
    }


def sync_phase_outputs(artifact_root: Path, workdir: Path, phase_name: str) -> None:
    for relative_path in writable_paths_for_phase(phase_name):
        staged = workdir / relative_path
        destination = artifact_root / relative_path
        if staged.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(staged, destination)


def validate_subagent_artifacts(
    phase_name: str,
    workdir: Path,
    worker_input: dict[str, object],
    payload: dict[str, object],
) -> None:
    allowed_control_artifacts = {"phase-worker-input.json", "phase-worker-result.json"}
    staged_artifacts = set(ensure_string_list("stagedArtifacts", worker_input["stagedArtifacts"]))
    writable_artifacts = set(ensure_string_list("writableArtifacts", worker_input["writableArtifacts"]))
    read_only_artifacts = set(ensure_string_list("readOnlyArtifacts", worker_input["readOnlyArtifacts"]))
    staged_snapshot = worker_input.get("stagedSnapshot")
    if not isinstance(staged_snapshot, dict) or any(
        not isinstance(key, str) or not isinstance(value, str)
        for key, value in staged_snapshot.items()
    ):
        raise ValueError("Phase worker input `stagedSnapshot` is invalid.")

    current_snapshot = snapshot_workdir(workdir)
    current_paths = set(current_snapshot.keys())
    unexpected_paths = sorted(
        path
        for path in (current_paths - staged_artifacts)
        if path not in allowed_control_artifacts
    )
    if unexpected_paths:
        raise ValueError(
            "Phase workdir contains unexpected files outside the allowlist: "
            + ", ".join(unexpected_paths)
        )

    missing_outputs = sorted(writable_artifacts - current_paths)
    if missing_outputs:
        raise ValueError(
            "Phase workdir is missing required output artifacts: " + ", ".join(missing_outputs)
        )

    mutated_read_only = sorted(
        path
        for path in read_only_artifacts
        if current_snapshot.get(path) != staged_snapshot.get(path)
    )
    if mutated_read_only:
        raise ValueError(
            "Phase modified read-only staged artifacts: " + ", ".join(mutated_read_only)
        )

    if payload["status"] in CHECKPOINT_STATUSES:
        changed_outputs = sorted(
            path
            for path in writable_artifacts
            if current_snapshot.get(path) != staged_snapshot.get(path)
        )
        if not changed_outputs:
            raise ValueError(
                "Checkpoint statuses require draft artifact updates before returning control."
            )


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
        "inputArtifacts": list(PHASE_DEFINITIONS["readiness-audit"]["allowed_input_artifacts"]),
        "outputArtifacts": list(PHASE_DEFINITIONS["readiness-audit"]["expected_output_artifacts"]),
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
            "inputArtifacts": list(PHASE_DEFINITIONS["preflight"]["allowed_input_artifacts"]),
            "outputArtifacts": list(PHASE_DEFINITIONS["preflight"]["expected_output_artifacts"]),
            "blockingIssues": missing,
        }
    return {
        "phase": "preflight",
        "status": "complete",
        "message": "Preflight confirmed the scaffolded plan package is ready.",
        "inputArtifacts": list(PHASE_DEFINITIONS["preflight"]["allowed_input_artifacts"]),
        "outputArtifacts": list(PHASE_DEFINITIONS["preflight"]["expected_output_artifacts"]),
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


def build_failure_payload(phase_name: str, message: str, blocking_issues: list[str]) -> dict[str, object]:
    return {
        "phase": phase_name,
        "status": "failed",
        "message": message,
        "inputArtifacts": list(PHASE_DEFINITIONS[phase_name]["allowed_input_artifacts"]),
        "outputArtifacts": ["workspace/phase-result.json"],
        "blockingIssues": blocking_issues,
    }


def prepare_phase(artifact_root: Path, manifest: dict[str, object], phase_name: str) -> dict[str, object]:
    control_dir = phase_control_dir(artifact_root, phase_name)
    control_dir.mkdir(parents=True, exist_ok=True)
    result_path = worker_result_path(control_dir)
    if result_path.exists():
        result_path.unlink()

    if PHASE_DEFINITIONS[phase_name]["kind"] == "deterministic":
        if phase_name == "preflight":
            payload = run_preflight(artifact_root)
        elif phase_name == "readiness-audit":
            payload = run_readiness_audit(artifact_root)
        else:
            raise ValueError(f"Unsupported deterministic phase `{phase_name}`.")
        write_json_file(result_path, payload)
        return {
            "phase": phase_name,
            "runner": "deterministic",
            "controlDir": str(control_dir),
            "resultFile": str(result_path),
            "message": "Deterministic phase prepared and result captured.",
        }

    workdir = phase_workdir(artifact_root, manifest, phase_name)
    stage_phase_workspace(artifact_root, workdir, phase_name)
    payload = build_phase_worker_input(
        artifact_root=artifact_root,
        workdir=workdir,
        control_dir=control_dir,
        phase_name=phase_name,
    )
    write_json_file(worker_input_path(control_dir), payload)
    return {
        "phase": phase_name,
        "runner": "subagent",
        "controlDir": str(control_dir),
        "phaseWorkdir": str(workdir),
        "workerInputFile": str(worker_input_path(control_dir)),
        "resultFile": str(result_path),
        "message": "Phase worker packet prepared.",
    }


def apply_phase(
    artifact_root: Path,
    manifest_path: Path,
    manifest: dict[str, object],
    phase_name: str,
    result_file_arg: str,
) -> tuple[dict[str, object], int]:
    control_dir = phase_control_dir(artifact_root, phase_name)
    canonical_result_path = worker_result_path(control_dir)
    if result_file_arg:
        result_path = Path(result_file_arg).resolve()
    else:
        result_path = canonical_result_path
    if not result_path.exists():
        raise ValueError(f"Phase worker result file is missing: {result_path}")

    raw_payload = json.loads(result_path.read_text(encoding="utf-8"))
    if not isinstance(raw_payload, dict):
        raise ValueError("Phase worker result payload must be a JSON object.")
    payload = normalize_result_payload(phase_name, raw_payload)

    if result_path != canonical_result_path:
        canonical_result_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(result_path, canonical_result_path)

    if PHASE_DEFINITIONS[phase_name]["kind"] == "subagent":
        prepared_input = read_json_file(worker_input_path(control_dir))
        validate_subagent_artifacts(
            phase_name=phase_name,
            workdir=phase_workdir(artifact_root, manifest, phase_name),
            worker_input=prepared_input,
            payload=payload,
        )
        sync_phase_outputs(
            artifact_root=artifact_root,
            workdir=phase_workdir(artifact_root, manifest, phase_name),
            phase_name=phase_name,
        )

    persist_phase_result(artifact_root, manifest_path, phase_name, payload)
    return payload, 0 if payload["status"] != "failed" else 1


def main() -> int:
    args = parse_args()
    artifact_root = Path(args.artifact_root).resolve()
    manifest_path = ensure_manifest(artifact_root)
    manifest = read_json_file(manifest_path)

    errors = validate_phase_manifest(manifest, args.phase)
    if args.phase != "preflight":
        errors.extend(required_inputs_exist(artifact_root, args.phase))
    if errors:
        payload = build_failure_payload(
            args.phase,
            "Phase contract validation failed before execution.",
            errors,
        )
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        for error in errors:
            print(error)
        return 1

    try:
        if args.command == "prepare":
            payload = prepare_phase(artifact_root, manifest, args.phase)
            print(json.dumps(payload, indent=2))
            return 0

        payload, exit_code = apply_phase(
            artifact_root=artifact_root,
            manifest_path=manifest_path,
            manifest=manifest,
            phase_name=args.phase,
            result_file_arg=args.result_file,
        )
        print(json.dumps(payload, indent=2))
        return exit_code
    except subprocess.CalledProcessError as exc:
        payload = build_failure_payload(
            args.phase,
            "Phase execution failed.",
            [f"Command failed with exit code {exc.returncode}."],
        )
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        return exc.returncode or 1
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        payload = build_failure_payload(
            args.phase,
            "Phase result validation failed during apply." if args.command == "apply" else "Phase preparation failed.",
            [str(exc)],
        )
        persist_phase_result(artifact_root, manifest_path, args.phase, payload)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
