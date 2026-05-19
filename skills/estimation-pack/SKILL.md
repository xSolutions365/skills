---
name: estimation-pack
metadata:
  version: "3.1"
  changelog: "V3.1 (2026-05): adds CreateFuture Activation terminology, additive Activation sizing by named triggers, and the Activation compression trap. V3 (2025): AI-native delivery readiness, agentic tooling maturity, architectural review + AI showcase shapes, quality-gate calibration."
description: >
  USE WHEN a pre-sales lead, delivery lead, architect, or commercial lead needs to qualify a software delivery opportunity, shape an estimate, recommend a delivery approach, or produce a proposal. Triggers include: "can we estimate this?", "what should our Phase 1 be?", "help me shape this bid", "is this ready to price?", "write me a question pack for the client", "what delivery model fits this?", "calibrate this estimate", "red flag check", "how should we staff this?", or any conversation involving pre-sales qualification, scoping, effort sizing, or delivery model selection. Also use it whenever the user shares a project brief, RFP, or opportunity description and wants estimation or proposal support, even without the word "estimate". V3.1 covers AI-native delivery readiness, agentic tooling maturity, architectural review and AI showcase engagement shapes, quality-gate calibration, CreateFuture Activation sizing with named triggers, and the Activation compression trap.
---

# Workflow

### Step 0: Run the estimation operating pack

- **Purpose**: Qualify opportunities, shape estimates, recommend delivery approaches, and produce proposal-ready outputs using the full operating pack below.
- **When**: Use whenever the skill trigger applies.
- Follow the gates in order, loading supporting material from [references/templates.md](references/templates.md) only when the matching output template is needed.

## Output

### Result Format

- Return the readiness level, red flags, targeted questions, recommended delivery shape, calibration assumptions, confidence grading, and proposal or handover artifacts requested by the user.
- Include explicit assumptions, risks, confidence levels, and unresolved evidence gaps.
- Do not present proposal-grade precision unless Gate 1 reaches Level 3.

## Internal Estimation Pack, V3.1

An internal operating pack for CreateFuture pre-sales leads, delivery leads, architects, product leads, and commercial leads. Use when qualifying opportunities, shaping estimates, recommending delivery approaches, and producing proposal-ready outputs.

V3 extends V2 with explicit treatment of **AI-native delivery readiness**: the agentic tooling, quality gates, and execution-planning patterns that make AI-accelerated calibration credible. The pack now distinguishes between "AI-native estimate, AI-native ready team" and "AI-native estimate, conventionally tooled team" and prices the gap between them.

**Always work through the gates in order.** In compressed mode (deadline < 5 days), run Gates 1 to 3 simultaneously, default aggressively, cap at Level 2, and flag the confidence drop.

---

## Core operating principles

1. Do not estimate before establishing estimate readiness.
2. Optimise for useful decisions, not false precision.
3. Prefer the best delivery approach, not the biggest one.
4. Keep the first release narrower than stakeholders usually ask for, unless strong evidence suggests otherwise.
5. Separate estimate accuracy from proposal fit.
6. Separate AI-accelerated work from human-constrained work.
7. Separate pure effort truth from commercial staffing shape.
8. Prefer complete milestones over broad partial coverage.
9. Make assumptions explicit, confidence visible, and risks auditable.
10. If the evidence is weak, say so and constrain the output accordingly.
11. **Factor in the cost of AI tooling maturity.** An AI-native estimate is only credible if the team's agentic workflows, quality gates, and execution-planning patterns are already in place, or if the estimate explicitly includes the time to establish them. Never apply optimistic AI-native ranges to a team that has not yet earned them.

---

## Gate ownership

| Gate | Decision owner | Key contributors |
|---|---|---|
| Gate 1, Estimate readiness | Pre-sales lead | Commercial lead, delivery lead |
| Gate 2, Red-flag check | Pre-sales lead | Delivery lead, architect |
| Gate 3, Targeted questioning | Pre-sales lead | Architect, product lead |
| Gate 4, Delivery-shape recommendation | Delivery lead | Architect, product lead |
| Gate 5, Calibration application | Delivery lead | Architect, engineering lead |
| Gate 6, Estimation and packaging | Pre-sales + delivery lead jointly | Commercial lead, architect |

---

## Gate 1, Estimate readiness

Assign one of four readiness levels:

