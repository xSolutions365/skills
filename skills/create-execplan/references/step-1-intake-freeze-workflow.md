# Step 1 Workflow: Capture and freeze requirements

## Objective

Produce a user-confirmed requirement set before context analysis or plan drafting.

## Step 1 Behavior Rules

- **ALWAYS** treat the user request and any user-supplied artifacts as the authoritative source for Step 1 requirement capture unless the user explicitly asks for challenge or redesign.
- **ALWAYS** translate supplied requirements, invariants, compliance obligations, ADR actions, gates, and named deliverables into the freeze with the same normative force they have in the source.
- **NEVER** compress or summarize a requirement if that would drop operative semantics, failure modes, sequencing constraints, scope boundaries, named tools, named ADRs, or compliance details that materially change implementation expectations.
- **ALWAYS** surface conflicts between the supplied source and the drafted freeze as blockers that must be resolved before Step 1 approval.
- **NEVER** describe an existing verification surface as sufficient when the supplied source says it is missing, broken, crashing, inadequate, or still requires parity work.

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
6. Run the skeptical approval-gate review from [translation-validation-workflow.md](translation-validation-workflow.md) against `workspace/requirements-freeze.md` before surfacing the freeze for user approval.
7. Ask for explicit confirmation:
   - `Confirm the requirements playback in workspace/requirements-freeze.md is final and I should proceed to context analysis.`
8. **STOP** and wait for explicit user confirmation before Step 2.
9. Record the Step 1 confirmation prompt, timestamp, and user response excerpt in `workspace/requirements-freeze.md`.
10. Do not launch any subagent planning phase until the confirmation evidence is written.

## Done when

- `workspace/requirements-freeze.md` exists with playback and confirmation evidence.
- `workspace/translation-validation.md` records a resolved skeptical review for the Step 1 freeze artifact.
- `workspace/context-discovery.md` captures clarifications, verification baseline, and approved research scope.
- `execplan.md` mirrors the confirmed requirements.
- Nothing proceeds to Step 2 without the Step 1 confirmation response.
