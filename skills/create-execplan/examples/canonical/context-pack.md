# Context Pack: Demo create-execplan rewrite

- Created: 2026-03-24
- Repo root: `.`
- Target path: `.`
- Project mode: `brownfield`
- Artifact root: `.plan/create-execplan/demo`
- Workspace root: `.plan/create-execplan/demo/workspace`
- Related links: docs/specs/create-execplan-rewrite.md

## Change Brief (1-3 paragraphs)

This example package demonstrates the Codex-first phase orchestration model while preserving the existing handoff package. The intermediate workspace artifacts carry clarification, research, design, and structure decisions forward without leaking raw transcript history.

## Requirement Freeze (user-confirmed)

- R1: Keep the ExecPlan as the living human document.
- R2: Preserve the narrow runtime input artifact for packet-only execution.
- R3: Record upstream planning and approval evidence in workspace artifacts.
- Confirmed by user at: 2026-03-24T09:00:00Z

## Discovery Inputs

- Intake artifact: `.plan/create-execplan/demo/workspace/context-discovery.md`
- Evidence artifact: `.plan/create-execplan/demo/workspace/context-evidence.json`
- Codemap artifact: `.plan/create-execplan/demo/workspace/context-codemap.md`
- Requirements freeze artifact: `.plan/create-execplan/demo/workspace/requirements-freeze.md`
- Phase manifest artifact: `.plan/create-execplan/demo/workspace/phase-manifest.json`
- Latest phase result artifact: `.plan/create-execplan/demo/workspace/phase-result.json`
- Research questions artifact: `.plan/create-execplan/demo/workspace/research-questions.md`
- Research findings artifact: `.plan/create-execplan/demo/workspace/research-findings.md`
- Design options artifact: `.plan/create-execplan/demo/workspace/design-options.md`
- Structure outline artifact: `.plan/create-execplan/demo/workspace/structure-outline.md`
- Notes: The example package uses repo-local references only.

## Guardrails (must-follow)

- Repository rules: keep the final package unchanged and keep packet rows explicit.
- Security/privacy constraints: do not print secrets in helper output.
- Prohibited actions: do not edit the derived runtime input by hand.

## Research Scope & Recency Policy

- Online research allowed: no
- Approved source types: local repository references only
- Approved domains/APIs: none
- Recency expectation: local repository truth only
- Exception handling: not permitted

## Evidence Inventory

| Evidence ID | Type | Source | Published | Retrieved | Trust rationale |
| ----------- | ---- | ------ | --------- | --------- | --------------- |
| E1 | doc | skills/create-execplan/references/artifact-contract.md | undated:repo-reference | 2026-03-24 | canonical artifact contract reference |
| E2 | code | skills/create-execplan/scripts/run_phase.py | undated:repo-reference | 2026-03-24 | deterministic phase controller reference |

## Verification Baseline & Strategy

- Verification scenario: `brownfield-existing`
- Existing verification commands: `bash tests/run_create_execplan_helpers.sh`
- User decision when verification missing: `n/a-existing`
- Planned verification scope: validate scaffolded artifacts, runner contract, rubric checks, and runtime-input generation
- Mandatory smoke gate command: `bash tests/run_create_execplan_helpers.sh`
- Smoke gate expected success signal: create-execplan helper checks passed

## Existing Change Surface (required for brownfield; optional for greenfield)

| Area | File anchor | Current behavior | Integration concern | Evidence IDs |
| ---- | ----------- | ---------------- | ------------------- | ------------ |
| phase controller | `skills/create-execplan/scripts/run_phase.py:1` | routes one phase at a time through a fresh runner invocation | must enforce artifact-only handoff for isolated phases | E2 |

## Repo Facts (execution-relevant only)

- Languages/frameworks: Python and Bash
- Package manager(s): none required for helper execution
- Build tooling: none
- Test tooling: shell helper checks plus Python validators
- Key environment variables/config files: no special environment required beyond a resolved Python runtime

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Expected success signal |
| ---------- | ------- | ------------- | --------------- | ------ | ----------------------- |
| codex cli | run fresh phase invocations | `codex --version` | `n/a` | local tool installation | Codex CLI responds |

## Code Map (line-numbered)

List only the places the executor must touch. Prefer repo-relative `path:line` anchors for in-repo files.

| Area | File anchor | What it contains | Why it matters | Planned change |
| ---- | ----------- | ---------------- | -------------- | -------------- |
| scaffold | `skills/create-execplan/scripts/scaffold_execplan.py:1` | scaffold logic for final and intermediate artifacts | must create canonical workspace contracts | materialize phase artifacts |
| controller | `skills/create-execplan/scripts/run_phase.py:1` | phase routing and handoff enforcement | defines fresh-process behavior | enforce phase contracts |

## Requirement to Evidence Traceability

| Requirement ID | Requirement | Evidence IDs | Context section(s) | Planned task refs |
| -------------- | ----------- | ------------ | ------------------ | ----------------- |
| R1 | Keep the ExecPlan as the living human document. | E1,E2 | Change Brief, Code Map | P1-T1,P2-T3 |
| R2 | Preserve the narrow runtime input artifact for packet-only execution. | E1 | Change Brief, Verification Baseline & Strategy | P1-T2,P2-T3 |
| R3 | Record upstream planning and approval evidence in workspace artifacts. | E2 | Discovery Inputs, Code Map | P1-T1,P2-T2 |

## Contracts & Interfaces

Only include what the change touches:

- phase manifest and phase result JSON contracts
- workspace artifact layout
- helper script invocation contract
- runtime input JSON schema

## Risk Register

| Risk | Impact | Mitigation | Verification command | Evidence IDs |
| ---- | ------ | ---------- | -------------------- | ------------ |
| phase contamination | later planning phases inherit hidden prior context | run isolated phases from curated artifact-only workdirs | `bash tests/run_create_execplan_helpers.sh` | E2 |
