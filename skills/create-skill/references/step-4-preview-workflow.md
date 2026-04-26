# Step 4 Workflow: Preview route-specific output

## Objective

Produce deterministic previews for all files before any write.

## Required actions

1. Select exactly one `SKILL.md` template from the approved `template_type`:
   - `assets/templates/behaviour-guidance-skill-template.md`
   - `assets/templates/simple-task-skill-template.md`
   - `assets/templates/simple-task-runbook-index-template.md`
   - `assets/templates/multi-step-workflow-skill-template.md`
2. Render optional references only when the route requires them:
   - use `assets/templates/reference-runbook-template.md` for `simple-task:runbook-index`
   - use `assets/templates/reference-workflow-template.md` for `multi-step-workflow`
   - use `assets/templates/readme-template.md` for `multi-step-workflow`
3. Generate preview in fixed order:
   - `SKILL.md`
   - `README.md` when `template_type` is `multi-step-workflow`
   - reference documents sorted by `path` ascending
4. Validate `SKILL.md` frontmatter before presenting preview:
   - quote frontmatter string values instead of relying on YAML plain scalars
   - keep `description` to one routing sentence under 200 chars
   - include exactly one `USE WHEN` clause
5. Reject preview text that copies generator-only author guidance into generated outputs.
6. Reject any generated file named `generation-summary.md`.
7. For each file, present:
   - target relative path
   - complete proposed content
   - concise change summary versus current file (`new`, `replace`, or `no-change`)
8. If any preview is rejected, revise payload and rerun preview.

## Done when

- Every target file has an approved preview.
- No unresolved corrections remain.
- Generation-ready payload and preview are synchronized.
