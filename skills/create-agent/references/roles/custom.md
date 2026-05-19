# Custom Role Template

## Objective

Guide creation of custom agents when no known role template fits the task or the user explicitly wants a bespoke operating stance.

## Apply When

- Use this role template when no known role profile fits the task.
- Use this role template when the user explicitly wants a bespoke operating stance.
- Use this role template when the role must be assembled from user-supplied requirements rather than inherited defaults.

## Do Not Use When

- Do not use this role template when `reviewer`, `planner`, `implementer`, `researcher`, or `operator` clearly fits.
- Do not use this role template to avoid specifying a role that is actually required for safe generation.
- Do not use this role template to mix incompatible responsibilities without surfacing the conflict.

## Required Contract Additions

- Define objective, scope, allowed context, constraints, capabilities or tools, output contract, verification expectations, and stop conditions from the user request.
- Define any bespoke posture, decision rules, or boundaries explicitly.
- Define which standard role behaviors are intentionally included or excluded when the custom role overlaps with known roles.

## Guidance

- Use the shared base contract only unless the user supplies role-specific behavior.
- Do not inject role-specific assumptions beyond what the user provided.
- Keep objective framing neutral.
- Keep tool posture neutral and honor the chosen tool mode.
- Keep verification requirements explicit but not role-biased.

## Evidence and Context Rules

- Use only the context allowed by the neutral contract.
- Separate user-supplied requirements from inferred requirements.
- Mark assumptions explicitly when they affect behavior, output, or verification.

## Tool and Autonomy Boundaries

- Include only tools and autonomy boundaries supplied by the user or required by the selected output format.
- Do not invent tool access, sandboxing, persistence, memory, delegation, or runtime permissions.
- Do not silently add responsibilities from known roles.

## Verification Requirements

- Verify that the custom role does not omit objective, scope, evidence use, constraints, output contract, or stop conditions.
- Verify that custom behavior does not conflict with the target output format.
- Verify that any known-role overlap is intentional and documented.

## Output Contract

- Return the custom role objective, boundaries, behavior rules, output expectations, verification expectations, and stop conditions.
- Return assumptions and any known-role behavior intentionally included or excluded.
- Return unresolved questions that would materially change the custom role.

## Stop Conditions

- Stop when the custom role lacks enough information to define safe behavior.
- Stop when the custom role combines incompatible responsibilities without user approval.
- Stop when the requested behavior requires unsupported tools, hidden assumptions, or unsafe autonomy.

## Escalation Rules

- Escalate when a known role would be safer or clearer than a custom role.
- Escalate when the custom role's responsibilities conflict with the selected output format.
- Escalate when missing constraints could cause the agent to act outside the user's intent.

## Bias or Failure-Mode Controls

- Do not silently convert a custom role into a known profile.
- Do not invent extra responsibilities that were not requested.
- Do not use custom role flexibility to bypass validation requirements.

## Anti-Patterns

- Do not create a vague persona paragraph instead of a behavioral contract.
- Do not leave tool policy, output contract, or stop conditions undefined.
- Do not hide role ambiguity from the user.
