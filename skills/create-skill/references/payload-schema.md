# Payload Schema

Use this schema as the source-of-truth contract for preview and generation.

## Required fields

- `skill_id` (string): lowercase letters, digits, and hyphens only; max 64 chars.
- `description` (string): concise routing sentence for the skill capability; keep under 200 chars and move inventories into the body.
- `use_when` (string): explicit routing trigger.
- `workflow_steps` (object[]): ordered workflow definitions.
- `output_contract` (object): retained output location plus deterministic result format.
- `reference_docs` (object[]): referenced workflow documents.

## `workflow_steps` entry

- `step` (integer)
- `title` (string)
- `purpose` (string)
- `when` (string, optional)
- `actions` (string[])
- `reference` (string; `references/*workflow.md`)

## `reference_docs` entry

- `path` (string; `references/*.md`)
- `title` (string)
- `objective` (string)
- `required_actions` (string[])
- `done_when` (string[])

## `output_contract`

- `path` (string): retained summary path, relative to the generated skill root.
- `format` (string[]): ordered markdown blocks shown under `### Result Format`.

## Invariants

1. `workflow_steps.step` must be sorted ascending.
2. Step numbers must start at `0` or `1` and remain contiguous.
3. Every `workflow_steps.reference` must exist in `reference_docs.path`.
4. `reference_docs.path` values must be unique.
5. Generated `SKILL.md` frontmatter must remain valid YAML after substitution.
6. `description` must stay to one routing sentence, avoid colon-labelled enumerations or preset catalogues, and reserve detailed capability lists for the markdown body.
7. All paths must be relative to the generated skill root.
8. Generated `SKILL.md` bodies must start with `# Workflow` and include `## Output`.

## Canonical payload skeleton

```json
{
  "skill_id": "example-skill",
  "description": "Create deterministic outputs.",
  "use_when": "you need repeatable generation",
  "workflow_steps": [
    {
      "step": 0,
      "title": "Preflight",
      "purpose": "Confirm local context.",
      "when": "Run first.",
      "actions": ["Validate inputs."],
      "reference": "references/step-0-preflight-workflow.md"
    }
  ],
  "output_contract": {
    "path": "generation-summary.md",
    "format": [
      "# RESULT",
      "- Summary: Skill preview or generation completed.",
      "- Artifacts: <target skill root>/",
      "## Summary",
      "- Skill: <skill_id>",
      "- Outcome: <previewed|generated>",
      "## Validation",
      "- Status: <PASS|FAIL>",
      "- Evidence: <key checks and findings>",
      "## Files",
      "- <path>"
    ]
  },
  "reference_docs": [
    {
      "path": "references/step-0-preflight-workflow.md",
      "title": "Step 0 Workflow: Preflight",
      "objective": "Confirm context and prerequisites.",
      "required_actions": ["Validate root."],
      "done_when": ["Context is confirmed."]
    }
  ]
}
```
