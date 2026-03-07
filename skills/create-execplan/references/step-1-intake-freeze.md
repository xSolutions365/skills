# Step 1: Intake + requirements freeze

Objective: produce a user-confirmed requirement set before planning details.

## Required actions

1. Run clarifying rounds until requirements are concrete and testable, even if the user supplied artifacts or an existing draft.
2. Capture:
   - Scope and user-visible outcomes.
   - Constraints and non-goals.
   - Delivery expectations and quality gates.
   - User-provided artifacts and starting views.
   - Online research permissions (allowed/disallowed, approved domains/APIs).
   - Recency expectations for external facts and library recommendations.
   - Verification baseline:
     - whether existing verification commands exist
     - where they run (local/CI)
     - baseline smoke check capability
3. If no existing verification is present, ask:
   - `No existing verification was found. Do you want the plan to add change-scoped verification for the new changes?`
4. Record intake outputs in `<artifact-root>/workspace/`:
   - `context-discovery.md`
   - `context-evidence.json` (initialize with known requirement evidence stubs)
   - `requirements-freeze.md`
5. Write a requirements playback in `workspace/requirements-freeze.md`:
   - captured requirements
   - constraints and non-goals
   - provided artifacts
   - explicit assumptions
   - verification decision from step 3
6. Copy the frozen requirement list into `execplan.md` under `## Requirements Freeze`.
7. Ask for explicit confirmation with playback:
   - `Confirm the requirements playback in workspace/requirements-freeze.md is final and I should proceed to context analysis.`
8. **STOP** and @ASK_USER_CONFIRMATION, then end the turn immediately before Step 2:
   - do not run additional commands
   - do not write new artifacts
   - do not continue to Step 2 work in the same turn
9. Resume only after a user message that explicitly approves the Step 1 confirmation request:
   - do not treat the original task request as freeze confirmation
10. Record Step 1 confirmation evidence in `workspace/requirements-freeze.md`:

- `Confirmed by user at`
- `Confirmation prompt`
- `User approval response (verbatim excerpt)`

## Hard gate

- Stop until explicit user confirmation is received and recorded in `workspace/requirements-freeze.md`.
- Stop when no existing verification is present and the user declines change-scoped verification onboarding; escalate and wait for explicit user direction before Step 2.
- Stop if confirmation evidence does not include a post-checkpoint user approval response.
- Stop if confirmation was inferred from the initial task request.

## Done when

- `workspace/requirements-freeze.md` exists with playback and confirmation timestamp.
- `workspace/requirements-freeze.md` records both the checkpoint prompt and user approval response excerpt.
- `execplan.md` `## Requirements Freeze` mirrors the confirmed requirements.
- `workspace/context-discovery.md` captures clarifications, verification baseline, and approved research scope.
