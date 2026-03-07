#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shlex
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

STEP_HEADING = re.compile(r"^### Step (\d+):")
README_HEADING = re.compile(r"^## (Overview|When to use it|Example prompts|References)\s*$")
WORKFLOW_REFERENCE_LINK = re.compile(
    r"\[[^\]]+\]\((references/[^)#]+\.md(?:#[^)]+)?)\)"
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SCHEME_PREFIX = re.compile(r"^(?P<scheme>[A-Za-z][A-Za-z0-9+.\-]*):")
WINDOWS_DRIVE_PREFIX = re.compile(r"^[A-Za-z]:")
SKIPPED_LINK_SCHEMES = {"http", "https", "mailto"}
SCRIPT_EXTENSIONS = (".py", ".sh", ".bash", ".zsh", ".js")
FENCE_PREFIXES = ("```", "~~~")
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
README_EXPECTED_SECTIONS = [
    "Overview",
    "When to use it",
    "Example prompts",
]
README_ALLOWED_SECTIONS = README_EXPECTED_SECTIONS + ["References"]


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lint skill directories for createfuture opinionated structure."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to lint.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.root.resolve()
    skills_root = repo_root / "skills"

    if not skills_root.is_dir():
        print("skills root not found", file=sys.stderr)
        return 1

    issues = lint_repository(skills_root)
    if issues:
        for issue in sorted(issues, key=lambda item: (item.path.as_posix(), item.line, item.message)):
            print(f"{issue.path.relative_to(repo_root)}:{issue.line}: [error] {issue.message}")
        return 1

    print("skills: lint passed")
    return 0


def lint_repository(skills_root: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_dirs = sorted(
        path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not skill_dirs:
        issues.append(Issue(skills_root, 1, "No skill directories found under skills/."))
        return issues

    for skill_dir in skill_dirs:
        issues.extend(lint_skill_dir(skill_dir))
    return issues


def lint_skill_dir(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_md = skill_dir / "SKILL.md"
    readme_md = skill_dir / "README.md"

    if not skill_md.exists():
        issues.append(Issue(skill_md, 1, "Skill directory is missing required SKILL.md entrypoint."))
        return issues
    if not readme_md.exists():
        issues.append(Issue(readme_md, 1, "Skill directory is missing required README.md overview file."))

    markdown_files = sorted(
        path for path in skill_dir.rglob("*.md") if ".git" not in path.parts
    )
    for markdown_file in markdown_files:
        content = markdown_file.read_text(encoding="utf-8")
        issues.extend(check_markdown_links(skill_dir, markdown_file, content))

    skill_content = skill_md.read_text(encoding="utf-8")
    issues.extend(check_skill_frontmatter(skill_dir, skill_md, skill_content))
    issues.extend(check_skill_structure(skill_dir, skill_md, skill_content))
    issues.extend(check_stale_markdown(skill_dir, markdown_files))
    issues.extend(check_skill_script_references(skill_dir, skill_md, skill_content))

    if readme_md.exists():
        readme_content = readme_md.read_text(encoding="utf-8")
        issues.extend(check_readme_structure(skill_dir, readme_md, readme_content))

    return issues


def check_skill_frontmatter(skill_dir: Path, path: Path, content: str) -> list[Issue]:
    issues: list[Issue] = []
    frontmatter, _body, error = split_frontmatter(content)
    if error:
        return [Issue(path, 1, error)]

    fields = parse_frontmatter_scalars(frontmatter)
    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()

    if not name:
        issues.append(Issue(path, 1, "SKILL.md frontmatter must include 'name'."))
    elif not NAME_PATTERN.match(name) or len(name) > 64:
        issues.append(
            Issue(
                path,
                1,
                "Skill name must be 1-64 chars, lowercase alphanumerics and hyphens only.",
            )
        )
    elif name != skill_dir.name:
        issues.append(
            Issue(path, 1, f"Skill name '{name}' must match directory name '{skill_dir.name}'.")
        )

    if not description:
        issues.append(Issue(path, 1, "SKILL.md frontmatter must include 'description'."))
    elif "USE WHEN" not in description:
        issues.append(
            Issue(path, 1, "Skill description must include an explicit 'USE WHEN ...' clause.")
        )

    return issues


def check_skill_structure(skill_dir: Path, path: Path, content: str) -> list[Issue]:
    issues: list[Issue] = []
    _frontmatter, body, error = split_frontmatter(content)
    if error:
        return issues

    if "## Workflow" not in body:
        issues.append(Issue(path, 1, "SKILL.md must include a '## Workflow' section."))
        return issues

    step_rows: list[tuple[int, int]] = []
    for line_no, line in enumerate(body.splitlines(), start=1):
        match = STEP_HEADING.match(line.strip())
        if match:
            step_rows.append((line_no, int(match.group(1))))

    if not step_rows:
        issues.append(
            Issue(path, line_for_text(body, "## Workflow"), "Workflow section must include numbered '### Step N: ...' headings.")
        )
        return issues

    numbers = [number for _, number in step_rows]
    if numbers != sorted(numbers):
        issues.append(Issue(path, step_rows[0][0], "Step headings must be sorted in ascending order."))
    if numbers[0] not in (0, 1):
        issues.append(Issue(path, step_rows[0][0], "Step numbering must start at 0 or 1."))
    expected = list(range(numbers[0], numbers[0] + len(numbers)))
    if numbers != expected:
        issues.append(
            Issue(path, step_rows[0][0], "Step numbering must be contiguous with no gaps or duplicates.")
        )

    for line_no, step_number, section_lines in iter_step_sections(body):
        ref_links: list[str] = []
        for line in section_lines:
            ref_links.extend(match.group(1) for match in WORKFLOW_REFERENCE_LINK.finditer(line))
        if len(ref_links) != 1:
            issues.append(
                Issue(
                    path,
                    line_no,
                    f"Step {step_number} must include exactly one reference link to a file under references/.",
                )
            )

    issues.extend(check_skill_script_references(skill_dir, path, content))
    return issues


def check_readme_structure(skill_dir: Path, path: Path, content: str) -> list[Issue]:
    issues: list[Issue] = []
    lines = content.splitlines()
    non_empty = [line for line in lines if line.strip()]
    expected_title = f"# {skill_dir.name}"
    if not non_empty or non_empty[0].strip() != expected_title:
        issues.append(Issue(path, 1, f"README.md must start with '{expected_title}'."))

    headings: list[tuple[int, str]] = []
    for line_no, line in enumerate(lines, start=1):
        match = README_HEADING.match(line.strip())
        if match:
            headings.append((line_no, match.group(1)))

    found_sections = [heading for _, heading in headings]
    if found_sections[: len(README_EXPECTED_SECTIONS)] != README_EXPECTED_SECTIONS:
        issues.append(
            Issue(
                path,
                1,
                "README.md must use the section order: Overview, When to use it, Example prompts.",
            )
        )

    for line_no, heading in headings:
        if heading not in README_ALLOWED_SECTIONS:
            issues.append(Issue(path, line_no, f"Unsupported README section '{heading}'."))

    if found_sections.count("References") > 1:
        issues.append(Issue(path, headings[-1][0], "README.md may include at most one References section."))
    if "References" in found_sections and found_sections[-1] != "References":
        ref_line = next(line_no for line_no, heading in headings if heading == "References")
        issues.append(Issue(path, ref_line, "README.md References section must be the final section."))

    issues.extend(ensure_list_items_under_section(path, lines, headings, "When to use it"))
    issues.extend(ensure_list_items_under_section(path, lines, headings, "Example prompts"))
    return issues


def ensure_list_items_under_section(
    path: Path, lines: list[str], headings: list[tuple[int, str]], section_name: str
) -> list[Issue]:
    for index, (line_no, heading) in enumerate(headings):
        if heading != section_name:
            continue
        start = line_no
        end = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
        section_lines = lines[start:end]
        if any(line.lstrip().startswith("- ") for line in section_lines):
            return []
        return [Issue(path, line_no, f"README.md section '{section_name}' must include at least one bullet item.")]
    return [Issue(path, 1, f"README.md is missing required section '{section_name}'.")]


def check_markdown_links(skill_dir: Path, path: Path, content: str) -> list[Issue]:
    issues: list[Issue] = []
    for line_no, target in iter_markdown_links(content):
        issue = validate_markdown_link(skill_dir, path, line_no, target)
        if issue is not None:
            issues.append(issue)
    return issues


def validate_markdown_link(skill_dir: Path, path: Path, line_no: int, target: str) -> Issue | None:
    link_path = strip_link_suffix(target)
    if not link_path:
        return None
    if WINDOWS_DRIVE_PREFIX.match(link_path) or link_path.startswith("/"):
        return Issue(path, line_no, "Markdown links must not use absolute filesystem paths.")

    resolved = (path.parent / link_path).resolve()
    if not resolved.exists():
        return Issue(path, line_no, f"Linked file does not exist: {link_path}")
    if not resolved.is_relative_to(skill_dir.resolve()):
        return Issue(path, line_no, f"Linked file escapes skill root: {link_path}")
    return None


def check_stale_markdown(skill_dir: Path, markdown_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    skill_md = (skill_dir / "SKILL.md").resolve()
    loaded = {path.resolve(): path.read_text(encoding="utf-8") for path in markdown_files}
    adjacency: dict[Path, set[Path]] = defaultdict(set)

    for path, content in loaded.items():
        for _line_no, target in iter_markdown_links(content):
            resolved = resolve_markdown_target(path, target)
            if resolved and resolved in loaded and resolved.is_relative_to(skill_dir.resolve()):
                adjacency[path].add(resolved)

    reachable: set[Path] = set()
    queue: deque[Path] = deque([skill_md])
    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)
        for nxt in adjacency.get(current, set()):
            if nxt not in reachable:
                queue.append(nxt)

    for path in sorted(loaded):
        if path == skill_md or path.name == "README.md":
            continue
        if path in reachable:
            continue
        issues.append(
            Issue(
                path,
                1,
                "Markdown file appears unreachable from SKILL.md; remove it or link it from the workflow chain.",
            )
        )
    return issues


def check_skill_script_references(skill_dir: Path, path: Path, content: str) -> list[Issue]:
    issues: list[Issue] = []
    for line_no, line in iter_fenced_lines(content):
        tokens = tokenize_line(line)
        for index, token in enumerate(tokens):
            previous = tokens[index - 1] if index > 0 else None
            if not is_script_token(token, previous):
                continue
            if is_allowed_skill_script(token):
                continue
            issues.append(
                Issue(
                    path,
                    line_no,
                    "Direct script references must stay within the skill's scripts/ directory.",
                )
            )
            break
    return issues


def split_frontmatter(content: str) -> tuple[str, str, str | None]:
    if not content.startswith("---"):
        return "", content, "SKILL.md must start with YAML frontmatter."
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", content, "SKILL.md frontmatter must start with '---'."
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = "\n".join(lines[: index + 1]).rstrip() + "\n"
            body = "\n".join(lines[index + 1 :]).lstrip("\n")
            return frontmatter, body, None
    return "", content, "SKILL.md frontmatter missing closing '---'."


def parse_frontmatter_scalars(frontmatter: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in frontmatter.splitlines()[1:-1]:
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            continue
        if ":" not in raw_line:
            continue
        key, raw_value = raw_line.split(":", 1)
        value = raw_value.strip()
        if not value:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        fields[key.strip()] = value
    return fields


def iter_step_sections(body: str) -> list[tuple[int, int, list[str]]]:
    lines = body.splitlines()
    step_rows: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = STEP_HEADING.match(line.strip())
        if match:
            step_rows.append((index, int(match.group(1))))

    sections: list[tuple[int, int, list[str]]] = []
    for offset, (start_index, step_number) in enumerate(step_rows):
        end_index = len(lines)
        if offset + 1 < len(step_rows):
            end_index = step_rows[offset + 1][0]
        sections.append((start_index + 1, step_number, lines[start_index + 1 : end_index]))
    return sections


def line_for_text(content: str, needle: str) -> int:
    for line_no, line in enumerate(content.splitlines(), start=1):
        if needle in line:
            return line_no
    return 1


def iter_markdown_links(content: str) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    for line_no, line in enumerate(content.splitlines(), start=1):
        for match in MARKDOWN_LINK.finditer(line):
            target = normalize_link_target(match.group(1).strip())
            if should_skip_link_target(target):
                continue
            links.append((line_no, target))
    return links


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    try:
        parts = shlex.split(target)
    except ValueError:
        parts = target.split()
    return parts[0] if parts else ""


def should_skip_link_target(target: str) -> bool:
    if not target or target.startswith("#"):
        return True
    if WINDOWS_DRIVE_PREFIX.match(target):
        return False
    match = SCHEME_PREFIX.match(target)
    return bool(match and match.group("scheme").lower() in SKIPPED_LINK_SCHEMES)


def strip_link_suffix(target: str) -> str:
    without_anchor = target.split("#", maxsplit=1)[0]
    return without_anchor.split("?", maxsplit=1)[0]


def resolve_markdown_target(path: Path, target: str) -> Path | None:
    link_path = strip_link_suffix(target)
    if not link_path:
        return None
    resolved = (path.parent / link_path).resolve()
    if resolved.suffix.lower() != ".md":
        return None
    return resolved


def iter_fenced_lines(content: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    in_block = False
    fence = ""
    for line_no, line in enumerate(content.splitlines(), start=1):
        stripped = line.lstrip()
        if not in_block:
            if stripped.startswith(FENCE_PREFIXES):
                in_block = True
                fence = stripped[:3]
            continue
        if stripped.startswith(fence):
            in_block = False
            fence = ""
            continue
        rows.append((line_no, line))
    return rows


def tokenize_line(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return []
    try:
        return shlex.split(stripped)
    except ValueError:
        return stripped.split()


def is_script_token(token: str, previous_token: str | None) -> bool:
    normalized = token.strip().strip("\"'`()[]{}")
    if "/scripts/" in normalized or normalized.startswith(("scripts/", "./scripts/")):
        return True
    lower = normalized.lower()
    if not lower.endswith(SCRIPT_EXTENSIONS):
        return False
    if normalized.startswith(("./", "../", "/")):
        return True
    if previous_token is None:
        return False
    prev = previous_token.strip().strip("\"'`()[]{}").lower()
    return prev.startswith("python") or prev in {"node", "nodejs", "bash", "sh", "zsh"}


def is_allowed_skill_script(token: str) -> bool:
    normalized = token.strip().strip("\"'`()[]{}")
    return normalized.startswith("scripts/") or normalized.startswith("./scripts/")


if __name__ == "__main__":
    raise SystemExit(main())
