# Hermes Kanban Worker Output Format Template

## Objective

Render a neutral agent contract into a Hermes Kanban worker or orchestrator task specification.

## Guidance

- Use this format template when the requested agent system is Hermes and the desired output is a durable multi-agent Kanban workflow task.
- Render a Kanban task packet, worker profile assumptions, and completion contract rather than a one-shot subagent file.
- Name the worker or orchestrator profile expected to receive the task when the user supplies it; otherwise mark the profile as a required input.
- Include task objective, allowed context, evidence inputs, constraints, rubric or work criteria, dependencies, stop conditions, and expected completion summary.
- Include assignment, labels, priority, blocked-by relationships, due dates, or metadata only when supplied by the user or neutral contract.
- Include a completion contract that states what the worker must return through `kanban_complete`, including summary, evidence, decisions, unresolved risks, and follow-up work.
- If the task coordinates multiple profiles, define handoff boundaries and what each worker is allowed to decide.
- Do not invent Hermes board names, profile names, toolsets, or persistence settings unless the user requested them or approved the default.
- After writing, report the selected role template, `hermes-kanban-worker` format, task target, and any required profile or board assumptions.
