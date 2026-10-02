---
name: payment-legislation-gap-analysis
description: >
  Sweep the operator payments code (payments library, deposit/withdraw/refund + webhook APIs,
  wallet ledger) against US + Canada PAYMENT / financial-services LEGISLATION — EFTA/Reg E,
  Nacha/ACH return codes, tax withholding on payouts, card-network programs, money-transmitter &
  stored-value, OFAC/sanctions, BSA/AML, data privacy, DFS fund-types, CFTC/FMX segregation,
  chargebacks, prohibited-state geofencing — checking code compliance + unit/FAST test coverage,
  one subagent per lane, into a RAG matrix. Use when you need a payment-law / financial-services
  compliance review of the payments code, to re-run the payment legislation sweep, pull the latest
  payment legislation, add a lane, or check ONE area (Nacha R01-vs-R10, Reg E disputes, OFAC on
  payouts, AFT/OCT/MCC, W-2G, DFS/FMX). Financial-services-LAW layer: for per-STATE GAMING rules
  (withdrawal SLAs, RG/self-exclusion lists, reserve, cash-at-cage) use the sibling
  state-compliance-gap-analysis skill; not for ordinary coding or non-payments compliance.
compatibility: Requires the Agent tool (parallel subagents), Bash, and Python with openpyxl for the matrix build. Codebase(s) must be readable on the local filesystem.
metadata:
  author: Alyssa Henley
  version: "1.0"
---

# Workflow

Reviews the payments codebase against **payment/financial-services legislation** — the federal
and cross-cutting money-movement laws that apply *regardless of which state's gaming rules are
in force*. This is the complement to `state-compliance-gap-analysis` (per-state gaming operating
rules). Two things are assessed for **every** requirement: **code compliance** (does the code
implement the requirement correctly?) and **test coverage** (is the *correct* behavior and its
failure mode asserted, and at what layer — unit is preferred over integration). A control that
exists but is untested is a latent gap; a test that asserts non-compliant behavior is worse than
none.

### Step 1: Scope and optionally refresh the legislation lanes

- **Purpose**: Fix what the run will cover and decide whether to refresh the bundled law first.
- **When**: Once, before any recon or fan-out.
- Confirm (or state assumptions if unattended): codebase paths in scope, lanes to run (default:
  every lane), web verification / legislation refresh on or off, and prior workspace if this is
  a refresh.
- Create a workspace next to nothing important: `payment-legislation-analysis-<date>/` with a
  `findings/` subdirectory.
- Read the lane catalogue, repos-in-scope, refresh mechanics, and add-a-lane guidance in
  [references/lanes-index.md](references/lanes-index.md).

### Step 2: Recon the repos and write the repo map

- **Purpose**: Discover the repo once so subagents don't each rediscover it.
- **When**: After scope, before fan-out.
- Explore the codebase briefly and write `<workspace>/repo-map.md` (~40-80 lines): module layout
  across the repos; payment-flow entry points (deposit, withdrawal, refund, webhooks, ledger
  write); where per-state/config data lives; test-suite layout and how unit vs integration/e2e
  tests are separated; build/CI files. Reuse a prior repo-map if one exists.
- The review method every lane subagent follows (code compliance AND test coverage) is in
  [references/review-checklist.md](references/review-checklist.md).

### Step 3: Fan out one subagent per lane

- **Purpose**: Review each legislation lane against the code and tests in parallel.
- **When**: After the repo map exists.
- Spawn one general-purpose subagent per lane in parallel batches of ~6-8 (a batch per message;
  wait for a batch before the next so failures are visible early). If no Agent tool is available,
  run the lanes yourself sequentially with the same method and contract.
- Use the prompt template, batching rules, and eager-to-please guardrails in
  [references/orchestration.md](references/orchestration.md).

### Step 4: Validate, retry, and spot-check findings

- **Purpose**: Make sure the findings are schema-valid and actually hold before condensing.
- **When**: After each batch, and again before reporting.
- Validate each batch with the matrix builder's `--check` mode; re-run any invalid/missing lane
  once; a lane that fails twice is recorded `unknown` with a note. Then spot-check 3-5 findings
  (every `red`, plus one suspiciously-clean lane) against the cited files/lines.
- The output contract subagents must satisfy is defined in
  [references/findings-schema.md](references/findings-schema.md).

### Step 5: Condense, deliver, and handle refresh runs

- **Purpose**: Produce the RAG decision matrix and executive summary, and ship them.
- **When**: After spot-checking passes.
- Build the matrix and summary, replace the summary placeholder with real cross-lane synthesis
  (the code-gap vs test-gap split, what to fix first), deliver both files with the not-legal-advice
  caveat, and on a re-run lead with what changed.
- The commands, spot-check discipline, synthesis guidance, and refresh-run rules are in
  [references/condense-and-deliver.md](references/condense-and-deliver.md).

## Output

### Result Format

- Two deliverables written into the workspace: a decision matrix (`decision_matrix.xlsx`, lanes ×
  areas RAG plus a filterable findings sheet and a summary sheet) and an `executive_summary.md`
  whose placeholder has been replaced with 2-3 paragraphs of real cross-lane synthesis.
- Each finding records both a code-compliance rating and a test-coverage rating, cites real
  files/lines, and uses `not_found` with a where-you-looked note (or an external-ownership note)
  rather than a guessed `present`.
- Hand-off message names the overall RAG, the worst findings, the code-gap vs test-gap split, and
  the standing caveat that citations were researched/refreshed at run time and this is not legal
  advice.
