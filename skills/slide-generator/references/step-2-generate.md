```markdown
# Step 2: Generate Slides

Use the CreateFuture template system from:

`cf-slide-generator`

Use snippet sections from:

`skills/skills/slide-generator/snippets`

Build command (run from `cf-slide-generator`):

```bash
npm install
mkdir -p ../skills/skills/slide-generator/presentations
node bin/cli.js build presentations/<name>/index.html ../skills/skills/slide-generator/presentations/<name>-dist
```

Rules:

- Ensure dependencies are installed in `cf-slide-generator` (`npm install`) so `node_modules/` is available there.
- If `../skills/skills/slide-generator/presentations` is missing, create it automatically.
- Do not overwrite existing output directories.
- If `../skills/skills/slide-generator/presentations/<name>-dist` already exists, use `../skills/skills/slide-generator/presentations/<name>-dist-v2`.

Open command:

```bash
open ../skills/skills/slide-generator/presentations/<name>-dist/index.html
```

For CreateFuture layouts, the slide sections should be composed from snippet files such as `cover.html`, `section-divider.html`, `two-col.html`, `quote.html`, and `end.html` before final HTML generation.

## Output

- Generated file: `../skills/skills/slide-generator/presentations/<name>-dist/index.html`

## Verify output

- [ ] Source deck exists in `cf-slide-generator/presentations/<name>/index.html`
- [ ] Output html exists in `skills/skills/slide-generator/presentations/<name>-dist/index.html`
- [ ] Existing output directories were not overwritten
```

See also: [local-generate-commands.md](local-generate-commands.md)
