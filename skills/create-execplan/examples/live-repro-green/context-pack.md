# Context Pack: Harden create-execplan phase isolation

- Created: 2026-03-30
- Repo root: `.`
- Target path: `.`
- Project mode: `brownfield`
- Artifact root: `skills/create-execplan/examples/live-repro-green`
- Workspace root: `skills/create-execplan/examples/live-repro-green/workspace`
- Related links: `skills/create-execplan/SKILL.md`

## Change Brief (1-3 paragraphs)

This mock package captures a brownfield maintenance change for `create-execplan`. The validated outcome is to keep the existing deterministic package flow intact while moving non-deterministic phases onto staged worker packets and parent-managed subagent execution.

The immediate fix surface is narrow: replace the subprocess wrapper with `prepare/apply`, harden the worker prompt and schema, keep approvals in the parent layer, and extend regression coverage to prove the staged worker contract holds. A separate brownfield research-staging tension remains for phases that need repo evidence not present in staged artifacts, but that redesign is explicitly out of scope for this change.

## Requirement Freeze (user-confirmed)

- R1: Preserve the deterministic `create-execplan` package flow: scaffold, manifest/result checkpointing, staged `prepare/apply` control steps, fresh worker subagents, finalized `execplan.md`, generated runtime input, readiness audit, and handoff checklist.
- R2: Ensure a child phase run cannot invoke nested planning or child-agent orchestration; the effective execution boundary must remain one fresh worker subagent working only on staged artifacts.
- R3: Add or tighten regression coverage so the isolation rule is testable with repo-local checks and a live installed-skill run, and the mock package can reach a green readiness audit.
- Confirmed by user at: 2026-03-30T16:10:00Z

## Discovery Inputs

- Intake artifact: `skills/create-execplan/examples/live-repro-green/workspace/context-discovery.md`
- Evidence artifact: `skills/create-execplan/examples/live-repro-green/workspace/context-evidence.json`
- Codemap artifact: `skills/create-execplan/examples/live-repro-green/workspace/context-codemap.md`
- Requirements freeze artifact: `skills/create-execplan/examples/live-repro-green/workspace/requirements-freeze.md`
- Planning brief artifact: `skills/create-execplan/examples/live-repro-green/workspace/planning-brief.md`
- Phase manifest artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-manifest.json`
- Latest phase result artifact: `skills/create-execplan/examples/live-repro-green/workspace/phase-result.json`
- Research questions artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-questions.md`
- Research findings artifact: `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md`
- Design options artifact: `skills/create-execplan/examples/live-repro-green/workspace/design-options.md`
- Structure outline artifact: `skills/create-execplan/examples/live-repro-green/workspace/structure-outline.md`
- Notes: mock approvals were recorded by the parent controller to complete the end-to-end validation run, including the approved planning brief that bounded later worker phases.

## Guardrails (must-follow)

- Repository rules: do not reintroduce legacy packet artifacts, fallback modes, or backward-compatibility branches.
- Security/privacy constraints: do not print secrets in helper output; copy only authentication state needed for child Codex execution.
- Prohibited actions: do not hand-edit the derived runtime input; do not let child phases inherit global Codex home instructions.

## Research Scope & Recency Policy

- Online research allowed: no
- Approved source types: local repository code, tests, and generated repro artifacts only
- Approved domains/APIs: none
- Recency expectation: repository-local truth only
- Exception handling: external sources are not permitted for this mock scenario

## Evidence Inventory

| Evidence ID | Type | Source | Published | Retrieved | Trust rationale |
| ----------- | ---- | ------ | --------- | --------- | --------------- |
| E1 | code | `skills/create-execplan/scripts/run_phase.py` | undated:repo-reference | 2026-03-30 | canonical phase controller and prompt/schema source |
| E2 | code | `skills/create-execplan/SKILL.md` | undated:repo-reference | 2026-03-30 | canonical parent and worker orchestration contract |
| E3 | test | `tests/run_create_execplan_helpers.sh` | undated:repo-reference | 2026-03-30 | regression harness for wrapper/controller behavior |
| E4 | doc | `skills/create-execplan/references/manual-acceptance.md` | undated:repo-reference | 2026-03-30 | installed-skill live acceptance flow |
| E5 | artifact | `skills/create-execplan/examples/live-repro-green/workspace/research-findings.md` | 2026-03-30 | 2026-03-30 | summarized repro evidence and known tensions from the mock run |

## Verification Baseline & Strategy

