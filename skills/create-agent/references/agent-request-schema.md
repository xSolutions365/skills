# Agent Request Schema

Use this schema as the single source of truth for both supplied YAML input and guided intake.

## Required fields

- `agent_id` (string): lowercase letters, digits, and hyphens only; use as the output directory name.
- `role_profile` (string): one of `implementer`, `reviewer`, `skeptical-evaluator`, `researcher`, `planner`, `operator`, or `custom`.
- `role_name` (string): human-readable role label used in generated files.
- `objective` (string): the primary outcome the agent must achieve.
- `deliverables` (string[]): concrete outputs the agent must produce.
- `success_criteria` (string[]): testable completion conditions.
- `tools.mode` (string): one of `infer`, `none`, or `explicit`.
- `verification.required_checks` (string[]): checks required before handoff.
- `output.root_dir` (string): relative output directory for generated files.

## Optional fields

- `context.repo_or_domain` (string)
- `context.relevant_files` (string[])
- `context.background` (string[])
- `constraints.in_scope` (string[])
- `constraints.out_of_scope` (string[])
- `constraints.hard_rules` (string[])
- `tools.allowed` (string[]): required when `tools.mode` is `explicit`
- `tools.notes` (string[])
- `approvals.required_for` (string[])
- `approvals.stop_conditions` (string[])
- `memory.mode` (string): `none`, `session`, or `persistent`
- `memory.artifacts` (string[])
- `verification.output_style` (string)
- `subagents.mode` (string): `none`, `optional`, or `required`
- `subagents.entries` (object[])
- `profile_rationale` (string)

## Subagent entry

Each `subagents.entries` item should use the same core contract shape, reduced to the fields needed for one bounded role:

- `agent_id`
- `role_profile`
- `role_name`
- `objective`
- `deliverables`
- `success_criteria`
- `tools`
- `approvals`
- `verification`

## Resolution rules

1. Explicit user corrections override all prior assumptions.
2. Supplied YAML overrides inferred defaults unless it conflicts with explicit later user corrections.
3. Role profile defaults act as overlays only and must never overwrite explicit request values.
4. When `tools.mode` is `none`, do not infer or add tool access later.
5. When `tools.mode` is omitted, default to `infer` and say so in the frozen contract.
6. When `role_profile` is `custom`, do not apply role-profile defaults beyond the shared base contract.

## Recommended normalized contract shape

```yaml
agent_id: example-agent
role_profile: implementer
role_name: Implementer
profile_rationale: Use implementer defaults because the task requires code changes plus verification.
objective: Ship one bounded change safely.
deliverables:
  - Updated implementation
  - Matching tests
success_criteria:
  - The requested behavior is implemented.
  - Required verification passes.
context:
  repo_or_domain: example-app
  relevant_files:
    - src/app.ts
  background:
    - Preserve the current API contract.
constraints:
  in_scope:
    - Fix the login redirect flow.
  out_of_scope:
    - Do not redesign authentication.
  hard_rules:
    - Do not add fallback behavior.
tools:
  mode: explicit
  allowed:
    - read files
    - edit files
    - run tests
  notes:
    - Ask before destructive commands.
approvals:
  required_for:
    - deleting files
    - schema changes
  stop_conditions:
    - requirements conflict
    - tests fail unexpectedly
memory:
  mode: session
  artifacts:
    - progress log
verification:
  required_checks:
    - targeted tests pass
    - no unrelated files changed
  output_style: concise implementation handoff
subagents:
  mode: optional
  entries: []
output:
  root_dir: generated-agents/example-agent
```

## Intake questions when YAML is absent

Ask only for fields that remain unresolved:

1. What should the agent be called, and which role profile fits best?
2. What is the objective?
3. What deliverables and success criteria define completion?
4. What context, constraints, and approvals matter?
5. What tool mode applies: `infer`, `none`, or `explicit`?
6. What verification is required?
7. Should this package include subagents?
