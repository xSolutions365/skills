# Validation Checklist

Use this checklist after preview generation and after final file generation. Output must be binary: `PASS` or `FAIL`.

## Deterministic checklist rules

- `C1` Contract completeness:
  - required fields from `references/agent-request-schema.md` are present or explicitly inferred
  - output root is relative
  - tool mode is one of `infer`, `none`, or `explicit`
- `C2` File package completeness:
  - preview includes `system-contract.md`
  - preview includes `task-packet.md`
  - preview includes `verification-checklist.md`
  - subagent files appear only when enabled
- `C3` Role fidelity:
  - the selected role profile is reflected in the package
  - `custom` does not inject unrelated role defaults
  - `skeptical-evaluator` is findings-first and issue-seeking rather than broadly approving
- `C4` Tool and approval clarity:
  - tool rules are explicit
  - no-tools requests remain no-tools
  - approvals and stop conditions are concrete
- `C5` Path and portability integrity:
  - all package paths are relative
  - no absolute filesystem paths appear in generated files
  - instructions remain portable across repositories

## Natural-language quality rules

- `N1` Procedural clarity:
  - the system contract tells the agent how to operate, not only what the task is
  - the task packet turns the objective into bounded work
- `N2` Verification quality:
  - verification checks are concrete and testable
  - missing verification is rejected
- `N3` Vague action rejection:
  - avoid `investigate`, `review`, `consider`, `look at`, `think about`, or `explore` unless paired with a concrete output criterion
- `N4` Handoff discipline:
  - final handoff is concise
  - generation returns file links rather than full file dumps by default

## Evaluation procedure

1. Evaluate `C1` through `C5` in order.
2. Evaluate `N1` through `N4` only if all deterministic rules pass.
3. Record one evidence line for every rule group.
4. If any rule fails, return `FAIL` and list corrective actions.

## Required output format

```text
VALIDATION_STATUS: PASS|FAIL
FAILED_GATES: <comma-separated gate IDs or NONE>
EVIDENCE:
- C1: <evidence>
- C2: <evidence>
- C3: <evidence>
- C4: <evidence>
- C5: <evidence>
- N1: <evidence>
- N2: <evidence>
- N3: <evidence>
- N4: <evidence>
CORRECTIVE_ACTIONS:
- <required fix 1>
- <required fix 2>
```
