#!/usr/bin/env python3
"""Build engagement-report Markdown and standalone HTML from period notes."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import mimetypes
import re
import shutil
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
MILESTONE_WORDS = re.compile(
    r"\b(sow|statement of work|release|milestone|launch|go-live|deadline|"
    r"phase|kick[ -]?off|start(?:s|ed)?|end(?:s|ed)?)\b",
    re.IGNORECASE,
)
ISO_DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
EXPLICIT_EVENT = re.compile(
    r"^\s*[-*]\s*(20\d{2}-\d{2}-\d{2})\s*\|\s*([^|]+?)"
    r"(?:\s*\|\s*([a-z0-9-]+))?\s*$",
    re.IGNORECASE,
)
MARKDOWN_IMAGE = re.compile(
    r"!\[([^\]]*)\]\(\s*(?:<([^>]+)>|([^\s)]+))"
    r"(?:\s+[\"']([^\"']+)[\"'])?\s*\)"
)


@dataclass(frozen=True)
class TimelineEvent:
    event_date: str
    label: str
    event_type: str = "milestone"

    def as_dict(self) -> dict[str, str]:
        return {"date": self.event_date, "label": self.label, "type": self.event_type}


@dataclass
class ReportImage:
    caption: str
    alt: str
    kind: str
    source: str
    remote: bool
    markdown_path: str = ""
    src: str = ""
    local_path: str = ""

    def as_dict(self) -> dict[str, object]:
        return {
            "caption": self.caption,
            "alt": self.alt,
            "kind": self.kind,
            "source": self.source,
            "remote": self.remote,
            "src": self.src,
        }


@dataclass
class Evidence:
    events: list[TimelineEvent] = field(default_factory=list)
    images: list[ReportImage] = field(default_factory=list)
    rejected_images: list[str] = field(default_factory=list)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("name must contain at least one letter or number")
    return slug


def parse_iso(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"invalid ISO date: {value}") from exc


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def infer_event_type(label: str, supplied: str = "") -> str:
    if supplied:
        return slugify(supplied)
    lowered = label.lower()
    if "statement of work" in lowered or re.search(r"\bsow\b", lowered):
        if re.search(r"\b(end|ends|ending|expiry|expires)\b", lowered):
            return "sow-end"
        if re.search(r"\b(start|starts|starting|effective)\b", lowered):
            return "sow-start"
        return "sow"
    for event_type, pattern in (
        ("release", r"\brelease\b"),
        ("launch", r"\b(launch|go-live)\b"),
        ("deadline", r"\bdeadline\b"),
        ("phase", r"\bphase\b"),
        ("milestone", r"\bmilestone\b"),
        ("kickoff", r"\bkick[ -]?off\b"),
    ):
        if re.search(pattern, lowered):
            return event_type
    return "milestone"


def clean_event_label(line: str, event_date: str) -> str:
    label = re.sub(r"^\s*[-*]\s*", "", line).strip()
    label = re.sub(rf"\b{re.escape(event_date)}\b", "", label)
    label = re.sub(r"\s+", " ", label).strip(" .:;|-\t")
    label = re.sub(r"\s+\b(?:on|at|by)\b$", "", label, flags=re.IGNORECASE)
    return label or "Milestone"


def table_events(lines: list[str]) -> list[TimelineEvent]:
    events: list[TimelineEvent] = []
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        lowered = [cell.lower() for cell in cells]
        if "date" not in lowered or not any(value in lowered for value in ("event", "milestone")):
            continue
        date_index = lowered.index("date")
        event_index = lowered.index("event") if "event" in lowered else lowered.index("milestone")
        type_index = lowered.index("type") if "type" in lowered else None
        for row in lines[index + 2 :]:
            if not row.lstrip().startswith("|"):
                break
            values = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if max(date_index, event_index) >= len(values):
                continue
            event_date = values[date_index]
            label = values[event_index]
            supplied_type = values[type_index] if type_index is not None and type_index < len(values) else ""
            try:
                parse_iso(event_date)
            except ValueError:
                continue
            if label:
                events.append(TimelineEvent(event_date, label, infer_event_type(label, supplied_type)))
    return events


def extract_events(markdown: str) -> list[TimelineEvent]:
    lines = markdown.splitlines()
    events = table_events(lines)
    explicit_lines: set[int] = set()
    for index, line in enumerate(lines):
        match = EXPLICIT_EVENT.match(line)
        if not match:
            continue
        event_date, label, supplied_type = match.groups()
        parse_iso(event_date)
        events.append(TimelineEvent(event_date, label.strip(), infer_event_type(label, supplied_type or "")))
        explicit_lines.add(index)
    for index, line in enumerate(lines):
        if index in explicit_lines or "|" in line or not MILESTONE_WORDS.search(line):
            continue
        matches = ISO_DATE.findall(line)
        if len(matches) != 1:
            continue
        event_date = matches[0]
        parse_iso(event_date)
        label = clean_event_label(line, event_date)
        events.append(TimelineEvent(event_date, label, infer_event_type(label)))
    deduped: dict[tuple[str, str], TimelineEvent] = {}
    for event in events:
        key = (event.event_date, re.sub(r"\W+", "", event.label).lower())
        deduped.setdefault(key, event)
    return sorted(deduped.values(), key=lambda item: (item.event_date, item.label.lower()))


def image_kind(caption: str, path: str) -> str:
    value = f"{caption} {path}".lower()
    return "progress" if re.search(r"burn(?:down|up)|progress|release|plan|roadmap|velocity", value) else "supporting"


def resolve_local_image(raw_target: str, source: Path, period: Path) -> Path | None:
    target = unquote(raw_target.split("#", 1)[0].split("?", 1)[0])
    parsed = urlparse(target)
    if parsed.scheme or Path(target).is_absolute():
        return None
    candidates = (source.parent / target, period / target)
    period_root = period.resolve()
    for candidate in candidates:
        try:
            resolved = candidate.resolve(strict=True)
        except FileNotFoundError:
            continue
        if (
            resolved.is_file()
            and resolved.suffix.lower() in IMAGE_SUFFIXES
            and is_within(resolved, period_root)
        ):
            return resolved
    return None


def copy_image(source: Path, period: Path) -> tuple[str, str]:
    content = source.read_bytes()
    destination_dir = period / "assets" / "report"
    destination_dir.mkdir(parents=True, exist_ok=True)
    if source.parent.resolve() == destination_dir.resolve():
        destination = source
    else:
        digest = hashlib.sha256(content).hexdigest()[:10]
        safe_stem = slugify(source.stem)
        destination = destination_dir / f"{safe_stem}-{digest}{source.suffix.lower()}"
        if not destination.exists():
            shutil.copyfile(source, destination)
    mime = "image/svg+xml" if source.suffix.lower() == ".svg" else (
        mimetypes.guess_type(source.name)[0] or "application/octet-stream"
    )
    data_uri = f"data:{mime};base64,{base64.b64encode(content).decode('ascii')}"
    return destination.relative_to(period).as_posix(), data_uri


def extract_images(markdown: str, source: Path, period: Path) -> tuple[list[ReportImage], list[str]]:
    images: list[ReportImage] = []
    rejected: list[str] = []
    for match in MARKDOWN_IMAGE.finditer(markdown):
        alt, angle_target, plain_target, title = match.groups()
        target = angle_target or plain_target or ""
        caption = (title or alt or Path(target).stem.replace("-", " ")).strip()
        parsed = urlparse(target)
        if parsed.scheme == "https" and parsed.netloc:
            images.append(
                ReportImage(
                    caption=caption,
                    alt=alt or caption,
                    kind=image_kind(caption, target),
                    source=target,
                    remote=True,
                    src=target,
                )
            )
            continue
        if parsed.scheme:
            rejected.append(f"{source.relative_to(period)}: unsupported image URL {target}")
            continue
        resolved = resolve_local_image(target, source, period)
        if resolved is None:
            rejected.append(f"{source.relative_to(period)}: unsafe or missing image {target}")
            continue
        markdown_path, data_uri = copy_image(resolved, period)
        images.append(ReportImage(
            caption=caption,
            alt=alt or caption,
            kind=image_kind(caption, target),
            source=markdown_path,
            remote=False,
            markdown_path=markdown_path,
            src=data_uri,
            local_path=str(resolved),
        ))
    return images, rejected


def discover_attachment_images(notes: Path, referenced: set[Path]) -> list[Path]:
    found: list[Path] = []
    if not notes.exists():
        return found
    for path in sorted(notes.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        if path.resolve() in referenced:
            continue
        relative_parts = [part.lower() for part in path.relative_to(notes).parts[:-1]]
        if any(part in {"assets", "images"} for part in relative_parts):
            found.append(path.resolve())
    return found


def collect_evidence(period: Path, report: Path | None = None) -> Evidence:
    evidence = Evidence()
    notes = period / "notes"
    sources = sorted(notes.rglob("*.md")) if notes.exists() else []
    if report and report.exists():
        sources.append(report)
    referenced_local: set[Path] = set()
    for source in sources:
        markdown = source.read_text(encoding="utf-8")
        evidence.events.extend(extract_events(markdown))
        images, rejected = extract_images(markdown, source, period)
        evidence.images.extend(images)
        evidence.rejected_images.extend(rejected)
        referenced_local.update(Path(item.local_path).resolve() for item in images if not item.remote)
    for attachment in discover_attachment_images(notes, referenced_local):
        markdown_path, data_uri = copy_image(attachment, period)
        caption = attachment.stem.replace("-", " ").replace("_", " ").strip().title()
        evidence.images.append(ReportImage(
            caption=caption,
            alt=caption,
            kind=image_kind(caption, attachment.name),
            source=markdown_path,
            remote=False,
            markdown_path=markdown_path,
            src=data_uri,
            local_path=str(attachment),
        ))
    event_map: dict[tuple[str, str], TimelineEvent] = {}
    for event in evidence.events:
        key = (event.event_date, re.sub(r"\W+", "", event.label).lower())
        event_map.setdefault(key, event)
    evidence.events = sorted(event_map.values(), key=lambda item: (item.event_date, item.label.lower()))
    image_map: dict[str, ReportImage] = {}
    for image in evidence.images:
        key = image.source if image.remote else hashlib.sha256(Path(image.local_path).read_bytes()).hexdigest()
        image_map.setdefault(key, image)
    evidence.images = list(image_map.values())
    return evidence


def section_body(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"(?ms)^# {re.escape(heading)}\s*\n(.*?)(?=^# |\Z)"
    )
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def replace_section(markdown: str, heading: str, body: str) -> str:
    replacement = f"# {heading}\n\n{body.strip()}\n\n" if body.strip() else f"# {heading}\n\n"
    pattern = re.compile(rf"(?ms)^# {re.escape(heading)}\s*\n.*?(?=^# |\Z)")
    if pattern.search(markdown):
        return pattern.sub(replacement, markdown).rstrip() + "\n"
    return markdown.rstrip() + "\n\n" + replacement


def render_plan_visual(images: list[ReportImage]) -> str:
    rows: list[str] = []
    for image in images:
        if image.remote:
            rows.append(f"- [{image.caption}]({image.source}) — remote image reference; not embedded")
        else:
            escaped_caption = image.caption.replace('"', "'")
            rows.append(f'![{image.alt}]({image.markdown_path} "{escaped_caption}")')
    return "\n\n".join(rows)


def render_timeline(events: list[TimelineEvent]) -> str:
    if not events:
        return ""
    rows = ["| Date | Event | Type |", "| --- | --- | --- |"]
    rows.extend(
        f"| {event.event_date} | {event.label.replace('|', '&#124;')} | {event.event_type} |"
        for event in events
    )
    return "\n".join(rows)


def frontmatter(markdown: str) -> dict[str, str]:
    if not markdown.startswith("---\n"):
        return {}
    end = markdown.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in markdown[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("\"'")
    return values


def table_rows(body: str) -> list[list[str]]:
    rows = []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def bullets(body: str) -> list[str]:
    return [match.group(1).strip() for line in body.splitlines() if (match := re.match(r"\s*[-*]\s+(.+)", line))]


def subsections(body: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^## (.+)\n", body))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        result[match.group(1).strip()] = body[match.end() : end].strip()
    return result


def parse_report_data(markdown: str, evidence: Evidence, period: Path) -> dict[str, object]:
    metadata = frontmatter(markdown)
    overall = [
        {"dimension": row[0], "status": row[1], "detail": row[2]}
        for row in table_rows(section_body(markdown, "Overall"))
        if len(row) >= 3
    ]
    key_sections = subsections(section_body(markdown, "Key points"))
    action_sections = subsections(section_body(markdown, "Actions"))
    raids = [
        {"type": row[0], "category": row[1], "raised": row[2], "detail": row[3], "next_steps": row[4]}
        for row in table_rows(section_body(markdown, "Key RAIDs"))
        if len(row) >= 5
    ]
    casting = [
        {"who": row[0], "role": row[1], "grade": row[2], "start": row[3], "end": row[4], "notes": row[5]}
        for row in table_rows(section_body(markdown, "Casting"))
        if len(row) >= 6
    ]
    local_images = [image for image in evidence.images if not image.remote]
    return {
        "engagement": metadata.get("engagement", ""),
        "period_start": metadata.get("period_start", ""),
        "period_end": metadata.get("period_end", ""),
        "team_leadership": metadata.get("team_leadership", ""),
        "client_logo": embed_optional_asset(metadata.get("client_logo", ""), period),
        "overall": overall,
        "key_points": {
            "delivered": bullets(key_sections.get("Value delivered this period", "")),
            "next": bullets(key_sections.get("Decisions for next period", "")),
        },
        "plan_visual": local_images[0].src if len(local_images) == 1 else None,
        "plan_visuals": [image.as_dict() for image in evidence.images],
        "actions": [{"owner": owner, "items": bullets(body)} for owner, body in action_sections.items()],
        "raids": raids,
        "casting": casting,
        "timeline": [event.as_dict() for event in evidence.events],
    }


def embed_optional_asset(value: str, period: Path) -> str:
    if not value or value.startswith("data:image/"):
        return value
    resolved = resolve_local_image(value, period / "_report.md", period)
    if resolved is None:
        return ""
    content = resolved.read_bytes()
    mime = "image/svg+xml" if resolved.suffix.lower() == ".svg" else (
        mimetypes.guess_type(resolved.name)[0] or "application/octet-stream"
    )
    return f"data:{mime};base64,{base64.b64encode(content).decode('ascii')}"


def safe_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2).replace("<", "\\u003c")


def render_presentation(markdown: str, evidence: Evidence, output: Path) -> None:
    template = Path(__file__).resolve().parent.parent / "assets" / "templates" / "presentation-template.html"
    report_json = safe_json(parse_report_data(markdown, evidence, output.parent))
    output.write_text(template.read_text(encoding="utf-8").replace("__REPORT_JSON__", report_json), encoding="utf-8")


def create_report(period: Path, engagement: str, period_start: str, period_end: str) -> Path:
    template = Path(__file__).resolve().parent.parent / "assets" / "templates" / "report-template.md"
    report = period / f"{engagement}-{period_start}_{period_end}-report.md"
    if not report.exists():
        content = template.read_text(encoding="utf-8")
        content = content.replace("{{ engagement }}", engagement.replace("-", " ").title())
        content = content.replace("{{ period_start }}", period_start).replace("{{ period_end }}", period_end)
        report.write_text(content, encoding="utf-8")
    return report


def update_period(period: Path, engagement: str | None = None) -> dict[str, object]:
    period = period.resolve()
    if not period.is_dir():
        raise ValueError(f"period directory does not exist: {period}")
    match = re.fullmatch(r"(20\d{2}-\d{2}-\d{2})_(20\d{2}-\d{2}-\d{2})", period.name)
    if not match:
        raise ValueError("period directory must be named YYYY-MM-DD_YYYY-MM-DD")
    period_start, period_end = match.groups()
    if parse_iso(period_start) > parse_iso(period_end):
        raise ValueError("period start must not be after period end")
    engagement_slug = engagement or period.parent.name
    reports = sorted(period.glob("*-report.md"))
    report = reports[0] if reports else create_report(period, engagement_slug, period_start, period_end)
    evidence = collect_evidence(period, report)
    markdown = report.read_text(encoding="utf-8")
    markdown = replace_section(markdown, "Plan visual", render_plan_visual(evidence.images))
    markdown = replace_section(markdown, "Timeline", render_timeline(evidence.events))
    report.write_text(markdown, encoding="utf-8")
    presentation = period / report.name.replace("-report.md", "-presentation.html")
    render_presentation(markdown, evidence, presentation)
    return {
        "report": str(report),
        "presentation": str(presentation),
        "timeline_events": len(evidence.events),
        "images": len(evidence.images),
        "rejected_images": evidence.rejected_images,
    }


def add_engagement(repo: Path, name: str) -> dict[str, str]:
    repo = repo.resolve()
    if not repo.is_dir():
        raise ValueError(f"report repository does not exist: {repo}")
    slug = slugify(name)
    engagement = repo / slug
    engagement.mkdir(exist_ok=True)
    readme = engagement / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {name.strip()}\n\n"
            "Reporting periods use `YYYY-MM-DD_YYYY-MM-DD/` directories. "
            "Place source material in each period's `notes/` tree.\n",
            encoding="utf-8",
        )
    return {"engagement": slug, "path": str(engagement)}


def generate_period(repo: Path, engagement: str, period_start: str, period_end: str) -> dict[str, object]:
    start = parse_iso(period_start)
    end = parse_iso(period_end)
    if start > end:
        raise ValueError("period start must not be after period end")
    slug = slugify(engagement)
    engagement_dir = repo.resolve() / slug
    engagement_dir.mkdir(parents=True, exist_ok=True)
    period = engagement_dir / f"{period_start}_{period_end}"
    (period / "notes" / "processed").mkdir(parents=True, exist_ok=True)
    return update_period(period, slug)


def parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add-engagement", help="create an engagement directory")
    add.add_argument("--repo", type=Path, required=True)
    add.add_argument("--name", required=True)
    generate = commands.add_parser("generate", help="create or refresh a reporting period")
    generate.add_argument("--repo", type=Path, required=True)
    generate.add_argument("--engagement", required=True)
    generate.add_argument("--period-start", required=True)
    generate.add_argument("--period-end", required=True)
    update = commands.add_parser("update", help="refresh an existing reporting period")
    update.add_argument("--period", type=Path, required=True)
    return cli


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "add-engagement":
            result = add_engagement(args.repo, args.name)
        elif args.command == "generate":
            result = generate_period(args.repo, args.engagement, args.period_start, args.period_end)
        else:
            result = update_period(args.period)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    for warning in result.get("rejected_images", []):
        print(f"warning: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
