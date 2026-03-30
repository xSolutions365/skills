# ExecPlan: Harden create-execplan phase isolation against nested child-agent work

- Status: In Progress
- Start: 2026-03-30 • Last Updated: 2026-03-30T16:46:00Z
- Artifact root: `skills/create-execplan/examples/live-repro-green/`
- Workspace root: `skills/create-execplan/examples/live-repro-green/workspace/`
- Context Pack: `skills/create-execplan/examples/live-repro-green/context-pack.md`
- Runtime Input artifact: `skills/create-execplan/examples/live-repro-green/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `skills/create-execplan/examples/live-repro-green/workspace/requirements-freeze.md`
- Draft Review artifact: `skills/create-execplan/examples/live-repro-green/workspace/draft-review.md`
- Phase Manifest artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-manifest.json`
- Phase Result artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-result.json`
- Research Questions artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-questions.md`
- Research Findings artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md`
- Design Options artifact: `skills/create-execplan/examples/live-repro-green/workspace/design-options.md`
- Structure Outline artifact: `skills/create-execplan/examples/live-repro-green/workspace/structure-outline.md`
- Links: `skills/create-execplan/SKILL.md`

## Requirements Freeze

- R1: Preserve the deterministic `create-execplan` package flow: scaffold, manifest/result checkpointing, fresh `codex exec` phase runs, finalized `execplan.md`, generated runtime input, readiness audit, and handoff checklist.
- R2: Ensure a child phase run cannot invoke nested planning or child-agent orchestration; the effective execution boundary must remain one fresh Codex process working only on staged artifacts.
- R3: Add or tighten regression coverage so the isolation rule is testable with repo-local checks and a live Codex smoke, and the mock package can reach a green readiness audit.
- Confirmed by user at: 2026-03-30T16:10:00Z

## Purpose / Big Picture

Stabilize `create-execplan` child-phase execution so the workflow remains deterministic and auditable even in environments where the parent Codex home carries global delegation rules or skills. The plan keeps the final handoff package shape unchanged while hardening the boundary between parent controller and child phase worker.

## Success Criteria (how to prove "done")

- [ ] Smoke: `CREATE_EXECPLAN_ENABLE_LIVE_CODEX=1 bash tests/run_create_execplan_live_codex_smoke.sh` -> `create-execplan live Codex smoke passed`
- [ ] A live phase reproduction no longer records `spawn_agent` or other agent-management tool calls inside `.codex-phase/stdout.jsonl`
- [ ] `bash tests/run_create_execplan_helpers.sh` passes with assertions for clean `CODEX_HOME`, isolated prompt wording, and required schema fields
- Non-Goals: redesign brownfield source-evidence staging for all isolated phases

## Constraints & Guardrails

- Preserve the existing scaffold, manifest/result checkpointing, readiness audit, and handoff checklist flow.
- Keep the child fix surface narrow to schema, prompt, runtime boundary, and regression coverage.
- Do not reintroduce legacy runtime-input fields or fallback execution modes.

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| codex cli | run child phases and live smoke | `codex --version` | `n/a` | local tool installation | stop and escalate to user on install failure |
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
|        | 1 | 1 | Code | R1,R2 | `skills/create-execplan/scripts/run_phase.py:157`,`skills/create-execplan/scripts/run_phase.py:184` | `skills/create-execplan/SKILL.md:1`,`skills/create-execplan/references/step-1-intake-freeze-workflow.md:1`,`skills/create-execplan/references/step-2-context-pack-workflow.md:1` | `n/a` | child schema and prompt reject recursive planning behavior and satisfy the current API schema contract | Update the phase controller so the child response schema is valid and the child prompt enforces an isolated single-process phase boundary. |
|        | 1 | 2 | Code | R1,R2 | `skills/create-execplan/scripts/run_codex_phase.sh:79` | `skills/create-execplan/scripts/run_phase.py:227`,`skills/create-execplan/references/runtime-resolution.md:1` | `n/a` | child runtime launches inside temporary `CODEX_HOME` with writable staged sandbox | Update the wrapper so child phases do not inherit global Codex home instructions or read-only defaults. |
|        | 2 | 3 | Code | R3 | `tests/run_create_execplan_helpers.sh:56` | `skills/create-execplan/scripts/run_phase.py:157`,`skills/create-execplan/scripts/run_codex_phase.sh:79` | `n/a` | helper regression suite asserts clean `CODEX_HOME`, isolated prompt wording, and schema completeness | Extend the helper checks to lock in the new wrapper and controller contract. |
|        | 2 | 4 | Test | R2,R3 | `n/a` | `tests/run_create_execplan_helpers.sh:1` | `bash tests/run_create_execplan_helpers.sh` | `create-execplan helper checks passed` | Run the helper regression suite after the controller and wrapper changes. |
|        | 2 | 5 | Test | R2,R3 | `n/a` | `tests/run_create_execplan_live_codex_smoke.sh:1` | `CREATE_EXECPLAN_ENABLE_LIVE_CODEX=1 bash tests/run_create_execplan_live_codex_smoke.sh` | `create-execplan live Codex smoke passed` | Run the live smoke to confirm a real child `codex exec` still works after the isolation changes. |

## Progress Log (running)

- (2026-03-30T16:46Z) Mock package updated after reproducing the schema failure and nested child-agent recursion, validating the wrapper isolation fix, and capturing the remaining research-staging tension as out of scope.

## Decision Log

- Decision: isolate child phases at the runtime boundary instead of relying on prompt wording alone.
  - Rationale: the live reproduction showed inherited global Codex instructions can override prompt-only controls and trigger `spawn_agent`.
  - Date: 2026-03-30

- Decision: keep brownfield source-evidence staging out of the immediate fix scope.
  - Rationale: the reproduced defect is child runtime isolation; redesigning how all brownfield phases consume repo evidence is a larger controller change.
  - Date: 2026-03-30

## Execution Findings

- Finding: a live `requirements-freeze` run first failed on `invalid_json_schema`, then invoked `spawn_agent` once the schema bug was fixed but the inherited global Codex home was still present.
- Evidence: `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md`
- Decision link: isolate child phases at the runtime boundary instead of relying on prompt wording alone
- User approval (required if this introduces new discovery scope): not required

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` values like `P2-T4` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | the wrapper launches a real child `codex exec` | the live smoke harness runs with `CREATE_EXECPLAN_ENABLE_LIVE_CODEX=1` | the wrapper returns structured JSON and the smoke passes | `CREATE_EXECPLAN_ENABLE_LIVE_CODEX=1 bash tests/run_create_execplan_live_codex_smoke.sh` | P2-T5 |
| S2 | P1 | the fake-Codex helper harness captures wrapper and prompt details | the helper regression suite runs | prompt isolation rules, clean `CODEX_HOME`, and required schema fields all hold | `bash tests/run_create_execplan_helpers.sh` | P2-T4 |
| S3 | P1 | a child phase is launched from the fixed controller | the `requirements-freeze` reproduction writes `.codex-phase/stdout.jsonl` | no `spawn_agent` event appears in the child event log | `bash tests/run_create_execplan_helpers.sh` | P1-T1 |

## Idempotence & Recovery

Re-running the controller reruns only the selected phase. Re-running the helper or live smoke checks is safe and should not mutate repo state. Re-running readiness audit regenerates the runtime input from the markdown sources. If validation fails, update the source markdown or wrapper/controller code and rerun the validators instead of editing generated JSON by hand.
