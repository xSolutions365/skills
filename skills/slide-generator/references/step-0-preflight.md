```markdown
# Step 0: Preflight - Detect Trigger and Validate Input

## Direct execution rule

- Do not pause for setup confirmations or tool availability checks.
- Do NOT use sensible defaults when content is missing — ask instead.

## Trigger examples

- create slides based on this: ...
- turn this into slides
- make a presentation from this

## Checklist

- [ ] User provided content (text, markdown, or screenshot description)
- [ ] Content meets minimum threshold: at least 5 distinct points or ~100 words on a clear topic
- [ ] Node.js is available
- [ ] Do not run npm install and do not create `node_modules/`
- [ ] If `skills/slide-generator/presentations` is missing, create it automatically
- [ ] Confirm target output filenames do not overwrite existing files

## Output convention

- Input markdown: `examples/<name>.md`
- Generated slides: `skills/slide-generator/presentations/<name>/index.html`

## When to stop and ask follow-up

- Content is completely missing
- Input is a single word, short phrase, or topic name with no supporting detail
- Input is fewer than 5 distinct points or fewer than ~100 words
- User intent is not about creating slides
- Content is sensitive and needs confirmation before transformation

When input is too thin, reply with exactly:
> To generate your slides, share one of:
> - 5–10 key points you want covered, or
> - A short paragraph (~100+ words) on the topic, or
> - Your audience + goal + duration

Do NOT proceed to Step 1 until the threshold is met.
```