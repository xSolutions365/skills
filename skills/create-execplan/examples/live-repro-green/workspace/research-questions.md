# Research Questions

- Created: 2026-03-30
- Last updated: 2026-03-30T16:20:00Z

## Objective Research Questions

1. In the current `create-execplan` workflow, which controller and phase-runner code paths are responsible for launching each child phase as a fresh `codex exec` process, and what deterministic artifacts or checkpoints must remain unchanged to preserve the existing package flow required by R1?
2. Where does the current child-phase execution environment still expose permissions, instructions, or runtime context that could let a phase recurse into nested planning or child-agent orchestration, and what repo-local boundary can be enforced so a phase is limited to one fresh Codex process operating only on staged artifacts as required by R2?
3. What existing tests, harness helpers, and validator checks already exercise `create-execplan`, and which specific gaps must be covered so the isolation rule becomes regression-testable through repo-local checks plus the existing live Codex smoke required by R3?
4. What conditions must the mock `create-execplan` package satisfy for the readiness audit and handoff flow to finish green after the isolation fix, and which outputs in the normal workflow prove that the package stayed validator-clean end to end?

## Scope Guardrails

- Ask only codebase or approved-source questions tied to the frozen requirements.
- Do not encode a preferred implementation before research completes.
