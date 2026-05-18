---
name: "slide-generator"
description: "Generate presentation slides from pasted content. USE WHEN the user says create slides based on this or asks to turn text into slides."
---

# Workflow

### Step 0: Detect trigger and collect input

- Trigger on prompts like:
	- create slides based on this: ...
	- turn this into slides
	- make a presentation from this
- Accept input as pasted text, markdown, or screenshot description.
- **STOP before Step 1** if input is a single word, short phrase, or fewer than 5 points / ~100 words. Ask the user to elaborate — do not proceed.
- Derive a short `<name>` slug from the content (e.g. company name or topic).
- Workflow: [references/step-0-preflight.md](references/step-0-preflight.md)

### Step 1: Write content file

- Write the user's input **verbatim** to `skills/examples/<name>.md`. Do NOT expand or add content.
- Create the `skills/examples/` directory if it does not exist.
- Workflow: [references/step-1-configure.md](references/step-1-configure.md)

### Step 2: Generate HTML slides

- Run exactly these two commands from the `skills/skills/slide-generator` directory — no compound commands, no pwd/ls, no extra steps:
  ```
  node scripts/generate-cf-deck.mjs --title "<Title>" --content-file ../../examples/<name>.md
  ```
  Then:
  ```
  open presentations/<name>/index.html
  ```
- Do NOT run pwd, ls, or any diagnostic commands before or after.
- Workflow: [references/step-2-generate.md](references/step-2-generate.md)

### Step 3: Validate and report

- After the script prints `OUTPUT_HTML=...`, reply with one line only:
  ```
  Slides ready: presentations/<name>/index.html
  ```
- If the script exits with `INPUT_TOO_SHORT`, reply with exactly:
  ```
  To generate your slides, share one of:
  - 5–10 key points you want covered, or
  - A short paragraph (~100+ words) on the topic, or
  - Your audience + goal + duration
  ```
- Do not narrate steps, do not explain what was done, do not list layouts.
- Workflow: [references/step-3-validate.md](references/step-3-validate.md)

## Output

### Result Format

- Report:
	- output file path in `skills/skills/slide-generator/presentations/`
	- generation status (success or failure)

