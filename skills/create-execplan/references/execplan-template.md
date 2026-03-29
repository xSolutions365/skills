# ExecPlan template (living plan)

The ExecPlan is the living execution document. It should stay lean, hold only execution-facing information, and treat the Context Pack as the canonical home for broader repo facts and shared verification posture.

The key design constraint: a lower-reasoning packet-only executor should be able to implement tasks from the structured task rows, using the Context Pack only for navigation and supporting context anchors.
For brownfield plans, keep every task row packet-ready: `Code` rows need concrete edit targets, executable `Action`/`Test`/`Gate` rows need concrete allowed commands, standalone onboarding or human-only rows are not valid runtime tasks, and vague discovery-oriented text is not acceptable.

## Template

```md
# ExecPlan: <short, action-oriented title>

- Status: <Proposed|In Progress|Blocked|Complete>
- Start: <YYYY-MM-DD> • Last Updated: <ISO8601 UTC>
- Artifact root: `.plan/create-execplan/<timestamp>/`
- Workspace root: `.plan/create-execplan/<timestamp>/workspace/`
- Context Pack: `.plan/create-execplan/<timestamp>/context-pack.md`
- Runtime Input artifact: `.plan/create-execplan/<timestamp>/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `.plan/create-execplan/<timestamp>/workspace/requirements-freeze.md`
- Draft Review artifact: `.plan/create-execplan/<timestamp>/workspace/draft-review.md`
- Phase Manifest artifact: `.plan/create-execplan/<timestamp>/workspace/phase-manifest.json`
- Phase Result artifact: `.plan/create-execplan/<timestamp>/workspace/phase-result.json`
- Research Questions artifact: `.plan/create-execplan/<timestamp>/workspace/research-questions.md`
- Research Findings artifact: `.plan/create-execplan/<timestamp>/workspace/research-findings.md`
- Design Options artifact: `.plan/create-execplan/<timestamp>/workspace/design-options.md`
- Structure Outline artifact: `.plan/create-execplan/<timestamp>/workspace/structure-outline.md`
- Links: <issue/PR/spec/runbook>

## Requirements Freeze

- R1:
- R2:
- R3:
- Confirmed by user at: <ISO8601 UTC>

## Purpose / Big Picture

<Explain the user-visible outcome and why it matters.>

## Success Criteria (how to prove "done")

- [ ] Smoke: `<command>` -> <observable smoke result>
- [ ] <observable completed behavior>
- [ ] <observable verification result>
- Non-Goals: <explicit exclusions>

## Constraints & Guardrails

<List the rules that constrain implementation choices, such as architecture, security, or process rules.>

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| <name>     | <why>   | `<command>`   | `<command>`     | <src>  | stop and escalate to user on install failure |

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
- keep every runtime row directly executable; fold onboarding context into supporting anchors on the first executable task instead of creating standalone `Read` or `Human` rows
- stay concrete enough for a packet-only brownfield harness to execute without repo-wide search

- Keep task rows compact:
- `Edit Targets` are the files expected to change for that task.
- `Supporting Context Anchors` are read-only navigation anchors.
- `Commands` are the exact task-local shell commands the executor may run. Scenario-level evidence belongs in `## Test Plan`.

| Status | Phase # | Task # | Type | Req IDs | Edit Targets | Supporting Context Anchors | Commands | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | -------------------------- | -------- | --------------- | ------ |
|        | 1       | 1      | Action | R1 | `n/a` | `path/to/install.md:5`,`path/to/policy.md:8` | `<check-cmd>` | dependency present | Run the dependency precheck before any edits begin. |
|        | 1       | 2      | Gate | R1 | `n/a` | `path/to/install.md:5` | `<dependency-precheck-cmd>` | dependency present or explicit escalation recorded | Run the dependency precheck before any install step and stop for user escalation on failure. |
|        | 2       | 3      | Code | R2 | `path/to/file.py:25` | `path/to/adjacent.py:40`,`path/to/policy.md:8` | `n/a` | code change applied | Implement the required change at the anchored location without expanding beyond the listed edit targets. |
|        | 3       | 4      | Test | R2,R3 | `n/a` | `path/to/test_file.py:1` | `<smoke-cmd>` | <smoke-success-signal> | Run the mandatory smoke verification. |
|        | 3       | 5      | Test | R3 | `n/a` | `path/to/test_file.py:1` | `<test-cmd>` | <expected output> | Run the targeted verification for changed behavior. |

## Progress Log (running)

- (<YYYY-MM-DDThh:mmZ>) <what changed + what is next>

## Decision Log

- Decision: <what>
  - Rationale: <why>
  - Date: <YYYY-MM-DD>

## Execution Findings

- Finding: <what changed from expectation>
- Evidence: `<path/to/artifact>`
- Decision link: <Decision Log entry ID>
- User approval (required if this introduces new discovery scope): <approval note + timestamp>

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1          | P0       | <baseline context> | <trigger action> | <observable smoke outcome> | `<command>` | P3-T5 |
| S2          | P1       | <baseline context> | <trigger action> | <observable outcome> | `<command>` | P3-T6 |

## Idempotence & Recovery

Describe what can be safely re-run and how to recover from destructive or partially applied steps.
```
