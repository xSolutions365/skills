# Context Pack: Greenfield Fixture

- Created: 2026-04-01
- Repo root: `.`
- Target path: `.`
- Project mode: `greenfield`
- Artifact root: `.plan/create-execplan/greenfield-fixture`
- Workspace root: `.plan/create-execplan/greenfield-fixture/workspace`
- Related links: `.plan/create-execplan/greenfield-fixture/execplan.md`

## Change Brief (1-3 paragraphs)

This fixture validates the greenfield create-execplan path with a minimal but fully structured package.

## Requirement Freeze (user-confirmed)

- R1: Create a new CLI package with a typed entrypoint.
- R2: Use an established CLI library instead of a bespoke parser.
- R3: Define an executable smoke path for the initial greenfield implementation.
- Confirmed by user at: 2026-04-01T09:00:00Z

## Discovery Inputs

- Intake artifact: `.plan/create-execplan/greenfield-fixture/workspace/context-discovery.md`
- Evidence artifact: `.plan/create-execplan/greenfield-fixture/workspace/context-evidence.json`
- Codemap artifact: `.plan/create-execplan/greenfield-fixture/workspace/context-codemap.md`
- Requirements freeze artifact: `.plan/create-execplan/greenfield-fixture/workspace/requirements-freeze.md`
- Notes: fixture-only greenfield validation package

## Guardrails (must-follow)

- Repository rules: keep the package deterministic and repo-relative.
- Security/privacy constraints: none beyond standard secret-handling rules.
- Prohibited actions: no placeholder runtime fields in finalized artifacts.

## Research Scope & Recency Policy

- Online research allowed: no
- Approved source types: local fixture references only
- Approved domains/APIs: none
- Recency expectation: not applicable for fixture-only validation
- Exception handling: use local references only

## Evidence Inventory

| Evidence ID | Type | Source | Published | Retrieved | Trust rationale |
| ----------- | ---- | ------ | --------- | --------- | --------------- |
| E1 | fixture doc | `docs/greenfield-spec.md` | 2026-04-01 | 2026-04-01 | captures desired CLI behavior |
| E2 | fixture reference | `pyproject.toml` | undated:fixture | 2026-04-01 | represents dependency wiring surface |

## Verification Baseline & Strategy

- Verification scenario: `greenfield-setup`
- Existing verification commands: none
- User decision when verification missing: `approved-change-scoped`
- Planned verification scope: create a narrow pytest smoke path for the first CLI slice
- Mandatory smoke gate command: `uv run pytest tests/test_cli.py tests/test_smoke.py`
- Smoke gate expected success signal: greenfield smoke tests pass

## Established Library Comparison (required for greenfield; optional for brownfield)

| Option | Maturity signal | Last release/reference | Compatibility | Reuse decision | Evidence IDs |
| ------ | ---------------- | ---------------------- | ------------- | -------------- | ------------ |
| Typer | established Python CLI library | 2026-04-01 | typed commands match the requirement shape | adopt for the fixture plan | E1,E2 |
| argparse | stdlib baseline | 2026-04-01 | works but adds more boilerplate for typed command growth | reject in favor of Typer for the fixture plan | E1 |
| click | mature CLI library | 2026-04-01 | viable but less direct for typed ergonomics in this fixture | reject for simpler typed entrypoint ergonomics | E1,E2 |

## Repo Facts (execution-relevant only)

- Languages/frameworks: Python
- Package manager(s): `uv`
- Build tooling: `uv`
- Test tooling: `pytest`
- Key environment variables/config files: `pyproject.toml`

## Dependency Preconditions

| Dependency | Purpose | Check command | Install command | Source | Expected success signal |
| ---------- | ------- | ------------- | --------------- | ------ | ----------------------- |
| `uv` | install and run the greenfield package | `uv --version` | `brew install uv` | Homebrew | `uv` is available |

## Code Map (line-numbered)

| Area | File anchor | What it contains | Why it matters | Planned change |
| ---- | ----------- | ---------------- | -------------- | -------------- |
| package config | `pyproject.toml:1` | dependency and script registration surface | defines the adopted CLI library and entrypoint | add Typer dependency and script |
| CLI entrypoint | `src/greenfield_app/cli.py:1` | main command implementation | holds the typed greenfield command path | create the initial command module |

## Requirement to Evidence Traceability

| Requirement ID | Requirement | Evidence IDs | Context section(s) | Planned task refs |
| -------------- | ----------- | ------------ | ------------------ | ----------------- |
| R1 | Create a new CLI package with a typed entrypoint. | E1,E2 | Change Brief, Code Map | P1-T1,P2-T2 |
| R2 | Use an established CLI library instead of a bespoke parser. | E1,E2 | Established Library Comparison, Code Map | P1-T1,P2-T2 |
| R3 | Define an executable smoke path for the initial greenfield implementation. | E1 | Verification Baseline & Strategy, Dependency Preconditions | P2-T2 |

## Contracts & Interfaces

Only include what the change touches:

- CLI commands and arguments
- package entrypoint registration

## Risk Register

| Risk | Impact | Mitigation | Verification command | Evidence IDs |
| ---- | ------ | ---------- | -------------------- | ------------ |
| library choice drift | the plan could regress to a bespoke parser | keep the selected library explicit in the comparison table and tasks | `uv run pytest tests/test_cli.py tests/test_smoke.py` | E1,E2 |
