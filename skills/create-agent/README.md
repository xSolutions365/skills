# create-agent

## Overview

Create a structured agent file package from either supplied YAML or guided intake, freeze one source-of-truth contract, preview the result, validate it, and only then write files.

## When to use it

- You need a reusable agent or subagent package instead of a one-off prompt.
- You want one schema that supports both YAML requests and guided requirement capture.
- You need an approval gate before any files are generated.
- You want role-profile starting points such as `implementer`, `reviewer`, or `skeptical-evaluator` without losing support for `custom`.

## Example prompts

- "Use `create-agent` to generate an implementer agent from this YAML request."
- "Use `create-agent` to walk me through guided intake and create a skeptical-evaluator package."
- "Use `create-agent` to build a planner agent with optional researcher and reviewer subagents."
- "Use `create-agent` to create a no-tools custom agent package that only produces a written analysis."

## References

- The generated agent package writes files to disk and returns file links instead of dumping the full package to the terminal.
- Role profiles are overlays on top of one shared request contract, not rigid prompt libraries.
