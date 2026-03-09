# create-skill

## Overview

Create or update a structured multi-file skill through a deterministic workflow that captures requirements, previews output, validates it, and then writes the files.

## When to use it

- You need to author a new skill from scratch.
- You need to create or update an existing skill in the structured multi-step workflow pattern.
- You want explicit review checkpoints before any files are generated.
- You need to refactor a compact skill that has grown beyond 500 lines into linked reference files without losing detail.

## Example prompts

- "Use `create-skill` to create a new skill for writing product launch briefs."
- "Use `create-skill` to update this skill so it supports a stricter validation checklist."
- "Use `create-skill` to draft a portable skill that generates onboarding plans."
- "Refactor <skill-in-question> to align with the create-skill pattern, whilst retaining all content with granular detail moving to reference files."

## References

- Compact single-file skills under 500 lines are allowed in this repo and do not need to use `create-skill`.
- Reserve `create-skill` for structured skills that need `README.md`, linked workflow references, or content split across multiple files.
