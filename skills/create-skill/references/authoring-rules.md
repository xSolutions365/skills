# Authoring Rules

Use frontmatter as the canonical identity and routing surface. Start generated `SKILL.md` bodies directly with `# Workflow`, then `## Output`.

## Body structure

- Body starts at `# Workflow` with no decorative H1 title block.
- Do not repeat the frontmatter description as a summary paragraph.
- Do not add standalone use-case bullets above `# Workflow`.
- Keep detailed mechanics in referenced workflow files, not in decorative prose around the workflow.

## Workflow rules

- Use numbered `### Step N: <title>` headings.
- Each step should state purpose, timing when needed, and concrete actions.
- Each step should include exactly one workflow reference link to `references/*workflow.md`.
- Keep runtime commands and environment setup in the corresponding workflow reference file, not in the generated `SKILL.md` body.

## Output rules

- Add `## Output` after `# Workflow`.
- Include `### Result Format`.
- State that the same structure is presented in the terminal and saved to the retained artifact path.
- Keep the output contract concise and deterministic.
