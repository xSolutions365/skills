#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_ROOT="$ROOT_DIR/skills/create-execplan"

contract_files=(
  "$SKILL_ROOT/SKILL.md"
  "$SKILL_ROOT/README.md"
  "$SKILL_ROOT/references/context-pack-template.md"
  "$SKILL_ROOT/references/execplan-template.md"
  "$SKILL_ROOT/references/review-checklist.md"
  "$SKILL_ROOT/references/review-checklist-template.md"
  "$SKILL_ROOT/references/runtime-resolution.md"
  "$SKILL_ROOT/references/step-0-preflight-workflow.md"
  "$SKILL_ROOT/references/step-1-intake-freeze-workflow.md"
  "$SKILL_ROOT/references/step-2-context-pack-workflow.md"
  "$SKILL_ROOT/references/step-3-draft-review-workflow.md"
  "$SKILL_ROOT/references/step-4-finalize-execplan-workflow.md"
  "$SKILL_ROOT/references/step-5-readiness-audit-workflow.md"
  "$SKILL_ROOT/references/step-6-checklist-workflow.md"
  "$SKILL_ROOT/examples/finalized-context-pack.md"
  "$SKILL_ROOT/examples/finalized-execplan.md"
  "$SKILL_ROOT/examples/expected-runtime-input.json"
  "$SKILL_ROOT/examples/workspace/execplan-runtime-input.json"
  "$ROOT_DIR/scripts/run-ci-quality-gates.sh"
  "$ROOT_DIR/tests/run_create_execplan_helpers.sh"
)

existing_contract_files=()
for path in "${contract_files[@]}"; do
  if [[ -f "$path" ]]; then
    existing_contract_files+=("$path")
  fi
done

python_refs="$(
  rg -n \
    "python3[[:space:]]+(-m|[^[:space:]]+\\.py\\b)" \
    "${existing_contract_files[@]}" || true
)"

legacy_refs="$(
  rg -n \
    "execplan-task-packets\\.json|## Verification Strategy|## Quality Gates|## Artifacts & Notes|## Plan Overview \\(phases\\)" \
    "${existing_contract_files[@]}" || true
)"

if [[ -n "$python_refs" ]]; then
  echo "hardcoded python3 references are not allowed outside the runtime resolver:" >&2
  echo "$python_refs" >&2
  exit 1
fi

if [[ -n "$legacy_refs" ]]; then
  echo "legacy create-execplan names or sections are still present:" >&2
  echo "$legacy_refs" >&2
  exit 1
fi

echo "create-execplan runtime references passed"
