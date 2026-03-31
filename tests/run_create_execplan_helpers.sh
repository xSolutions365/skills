#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESOLVER="$ROOT_DIR/skills/create-execplan/scripts/resolve_python.sh"
PYTHON_CMD="$("$RESOLVER")"
EXAMPLES_DIR="$ROOT_DIR/skills/create-execplan/examples"
CANONICAL_EXAMPLES_DIR="$EXAMPLES_DIR/canonical"
LIVE_REPRO_FIXTURE_DIR="$EXAMPLES_DIR/live-repro-green"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

write_phase_result() {
  local phase_name="$1"
  local phase_root="$2"
  local status="$3"
  local message="$4"
  local result_path="$5"

  "$PYTHON_CMD" - "$phase_name" "$phase_root" "$status" "$message" "$result_path" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

phase_name, phase_root, status, message, result_path = sys.argv[1:]
manifest = json.loads((Path(phase_root) / "workspace/phase-manifest.json").read_text(encoding="utf-8"))
phase = manifest["phases"][phase_name]
payload = {
    "phase": phase_name,
    "status": status,
    "message": message,
    "inputArtifacts": phase["allowedInputArtifacts"],
    "outputArtifacts": phase["expectedOutputArtifacts"],
    "blockingIssues": [],
}
Path(result_path).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
PY
}

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime_input.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" --help >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" \
  --title "Fixture Rewrite" \
  --artifact-root "$TMP_DIR/scaffold" \
  --project-mode brownfield >/dev/null

[[ -f "$TMP_DIR/scaffold/context-pack.md" ]]
[[ -f "$TMP_DIR/scaffold/execplan.md" ]]
[[ -f "$TMP_DIR/scaffold/review-checklist.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/context-discovery.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/phase-manifest.json" ]]
[[ -f "$TMP_DIR/scaffold/workspace/phase-result.json" ]]
[[ -f "$TMP_DIR/scaffold/workspace/planning-brief.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/research-questions.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/research-findings.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/design-options.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/structure-outline.md" ]]
[[ ! -f "$TMP_DIR/scaffold/workspace/execplan-runtime-input.json" ]]
! rg -q '^## Established Library Comparison \(required for greenfield; optional for brownfield\)$' "$TMP_DIR/scaffold/context-pack.md"
rg -q '^## Existing Change Surface \(required for brownfield; optional for greenfield\)$' "$TMP_DIR/scaffold/context-pack.md"
rg -q '"currentPhase": "preflight"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
rg -q '"selectedRunner": "subagent"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
rg -q '"runner": "subagent"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
rg -q '"runner": "deterministic"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
! rg -q '"requirements-freeze": \{' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
rg -q '^\| Status \| Phase # \| Task # \| Type \| Req IDs \| Edit Targets \| Supporting Context Anchors \| Commands \| Expected Output \| Action \|$' "$TMP_DIR/scaffold/execplan.md"
rg -q '^- Confirmed by user at: <ISO8601 UTC>$' "$TMP_DIR/scaffold/context-pack.md"
rg -q '^- Confirmed by user at: <ISO8601 UTC>$' "$TMP_DIR/scaffold/execplan.md"
rg -q '^  - Date: <YYYY-MM-DD>$' "$TMP_DIR/scaffold/execplan.md"

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" \
  --title "Greenfield Fixture" \
  --artifact-root "$TMP_DIR/greenfield" \
  --project-mode greenfield >/dev/null

rg -q '^## Established Library Comparison \(required for greenfield; optional for brownfield\)$' "$TMP_DIR/greenfield/context-pack.md"
! rg -q '^## Existing Change Surface \(required for brownfield; optional for greenfield\)$' "$TMP_DIR/greenfield/context-pack.md"

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  prepare \
  --phase preflight \
  --artifact-root "$TMP_DIR/scaffold" >/dev/null

[[ -f "$TMP_DIR/scaffold/workspace/phases/preflight/phase-worker-result.json" ]]

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  apply \
  --phase preflight \
  --artifact-root "$TMP_DIR/scaffold" >/dev/null

rg -q '"phase": "preflight"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"status": "complete"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"currentPhase": "research-questions"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  prepare \
  --phase research \
  --artifact-root "$TMP_DIR/scaffold" >/dev/null

RESEARCH_WORKDIR="$("$PYTHON_CMD" - "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json" <<'PY'
from __future__ import annotations
import json
import sys
from pathlib import Path

payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
print(payload["phaseWorkdir"])
PY
)"
RESEARCH_RESULT="$TMP_DIR/scaffold/workspace/phases/research/phase-worker-result.json"