- **Level 0, Not estimate-ready.** Too little information. Produce observations, blockers, and next questions only.
- **Level 1, ROM only.** Directional sizing and delivery-shape guidance. Not proposal-grade.
- **Level 2, Shaped estimate with assumptions.** Delivery approach, phase structure, team shape, indicative commercial options.
- **Level 3, Proposal-grade estimate.** Full customer-facing proposal draft and pricing inputs with clear confidence.

**Minimum evidence test.** Check for: desired business outcome, likely Phase 1 boundary, major system components, main users or workflows, target environment/platform constraints, known integrations or data dependencies, timeline or milestone pressure, buying/decision context, and **agentic readiness of the target codebase (brownfield only)**.

For the agentic readiness check, the relevant question is whether the team has the six capability classes in `references/agentic-tooling-baseline.md` established (quality-gate pipeline, analyzer suite, execution-plan tooling, KB chain, codification, context capture). Class 1 (quality gates) is mandatory for any AI-native calibration. Classes 2 to 4 govern specific calibration adjustments in Gate 5. Classes 5 and 6 are confidence inputs.

If more than half of the readiness inputs are unknown, default to Level 0 or Level 1.

If agentic readiness is unknown but the engagement is being pitched as AI-native, cap at Level 2 until evidenced.

---

## Gate 2, Red-flag check

If any flag is present, constrain the estimate and recommend a narrower first engagement or paid Activation (see Gate 4 and the Activation sizing section).

### Scope risk flags (primary danger: building the wrong thing)
- No clear Phase 1 success definition.
- Multiple bundled scopes with one deadline.
- Commercially visible capabilities that are not operationally defined.
- Fixed scope and fixed deadline despite high uncertainty.
- Coexistence or migration obligations unclear.
- **Voice or conversational AI integration with vendor dependency** (e.g. ElevenLabs, Gemini, OpenAI Realtime). Vendor API stability, latency profile, and per-interaction cost are genuine unknowns and need a spike before commitment.
- **Multi-system data synchronisation without API documentation or sample data.** Sync semantics (push vs. pull, conflict resolution, idempotency) are typically under-specified and create open-ended scope.

**Response.** Recommend **Activation** (paid pre-Phase 1 engagement; size per the Activation sizing section after Gate 4), separate committed from aspirational scope, increase prominence of assumptions.

### Delivery risk flags (primary danger: building the right thing slowly or expensively)
- Legacy systems with no API and no documented schema.
- Sample data unavailable before delivery starts.
- Enterprise security or AI-tooling approval unresolved.
- Cloud or environment access model unclear.
- No decision-maker or product owner availability.
- NFRs unresolved but materially important.
- **Cross-platform infrastructure in scope** (e.g. GCP Terraform plus Azure Terraform in the same engagement) with deployment model and ownership unclear. Doubles the platform learning curve and the security review surface.
- **Large repo estate (50+ repos) with no domain mapping.** Estimating delivery work across an undocumented estate is unsafe. Recommend an architectural review engagement before any feature estimation.

**Response.** Add dependency assumptions and contingency, increase infra/integration estimates, recommend a mobilisation sprint, price governance overhead visibly.

**General red-flag actions.** Lower readiness by one level, recommend tighter first phase, reduce estimate granularity, increase visible assumptions and confidence warnings, avoid implying proposal-grade precision.

---

## Gate 3, Targeted questioning

Surface only the missing information with the highest impact. Classify each question as:

- **Critical.** Estimate or proposal likely >20% wrong without it.
- **Important.** Estimate likely 10 to 20% wrong without it.
- **Useful.** Improves fit but can be handled with defaults.

**Cap.** Max 6 critical, max 6 important, max 4 useful.

For the full question bank across all eleven categories (A through K), see `references/question-bank.md`. V3 adds:

- **Category J, AI-native delivery readiness.** Designed to test the six capability classes from `references/agentic-tooling-baseline.md`: quality-gate pipeline, analyzer suite, execution-plan tooling, KB chain, codification, context capture. Also covers AI-generated code policy and dev-environment freedom.
- **Category K, Platform and deployment.** Cloud provider, IaC maturity, container registry and pipeline, secrets management.

Ask for **evidence**, not just verbal answers.

---

## Gate 4, Delivery-shape recommendation

