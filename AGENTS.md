# Repository Notes

- Install the Git hooks before your first commit with `pre-commit install` and `pre-commit install --hook-type commit-msg`.
- This repository uses a centralized pre-commit quality gate runner at `scripts/run-ci-quality-gates.sh`.
- The quality gates include a custom Python linter for the repo's opinionated skill structure, plus parity checks so local hooks and GitHub Actions run the same entrypoint.
