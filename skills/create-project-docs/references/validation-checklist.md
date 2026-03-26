# Validation Checklist

Use this checklist after drafting and again after final file generation. Output must be binary: `PASS` or `FAIL`.

## Deterministic checklist rules

- `D1` Evidence integrity:
  - every command, path, environment variable, and config snippet in the generated docs traces to target-repo evidence
  - unresolved or contradictory evidence is recorded as a gap instead of being invented away
- `D2` README structure:
  - `README.md` includes title, badges, `Quick Install`, `Quick Start`, `What <Project> Does`, `Core Concepts`, and `Go Deeper`
  - the README uses one canonical install path and one canonical quick-start path
  - the README includes at most one advanced example
- `D3` Reference-doc discipline:
  - each `docs/references/*.md` file has one clear topic
  - each deeper doc has a documented placement reason
  - deeper docs do not merely restate README content
- `D4` Link and path integrity:
  - all local links resolve
  - no absolute filesystem paths appear in generated docs unless the user explicitly requested them
  - doc paths stay relative to the target repo
- `D5` Progressive-disclosure flow:
  - onboarding-critical content remains in the README
  - schema-heavy, exhaustive, table-driven, or caveat-heavy detail has moved into deeper docs
  - the README remains readable top-to-bottom without requiring the deeper docs first

## Natural-language quality rules

- `N1` Plain-language onboarding:
  - the README explains the repo's purpose in plain language before heavy internal jargon
  - core concepts are defined briefly and scan cleanly
- `N2` Example quality:
  - examples are real and evidence-backed
  - examples improve comprehension instead of overwhelming the reader
- `N3` Vague action rejection:
  - avoid `investigate`, `review`, `consider`, `look at`, `think about`, or `explore` unless paired with a concrete output criterion
- `N4` Handoff discipline:
  - created or updated files are reported clearly
  - remaining gaps or contradictions are surfaced explicitly

## Evaluation procedure

1. Evaluate `D1` through `D5` in order.
2. Evaluate `N1` through `N4` only if all deterministic rules pass.
3. Record one evidence line for every rule group.
4. If any rule fails, return `FAIL` and list corrective actions.

## Required output format

```text
VALIDATION_STATUS: PASS|FAIL
FAILED_GATES: <comma-separated gate IDs or NONE>
EVIDENCE:
- D1: <evidence>
- D2: <evidence>
- D3: <evidence>
- D4: <evidence>
- D5: <evidence>
- N1: <evidence>
- N2: <evidence>
- N3: <evidence>
- N4: <evidence>
CORRECTIVE_ACTIONS:
- <required fix 1>
- <required fix 2>
```
