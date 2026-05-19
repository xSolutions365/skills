---
name: "create-agent"
description: "Create reusable agent specs from role templates and output-format templates. USE WHEN you need a reusable agent or subagent spec for a defined role and target format."
---

# Task

## Procedure

- Preflight the user request by confirming the target agent system before drafting. Supported initial systems are `codex` and `hermes`.
- Confirm the requested agent role type and target output format. Do not assume any output format unless the user asks for it or accepts it as the default.
- If the agent system or output format is missing, ask for it before drafting.
- For `codex`, the initial supported output format is `codex-custom-agent-toml`.
- For `hermes`, the initial supported output formats are `hermes-profile`, `hermes-delegation-task`, and `hermes-kanban-worker`.
- If the role type is missing, ask for it before drafting. The initial supported role types are `reviewer`, `planner`, `implementer`, `researcher`, `operator`, and `custom`.
- Capture a neutral agent contract before rendering: agent name, role type, target format, objective, target artifact or task, allowed context, evidence rules, capabilities or tools, constraints, stop conditions, output contract, and verification expectations.
- Apply the selected role runbook as a behavior overlay. Explicit user requirements override role-template defaults.
- Apply the selected format runbook as the renderer. Format-specific fields must be derived from the neutral contract rather than invented late.
- Preview the rendered agent spec before writing.
- Validate the preview for role fit, format validity, no unsupported assumptions, no secrets, and no drift from the neutral contract.
- Write the rendered spec only after preview validation passes and the user approves generation.

## Validation

- Reject requests where the target agent system is not stated unless the user provides it before drafting.
- Reject requests where the target output format is unknown or unsupported unless the user approves a new format template to be drafted.
- Reject requests where the role type is unknown or unsupported unless the user approves a new role template to be drafted.
- Reject agent specs that do not define objective, scope, evidence use, constraints, output contract, and stop conditions.
- Reject role templates that do not define objective, apply conditions, evidence and context rules, tool and autonomy boundaries, verification requirements, output contract, stop conditions, escalation rules, and anti-patterns.
- Reject role templates that hard-code one domain, artifact format, or review target unless the user explicitly requested that specialization.
- Reject rendered specs where format-specific fields add behavior not present in the neutral contract.
- Confirm model, reasoning effort, sandboxing, and tool settings are included only when the target format supports them or the user explicitly asks for them.
- Confirm the final rendered spec contains no secrets and does not instruct the agent to print or expose sensitive values.

## Output

- Return the generated or previewed file path, selected role type, selected output format, validation status, and assumptions that affected the generated agent contract.

## Role Runbooks

- [Reviewer Role Template](references/roles/reviewer.md)
- [Planner Role Template](references/roles/planner.md)
- [Implementer Role Template](references/roles/implementer.md)
- [Researcher Role Template](references/roles/researcher.md)
- [Operator Role Template](references/roles/operator.md)
- [Custom Role Template](references/roles/custom.md)

## Format Runbooks

- [Codex Custom Agent TOML Output Format Template](references/formats/codex-custom-agent-toml-format.md)
- [Hermes Delegation Task Output Format Template](references/formats/hermes-delegation-task-format.md)
- [Hermes Kanban Worker Output Format Template](references/formats/hermes-kanban-worker-format.md)
- [Hermes Profile Output Format Template](references/formats/hermes-profile-format.md)
