# Shared Context Pack requirements (Step 2 core)

Objective: capture deterministic context artifacts that both project modes require.

## Required actions

1. Confirm Step 1 outputs are present and current:
   - `workspace/requirements-freeze.md` with explicit confirmation timestamp
   - `workspace/requirements-freeze.md` with checkpoint prompt and user approval response excerpt
   - `workspace/context-discovery.md`
   - `workspace/context-evidence.json`
2. Stop immediately if `workspace/requirements-freeze.md` is missing or unconfirmed.
3. Resolve research policy from Step 1 in `workspace/context-discovery.md`:
   - If online research is allowed, run targeted external research only within approved scope.
   - If online research is disallowed, use local evidence only and record the research constraint in `Evidence Inventory`.
4. Fill `context-pack.md` using:
   - [context-pack-template.md](context-pack-template.md)
5. Build and align these sections in `context-pack.md`:
   - `Requirement Freeze (user-confirmed)`
   - `Evidence Inventory`
   - `Verification Baseline & Strategy`
   - `Dependency Preconditions`
   - `Requirement to Evidence Traceability`
   - `Code Map (line-numbered)`
   - `Risk Register`
6. Update `workspace/context-codemap.md` with all file anchors from `Code Map (line-numbered)`.
7. Ensure every requirement has traceability links:
   - Requirement -> evidence IDs -> expected ExecPlan task coverage.
8. Capture recency metadata for external sources in `workspace/context-evidence.json`:
   - `published_at`
   - `retrieved_at`
   - `trust_rationale`
   - `source_type`
9. Include only evidence that is directly used by requirements or risk decisions.
10. Ensure `Verification Baseline & Strategy` includes a mandatory smoke gate command and expected success signal.
11. Keep the placement rules aligned with [information-placement.md](information-placement.md):
   - Context Pack owns shared verification posture, evidence traceability, code map, and risk register.
   - ExecPlan owns execution tasks, task-local commands, progress, decisions, findings, and scenario verification coverage.

## Required online research handling (when permitted)

- Run targeted online research when requirements depend on unstable external facts:
  - libraries/framework versions
  - policy/standard updates
  - provider/API capabilities
- Prefer primary sources (official docs, release notes, maintainer repositories).
- Record date metadata for every external source and reference the source in `Evidence Inventory`.
- If online research is disallowed by Step 1 permissions, document `not permitted` in `Research Scope & Recency Policy` and skip external collection.

## Hard rules

- Do not leave a requirement without at least one evidence ID.
- Do not include unanchored code-map rows (every row needs `path/to/file:line`).
- Do not proceed when Step 1 freeze confirmation is missing.
- Do not proceed when Step 1 checkpoint prompt and user approval response evidence are missing.
- Do not omit the minimum smoke command from `Verification Baseline & Strategy`.

## Done when

- Shared sections are fully populated and internally consistent.
- `context-pack.md`, `workspace/context-codemap.md`, and `workspace/context-evidence.json` agree on evidence IDs and file anchors.
