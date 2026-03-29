# Step 1 Workflow: Capture and freeze requirements

## Objective

Produce a user-confirmed requirement set before context analysis or plan drafting.

## Required actions

1. Run clarifying rounds until requirements are concrete and testable, even if the user supplied artifacts or an existing draft.
2. Capture:
   - scope and user-visible outcomes
   - constraints and non-goals
   - user-provided artifacts and starting views
   - online research permissions and approved sources
   - recency expectations for volatile facts
   - verification baseline, including whether existing verification exists and whether smoke coverage exists
3. Record the intake outputs in `<artifact-root>/workspace/`:
   - `context-discovery.md`
   - `context-evidence.json`
   - `requirements-freeze.md`
4. Run the requirements-freeze phase through the deterministic controller so the latest checkpoint is written back to `workspace/phase-result.json`.
5. Write a requirements playback in `workspace/requirements-freeze.md` and mirror the frozen requirement list into `execplan.md` under `## Requirements Freeze`.
6. Ask for explicit confirmation:
   - `Confirm the requirements playback in workspace/requirements-freeze.md is final and I should proceed to context analysis.`
7. **STOP** and wait for explicit user confirmation before Step 2.
8. Record the Step 1 confirmation prompt, timestamp, and user response excerpt in `workspace/requirements-freeze.md`.
9. Normalize the approval checkpoint back into `workspace/phase-result.json` before any later phase runs.

## Done when

- `workspace/requirements-freeze.md` exists with playback and confirmation evidence.
- `workspace/context-discovery.md` captures clarifications, verification baseline, and approved research scope.
- `workspace/phase-result.json` records the latest normalized requirements-freeze checkpoint.
- `execplan.md` mirrors the confirmed requirements and nothing proceeds to Step 2 without the checkpoint response.
