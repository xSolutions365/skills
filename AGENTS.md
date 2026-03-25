# Repository Notes

- Install the Git hooks before your first commit with `pre-commit install` and `pre-commit install --hook-type commit-msg`.
- This repository uses a centralized pre-commit quality gate runner at `scripts/run-ci-quality-gates.sh`.
- The quality gates include a custom shell-based linter for the repo's opinionated skill structure, plus parity checks so local hooks and GitHub Actions run the same entrypoint.
- Use `AGENTS.md` as the canonical repository instruction filename. Do not add a lowercase `agents.md` variant.
- Local skill deployment uses `scripts/deploy-skill-local.sh <skill-id>`, which syncs `skills/<skill-id>/` into `~/.agents/skills/<skill-id>/`.
