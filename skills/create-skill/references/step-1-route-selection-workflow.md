# Step 1 Workflow: Classify skill template route

## Objective

Select one route before collecting detailed requirements.

## Required actions

1. Classify the requested skill using these route rules:
   - `behaviour-guidance`: general behavior, constraints, or tool-use guidance at or under 100 lines in one `SKILL.md`.
   - `simple-task:inline`: self-contained task procedure at or under 500 lines in one `SKILL.md`.
   - `simple-task:runbook-index`: task procedure at or under 500 lines where `SKILL.md` points to `references/*.md` runbooks that are optional to load at runtime.
   - `multi-step-workflow`: workflows with distinct ordered steps, checkpoints, approvals, mandatory external workflow files, or total content over 500 lines.
2. Treat `multi-step-workflow` as required when the skill needs numbered checkpoints or mandatory external workflow files.
3. Use this tie-break when guidance and task procedure both seem plausible:
   - choose `behaviour-guidance` when the skill tells the agent how to behave generally across user requests
   - choose `simple-task:inline` or `simple-task:runbook-index` when the skill completes a user task with a concrete output
4. Treat `simple-task:runbook-index` as required when extra detail should be loaded only when needed and the main `SKILL.md` remains compact.
5. Ask the user to confirm the route only when the request still fits more than one route or the line-count target is unclear after applying the tie-breaks.
6. Record the chosen `template_type` exactly as one of the four route values.

## Done when

- Exactly one `template_type` is selected.
- Any ambiguity has explicit user confirmation.
- The selected route can be validated against its line and file-shape constraints.
