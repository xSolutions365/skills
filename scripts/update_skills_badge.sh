#!/usr/bin/env bash
set -euo pipefail

parse_args() {
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
  CHECK_MODE="false"

  while (($# > 0)); do
    case "$1" in
      --root)
        shift
        [[ $# -gt 0 ]] || { echo "Missing value for --root" >&2; exit 1; }
        REPO_ROOT="$(cd "$1" && pwd -P)"
        shift
        ;;
      --check)
        CHECK_MODE="true"
        shift
        ;;
      *)
        echo "Unknown argument: $1" >&2
        exit 1
        ;;
    esac
  done
}

count_skills() {
  local skills_root="$1"
  if [[ ! -d "$skills_root" ]]; then
    printf '0\n'
    return
  fi

  find "$skills_root" -mindepth 1 -maxdepth 1 -type d ! -name '.*' | wc -l | tr -d ' '
}

render_payload() {
  local skill_count="$1"
  cat <<EOF
{
  "schemaVersion": 1,
  "label": "skills",
  "message": "$skill_count",
  "color": "2ea44f"
}
EOF
}

main() {
  parse_args "$@"

  local skills_root="$REPO_ROOT/skills"
  local output_path="$REPO_ROOT/badges/skills-count.json"
  local skill_count rendered current

  skill_count="$(count_skills "$skills_root")"
  rendered="$(render_payload "$skill_count")"

  if [[ "$CHECK_MODE" == "true" ]]; then
    if [[ ! -f "$output_path" ]]; then
      echo "Missing badge payload: $output_path" >&2
      exit 1
    fi

    current="$(cat "$output_path")"
    if [[ "$current"$'\n' != "$rendered"$'\n' ]]; then
      echo "skills count badge payload is out of date; run scripts/update_skills_badge.sh" >&2
      exit 1
    fi

    echo "skills badge payload is up to date"
    exit 0
  fi

  mkdir -p "$(dirname "$output_path")"
  printf '%s\n' "$rendered" >"$output_path"
  echo "updated $output_path"
}

main "$@"
