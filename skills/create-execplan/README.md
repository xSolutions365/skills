# create-execplan

## Overview

Create a plan package that turns validated context into a detailed, trackable implementation plan for downstream execution, with a generated runtime task-packet artifact for tooling.

## When to use it

- You need a deterministic plan with explicit steps and dependencies.
- You want context capture and execution planning separated into clear artifacts.
- You need a plan that can be updated in place as work progresses.

## Example prompts

- "Use `create-execplan` to build an exec plan for migrating this service to a new auth provider."
- "Use `create-execplan` to update the existing plan for the dashboard rebuild based on these new constraints."
- "Use `create-execplan` to produce a brownfield plan for adding SSO to this codebase."
