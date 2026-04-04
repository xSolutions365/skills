# Validation Checklist

Use this checklist after preview generation and after final file generation. Output must be binary: `PASS` or `FAIL`.

## Deterministic checklist rules

- `G1` Frontmatter integrity:
  - frontmatter parses as valid YAML
  - `name` exists and matches the directory name
  - frontmatter string values are quoted
  - `description` includes a `USE WHEN` clause
  - `description` is one routing sentence under 200 characters
  - detailed capability lists, preset catalogues, and colon-labelled enumerations are absent from frontmatter
- `G2` Workflow structure:
  - `# Workflow` exists
  - `## Output` exists after `# Workflow`
  - `## Output` includes `### Result Format`
  - each `### Step N` includes exactly one workflow reference link to `references/*workflow.md`
  - step numbering is contiguous and ordered
  - generated `SKILL.md` content does not include generator-only meta-instruction lines
  - no redundant H1 title block, summary paragraph, or primary use-case bullets appear before `# Workflow`
- `G3` Step integrity:
  - each step states a purpose
  - each step states when to run if timing is conditional
  - each step includes concrete actions, not only definitions
  - user checkpoints use `**STOP**` only for explicit user confirmations
- `G4` Link and path integrity:
  - all relative links resolve within the skill root
  - no absolute filesystem paths appear in generated content
  - no references to external rendered output trees or repo-private tooling paths
- `G5` Self-contained constraint:
  - the workflow does not rely on repo-specific CLIs, scripts, or directories outside the skill root
  - all required templates and references live inside this skill directory
- `G6` Runtime-locality constraint:
  - no command execution or environment mutation appears outside `### Step N` sections
  - short orchestration snippets are only allowed inside the relevant step
  - detailed runtime commands and variable setup belong in the corresponding `references/*workflow.md` file
  - references must remain consistent with the step actions (each step that delegates runtime behavior names the same mechanism)

## Natural-language quality rules

- `N1` Procedural guidance quality:
  - instructions explain how to execute the workflow, not just what terms mean
  - at least 30% of step bullets are imperative actions
- `N2` Preview fidelity:
  - the preview matches the approved payload with no hidden additions
  - file order is deterministic
- `N3` Vague action rejection:
  - avoid `investigate`, `review`, `consider`, `look at`, `think about`, or `explore` unless paired with concrete output criteria
- `N4` Portability:
  - instructions remain portable across repositories and do not assume one repo's internal tooling
- `N5` Generator-guidance exclusion:
  - generated outputs do not copy authoring guidance that is only meant for `create-skill` itself
  - generated workflow prose should read like target-skill instructions, not template commentary

## Evaluation procedure

1. Evaluate `G1` through `G6` in order and fail immediately if frontmatter is not valid YAML.
2. Evaluate `N1` through `N5` only if all deterministic rules pass.
3. Record one evidence line for every rule group.
4. If any rule fails, return `FAIL` and list corrective actions.

## Required output format

```text
VALIDATION_STATUS: PASS|FAIL
FAILED_GATES: <comma-separated gate IDs or NONE>
EVIDENCE:
- G1: <evidence>
- G2: <evidence>
- G3: <evidence>
- G4: <evidence>
- G5: <evidence>
- G6: <evidence>
- N1: <evidence>
- N2: <evidence>
- N3: <evidence>
- N4: <evidence>
- N5: <evidence>
CORRECTIVE_ACTIONS:
- <required fix 1>
- <required fix 2>
```
