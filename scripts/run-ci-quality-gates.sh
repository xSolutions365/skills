#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNNER_PATH="scripts/run-ci-quality-gates.sh"
FIX_MODE="false"
STAGE_MODE="false"

while (($# > 0)); do
  case "$1" in
    --fix)
      FIX_MODE="true"
      shift
      ;;
    --stage)
      STAGE_MODE="true"
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

run_step() {
  local name="$1"
  shift
  echo "[quality-gates] $name"
  "$@"
}

check_parity() {
  local precommit="$ROOT_DIR/.pre-commit-config.yaml"
  local workflow="$ROOT_DIR/.github/workflows/ci-quality-gates.yml"

  if [[ ! -f "$precommit" ]]; then
    echo "Missing .pre-commit-config.yaml for parity check." >&2
    return 1
  fi
  if [[ ! -f "$workflow" ]]; then
    echo "Missing .github/workflows/ci-quality-gates.yml for parity check." >&2
    return 1
  fi
  if ! grep -Fq "$RUNNER_PATH" "$precommit"; then
    echo "Pre-commit config does not reference $RUNNER_PATH." >&2
    return 1
  fi
  if ! grep -Fq "$RUNNER_PATH" "$workflow"; then
    echo "CI workflow does not reference $RUNNER_PATH." >&2
    return 1
  fi
}

python_files=(
  "$ROOT_DIR/skills/create-execplan/scripts/render_execplan_runtime.py"
  "$ROOT_DIR/skills/create-execplan/scripts/scaffold_execplan.py"
  "$ROOT_DIR/skills/create-execplan/scripts/validate_context_pack.py"
  "$ROOT_DIR/skills/create-execplan/scripts/validate_execplan.py"
)

if [[ "$FIX_MODE" == "true" ]]; then
  run_step "Update skills badge payload" bash "$ROOT_DIR/scripts/update_skills_badge.sh"
else
  run_step "Check skills badge payload" bash "$ROOT_DIR/scripts/update_skills_badge.sh" --check
fi
run_step "Skill lint" bash "$ROOT_DIR/scripts/lint_skills.sh"
run_step "Lint integration tests" bash "$ROOT_DIR/tests/run_lint_skills_integration.sh"
run_step "Shell syntax check" bash -n "$ROOT_DIR/scripts/update_skills_badge.sh" "$ROOT_DIR/scripts/lint_skills.sh" "$ROOT_DIR/scripts/run-ci-quality-gates.sh" "$ROOT_DIR/tests/run_lint_skills_integration.sh"
run_step "Python syntax check" python3 -B -m py_compile "${python_files[@]}"
run_step "Parity guard" check_parity

if [[ "$FIX_MODE" == "true" ]]; then
  echo "[quality-gates] Fix mode completed."
fi

if [[ "$STAGE_MODE" == "true" ]]; then
  git add "$ROOT_DIR/badges/skills-count.json" >/dev/null 2>&1 || true
  echo "[quality-gates] Staged generated badge payloads."
fi
