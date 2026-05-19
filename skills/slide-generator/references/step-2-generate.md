```markdown
# Step 2: Generate Slides

Run from:

`skills/skills/slide-generator`

Use snippet sections from:

`skills/skills/slide-generator/snippets`

Build command:

```bash
node scripts/generate-cf-deck.mjs --title "<Title>" --content-file examples/<name>.md
```

Rules:

- If `skills/skills/slide-generator/presentations` is missing, create it automatically.
- Reuse `skills/skills/slide-generator/presentations/<name>` on each run (overwrite mode).

Open command:

```bash
open presentations/<name>/index.html
```

For CreateFuture layouts, the slide sections should be composed from snippet files such as `cover.html`, `section-divider.html`, `two-col.html`, `quote.html`, and `end.html` before final HTML generation.

## Output

- Generated file: `skills/skills/slide-generator/presentations/<name>/index.html`

## Verify output

- [ ] Output html exists in `skills/skills/slide-generator/presentations/<name>/index.html`
- [ ] Output folder was updated in place
```
