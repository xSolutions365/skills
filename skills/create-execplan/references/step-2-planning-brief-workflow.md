# Step 2 Workflow: Build and approve the planning brief

## Objective

Convert the confirmed requirements into one parent-owned planning brief that becomes the source of truth for all upstream planning subagent phases.

## Required actions

1. Confirm Step 1 approval evidence exists in `workspace/requirements-freeze.md`.
2. Build and maintain `workspace/planning-brief.md` using only the frozen requirements plus the confirmed intake context.
3. Capture the planning contract in `workspace/planning-brief.md`:
   - objective summary and non-goals
   - selected project mode and rationale
   - verification scenario and mandatory smoke gate command
   - online research policy, approved source boundaries, and recency expectations
   - the concrete questions or trade-offs the research, design, and structure phases must resolve
4. Keep Step 2 parent-owned:
   - do not spawn worker subagents yet
   - do not let later phases infer project mode or research scope from raw transcript history
   - treat `workspace/planning-brief.md` as the only approved planning contract for upstream phases
5. Ask for explicit confirmation:
   - `Is the planning brief in workspace/planning-brief.md approved as the source of truth for upstream planning phases?`
6. **STOP** and wait for explicit user confirmation before Step 3.
7. Record the approval prompt, timestamp, and response excerpt in `workspace/planning-brief.md`.

## Done when

- `workspace/planning-brief.md` exists and records the approved planning contract.
- Project mode, research policy, and verification posture are frozen before any subagent planning phase begins.
- Nothing proceeds to Step 3 without the Step 2 approval response.
