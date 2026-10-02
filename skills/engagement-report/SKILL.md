---
name: "engagement-report"
description: "Use when creating or updating engagement reports and standalone presentations from period notes."
---

# Workflow

### Step 0: Confirm the reporting context

- **Purpose**: Locate the report repository, engagement, reporting period, notes, and prior report before changing files.
- **When**: Run first for both new and existing engagements.
- Treat the reporting-period directory as the trust boundary for note attachments.
- Preserve the established report headings and presentation `REPORT` data contract.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Add or select an engagement

- **Purpose**: Create the portable folder structure or select an existing engagement without disturbing its history.
- **When**: Run after preflight.
- Use `add-engagement` only when the engagement directory does not exist.
- Select explicit ISO period dates for every generation run.
- Workflow: [references/step-1-engagement-workflow.md](references/step-1-engagement-workflow.md)

### Step 2: Collect period evidence

- **Purpose**: Read notes, dated events, and image attachments into a safe deterministic evidence set.
- **When**: Run before drafting or updating the canonical Markdown report.
- Prefer the explicit conventions in `references/source-note-conventions.md`.
- Also extract unambiguous ISO-dated milestones and Markdown image references from ordinary notes.
- Workflow: [references/step-2-evidence-workflow.md](references/step-2-evidence-workflow.md)

### Step 3: Draft or update the report

- **Purpose**: Produce the canonical Markdown report while preserving evidence, history, and report structure.
- **When**: Run after evidence collection.
- Use the generator to establish or refresh managed timeline and plan-visual sections.
- Synthesize narrative sections from source evidence; never infer unsupported status, ownership, or dates.
- Workflow: [references/step-3-report-workflow.md](references/step-3-report-workflow.md)

### Step 4: Render the standalone presentation

- **Purpose**: Convert the canonical report into a self-contained presentation with chronological timeline and image slides.
- **When**: Run after the Markdown report is complete.
- Embed copied local image assets as data URIs.
- Keep remote images as explicit links and never fetch or embed them.
- Workflow: [references/step-4-presentation-workflow.md](references/step-4-presentation-workflow.md)

### Step 5: Validate and hand off

- **Purpose**: Verify generated dates, images, report structure, and presentation portability.
- **When**: Run after every generation or update.
- Inspect the generated Markdown and the presentation `REPORT` object.
- Run the packaged tests when the skill itself changes.
- Workflow: [references/step-5-validation-workflow.md](references/step-5-validation-workflow.md)

## Output

### Result Format

- Report created or updated period paths.
- List timeline events and copied or linked images included.
- Identify ignored unsafe or unsupported image references.
- Report validation commands and results.
