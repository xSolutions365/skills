# Question Bank, All Categories (V3)

Use this bank when running Gate 3. Only surface the unanswered gaps. Questions are listed in priority order within each category.

---

## Category A, Phase 1 success and scope shape

1. What does "done" look like for the first phase? If only one thing succeeds, what is it? *[Priority 1]*
2. Which parts of the brief are true Phase 1 requirements, and which are broader vision? *[Priority 1]*
3. Which capabilities must fully work in Phase 1, and which only need to be visible enough for demo, pre-sales, investor confidence, or internal buy-in? *[Priority 1]*
4. Is timeline fixed, scope fixed, or is one adjustable? *[Priority 2]*
5. Are multiple scopes bundled together, and if so can they be sequenced? *[Priority 2]*
6. Which domain, user group, or journey must go first? *[Priority 2]*
7. Are we optimising Phase 1 for one working use case or for a broader reusable engine? *[Priority 3]*

**Evidence to request:** prioritised scope list, roadmap or investment narrative, sales narrative or investor deck if visibility matters, milestone or deadline commitments already made.

---

## Category B, Market narrative and visibility requirements

1. What must the client be able to say or show after Phase 1 that they cannot credibly say or show today? *[Priority 1]*
2. What must be visibly demonstrable in the first release even if not fully mature? *[Priority 1]*
3. What reaction is the client trying to trigger after Phase 1: adoption, confidence, differentiation, investor validation, internal buy-in? *[Priority 2]*
4. Which capabilities are central to how the client wants to reposition in market? *[Priority 2]*
5. Must Phase 1 support demos and pre-sales, or only live operational use? *[Priority 3]*
6. Is a configurable engine required in Phase 1, or are constrained templates acceptable? *[Priority 3]*

**Evidence to request:** sales deck, proposition messaging, target buyer demos, screenshots or examples of expected visible capability.

---

## Category C, Platform, infrastructure, and governance

1. Are we deploying into existing cloud accounts or standing up new ones? *[Priority 1]*
2. Are there enterprise controls, SCP restrictions, CAB processes, platform teams, or security approvals involved? *[Priority 1]*
3. Who owns admin access and environment provisioning? *[Priority 2]*
4. Is CI/CD tooling mandated or undecided? *[Priority 2]*
5. Is new tooling adoption subject to security review, including AI tooling? *[Priority 3]*

**Evidence to request:** target architecture diagrams, platform constraints, security review checklist, environment access process, preferred toolchain policy.

---

## Category D, Data, integrations, and legacy certainty

1. Can sample payloads or data files be provided before delivery starts? *[Priority 1]*
2. Do legacy systems have documented APIs? *[Priority 1]*
3. Do legacy systems have documented schemas? *[Priority 1]*
4. Can we get read access for analysis? *[Priority 2]*
5. How many providers, feeds, or vendors are in scope for Phase 1? *[Priority 2]*
6. Are reference datasets, rules, mappings, taxonomies, or pricing matrices available in structured form? *[Priority 2]*
7. Does historical data exist and is migration expected? *[Priority 3]*

**Evidence to request:** sample data, API docs, schema extracts, integration inventory, mapping or reference files.

---

## Category E, Workflow ownership and configurability

1. Who will create and maintain workflows in the target model: internal teams, customers, or both? *[Priority 1]*
2. What is the smallest configurability capability that would still feel differentiated? *[Priority 1]*
3. Should users start from blank workflows, editable templates, or packaged journeys? *[Priority 2]*
4. Are there 2 or 3 canonical templates or journeys already known for the first release? *[Priority 2]*

**Evidence to request:** workflow examples, existing process maps, screenshots or prototypes, template examples.

---

## Category F, Stakeholders, decisions, and delivery maturity

1. Who makes scope and priority decisions during delivery? *[Priority 1]*
2. Will a product owner or domain expert be available throughout the engagement? *[Priority 1]*
3. Are key NFRs agreed or still open? *[Priority 2]*
4. Has a pilot customer, first user group, or first live consumer been identified? *[Priority 2]*
5. Are there blackout periods that materially affect decision speed? *[Priority 3]*

**Evidence to request:** stakeholder map, delivery governance model, decision owner list, NFR baseline.

---

## Category G, Team model and AI-native ways of working

1. Are AI-native practices and tooling permitted in the client environment? *[Priority 1]*
2. Is the client expecting AI to accelerate engineering only, or the whole lifecycle? *[Priority 1]*
3. Is there a budget or headcount envelope implied by the client? *[Priority 2]*
4. What delivery interaction model is expected: remote, hybrid, co-located? *[Priority 2]*
5. How important are maintainability, handover, and post-launch evolvability? *[Priority 2]*
6. How important is supplier maturity in AI-native delivery? *[Priority 3]*

