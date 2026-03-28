# Context Pack: Demo create-execplan rewrite

- Created: 2026-03-24
- Repo root: `.`
- Target path: `.`
- Project mode: `brownfield`
- Artifact root: `.plan/create-execplan/demo`
- Workspace root: `.plan/create-execplan/demo/workspace`
- Related links: docs/specs/create-execplan-rewrite.md

## Change Brief (1-3 paragraphs)

This example package demonstrates the rewritten create-execplan contract. It keeps shared verification posture in the Context Pack, keeps task-local execution details in the ExecPlan, and uses a derived runtime input artifact for tooling.

## Requirement Freeze (user-confirmed)

- R1: Keep the ExecPlan as the living human document.
- R2: Generate a narrow runtime input artifact from explicit task packets.
- R3: Keep scaffolded plan metadata and helper examples repo-relative and packet-executable.
- Confirmed by user at: 2026-03-24T09:00:00Z

## Discovery Inputs

- Intake artifact: `.plan/create-execplan/demo/workspace/context-discovery.md`
- Evidence artifact: `.plan/create-execplan/demo/workspace/context-evidence.json`
- Codemap artifact: `.plan/create-execplan/demo/workspace/context-codemap.md`
- Requirements freeze artifact: `.plan/create-execplan/demo/workspace/requirements-freeze.md`
- Notes: The example is intentionally small and uses repo-local references only.

## Guardrails (must-follow)

- Repository rules: keep the ExecPlan lean and avoid duplicate plan surfaces.
- Security/privacy constraints: do not print secrets in validation or helper output.
- Prohibited actions: do not edit the generated runtime input by hand.

## Research Scope & Recency Policy

- Online research allowed: no
- Approved source types: local repository references only
- Approved domains/APIs: none
- Recency expectation: local repository truth only
- Exception handling: not permitted

## Evidence Inventory

| Evidence ID | Type | Source | Published | Retrieved | Trust rationale |
| ----------- | ---- | ------ | --------- | --------- | --------------- |
| E1 | doc | skills/create-execplan/references/openai-codex-exec-plans.md | undated:repo-reference | 2026-03-24 | baseline structure reference |
| E2 | code | skills/create-execplan/scripts/render_execplan_runtime_input.py | undated:repo-reference | 2026-03-24 | renderer implementation reference |

## Verification Baseline & Strategy

- Verification scenario: `brownfield-existing`
- Existing verification commands: `bash scripts/run-ci-quality-gates.sh`
- User decision when verification missing: `n/a-existing`
- Planned verification scope: update create-execplan docs, templates, helper scripts, and golden examples touched by the rewrite
- Mandatory smoke gate command: `bash tests/run_create_execplan_helpers.sh`
- Smoke gate expected success signal: create-execplan helper checks passed

## Existing Change Surface (required for brownfield; optional for greenfield)

| Area | File anchor | Current behavior | Integration concern | Evidence IDs |
| ---- | ----------- | ---------------- | ------------------- | ------------ |
| runtime input | `skills/create-execplan/scripts/render_execplan_runtime_input.py:1` | renderer currently emits the legacy runtime packet shape | runtime artifact must stay narrow and explicit for packet-only execution | E2 |

## Repo Facts (execution-relevant only)

- Languages/frameworks: Python and Bash
- Package manager(s): none required for helper execution
- Build tooling: none
- Test tooling: shell quality gates plus Python helper validation
- Key environment variables/config files: none required beyond a resolved Python runtime

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Expected success signal |
| ---------- | ------- | ------------- | --------------- | ------ | ----------------------- |
| none | no external dependencies beyond repo-standard tooling | `n/a` | `n/a` | n/a | n/a |

## Code Map (line-numbered)

List only the places the executor must touch. Prefer `path:line` anchors.

| Area | File anchor | What it contains | Why it matters | Planned change |
| ---- | ----------- | ---------------- | -------------- | -------------- |
| scaffolded paths | `skills/create-execplan/scripts/scaffold_execplan.py:1` | scaffold helper that materializes the plan package | in-repo artifact metadata should default to repo-relative paths for worktree portability | render repo-relative artifact metadata |
| runtime renderer | `skills/create-execplan/scripts/render_execplan_runtime_input.py:1` | derived runtime artifact renderer | runtime artifact must serialize only explicit task packet fields | replace legacy packet output |

## Requirement to Evidence Traceability

| Requirement ID | Requirement | Evidence IDs | Context section(s) | Planned task refs |
| -------------- | ----------- | ------------ | ------------------ | ----------------- |
| R1 | Keep the ExecPlan as the living human document. | E1 | Change Brief, Existing Change Surface | P1-T1,P3-T4 |
| R2 | Generate a narrow runtime input artifact from explicit task packets. | E1,E2 | Existing Change Surface, Code Map | P2-T2,P3-T4 |
| R3 | Keep scaffolded plan metadata and helper examples repo-relative and packet-executable. | E2 | Verification Baseline & Strategy, Code Map | P1-T2,P2-T3 |

## Contracts & Interfaces

Only include what the change touches:

- plan package artifact paths
- helper script invocation contract
- runtime input JSON schema
- in-repo artifact path portability

## Risk Register

| Risk | Impact | Mitigation | Verification command | Evidence IDs |
| ---- | ------ | ---------- | -------------------- | ------------ |
| packet/schema drift | helper examples and emitted runtime input diverge from the harness packet contract | keep the examples, renderer, validator, and scaffold aligned to one explicit schema | `bash tests/run_create_execplan_helpers.sh` | E2 |
