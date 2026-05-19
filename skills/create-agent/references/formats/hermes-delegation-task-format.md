# Hermes Delegation Task Output Format Template

## Objective

Render a neutral agent contract into a Hermes `delegate_task` call or task packet for a short-lived subagent.

## Guidance

- Use this format template when the requested agent system is Hermes and the desired output is runtime subagent delegation.
- Render a delegation packet rather than a persistent profile.
- Include `goal` as the delegated agent's bounded objective.
- Include `context` with only the evidence, constraints, rubric, output contract, and stop conditions the delegated agent is allowed to use.
- Include `toolsets` only when the neutral contract or user request explicitly permits them.
- Include `max_iterations`, timeout, or similar execution limits only when requested or present in the neutral contract.
- For batch delegation, render each task as an independent `{goal, context, toolsets}` entry with no hidden shared context unless the user explicitly requested it.
- Keep the delegated agent bounded: it should return a final summary or review output and should not silently persist state, alter parent context, or expand scope.
- Do not include secrets in the delegated context; reference secret presence checks or required variable names only.
- After writing, report the selected role template, `hermes-delegation-task` format, and the exact delegation fields that came from the neutral contract.
