# Greenfield option and library selection (Step 2 branch)

Objective: choose a low-complexity implementation approach backed by current evidence.

## Required actions

1. Create at least three viable solution options.
2. Populate `Established Library Comparison` in `context-pack.md` with:
   - library/tool option
   - maintenance signal
   - latest release/reference date
   - compatibility with requirements
   - reuse decision and rationale
3. Compare options against shared criteria:
   - implementation complexity
   - integration effort
   - long-term maintenance risk
   - team readiness
4. Select one recommended approach and justify it with evidence IDs from `Evidence Inventory`.
5. Record rejected options and why they were not selected.
6. Define greenfield verification setup in `Verification Baseline & Strategy`:
   - select verification tooling aligned to the recommended stack
   - include minimum smoke test command and expected success signal
7. Populate `Dependency Preconditions` for selected libraries/tools:
   - check command
   - install command
   - installation source
   - expected success signal

## Required recency checks

- Use fresh sources for volatile ecosystem claims.
- If a source is older than the agreed recency expectation, document why it is still acceptable.
- Capture every cited source in `workspace/context-evidence.json` and `Evidence Inventory`.

## Hard rules

- Do not recommend bespoke implementations if a suitable established library exists.
- Do not choose an option without explicit trade-off analysis.
- Do not leave recommendation rationale unlinked to evidence IDs.
- Do not leave verification setup undefined for the selected stack.

## Done when

- `Established Library Comparison` is complete and evidence-backed.
- `Verification Baseline & Strategy` is complete for greenfield setup.
- Recommended approach is explicit, justified, and traceable to requirements.
