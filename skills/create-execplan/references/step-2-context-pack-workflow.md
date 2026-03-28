# Step 2 Workflow: Build the Context Pack

## Objective

Produce the durable context artifact that removes repeat discovery and keeps verification posture, change-surface evidence, and risks in one canonical place.

## Required actions

1. Run the shared context requirements from [step-2-context-pack-core.md](step-2-context-pack-core.md).
2. Select project mode using this rule:
   - choose `greenfield` when the change builds net-new capability with no required edits to existing runtime behavior
   - choose `brownfield` when the change modifies existing behavior, interfaces, schemas, or operational flows
   - choose `brownfield` when uncertain
3. Set `Project mode` in `context-pack.md`.
4. Run exactly one mode path:
   - Greenfield: [step-2-context-pack-greenfield.md](step-2-context-pack-greenfield.md)
   - Brownfield: [step-2-context-pack-brownfield.md](step-2-context-pack-brownfield.md)
5. Fill the Context Pack using [context-pack-template.md](context-pack-template.md).
6. Keep section ownership aligned to [information-placement.md](information-placement.md) so shared verification posture stays in the Context Pack while task-local commands stay in ExecPlan rows.

## Done when

- Shared requirements and the selected mode requirements are all satisfied.
- `context-pack.md`, `workspace/context-codemap.md`, and `workspace/context-evidence.json` are consistent.
- Verification posture is explicit in the Context Pack and task-local commands are not duplicated there.
