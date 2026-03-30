#!/usr/bin/env bash
set -euo pipefail

PHASE=""
PHASE_WORKDIR=""
PROMPT_FILE=""
SCHEMA_FILE=""
RESULT_FILE=""
STDOUT_FILE=""
STDERR_FILE=""
CODEX_BIN="${CODEX_BIN:-codex}"

usage() {
  cat <<'EOF'
Usage: run_codex_phase.sh --workdir <dir> --prompt-file <path> --schema-file <path> --result-file <path> [--stdout-file <path>] [--stderr-file <path>] [--codex-bin <path>]
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workdir)
      PHASE_WORKDIR="$2"
      shift 2
      ;;
    --prompt-file)
      PROMPT_FILE="$2"
      shift 2
      ;;
    --schema-file)
      SCHEMA_FILE="$2"
      shift 2
      ;;
    --result-file)
      RESULT_FILE="$2"
      shift 2
      ;;
    --stdout-file)
      STDOUT_FILE="$2"
      shift 2
      ;;
    --stderr-file)
      STDERR_FILE="$2"
      shift 2
      ;;
    --codex-bin)
      CODEX_BIN="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

for required in "$PHASE_WORKDIR" "$PROMPT_FILE" "$SCHEMA_FILE" "$RESULT_FILE"; do
  if [[ -z "$required" ]]; then
    echo "Missing required arguments for run_codex_phase.sh" >&2
    usage >&2
    exit 2
  fi
done

mkdir -p "$(dirname "$RESULT_FILE")"
if [[ -n "$STDOUT_FILE" ]]; then
  mkdir -p "$(dirname "$STDOUT_FILE")"
fi
if [[ -n "$STDERR_FILE" ]]; then
  mkdir -p "$(dirname "$STDERR_FILE")"
fi

stdout_target="${STDOUT_FILE:-/dev/stdout}"
stderr_target="${STDERR_FILE:-/dev/stderr}"
SOURCE_CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
TMP_CODEX_HOME="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_CODEX_HOME"
}
trap cleanup EXIT

if [[ -f "$SOURCE_CODEX_HOME/auth.json" ]]; then
  cp "$SOURCE_CODEX_HOME/auth.json" "$TMP_CODEX_HOME/auth.json"
fi

CODEX_HOME="$TMP_CODEX_HOME" "$CODEX_BIN" exec \
  --ephemeral \
  --json \
  --color never \
  --sandbox workspace-write \
  --skip-git-repo-check \
  -C "$PHASE_WORKDIR" \
  --output-schema "$SCHEMA_FILE" \
  -o "$RESULT_FILE" \
  - < "$PROMPT_FILE" >"$stdout_target" 2>"$stderr_target"
