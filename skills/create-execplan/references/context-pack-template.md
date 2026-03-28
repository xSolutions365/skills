# Context Pack template (durable execution context)

The Context Pack is the durable context artifact. It minimizes repeat discovery and remains the canonical home for repo facts, shared verification posture, traceability, and line-anchored change surface information.

Use it to capture:

- The minimum repo facts required to execute changes safely.
- A line-numbered code map that points to the exact change surface.
- Shared verification baseline without duplicating task-local commands into the living ExecPlan.

## Template

```md
# Context Pack: <short title>

- Created: <YYYY-MM-DD>
- Repo root: `<repo-relative-path>`
- Target path: `<path-or-.>`
- Project mode: `<greenfield|brownfield>`
- Artifact root: `<artifact-root>`
- Workspace root: `<workspace-root>`
- Related links: <issue/PR/spec URLs or file paths>

## Change Brief (1-3 paragraphs)

<Restate the user-visible outcome, scope, and constraints in plain language.>

## Requirement Freeze (user-confirmed)

- R1:
- R2:
- R3:
- Confirmed by user at: <ISO8601 UTC>

## Discovery Inputs

- Intake artifact: `<workspace-root>/context-discovery.md`
- Evidence artifact: `<workspace-root>/context-evidence.json`
- Codemap artifact: `<workspace-root>/context-codemap.md`
- Requirements freeze artifact: `<workspace-root>/requirements-freeze.md`
- Notes: <important assumptions or constraints from intake>

## Guardrails (must-follow)

- Repository rules:
- Security/privacy constraints:
- Prohibited actions:

## Research Scope & Recency Policy

- Online research allowed: <yes|no>
- Approved source types: <official docs/release notes/repos/etc>
- Approved domains/APIs: <list>
- Recency expectation: <e.g. <= 12 months for volatile tooling claims>
- Exception handling: <how stale or undated sources are justified>

## Evidence Inventory

| Evidence ID | Type | Source | Published | Retrieved | Trust rationale |
| ----------- | ---- | ------ | --------- | --------- | --------------- |
| E1          | <source-type> | <url-or-path> | <YYYY-MM-DD or undated:reason> | <YYYY-MM-DD> | <why trusted> |

## Verification Baseline & Strategy

- Verification scenario: `<greenfield-setup|brownfield-existing|brownfield-none>`
- Existing verification commands:
- User decision when verification missing: `<approved-change-scoped|declined-blocked|n/a-existing>`
- Planned verification scope:
- Mandatory smoke gate command:
- Smoke gate expected success signal:

## Established Library Comparison (required for greenfield; optional for brownfield)

| Option | Maturity signal | Last release/reference | Compatibility | Reuse decision | Evidence IDs |
| ------ | ---------------- | ---------------------- | ------------- | -------------- | ------------ |
| <lib-or-tool> | <signal> | <YYYY-MM-DD> | <fit summary> | <adopt or reject + reason> | <E1,E2> |

## Existing Change Surface (required for brownfield; optional for greenfield)

| Area | File anchor | Current behavior | Integration concern | Evidence IDs |
| ---- | ----------- | ---------------- | ------------------- | ------------ |
| <area> | `path/to/file.py:123` | <summary> | <risk or constraint> | <E3> |

## Repo Facts (execution-relevant only)

- Languages/frameworks:
- Package manager(s):
- Build tooling:
- Test tooling:
- Key environment variables/config files:

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Expected success signal |
| ---------- | ------- | ------------- | --------------- | ------ | ----------------------- |
| <name> | <why needed> | `<command>` | `<command>` | <registry/repo/package source> | <signal> |

## Code Map (line-numbered)

List only the places the executor must touch. Prefer repo-relative `path:line` anchors for in-repo files.

| Area | File anchor | What it contains | Why it matters | Planned change |
| ---- | ----------- | ---------------- | -------------- | -------------- |
| <x> | `path/to/file.py:123` | <summary> | <reason> | <edit intent> |

## Requirement to Evidence Traceability

| Requirement ID | Requirement | Evidence IDs | Context section(s) | Planned task refs |
| -------------- | ----------- | ------------ | ------------------ | ----------------- |
| R1 | <requirement text> | <E1,E2> | <section names> | <P1-T1,P2-T4> |

## Contracts & Interfaces

Only include what the change touches:

- APIs (endpoints, handlers, routes)
- Schemas (DB, events, JSON)
- CLI commands and arguments

## Risk Register

| Risk | Impact | Mitigation | Verification command | Evidence IDs |
| ---- | ------ | ---------- | -------------------- | ------------ |
| <risk> | <impact> | <mitigation> | `<command>` | <E4> |
```
