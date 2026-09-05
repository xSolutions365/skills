# Step 3 Workflow: Build and approve typed payload

## Objective

Build one deterministic route-specific payload contract that drives preview and generation.

## Required actions

1. Create a payload object that matches [payload-schema.md](payload-schema.md) for the selected `template_type`.
2. Validate shared invariants before presenting payload:
   - `skill_id` matches lowercase-hyphen naming rules
   - `description` contains only one routing sentence beginning with `Use when` and stays under 200 characters
   - generated frontmatter contains no capability summary or separate routing clause
   - all generated paths remain relative to the target skill root
   - no payload field names or values require `generation-summary.md`
3. Validate route invariants:
   - every generated `SKILL.md` and `references/*.md` file is at or under 120 lines
   - `behaviour-guidance` has no reference documents and targets at or under 100 lines
   - `simple-task:inline` has no reference documents
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
