```markdown
# Step 3: Validate and Report

## Validation

- Check `skills/slide-generator/presentations/<name>-dist/index.html` exists.
- Open the generated HTML in a browser.
- Verify slide order and content formatting.
- Confirm no existing output directory was overwritten.
- Confirm no `node_modules/` folder was created by this workflow.

## Report to user

- Slides generated successfully.
- Output path: `skills/slide-generator/presentations/<name>-dist/index.html`.
- Note whether a versioned output folder (for example `-dist-v2`) was used.

## If generation fails

- Confirm source deck exists at `cf-slide-generator/presentations/<name>/index.html`.
- Re-run the CreateFuture build command from step 2.
```