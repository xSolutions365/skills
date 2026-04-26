# Validation Checklist

Use this checklist after preview generation and after final file generation. Output must be binary: `PASS` or `FAIL`.

## Shared deterministic rules

- `G1` Frontmatter integrity:
  - frontmatter parses as valid YAML
  - `name` exists and matches the directory name
  - generated output quotes frontmatter string values
  - `description` includes exactly one `USE WHEN` clause
  - `description` is one routing sentence under 200 characters
  - detailed capability lists, preset catalogues, and colon-labelled enumerations are absent from frontmatter
- `G2` Route classification:
  - exactly one route is selected
  - generated file shape matches the selected route
  - route-specific line limits are satisfied
- `G3` Link and path integrity:
  - all relative links resolve within the skill root
  - no absolute filesystem paths appear in generated content
  - no references to external rendered output trees or repo-private tooling paths
- `G4` Self-contained constraint:
  - required templates and references live inside the generated skill directory when the route needs them
  - no generated skill relies on repo-specific CLIs, scripts, or directories outside the skill root
- `G5` Summary-artifact exclusion:
  - no file named `generation-summary.md` is generated
  - no payload field named `output_contract` is present
  - no instruction says to save a retained summary artifact

## Route-specific rules

Before evaluating route-specific rules, identify `template_type` from the approved payload. The approved payload is the source of truth for route selection; do not infer the route from generated file shape unless the payload is unavailable. Evaluate exactly one route rule and ignore the other three:

- `behaviour-guidance`: evaluate `R1` only; ignore `R2`, `R3`, and `R4`.
- `simple-task:inline`: evaluate `R2` only; ignore `R1`, `R3`, and `R4`.
- `simple-task:runbook-index`: evaluate `R3` only; ignore `R1`, `R2`, and `R4`.
- `multi-step-workflow`: evaluate `R4` only; ignore `R1`, `R2`, and `R3`.

If `template_type` is missing or not one of these exact values, fail `G2`.

When validating an existing skill without an approved payload, infer the route from file shape:

- `# Guidance` plus single `SKILL.md`: infer `behaviour-guidance`.
- `# Task` plus no `references/`: infer `simple-task:inline`.
- `# Task` plus `references/`: infer `simple-task:runbook-index`.
- `# Workflow` plus `README.md` or `references/`: infer `multi-step-workflow`.
- Any other shape fails `G2`.

- `R1` Behaviour guidance:
  - body starts at `# Guidance`
  - generated output is a single `SKILL.md`
  - total `SKILL.md` length is at or under 100 lines
  - no `references/`, `assets/`, `scripts/`, or `README.md` files are generated
- `R2` Simple task inline:
  - body starts at `# Task`
  - generated output is a single `SKILL.md`
  - total `SKILL.md` length is at or under 500 lines
  - procedure, validation, and output guidance are self-contained
- `R3` Simple task runbook index:
  - body starts at `# Task`
  - `SKILL.md` stays at or under 500 lines
  - every runbook is under `references/*.md`
  - every runbook is linked from `SKILL.md`
  - runbooks are optional to load at runtime, but every generated runbook file must be linked from `SKILL.md`
- `R4` Multi-step workflow:
  - body starts directly at `# Workflow`
  - `## Output` appears after `# Workflow`
  - `## Output` includes `### Result Format`
  - each `### Step N` includes exactly one workflow reference link to `references/*workflow.md`
  - step numbering is contiguous and ordered
  - `README.md` exists with Overview, When to use it, and Example prompts sections
  - no redundant H1 title block, summary paragraph, or primary use-case bullets appear before `# Workflow`

## Natural-language quality rules

- `N1` Procedural guidance quality:
  - instructions explain how to execute the route, not just what terms mean
  - imperative actions are concrete and testable
- `N2` Preview fidelity:
  - the preview matches the approved payload with no hidden additions
  - file order is deterministic
- `N3` Vague action rejection:
  - avoid `investigate`, `review`, `consider`, `look at`, `think about`, or `explore` unless paired with concrete output criteria
- `N4` Portability:
  - instructions remain portable across repositories and do not assume one repo's internal tooling
- `N5` Generator-guidance exclusion:
  - generated outputs do not copy authoring guidance that is only meant for `create-skill` itself
  - generated prose should read like target-skill instructions, not template commentary

## Evaluation procedure

1. Evaluate `G1` through `G5` in order and fail immediately if frontmatter is not valid YAML.
2. Map `template_type` to exactly one route rule using the route-specific table.
3. Evaluate `N1` through `N5` only if all deterministic rules pass.
4. Record one evidence line for every evaluated rule group.
5. If any rule fails, return `FAIL` and list corrective actions.

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
- SELECTED_ROUTE: <template_type>
- ROUTE_RULE_EVALUATED: <R1|R2|R3|R4>
- ROUTE_RULE_IGNORED: <comma-separated non-selected route IDs>
- R*: <selected route evidence>
- N1: <evidence>
- N2: <evidence>
- N3: <evidence>
- N4: <evidence>
- N5: <evidence>
CORRECTIVE_ACTIONS:
- <required fix 1>
- <required fix 2>
```
