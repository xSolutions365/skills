---
name: "example-structured"
description: "Run a structured multi-step workflow. USE WHEN you need linked reference documents for a larger skill."
---

# Example Structured

This skill demonstrates the repo's structured multi-file lint path.

- Use this when the workflow needs linked references.
- Use this when the skill has grown beyond a compact single file.

## Workflow

### Step 1: Prepare scope

- **Purpose**: Confirm the input and output boundaries.
- **When**: Run first.
- Capture the requested outcome and constraints.
- Workflow: [references/step-1-prepare-scope.md](references/step-1-prepare-scope.md)

### Step 2: Deliver output

- **Purpose**: Produce the requested result after scope approval.
- **When**: Run after Step 1.
- Complete the work using the confirmed scope.
- Workflow: [references/step-2-deliver-output.md](references/step-2-deliver-output.md)
