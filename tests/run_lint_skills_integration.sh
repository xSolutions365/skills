#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LINT_SCRIPT="$ROOT_DIR/scripts/lint_skills.sh"
FIXTURES_ROOT="$ROOT_DIR/tests/fixtures/lint_skills"

run_fixture() {
  local fixture_name="$1"
  local fixture_root="$FIXTURES_ROOT/$fixture_name"
  local output

  if [[ ! -d "$fixture_root" ]]; then
    echo "missing fixture repo: $fixture_root" >&2
    return 1
  fi

  if ! output="$(bash "$LINT_SCRIPT" --root "$fixture_root" 2>&1)"; then
    echo "$output" >&2
    return 1
  fi

  if [[ "$output" != *"skills: lint passed"* ]]; then
    echo "lint output missing success marker for fixture: $fixture_name" >&2
    echo "$output" >&2
    return 1
  fi
}

run_fixture "compact_repo"
run_fixture "structured_repo"

echo "lint integration fixtures passed"
