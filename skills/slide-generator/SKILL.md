---
name: "slide-generator"
description: "Generate presentation slides from pasted content. USE WHEN the user says create slides based on this or asks to turn text into slides."
---

# Workflow

## Execution mode

- Run end-to-end automatically when this skill is selected.
- Do not ask step-by-step setup questions.
- Do not ask for command approval when input content is present; execute the default flow directly.
- Use defaults for title, layout mapping, and output naming when not specified.
- Default output root: `skills/skills/slide-generator/presentations`.
- Ask follow-up questions only when source content is missing.

### Step 0: Detect trigger and collect input

- Trigger on prompts like:
	- create slides based on this: ...
	- turn this into slides
	- make a presentation from this
- Accept input as pasted text, markdown, or screenshot description.
- Derive a short `<name>` slug from the content (e.g. company name or topic).
- If input is short, expand it into a richer paragraph automatically before writing.
- Workflow: [references/step-0-preflight.md](references/step-0-preflight.md)

### Step 1: Write content file

- Write the (optionally expanded) content to `skills/skills/slide-generator/examples/<name>.md`.
- Create the `examples/` directory if it does not exist.
- Workflow: [references/step-1-configure.md](references/step-1-configure.md)

### Step 2: Generate HTML slides

- Run a **single command** from the `skills/skills/slide-generator` directory (use the workspace-relative path):
  ```
  node scripts/generate-cf-deck.mjs --title "<Title>" --content-file examples/<name>.md
  ```
- Resolve the working directory relative to the workspace root — do **not** hardcode absolute user paths.
- The script handles versioning automatically — no extra commands needed.
- After generation, open the output file:
  ```
  open presentations/<name>-dist/index.html
  ```
- Workflow: [references/step-2-generate.md](references/step-2-generate.md)

### Step 3: Validate and report

- Confirm the `OUTPUT_HTML` path printed by the script exists.
- Return the final path to the user.
- Include a concise summary of chosen snippet layouts.
- Workflow: [references/step-3-validate.md](references/step-3-validate.md)

## Output

### Result Format

- Report:
	- output file path in `skills/skills/slide-generator/presentations/`
	- generation status (success or failure)


```
