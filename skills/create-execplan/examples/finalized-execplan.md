# ExecPlan: Demo create-execplan rewrite

- Status: In Progress
- Start: 2026-03-24 • Last Updated: 2026-03-24T09:30:00Z
- Artifact root: `.plan/create-execplan/demo/`
- Workspace root: `.plan/create-execplan/demo/workspace/`
- Context Pack: `.plan/create-execplan/demo/context-pack.md`
- Runtime Input artifact: `.plan/create-execplan/demo/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `.plan/create-execplan/demo/workspace/requirements-freeze.md`
- Draft Review artifact: `.plan/create-execplan/demo/workspace/draft-review.md`
- Links: docs/specs/create-execplan-rewrite.md

## Requirements Freeze

- R1: Keep the ExecPlan as the living human document.
- R2: Generate a narrow runtime input artifact from explicit task packets.
- R3: Keep scaffolded plan metadata and helper examples repo-relative and packet-executable.
- Confirmed by user at: 2026-03-24T09:00:00Z

## Purpose / Big Picture

Deliver a slimmer plan package that keeps the markdown ExecPlan as the human-facing source of truth while generating a smaller, explicit runtime artifact that a packet-only harness can execute safely.

## Success Criteria (how to prove "done")

- [ ] Smoke: `bash tests/run_create_execplan_helpers.sh` -> create-execplan helper checks passed
- [ ] `execplan.md` uses the canonical lean sections and explicit task packet columns
- [ ] `workspace/execplan-runtime-input.json` contains only derived requirements and explicit task packet fields
- Non-Goals: preserve legacy `fileAnchors` or `verificationScenarios` runtime fields

## Constraints & Guardrails

- Keep verification posture and command inventory in the Context Pack.
- Keep the runtime artifact derived only from explicit ExecPlan fields.
- Do not preserve legacy section names or legacy runtime artifact fields.

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| none | no external dependencies beyond repo-standard tooling | `n/a` | `n/a` | n/a | continue with repo-standard tooling only |

## Task Table (single source of truth)

Status keys:

- `@` = in progress
- `X` = complete
- (blank) = outstanding

Task Types:

- Code, Action, Test, Gate

Use `n/a` when `Edit Targets`, `Supporting Context Anchors`, `Allowed Commands`, `Verification Commands`, or `Evidence Commands` does not apply. Every row must:

- map to one or more requirement IDs
- distinguish edit targets from read-only supporting context anchors
- list only commands the executor is allowed to run for that task
- state the expected output or completion signal
- avoid implicit discovery
- keep every runtime row directly executable; do not emit standalone onboarding or human-only rows

| Status | Phase # | Task # | Type | Req IDs | Edit Targets | Supporting Context Anchors | Allowed Commands | Verification Commands | Evidence Commands | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | -------------------------- | ---------------- | --------------------- | ----------------- | --------------- | ------ |
|        | 1       | 1      | Code | R1,R2 | `skills/create-execplan/scripts/render_execplan_runtime_input.py:1`,`skills/create-execplan/scripts/validate_execplan.py:1` | `skills/create-execplan/references/information-placement.md:1`,`skills/create-execplan/references/runtime-input-schema.md:1`,`skills/create-execplan/references/step-4-finalize-execplan-workflow.md:1` | `n/a` | `bash tests/run_create_execplan_helpers.sh` | `bash tests/run_create_execplan_helpers.sh` | runtime input emits schema 3.0 explicit task packets and validator enforces the same contract | Update the runtime renderer and validator to use explicit task packet fields and executable-only task semantics. |
|        | 1       | 2      | Code | R1,R3 | `skills/create-execplan/scripts/scaffold_execplan.py:1`,`skills/create-execplan/references/execplan-template.md:1`,`skills/create-execplan/examples/finalized-execplan.md:1`,`skills/create-execplan/references/context-pack-template.md:1` | `skills/create-execplan/references/step-0-preflight-workflow.md:1`,`skills/create-execplan/references/step-2-context-pack-brownfield.md:1`,`skills/create-execplan/examples/finalized-context-pack.md:1` | `n/a` | `bash tests/run_create_execplan_helpers.sh` | `bash tests/run_create_execplan_helpers.sh` | scaffolded plan artifacts and examples use repo-relative metadata and executable brownfield task rows | Update scaffolded metadata and golden examples to use repo-relative in-repo paths and executable-only packet columns. |
|        | 2       | 3      | Test | R1,R2,R3 | `n/a` | `tests/run_create_execplan_helpers.sh:1` | `bash tests/run_create_execplan_helpers.sh` | `bash tests/run_create_execplan_helpers.sh` | `bash tests/run_create_execplan_helpers.sh` | create-execplan helper checks passed | Run the resolved-runtime helper smoke checks. |

## Progress Log (running)

- (2026-03-24T09:30Z) Draft contract finalized and runtime-input generation moved to post-finalization.

## Decision Log

- Decision: runtime task packets must be explicit enough for a packet-only harness to execute without plan-wide discovery.
  - Rationale: the harness only sees the current task packet, so edit scope, supporting context anchors, and commands must be explicit in that packet.
  - Date: 2026-03-24

## Execution Findings

- Finding: vague brownfield task rows produce execution-time ADRs instead of deterministic implementation.
- Evidence: `skills/create-execplan/references/runtime-input-schema.md`
- Decision link: runtime task packets must be explicit enough for a packet-only harness to execute without plan-wide discovery
- User approval (required if this introduces new discovery scope): not required

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | finalized example artifacts exist | the helper smoke checks run through the resolved runtime | the create-execplan helper suite passes | `bash tests/run_create_execplan_helpers.sh` | P2-T3 |
| S2 | P1 | the runtime renderer and validator read the structured task rows | the helper fixture rerenders the runtime input | the runtime artifact contains only derived explicit packet fields | `bash tests/run_create_execplan_helpers.sh` | P1-T1 |
| S3 | P1 | scaffolded examples and templates use repo-relative metadata | the helper fixture validates the example package | the example ExecPlan stays packet-executable and validator-clean | `bash tests/run_create_execplan_helpers.sh` | P1-T2 |

## Idempotence & Recovery

Running scaffold with a fresh artifact root is safe. Re-running the renderer replaces only the generated runtime input. If validation fails, update the source markdown and rerender instead of editing the JSON directly.
