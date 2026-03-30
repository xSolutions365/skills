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

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime_input.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" --help >/dev/null
"$ROOT_DIR/skills/create-execplan/scripts/run_codex_phase.sh" --help >/dev/null

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
[[ -f "$TMP_DIR/scaffold/workspace/research-questions.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/research-findings.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/design-options.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/structure-outline.md" ]]
[[ ! -f "$TMP_DIR/scaffold/workspace/execplan-runtime-input.json" ]]
! rg -q '^## Established Library Comparison \(required for greenfield; optional for brownfield\)$' "$TMP_DIR/scaffold/context-pack.md"
rg -q '^## Existing Change Surface \(required for brownfield; optional for greenfield\)$' "$TMP_DIR/scaffold/context-pack.md"
rg -q '"currentPhase": "preflight"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
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

FAKE_CODEX="$TMP_DIR/fake-codex"
cat > "$FAKE_CODEX" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

RESULT_FILE=""
WORKDIR=""
PROMPT_CAPTURE=""
ARGS_CAPTURE=""
CODEX_HOME_CAPTURE=""

subcommand="$1"
shift
if [[ "$subcommand" != "exec" ]]; then
  echo "expected exec subcommand" >&2
  exit 2
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    -C)
      WORKDIR="$2"
      shift 2
      ;;
    -o)
      RESULT_FILE="$2"
      shift 2
      ;;
    --output-schema)
      [[ -f "$2" ]]
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

ARGS_CAPTURE="${WORKDIR}/fake-codex-argv.txt"
PROMPT_CAPTURE="${WORKDIR}/fake-codex-prompt.txt"
CODEX_HOME_CAPTURE="${WORKDIR}/fake-codex-codex-home.txt"
printf '%s\n' "$0 exec --ephemeral --json --color never --skip-git-repo-check -C $WORKDIR -o $RESULT_FILE" > "$ARGS_CAPTURE"
printf '%s\n' "${CODEX_HOME:-}" > "$CODEX_HOME_CAPTURE"
cat > "$PROMPT_CAPTURE"

phase_name="$(sed -n 's/.*isolated planning phase `\([^`]*\)`.*/\1/p' "$PROMPT_CAPTURE" | head -n 1)"
if [[ -z "$phase_name" ]]; then
  phase_name="research"
fi

if [[ "$phase_name" == "research" ]]; then
  input_artifacts='["workspace/requirements-freeze.md","workspace/research-questions.md","workspace/context-evidence.json","workspace/context-codemap.md","workspace/research-findings.md"]'
  output_artifacts='["workspace/context-evidence.json","workspace/context-codemap.md","workspace/research-findings.md","workspace/phase-result.json"]'
else
  input_artifacts='[]'
  output_artifacts='[]'
fi

cat > "$RESULT_FILE" <<JSON
{"phase":"$phase_name","status":"complete","message":"fake codex ok","inputArtifacts":$input_artifacts,"outputArtifacts":$output_artifacts,"blockingIssues":[]}
JSON
printf '%s\n' '{"type":"thread.started","thread_id":"fake"}'
printf '%s\n' '{"type":"turn.completed","usage":{"input_tokens":1,"cached_input_tokens":0,"output_tokens":1}}'
printf '%s\n' 'fake codex diagnostic' >&2
EOF
chmod +x "$FAKE_CODEX"

NONREPO_WORKDIR="$TMP_DIR/nonrepo-phase"
mkdir -p "$NONREPO_WORKDIR"
cat > "$TMP_DIR/wrapper-prompt.txt" <<'EOF'
You are executing the isolated planning phase `research` for an already-scaffolded plan package.
EOF
cat > "$TMP_DIR/wrapper-schema.json" <<'EOF'
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object"
}
EOF
"$ROOT_DIR/skills/create-execplan/scripts/run_codex_phase.sh" \
  --codex-bin "$FAKE_CODEX" \
  --workdir "$NONREPO_WORKDIR" \
  --prompt-file "$TMP_DIR/wrapper-prompt.txt" \
  --schema-file "$TMP_DIR/wrapper-schema.json" \
  --result-file "$TMP_DIR/wrapper-result.json" \
  --stdout-file "$TMP_DIR/wrapper-stdout.jsonl" \
  --stderr-file "$TMP_DIR/wrapper-stderr.log"

