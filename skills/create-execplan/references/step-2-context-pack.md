# Step 2: Build Context Pack

Objective: produce a line-anchored context artifact that removes repeat discovery.

## Required actions

1. Run shared Step 2 requirements:
   - [step-2-context-pack-core.md](step-2-context-pack-core.md)
2. Select project mode using this rule:
   - Choose `greenfield` when the change builds net-new capability with no required edits to existing runtime behavior.
   - Choose `brownfield` when the change modifies existing behavior, interfaces, schemas, or operational flows.
   - Choose `brownfield` when uncertain.
3. Set `Project mode` in `context-pack.md`:
   - `greenfield`
   - `brownfield`
4. Run exactly one mode path:
   - Greenfield: [step-2-context-pack-greenfield.md](step-2-context-pack-greenfield.md)
   - Brownfield: [step-2-context-pack-brownfield.md](step-2-context-pack-brownfield.md)
5. Fill the Context Pack template:
   - [context-pack-template.md](context-pack-template.md)

## Done when

- Shared requirements and the selected mode requirements are all satisfied.
- `context-pack.md`, `workspace/context-codemap.md`, and `workspace/context-evidence.json` are consistent.
