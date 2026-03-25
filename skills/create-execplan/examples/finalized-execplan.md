# ExecPlan: Demo create-execplan rewrite

- Status: In Progress
- Start: 2026-03-24 • Last Updated: 2026-03-24T09:30:00Z
- Artifact root: `/repo/.plan/create-execplan/demo/`
- Workspace root: `/repo/.plan/create-execplan/demo/workspace/`
- Context Pack: `/repo/.plan/create-execplan/demo/context-pack.md`
- Runtime Input artifact: `/repo/.plan/create-execplan/demo/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `/repo/.plan/create-execplan/demo/workspace/requirements-freeze.md`
- Draft Review artifact: `/repo/.plan/create-execplan/demo/workspace/draft-review.md`
- Links: docs/specs/create-execplan-rewrite.md

## Requirements Freeze

- R1: Keep the ExecPlan as the living human document.
- R2: Generate a narrow runtime input artifact from explicit task rows.
- R3: Remove hardcoded python3 usage from shell-facing invocations.
- Confirmed by user at: 2026-03-24T09:00:00Z

## Purpose / Big Picture

Deliver a slimmer plan package that gives humans the living markdown document and gives tooling a smaller derived runtime artifact without creating a second plan.

## Success Criteria (how to prove "done")

- [ ] Smoke: `bash tests/run_create_execplan_helpers.sh` -> create-execplan helper checks passed
- [ ] `execplan.md` uses only the canonical lean sections and the structured task table
- [ ] `workspace/execplan-runtime-input.json` contains only derived requirements, tasks, and verification scenarios
- Non-Goals: preserve legacy section names or the legacy runtime artifact name

## Constraints & Guardrails

- Keep verification posture and command inventory in the Context Pack.
- Keep the runtime artifact derived only from explicit ExecPlan fields.
- Do not preserve legacy section names or legacy runtime artifact references.

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

- Code, Read, Action, Test, Gate, Human

Use `n/a` when `File Anchors` or `Command` does not apply. Every row must:

- map to one or more requirement IDs
- include at least one concrete file anchor or command
- state the expected output or completion signal
- avoid implicit discovery

| Status | Phase # | Task # | Type | Req IDs | File Anchors | Command | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | ------- | --------------- | ------ |
|        | 1       | 1      | Read | R1 | `skills/create-execplan/references/information-placement.md:1` | `n/a` | placement rules understood | Read the canonical information placement rules before editing the plan contract. |
|        | 2       | 2      | Code | R2 | `skills/create-execplan/scripts/render_execplan_runtime_input.py:1` | `n/a` | runtime input derives from explicit task columns | Update the renderer to serialize only derived task and scenario fields. |
|        | 2       | 3      | Code | R3 | `skills/create-execplan/scripts/scaffold_execplan.py:1` | `n/a` | scaffold leaves runtime input ungenerated until finalization | Update the scaffold flow to stop before runtime-input generation. |
|        | 3       | 4      | Test | R1,R2,R3 | `n/a` | `bash tests/run_create_execplan_helpers.sh` | create-execplan helper checks passed | Run the resolved-runtime helper smoke checks. |

## Progress Log (running)

- (2026-03-24T09:30Z) Draft contract finalized and runtime-input generation moved to post-finalization.

## Decision Log

- Decision: runtime selection happens at the shell boundary and not inside every shell invocation.
  - Rationale: one resolver keeps shell-facing invocation portable while helper scripts stay in Python.
  - Date: 2026-03-24

## Execution Findings

- Finding: verification posture and command inventory create duplication when copied into standalone ExecPlan sections.
- Evidence: `skills/create-execplan/references/information-placement.md`
- Decision link: runtime selection happens at the shell boundary and not inside every shell invocation
- User approval (required if this introduces new discovery scope): not required

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | finalized example artifacts exist | the helper smoke checks run through the resolved runtime | the create-execplan helper suite passes | `bash tests/run_create_execplan_helpers.sh` | P3-T4 |
| S2 | P1 | the runtime renderer reads the structured task rows | the helper fixture check rerenders the runtime input | the runtime artifact contains only derived structure | `bash tests/run_create_execplan_helpers.sh` | P2-T2,P2-T3 |

## Idempotence & Recovery

Running scaffold with a fresh artifact root is safe. Re-running the renderer replaces only the generated runtime input. If validation fails, update the source markdown and rerender instead of editing the JSON directly.
