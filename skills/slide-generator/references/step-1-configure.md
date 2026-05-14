```markdown
# Step 1: Map Content To CreateFuture Snippets

## Goal

Transform user input into slide sections that match CreateFuture layouts.

## Rules

- Choose snippet layouts from `skills/skills/slide-generator/snippets`.
- Keep the deck to 5-10 slides unless the user asks otherwise.
- Use the snippet that matches the content shape instead of forcing everything into a generic bullet slide.

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

`examples/<name>.md`

If that file already exists, do not overwrite it. Use a new name such as:

`examples/<name>-v2.md`

Then continue to generation step.
```
