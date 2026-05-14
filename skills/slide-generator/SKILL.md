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
- If input is short, expand it into a minimum 5-slide structure automatically.
- Install dependencies in `cf-slide-generator` when needed (`npm install`) so build tools and `node_modules` are available there.
- If the target `presentations` output folder does not exist, create it automatically.
- Workflow: [references/step-0-preflight.md](references/step-0-preflight.md)

### Step 1: Map content to CreateFuture snippets

- Select layouts from `skills/skills/slide-generator/snippets`.
- Prefer these defaults:
	- `cover.html` for title and opening slide
	- `section-divider.html` for transitions
	- `two-col.html` for comparisons or split content
	- `quote.html` for a standout message
	- `end.html` for the closing slide
- Use `split-image.html`, `centered.html`, or `top-bottom.html` when the content calls for those patterns.
- Workflow: [references/step-1-configure.md](references/step-1-configure.md)

### Step 2: Generate HTML slides

- Use the CreateFuture template and snippet system from `cf-slide-generator`.
- Reference snippet files from `skills/skills/slide-generator/snippets` when building slide sections.
- Build from `cf-slide-generator/presentations/<name>/index.html`.
- Write standalone output to `skills/skills/slide-generator/presentations/<name>-dist`.
- Create `skills/skills/slide-generator/presentations` automatically if missing.
- If output folder already exists, use a versioned name such as `<name>-dist-v2`.
- Default command flow:
	- `cd /Users/nehaprakash/Documents/Projects/cf-slide-generator && npm install`
	- `mkdir -p ../skills/skills/slide-generator/presentations`
	- `npx cf-slides new <name>`
	- `out="../skills/skills/slide-generator/presentations/<name>-dist" && if [ -d "$out" ]; then i=2; while [ -d "${out}-v${i}" ]; do i=$((i+1)); done; out="${out}-v${i}"; fi && node bin/cli.js build presentations/<name>/index.html "$out" && open "$out/index.html"`
- Workflow: [references/step-2-generate.md](references/step-2-generate.md)

### Step 3: Validate and report

- Confirm output exists in `skills/skills/slide-generator/presentations/`.
- Return the final path to the user.
- Include a concise summary of chosen snippet layouts.
- Workflow: [references/step-3-validate.md](references/step-3-validate.md)

## Output

### Result Format

- Report:
	- output file path in `skills/skills/slide-generator/presentations/`
	- generation status (success or failure)


```
