# Step 3 Workflow: Build and approve typed payload

## Objective

Build one deterministic route-specific payload contract that drives preview and generation.

## Required actions

1. Create a payload object that matches [payload-schema.md](payload-schema.md) for the selected `template_type`.
2. Validate shared invariants before presenting payload:
   - `skill_id` matches lowercase-hyphen naming rules
   - `description` is one routing sentence under 200 characters
   - `use_when` is explicit and concise
   - generated frontmatter will include `USE WHEN`
   - all generated paths remain relative to the target skill root
   - no payload field names or values require `generation-summary.md`
3. Validate route invariants:
   - `behaviour-guidance` has no reference documents and targets at or under 100 lines
   - `simple-task:inline` has no reference documents and targets at or under 500 lines
   - `simple-task:runbook-index` has unique `references/*.md` runbooks linked from `SKILL.md`
   - `multi-step-workflow` has contiguous ordered workflow steps, one workflow reference per step, `README.md` content, and output text for `### Result Format`
4. Attach a deterministic file plan in this fixed order:
   - `SKILL.md`
   - `README.md` for `multi-step-workflow`
   - each reference document sorted by path ascending
   - each template or asset sorted by path ascending, when the generated skill needs them
5. Present payload for user approval with no hidden defaults.

## Done when

- Payload passes all shared and route-specific invariants.
- File plan is deterministic and ordered.
- User approves payload as the source of truth.
