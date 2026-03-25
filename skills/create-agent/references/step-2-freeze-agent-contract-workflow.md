# Step 2 Workflow: Build and freeze agent contract

## Objective

Build one deterministic source-of-truth contract and stop for explicit approval.

## Required actions

1. Normalize the request into one contract using `references/agent-request-schema.md`.
2. Apply role-profile defaults only when `role_profile` is one of:
   - `implementer`
   - `reviewer`
   - `skeptical-evaluator`
   - `researcher`
   - `planner`
   - `operator`
3. Preserve `custom` requests without introducing role-specific defaults beyond the shared base contract.
4. Preserve `tools.mode` exactly:
   - `infer` means the skill may propose a tool contract
   - `none` means the package must forbid tool use
   - `explicit` means only the named tools are allowed
5. Freeze the output directory, file set, and optional subagent list.
6. Present the full normalized contract and mark any inferred values explicitly.
7. **STOP** and ask the user for confirmation and wait for the response: "Is this agent contract approved as the source of truth for preview and generation?"

## Done when

- The contract is complete and deterministic.
- Inferred values are explicitly marked.
- User approval is requested before preview generation.
