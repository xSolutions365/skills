# create-project-docs

## Overview

Create an onboarding-first documentation set for a repository by generating a concise `README.md` and only the deeper `docs/references/*.md` files that the repo's evidence actually justifies.

## When to use it

- You need a cleaner README that gets new contributors to first success quickly.
- You need to move schema-heavy, workflow-heavy, or reference-heavy content out of the README without losing clarity.
- You need documentation generated from repo evidence rather than invented commands or examples.
- You want reusable templates and portable example snapshots to guide structure and depth.

## Example prompts

- "Use `create-project-docs` to rewrite this repo's README and split deeper topics into `docs/references`."
- "Use `create-project-docs` to create onboarding docs for this repo from its Makefile, package manifests, and current code layout."
- "Use `create-project-docs` to analyze this repo and decide what belongs in `README.md` versus reference docs."

## References

- Main workflow: [SKILL.md](SKILL.md)
- Validation gate: [references/validation-checklist.md](references/validation-checklist.md)
- README template: [assets/templates/project-readme-template.md](assets/templates/project-readme-template.md)
- Example snapshots: [examples/](examples)
