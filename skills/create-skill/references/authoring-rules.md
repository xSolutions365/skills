# Authoring Rules

Use frontmatter as the canonical identity and routing surface. Every generated `SKILL.md` must start with quoted `name` and `description` fields. The `description` must contain only one routing sentence beginning with `Use when`.

## Route rules

- `behaviour-guidance`: use one `SKILL.md` at or under 100 lines. Start the body at `# Guidance`. Do not create references, README, assets, or retained summaries.
- `simple-task:inline`: use one `SKILL.md` at or under 120 lines. Start the body at `# Task`. Keep procedure, validation, and output guidance in the same file.
- `simple-task:runbook-index`: use `SKILL.md` as a progressive-disclosure index at or under 120 lines. Start the body at `# Task`, link every generated runbook under `references/*.md`, and keep each runbook at or under 120 lines.
- `multi-step-workflow`: use the structured pattern. Start the body at `# Workflow`, add numbered `### Step N: <title>` sections, include exactly one `references/*workflow.md` link per step, and keep `SKILL.md` and each workflow reference at or under 120 lines.

## Shared body rules

- Do not repeat the frontmatter description as a summary paragraph.
- Do not add decorative H1 title blocks before the canonical route heading.
- Keep generator-only commentary out of generated outputs.
- Do not generate `generation-summary.md` or any retained summary artifact.
- Keep every generated `SKILL.md` and `references/*.md` file at or under 120 lines.

## Multi-step workflow rules

- Use numbered `### Step N: <title>` headings.
- Each step should state purpose, timing when needed, and concrete actions.
- Each step should include exactly one workflow reference link to `references/*workflow.md`.
- Keep runtime commands and environment setup in the corresponding workflow reference file, not in the generated `SKILL.md` body.
