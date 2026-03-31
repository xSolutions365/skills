# ExecPlan: Harden create-execplan phase isolation against nested child-agent work

- Status: In Progress
- Start: 2026-03-30 • Last Updated: 2026-03-30T16:46:00Z
- Artifact root: `skills/create-execplan/examples/live-repro-green/`
- Workspace root: `skills/create-execplan/examples/live-repro-green/workspace/`
- Context Pack: `skills/create-execplan/examples/live-repro-green/context-pack.md`
- Runtime Input artifact: `skills/create-execplan/examples/live-repro-green/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `skills/create-execplan/examples/live-repro-green/workspace/requirements-freeze.md`
- Planning Brief artifact: `skills/create-execplan/examples/live-repro-green/workspace/planning-brief.md`
- Draft Review artifact: `skills/create-execplan/examples/live-repro-green/workspace/draft-review.md`
- Phase Manifest artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-manifest.json`
- Phase Result artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-result.json`
- Research Questions artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-questions.md`
- Research Findings artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md`
- Design Options artifact: `skills/create-execplan/examples/live-repro-green/workspace/design-options.md`
- Structure Outline artifact: `skills/create-execplan/examples/live-repro-green/workspace/structure-outline.md`
- Links: `skills/create-execplan/SKILL.md`

## Requirements Freeze

- R1: Preserve the deterministic `create-execplan` package flow: scaffold, manifest/result checkpointing, staged `prepare/apply` control steps, fresh worker subagents, finalized `execplan.md`, generated runtime input, readiness audit, and handoff checklist.
- R2: Ensure a child phase run cannot invoke nested planning or child-agent orchestration; the effective execution boundary must remain one fresh worker subagent working only on staged artifacts.
- R3: Add or tighten regression coverage so the isolation rule is testable with repo-local checks and a live installed-skill run, and the mock package can reach a green readiness audit.
- Confirmed by user at: 2026-03-30T16:10:00Z

## Purpose / Big Picture

Stabilize `create-execplan` child-phase execution so the workflow remains deterministic and auditable even in environments where the parent Codex home carries global delegation rules or skills. The plan keeps the final handoff package shape unchanged while hardening the boundary between parent controller and child phase worker.

## Success Criteria (how to prove "done")

- [ ] Smoke: `bash tests/run_create_execplan_helpers.sh` -> create-execplan helper checks passed
- [ ] A live installed-skill phase run completes through `prepare -> worker -> apply` without nested delegation
- [ ] `bash tests/run_create_execplan_helpers.sh` passes with assertions for staged worker packets, isolated prompt wording, and apply-time validation
- Non-Goals: redesign brownfield source-evidence staging for all isolated phases

## Constraints & Guardrails

- Preserve the existing scaffold, manifest/result checkpointing, readiness audit, and handoff checklist flow.
- Keep the refactor surface narrow to schema, staged worker packet generation, apply-time validation, and regression coverage.
- Do not reintroduce legacy runtime-input fields or fallback execution modes.

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| codex app | host parent and worker subagents | `n/a` | `n/a` | Codex desktop/app runtime | stop and escalate to user if subagent tools are unavailable |
| python runtime | run controller and validators | `./skills/create-execplan/scripts/resolve_python.sh` | `n/a` | local tool installation | stop and escalate to user on runtime resolution failure |

## Task Table (single source of truth)

Status keys:

- `@` = in progress
- `X` = complete
- (blank) = outstanding

Task Types:

- Code, Action, Test, Gate

Use `n/a` when `Edit Targets`, `Supporting Context Anchors`, or `Commands` does not apply. Every row must:

- map to one or more requirement IDs
- distinguish edit targets from read-only supporting context anchors
- list only task-local commands the executor is allowed to run for that task
- state the expected output or completion signal
- avoid implicit discovery
- keep every runtime row directly executable; do not emit standalone onboarding or human-only rows

| Status | Phase # | Task # | Type | Req IDs | Edit Targets | Supporting Context Anchors | Commands | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | -------------------------- | -------- | --------------- | ------ |
|        | 1 | 1 | Code | R1,R2 | `skills/create-execplan/scripts/run_phase.py:1`,`skills/create-execplan/scripts/execplan_common.py:1`,`skills/create-execplan/SKILL.md:1` | `skills/create-execplan/references/step-1-intake-freeze-workflow.md:1`,`skills/create-execplan/references/step-2-context-pack-workflow.md:1` | `n/a` | staged worker packets and apply-time validation replace the subprocess wrapper | Update the controller and skill contract so each non-deterministic phase uses `prepare -> worker -> apply`. |
|        | 1 | 2 | Code | R1,R2 | `skills/create-execplan/references/artifact-contract.md:1`,`skills/create-execplan/references/manual-acceptance.md:1` | `skills/create-execplan/README.md:1`,`skills/create-execplan/references/step-0-preflight-workflow.md:1` | `n/a` | docs and audit artifacts describe worker packets and parent-owned approvals | Update the docs and retained fixture package to the subagent contract. |
|        | 2 | 3 | Test | R3 | `tests/run_create_execplan_helpers.sh:1` | `skills/create-execplan/scripts/run_phase.py:1`,`skills/create-execplan/references/manual-acceptance.md:1` | `bash tests/run_create_execplan_helpers.sh` | `create-execplan helper checks passed` | Run the helper regression suite after the controller refactor. |
|        | 2 | 4 | Action | R2,R3 | `n/a` | `skills/create-execplan/references/manual-acceptance.md:1`,`skills/create-execplan/examples/live-repro-green/README.md:1` | `./scripts/deploy-skill-local.sh create-execplan` | installed skill deployed locally and ready for the retained-fixture live acceptance flow | Deploy the updated skill locally before running the retained-fixture live acceptance flow in the Codex app. |

## Progress Log (running)

- (2026-03-30T16:46Z) Mock package updated to retain the original repro context while documenting the canonical fix as `prepare/apply` plus fresh worker subagents.

## Decision Log

- Decision: replace subprocess child phases with parent-managed worker subagents instead of relying on prompt wording alone.
  - Rationale: the live reproduction showed that subprocess boundaries were not the right control surface for delegation and approval handling.
  - Date: 2026-03-30

- Decision: keep brownfield source-evidence staging out of the immediate fix scope.
  - Rationale: the reproduced defect is child runtime isolation; redesigning how all brownfield phases consume repo evidence is a larger controller change.
  - Date: 2026-03-30

## Execution Findings

- Finding: the retained repro proved prompt-only subprocess isolation was insufficient, so the canonical fix moved phase boundaries into the parent-managed worker contract.
- Evidence: `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md`
- Decision link: replace subprocess child phases with parent-managed worker subagents instead of relying on prompt wording alone
- User approval (required if this introduces new discovery scope): not required

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` values like `P2-T4` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | the helper suite exercises the smoke path for prepare/apply against staged worker packets | the regression harness runs | smoke packet generation, apply-time validation, and manifest advancement all pass | `bash tests/run_create_execplan_helpers.sh` | P2-T3 |
| S2 | P1 | the retained fixture is used with the installed skill | the updated skill is deployed locally and one non-deterministic phase is run through `prepare -> worker -> apply` | the phase completes without nested delegation and the package remains valid | `./scripts/deploy-skill-local.sh create-execplan` | P2-T4 |
| S3 | P1 | a checkpoint phase returns `needs_approval` or `needs_user_input` | `apply` validates the result | checkpoint statuses fail unless draft artifacts were already updated in the staged workdir | `bash tests/run_create_execplan_helpers.sh` | P1-T1 |

## Idempotence & Recovery

Re-running the controller reruns only the selected phase. Re-running the helper checks or redeploying the installed skill is safe and should not mutate repo state outside the staged fixture flow. Re-running readiness audit regenerates the runtime input from the markdown sources. If validation fails, update the source markdown or controller code and rerun the validators instead of editing generated JSON by hand.
