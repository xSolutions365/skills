# Payload Schema

Use this schema as the source-of-truth contract for preview and generation.

## Shared required fields

- `skill_id` (string): lowercase letters, digits, and hyphens only; max 64 chars.
- `description` (string): concise routing sentence for the skill capability; keep under 200 chars.
- `use_when` (string): explicit routing trigger appended to frontmatter as `USE WHEN`.
- `template_type` (string): one of `behaviour-guidance`, `simple-task:inline`, `simple-task:runbook-index`, or `multi-step-workflow`.

## Route fields

### `behaviour-guidance`

- `guidance_sections` (object[]): ordered sections for `SKILL.md`.
  - `heading` (string)
  - `bullets` (string[])

### `simple-task:inline`

- `task_sections` (object[]): ordered sections for `SKILL.md`.
  - `heading` (string)
  - `content` (string[])

### `simple-task:runbook-index`

- `task_sections` (object[]): ordered index sections for `SKILL.md`.
- `reference_docs` (object[]): runbook files linked from `SKILL.md`; loading them at runtime is optional, but every generated runbook file must be linked.
  - `path` (string; `references/*.md`)
  - `title` (string)
  - `objective` (string)
  - `content` (string[])

### `multi-step-workflow`

- `workflow_steps` (object[]): ordered workflow definitions.
  - `step` (integer)
  - `title` (string)
  - `purpose` (string)
  - `when` (string, optional)
  - `actions` (string[])
  - `reference` (string; `references/*workflow.md`)
- `reference_docs` (object[]): referenced workflow documents.
  - `path` (string; `references/*.md`)
  - `title` (string)
  - `objective` (string)
  - `required_actions` (string[])
  - `done_when` (string[])
- `output_sections` (string[]): concise terminal handoff format for `## Output`.
- `readme` (object): required README content for the structured multi-step layout.
  - `overview` (string)
  - `when_to_use` (string[])
  - `example_prompts` (string[])
  - `references` (string[], optional)

## Invariants

1. `skill_id` must match the generated directory name.
2. Generated `SKILL.md` frontmatter must remain valid YAML after substitution and quote string values.
3. `description` must stay to one routing sentence, avoid colon-labelled enumerations or preset catalogues, and reserve detailed capability lists for the body or references.
4. All generated paths must be relative to the generated skill root.
5. `generation-summary.md`, `output_contract`, and retained summary paths are prohibited.
6. `behaviour-guidance` must generate only `SKILL.md` and target at or under 100 lines.
7. `simple-task:inline` must generate only `SKILL.md` and target at or under 500 lines.
8. `simple-task:runbook-index` must keep `SKILL.md` at or under 500 lines and link every `reference_docs.path`.
9. `multi-step-workflow` is required for any skill over 500 lines, and for any skill with ordered checkpoints or approval gates at any length.
10. `multi-step-workflow.workflow_steps.step` must be sorted ascending, start at `0` or `1`, and remain contiguous.
11. Every `multi-step-workflow.workflow_steps.reference` must exist in `reference_docs.path`.
12. `multi-step-workflow` must generate `README.md` using the required README section order: Overview, When to use it, Example prompts, then optional References.
13. `multi-step-workflow.output_sections` renders under `### Result Format`.
14. `reference_docs.path` values must be unique.

## Canonical payload skeleton

```json
{
  "skill_id": "example-skill",
  "description": "Guide repeatable work.",
  "use_when": "you need repeatable task guidance",
  "template_type": "simple-task:inline",
  "task_sections": [
    {
      "heading": "Procedure",
      "content": ["Confirm the input.", "Produce the requested output."]
    },
    {
      "heading": "Validation",
      "content": ["Check the result against the user's request before handoff."]
    }
  ]
}
```
