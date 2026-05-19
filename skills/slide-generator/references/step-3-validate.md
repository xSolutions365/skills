```markdown
# Step 3: Validate and Report

## Validation

- Check `skills/slide-generator/presentations/<name>/index.html` exists.
- Open the generated HTML in a browser.
- Verify slide order and content formatting.
- Confirm output directory was updated in place.
- Confirm no `node_modules/` folder was created by this workflow.

## Report to user

- Slides generated successfully.
- Output path: `skills/slide-generator/presentations/<name>/index.html`.

## If generation fails

- Check Node.js is available and the script path is correct.
- Re-run: `node scripts/generate-cf-deck.mjs --title "<Title>" --content-file examples/<name>.md`
```