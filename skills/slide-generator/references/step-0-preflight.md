```markdown
# Step 0: Preflight - Detect Trigger and Validate Input

## Direct execution rule

- When this skill is selected, proceed immediately with slide generation.
- Do not pause for setup confirmations.
- Use sensible defaults when details are missing.

## Trigger examples

- create slides based on this: ...
- turn this into slides
- make a presentation from this

## Checklist

- [ ] User provided content (text, markdown, or screenshot description)
- [ ] Content has enough material for at least 3 slides
- [ ] Node.js is available
- [ ] CreateFuture slide tooling is available in `cf-slide-generator`
- [ ] Run `npm install` in `cf-slide-generator` to ensure `node_modules/` is available there
- [ ] If `skills/skills/slide-generator/presentations` is missing, create it automatically
- [ ] Confirm target output filenames do not overwrite existing files

## Output convention

- Input markdown: `examples/<name>.md`
- Generated slides: `skills/skills/slide-generator/presentations/<name>-dist/index.html`

## When to stop and ask follow-up

- Content is completely missing
- User intent is not about creating slides
- Content is sensitive and needs confirmation before transformation
```