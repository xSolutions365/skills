# createfuture skills

A multi-skill repository for `npx skills add`.  It uses an opinionated approach to the www.agentskills.io standard.

This approach is reinforced by the available create-skill.

## Repository shape

The installer scans for `SKILL.md` files. This repo intentionally uses:

- `skills/<skill-folder>/SKILL.md`

This keeps the root free of a top-level `SKILL.md`, so `npx skills add <repo> --list` discovers a collection of skills.

## Install examples

```bash
# List skills from this repo
npx skills add <repo-url> --list

# Install interactively
npx skills add <repo-url>

# Install one skill only
npx skills add <repo-url> --skill create-skill

# Install all skills to all agents without prompts
npx skills add <repo-url> --all
```

## Included skills

- `create-skill`
- `adaptive-prose`
- `create-execplan`
- `visual-explainer`
