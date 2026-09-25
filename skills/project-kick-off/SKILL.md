---
name: "project-kick-off"
description: "Use when a cast team is preparing to kick off a client engagement and needs internal handover and client kick-off artefacts built from the SoW, transcripts and casting."
metadata:
  discipline: "product, design, delivery"
  stage: "discover, deliver"
  engagement: "discovery, build, strategic"
  owner: "product-and-experience"
  version: "0.4"
---

# Workflow

### Step 0: Preflight inputs and boundaries

- **Purpose**: Confirm the inputs, engagement shape, audiences, and output location before extracting anything.
- **When**: Run once at the start of every request.
- Require the signed or latest SoW or proposal, the casting list, and at least one pitch or scope transcript or set of notes; ask for anything missing.
- Classify the engagement as `discovery`, `build`, or `strategic` and set `@OUTPUT_ROOT` for the internal and client packs.
- Load the audience boundary, missing data, and cross-reference rules before reading any input, and rate context coverage.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Build the evidence ledger

- **Purpose**: Turn every input into a sourced ledger of commitments, stakeholders, expectations, dates, dependencies, and people.
- **When**: Run after Step 0 and before drafting any artefact.
- Tag each ledger entry with its source and whether it is `client-safe` or `internal-only`.
- Record every place where transcripts and the SoW disagree as a candidate expectation or scope entry.
- Workflow: [references/step-1-evidence-ledger-workflow.md](references/step-1-evidence-ledger-workflow.md)

### Step 2: Draft the internal team pack

- **Purpose**: Give the cast team everything the pitch team knows, plus a plan that fits the team as cast.
- **When**: Run after the ledger is complete.
- Draft the handover brief, expectation register, plan and ownership, trade-offs and RAID, and growth map from the internal templates.
- Treat casting as fixed; raise only uncast roles or unowned deliverables back to casting.
- Workflow: [references/step-2-internal-pack-workflow.md](references/step-2-internal-pack-workflow.md)

### Step 3: Draft the client kick-off pack

- **Purpose**: Produce the client-facing artefacts that get the engagement moving in week one.
- **When**: Run after the internal pack exists, using only `client-safe` ledger entries.
- Draft the kick-off agenda and deck content, engagement plan, prerequisites checklist, research access plan, ways of working, and final playback skeleton.
- Build the playback skeleton around the tangible outputs the final audience needs to see.
- Workflow: [references/step-3-client-pack-workflow.md](references/step-3-client-pack-workflow.md)

### Step 4: Validate both packs

- **Purpose**: Block leaks, unsourced claims, and unowned commitments before anything is shared.
- **When**: Run after both packs are drafted.
- Run the validation checklist and fix every failure before continuing.
- Workflow: [references/step-4-validation-workflow.md](references/step-4-validation-workflow.md)

### Step 5: Write files and hand back open questions

- **Purpose**: Save both packs and give the delivery lead a short list of decisions to confirm.
- **When**: Run only after Step 4 passes.
- Write the packs to `@OUTPUT_ROOT`, then report the open decisions, casting asks, and prerequisites with the earliest deadlines.
- Workflow: [references/step-5-delivery-workflow.md](references/step-5-delivery-workflow.md)

## Output

### Result Format

- `@OUTPUT_ROOT/internal/` holds the handover brief, expectation register, plan and ownership, trade-offs and RAID, growth map, pitch-lead questions when needed, and a `README.md` index. Mark every file `INTERNAL: do not share with client`.
- `@OUTPUT_ROOT/client/` holds a `README.md` index plus the kick-off agenda and deck content, engagement plan, prerequisites checklist, research access plan, ways of working, and final playback skeleton.
- Start the chat response with the readiness verdict (`READY`, `READY WITH GAPS`, or `HOLD`), then give: open decisions, casting asks, and the three most urgent prerequisites with owners and dates.
- Never invent names, dates, figures, or commitments that are missing from the evidence ledger; mark them `TO CONFIRM`, and mark sections built on missing inputs `LOW CONTEXT`.
