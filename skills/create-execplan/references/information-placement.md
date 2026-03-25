# Information Placement

The rewrite intentionally gives each artifact one canonical responsibility.

## Context Pack owns

- verification baseline and strategy
- execution command catalog
- repo facts
- requirement-to-evidence traceability
- code map and change surface
- risk register

## ExecPlan owns

- living execution status
- structured task table
- progress log
- decision log
- execution findings
- scenario-focused test plan
- recovery guidance

## Runtime input owns

- derived requirement list
- derived structured tasks
- derived verification scenarios

## Checklist and validation artifacts own

- binary handoff gates
- evidence that the package passed deterministic validation

## Removed duplicate sections

The rewritten ExecPlan must not include standalone sections for:

- `Verification Strategy`
- `Quality Gates`
- `Artifacts & Notes`
- `Plan Overview`

Those concerns stay in the Context Pack, top metadata, logs, or checklist artifacts instead.
