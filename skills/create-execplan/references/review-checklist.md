# Review checklist (plan + implementation)

Use this checklist to keep plan-driven execution tight without turning the handoff review into a duplicate validator dump.

## Recording format (required)

Record results in the generated artifact `review-checklist.md` using:

- [review-checklist-template.md](review-checklist-template.md)

`Plan Handoff Gate` passes only when all `P*` checks are `pass`.
Before implementation starts, mark `E*` checks as `na`.

## Plan Handoff Gate (required before handoff)

- P1: Purpose is user-visible and outcome-focused.
- P2: Requirements Freeze exists, is coherent, and records explicit user confirmation.
- P3: Context Pack captures the real change surface with line anchors, evidence, and the correct mode-specific section.
- P4: Success criteria are observable and non-goals are explicit.
- P5: Task rows are packet-executable, concrete, and avoid implicit discovery.
- P6: Shared verification posture stays in the Context Pack while task-local commands stay in the ExecPlan.
- P7: Test Plan is scenario-focused, executable, and includes a `P0` smoke scenario.
- P8: Risky or destructive steps include recovery or rollback guidance.
- P9: Runtime input exists, is repo-relative for in-repo paths, and remains a derived artifact rather than a second plan.
- P10: Draft review, final approval, and required validation artifacts are all present.

## Execution Follow-through (during/after implementation)

- E1: Changes achieve intent with minimal scope creep.
- E2: No unintended side effects are introduced across touched surfaces, configs, or interfaces.
- E3: Complexity stays low and no fallback behavior is introduced.
- E4: Tests and quality gates match the ExecPlan and remain meaningful.
