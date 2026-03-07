# Step 2 Workflow: Build and approve payload contract

## Objective

Build one deterministic payload contract that drives preview and generation.

## Required actions

1. Create a payload object that matches [payload-schema.md](payload-schema.md) exactly.
2. Validate these invariants before presenting payload:
   - `workflow_steps` are sorted and contiguous
   - every `workflow_steps.reference` exists in `reference_docs.path`
   - `skill_id` matches lowercase-hyphen naming rules
   - all generated paths remain relative to the target skill root
3. Attach a deterministic file plan in this fixed order:
   - `SKILL.md`
   - each reference document sorted by path ascending
   - each template sorted by path ascending
4. Present payload for user approval with no hidden defaults.

## Done when

- Payload passes all invariants.
- File plan is deterministic and ordered.
- User approves payload as the source of truth.
