# ExecPlan: Greenfield Fixture

- Status: Proposed
- Start: 2026-04-01 • Last Updated: 2026-04-01T09:15:00Z
- Artifact root: `.plan/create-execplan/greenfield-fixture/`
- Workspace root: `.plan/create-execplan/greenfield-fixture/workspace/`
- Context Pack: `.plan/create-execplan/greenfield-fixture/context-pack.md`
- Runtime Input artifact: `.plan/create-execplan/greenfield-fixture/workspace/execplan-runtime-input.json` (generated after finalization; do not edit)
- Requirements Freeze artifact: `.plan/create-execplan/greenfield-fixture/workspace/requirements-freeze.md`
- Draft Review artifact: `.plan/create-execplan/greenfield-fixture/workspace/draft-review.md`
- Links: n/a

## Requirements Freeze

- R1: Create a new CLI package with a typed entrypoint.
- R2: Use an established CLI library instead of a bespoke parser.
- R3: Define an executable smoke path for the initial greenfield implementation.
- Confirmed by user at: 2026-04-01T09:00:00Z

## Purpose / Big Picture

Create a minimal greenfield CLI slice with an established typed command library and an executable smoke path.

## Success Criteria (how to prove "done")

- [ ] Smoke: `uv run pytest tests/test_cli.py tests/test_smoke.py` -> greenfield smoke tests pass
- [ ] `pyproject.toml` and `src/greenfield_app/cli.py` define a typed CLI entrypoint.
- [ ] Runtime input stays derived from the compact task rows with no duplicate verification arrays.
- Non-Goals: design a bespoke CLI framework; expand beyond the first command path; add hidden fallback behavior.

## Constraints & Guardrails

- Use an established CLI library selected in the Context Pack.
- Keep the runtime artifact derived only from explicit ExecPlan fields.
- Keep the initial slice narrow and executable.

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Hard-fail behavior |
| ---------- | ------- | ------------- | --------------- | ------ | ------------------ |
| `uv` | run installs and tests for the greenfield slice | `uv --version` | `brew install uv` | Homebrew | stop and install `uv` before proceeding |

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

| Status | Phase # | Task # | Type | Req IDs | Edit Targets | Supporting Context Anchors | Commands | Expected Output | Action |
| ------ | ------- | ------ | ---- | ------- | ------------ | -------------------------- | -------- | --------------- | ------ |
|        | 1       | 1      | Code | R1,R2 | `pyproject.toml:1`,`src/greenfield_app/cli.py:1` | `docs/greenfield-spec.md:1`,`tests/test_cli.py:1` | `n/a` | typed CLI entrypoint and dependency wiring added | Create the initial CLI package using the selected established library. |
|        | 2       | 2      | Test | R1,R2,R3 | `n/a` | `tests/test_cli.py:1`,`tests/test_smoke.py:1` | `uv run pytest tests/test_cli.py tests/test_smoke.py` | greenfield smoke tests pass | Run the greenfield smoke and CLI tests. |

## Progress Log (running)

- (2026-04-01T09:15Z) Finalized the greenfield fixture package for contract validation.

## Decision Log

- Decision: Use an established typed CLI library for the initial command surface.
  - Rationale: It reduces bespoke code and keeps the first slice narrow.
  - Date: 2026-04-01

## Execution Findings

- Finding: greenfield packages still need the same compact task-row contract as brownfield packages.
- Evidence: `workspace/execplan-runtime-input.json`
- Decision link: Use an established typed CLI library for the initial command surface.
- User approval (required if this introduces new discovery scope): not required for the fixture validation package.

## Test Plan

Use scenario-focused BDD coverage for changed behavior and high-risk regressions.

- Keep `Given`, `When`, and `Then` to one concise line each.
- Keep evidence commands executable.
- Use `Task Ref` format `P<phase>-T<task>` and ensure each row maps to one or more executable task rows.

| Scenario ID | Priority | Given | When | Then | Evidence Command | Task Ref |
| ----------- | -------- | ----- | ---- | ---- | ---------------- | -------- |
| S1 | P0 | the greenfield CLI package is scaffolded | `uv run pytest tests/test_cli.py tests/test_smoke.py` runs | the first command path and smoke tests pass | `uv run pytest tests/test_cli.py tests/test_smoke.py` | P2-T2 |

## Idempotence & Recovery

Re-running the runtime renderer is safe because it replaces only the generated JSON artifact. If validation fails, update the source markdown and rerender instead of editing the JSON directly.