Determine the best first engagement shape based on: product certainty, technical risk concentration, dependency/decision structure, path to earliest demonstrable value, client commitment appetite, natural decomposition points, feedback dependency, and commercial and competitive context.

Do **not** select from a fixed menu first. Let the shape emerge from the opportunity.

**Alternative engagement shapes** (when full delivery commitment is not appropriate):

CreateFuture's umbrella term for the paid pre-Phase 1 engagement is **Activation**. The rows below are the sub-forms an Activation can take. A real Activation often bundles two or more of them — e.g. discovery-led with a foundations component, or shaping with an architectural review. Size the Activation against the cumulative triggers rather than picking a single row (see the Activation sizing section below).

| Shape | When to use | Typical duration | Output |
|---|---|---|---|
| Activation (discovery-led) | Product certainty is low | 2 to 4 weeks | Validated scope, backlog, architecture options, delivery plan |
| Shaping sprint | Brief too ambiguous to estimate directly | 1 to 2 weeks | Shaped brief, ROM estimate, recommended delivery approach |
| Technical spike | One technical risk dominates | 1 to 2 weeks | PoC, feasibility assessment, revised estimate |
| Foundations phase | Delivery path clear but env/access/governance will consume early sprints | 2 to 4 weeks | Working CI/CD, environments, access, baseline architecture |
| **Architectural review** | Client has a large existing estate with unclear tech debt, domain boundaries, or modernisation path | 1 to 3 weeks | Domain map, repo analysis (architecture, code-quality, security baselines), tech stack inventory, modernisation recommendations, optional explorer UI. Use a deterministic-plus-LLM analyzer suite where available rather than bespoke analysis |
| **AI showcase / rapid prototype** | Client needs to see AI-native delivery speed before committing, or a demo or proof-of-concept is the buying trigger | 1 to 3 days | Working deployed prototype (Firebase or Cloudflare hosted), demo-grade UI, evidence of velocity |

The architectural review shape is especially appropriate where a "large estate, no map" delivery flag was raised in Gate 2. The AI showcase shape is appropriate where the client is sceptical of AI-native claims and needs evidence before any sizeable commitment.

---

## Activation sizing and the compression trap

Activation is where commercial pressure most reliably degrades a sound estimate. Compression below a minimum viable duration is the single most consistent predictor of issues surfacing in delivery time that should have been retired in pre-engagement time. Treat this section as mandatory whenever the Gate 4 recommendation includes any form of Activation.

**Why this section exists.** Once an Activation has been recommended, the pre-sales lead is often pushed — internally by commercial, or externally by the client — to compress it. The pressure is usually framed as "we can pick that up in Sprint 1" or "let's not delay mobilisation". Both are wrong when triggers compound. Use this section to calculate the floor, name the consequences explicitly, and surface the compression decision in the decision log.

### Minimum viable Activation by trigger

Triggers stack **additively**. Start from a 1-week floor for any paid Activation and add the increments below. Cap at 6 weeks total unless multiple severe triggers apply.

| Trigger present in the brief or pursuit | Adds to the floor | Why |
|---|---|---|
| Multi-system data integration with no sample data or documented schemas | **+2 weeks** | Sample data acquisition + schema documentation + integration inventory cannot reliably compress below this without leaving open-ended scope in the delivery contract |
| Large existing repo estate / undocumented domain map / brownfield codebase | **+2 weeks** (architectural review minimum) | Class 2 analyzer suite needs runtime against the actual estate, not interview output. Domain mapping needs at least one pass |
| AI-native delivery pitched but client AI policy / security review unconfirmed | **+1 week** | Security/IP review cycles cannot be parallelised with delivery without taking the AI-native uplift on faith. Class 1 quality-gate mobilisation needs the agreed policy first |
| Enterprise security review / Cyber Essentials Plus / unfamiliar landing zone | **+1 week** | AWS SCP / platform-team / account-model surprises emerge here, not in delivery sprints |
| NFRs aspirational but contractually material (sub-100ms p99, multi-nine SLAs, real-time guarantees) | **+1 week** | NFR baselining and current-state measurement is a discrete activity; assuming it can happen in delivery sprints is a category error |
| Ops workflow undocumented but materially involved in Phase 1 (data correction, approval workflows, content review queues, automation impact on staff) | **+1 week** | Workflow shadowing surfaces operationally-sensitive scope before it becomes a delivery-time scope shaper |
| Single decision-owner not yet named, or multi-stakeholder governance complex | **+0.5 weeks** | Decision-routing during Activation alone retires more risk than another week of discovery on a thing with no decision-owner |

