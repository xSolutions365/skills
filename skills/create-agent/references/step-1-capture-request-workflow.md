# Step 1 Workflow: Capture request source

## Objective

Normalize YAML-driven and guided-intake requests into one deterministic intake path.

## Required actions

1. Detect whether the user supplied YAML directly, linked a YAML file, or provided only natural-language requirements.
2. If YAML exists:
   - parse the provided fields against `references/agent-request-schema.md`
   - keep valid supplied values
   - list only the missing or ambiguous required fields
3. If YAML does not exist:
   - ask targeted intake questions using the order from `references/agent-request-schema.md`
   - capture only concrete answers
4. Resolve tie-break behavior:
   - explicit user corrections override YAML
   - YAML overrides inferred defaults
   - role profiles never override explicit fields
5. Carry forward the intake path as either `yaml` or `guided`.

## Done when

- The request source is identified.
- All required fields are concrete enough for contract drafting.
- Any remaining ambiguity is limited to optional fields only.
