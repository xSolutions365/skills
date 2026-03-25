"""Shared parsing helpers for create-execplan Python utilities."""

from __future__ import annotations

import re

HEADING_PATTERN = re.compile(r"^#{1,6}\s+")
PLACEHOLDER_PATTERN = re.compile(r"<[^>]+>")
REQ_ID_PATTERN = re.compile(r"^R\d+$")
TASK_REF_PATTERN = re.compile(r"^P\d+-T\d+$")
ANCHOR_PATTERN = re.compile(r"[^`\s]+:\d+$")

NA_VALUES = {"", "n/a", "na", "none", "not applicable"}


def lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").split("\n")


def read_section(source: str, heading: str) -> str:
    all_lines = lines(source)
    start_index = -1
    for index, line in enumerate(all_lines):
        if line.strip() == heading:
            start_index = index
            break
    if start_index == -1:
        return ""

    end_index = len(all_lines)
    for index in range(start_index + 1, len(all_lines)):
        if HEADING_PATTERN.match(all_lines[index].strip()):
            end_index = index
            break

    return "\n".join(all_lines[start_index + 1 : end_index]).strip()


def read_bullet_items(section: str) -> list[str]:
    items: list[str] = []
    for line in lines(section):
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def normalize_cell(value: str) -> str:
    return value.strip()


def strip_code_markers(value: str) -> str:
    stripped = value.strip()
    if stripped.startswith("`") and stripped.endswith("`") and len(stripped) >= 2:
        return stripped[1:-1].strip()
    return stripped


def parse_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    table_lines = [
        line.strip()
        for line in lines(section)
        if line.strip().startswith("|") and line.strip().endswith("|")
    ]
    if len(table_lines) < 3:
        return [], []

    headers = [normalize_cell(cell) for cell in table_lines[0][1:-1].split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[1:]:
        if re.fullmatch(r"(\|[\s:-]+)+\|", line):
            continue
        values = [normalize_cell(cell) for cell in line[1:-1].split("|")]
        while len(values) < len(headers):
            values.append("")
        rows.append(dict(zip(headers, values, strict=False)))
    return headers, rows


def is_na(value: str) -> bool:
    return strip_code_markers(value).lower() in NA_VALUES


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped == "" or bool(PLACEHOLDER_PATTERN.search(stripped))


def split_csv_tokens(raw: str) -> list[str]:
    if is_na(raw):
        return []
    tokens: list[str] = []
    for token in raw.split(","):
        normalized = strip_code_markers(token)
        if normalized and not is_na(normalized):
            tokens.append(normalized)
    return tokens


def parse_requirements(section: str) -> list[dict[str, str]]:
    requirements: list[dict[str, str]] = []
    for item in read_bullet_items(section):
        match = re.match(r"^(R\d+):\s*(.*)$", item)
        if match:
            requirements.append({"id": match.group(1), "text": match.group(2).strip()})
    return requirements


def task_ref(phase_number: int, task_number: int) -> str:
    return f"P{phase_number}-T{task_number}"


def normalize_status(raw: str) -> str:
    stripped = raw.strip()
    if stripped == "@":
        return "in_progress"
    if stripped == "X":
        return "complete"
    return "outstanding"