**Apply additively.** A brief with sample-data + AI-policy + NFR triggers = a 4-week minimum, not "2-3 weeks should be enough". A brief with sample-data + repo-estate + AI-policy + ops-workflow = the 6-week cap.

### Compression consequences to name explicitly

When pushing back on pressure to compress Activation below the calculated floor, name the consequences. Use this language in the proposal, the internal commercial conversation, and the decision log:

- **AI-native uplift confidence drops to Low.** The optimistic backend calibration ranges (0.65x to 0.8x) become unfundable. Effort returns to the traditional comparator (+25% to 40% person-days). If this is not factored into the price, the delivery team eats it.
- **Data-integration estimate becomes Low confidence.** Downstream scope-gap risk shifts into the delivery contract — where it becomes a change request, not an Activation finding, and the commercial conversation happens at the worst possible time.
- **Stakeholder / ops-workflow scope discovery slips into delivery sprints.** Operationally-sensitive findings (workflow automation impact on staff, data trust gaps, override semantics, multi-team governance) surface as scope-shapers two-thirds of the way through Phase 1 rather than as Phase 1 boundary inputs.
- **NFR contradictions surface in late hardening.** What reads as a single availability line in the brief is often a five-nines requirement in one document and a two-nines reality in another. The compression-induced gap typically lands as a remediation plan halfway through Phase 1.
- **Quality-gate establishment moves into delivery sprints.** Class 1 establishment is non-negotiable; if it does not happen in Activation, it happens in Sprint 1, where it competes with feature delivery and looks like slow throughput rather than necessary investment.

### When compression is unavoidable

Sometimes the commercial conversation forces a shorter Activation. When that happens:

- **Hold the Phase 1 commitment soft.** Re-price Phase 1 only after the compressed Activation has surfaced the largest unknowns. Do not commit to a fixed Phase 1 price against unresolved triggers.
- **Cap Activation scope to the highest-impact triggers.** The three load-bearing activities are almost always: data discovery (sample data + schemas), AI policy alignment, and NFR baselining. If compression forces a choice, those three are the ones to keep.
- **Surface the compression decision in the decision log (Template E).** Named consequences, named impact-if-wrong analysis, named acceptance from the commercial sponsor. This is not optional — the team that inherits the delivery contract needs to see the trade-off that was made.
- **Increase visible contingency on the items that didn't make the cut.** A trigger that's been skipped in Activation gets a +20% to 30% loading on the relevant Phase 1 effort line, with the assumption explicit in the proposal.

---

## Gate 5, Calibration application

Apply calibration ranges from the tables below. Use the transfer table (Template F) to decide which benchmark lessons apply strongly, partially, or not at all.

### Default calibration ranges

| Area | Default range | Notes |
|---|---|---|
| AI-assisted backend delivery | 0.65x to 0.8x traditional equivalent | Best for repeated backend/service patterns |
| AI-assisted spec/doc work | 0.3x to 0.5x traditional equivalent | Only where approval cycles are not the bottleneck |
| Complex frontend with business logic | 1.2x to 1.5x equivalent backend complexity | Builders, dynamic forms, role-sensitive admin UI |
| Enterprise infrastructure overhead | 1.2x to 1.5x naive infra effort | Where governance and approvals are real |
| Second comparable vendor integration | 0.4x to 0.6x of first comparable integration | Only if adapter/auth/data patterns are genuinely similar |
| Alignment allowance | +3 to +7 person-days per major milestone | Depends on number of parallel workstreams |
| Discovery overhang in Sprint 1 to 2 | 20% to 35% non-feature throughput | Use when major decisions remain live |
| Final convergence capacity | 60% to 75% feature capacity | Protect final milestone/sprint |
| Additional engineering capacity if AI removed (timeline fixed) | +25% to 40% | Mostly on backend/docs-heavy programmes |
| Timeline increase if AI removed (team size fixed) | +20% to 35% | Less benefit in governance-heavy work |
| **AI-generated showcase or rapid prototype** | **0.5 to 2 person-days** | **Only where scope is demo-grade, a template exists, and deployment is pre-wired (Firebase or Cloudflare). Not production code.** |
| **Repo-wide baseline assessment (analyzer-driven)** | **1 to 3 person-days for a typical medium repo (50k to 500k LOC), 3 to 7 person-days for large or multi-repo estates** | **Using the deterministic-plus-LLM analyzer suite (architecture, quality, security, performance, root cause). Not feature delivery effort. If analyzer suite is not established, see Gate 5 tooling maturity modifier.** |
| **KB-chain spec generation (lean canvas, PRD, impact analysis)** | **1 to 3 person-days per medium feature** | **Only where the KB chain (class 4 of agentic tooling baseline) is established. If absent, revert to traditional spec calibration.** |

