# Manual Acceptance

Use this when validating the installed `create-execplan` skill end to end.

## Goal

Confirm the deployed skill keeps initial brief shaping in the parent layer, then uses `prepare/apply` control steps plus one fresh worker subagent per non-deterministic phase.

## Procedure

1. Deploy the repo copy with `scripts/deploy-skill-local.sh create-execplan`.
2. Open the installed skill at `~/.agents/skills/create-execplan/SKILL.md` and confirm it matches the repo copy.
3. Use the retained live fixture at `skills/create-execplan/examples/live-repro-green/` as the test package.
4. Confirm the retained package includes approved Step 1 and Step 2 artifacts:
   - `workspace/requirements-freeze.md`
   - `workspace/planning-brief.md`
5. Run one non-deterministic phase through the installed skill contract:
   - run `scripts/run_phase.py prepare --phase <phase> --artifact-root <fixture-root>`
   - launch one worker using `workspace/phases/<phase>/phase-worker-input.json`
   - wait for completion and save the returned JSON as `workspace/phases/<phase>/phase-worker-result.json`
   - run `scripts/run_phase.py apply --phase <phase> --artifact-root <fixture-root>`
6. Verify:
   - the worker packet requires fresh context, staged-artifact scope, and no delegation
   - the worker packet is driven by the approved `workspace/planning-brief.md` rather than raw transcript history
   - the worker does not ask the user questions directly
   - the latest checkpoint is written only to `workspace/phase-result.json`
   - `workspace/phase-manifest.json` advances only after `apply`
7. Re-run readiness audit and handoff checklist if the fixture was mutated during the test.

## Pass Criteria

- Parent-owned brief shaping completes before any worker phase starts.
- Each non-deterministic phase is driven by `prepare -> worker -> apply`.
- No worker performs nested delegation.
- Approvals surface only through the parent agent.
- The package remains validator-clean after the live test.
