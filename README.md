# createfuture skills

A multi-skill repository for `npx skills add`.  It uses an opinionated approach to the www.agentskills.io standard.

This approach is reinforced by the available create-skill.

## Repository shape

The installer scans for `SKILL.md` files. This repo intentionally uses:

- `skills/<skill-folder>/SKILL.md`

This keeps the root free of a top-level `SKILL.md`, so `npx skills add <repo> --list` discovers a collection of skills.

## Install examples

By default, `npx skills add` installs into the current project's `.agents/` directory. Use `-g` to install these skills at user level instead.

```bash
# List skills from this repo
npx skills add <repo-url> --list

# Install interactively at user level
npx skills add <repo-url> -g

# Install one skill only at user level
npx skills add <repo-url> --skill create-skill -g

# Install all skills to all agents at user level without prompts
npx skills add <repo-url> --all -g
```

## Included skills

- `create-skill`
- `adaptive-prose`
- `create-execplan`
- `visual-explainer`
