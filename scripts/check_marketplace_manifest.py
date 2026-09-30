#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


def fail(message):
    print(f"marketplace manifest: {message}", file=sys.stderr)
    return 1


def check_manifest(root):
    manifest_path = root / ".claude-plugin" / "marketplace.json"
    try:
        with manifest_path.open(encoding="utf-8") as manifest_file:
            manifest = json.load(manifest_file)
    except (OSError, json.JSONDecodeError) as error:
        return fail(f"cannot read valid JSON from {manifest_path}: {error}")

    if not isinstance(manifest, dict):
        return fail("manifest must be an object")

    name = manifest.get("name")
    if not isinstance(name, str) or not name.strip():
        return fail("marketplace must have a non-empty name")

    owner = manifest.get("owner")
    if not isinstance(owner, dict) or not isinstance(owner.get("name"), str) or not owner["name"].strip():
        return fail("marketplace owner must have a non-empty name")

    if not isinstance(manifest.get("plugins"), list):
        return fail("plugins must be an array")

    declared_skills = set()
    plugin_names = set()
    for index, plugin in enumerate(manifest["plugins"]):
        if not isinstance(plugin, dict):
            return fail(f"plugin entry {index + 1} must be an object")

        name = plugin.get("name")
        if not isinstance(name, str) or not name:
            return fail(f"plugin entry {index + 1} must have a non-empty name")
        if name in plugin_names:
            return fail(f"duplicate plugin entry: {name}")
        plugin_names.add(name)

        source = plugin.get("source")
        if not (
            isinstance(source, str) and source.strip()
            or isinstance(source, dict) and source
        ):
            return fail(f"plugin {name} must have a non-empty source")

        skills = plugin.get("skills")
        if not isinstance(skills, list) or len(skills) != 1:
            return fail(f"plugin {name} must declare exactly one skill path")
        skill_path = skills[0]
        if not isinstance(skill_path, str) or not skill_path.startswith("./skills/"):
            return fail(f"plugin {name} has an invalid skill path: {skill_path!r}")

        skill_dir = skill_path.removeprefix("./skills/")
        if not skill_dir or "/" in skill_dir or skill_dir in {".", ".."}:
            return fail(f"plugin {name} has an invalid skill path: {skill_path!r}")
        if skill_dir != name:
            return fail(f"plugin {name} must reference ./skills/{name}")
        if skill_dir in declared_skills:
            return fail(f"duplicate skill path: {skill_path}")
        if not (root / "skills" / skill_dir / "SKILL.md").is_file():
            return fail(f"missing skill file: skills/{skill_dir}/SKILL.md")
        declared_skills.add(skill_dir)

    actual_skills = {
        skill_file.parent.name
        for skill_file in (root / "skills").glob("*/SKILL.md")
        if skill_file.is_file()
    }
    missing_entries = sorted(actual_skills - declared_skills)
    if missing_entries:
        return fail(f"skills missing plugin entries: {', '.join(missing_entries)}")

    extra_entries = sorted(declared_skills - actual_skills)
    if extra_entries:
        return fail(f"plugin entries without skill files: {', '.join(extra_entries)}")

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    return check_manifest(args.root.resolve())


if __name__ == "__main__":
    sys.exit(main())
