#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENABLE_LIVE_SMOKE="${CREATE_EXECPLAN_ENABLE_LIVE_CODEX:-0}"
CODEX_BIN="${CODEX_BIN:-codex}"
LIVE_MODEL="${CREATE_EXECPLAN_LIVE_MODEL:-}"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

if [[ "$ENABLE_LIVE_SMOKE" != "1" ]]; then
  echo "skipping live Codex smoke; set CREATE_EXECPLAN_ENABLE_LIVE_CODEX=1 to enable"
  exit 0
fi

if ! command -v "$CODEX_BIN" >/dev/null 2>&1; then
  echo "live Codex smoke requires Codex CLI on PATH or CODEX_BIN to point to it" >&2
  exit 1
fi

WORKDIR="$TMP_DIR/nonrepo-phase"
mkdir -p "$WORKDIR"

PROMPT_FILE="$TMP_DIR/prompt.txt"
SCHEMA_FILE="$TMP_DIR/schema.json"
RESULT_FILE="$TMP_DIR/result.json"
STDOUT_FILE="$TMP_DIR/stdout.jsonl"
STDERR_FILE="$TMP_DIR/stderr.log"

cat > "$PROMPT_FILE" <<'EOF'
You are executing the create-execplan `research` phase.
Return only a JSON object matching the schema.
Set phase to `research`, status to `complete`, and message to `live codex smoke ok`.
Set inputArtifacts, outputArtifacts, and blockingIssues to empty arrays.
EOF

cat > "$SCHEMA_FILE" <<'EOF'
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "phase": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": ["complete", "needs_user_input", "needs_approval", "blocked", "failed"]
    },
    "message": {
      "type": "string"
    },
    "inputArtifacts": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "outputArtifacts": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "blockingIssues": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "phase",
    "status",
    "message",
    "inputArtifacts",
    "outputArtifacts",
    "blockingIssues"
  ]
}
EOF

RUNNER_ARGS=(
  --codex-bin "$CODEX_BIN"
  --workdir "$WORKDIR"
  --prompt-file "$PROMPT_FILE"
  --schema-file "$SCHEMA_FILE"
  --result-file "$RESULT_FILE"
  --stdout-file "$STDOUT_FILE"
  --stderr-file "$STDERR_FILE"
)

if [[ -n "$LIVE_MODEL" ]]; then
  export CODEX_BIN
  cat > "$TMP_DIR/codex-wrapper.sh" <<EOF
#!/usr/bin/env bash
set -euo pipefail
exec "$CODEX_BIN" -m "$LIVE_MODEL" "\$@"
EOF
  chmod +x "$TMP_DIR/codex-wrapper.sh"
  RUNNER_ARGS=(--codex-bin "$TMP_DIR/codex-wrapper.sh" "${RUNNER_ARGS[@]:2}")
fi

"$ROOT_DIR/skills/create-execplan/scripts/run_codex_phase.sh" "${RUNNER_ARGS[@]}"

grep -q '"phase":"research"' "$RESULT_FILE"
grep -q '"status":"complete"' "$RESULT_FILE"
grep -q '"message":"live codex smoke ok"' "$RESULT_FILE"

echo "create-execplan live Codex smoke passed"
