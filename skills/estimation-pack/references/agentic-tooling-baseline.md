# Agentic Tooling Baseline

This reference captures what counts as "established AI-native delivery tooling" for the purposes of Gate 1 readiness, Gate 5 calibration, and Template H mobilisation. It uses the **Enaible** framework (`xSolutions365/enaible`) as the canonical reference implementation, but the capability classes are framework-agnostic. A team using a different toolchain that covers the same capability classes should be treated equivalently.

Use this file when you need to decide whether a team can be credibly calibrated against optimistic AI-native ranges, or whether mobilisation effort needs to be added to the estimate.

---

## The six capability classes

A team that has all six in regular use can be calibrated against optimistic AI-native ranges with confidence. A team missing classes 1, 2, or 3 cannot be credibly calibrated as AI-native without mobilisation effort.

### 1. Quality-gate pipeline (foundational, mandatory)

The deterministic guardrails that make AI-generated code safe to accept at speed.

| Capability | Reference tool | What "established" looks like |
|---|---|---|
| Linting and formatting | Ruff (Python), ESLint + Prettier (TS/JS), gofmt (Go), rustfmt (Rust) | Pre-commit hook enforces; CI re-checks |
| Strict type checking | Mypy strict, TypeScript strict mode, equivalents | Pre-commit hook enforces |
| Complexity limits | Lizard, jscpd duplication detection | CI gate or pre-commit |
| Test runner with coverage | pytest, vitest, go test, equivalents | CI gate; minimum coverage enforced |
| Secrets and security scan | detect-secrets, semgrep | Pre-commit and CI |
| Build verification | Native build per language | Pre-commit enforces; CI re-runs |

If any of typing, linting, formatting, or build is not pre-commit enforced, treat the quality-gate pipeline as **absent** and apply the 3 to 5 day mobilisation block from Gate 5.

### 2. Analyzer suite (assessment and triage)

Deterministic plus LLM hybrid analyzers that turn a codebase into evidence-grade findings. Distinct from feature-delivery work.

| Domain | Reference tools | Estimation use |
|---|---|---|
| Architecture | Component identification, complexity, coupling analysis | Repo-wide baseline assessment, modernisation triage |
| Code quality | Ruff, Lizard, jscpd, Prettier | Maintainability and tech debt assessment |
| Security | Semgrep, detect-secrets, injection and concurrency pattern detection | Pre-engagement security baseline |
| Performance | Bottleneck and hot-path detection | Pre-optimisation triage |
| Root cause | Execution flow, error patterns, recent-change correlation | Incident and regression triage |

When this class is established, repo-wide baseline assessments can be calibrated tightly (see Gate 5 calibration table). When it is absent, baseline work resembles bespoke analysis and should be priced accordingly.

### 3. Execution-plan tooling (task decomposition)

The capability that turns a vague feature request into agent-executable tasks before coding starts. Reference: `create-execplan`.

When established, tasks arrive at the agent pre-decomposed with explicit acceptance criteria, which justifies the 5 to 10% reduction in discovery overhang. When absent, the agent is decomposing on the fly, which produces lower-quality output and reabsorbs the overhang.

### 4. KB chain (spec and PRD generation)

The chain that turns repository evidence into structured product artefacts: lean canvas, PRDs with stable requirement IDs, spec impact analysis, code-drift detection, external KB reconciliation.

| Skill | Output |
|---|---|
| `kb-repository-setup` | KB contract and routing map |
| `kb-lean-canvas` | Lean canvas drafted from repo evidence |
| `kb-prd-creator` | BDD-style PRD with stable requirement IDs |
| `kb-spec-impact-analysis` | Spec change traced to impacted code surfaces |
| `kb-code-drift` | KB drift detection vs. code |
| `kb-external-kb-consolidation` | External KB reconciled into local docs |

When established, the optimistic 0.3x to 0.5x calibration on spec and documentation work is credible. When absent, spec work reverts to traditional cycles regardless of AI tooling elsewhere.