[[ "$RESEARCH_WORKDIR" = /* ]]
[[ "$RESEARCH_WORKDIR" != "$TMP_DIR/scaffold"* ]]
[[ -f "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json" ]]
rg -q '"runner": "subagent"' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q '"workspace/planning-brief.md"' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q 'fresh context' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q 'do not load or invoke skills' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q 'do not ask the user questions directly' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q 'do not use agent-management tools' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"
rg -q '"blockingIssues"' "$TMP_DIR/scaffold/workspace/phases/research/phase-worker-input.json"

"$PYTHON_CMD" - "$RESEARCH_WORKDIR/workspace/context-evidence.json" "$RESEARCH_WORKDIR/workspace/research-findings.md" "$RESEARCH_WORKDIR/workspace/context-codemap.md" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

evidence_path = Path(sys.argv[1])
findings_path = Path(sys.argv[2])
codemap_path = Path(sys.argv[3])

payload = json.loads(evidence_path.read_text(encoding="utf-8"))
payload["helperMarker"] = "research-phase"
evidence_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
findings_path.write_text(findings_path.read_text(encoding="utf-8") + "\n- Helper test note: research output updated.\n", encoding="utf-8")
codemap_path.write_text(codemap_path.read_text(encoding="utf-8") + "\n| helper | `workspace/research-findings.md:1` | helper coverage | apply path | helper update |\n", encoding="utf-8")
PY

write_phase_result "research" "$TMP_DIR/scaffold" "complete" "helper research ok" "$RESEARCH_RESULT"

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  apply \
  --phase research \
  --artifact-root "$TMP_DIR/scaffold" >/dev/null

rg -q '"phase": "research"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"status": "complete"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"currentPhase": "design"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
rg -q 'helperMarker' "$TMP_DIR/scaffold/workspace/context-evidence.json"
rg -q 'Helper test note: research output updated\.' "$TMP_DIR/scaffold/workspace/research-findings.md"

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" \
  --title "Checkpoint Failure" \
  --artifact-root "$TMP_DIR/checkpoint-failure" \
  --project-mode brownfield >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  prepare \
  --phase execplan-draft \
  --artifact-root "$TMP_DIR/checkpoint-failure" >/dev/null

write_phase_result \
  "execplan-draft" \
  "$TMP_DIR/checkpoint-failure" \
  "needs_approval" \
  "approval requested without edits" \
  "$TMP_DIR/checkpoint-failure/workspace/phases/execplan-draft/phase-worker-result.json"

if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  apply \
  --phase execplan-draft \
  --artifact-root "$TMP_DIR/checkpoint-failure" >/dev/null 2>&1; then
  echo "run_phase.py should reject checkpoint results without artifact updates" >&2
  exit 1
fi

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" \
  --title "Readonly Failure" \
  --artifact-root "$TMP_DIR/readonly-failure" \
  --project-mode brownfield >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  prepare \
  --phase research \
  --artifact-root "$TMP_DIR/readonly-failure" >/dev/null

READONLY_WORKDIR="$("$PYTHON_CMD" - "$TMP_DIR/readonly-failure/workspace/phases/research/phase-worker-input.json" <<'PY'
from __future__ import annotations
import json
import sys
from pathlib import Path

payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
print(payload["phaseWorkdir"])
PY
)"
printf '\n- illegal readonly mutation\n' >> "$READONLY_WORKDIR/workspace/requirements-freeze.md"
write_phase_result \
  "research" \
  "$TMP_DIR/readonly-failure" \
  "complete" \
  "readonly mutation" \
  "$TMP_DIR/readonly-failure/workspace/phases/research/phase-worker-result.json"

if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  apply \
  --phase research \
  --artifact-root "$TMP_DIR/readonly-failure" >/dev/null 2>&1; then
  echo "run_phase.py should reject read-only staged artifact mutations" >&2
  exit 1
fi

cp -R "$TMP_DIR/scaffold" "$TMP_DIR/scaffold-invalid"
"$PYTHON_CMD" - "$TMP_DIR/scaffold-invalid/workspace/phase-manifest.json" <<'PY'
from __future__ import annotations
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
payload = json.loads(manifest_path.read_text(encoding="utf-8"))
payload["phases"]["research"]["allowedInputArtifacts"].append("workspace/unapproved-handoff.md")
manifest_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
PY

if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  prepare \
  --phase research \
  --artifact-root "$TMP_DIR/scaffold-invalid" >/dev/null 2>&1; then
  echo "run_phase.py should reject a drifted manifest contract" >&2
  exit 1
fi

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" \
  --context-pack "$CANONICAL_EXAMPLES_DIR/context-pack.md" \
  --output "$TMP_DIR/context-pack-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" \
  --execplan "$CANONICAL_EXAMPLES_DIR/execplan.md" \
  --output "$TMP_DIR/execplan-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" \
  --artifact-root "$CANONICAL_EXAMPLES_DIR" \
  --output "$TMP_DIR/plan-rubric-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" \
  --context-pack "$LIVE_REPRO_FIXTURE_DIR/context-pack.md" \
  --output "$TMP_DIR/live-repro-context-pack-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" \
  --execplan "$LIVE_REPRO_FIXTURE_DIR/execplan.md" \
  --output "$TMP_DIR/live-repro-execplan-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" \
  --artifact-root "$LIVE_REPRO_FIXTURE_DIR" \
  --output "$TMP_DIR/live-repro-plan-rubric-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime_input.py" \
  --execplan "$CANONICAL_EXAMPLES_DIR/execplan.md" \
  --output "$TMP_DIR/actual-runtime-input.json" \
  --generated-at "2026-04-01T09:00:00Z" >/dev/null

diff -u \
  "$CANONICAL_EXAMPLES_DIR/workspace/execplan-runtime-input.json" \
  "$TMP_DIR/actual-runtime-input.json"

cp -R "$CANONICAL_EXAMPLES_DIR" "$TMP_DIR/rubric-missing-structure"
"$PYTHON_CMD" - "$TMP_DIR/rubric-missing-structure/workspace/structure-outline.md" <<'PY'
from __future__ import annotations
import sys
from pathlib import Path

Path(sys.argv[1]).unlink()
PY

if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" \
  --artifact-root "$TMP_DIR/rubric-missing-structure" >/dev/null 2>&1; then
  echo "validate_plan_rubric.py should fail when structure artifact is missing" >&2
  exit 1
fi
