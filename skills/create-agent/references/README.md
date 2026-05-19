# Agent Template References

This directory is the canonical source for agent creation runbooks.

## Structure

- `roles/` contains platform-neutral role templates. A role template defines behavior: objective, activation conditions, evidence and context rules, tool and autonomy boundaries, verification requirements, output contract, stop conditions, escalation rules, and anti-patterns.
- `formats/` contains output-format templates. A format template renders a neutral agent contract and selected role behavior into a target system such as Codex or Hermes.

## Contract Flow

1. Capture the neutral agent contract from the user request.
2. Apply one role template from `roles/` as a behavior overlay.
3. Apply one format template from `formats/` as the renderer.
4. Validate that rendered format fields do not add behavior that was absent from the neutral contract and role template.

Roles define behavior. Formats define serialization and platform placement.
