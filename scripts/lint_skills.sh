#!/usr/bin/env bash
set -euo pipefail

COMPACT_SKILL_MAX_LINES=500
BEHAVIOUR_GUIDANCE_MAX_LINES=100
ISSUES_FILE="$(mktemp)"
TEMP_FILES=("$ISSUES_FILE")

cleanup() {
  local path
  for path in "${TEMP_FILES[@]}"; do
    [[ -n "${path:-}" && -e "$path" ]] && rm -f "$path"
  done
}
trap cleanup EXIT

register_temp_file() {
  TEMP_FILES+=("$1")
}

trim() {
  local value="$1"
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  printf '%s' "$value"
}

to_lower() {
  printf '%s' "$1" | tr '[:upper:]' '[:lower:]'
}

strip_quotes() {
  local value
  value="$(trim "$1")"
  if [[ ${#value} -ge 2 ]]; then
    if [[ "${value:0:1}" == '"' && "${value: -1}" == '"' ]]; then
      value="${value:1:${#value}-2}"
    elif [[ "${value:0:1}" == "'" && "${value: -1}" == "'" ]]; then
      value="${value:1:${#value}-2}"
    fi
  fi
  printf '%s' "$value"
}

add_issue() {
  printf '%s\t%s\t%s\n' "$1" "$2" "$3" >>"$ISSUES_FILE"
}

relative_to_root() {
  local path="$1"
  case "$path" in
    "$REPO_ROOT"/*) printf '%s' "${path#$REPO_ROOT/}" ;;
    "$REPO_ROOT") printf '.' ;;
    *) printf '%s' "$path" ;;
  esac
}

canonical_existing_path() {
  local path="$1"
  if [[ -d "$path" ]]; then
    (cd "$path" && pwd -P)
    return
  fi
  local dir base
  dir="$(cd "$(dirname "$path")" && pwd -P)"
  base="$(basename "$path")"
  printf '%s/%s\n' "$dir" "$base"
}

is_within_root() {
  local path="$1"
  case "$path" in
    "$SKILL_ROOT_ABS"|"$SKILL_ROOT_ABS"/*) return 0 ;;
    *) return 1 ;;
  esac
}

line_for_text() {
  local file="$1"
  local needle="$2"
  local line
  line="$(awk -v needle="$needle" 'index($0, needle) { print NR; exit }' "$file")"
  if [[ -z "$line" ]]; then
    printf '1\n'
  else
    printf '%s\n' "$line"
  fi
}

frontmatter_end_line() {
  awk 'NR > 1 && $0 == "---" { print NR; exit }' "$1"
}

extract_frontmatter_field() {
  local file="$1"
  local field="$2"
  local end_line="$3"
  awk -v field="$field" -v end_line="$end_line" '
    NR > 1 && NR < end_line {
      raw = $0
      if (raw ~ /^[[:space:]]*$/) next
      if (raw ~ /^[[:space:]]*#/) next
      if (raw ~ /^[[:space:]]/) next
      colon_index = index(raw, ":")
      if (colon_index == 0) next
      key = substr(raw, 1, colon_index - 1)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", key)
      if (key != field) next
      value = substr(raw, colon_index + 1)
      gsub(/^[[:space:]]+/, "", value)
      print value
      exit
    }
  ' "$file"
}

normalize_link_target() {
  local target
  target="$(trim "$1")"
  if [[ "$target" == \<* && "$target" == *\> ]]; then
    target="${target#<}"
    target="${target%>}"
    target="$(trim "$target")"
  fi
  printf '%s' "${target%%[[:space:]]*}"
}

should_skip_link_target() {
  local target="$1"
  [[ -z "$target" || "$target" == \#* ]] && return 0
  [[ "$target" =~ ^[A-Za-z]: ]] && return 1
  [[ "$target" =~ ^[A-Za-z][A-Za-z0-9+.-]*: ]] || return 1
  case "$(to_lower "${target%%:*}")" in
    http|https|mailto) return 0 ;;
    *) return 1 ;;
  esac
}

strip_link_suffix() {
  local target="$1"
  target="${target%%#*}"
  target="${target%%\?*}"
  printf '%s' "$target"
}

extract_markdown_links() {
  awk '
    {
      line = $0
      while (match(line, /\[[^][]+\]\(([^)]+)\)/)) {
        full = substr(line, RSTART, RLENGTH)
        target = full
        sub(/^[^()]*\(/, "", target)
        sub(/\)$/, "", target)
        print NR "\t" target
        line = substr(line, RSTART + RLENGTH)
      }
    }
  ' "$1"
}

extract_markdown_path_mentions() {
  grep -nEo '(\.\.?/|[A-Za-z0-9_-]+/)[A-Za-z0-9_./<>-]+\.md([#?][^[:space:]`)>]*)?' "$1" |
    while IFS=: read -r line_no target; do
      printf '%s\t%s\n' "$line_no" "$target"
    done || true
}

extract_fenced_lines() {
  awk '
    BEGIN {
      in_block = 0
      fence = ""
    }
    {
      stripped = $0
      sub(/^[[:space:]]+/, "", stripped)
      prefix = substr(stripped, 1, 3)
      if (!in_block) {
        if (prefix == "```" || prefix == "~~~") {
          in_block = 1
          fence = prefix
        }
        next
      }
      if (prefix == fence) {
        in_block = 0
        fence = ""
        next
      }
      print NR "\t" $0
    }
  ' "$1"
}

strip_token() {
  local token="$1"
  local first_char last_char
  while [[ -n "$token" ]]; do
    first_char="${token:0:1}"
    case "$first_char" in
      '"'|"'"|'`'|'('|')'|'['|']'|'{'|'}') token="${token:1}" ;;
      *) break ;;
    esac
  done

  while [[ -n "$token" ]]; do
    last_char="${token:${#token}-1:1}"
    case "$last_char" in
      '"'|"'"|'`'|'('|')'|'['|']'|'{'|'}') token="${token%?}" ;;
      *) break ;;
    esac
  done

  printf '%s' "$token"
}

is_allowed_skill_script() {
  local token="$1"
  [[ "$token" == scripts/* || "$token" == ./scripts/* ]]
}

has_script_extension() {
  local lower
  lower="$(to_lower "$1")"
  case "$lower" in
    *.py|*.sh|*.bash|*.zsh|*.js) return 0 ;;
    *) return 1 ;;
  esac
}

is_script_token() {
  local token="$1"
  local previous="$2"
  local lower
  lower="$(to_lower "$token")"

  [[ "$token" == *"/scripts/"* || "$token" == scripts/* || "$token" == ./scripts/* ]] && return 0
  has_script_extension "$token" || return 1
  [[ "$token" == ./* || "$token" == ../* || "$token" == /* ]] && return 0
  [[ -n "$previous" ]] || return 1
  local prev_lower
  prev_lower="$(to_lower "$previous")"
  [[ "$prev_lower" == python* || "$prev_lower" == node || "$prev_lower" == nodejs || "$prev_lower" == bash || "$prev_lower" == sh || "$prev_lower" == zsh ]]
}

check_skill_script_references() {
  local path="$1"
  local line_no line token previous normalized
  while IFS=$'\t' read -r line_no line; do
    [[ -n "${line_no:-}" ]] || continue
    previous=""
    read -r -a tokens <<<"$line"
    for token in "${tokens[@]}"; do
      normalized="$(strip_token "$token")"
      [[ -n "$normalized" ]] || continue
      if is_script_token "$normalized" "$previous" && ! is_allowed_skill_script "$normalized"; then
        add_issue "$path" "$line_no" "Direct script references must stay within the skill's scripts/ directory."
        break
      fi
      previous="$normalized"
    done
  done < <(extract_fenced_lines "$path")
}

check_markdown_links() {
  local skill_dir="$1"
  local path="$2"
  local path_dir raw_target target link_path joined resolved line_no
  path_dir="$(cd "$(dirname "$path")" && pwd -P)"
  while IFS=$'\t' read -r line_no raw_target; do
    target="$(normalize_link_target "$raw_target")"
    should_skip_link_target "$target" && continue
    link_path="$(strip_link_suffix "$target")"
    [[ -n "$link_path" ]] || continue
    if [[ "$link_path" == /* || "$link_path" =~ ^[A-Za-z]: ]]; then
      add_issue "$path" "$line_no" "Markdown links must not use absolute filesystem paths."
      continue
    fi

    joined="$path_dir/$link_path"
    if [[ ! -e "$joined" ]]; then
      add_issue "$path" "$line_no" "Linked file does not exist: $link_path"
      continue
    fi
    resolved="$(canonical_existing_path "$joined")"
    if ! is_within_root "$resolved"; then
      add_issue "$path" "$line_no" "Linked file escapes skill root: $link_path"
    fi
  done < <(extract_markdown_links "$path")
}

classify_skill_layout() {
  local skill_dir="$1"
  local markdown_list="$2"
  local first_body_text
  first_body_text="$(first_body_heading "$skill_dir/SKILL.md")"

  if [[ -f "$skill_dir/README.md" ]]; then
    printf 'multi-step-workflow\n'
    return
  fi
  if [[ -d "$skill_dir/scripts" || -d "$skill_dir/assets" ]]; then
    printf 'multi-step-workflow\n'
    return
  fi
  if [[ -d "$skill_dir/references" ]]; then
    if [[ "$first_body_text" == "# Task" ]]; then
      printf 'simple-task-runbook-index\n'
    else
      printf 'multi-step-workflow\n'
    fi
    return
  fi
  while IFS= read -r path; do
    case "$(basename "$path")" in
      SKILL.md|README.md) ;;
      *)
        if [[ "$first_body_text" == "# Task" ]]; then
          printf 'simple-task-runbook-index\n'
        else
          printf 'multi-step-workflow\n'
        fi
        return
        ;;
    esac
  done <"$markdown_list"
  if [[ "$first_body_text" == "# Guidance" ]]; then
    printf 'behaviour-guidance\n'
  else
    printf 'simple-task-inline\n'
  fi
}

first_body_heading() {
  local path="$1"
  local end_line
  end_line="$(frontmatter_end_line "$path")"
  if [[ -z "$end_line" ]]; then
    printf ''
    return
  fi
  awk -v end_line="$end_line" 'NR > end_line && NF { print; exit }' "$path"
}

check_skill_frontmatter() {
  local skill_dir="$1"
  local path="$2"
  local first_line end_line raw_name raw_description name description

  first_line="$(awk 'NR == 1 { print; exit }' "$path")"
  if [[ "$first_line" != "---" ]]; then
    add_issue "$path" 1 "SKILL.md must start with YAML frontmatter."
    return
  fi

  end_line="$(frontmatter_end_line "$path")"
  if [[ -z "$end_line" ]]; then
    add_issue "$path" 1 "SKILL.md frontmatter missing closing '---'."
    return
  fi

  raw_name="$(extract_frontmatter_field "$path" "name" "$end_line")"
  raw_description="$(extract_frontmatter_field "$path" "description" "$end_line")"
  name="$(strip_quotes "$raw_name")"
  description="$(strip_quotes "$raw_description")"

  if [[ -z "$name" ]]; then
    add_issue "$path" 1 "SKILL.md frontmatter must include 'name'."
  elif ! [[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || [[ ${#name} -gt 64 ]]; then
    add_issue "$path" 1 "Skill name must be 1-64 chars, lowercase alphanumerics and hyphens only."
  elif [[ "$name" != "$(basename "$skill_dir")" ]]; then
    add_issue "$path" 1 "Skill name '$name' must match directory name '$(basename "$skill_dir")'."
  fi

  if [[ -z "$description" ]]; then
    add_issue "$path" 1 "SKILL.md frontmatter must include 'description'."
  elif [[ "$description" != *"USE WHEN"* ]]; then
    add_issue "$path" 1 "Skill description must include an explicit 'USE WHEN ...' clause."
  fi
}

check_skill_line_limit() {
  local path="$1"
  local max_lines="$2"
  local label="$3"
  local line_count
  line_count="$(wc -l <"$path" | tr -d ' ')"
  if [[ "$line_count" -gt "$max_lines" ]]; then
    add_issue "$path" 1 "$label SKILL.md must stay at or under $max_lines lines."
  fi
}

check_first_body_heading() {
  local path="$1"
  local expected="$2"
  local label="$3"
  local end_line first_body_line first_body_text

  end_line="$(frontmatter_end_line "$path")"
  first_body_line="$(awk -v end_line="$end_line" 'NR > end_line && NF { print NR; exit }' "$path")"
  first_body_text="$(awk -v end_line="$end_line" 'NR > end_line && NF { print; exit }' "$path")"
  if [[ -z "$first_body_line" || "$first_body_text" != "$expected" ]]; then
    add_issue "$path" "${first_body_line:-1}" "$label SKILL.md must begin with a '$expected' heading immediately after frontmatter."
  fi
}

check_single_file_route() {
  local skill_dir="$1"
  local markdown_list="$2"
  local label="$3"
  local path
  while IFS= read -r path; do
    [[ "$path" == "$skill_dir/SKILL.md" ]] && continue
    add_issue "$path" 1 "$label skills must only generate SKILL.md."
  done <"$markdown_list"
  [[ ! -d "$skill_dir/references" ]] || add_issue "$skill_dir/references" 1 "$label skills must not include references/."
  [[ ! -d "$skill_dir/assets" ]] || add_issue "$skill_dir/assets" 1 "$label skills must not include assets/."
  [[ ! -d "$skill_dir/scripts" ]] || add_issue "$skill_dir/scripts" 1 "$label skills must not include scripts/."
}

check_simple_runbook_layout() {
  local skill_dir="$1"
  local path="$2"
  check_first_body_heading "$path" "# Task" "Simple task runbook-index"
  check_skill_line_limit "$path" "$COMPACT_SKILL_MAX_LINES" "Simple task runbook-index"
  [[ -d "$skill_dir/references" ]] || add_issue "$path" 1 "Simple task runbook-index skills must include references/ runbooks."
  [[ ! -f "$skill_dir/README.md" ]] || add_issue "$skill_dir/README.md" 1 "Simple task runbook-index skills must not include README.md."
  [[ ! -d "$skill_dir/assets" ]] || add_issue "$skill_dir/assets" 1 "Simple task runbook-index skills must not include assets/."
}

check_skill_structure() {
  local path="$1"
  local end_line first_body_line first_body_text workflow_line output_line result_format_line
  local steps_file step_count idx line_no step_no next_line expected references total_lines last_step_line

  end_line="$(frontmatter_end_line "$path")"
  first_body_line="$(awk -v end_line="$end_line" 'NR > end_line && NF { print NR; exit }' "$path")"
  first_body_text="$(awk -v end_line="$end_line" 'NR > end_line && NF { print; exit }' "$path")"

  if [[ -z "$first_body_line" || "$first_body_text" != "# Workflow" ]]; then
    add_issue "$path" "${first_body_line:-1}" "Structured SKILL.md must begin with a '# Workflow' heading immediately after frontmatter."
    return
  fi
  workflow_line="$first_body_line"

  output_line="$(awk '/^## Output$/ { print NR; exit }' "$path")"
  if [[ -z "$output_line" ]]; then
    add_issue "$path" "$workflow_line" "SKILL.md must include a '## Output' section."
  fi

  result_format_line="$(awk '/^### Result Format$/ { print NR; exit }' "$path")"
  if [[ -z "$result_format_line" ]]; then
    add_issue "$path" "${output_line:-$workflow_line}" "Output section must include a '### Result Format' heading."
  fi

  steps_file="$(mktemp)"
  register_temp_file "$steps_file"
  awk '/^### Step [0-9]+:/ { line = $0; sub(/^### Step /, "", line); sub(/:.*/, "", line); print NR "\t" line }' "$path" >"$steps_file"

  step_count="$(wc -l <"$steps_file" | tr -d ' ')"
  if [[ "$step_count" -eq 0 ]]; then
    add_issue "$path" "$workflow_line" "Workflow section must include numbered '### Step N: ...' headings."
    return
  fi

  idx=0
  while IFS=$'\t' read -r line_no step_no; do
    STEP_LINES[idx]="$line_no"
    STEP_NUMBERS[idx]="$step_no"
    idx=$((idx + 1))
  done <"$steps_file"

  if [[ "${STEP_NUMBERS[0]}" -ne 0 && "${STEP_NUMBERS[0]}" -ne 1 ]]; then
    add_issue "$path" "${STEP_LINES[0]}" "Step numbering must start at 0 or 1."
  fi

  expected="${STEP_NUMBERS[0]}"
  for ((idx = 0; idx < step_count; idx++)); do
    if (( idx > 0 )) && [[ "${STEP_NUMBERS[idx]}" -lt "${STEP_NUMBERS[idx-1]}" ]]; then
      add_issue "$path" "${STEP_LINES[0]}" "Step headings must be sorted in ascending order."
      break
    fi
  done

  for ((idx = 0; idx < step_count; idx++)); do
    if [[ "${STEP_NUMBERS[idx]}" -ne "$expected" ]]; then
      add_issue "$path" "${STEP_LINES[0]}" "Step numbering must be contiguous with no gaps or duplicates."
      break
    fi
    expected=$((expected + 1))
  done

  total_lines="$(wc -l <"$path" | tr -d ' ')"
  for ((idx = 0; idx < step_count; idx++)); do
    line_no="${STEP_LINES[idx]}"
    step_no="${STEP_NUMBERS[idx]}"
    if (( idx + 1 < step_count )); then
      next_line=$((STEP_LINES[idx + 1] - 1))
    else
      next_line="$total_lines"
    fi
    references="$(sed -n "${line_no},${next_line}p" "$path" | { grep -Eo '\[[^]]+\]\(references/[^)#]+\.md(#[^)]*)?\)' || true; } | wc -l | tr -d ' ')"
    if [[ "$references" -ne 1 ]]; then
      add_issue "$path" "$line_no" "Step $step_no must include exactly one reference link to a file under references/."
    fi
  done

  if [[ -n "$output_line" ]]; then
    last_step_line="${STEP_LINES[$((step_count - 1))]}"
    if [[ "$output_line" -le "$last_step_line" ]]; then
      add_issue "$path" "$output_line" "The '## Output' section must appear after all workflow steps."
    fi
  fi
}

check_readme_structure() {
  local skill_dir="$1"
  local path="$2"
  local expected_title first_non_empty headings_file heading_count idx heading_name heading_line

  expected_title="# $(basename "$skill_dir")"
  first_non_empty="$(awk 'NF { print; exit }' "$path")"
  if [[ "$first_non_empty" != "$expected_title" ]]; then
    add_issue "$path" 1 "README.md must start with '$expected_title'."
  fi

  headings_file="$(mktemp)"
  register_temp_file "$headings_file"
  awk '/^## / { print NR "\t" substr($0, 4) }' "$path" >"$headings_file"
  heading_count="$(wc -l <"$headings_file" | tr -d ' ')"

  README_HEADING_LINES=()
  README_HEADING_NAMES=()
  idx=0
  while IFS=$'\t' read -r heading_line heading_name; do
    [[ -n "${heading_line:-}" ]] || continue
    README_HEADING_LINES[idx]="$heading_line"
    README_HEADING_NAMES[idx]="$heading_name"
    case "$heading_name" in
      Overview|When\ to\ use\ it|Example\ prompts|References) ;;
      *) add_issue "$path" "$heading_line" "Unsupported README section '$heading_name'." ;;
    esac
    idx=$((idx + 1))
  done <"$headings_file"

  if (( heading_count < 3 )) || [[ "${README_HEADING_NAMES[0]:-}" != "Overview" || "${README_HEADING_NAMES[1]:-}" != "When to use it" || "${README_HEADING_NAMES[2]:-}" != "Example prompts" ]]; then
    add_issue "$path" 1 "README.md must use the section order: Overview, When to use it, Example prompts."
  fi

  local reference_count=0
  local reference_line=""
  for ((idx = 0; idx < heading_count; idx++)); do
    if [[ "${README_HEADING_NAMES[idx]}" == "References" ]]; then
      reference_count=$((reference_count + 1))
      reference_line="${README_HEADING_LINES[idx]}"
      if (( idx != heading_count - 1 )); then
        add_issue "$path" "$reference_line" "README.md References section must be the final section."
      fi
    fi
  done
  if (( reference_count > 1 )); then
    add_issue "$path" "${reference_line:-1}" "README.md may include at most one References section."
  fi

  ensure_list_items_under_section "$path" "When to use it"
  ensure_list_items_under_section "$path" "Example prompts"
}

