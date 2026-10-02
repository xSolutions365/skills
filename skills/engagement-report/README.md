# engagement-report

## Overview

Create or update engagement-report period folders from Markdown notes, then render the canonical report as a standalone HTML presentation. The workflow preserves the existing `# Plan visual` and `# Timeline` sections and the presentation `REPORT.plan_visual` and `REPORT.timeline` fields while adding multi-image support through `REPORT.plan_visuals`.

## When to use it

- Add a new engagement to an engagement-report repository.
- Generate a reporting period from a `notes/` tree.
- Update an existing Markdown report and presentation with new notes.
- Carry SOW dates, releases, milestones, burndown charts, and other note attachments into report output.

## Example prompts

- "Add the Payments Platform engagement and create its first weekly report."
- "Update this reporting period from the new notes and rebuild the presentation."
- "Include the SOW dates, release milestones, and both burndown images in the report."

## References

- Workflow: [SKILL.md](SKILL.md)
- Source-note conventions: [references/source-note-conventions.md](references/source-note-conventions.md)
- CLI: [scripts/engagement_report.py](scripts/engagement_report.py)
