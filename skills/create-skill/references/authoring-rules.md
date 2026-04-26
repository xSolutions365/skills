# Authoring Rules

Use frontmatter as the canonical identity and routing surface. Every generated `SKILL.md` must start with quoted `name` and `description` fields, and `description` must contain one `USE WHEN` clause.

## Route rules

- `behaviour-guidance`: use one `SKILL.md` at or under 100 lines. Start the body at `# Guidance`. Do not create references, README, assets, or retained summaries.
- `simple-task:inline`: use one `SKILL.md` at or under 500 lines. Start the body at `# Task`. Keep procedure, validation, and output guidance in the same file.
- `simple-task:runbook-index`: use `SKILL.md` at or under 500 lines as a progressive-disclosure index. Start the body at `# Task` and link every generated runbook under `references/*.md`; runbooks are optional to load at runtime, not optional to link.
- `multi-step-workflow`: use the structured pattern. Start the body at `# Workflow`, add numbered `### Step N: <title>` sections, and include exactly one `references/*workflow.md` link per step.

## Shared body rules

- Do not repeat the frontmatter description as a summary paragraph.
- Do not add decorative H1 title blocks before the canonical route heading.
- Keep generator-only commentary out of generated outputs.
- Do not generate `generation-summary.md` or any retained summary artifact.

## Multi-step workflow rules

- Use numbered `### Step N: <title>` headings.
- Each step should state purpose, timing when needed, and concrete actions.
- Each step should include exactly one workflow reference link to `references/*workflow.md`.
- Keep runtime commands and environment setup in the corresponding workflow reference file, not in the generated `SKILL.md` body.
