# Research Findings

- Created: 2026-03-30
- Last updated: 2026-03-30T16:36:00Z

## Facts

- F1: `skills/create-execplan/scripts/run_phase.py:157` defined `blockingIssues` in the child response schema but omitted it from the schema's `required` list, and a live `requirements-freeze` reproduction failed with `invalid_json_schema` before the child phase could do any work.
- F2: Before the wrapper change, a live `requirements-freeze` reproduction recorded a child `spawn_agent` call inside `.codex-phase/stdout.jsonl`, proving the phase worker could recurse into child-agent orchestration instead of remaining a single fresh `codex exec` pass.
- F3: `~/.codex/AGENTS.md` contains a mandatory delegation rule; isolating child runs behind a temporary `CODEX_HOME` seeded only with `auth.json` prevents that inherited rule set and the related state-db warnings from leaking into phase workers.
- F4: Once `CODEX_HOME` is isolated, `codex exec` no longer inherits the user's default sandbox config, so `skills/create-execplan/scripts/run_codex_phase.sh:91` must explicitly pass `--sandbox workspace-write` or the child phase cannot update staged artifacts.
- F5: The helper regression suite in `tests/run_create_execplan_helpers.sh:1` now covers the wrapper/controller contract, and the live smoke harness in `tests/run_create_execplan_live_codex_smoke.sh:1` confirms a real `codex exec` still succeeds after the wrapper changes.

## Assumptions

- A1: The immediate change should fix child-phase isolation and regression coverage without redesigning the entire brownfield research staging contract in the same patch.

## Unknowns

- U1: The current `research` phase still cannot inspect repo files that are referenced only by path in `workspace/context-evidence.json` because those sources are not staged into the isolated workdir.

## Risks

- R1: Prompt-only restrictions are insufficient because higher-priority inherited instructions can still cause delegation.
- R2: Isolating `CODEX_HOME` without an explicit sandbox flag breaks child-phase writes.
- R3: Brownfield research remains fragile until source evidence is staged or summarized into workspace artifacts before isolated phases consume it.
