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
4. Validate generated body structure before presenting preview:
   - body starts directly at `# Workflow`
   - `## Output` appears after `# Workflow`
   - no H1 title block, summary paragraph, or use-case bullets appear before `# Workflow`
5. Reject preview text that copies generator-only author guidance into generated outputs:
   - do not include meta lines such as `Use this section for step context only. Keep detailed mechanics in the referenced workflow files.`
   - keep generated workflow sections focused on the target skill's instructions, not commentary about how `create-skill` is organized
6. For each file, present:
   - target relative path
   - complete proposed content
   - concise change summary versus current file (`new`, `replace`, or `no-change`)
7. If any preview is rejected, revise payload and rerun preview.

## Done when

- Every target file has an approved preview.
- No unresolved corrections remain.
- Generation-ready payload and preview are synchronized.
