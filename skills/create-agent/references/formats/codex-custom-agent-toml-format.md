# Codex Custom Agent TOML Output Format Template

## Objective

Render a neutral agent contract into a Codex custom-agent TOML file.

## Guidance

- Use this format template when the requested output is a Codex custom agent or Codex subagent.
- Render one `.toml` file for the agent.
- Required fields are `name`, `description`, and `developer_instructions`.
- Use lowercase snake_case for `name` unless the user supplies a valid target-specific name.
- Keep `description` as a concise routing sentence that says when to use the agent.
- Render the neutral contract, role template, constraints, rubric, output contract, stop conditions, and bias controls into `developer_instructions`.
- Include optional fields only when requested or clearly supported by the neutral contract, such as `model`, `model_reasoning_effort`, `sandbox_mode`, or `nickname_candidates`.
- Do not add Codex-specific tool, sandbox, model, or reasoning defaults unless the user requested them or approved the default.
- Validate the rendered TOML parses before writing.
- After writing, report the file path and the selected role and format templates.
