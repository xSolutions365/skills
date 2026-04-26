---
name: "deploy-helper"
description: "Guide a small deployment task with optional runbooks. USE WHEN deployment guidance needs progressive disclosure."
---

# Task

## Procedure

- Confirm the target environment and deployment window.
- Run the normal deployment path from the current project instructions.
- Load [references/rollback.md](references/rollback.md) only when rollback planning or recovery is requested.

## Validation

- Confirm the deployment command completed successfully.
- Report the environment, version, and any follow-up action.

## Output

- Return the deployment result and validation evidence in the terminal.

## Runbooks

- [Rollback](references/rollback.md)