rg -q -- '--skip-git-repo-check' "$NONREPO_WORKDIR/fake-codex-argv.txt"
rg -q 'isolated planning phase `research`' "$NONREPO_WORKDIR/fake-codex-prompt.txt"
! rg -q 'create-execplan' "$NONREPO_WORKDIR/fake-codex-prompt.txt"
rg -q '"phase":"research"' "$TMP_DIR/wrapper-result.json"
rg -q 'fake codex diagnostic' "$TMP_DIR/wrapper-stderr.log"
[[ -s "$NONREPO_WORKDIR/fake-codex-codex-home.txt" ]]
[[ "$(cat "$NONREPO_WORKDIR/fake-codex-codex-home.txt")" != "$HOME/.codex" ]]

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  --phase preflight \
  --artifact-root "$TMP_DIR/scaffold" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/run_phase.py" \
  --phase research \
  --artifact-root "$TMP_DIR/scaffold" \
  --codex-bin "$FAKE_CODEX" >/dev/null

RESEARCH_WORKDIR="$("$PYTHON_CMD" - "$TMP_DIR/scaffold/workspace/phase-manifest.json" <<'PY'
from __future__ import annotations
import json
import sys
from pathlib import Path

payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
print(payload["phases"]["research"]["workdir"])
PY
)"

rg -q '"phase": "research"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"status": "complete"' "$TMP_DIR/scaffold/workspace/phase-result.json"
rg -q '"currentPhase": "design"' "$TMP_DIR/scaffold/workspace/phase-manifest.json"
[[ "$RESEARCH_WORKDIR" = /* ]]
[[ "$RESEARCH_WORKDIR" != "$TMP_DIR/scaffold"* ]]
[[ -f "$RESEARCH_WORKDIR/fake-codex-prompt.txt" ]]
rg -q 'do not delegate or use agent-management tools' "$TMP_DIR/scaffold/workspace/phases/research/.codex-phase/prompt.txt"
rg -q 'do not inspect git state, git history, or ancestor directories' "$TMP_DIR/scaffold/workspace/phases/research/.codex-phase/prompt.txt"
rg -q 'do not load or invoke any skills' "$TMP_DIR/scaffold/workspace/phases/research/.codex-phase/prompt.txt"
rg -q '"blockingIssues"' "$TMP_DIR/scaffold/workspace/phases/research/.codex-phase/schema.json"
"$PYTHON_CMD" - "$TMP_DIR/scaffold/workspace/phases/research/.codex-phase/schema.json" <<'PY'
from __future__ import annotations
import json
import sys
from pathlib import Path

payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
required = payload.get("required", [])
if "blockingIssues" not in required:
    raise SystemExit("schema.json must require blockingIssues")
PY

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
  --phase research \
  --artifact-root "$TMP_DIR/scaffold-invalid" \
  --codex-bin "$FAKE_CODEX" >/dev/null 2>&1; then
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

cp -R "$CANONICAL_EXAMPLES_DIR" "$TMP_DIR/rubric-unresolved-freeze"
"$PYTHON_CMD" - "$TMP_DIR/rubric-unresolved-freeze/workspace/requirements-freeze.md" <<'PY'
from __future__ import annotations
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8").replace(
    "- User approval response (verbatim excerpt): requirements confirmed; proceed to context analysis",
    "- User approval response (verbatim excerpt): <approval-excerpt>",
)
path.write_text(text, encoding="utf-8")
PY
if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" \
  --artifact-root "$TMP_DIR/rubric-unresolved-freeze" >/dev/null 2>&1; then
  echo "validate_plan_rubric.py should fail when requirements freeze still contains unresolved placeholders" >&2
  exit 1
fi

cp -R "$CANONICAL_EXAMPLES_DIR" "$TMP_DIR/rubric-vague-packet"
"$PYTHON_CMD" - "$TMP_DIR/rubric-vague-packet/execplan.md" <<'PY'
from __future__ import annotations
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8").replace(
    "Run the helper regression checks against the updated examples and scaffolder.",
    "Identify the relevant regression checks and run whatever seems appropriate.",
)
path.write_text(text, encoding="utf-8")
PY
if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" \
  --execplan "$TMP_DIR/rubric-vague-packet/execplan.md" >/dev/null 2>&1; then
  echo "validate_execplan.py should fail when a brownfield packet row requires discovery" >&2
  exit 1
fi

cp -R "$CANONICAL_EXAMPLES_DIR" "$TMP_DIR/rubric-missing-approval"
"$PYTHON_CMD" - "$TMP_DIR/rubric-missing-approval/workspace/draft-review.md" <<'PY'
from __future__ import annotations
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8").replace(
    "- User approval response (verbatim excerpt): approved for finalization",
    "- User approval response (verbatim excerpt): <approval-excerpt>",
)
path.write_text(text, encoding="utf-8")
PY
if "$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_plan_rubric.py" \
  --artifact-root "$TMP_DIR/rubric-missing-approval" >/dev/null 2>&1; then
  echo "validate_plan_rubric.py should fail when approval evidence is missing" >&2
  exit 1
fi

echo "create-execplan helper checks passed"
