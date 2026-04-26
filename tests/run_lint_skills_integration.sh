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
run_fixture "behaviour_guidance_repo"
run_fixture "simple_task_repo"
run_fixture "simple_runbook_repo"
run_fixture "structured_repo"

run_negative_fixture() {
  local fixture_name="$1"
  local expected_message="$2"
  local fixture_root
  local output
  fixture_root="$(mktemp -d)"
  mkdir -p "$fixture_root/skills/$fixture_name"

  case "$fixture_name" in
    behaviour-too-long)
      {
        printf '%s\n' '---'
        printf '%s\n' 'name: "behaviour-too-long"'
        printf '%s\n' 'description: "Guide overly long behavior. USE WHEN a behaviour guidance fixture should fail."'
        printf '%s\n' '---'
        printf '%s\n' ''
        printf '%s\n' '# Guidance'
        printf '%s\n' ''
        printf '%s\n' '## Rules'
        for idx in $(seq 1 101); do
          printf -- '- Rule %s.\n' "$idx"
        done
      } >"$fixture_root/skills/$fixture_name/SKILL.md"
      ;;
    simple-too-long)
      {
        printf '%s\n' '---'
        printf '%s\n' 'name: "simple-too-long"'
        printf '%s\n' 'description: "Guide overly long task work. USE WHEN a simple task fixture should fail."'
        printf '%s\n' '---'
        printf '%s\n' ''
        printf '%s\n' '# Task'
        printf '%s\n' ''
        printf '%s\n' '## Procedure'
        for idx in $(seq 1 501); do
          printf -- '- Step %s.\n' "$idx"
        done
      } >"$fixture_root/skills/$fixture_name/SKILL.md"
      ;;
    simple-wrong-heading)
      cat >"$fixture_root/skills/$fixture_name/SKILL.md" <<'EOF'
---
name: "simple-wrong-heading"
description: "Guide a task with the wrong heading. USE WHEN a simple task fixture should fail."
---

# Notes

## Procedure

- Complete the task.
EOF
      ;;
    unreachable-runbook)
      mkdir -p "$fixture_root/skills/$fixture_name/references"
      cat >"$fixture_root/skills/$fixture_name/SKILL.md" <<'EOF'
---
name: "unreachable-runbook"
description: "Guide a task with an unreachable runbook. USE WHEN a runbook fixture should fail."
---

# Task

## Procedure

- Complete the task.
EOF
      cat >"$fixture_root/skills/$fixture_name/references/extra.md" <<'EOF'
# Extra

## Guidance

- This runbook is intentionally unreachable.
EOF
      ;;
    broken-workflow)
      mkdir -p "$fixture_root/skills/$fixture_name/references"
      cat >"$fixture_root/skills/$fixture_name/SKILL.md" <<'EOF'
---
name: "broken-workflow"
description: "Run a broken workflow. USE WHEN a multi-step fixture should fail."
---

# Workflow

### Step 1: Missing reference

- Do the work.

## Output

### Result Format

- Report the result.
EOF
      cat >"$fixture_root/skills/$fixture_name/README.md" <<'EOF'
# broken-workflow

## Overview

Broken multi-step fixture.

## When to use it

- You need a failing fixture.

## Example prompts

- "Run the broken workflow."
EOF
      ;;
    *)
      echo "unknown negative fixture: $fixture_name" >&2
      return 1
      ;;
  esac

  if output="$(bash "$LINT_SCRIPT" --root "$fixture_root" 2>&1)"; then
    echo "negative fixture unexpectedly passed: $fixture_name" >&2
    echo "$output" >&2
    return 1
  fi

  if [[ "$output" != *"$expected_message"* ]]; then
    echo "negative fixture missing expected message: $fixture_name" >&2
    echo "expected: $expected_message" >&2
    echo "$output" >&2
    return 1
  fi
}

run_negative_fixture "behaviour-too-long" "Behaviour guidance SKILL.md must stay at or under 100 lines."
run_negative_fixture "simple-too-long" "Simple task inline SKILL.md must stay at or under 500 lines."
run_negative_fixture "simple-wrong-heading" "Simple task inline SKILL.md must begin with a '# Task' heading immediately after frontmatter."
run_negative_fixture "unreachable-runbook" "Markdown file appears unreachable from SKILL.md"
run_negative_fixture "broken-workflow" "Step 1 must include exactly one reference link to a file under references/."

echo "lint integration fixtures passed"
