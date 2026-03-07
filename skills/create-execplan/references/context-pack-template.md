# Context Pack template (for low-reasoning executors)

The Context Pack is a durable, reusable artifact that minimizes repeat discovery. It is initialized once per change request and updated when requirements or evidence change.

Use it to capture:

- The _minimum repo facts_ required to execute changes safely.
- A _line-numbered code map_ pointing to exactly where work will happen.
- Exact commands and expected outputs for checks/tests/quality gates.

## Template

```md
# Context Pack: <short title>

- Created: <YYYY-MM-DD>
- Repo root: `<absolute-or-repo-relative-path>`
- Target path: `<path-or-.>`
- Project mode: `<greenfield|brownfield>`
- Artifact root: `<artifact-root>`
- Workspace root: `<workspace-root>`
- Related links: <issue/PR/spec URLs or file paths>

## Change Brief (1–3 paragraphs)

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

- Quality gates: <commands, thresholds>
- Repo rules: <must-follow rule summary>
- Prohibited actions: <if relevant>

## Research Scope & Recency Policy

- Online research allowed: <yes|no>
- Approved source types: <official docs/release notes/repos/etc>
- Approved domains/APIs: <list>
- Recency expectation: <e.g., <= 12 months for volatile tooling claims>
- Exception handling: <how stale/undated sources are justified>

## Evidence Inventory

| Evidence ID | Type          | Source        | Published                      | Retrieved    | Trust rationale |
| ----------- | ------------- | ------------- | ------------------------------ | ------------ | --------------- |
| E1          | <source-type> | <url-or-path> | <YYYY-MM-DD or undated:reason> | <YYYY-MM-DD> | <why trusted>   |

## Verification Baseline & Strategy

- Verification scenario: `<greenfield-setup|brownfield-existing|brownfield-none>`
- Existing verification commands:
- User decision when verification missing: `<approved-change-scoped|declined-blocked|n/a-existing>`
- Planned verification scope:
- Mandatory smoke gate command:
- Smoke gate expected success signal:

## Established Library Comparison (required for greenfield; optional for brownfield)

| Option        | Maturity signal              | Last release/reference | Compatibility | Reuse decision          | Evidence IDs |
| ------------- | ---------------------------- | ---------------------- | ------------- | ----------------------- | ------------ |
| <lib-or-tool> | <stars/adoption/maintenance> | <YYYY-MM-DD>           | <fit summary> | <adopt/reject + reason> | <E1,E2>      |

## Existing Change Surface (required for brownfield; optional for greenfield)

| Area   | File anchor           | Current behavior | Integration concern | Evidence IDs |
| ------ | --------------------- | ---------------- | ------------------- | ------------ |
| <area> | `path/to/file.py:123` | <summary>        | <risk/constraint>   | <E3>         |

## Repo Facts (execution-relevant only)

- Languages/frameworks:
- Package manager(s):
- Build tooling:
- Test tooling:
- Key environment variables/config files:

## Dependency Preconditions

| Dependency | Purpose      | Check command | Install command | Source                         | Expected success signal |
| ---------- | ------------ | ------------- | --------------- | ------------------------------ | ----------------------- |
| <name>     | <why needed> | `<command>`   | `<command>`     | <registry/repo/package source> | <signal>                |

## Execution Command Catalog

| Purpose                         | Command     | Expected success signal |
| ------------------------------- | ----------- | ----------------------- |
| Install/setup                   | `<command>` | exit 0                  |
| Dependency check                | `<command>` | dependency present      |
| Dependency install (if missing) | `<command>` | dependency installed    |
| Smoke test (mandatory)          | `<command>` | smoke scenario passes   |
| Run                             | `<command>` | expected startup signal |
| Tests                           | `<command>` | all targeted tests pass |
| Quality gate                    | `<command>` | gate passes             |

## Code Map (line-numbered)

List only the places the executor must touch. Prefer `path:line` anchors.

| Area | File anchor           | What it contains | Why it matters | Planned change |
| ---- | --------------------- | ---------------- | -------------- | -------------- |
| <x>  | `path/to/file.py:123` | <summary>        | <reason>       | <edit intent>  |

## Requirement to Evidence Traceability

| Requirement ID | Requirement        | Evidence IDs | Context section(s) | Planned ExecPlan linkage |
| -------------- | ------------------ | ------------ | ------------------ | ------------------------ |
| R1             | <requirement text> | <E1,E2>      | <section names>    | <phase/task ref>         |

## Contracts & Interfaces

Only include what the change touches:

- APIs (endpoints, handlers, routes)
- Schemas (DB, events, JSON)
- CLI commands and arguments

## Risk Register

| Risk   | Impact   | Mitigation   | Verification command | Evidence IDs |
| ------ | -------- | ------------ | -------------------- | ------------ |
| <risk> | <impact> | <mitigation> | `<command>`          | <E4>         |
```
