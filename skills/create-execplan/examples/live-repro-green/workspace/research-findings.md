# Research Findings

- Created: 2026-03-30
- Last updated: 2026-03-30T16:36:00Z

## Facts

- F1: `skills/create-execplan/scripts/run_phase.py:157` defined `blockingIssues` in the child response schema but omitted it from the schema's `required` list, and a live `requirements-freeze` reproduction failed with `invalid_json_schema` before the child phase could do any work.
- F2: The retained live repro showed that prompt-only subprocess isolation was insufficient because a child phase could still recurse into child-agent orchestration.
- F3: Parent-managed worker subagents with fresh context remove the need for a subprocess-specific `CODEX_HOME` workaround and keep approval handling in one place.
- F4: Apply-time validation is the right enforcement point for staged artifact scope because the parent can reject malformed results, read-only mutations, and checkpoint returns without draft edits.
- F5: The helper regression suite in `tests/run_create_execplan_helpers.sh:1` now covers the staged worker packet contract, and installed-skill acceptance is documented in `skills/create-execplan/references/manual-acceptance.md:1`.

## Assumptions

- A1: The immediate change should fix child-phase isolation and regression coverage without redesigning the entire brownfield research staging contract in the same patch.

## Unknowns

- U1: The current `research` phase still cannot inspect repo files that are referenced only by path in `workspace/context-evidence.json` because those sources are not staged into the isolated workdir.

## Risks

- R1: Prompt-only restrictions are insufficient because higher-priority inherited instructions can still cause delegation.
- R2: Weak apply-time validation would let invalid worker outputs or read-only artifact mutations slip through the phase boundary.
- R3: Brownfield research remains fragile until source evidence is staged or summarized into workspace artifacts before isolated phases consume it.
