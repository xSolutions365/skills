# Brownfield existing-system integration analysis (Step 2 branch)

Objective: map the smallest safe change path in an existing codebase.

## Required actions

1. Populate `Existing Change Surface` in `context-pack.md` with:
   - all touched modules/files (`path:line`)
   - current behavior summaries
   - integration concerns
   - adjacent surfaces the packet-only harness must touch to finish the change
2. Expand `Code Map (line-numbered)` so each planned edit location is anchor-specific.
3. Document current control flow and interface touchpoints:
   - entry points
   - downstream consumers
   - configuration and schema boundaries
4. Build a blast-radius view in `Risk Register`:
   - risk
   - impact
   - mitigation
   - verification command
5. Confirm the proposed path is the smallest safe change set that satisfies requirements.
6. Resolve brownfield verification scenario in `Verification Baseline & Strategy`:
   - If existing verification exists, set scenario `brownfield-existing` and map how current gates are amended for touched scope.
   - If no verification exists and Step 1 user decision approved change-scoped verification, set scenario `brownfield-none` and scope added verification to new changes only.
   - If no verification exists and Step 1 user decision declined change-scoped verification, mark blocked, **STOP**, and @ASK_USER_CONFIRMATION before draft creation.
7. Ensure `Execution Command Catalog` includes a mandatory smoke command for runtime sanity.
8. Populate `Dependency Preconditions` for all external libraries/tools needed by the plan.
9. Carry the exact brownfield edit surface forward into Step 3:
   - planned `Code` tasks must inherit concrete edit targets from `Existing Change Surface` or `Code Map`
   - planned runtime tasks must be directly executable without a standalone onboarding row
   - planned `Action`/`Test`/`Gate` tasks must inherit the exact executable command set they need

## Required analysis depth

- Include direct and adjacent surfaces (not just edited files) when integration behavior can change.
- Include migration/order dependencies when changes must happen in sequence.
- Include explicit rollback/recovery notes for risky steps.
- Include targeted verification commands for changed surfaces when introducing net-new checks in brownfield-no-verification mode.
- Keep task-level rows executable from the packet alone: every Code row needs concrete edit targets and local supporting anchors, every executable Action/Test/Gate row needs a concrete command, and any row that still needs repo-wide discovery is too vague and must be split.
- Do not model standalone `Read` or `Human` rows in brownfield plans; fold read-only onboarding into the first executable task's `Supporting Context Anchors` and rely on harness ADR flow for human approvals.

## Hard rules

- Do not include unanchored touchpoints.
- Do not leave integration concerns without mitigation and verification command.
- Do not propose large-scope refactors when a smaller safe change satisfies requirements.
- Do not introduce repo-wide verification when Step 1 approved only change-scoped verification.
- Do not continue planning when Step 1 records declined verification onboarding for brownfield-no-verification; escalate and wait for user direction.
- Do not leave a task row under-specified for packet-only execution.

## Done when

- `Existing Change Surface`, `Code Map`, and `Risk Register` describe a safe, minimal, line-anchored path.
- Brownfield verification scenario and dependency preconditions are explicit in the Context Pack.
- The Context Pack contains enough concrete anchors and commands for Step 3 task rows to be packet-executable without new discovery.
- Integration and verification risks are explicitly covered.