### Tooling maturity modifier

Apply *after* the default ranges, based on the agentic and quality-gate maturity of the team and target environment. The capability classes referenced below are defined in `references/agentic-tooling-baseline.md`. A team using a non-Enaible toolchain that covers the same capability classes is treated equivalently.

| Condition | Calibration adjustment |
|---|---|
| Class 1 (quality-gate pipeline) established and pre-commit enforced (typing, linting, formatting, tests, build) | Apply optimistic AI-assisted backend ranges from Sprint 1 |
| Class 1 absent or partial (no pre-commit gates or CI pipeline) | Add 3 to 5 day mobilisation block before AI-native calibration applies, and grade AI-native uplift confidence as Low until established |
| Class 2 (analyzer suite) established | Apply tight calibration to repo-wide baseline assessments (1 to 3 person-days for medium repos) |
| Class 2 absent | Either add 2 to 5 days to set up an analyzer baseline, or recommend a separate architectural review engagement |
| Class 3 (execution-plan tooling) in use for task decomposition | Reduce discovery overhang by 5 to 10% (tasks arrive pre-decomposed) |
| Class 4 (KB chain: lean canvas, PRD, impact analysis) established | Apply 0.3x to 0.5x on spec and documentation work confidently |
| Class 4 absent | Revert to traditional spec calibration (1.0x); do not apply AI uplift to spec work |
| Class 5 (codification skills in use) | No calibration change; treat as positive confidence input on AI tooling maturity |
| Class 6 (context capture and health) absent | Add 0.5 to 1 day per sprint contingency for environment friction |
| Token usage and AI cost tracking configured (`ccusage` or equivalent) | No estimate adjustment, but improves commercial confidence grade |
| Multiple coding agents in scope (Claude Code plus Cursor plus Copilot, etc.) | Add 0.5 to 1 person-day per additional agent if a render pipeline is in place; 2 to 4 person-days per additional agent if not |
| Multiple target languages in scope | Multiply mobilisation block by 1.3 to 1.6 for per-language gate setup, unless pre-existing configuration is evidenced |

### Apply optimistic AI-native calibration when:
- Backend follows repeated CRUD/API/service patterns with well-understood data models.
- Schemas and sample data available before delivery starts.
- Team has used AI-native tooling on at least one prior engagement.
- CI/CD and environment provisioning already established.
- Spec and documentation work does not require multi-stakeholder approval cycles.
- Greenfield work with no legacy constraints.

### Do NOT apply optimistic AI-native calibration when (anti-transfer rules):
- Architecture is novel or safety-critical.
- Work is dominated by stakeholder decisions or approvals.
- Vendor responsiveness is likely to be slow.
- Security or compliance design is the main challenge.
- Frontend is highly bespoke and business-logic-heavy.
- Sample data and schemas are unavailable.
- Second integration is not truly comparable to the first.
- **Team has no experience with agentic coding tools** (Claude Code, Codex, Cursor, Copilot at agent tier, etc.). Either reduce the AI-native uplift by 50% or recommend an explicit 1-week ramp sprint to establish working patterns before optimistic ranges apply.

---

## Gate 6, Estimation and packaging

Produce the right output for the readiness level:

- **Level 0.** Observations, blockers, next questions, recommendation on how to get estimate-ready (Template A).
- **Level 1.** Recommended engagement shape, ROM range, top assumptions, top risks, confidence by area (Template A).
- **Level 2.** Everything above plus phase and milestone plan, deliberate Phase 1 exclusions log, team shape by phase, commercial options, decision log, confidence table, and the agentic delivery mobilisation checklist where AI-native delivery is in scope (Templates A, C, D, E, F, H).
- **Level 3.** Everything from Level 2 plus customer-facing proposal draft, storyboard or slide outline, pricing-sheet inputs, delivery handover brief (Templates A, B, C, D, E, F, G, H).

