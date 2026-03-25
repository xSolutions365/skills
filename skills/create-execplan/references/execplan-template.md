# ExecPlan template (living plan)

The ExecPlan is the living execution document. It should stay lean, hold only execution-facing information, and treat the Context Pack as the canonical home for broader repo facts, verification posture, and command inventory.

The key design constraint: a lower-reasoning executor should be able to implement tasks from the structured task rows, using the Context Pack only for navigation and supporting context.

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

- Code, Read, Action, Test, Gate, Human

Use `n/a` when `File Anchors` or `Command` does not apply. Every row must:

- map to one or more requirement IDs
- include at least one concrete file anchor or command
- state the expected output or completion signal
- avoid implicit discovery

| Status | Phase # | Task # | Type | Req IDs | File Anchors | Command | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | ------- | --------------- | ------ |
|        | 1       | 1      | Read | R1      | `path/to/file:10` | `n/a` | context confirmed | Read the linked context before execution starts. |
|        | 1       | 2      | Action | R1 | `n/a` | `<check-cmd>` | dependency present | Run the dependency precheck. |
|        | 1       | 3      | Gate | R1 | `n/a` | `n/a` | user escalated if install fails | Mark blocked and escalate immediately when installation fails. |
|        | 2       | 4      | Code | R2 | `path/to/file:25` | `n/a` | code change applied | Implement the required change at the anchored location. |
|        | 3       | 5      | Test | R2,R3 | `n/a` | `<smoke-cmd>` | <smoke-success-signal> | Run the mandatory smoke verification. |
|        | 3       | 6      | Test | R3 | `n/a` | `<test-cmd>` | <expected output> | Run the targeted verification for changed behavior. |

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