### 5. Codification (institutional learning)

Skills that capture and codify recurring patterns from git history, PR reviews, and AI-assisted sessions. Reference skills: `codify-git-history`, `codify-pr-reviews`, `codify-session-history`, plus the `analyze-git-history-opportunities` prompt.

This class is not a hard requirement for any specific calibration adjustment, but its presence is a strong signal that the team is genuinely operating AI-natively rather than performing AI-native theatre. Use as a confidence input on the "AI tooling and workflow maturity" line.

### 6. Context capture and health (observability)

The ability to retrieve recent agent context (`context_capture` across platforms) and verify environment health (`enaible doctor` or equivalent). When established, debugging cross-session continuity and tool-availability issues is fast. When absent, expect 0.5 to 1 day per sprint lost to environment troubleshooting.

---

## Multi-system and multi-language considerations

### Multiple coding agents in scope

Enaible supports nine coding-agent systems: Codex, Claude Code, Copilot IDE, Copilot CLI, Cursor, Gemini, Antigravity, Pi, OpenCode. If the client environment mandates more than one agent (common in enterprise where security has approved one and engineering uses another), each requires its own adapter setup and prompt rendering.

Estimation impact: add 0.5 to 1 person-day per additional agent for adapter setup and validation if a Jinja2-style render pipeline is in place. Add 2 to 4 person-days per additional agent if not.

### Multiple target languages in scope

Enaible supports six target languages: Python, TypeScript, Go, Rust, Java, C#. The quality-gate pipeline (class 1) and analyzer suite (class 2) need language-specific configuration per target language.

Estimation impact: if the project spans more than one target language, multiply the mobilisation block from Gate 5 by 1.3 to 1.6 to cover per-language gate setup, unless the team can evidence pre-existing configuration.

---

## What "established" means in practice

For a capability class to count as established:

1. **Evidenced.** Point to a working repo, configuration file, CI run, or recent artefact. "We use it sometimes" does not count.
2. **In the engagement repo.** A capability that exists in some other repo at the client does not transfer automatically. If the engagement is in a new repo, the mobilisation block applies even if the tooling is well-known internally.
3. **Owned.** Someone on the engagement team can run it, modify it, and debug it. A capability nobody on the engagement team owns is at best a research input.

---

## What to do when a class is absent

| Class | If absent | Recommended response |
|---|---|---|
| 1, Quality gates | AI-native calibration is invalid | Add 3 to 5 day mobilisation block before optimistic ranges apply |
| 2, Analyzer suite | Cannot price repo-wide baseline tightly | Either add 2 to 5 days to set up an analyzer baseline or recommend a separate architectural review engagement |
| 3, Execution-plan tooling | Discovery overhang stays at default | Do not apply the 5 to 10% reduction; grade AI-native uplift confidence Medium at best |
| 4, KB chain | Spec and doc calibration reverts to traditional | Apply 1.0x on spec work, not 0.3x to 0.5x |
| 5, Codification | No estimate impact | Note as a confidence input only |
| 6, Context and health | Friction overhead in delivery | Add 0.5 to 1 day per sprint contingency, or budget mobilisation to install equivalents |

---

## How to test this in a client conversation

Three questions in escalating depth, only the first is genuinely critical:

1. *"Can you show me a recent commit on the target repo with its CI run?"* If the run shows pre-commit hooks, type checking, linting, formatting, tests, and build all enforced, class 1 is established.
2. *"Walk me through how a feature gets from idea to a merged PR in your team."* Listen for spec generation tooling (class 4), execution-plan generation (class 3), and the analyzer suite running on the PR (class 2).
3. *"How does a new engineer onboard onto this codebase?"* Listen for context capture, primer prompts, and analyzer-driven onboarding (classes 2 and 6).

Treat the answers as evidence for the relevant Gate 5 modifier rows and for the AI tooling maturity confidence line.
