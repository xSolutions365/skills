# Step 4: Finalize approved ExecPlan

Objective: convert the approved draft into a handoff-ready living execution plan without reopening discovery.

## Required actions

1. Confirm Step 3 draft approval is recorded in `workspace/draft-review.md`.
2. Use the approved draft as the baseline and preserve approved requirements/scope.
3. Finalize `execplan.md` against the required structure:
   - [execplan-template.md](execplan-template.md)
4. Ensure task rows are explicit actions with:
   - file anchors
   - commands
   - expected outcomes
5. Ensure dependency preflight tasks are complete for each required external library/tool:
   - check command
   - install command (if missing)
   - installation source
   - hard-fail escalation step when install fails
6. Ensure verification tasks match the selected scenario:
   - greenfield setup
   - brownfield existing verification amendments
   - brownfield change-scoped verification onboarding
   - if brownfield-no-verification was declined by the user, keep plan blocked and route back to the user instead of finalizing
7. Ensure `## Test Plan` is a scenario-focused BDD table with required columns:
   - `Scenario ID`
   - `Req IDs`
   - `Priority`
   - `Given`
   - `When`
   - `Then`
   - `Evidence Command`
   - `Task Ref`
8. Ensure each Test Plan scenario is concise and traceable:
   - `Given/When/Then` each fit one concise line
   - `Req IDs` map to `Requirements Freeze` IDs (`R#`)
   - `Evidence Command` is executable
   - `Task Ref` maps to an explicit task row (`P<phase>-T<task>`)
9. Ensure a minimum smoke-test gate command appears in both `Success Criteria` and `Quality Gates`, and at least one `P0` smoke scenario exists in `Test Plan`.
10. Keep the task table as the single source of truth for progress.
11. If finalization reveals new blockers or unanswered questions, record them in `workspace/draft-review.md` and return to Step 3 before handoff.

- **STOP** and @ASK_USER_CONFIRMATION before returning to Step 3.

## Hard rule

- Do not introduce new requirements or discovery scope in Step 4; route those back to Step 3.
- Do not include vague tasks (`investigate`, `review`, `refactor`) unless entry point and completion proof are explicit.
- Do not include implicit discovery tasks in the task table.
- Do not use `## Test Plan` as a raw command dump; each row must be scenario-focused BDD coverage.
- Do not use unbounded permutation matrices in `## Test Plan`; keep coverage scoped to changed behavior and high-risk regressions.
- Do not continue when dependency installation fails; mark blocked, capture evidence, and escalate to the user.
- Do not finalize when brownfield-no-verification onboarding is declined; mark blocked and escalate to the user.

## Done when

- `execplan.md` is a finalized version of the approved draft with required gates/tasks complete.
- A low-reasoning executor can execute each task row using only `context-pack.md`, `execplan.md`, and the working tree.