### Agentic delivery mobilisation checklist (Template H)

Whenever the engagement will use AI-native delivery, include the mobilisation checklist as a Phase 0 or Sprint 0 in the plan. The estimate must either show these as already in place (with evidence) or include the time to establish them. The checklist is structured around the six capability classes in `references/agentic-tooling-baseline.md`:

- **Class 1, Quality-gate pipeline.** Pre-commit hooks for typing, linting, formatting, tests, and build, all enforced. Trunk-based development. CI re-checks on every push.
- **Class 2, Analyzer suite.** Architecture, code-quality, security, performance, and root-cause analyzers configured and runnable on the engagement repo.
- **Class 3, Execution-plan tooling.** Task decomposition tooling configured and execution plans created for first-milestone tasks.
- **Class 4, KB chain.** Knowledge-base repository configured for spec generation; lean canvas, PRD, and impact-analysis tooling available.
- **Class 5, Codification.** Skills configured for capturing patterns from git history, PR reviews, and AI-assisted sessions (confidence input only).
- **Class 6, Context capture and health.** Cross-platform agent context retrieval and environment health-check tooling in place.

Also confirm:
- Approved AI tooling list with the client (per-agent if more than one).
- Dev environments allow required CLI and extension installs.
- AI-generated code policy understood (IP, security review, approval flow).
- Token usage and AI cost tracking configured with agreed ceiling and review cadence.

If any item is missing and not budgeted, mark AI-native uplift confidence as Low and surface this in the confidence table. See Template H in `references/templates.md` for the structured checklist.

---

## Confidence grading

Every substantial output must include confidence by area using **High / Medium / Low**.

Mandatory areas: Phase 1 boundary, Delivery approach, Infrastructure or platform estimate, Data or integration estimate, Frontend or UX estimate, Team shape, Timeline, AI-native uplift assumptions, **AI tooling and workflow maturity** (is the agentic stack proven, partially established, or aspirational?), Commercial framing.

---

## Team shape rules

Always distinguish between **effort-based demand** (what the work strictly requires) and **commercial staffing recommendation** (what is sellable, resourceable, and delivery-sensible).

**Prefer.** Continuous engagement blocks, fewer roll-ons and roll-offs, stable core engineering and delivery leadership, 0.5 FTE across a phase rather than micro-spikes.

**Avoid.** Morse-code staffing, repeated short bursts for the same role, artificially fragmented client-facing team shapes.

**Burst roles.** Cloud or platform specialists, security specialists, UX or design during shaping-heavy periods, BA or strategy during early shaping.

**Continuity roles.** Product leadership, delivery leadership, backend engineering, frontend engineering, mobile engineering (where in scope), QA or quality leadership once delivery stabilises.

---

## Output templates

For all output templates (A through H), see `references/templates.md`. For the agentic tooling capability-class framework underpinning the mobilisation checklist and Gate 5 modifier, see `references/agentic-tooling-baseline.md`.

Templates included:
- **A**, Estimate readiness summary
- **B**, Tailored client question pack
- **C**, Internal estimation summary
- **D**, Confidence table
- **E**, Decision log
- **F**, Calibration transfer table
- **G**, Delivery handover brief
- **H**, Agentic delivery mobilisation checklist

---

## Common failure modes this pack prevents

- Overbuilding Phase 1.
- Treating aspirational scope as committed scope.
- Overclaiming AI speedups, especially on teams that have not yet earned them.
- Underestimating enterprise foundations.
- Ignoring decision and governance drag.
- Producing precise staffing patterns that are not resourceable.
- Making a proposal that is technically sensible but commercially mismatched.
- Losing critical context when pre-sales hands over to delivery.
- Pricing AI-native delivery as if quality gates and agentic tooling were already in place when they are not.
- Estimating feature delivery against a large undocumented repo estate without recommending an architectural review first.

---

## Bottom line

A good internal estimate is not the most detailed one. It is the one that recommends the right first commitment, is honest about uncertainty, calibrates AI claims credibly against the team's actual tooling maturity, can actually be staffed and delivered, improves the chances of winning the right work, and hands over cleanly to the team that will deliver it.
