# Step 3 Workflow: Preview generated output

## Objective

Produce deterministic previews for all files before any write.

## Required actions

1. Render preview content using local templates:
   - `assets/templates/skill-output-template.md`
   - `assets/templates/reference-workflow-template.md`
2. Generate preview in fixed order:
   - `SKILL.md`
   - reference documents sorted by `path` ascending
3. Validate `SKILL.md` frontmatter before presenting preview:
   - quote frontmatter string values instead of relying on YAML plain scalars
   - keep `description` to one routing sentence under 200 chars
   - move preset lists, aliases, and colon-labelled inventories into the body or references
4. For each file, present:
   - target relative path
   - complete proposed content
   - concise change summary versus current file (`new`, `replace`, or `no-change`)
5. If any preview is rejected, revise payload and rerun preview.

## Done when

- Every target file has an approved preview.
- No unresolved corrections remain.
- Generation-ready payload and preview are synchronized.
