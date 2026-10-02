---
name: state-compliance-gap-analysis
description: >
  Run a jurisdiction-by-jurisdiction gaming compliance gap analysis of a payment gateway codebase
  — all 50 US states + DC plus Ontario and Alberta, Canada — using parallel subagents, condensing
  findings into a RAG decision matrix (.xlsx) and executive summary. Use when the user asks to
  analyse the operator codebase against state or provincial regulations, review jurisdictions in
  parallel, check a jurisdiction's payment requirements against code, build or refresh the
  compliance decision matrix, or run "the gap analysis" — even if the user names just one, e.g.
  "check Michigan withdrawals against the code" or "does this cover Ontario or Alberta". Also use
  when asked what a jurisdiction requires of gaming payments (including AGCO/iGO, AGLC/AiGC, and
  Canadian PCMLTFA/FINTRAC obligations), or who wrote or last touched the code behind a gap, or to
  split findings by Create Future vs client authorship.
compatibility: Requires the Agent tool (parallel subagents), Bash, and Python with openpyxl for the matrix build. Codebase must be readable on the local filesystem; code-origin attribution additionally needs it to be a git clone with real history (not a shallow or export copy).
metadata:
  author: Alyssa Henley
  version: "1.0"
---

# Workflow

Reviews a payment gateway codebase against each jurisdiction's gaming/payments requirements using
one subagent per jurisdiction, then condenses everything into a decision matrix. Covers all 50 US
states + DC plus **Ontario and Alberta, Canada**, which run against a separate Canadian federal
baseline rather than the US one. Built for Create Future gaming-payments engagements, but works on
any North American gaming payments codebase. This is the per-state gaming complement to
`payment-legislation-gap-analysis` (federal money-movement law).

### Step 1: Scope the run

- **Purpose**: Fix codebase path, jurisdictions, web verification, prior workspace, and whether
  code-origin attribution runs.
- **When**: Once, before any recon or fan-out.
- Confirm (or state assumptions plainly if unattended): codebase path; jurisdictions in scope
  (default: every jurisdiction; a 3-5 jurisdiction pilot of `nj`, `pa`, `mi` + one or two others
  is a sensible first run); web verification on/off; prior workspace if this is a refresh; and
  attribution on/off (default on when the codebase is a git clone with real history).
- Create a workspace next to nothing important: `gap-analysis-<date>/` with a `findings/`
  subdirectory.
- The jurisdiction catalogue, the two federal baselines (pick by country), and the FAST-vs-unit
  terminology are in [references/jurisdictions-index.md](references/jurisdictions-index.md).

### Step 2: Recon the repo and write the repo map

- **Purpose**: Discover the repo once so subagents don't each rediscover it.
- **When**: After scope, before fan-out.
- Explore briefly and write `<workspace>/repo-map.md` (~40-80 lines): top-level module layout;
  where per-state configuration lives (paths + format); payment-flow entry points (deposit,
  withdrawal, refund, webhooks); test-suite layout — which suites are isolated unit tests versus
  FAST/service-level suites, and how they are separated; build/CI files. If the repo has no
  per-state configuration at all, say so — that itself is a cross-cutting finding.
- The review method every subagent follows is in
  [references/review-checklist.md](references/review-checklist.md).

### Step 3: Fan out per-jurisdiction and federal lanes

- **Purpose**: Review each jurisdiction (plus the right federal lane) against the code in parallel.
- **When**: After the repo map exists.
- Spawn one general-purpose subagent per jurisdiction plus one FED lane, in parallel batches of
  ~6-8. Pick the federal lane by country and never mix them; read the Canadian traps before
  letting any finding cross the border. If no Agent tool is available, run the lanes yourself
  sequentially with the same method and contract.
- The prompt template, federal-lane selection, unpublished-rule and Canada traps, and
  eager-to-please guardrails are in [references/orchestration.md](references/orchestration.md).

### Step 4: Validate, retry, and spot-check findings

- **Purpose**: Make sure the findings are schema-valid and actually hold before condensing.
- **When**: After each batch, and again before reporting.
- Validate each batch with the matrix builder's `--check` mode; re-run any invalid/missing state
  once; a state that fails twice is recorded `unknown` with a note. Then spot-check 3-5 findings
  (every `red`, plus one suspiciously-green state) against the cited files/lines.
- The output contract subagents must satisfy is defined in
  [references/findings-schema.md](references/findings-schema.md).

### Step 5: Attribute code origin

- **Purpose**: Label each gap Create Future vs client so it is routed to the right fixer. Skip if
  attribution is off.
- **When**: After findings are validated and spot-checked, before condensing.
- Run the blame-attribution script once over the collected findings (they already cite file and
  line ranges), confirm the CF-marker pattern against real commit emails first, and read
  `no_code`/`unknown` with the grain of salt they deserve.
- The command, flags, label meanings, and the last-toucher caveat are in
  [references/attribution.md](references/attribution.md).

### Step 6: Condense, deliver, and handle refresh runs

- **Purpose**: Produce the RAG decision matrix and executive summary, ship them, and on a re-run
  lead with what changed.
- **When**: After attribution (or after Step 4 if attribution is off).
- Build the matrix and summary, keep the named attribution in the separate internal workbook,
  replace the summary placeholder with real cross-state synthesis, deliver with the
  not-legal-advice caveat, and re-run attribution on refreshes rather than reusing the old file.
- The commands, internal-file handling, synthesis guidance, and refresh-run rules are in
  [references/condense-and-deliver.md](references/condense-and-deliver.md).

## Output

### Result Format

- Deliverables written into the workspace: a decision matrix (`decision_matrix.xlsx`, states ×
  areas RAG plus a filterable findings sheet and a summary sheet) and an `executive_summary.md`
  whose placeholder has been replaced with 2-3 paragraphs of real cross-state synthesis.
- When attribution ran, an Origin column (org labels only) and origin roll-up appear in the
  shared workbook, and the named attribution is kept in a separate internal-only
  `attribution_internal.xlsx`.
- Each finding cites real files/lines, classifies test coverage as `unit_tested`,
  `integration_only`, `untested`, or `unknown` (never bare "fast"), and uses `not_found` with a
  where-you-looked note rather than a guessed `present`.
- Hand-off message names the overall RAG picture, the worst findings, the untested-vs-missing
  split, and the standing caveat that citations were researched Aug 2026, spot-verified at run
  time, and are not legal advice.
