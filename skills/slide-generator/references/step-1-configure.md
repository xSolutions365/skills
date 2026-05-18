```markdown
# Step 1: Map Content To CreateFuture Snippets

## Goal

Save the user's input to a file so the generation script can validate and process it.

## Rules

- Write the user's input **verbatim** to the content file. Do NOT expand, paraphrase, reformat, or add content.
- The script will validate the content and exit with `INPUT_TOO_SHORT` if it is insufficient.

## Suggested mapping

1. `cover.html` for the title slide
2. `section-divider.html` before a major topic shift
3. `two-col.html` for side-by-side information
4. `quote.html` for a key statement or takeaway
5. `end.html` for the closing slide

Optional snippet choices:

- `split-image.html` for image-led slides
- `centered.html` for a single bold message
- `top-bottom.html` for heading plus structured lower content

## Save file

Write draft source content to:

`skills/examples/<name>.md`

If that file already exists, do not overwrite it. Use a new name such as:

`skills/examples/<name>-v2.md`

Then continue to generation step.
```
