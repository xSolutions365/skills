# Step 3: Clarify blockers + draft review loop

Objective: resolve Context Pack surfaced questions/blockers before drafting, then run iterative draft reviews until approval.

## Required actions

1. Build and maintain a draft review artifact at `<artifact-root>/workspace/draft-review.md`.
2. Inspect Step 2 outputs and identify newly surfaced questions or blockers that affect planning:
   - unresolved requirement ambiguities
   - missing approvals or inputs
   - dependency or verification blockers
3. If surfaced questions or blockers exist:
   - record each in `workspace/draft-review.md` under `Pre-draft Clarifications & Blockers`
   - present them to the user and resolve each item with explicit responses
   - **STOP** and @ASK_USER_CONFIRMATION before draft generation
4. If no surfaced questions or blockers exist:
   - record `No additional clarifications required before draft creation.` in `workspace/draft-review.md`
5. Generate an initial `execplan.md` draft and record the draft generation timestamp in `workspace/draft-review.md`.
6. Ask the user to review the draft artifacts and provide feedback.
7. For each feedback round:
   - apply required updates to `execplan.md`
   - update `context-pack.md` and workspace artifacts when context changes
   - append a round log entry in `workspace/draft-review.md` (feedback, changes, timestamp, status)
8. If feedback changes requirements, update:
   - `execplan.md` `## Requirements Freeze`
   - `context-pack.md` traceability and evidence links
   - `workspace/context-discovery.md` clarification log
   - `workspace/requirements-freeze.md` confirmation record
9. Ask for explicit draft approval:
   - `Confirm this draft plan is approved and I should proceed to finalization.`
10. **STOP** and @ASK_USER_CONFIRMATION, then end the turn immediately before Step 4:

- do not finalize the plan in the same turn as the approval request
- do not run Step 4 commands until explicit user approval is received

11. Resume Step 4 only after a user message that explicitly approves the draft.
12. Record Step 3 approval evidence in `workspace/draft-review.md`:

- `Approval prompt`
- `Approved by user at`
- `User approval response (verbatim excerpt)`

## Hard gate

- Stop until surfaced questions/blockers are resolved or explicitly deferred by the user.
- Stop until explicit draft approval is received.
- Stop when feedback introduces conflicting requirements; resume only after the user resolves the conflict.
- Stop if draft approval evidence does not include a post-checkpoint user approval response.

## Done when

- `workspace/draft-review.md` records pre-draft clarification status (`resolved` or `none`) and review rounds.
- `execplan.md` reflects the latest approved draft.
- Draft approval is recorded with timestamp, prompt, and response excerpt before Step 4.