ensure_list_items_under_section() {
  local path="$1"
  local section_name="$2"
  local idx start_line end_line section_has_bullet="false"
  local heading_count="${#README_HEADING_NAMES[@]}"

  for ((idx = 0; idx < heading_count; idx++)); do
    if [[ "${README_HEADING_NAMES[idx]}" != "$section_name" ]]; then
      continue
    fi
    start_line="${README_HEADING_LINES[idx]}"
    if (( idx + 1 < heading_count )); then
      end_line=$((README_HEADING_LINES[idx + 1] - 1))
    else
      end_line="$(wc -l <"$path" | tr -d ' ')"
    fi

    while IFS= read -r line; do
      if [[ "$line" =~ ^[[:space:]]*-\  ]]; then
        section_has_bullet="true"
        break
      fi
    done < <(sed -n "${start_line},${end_line}p" "$path")

    if [[ "$section_has_bullet" == "true" ]]; then
      return
    fi
    add_issue "$path" "$start_line" "README.md section '$section_name' must include at least one bullet item."
    return
  done

  add_issue "$path" 1 "README.md is missing required section '$section_name'."
}

check_stale_markdown() {
  local skill_dir="$1"
  local markdown_list="$2"
  local edges_file visited_file path target link_path joined resolved path_dir
  edges_file="$(mktemp)"
  visited_file="$(mktemp)"
  register_temp_file "$edges_file"
  register_temp_file "$visited_file"

  while IFS= read -r path; do
    path_dir="$(cd "$(dirname "$path")" && pwd -P)"
    while IFS=$'\t' read -r _line_no target; do
      target="$(normalize_link_target "$target")"
      should_skip_link_target "$target" && continue
      link_path="$(strip_link_suffix "$target")"
      [[ "$link_path" == *.md ]] || continue
      [[ "$link_path" == /* || "$link_path" =~ ^[A-Za-z]: ]] && continue
      joined="$path_dir/$link_path"
      [[ -e "$joined" ]] || continue
      resolved="$(canonical_existing_path "$joined")"
      is_within_root "$resolved" || continue
      if grep -Fxq "$resolved" "$markdown_list"; then
        printf '%s\t%s\n' "$path" "$resolved" >>"$edges_file"
      fi
    done < <(
      {
        extract_markdown_links "$path"
        extract_markdown_path_mentions "$path"
      } | awk -F '\t' '!seen[$1 FS $2]++'
    )
  done <"$markdown_list"

  printf '%s\n' "$SKILL_MD_ABS" >"$visited_file"
  local changed=1
  while [[ "$changed" -eq 1 ]]; do
    changed=0
    while IFS=$'\t' read -r src dst; do
      [[ -n "${src:-}" && -n "${dst:-}" ]] || continue
      if grep -Fxq "$src" "$visited_file" && ! grep -Fxq "$dst" "$visited_file"; then
        printf '%s\n' "$dst" >>"$visited_file"
        changed=1
      fi
    done <"$edges_file"
  done

  while IFS= read -r path; do
    [[ "$path" == "$SKILL_MD_ABS" ]] && continue
    [[ "$(basename "$path")" == "README.md" ]] && continue
    if ! grep -Fxq "$path" "$visited_file"; then
      add_issue "$path" 1 "Markdown file appears unreachable from SKILL.md; remove it or link it from the workflow chain."
    fi
  done <"$markdown_list"
}

lint_skill_dir() {
  local skill_dir="$1"
  local skill_md="$skill_dir/SKILL.md"
  local readme_md="$skill_dir/README.md"
  local markdown_list layout path

  SKILL_ROOT_ABS="$(cd "$skill_dir" && pwd -P)"
  SKILL_MD_ABS="$SKILL_ROOT_ABS/SKILL.md"

  if [[ ! -f "$skill_md" ]]; then
    add_issue "$skill_md" 1 "Skill directory is missing required SKILL.md entrypoint."
    return
  fi

  markdown_list="$(mktemp)"
  register_temp_file "$markdown_list"
  find "$skill_dir" -type f -name '*.md' ! -path '*/.git/*' | LC_ALL=C sort >"$markdown_list"

  while IFS= read -r path; do
    check_markdown_links "$skill_dir" "$path"
  done <"$markdown_list"

  layout="$(classify_skill_layout "$skill_dir" "$markdown_list")"
  check_skill_frontmatter "$skill_dir" "$skill_md"
  case "$layout" in
    multi-step-workflow)
      [[ -f "$readme_md" ]] || add_issue "$readme_md" 1 "Multi-step workflow skill directory is missing required README.md overview file."
      check_skill_structure "$skill_md"
      ;;
    behaviour-guidance)
      check_first_body_heading "$skill_md" "# Guidance" "Behaviour guidance"
      check_skill_line_limit "$skill_md" "$BEHAVIOUR_GUIDANCE_MAX_LINES" "Behaviour guidance"
      check_single_file_route "$skill_dir" "$markdown_list" "Behaviour guidance"
      ;;
    simple-task-inline)
      check_first_body_heading "$skill_md" "# Task" "Simple task inline"
      check_skill_line_limit "$skill_md" "$COMPACT_SKILL_MAX_LINES" "Simple task inline"
      check_single_file_route "$skill_dir" "$markdown_list" "Simple task inline"
      ;;
    simple-task-runbook-index)
      check_simple_runbook_layout "$skill_dir" "$skill_md"
      ;;
    *)
      add_issue "$skill_md" 1 "Unknown skill layout classification: $layout"
      ;;
  esac

  check_stale_markdown "$skill_dir" "$markdown_list"
  check_skill_script_references "$skill_md"

  if [[ "$layout" == "multi-step-workflow" && -f "$readme_md" ]]; then
    check_readme_structure "$skill_dir" "$readme_md"
  fi
}

parse_args() {
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
  while (($# > 0)); do
    case "$1" in
      --root)
        shift
        [[ $# -gt 0 ]] || { echo "Missing value for --root" >&2; exit 1; }
        REPO_ROOT="$(cd "$1" && pwd -P)"
        shift
        ;;
      *)
        echo "Unknown argument: $1" >&2
        exit 1
        ;;
    esac
  done
}

main() {
  parse_args "$@"

  local skills_root="$REPO_ROOT/skills"
  if [[ ! -d "$skills_root" ]]; then
    echo "skills root not found" >&2
    exit 1
  fi

  local found_skill_dir="false"
  local skill_dir
  while IFS= read -r skill_dir; do
    found_skill_dir="true"
    lint_skill_dir "$skill_dir"
  done < <(find "$skills_root" -mindepth 1 -maxdepth 1 -type d ! -name '.*' | LC_ALL=C sort)

  if [[ "$found_skill_dir" != "true" ]]; then
    add_issue "$skills_root" 1 "No skill directories found under skills/."
  fi

  if [[ -s "$ISSUES_FILE" ]]; then
    while IFS=$'\t' read -r path line message; do
      printf '%s:%s: [error] %s\n' "$(relative_to_root "$path")" "$line" "$message"
    done < <(LC_ALL=C sort -t $'\t' -k1,1 -k2,2n -k3,3 "$ISSUES_FILE")
    exit 1
  fi

  echo "skills: lint passed"
}

main "$@"
