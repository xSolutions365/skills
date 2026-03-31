# Step 3 Workflow: Produce planning artifacts and the Context Pack

## Objective

Produce the durable context artifact that removes repeat discovery and keeps verification posture, change-surface evidence, and risks in one canonical place after the approved planning brief has driven research, design, and structure phases.

## Required actions

1. Confirm the upstream planning artifacts exist or are ready to be produced:
   - `workspace/research-questions.md`
   - `workspace/research-findings.md`
   - `workspace/design-options.md`
   - `workspace/structure-outline.md`
2. Confirm Step 1 and Step 2 outputs are present and current:
   - `workspace/requirements-freeze.md` with explicit confirmation timestamp
   - `workspace/requirements-freeze.md` with confirmation prompt and user approval response excerpt
   - `workspace/planning-brief.md` with approval prompt and user approval response excerpt
   - `workspace/context-discovery.md`
   - `workspace/context-evidence.json`
3. Stop immediately if `workspace/requirements-freeze.md` or `workspace/planning-brief.md` is missing or unconfirmed.
4. Resolve research policy from Step 1 and Step 2:
   - If online research is allowed, run targeted external research only within approved scope.
   - If online research is disallowed, use local evidence only and record the research constraint in `Evidence Inventory`.
5. Carry the approved Step 2 project mode into `context-pack.md` without re-deciding it from worker transcript history.
6. Run the upstream non-deterministic phases with the deterministic controller:
   - `research-questions`
   - `research`
   - `design`
   - `structure`
   - `context-pack`
7. For each of those phases, follow the same control loop:
   - run `scripts/run_phase.py prepare --phase <name>`
   - spawn one worker with fresh context from `workspace/phases/<phase>/phase-worker-input.json`
   - wait for completion without nested delegation
   - run `scripts/run_phase.py apply --phase <name>`
8. Fill `context-pack.md` using [context-pack-template.md](context-pack-template.md), then fold the approved research/design/structure conclusions into the Context Pack without carrying forward raw transcript history.
9. Build and align these shared sections in `context-pack.md`:
   - `Requirement Freeze (user-confirmed)`
   - `Evidence Inventory`
   - `Verification Baseline & Strategy`
   - `Dependency Preconditions`
   - `Requirement to Evidence Traceability`
   - `Code Map (line-numbered)`
   - `Risk Register`
10. Update `workspace/context-codemap.md` with all file anchors from `Code Map (line-numbered)`.
11. Ensure every requirement has traceability links:
   - Requirement -> evidence IDs -> expected ExecPlan task coverage
12. Capture recency metadata for external sources in `workspace/context-evidence.json`:
   - `published_at`
   - `retrieved_at`
   - `trust_rationale`
   - `source_type`
13. Include only evidence that is directly used by requirements or risk decisions.
14. Ensure `Verification Baseline & Strategy` includes a mandatory smoke gate command and expected success signal.
15. If `Project mode` is `brownfield`, also:
   - populate `Existing Change Surface` in `context-pack.md` with all touched modules/files (`path:line`), current behavior summaries, integration concerns, and adjacent surfaces the packet-only harness must touch
   - expand `Code Map (line-numbered)` so each planned edit location is anchor-specific
   - document current control flow and interface touchpoints, including entry points, downstream consumers, and config/schema boundaries
   - build a blast-radius view in `Risk Register` with risk, impact, mitigation, and verification command
   - resolve brownfield verification scenario in `Verification Baseline & Strategy`:
     - If existing verification exists, set scenario `brownfield-existing` and map how current gates are amended for touched scope.
     - If no verification exists and Step 1 approved change-scoped verification, set scenario `brownfield-none` and scope added verification to new changes only.
     - If no verification exists and Step 1 declined change-scoped verification, mark blocked, **STOP**, and @ASK_USER_CONFIRMATION before draft creation.
   - carry the exact brownfield edit surface forward into Step 4 so planned `Code` tasks inherit concrete edit targets, runtime tasks remain directly executable, and no standalone onboarding row is required
16. If `Project mode` is `greenfield`, also:
   - create at least three viable solution options
   - populate `Established Library Comparison` in `context-pack.md` with library/tool option, maintenance signal, latest release/reference date, compatibility, reuse decision, and rationale
   - compare options against implementation complexity, integration effort, long-term maintenance risk, and team readiness
   - select one recommended approach and justify it with evidence IDs from `Evidence Inventory`
   - record rejected options and why they were not selected
   - define greenfield verification setup in `Verification Baseline & Strategy`, including the minimum smoke test command and expected success signal
   - populate `Dependency Preconditions` for selected libraries/tools with check command, install command, source, and expected success signal
17. Keep section ownership aligned to [information-placement.md](information-placement.md) so shared verification posture stays in the Context Pack while task-local commands stay in ExecPlan rows.

## Required online research handling (when permitted)

- Run targeted online research when requirements depend on unstable external facts:
  - libraries/framework versions
  - policy/standard updates
  - provider/API capabilities
- Prefer primary sources (official docs, release notes, maintainer repositories).
- Record date metadata for every external source and reference the source in `Evidence Inventory`.
- If online research is disallowed by Step 1 permissions, document `not permitted` in `Research Scope & Recency Policy` and skip external collection.

## Brownfield hard rules

- Do not include unanchored touchpoints.
- Do not leave integration concerns without mitigation and verification command.
- Do not propose large-scope refactors when a smaller safe change satisfies requirements.
- Do not introduce repo-wide verification when Step 1 approved only change-scoped verification.
- Do not continue planning when Step 1 records declined verification onboarding for brownfield-no-verification; escalate and wait for user direction.
- Do not leave a task row under-specified for packet-only execution.

## Greenfield hard rules

- Do not recommend bespoke implementations if a suitable established library exists.
- Do not choose an option without explicit trade-off analysis.
- Do not leave recommendation rationale unlinked to evidence IDs.
- Do not leave verification setup undefined for the selected stack.

## Shared hard rules

- Do not leave a requirement without at least one evidence ID.
- Do not include unanchored code-map rows.
- Do not proceed when Step 1 freeze confirmation is missing.
- Do not proceed when Step 2 planning-brief approval evidence is missing.
- Do not omit the minimum smoke command from `Verification Baseline & Strategy`.
- Do not let any worker spawn additional agents or interact with the user directly.

## Done when

- Shared requirements and the selected mode requirements are all satisfied.
- The approved planning brief and the upstream research/design/structure artifacts are consistent with the assembled Context Pack.
- `context-pack.md`, `workspace/context-codemap.md`, and `workspace/context-evidence.json` are consistent.
- Verification posture is explicit in the Context Pack and task-local commands are not duplicated there.
- Brownfield mode: `Existing Change Surface`, `Code Map`, and `Risk Register` describe a safe, minimal, line-anchored path with explicit integration and verification coverage.
- Greenfield mode: `Established Library Comparison` is complete, evidence-backed, and leads to an explicit recommended approach with defined verification setup.
