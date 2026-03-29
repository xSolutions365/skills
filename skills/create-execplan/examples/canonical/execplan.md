# ExecPlan: Canonical create-execplan package

- Status: In Progress
- Start: 2026-03-24 • Last Updated: 2026-03-24T09:30:00Z
- Artifact root: `.plan/create-execplan/canonical/`
- Workspace root: `.plan/create-execplan/canonical/workspace/`
- Context Pack: `.plan/create-execplan/canonical/context-pack.md`
- Runtime Input artifact: `.plan/create-execplan/canonical/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `.plan/create-execplan/canonical/workspace/requirements-freeze.md`
- Draft Review artifact: `.plan/create-execplan/canonical/workspace/draft-review.md`
- Phase Manifest artifact: `.plan/create-execplan/canonical/workspace/phase-manifest.json`
- Phase Result artifact: `.plan/create-execplan/canonical/workspace/phase-result.json`
- Research Questions artifact: `.plan/create-execplan/canonical/workspace/research-questions.md`
- Research Findings artifact: `.plan/create-execplan/canonical/workspace/research-findings.md`
- Design Options artifact: `.plan/create-execplan/canonical/workspace/design-options.md`
- Structure Outline artifact: `.plan/create-execplan/canonical/workspace/structure-outline.md`
- Links: skills/create-execplan/references/artifact-contract.md

## Requirements Freeze

- R1: Keep the ExecPlan as the living human document.
- R2: Generate a narrow runtime input artifact from explicit task packets.
- R3: Keep scaffolded plan metadata and helper examples repo-relative and packet-executable.
- Confirmed by user at: 2026-03-24T09:00:00Z

## Purpose / Big Picture

Deliver a slimmer plan package that keeps the markdown ExecPlan as the human-facing source of truth while generating a smaller runtime artifact that a packet-only harness can execute safely without duplicating plan-level verification data.

## Success Criteria (how to prove "done")

- [ ] Smoke: `bash tests/run_create_execplan_helpers.sh` -> create-execplan helper checks passed
- [ ] `execplan.md` uses the canonical lean sections and compact executable task rows
- [ ] `workspace/execplan-runtime-input.json` contains only derived requirements and task packet fields needed by the harness
- Non-Goals: preserve legacy `fileAnchors` or `verificationScenarios` runtime fields

## Constraints & Guardrails

- Keep shared verification posture in the Context Pack and task-local commands in the task table.
- Keep the runtime artifact derived only from explicit ExecPlan fields.
- Do not preserve legacy section names or legacy runtime artifact fields.

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| codex cli | run fresh phase invocations | `codex --version` | `n/a` | local tool installation | stop and escalate to user on install failure |

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
|        | 1       | 1      | Code | R1,R3 | `skills/create-execplan/scripts/scaffold_execplan.py:1`,`skills/create-execplan/scripts/run_phase.py:1`,`skills/create-execplan/scripts/run_codex_phase.sh:1` | `skills/create-execplan/references/step-0-preflight-workflow.md:1`,`tests/run_create_execplan_helpers.sh:1` | `n/a` | scaffold and controller create deterministic phase artifacts and fresh-run contracts | Add the phase controller, Codex runner wrapper, and scaffolded workspace contracts. |
|        | 1       | 2      | Code | R1,R2,R3 | `skills/create-execplan/scripts/validate_plan_rubric.py:1`,`skills/create-execplan/references/artifact-contract.md:1`,`skills/create-execplan/references/execplan-template.md:1`,`skills/create-execplan/references/context-pack-template.md:1` | `skills/create-execplan/references/step-5-readiness-audit-workflow.md:1`,`skills/create-execplan/references/step-6-checklist-workflow.md:1` | `n/a` | rubric validation and references enforce the new upstream planning contract without changing the final handoff package | Add skeptical rubric checks and update docs/templates/examples to the phase model. |
|        | 2       | 3      | Test | R1,R2,R3 | `n/a` | `tests/run_create_execplan_helpers.sh:1` | `bash tests/run_create_execplan_helpers.sh` | create-execplan helper checks passed | Run the helper regression checks against the updated examples and scaffolder. |

## Progress Log (running)

- (2026-03-24T09:30Z) Draft contract finalized and runtime-input generation moved to post-finalization.

## Decision Log

- Decision: runtime task packets must be explicit enough for a packet-only harness to execute without plan-wide discovery.
  - Rationale: the harness only sees the current task packet, so edit scope, supporting context anchors, and commands must be explicit in that packet.
  - Date: 2026-03-24

## Execution Findings

- Finding: upstream planning quality needs separate validation from the final packet contract.
- Evidence: `skills/create-execplan/scripts/validate_plan_rubric.py`
- Decision link: runtime task packets must be explicit enough for a packet-only harness to execute without plan-wide discovery
- User approval (required if this introduces new discovery scope): not required

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | canonical example artifacts exist | the helper smoke checks run through the resolved runtime | the create-execplan helper suite passes | `bash tests/run_create_execplan_helpers.sh` | P2-T3 |
| S2 | P1 | a fresh phase invocation is launched through the wrapper | the controller runs an isolated design phase | the phase result and manifest are updated from the runner output | `bash tests/run_create_execplan_helpers.sh` | P1-T1 |
| S3 | P1 | rubric validation reads the example workspace artifacts | the readiness checks run | missing approvals, missing structure, and vague packet language all fail validation | `bash tests/run_create_execplan_helpers.sh` | P1-T2 |

## Idempotence & Recovery

Running scaffold with a fresh artifact root is safe. Re-running the controller reruns only the selected phase. Re-running the renderer replaces only the generated runtime input. If validation fails, update the source markdown and rerender instead of editing the JSON directly.