- Verification scenario: `brownfield-existing`
- Existing verification commands: `bash tests/run_create_execplan_helpers.sh`; installed-skill manual acceptance using `skills/create-execplan/references/manual-acceptance.md`
- User decision when verification missing: `n/a-existing`
- Planned verification scope: validate the controller schema contract, staged worker packet isolation, apply-time validation, helper regression expectations, and installed-skill behavior
- Mandatory smoke gate command: `bash tests/run_create_execplan_helpers.sh`
- Smoke gate expected success signal: `create-execplan helper checks passed`

## Existing Change Surface (required for brownfield; optional for greenfield)

| Area | File anchor | Current behavior | Integration concern | Evidence IDs |
| ---- | ----------- | ---------------- | ------------------- | ------------ |
| phase controller | `skills/create-execplan/scripts/run_phase.py:157` | builds the child response schema and prompt contract | schema drift or permissive prompt wording can fail the child before work starts or allow recursive behavior | E1,E5 |
| skill contract | `skills/create-execplan/SKILL.md:1` | defines parent-owned approvals and single-worker phase execution | weak parent/worker rules could reintroduce nested delegation | E2,E5 |
| helper regression coverage | `tests/run_create_execplan_helpers.sh:1` | validates prepare/apply behavior with synthetic worker results | must assert the new isolation boundary so regressions fail locally | E3 |

## Repo Facts (execution-relevant only)

- Languages/frameworks: Python and Bash
- Package manager(s): none required beyond a working Python interpreter
- Build tooling: none
- Test tooling: shell helper checks, manual installed-skill acceptance, Python validators
- Key environment variables/config files: none beyond the parent Codex runtime

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Expected success signal |
| ---------- | ------- | ------------- | --------------- | ------ | ----------------------- |
| codex app | host parent and worker subagents | `n/a` | `n/a` | Codex desktop/app runtime | subagent tools are available |
| python runtime | run the controller and validators | `./skills/create-execplan/scripts/resolve_python.sh` | `n/a` | local tool installation | resolver prints an executable interpreter path |

## Code Map (line-numbered)

List only the places the executor must touch. Prefer repo-relative `path:line` anchors for in-repo files.

| Area | File anchor | What it contains | Why it matters | Planned change |
| ---- | ----------- | ---------------- | -------------- | -------------- |
| phase schema | `skills/create-execplan/scripts/run_phase.py:157` | child response schema construction | current API rejects schemas that omit required keys | require `blockingIssues` |
| phase prompt | `skills/create-execplan/scripts/run_phase.py:184` | child prompt and hard rules | must keep child work limited to staged artifacts and forbid recursive planning behavior | harden prompt boundaries |
| manual acceptance | `skills/create-execplan/references/manual-acceptance.md:1` | installed-skill live verification flow | proves the deployed skill uses the new parent/worker contract | document the live check |
| regression harness | `tests/run_create_execplan_helpers.sh:1` | helper regression checks | proves prepare/apply and packet validation locally | assert isolation and schema invariants |

## Requirement to Evidence Traceability

| Requirement ID | Requirement | Evidence IDs | Context section(s) | Planned task refs |
| -------------- | ----------- | ------------ | ------------------ | ----------------- |
| R1 | Preserve deterministic package flow and final artifact model. | E1,E2,E5 | Change Brief, Existing Change Surface, Code Map | P1-T1,P1-T2 |
| R2 | Keep each child phase to one fresh worker subagent with no nested planning or child-agent orchestration. | E1,E2,E5 | Change Brief, Verification Baseline & Strategy, Risk Register | P1-T1,P1-T2,P2-T4 |
| R3 | Keep the isolation rule regression-testable with repo-local checks and installed-skill acceptance. | E3,E4,E5 | Verification Baseline & Strategy, Code Map | P2-T3,P2-T4 |

## Contracts & Interfaces

Only include what the change touches:

- child response JSON schema
- child phase prompt contract
- staged worker packet contract
- helper and manual acceptance verification entrypoints

## Risk Register

| Risk | Impact | Mitigation | Verification command | Evidence IDs |
| ---- | ------ | ---------- | -------------------- | ------------ |
| worker prompt or apply contract weakens | nested child-agent work or invalid phase output affects deterministic execution | keep parent-owned approvals and reject invalid worker results in `apply` | `bash tests/run_create_execplan_helpers.sh` | E2,E3,E5 |
| brownfield research still lacks staged source evidence | later isolated phases cannot inspect repo code by path alone | keep immediate fix narrow and record the staging gap as follow-on design work | `bash tests/run_create_execplan_helpers.sh` | E4,E5 |
