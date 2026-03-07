# Review checklist (plan + implementation)

Use this checklist to keep plan-driven execution tight without bloating the ExecPlan.

## Recording format (required)

Record results in the generated artifact `review-checklist.md` using:

- [review-checklist-template.md](review-checklist-template.md)

`Plan Handoff Gate` passes only when all `P*` checks are `pass`.
Before implementation starts, mark `E*` checks as `na`.

## Plan Handoff Gate (required before handoff)

- P1: Purpose is user-visible and outcome-focused.
- P2: Requirements Freeze exists and has explicit user confirmation timestamp.
- P3: Success criteria are observable and include exact commands + expected outputs.
- P4: Non-goals are explicit.
- P5: Context Pack contains a line-numbered code map for every touched area.
- P6: Context Pack includes Requirement -> Evidence traceability for all frozen requirements.
- P7: Evidence inventory includes source metadata with published/retrieved dates for external claims.
- P8: Draft review round was completed and any newly surfaced clarifications are resolved.
- P9: Final requirements were re-confirmed after draft review with explicit post-checkpoint user response evidence.
- P10: Task table rows are explicit (no `investigate` tasks without entry points and completion criteria).
- P11: Every success criterion maps to at least one task + a verification command.
- P12: Risky steps include rollback/recovery guidance.
- P13: Mode-specific section is complete (`Established Library Comparison` for greenfield, `Existing Change Surface` for brownfield).
- P14: `context-pack-validation.json` exists and reports pass.
- P15: A reader can execute tasks using only the working tree, Context Pack, and ExecPlan.
- P16: The code map provides file anchors and the plan provides commands; no repo-wide search is required.
- P17: Workflow artifacts are split correctly (`workspace/*` for in-flight artifacts; root for handoff artifacts).
- P18: `workspace/requirements-freeze.md` exists, includes playback, and records explicit user confirmation.
- P19: Draft-first flow is evidenced (`workspace/draft-review.md` shows initial draft creation then feedback rounds and final approval).
- P20: Verification scenario is explicit and consistent with project mode/user decisions.
- P21: Dependency preflight includes check + install + source commands and hard-fail escalation behavior.
- P22: Minimum smoke gate is present in success criteria, quality gates, and execution command catalog.
- P23: Brownfield-no-verification with declined onboarding is marked blocked and escalated to the user (not handoff-ready).
- P24: Step 1 and Step 3 include checkpoint evidence with prompt text and user approval response excerpts captured after the STOP request.
- P25: `execplan-validation.json` exists and reports pass.
- P26: `Test Plan` is scenario-focused BDD coverage (`Given/When/Then`) with valid `Req IDs`, executable `Evidence Command`, valid `Task Ref` mappings, and at least one `P0` smoke scenario.

## Execution Follow-through (during/after implementation)

- E1: Changes achieve intent with minimal scope creep.
- E2: No unintended side effects (check touched surfaces, configs, APIs).
- E3: Complexity stays low and no fallback behavior is introduced.
- E4: Quality gates are green and meaningful (no bypasses).
- E5: Tests cover changed behavior and verification steps match the ExecPlan.
- E6: Any new discovery requirement is logged as a Decision and explicitly approved before execution proceeds.
