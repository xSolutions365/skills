#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or verify the skills count badge payload."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the existing badge payload is out of date.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.root.resolve()
    skills_root = repo_root / "skills"
    output_path = repo_root / "badges" / "skills-count.json"

    skill_count = count_skills(skills_root)
    payload = {
        "schemaVersion": 1,
        "label": "skills",
        "message": str(skill_count),
        "color": "2ea44f",
    }
    rendered = json.dumps(payload, indent=2) + "\n"

    if args.check:
        if not output_path.exists():
            print(f"Missing badge payload: {output_path}", file=sys.stderr)
            return 1
        current = output_path.read_text(encoding="utf-8")
        if current != rendered:
            print(
                "skills count badge payload is out of date; run scripts/update_skills_badge.py",
                file=sys.stderr,
            )
            return 1
        print("skills badge payload is up to date")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"updated {output_path}")
    return 0


def count_skills(skills_root: Path) -> int:
    if not skills_root.is_dir():
        return 0
    return sum(
        1 for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )


if __name__ == "__main__":
    raise SystemExit(main())
