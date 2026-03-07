# Step 5: Run readiness audit

Objective: verify deterministic executability for low-reasoning executors.

## Audit checks

- Plan is executable from only:
  - working tree
  - `context-pack.md`
  - `execplan.md`
- Requirements freeze artifact exists with explicit confirmation:
  - `<artifact-root>/workspace/requirements-freeze.md`
  - includes `Confirmation prompt` and `User approval response (verbatim excerpt)`
- Draft review artifact exists and records draft approval:
  - `<artifact-root>/workspace/draft-review.md`
  - includes `Approval prompt` and `User approval response (verbatim excerpt)`
- Draft-first loop evidence exists:
  - initial draft timestamp recorded before feedback rounds
  - feedback round log shows each amendment applied to `execplan.md`
- Context Pack passes deterministic validation:
  - `python3 scripts/validate_context_pack.py --context-pack "<artifact-root>/context-pack.md"`
- ExecPlan passes deterministic validation:
  - `python3 scripts/validate_execplan.py --execplan "<artifact-root>/execplan.md"`
- Every success criterion maps to at least one task and one verification command.
- `Test Plan` is a scenario-focused BDD table with required columns and concrete rows (`Scenario ID`, `Req IDs`, `Priority`, `Given`, `When`, `Then`, `Evidence Command`, `Task Ref`).
- Each Test Plan scenario maps to requirement IDs from `Requirements Freeze`, an executable evidence command, and an existing task reference (`P<phase>-T<task>`).
- At least one `P0` smoke scenario exists in `Test Plan`.
- `Requirements Freeze` includes explicit user confirmation timestamp.
- `Success Criteria`, `Quality Gates`, and `Execution Command Catalog` include a smoke-test command.
- Dependency preflight is complete (check/install/source defined) and unresolved install failures are marked blocked with user escalation evidence.
- Brownfield-no-verification with declined onboarding is marked blocked with user escalation evidence and is not marked handoff-ready.
- No undefined discovery tasks remain.

## Failure handling

- If any check fails, revise artifacts and re-run this audit.
- If validation commands rely on repo-root `shared/...` paths instead of skill-local `scripts/...` paths, fail the audit and correct the workflow references before handoff.
- If artifact paths resolve under the skill directory or under `.enaible/artifacts/...` instead of `<project-root>/.plan/create-execplan/...`, fail the audit and correct the workflow references before handoff.

## Done when

- All checks pass and no unresolved audit failures remain.
- `context-pack-validation.json` exists and reports `status: pass`.
- `execplan-validation.json` exists and reports `status: pass`.
