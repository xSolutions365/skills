# Step 3 Workflow: Draft and review the ExecPlan

## Objective

Resolve surfaced blockers before drafting, then iterate on `execplan.md` until the draft is explicitly approved.

## Required actions

1. Build and maintain `<artifact-root>/workspace/draft-review.md`.
2. Inspect Step 2 outputs and identify newly surfaced questions or blockers that affect planning.
3. If surfaced blockers exist, record them in `workspace/draft-review.md`, present them to the user, and stop until they are resolved.
4. Generate an initial `execplan.md` draft using [execplan-template.md](execplan-template.md).
5. Keep section ownership aligned with [information-placement.md](information-placement.md) so the draft stays lean.
6. Ask the user to review the draft and provide feedback.
7. For each feedback round:
   - update `execplan.md`
   - update `context-pack.md` and workspace artifacts when context changes
   - append the round summary, changed files, and timestamp to `workspace/draft-review.md`
8. Ask for explicit draft approval:
   - `Confirm this draft plan is approved and I should proceed to finalization.`
9. **STOP** and wait for explicit user approval before Step 4.
10. Record the approval prompt, timestamp, and response excerpt in `workspace/draft-review.md`.

## Done when

- `workspace/draft-review.md` records pre-draft blocker status and feedback rounds.
- `execplan.md` reflects the latest approved draft.
- Draft approval evidence is recorded before Step 4 begins.
