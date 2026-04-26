# Step 0 Workflow: Preflight local context

## Objective

Confirm deterministic local context before route selection.

## Required actions

1. Set working root to the directory that contains `SKILL.md`.
2. Resolve all paths relative to this root and do not use repo-root assumptions.
3. Confirm required references exist:
   - `references/authoring-rules.md`
   - `references/payload-schema.md`
   - `references/validation-checklist.md`
   - `references/step-1-route-selection-workflow.md`
4. Confirm route templates exist:
   - `assets/templates/behaviour-guidance-skill-template.md`
   - `assets/templates/simple-task-skill-template.md`
   - `assets/templates/simple-task-runbook-index-template.md`
   - `assets/templates/multi-step-workflow-skill-template.md`
   - `assets/templates/readme-template.md`
   - `assets/templates/reference-runbook-template.md`
   - `assets/templates/reference-workflow-template.md`
5. Confirm the target output root for the generated skill and express it as a relative path.
6. Record the preflight result as `PASS` or `FAIL` with one-line evidence.

## Done when

- Skill-root working context is confirmed.
- Required references and templates exist.
- Output root is agreed and expressed as a relative path.
- Preflight result is `PASS`.
