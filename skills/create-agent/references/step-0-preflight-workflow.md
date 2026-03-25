# Step 0 Workflow: Preflight local context

## Objective

Confirm deterministic local context before request handling.

## Required actions

1. Set the working root to the directory that contains `SKILL.md`.
2. Resolve all workflow paths relative to that root.
3. Confirm required references and templates exist inside this skill:
   - `references/agent-request-schema.md`
   - `references/validation-checklist.md`
   - `assets/templates/system-contract-template.md`
   - `assets/templates/task-packet-template.md`
   - `assets/templates/verification-checklist-template.md`
   - `assets/templates/subagent-spec-template.md`
4. Confirm the role-profile templates exist under `assets/templates/role-profiles/`.
5. Ask for or infer the target output directory for generated agent files and keep it relative.
6. Record the preflight result as `PASS` or `FAIL` with one-line evidence.

## Done when

- The skill-root working context is confirmed.
- Required references and templates exist.
- The output root for generated files is agreed and relative.
- Preflight result is `PASS`.
