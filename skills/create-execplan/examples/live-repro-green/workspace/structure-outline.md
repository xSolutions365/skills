# Structure Outline

- Created: 2026-03-30
- Last updated: 2026-03-30T16:38:00Z

## Interfaces

- `run_phase.py` owns the phase schema, prompt text, workspace staging, child invocation, and phase-result normalization.
- `run_codex_phase.sh` owns the executable child runtime boundary for `codex exec`.
- `tests/run_create_execplan_helpers.sh` owns fake-Codex regression checks for wrapper/controller contracts.
- `tests/run_create_execplan_live_codex_smoke.sh` owns the live smoke proof that the wrapper still works with a real Codex invocation.

## Boundaries

- Parent controller vs child phase worker: the parent handles approvals and artifact normalization; the child works only on staged artifacts and returns structured JSON.
- Repo/user Codex environment vs child runtime: the child must not inherit global `CODEX_HOME` instructions, skills, or state.
- Phase-local artifact set vs broader repo evidence: the current design still needs upstream staging when a brownfield phase requires direct code evidence.

## Data Flow

- Phase controller builds schema and prompt.
- `stage_phase_workspace` copies only allowed artifacts into the phase workdir.
- `run_codex_phase.sh` launches child `codex exec` inside a temporary `CODEX_HOME` with `workspace-write` sandbox.
- Child phase updates staged artifacts and returns JSON.
- Controller syncs expected outputs back to the artifact root and writes normalized phase state.
- Readiness audit regenerates runtime input and validators consume the final markdown artifacts.
