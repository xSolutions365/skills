# Step 0: Preflight + scaffold artifacts

Objective: create deterministic plan artifacts under a timestamped run directory.

## Inputs

- Plan title.
- Caller project root (git top-level from the current working directory when available; otherwise the current working directory).

## Required actions

1. Resolve artifact root:
   - `<project-root>/.plan/create-execplan/<timestamp>/`
   - Workspace subdirectory: `<project-root>/.plan/create-execplan/<timestamp>/workspace/`
2. Resolve the skill root as the directory containing `SKILL.md`, then treat `scripts/`, `references/`, and `templates/` paths from this workflow as anchored there.
3. Invoke the skill-local scaffold script while preserving the caller project working directory:
   - `python3 scripts/scaffold_execplan.py --title "<plan-title>"`
   - Do not reference repo paths such as `shared/skills/create-execplan/scripts/...` in deployed use.
   - Do not change the working directory to the skill root before invocation; artifact output must remain project-local.
4. Confirm final handoff files exist in the artifact root:
   - `context-pack.md`
   - `execplan.md`
   - `review-checklist.md`
5. Confirm workflow workspace files exist in `<artifact-root>/workspace/`:
   - `draft-review.md`
   - `context-discovery.md`
   - `context-evidence.json`
   - `context-codemap.md`
   - `requirements-freeze.md`

## Done when

- Artifact root exists and all required files are generated.
- Workspace artifacts are separated from final handoff artifacts.
- Context discovery, evidence, codemap, draft review, and requirements freeze artifacts are generated in `workspace/`.
- Step references, templates, and scripts are resolvable from the skill root, while artifacts resolve under the caller project root.
