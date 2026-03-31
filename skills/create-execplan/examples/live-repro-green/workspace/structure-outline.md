# Structure Outline

- Created: 2026-03-30
- Last updated: 2026-03-30T16:38:00Z

## Interfaces

- `run_phase.py` owns the phase schema, prompt text, workspace staging, worker packet generation, apply-time validation, and phase-result normalization.
- `SKILL.md` owns the parent-orchestrated `prepare -> worker -> apply` loop for non-deterministic phases.
- `tests/run_create_execplan_helpers.sh` owns deterministic regression checks for packet/controller contracts.
- `references/manual-acceptance.md` owns the installed-skill live verification flow.

## Boundaries

- Parent controller vs child phase worker: the parent handles approvals and artifact normalization; the child works only on staged artifacts and returns structured JSON.
- Parent orchestrator vs worker subagent: the parent owns approvals and checkpoint surfacing; the worker must not delegate or talk directly to the user.
- Phase-local artifact set vs broader repo evidence: the current design still needs upstream staging when a brownfield phase requires direct code evidence.

## Data Flow

- Phase controller builds schema, prompt, and staged worker packet.
- `stage_phase_workspace` copies only allowed artifacts into the phase workdir.
- Parent launches one worker subagent from the packet with fresh context.
- Worker phase updates staged artifacts and returns JSON.
- Controller syncs expected outputs back to the artifact root and writes normalized phase state.
- Readiness audit regenerates runtime input and validators consume the final markdown artifacts.
