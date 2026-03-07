# ExecPlan template (living plan)

The ExecPlan is the living execution document. It should be _lean_ and reference the Context Pack instead of duplicating repo orientation.

The key design constraint: a low-reasoning executor should be able to implement tasks by following the table rows, using the Context Pack for navigation.

## Template

```md
# ExecPlan: <short, action-oriented title>

- Status: <Proposed|In Progress|Blocked|Complete>
- Start: <YYYY-MM-DD> • Last Updated: <ISO8601 UTC>
- Artifact root: `.plan/create-execplan/<timestamp>/`
- Workspace root: `.plan/create-execplan/<timestamp>/workspace/`
- Context Pack: `.plan/create-execplan/<timestamp>/context-pack.md`
- Requirements Freeze artifact: `.plan/create-execplan/<timestamp>/workspace/requirements-freeze.md`
- Draft Review artifact: `.plan/create-execplan/<timestamp>/workspace/draft-review.md`
- Links: <issue/PR/spec/runbook>

## Executor Contract

- Allowed inputs: working tree + Context Pack + ExecPlan
- Required output: implemented change + updated ExecPlan + verification evidence
- Forbidden: undefined discovery tasks after requirements are frozen

## Requirements Freeze

- R1:
- R2:
- R3:
- Confirmed by user at: <ISO8601 UTC>

## Purpose / Big Picture

<Explain user-visible outcome and why it matters.>

## Success Criteria (how to prove “done”)

- [ ] <Smoke command + expected smoke result>
- [ ] <Command + expected output>
- [ ] <Command + expected output>
- Non-Goals: <explicit exclusions>

## Constraints & Guardrails

<List the rules that constrain implementation choices (quality gates, architecture constraints, security/privacy constraints).>

## Verification Strategy

- Scenario: <greenfield-setup|brownfield-existing|brownfield-none>
- Existing verification reused:
- Added verification scope:
- Minimum smoke gate command:
- If verification is missing, user decision: <approved-change-scoped|declined-blocked|n/a-existing>

## Dependency Preconditions

| Dependency | Check command | Install command | Source   | Hard-fail behavior                           |
| ---------- | ------------- | --------------- | -------- | -------------------------------------------- |
| <name>     | `<command>`   | `<command>`     | <source> | stop and escalate to user on install failure |

## Plan Overview (phases)

Keep to 3–6 phases. Each phase describes what will exist at the end and how to verify it.

- Phase 1: <objective + proof>
- Phase 2: <objective + proof>
- Phase 3: <objective + proof>

## Task Table (single source of truth)

Status keys:

- `@` = in progress
- `X` = complete
- (blank) = outstanding

Task Types:

- Code, Read, Action, Test, Gate, Human

Write each row as an explicit action. Every task must include one or more:

- file anchors: `path/to/file:line`
- commands to run
- expected outputs
- no task may rely on implicit discovery

| Status | Phase # | Task # | Type   | Description                                                                                |
| ------ | ------- | ------ | ------ | ------------------------------------------------------------------------------------------ |
|        | 1       | 1      | Read   | Read Context Pack at `.../context-pack.md` and confirm constraints + commands are correct. |
|        | 1       | 2      | Action | Run dependency check `<check-cmd>`; if missing run `<install-cmd>` from `<source>`.        |
|        | 1       | 3      | Gate   | If dependency install fails, mark Blocked, log evidence, and escalate to user immediately. |
|        | 2       | 4      | Action | Run `<quality-gate-cmd>` and record baseline results in Artifacts & Notes.                 |
|        | 3       | 5      | Code   | Edit `path/to/file:line` to <change>.                                                      |
|        | 3       | 6      | Test   | Run mandatory smoke command `<smoke-cmd>` and confirm `<smoke-success-signal>`.            |
|        | 3       | 7      | Test   | Run `<test-cmd>` and confirm <expected output>.                                            |

## Progress Log (running)

- (<YYYY-MM-DDThh:mmZ>) <what changed + what’s next>

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
- Do not paste command inventories here; keep broad command catalogs in `Quality Gates` and task rows.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to an executable command.

| Scenario ID | Req IDs | Priority | Given              | When             | Then                 | Evidence Command | Task Ref |
| ----------- | ------- | -------- | ------------------ | ---------------- | -------------------- | ---------------- | -------- |
| S1          | R1,R2   | P0       | <baseline context> | <trigger action> | <observable outcome> | `<command>`      | P3-T6    |
| S2          | R3      | P1       | <baseline context> | <trigger action> | <observable outcome> | `<command>`      | P3-T7    |

## Quality Gates

| Gate  | Command | Expectation                                 |
| ----- | ------- | ------------------------------------------- |
| Smoke | `<cmd>` | smoke scenario passes                       |
| Lint  | `<cmd>` | 0 errors                                    |
| Test  | `<cmd>` | required suite and changed-scope tests pass |

## Idempotence & Recovery

Describe what can be safely re-run and how to rollback any destructive steps.

## Artifacts & Notes

- Context Pack: `<path>`
- Evidence: `<path/to/log-or-json>`
```
