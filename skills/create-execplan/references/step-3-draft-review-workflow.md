# Step 4 Workflow: Draft and review the ExecPlan

## Objective

Resolve surfaced blockers before drafting, then iterate on `execplan.md` until the draft is explicitly approved.

## Required actions

1. Build and maintain `<artifact-root>/workspace/draft-review.md`.
2. Inspect the approved planning brief, assembled Context Pack, and the upstream research/design/structure artifacts to identify newly surfaced questions or blockers that affect planning.
3. If surfaced blockers exist, record them in `workspace/draft-review.md`, present them to the user, and stop until they are resolved.
4. Run a packet-executability review on every runtime task row before asking for user review:
   - each `Code` task must name concrete `Edit Targets`
   - `Supporting Context Anchors` must remain read-only navigation, not a substitute for edit scope
   - `Commands` must be the exact task-local command set the executor may run for that task
   - standalone onboarding or human-only rows are not valid runtime tasks; fold context into executable rows and keep approvals in harness ADR flow
   - in-repo anchors must stay repo-relative rather than absolute
   - if a row still relies on vague discovery terms like `relevant`, `canonical`, `appropriate`, `locate`, or `identify`, record a blocker and stop
5. Treat under-scoped brownfield tasks as draft blockers, not execution-time ADRs to be deferred downstream.
6. Generate an initial `execplan.md` draft using [execplan-template.md](execplan-template.md).
   - Use the phase packet in `workspace/phases/execplan-draft/phase-worker-input.json` and apply the worker result before surfacing the draft.
7. Keep section ownership aligned with [information-placement.md](information-placement.md) so the draft stays lean.
8. Run the skeptical approval-gate review from [translation-validation-workflow.md](translation-validation-workflow.md) against `execplan.md` before presenting the draft to the user.
9. Ask the user to review the draft and provide feedback.
10. For each feedback round:
   - update `execplan.md`
   - update `context-pack.md` and workspace artifacts when context changes
   - keep `workspace/phase-result.json` aligned to the latest checkpoint state
   - rerun the skeptical approval-gate review and resolve any new findings before asking for final approval
   - append the round summary, changed files, and timestamp to `workspace/draft-review.md`
11. Ask for explicit draft approval:
   - `Confirm this draft plan is approved and I should proceed to finalization.`
12. **STOP** and wait for explicit user approval before Step 5.
13. Record the approval prompt, timestamp, and response excerpt in `workspace/draft-review.md`.

## Done when

- `workspace/draft-review.md` records pre-draft blocker status and feedback rounds.
- `workspace/translation-validation.md` records a resolved skeptical review for the latest Step 4 draft.
- `execplan.md` reflects the latest approved draft.
- `workspace/phase-result.json` reflects the latest draft-review checkpoint outcome.
- Runtime task rows are explicit enough for a packet-only executor to act without repo-wide discovery.
- Draft approval evidence is recorded before Step 5 begins.
