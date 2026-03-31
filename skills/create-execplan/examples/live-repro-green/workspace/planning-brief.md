# Planning Brief

- Created: 2026-03-30
- Last updated: 2026-03-30T16:12:00Z

## Objective Summary

- User-visible outcome: preserve the deterministic `create-execplan` package flow while preventing nested child-agent behavior inside any worker phase.
- In-scope change surface: phase-controller prompts and schema, staged worker packet handling, parent-owned approvals, helper regression coverage, and retained fixture updates.
- Explicit non-goals: do not redesign brownfield evidence staging for every future phase, do not reintroduce subprocess wrappers, and do not widen the change into a new planning package format.

## Source of Truth Inputs

- Requirements freeze artifact: `skills/create-execplan/examples/live-repro-green/workspace/requirements-freeze.md`
- Context discovery artifact: `skills/create-execplan/examples/live-repro-green/workspace/context-discovery.md`
- Source links or seed artifacts: `skills/create-execplan/SKILL.md`, `skills/create-execplan/scripts/run_phase.py`, `tests/run_create_execplan_helpers.sh`, `skills/create-execplan/references/manual-acceptance.md`

## Planning Decisions

- Selected project mode (`greenfield`|`brownfield`): `brownfield`
- Mode rationale: the work updates existing skill behavior, helper scripts, and committed examples rather than creating a new planning product.
- Verification scenario to carry into planning: `brownfield-existing`
- Mandatory smoke gate command: `bash tests/run_create_execplan_helpers.sh`
- Online research policy carried forward: repo-local references and generated fixture artifacts only; no external sources permitted.

## Phase Guidance

- Research questions must answer: where nested delegation entered the old flow, which boundary should reject it, and what artifacts must prove the fix.
- Research must stay within these source boundaries: helper scripts, skill references, tests, and the generated live fixture package.
- Design options must compare these trade-offs: strict child isolation, parent-managed subagent phases, and fixture-backed regression coverage.
- Structure must anchor these edit surfaces or interfaces: `run_phase.py`, `execplan_common.py`, `SKILL.md`, helper tests, and retained example artifacts.

## Approval

- Approval prompt: Is the planning brief in workspace/planning-brief.md approved as the source of truth for upstream planning phases?
- Approved by user at: 2026-03-30T16:12:00Z
- User approval response (verbatim excerpt): planning brief approved; continue with the mock run
- Approval note: parent-owned approval recorded before any worker phase consumed the planning contract.
