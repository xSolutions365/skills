#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECK_SCRIPT="$ROOT_DIR/scripts/check_marketplace_manifest.py"
FIXTURE_ROOT="$(mktemp -d)"
trap 'rm -rf "$FIXTURE_ROOT"' EXIT

make_fixture() {
  local fixture="$1"
  mkdir -p "$FIXTURE_ROOT/$fixture/.claude-plugin" \
    "$FIXTURE_ROOT/$fixture/skills/alpha" \
    "$FIXTURE_ROOT/$fixture/skills/beta"
  touch "$FIXTURE_ROOT/$fixture/skills/alpha/SKILL.md" \
    "$FIXTURE_ROOT/$fixture/skills/beta/SKILL.md"
  cat >"$FIXTURE_ROOT/$fixture/.claude-plugin/marketplace.json" <<'EOF'
{
  "name": "example-marketplace",
  "owner": {"name": "Example"},
  "plugins": [
    {"name": "alpha", "source": "./", "skills": ["./skills/alpha"]},
    {"name": "beta", "source": "./", "skills": ["./skills/beta"]}
  ]
}
EOF
}

run_valid_fixture() {
  if ! python3 "$CHECK_SCRIPT" --root "$FIXTURE_ROOT/valid"; then
    echo "valid marketplace manifest fixture failed" >&2
    return 1
  fi
}

run_invalid_fixture() {
  local fixture="$1"
  local expected_message="$2"
  local output
  if output="$(python3 "$CHECK_SCRIPT" --root "$FIXTURE_ROOT/$fixture" 2>&1)"; then
    echo "invalid marketplace manifest fixture unexpectedly passed: $fixture" >&2
    return 1
  fi
  if [[ "$output" != *"$expected_message"* ]]; then
    echo "marketplace manifest fixture missing expected message: $fixture" >&2
    echo "expected: $expected_message" >&2
    echo "$output" >&2
    return 1
  fi
}

make_fixture valid
run_valid_fixture

make_fixture missing_marketplace_name
python3 - "$FIXTURE_ROOT/missing_marketplace_name/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest.pop("name")
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture missing_marketplace_name "marketplace must have a non-empty name"

make_fixture missing_owner
python3 - "$FIXTURE_ROOT/missing_owner/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest.pop("owner")
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture missing_owner "marketplace owner must have a non-empty name"

make_fixture missing_source
python3 - "$FIXTURE_ROOT/missing_source/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest["plugins"][0].pop("source")
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture missing_source "plugin alpha must have a non-empty source"

make_fixture malformed
printf '{not json\n' >"$FIXTURE_ROOT/malformed/.claude-plugin/marketplace.json"
run_invalid_fixture malformed "cannot read valid JSON"

make_fixture missing_path
python3 - "$FIXTURE_ROOT/missing_path/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest["plugins"][0] = {
    "name": "not-found",
    "source": "./",
    "skills": ["./skills/not-found"],
}
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture missing_path "missing skill file: skills/not-found/SKILL.md"

make_fixture duplicate
python3 - "$FIXTURE_ROOT/duplicate/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest["plugins"][1] = manifest["plugins"][0]
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture duplicate "duplicate plugin entry: alpha"

make_fixture omitted
python3 - "$FIXTURE_ROOT/omitted/.claude-plugin/marketplace.json" <<'PY'
import json
import sys
from pathlib import Path

manifest_path = Path(sys.argv[1])
manifest = json.loads(manifest_path.read_text())
manifest["plugins"].pop()
manifest_path.write_text(json.dumps(manifest))
PY
run_invalid_fixture omitted "skills missing plugin entries: beta"

echo "marketplace manifest integration fixtures passed"
