#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESOLVER="$ROOT_DIR/skills/create-execplan/scripts/resolve_python.sh"
PYTHON_CMD="$("$RESOLVER")"
EXAMPLES_DIR="$ROOT_DIR/skills/create-execplan/examples"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" --help >/dev/null
"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime_input.py" --help >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py" \
  --title "Fixture Rewrite" \
  --artifact-root "$TMP_DIR/scaffold" \
  --project-mode brownfield >/dev/null

[[ -f "$TMP_DIR/scaffold/context-pack.md" ]]
[[ -f "$TMP_DIR/scaffold/execplan.md" ]]
[[ -f "$TMP_DIR/scaffold/review-checklist.md" ]]
[[ -f "$TMP_DIR/scaffold/workspace/context-discovery.md" ]]
[[ ! -f "$TMP_DIR/scaffold/workspace/execplan-runtime-input.json" ]]

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py" \
  --context-pack "$EXAMPLES_DIR/finalized-context-pack.md" \
  --output "$TMP_DIR/context-pack-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py" \
  --execplan "$EXAMPLES_DIR/finalized-execplan.md" \
  --output "$TMP_DIR/execplan-validation.json" >/dev/null

"$PYTHON_CMD" "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime_input.py" \
  --execplan "$EXAMPLES_DIR/finalized-execplan.md" \
  --output "$TMP_DIR/actual-runtime-input.json" \
  --generated-at "2026-04-01T09:00:00Z" \
  --source-execplan-value "fixture/finalized-execplan.md" >/dev/null

diff -u \
  "$EXAMPLES_DIR/expected-runtime-input.json" \
  "$TMP_DIR/actual-runtime-input.json"

echo "create-execplan helper checks passed"