**Evidence to request:** AI policy, supplier selection criteria, ways-of-working expectations, post-launch operating model.

---

## Category H, Migration and coexistence

1. Does the new system need to feed legacy systems during transition? *[Priority 1]*
2. How many downstream consumers need compatible outputs during coexistence? *[Priority 2]*
3. Will real end users operate the new system in Phase 1, or is it technical foundation first? *[Priority 2]*

**Evidence to request:** downstream consumer inventory, current-state architecture, migration constraints.

---

## Category I, Commercial, procurement, and competitive context

1. Is this likely fixed price, T&M, or capped T&M? *[Priority 1]*
2. Is this a competitive pitch? If so, who are we competing against? *[Priority 1]*
3. Are we designing to a budget envelope or estimating bottom-up? *[Priority 1]*
4. What does the client value most in differentiation: speed of delivery, price, methodology, team quality, sector experience, or something else? *[Priority 2]*
5. Does procurement require a fully-scoped commitment before any initial engagement? *[Priority 2]*
6. Who can approve a narrower shaping or proving phase if that is the best recommendation? *[Priority 2]*
7. Is there an incumbent supplier? If so, what is the client's reason for considering alternatives? *[Priority 3]*

**Evidence to request:** procurement constraints, budget guidance, framework or buying route, competitive context, evaluation criteria if available.

---

## Category J, AI-native delivery readiness

Use this category whenever the engagement is being pitched, sold, or estimated as AI-native, or where AI-native calibration ranges from Gate 5 are being applied. Questions are grouped against the six capability classes from `agentic-tooling-baseline.md`.

### Class 1, Quality-gate pipeline

1. Can you show a recent commit on the target repo with its CI run, so we can see what is enforced pre-commit and in CI? *[Priority 1, Critical]*
2. Are typing, linting, formatting, tests, and build all pre-commit enforced and re-checked in CI? *[Priority 1, Critical]*
3. Is trunk-based development in operation, or is the team on long-lived feature branches? *[Priority 2, Important]*

### Class 2, Analyzer suite

4. Does the team currently run a deterministic-plus-LLM analyzer suite (architecture, code-quality, security, performance, root cause), or is repo analysis bespoke each time? *[Priority 2, Important]*
5. Has the engagement repo had a recent baseline assessment run on it? If yes, can we see the artefacts? *[Priority 3, Useful]*

### Class 3, Execution-plan tooling

6. Does task decomposition happen via tooling (execution-plan generation, similar) before coding starts, or does the agent decompose on the fly? *[Priority 2, Important]*

### Class 4, KB chain

7. Is there established tooling for spec generation: lean canvas, BDD-style PRDs with stable requirement IDs, spec-impact analysis, code-drift detection? *[Priority 2, Important]*

### Class 5 and 6, Codification, context capture, and health

8. Are codification patterns in use (git-history mining, PR review codification, session codification)? *[Priority 3, Useful]*
9. Is cross-platform agent context retrieval and environment health-check tooling in place? *[Priority 3, Useful]*

### Coverage and scope

10. Which AI coding agents are in scope for this engagement: Claude Code, Codex, Cursor, Copilot, Gemini, others? Single agent or multiple? *[Priority 1, Critical]*
11. Which target languages are in scope? *[Priority 2, Important]*
12. Does the client have policies on AI-generated code: IP ownership, security review, approval to merge, audit requirements? *[Priority 2, Important]*

### Environment and commercial

13. Will the team have access to install CLI tools, agent extensions, and required SDKs in their dev environment? *[Priority 3, Useful]*
14. Is there a token-usage and AI-cost tracking expectation, or is this a free-form spend? *[Priority 3, Useful]*

**Evidence to request:** existing repo with `.github/workflows` or equivalent CI config, pre-commit configuration files, recent analyzer artefacts or baseline assessment, AI-generated code policy or working agreement, list of approved AI tooling, language and agent inventory.

---

## Category K, Platform and deployment

Use this category whenever cloud, IaC, deployment, or secrets handling is materially in scope and not already understood.

1. What cloud provider or providers are in use, and is IaC (Terraform, Pulumi, Bicep, CDK) already established? *[Priority 1, Critical]*
2. Is there an existing container registry and deployment pipeline we can target, or does one need to be built? *[Priority 2, Important]*
3. Are secrets managed centrally (Key Vault, Secret Manager, AWS Secrets Manager, Vault) or ad hoc? *[Priority 3, Useful]*
4. Is there a defined non-prod to prod promotion model, or is this part of the engagement? *[Priority 3, Useful]*

**Evidence to request:** IaC repo and module inventory, sample pipeline configuration, secrets management policy, environment promotion documentation.
