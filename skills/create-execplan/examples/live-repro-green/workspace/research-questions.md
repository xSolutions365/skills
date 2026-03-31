# Research Questions

- Created: 2026-03-30
- Last updated: 2026-03-30T16:20:00Z

## Objective Research Questions

1. In the current `create-execplan` workflow, which controller and skill-contract code paths must own `prepare`, worker launch, and `apply` so the deterministic artifacts and checkpoints required by R1 remain unchanged?
2. Which validation boundary should reject nested planning behavior or out-of-scope artifact mutations so each phase stays one fresh worker subagent operating only on staged artifacts as required by R2?
3. What existing tests, harness helpers, and validator checks already exercise `create-execplan`, and which specific gaps must be covered so the isolation rule becomes regression-testable through repo-local checks plus the existing live Codex smoke required by R3?
4. What conditions must the mock `create-execplan` package satisfy for the readiness audit and handoff flow to finish green after the isolation fix, and which outputs in the normal workflow prove that the package stayed validator-clean end to end?

## Scope Guardrails

- Ask only codebase or approved-source questions tied to the frozen requirements.
- Do not encode a preferred implementation before research completes.
