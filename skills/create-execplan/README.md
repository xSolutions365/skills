# create-execplan

## Overview

Create a structured execution-plan package with a durable Context Pack, a living ExecPlan, and a generated runtime input artifact for tooling. The current implementation is Codex-first: upstream planning phases run through deterministic orchestration and fresh `codex exec` invocations, while approvals and checkpoint state stay normalized in workspace artifacts.

## When to use it

- You need a deterministic plan handoff for implementation work.
- You want context discovery, living execution state, and generated runtime input split into clear artifacts.
- You need hard phase boundaries between clarification, research, design, structure, and plan drafting.
- You need the plan package to stay auditable while work progresses.

## Example prompts

- "Use `create-execplan` to build an exec plan for migrating this service to a new auth provider."
- "Use `create-execplan` to update the existing plan for the dashboard rebuild based on these new constraints."
- "Use `create-execplan` to produce a brownfield plan for adding SSO to this codebase."

## References

- [Artifact Contract](references/artifact-contract.md)
- [Runtime Input Schema](references/runtime-input-schema.md)
- [Runtime Resolution](references/runtime-resolution.md)
- [Step 2 Context Pack Workflow](references/step-2-context-pack-workflow.md)
