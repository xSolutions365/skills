# Hermes Profile Output Format Template

## Objective

Render a neutral agent contract into a Hermes profile setup packet.

## Guidance

- Use this format template when the requested agent system is Hermes and the desired output is a persistent named agent profile.
- Render a profile-oriented packet, not a Codex-style standalone subagent file.
- Include a `SOUL.md` section for stable identity, role behavior, boundaries, evidence rules, output contract, stop conditions, and bias controls.
- Include a `config.yaml` section or snippet for supported Hermes profile settings such as model/provider choices, toolsets, working directory, delegation settings, skills, memory, and cron only when requested or present in the neutral contract.
- Include an optional `.env` guidance section only for required variable names or presence checks; never include secret values.
- Include setup notes for where the profile files should live when the user provides a Hermes profile directory convention.
- Do not invent Hermes provider, model, toolset, memory, or delegation defaults unless the user requested them or approved the default.
- Validate that the rendered profile packet keeps behavior in `SOUL.md` and operational settings in `config.yaml`.
- After writing, report the selected role template, `hermes-profile` format, generated files, and any assumptions about profile location.
