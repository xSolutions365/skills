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
4. Write a requirements playback in `workspace/requirements-freeze.md` and mirror the frozen requirement list into `execplan.md` under `## Requirements Freeze`.
5. Keep Step 1 parent-owned and conversational:
   - do not spawn worker subagents yet
   - do not run `prepare/apply` yet
   - resolve ambiguities with the user before freezing intent
6. Ask for explicit confirmation:
   - `Confirm the requirements playback in workspace/requirements-freeze.md is final and I should proceed to context analysis.`
7. **STOP** and wait for explicit user confirmation before Step 2.
8. Record the Step 1 confirmation prompt, timestamp, and user response excerpt in `workspace/requirements-freeze.md`.
9. Do not launch any subagent planning phase until the confirmation evidence is written.

## Done when

- `workspace/requirements-freeze.md` exists with playback and confirmation evidence.
- `workspace/context-discovery.md` captures clarifications, verification baseline, and approved research scope.
- `execplan.md` mirrors the confirmed requirements.
- Nothing proceeds to Step 2 without the Step 1 confirmation response.
