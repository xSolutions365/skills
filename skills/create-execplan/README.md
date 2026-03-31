# create-execplan

## Overview

Create a structured execution-plan package with a durable Context Pack, a living ExecPlan, and a generated runtime input artifact for tooling. The current implementation is hybrid by design: the parent agent owns the iterative brief-shaping and approval checkpoints up front, then upstream planning phases run through deterministic `prepare/apply` control steps plus fresh worker subagents.

## When to use it

- You need a deterministic plan handoff for implementation work.
- You want context discovery, living execution state, and generated runtime input split into clear artifacts.
- You need iterative user collaboration on the initial objective brief before bounded planning workers take over.
- You need hard phase boundaries between research, design, structure, context assembly, and plan drafting.
- You need the plan package to stay auditable while work progresses.

## Example prompts

- "Use `create-execplan` to build an exec plan for migrating this service to a new auth provider."
- "Use `create-execplan` to update the existing plan for the dashboard rebuild based on these new constraints."
- "Use `create-execplan` to produce a brownfield plan for adding SSO to this codebase."

## References

- [Artifact Contract](references/artifact-contract.md)
- [Manual Acceptance](references/manual-acceptance.md)
- [Runtime Input Schema](references/runtime-input-schema.md)
- [Runtime Resolution](references/runtime-resolution.md)
- [Step 2 Planning Brief Workflow](references/step-2-planning-brief-workflow.md)
- [Step 2 Context Pack Workflow](references/step-2-context-pack-workflow.md)
