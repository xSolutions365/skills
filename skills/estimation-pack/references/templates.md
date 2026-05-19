# Output Templates, A through H (V3)

---

## Template A, Estimate readiness summary

```
# Estimate Readiness Summary

**Opportunity:**  
**Date:**  
**Prepared by:**  
**Gate owner:**  

## Readiness level
- Level 0 / Level 1 / Level 2 / Level 3

## Mode
- Standard / Compressed

## Why
- 
- 
- 

## Major red flags

### Scope risk flags
- 
- 

### Delivery risk flags
- 
- 

## AI-native readiness signals (if relevant)
- Agentic tooling experience: Yes / Partial / No
- Quality gates in target repo: Established / Partial / Absent
- Execution-plan and spec tooling expected: Yes / No

## Best next move
- 
```

---

## Template B, Tailored client question pack

```
# Targeted Client Questions

## Critical

**Question:**  
**Category and priority:** e.g. D1, J1, K1  
**Why this matters:**  
**What we will assume if unanswered:**  
**Evidence requested:**  

## Important

**Question:**  
**Category and priority:** e.g. C3, J3  
**Why this matters:**  
**What we will assume if unanswered:**  
**Evidence requested:**  

## Useful

**Question:**  
**Category and priority:** e.g. G6, K3  
**Why this matters:**  
**What we will assume if unanswered:**  
**Evidence requested:**  
```

---

## Template C, Internal estimation summary

```
# Internal Estimation Summary

## 1. Recommended delivery approach

## 2. Why alternatives were not selected

## 3. Project summary

## 4. Phase and milestone plan
(Include Phase 0 / Sprint 0 mobilisation if AI-native delivery is in scope and any agentic readiness items are missing. See Template H.)

## 5. Deliberate Phase 1 exclusions

| Excluded capability | Why excluded | When it could be introduced | Risk if pulled into Phase 1 |
|---|---|---|---|
|  |  |  |  |

## 6. Team shape and resource plan

## 7. Pricing-sheet inputs

## 8. AI-native vs traditional comparator

## 9. Tooling maturity adjustments applied
(Optimistic ranges, mobilisation block added, ramp sprint recommended, etc. See Gate 5 Tooling Maturity Modifier.)

## 10. Assumptions and decisions needed

## 11. Confidence by area

## 12. Decision log
```

---

## Template D, Confidence table

```
| Area | Confidence | Why |
|---|---|---|
| Phase 1 boundary |  |  |
| Delivery approach |  |  |
| Infrastructure estimate |  |  |
| Data / integration estimate |  |  |
| Frontend / UX estimate |  |  |
| Team shape |  |  |
| Timeline |  |  |
| AI-native uplift |  |  |
| AI tooling and workflow maturity |  |  |
| Commercial framing |  |  |
```

---

## Template E, Decision log

```
| Decision | Chosen answer | Why | Impact if wrong |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
```

---

## Template F, Calibration transfer table

```
| Dimension | Similarity to reference | Impact on estimate | Adjustment decision |
|---|---|---|---|
| Cloud / infra environment | High / Medium / Low | High / Medium / Low | Keep, reduce, or increase infra multiplier |
| Backend delivery pattern | High / Medium / Low | High / Medium / Low | Keep or reduce AI backend adjustment |
| Frontend complexity | High / Medium / Low | High / Medium / Low | Add selective uplift if needed |
| Data / integration certainty | High / Medium / Low | High / Medium / Low | Add archaeology or dependency risk if weaker |
| Governance / decision drag | High / Medium / Low | High / Medium / Low | Increase human bottleneck risk where needed |
| Team continuity similarity | High / Medium / Low | Medium / Low | Apply continuity guidance selectively |
| Agentic tooling maturity | High / Medium / Low | High / Medium / Low | Apply optimistic ranges, add mobilisation, or recommend ramp sprint |
| Quality-gate establishment | High / Medium / Low | High / Medium / Low | Apply optimistic backend ranges or add 3 to 5 day mobilisation |
```

---

## Template G, Delivery handover brief

```
# Delivery Handover Brief

**Opportunity:**  
**Date:**  
**Handed over by:**  
**Handed over to:**  

## 1. What was sold and why
Summary of the committed scope, the commercial model, and the client's primary success criteria.

## 2. Key assumptions the delivery lead must understand

| Assumption | Client confirmed? | Impact if wrong |
|---|---|---|
|  |  |  |
|  |  |  |

## 3. Decisions that were commercially driven

| Decision | Commercial rationale | Technical implication |
|---|---|---|
|  |  |  |
|  |  |  |

## 4. Known risks not communicated to the client

| Risk | Why not communicated | Recommended mitigation |
|---|---|---|
|  |  |  |
|  |  |  |

## 5. Deliberate Phase 1 exclusions
(Copy from estimation summary)

## 6. Open questions still awaiting client answers
(Copy any unanswered questions from the question pack)

## 7. Calibration assumptions used
Summary of which calibration ranges were applied and any adjustments made during estimation, including the tooling maturity modifier where relevant.

## 8. Agentic delivery position at handover
- Items from Template H already in place
- Items still outstanding and where they sit in the plan
- Confidence that AI-native uplift is achievable in delivery
```

---

## Template H, Agentic delivery mobilisation checklist

Include as a Phase 0 or Sprint 0 in the plan whenever the engagement is being delivered AI-natively. The estimate must either show these as already in place (with evidence) or include the time and effort to establish them. The structure follows the six capability classes from `agentic-tooling-baseline.md`.

```
# Agentic Delivery Mobilisation Checklist

**Engagement:**  
**Status as of:**  
**Owner:**  

## Class 1, Quality-gate pipeline (mandatory)
- [ ] Pre-commit hooks: typing (Mypy strict / TypeScript strict / equivalent)
- [ ] Pre-commit hooks: linting and formatting (Ruff / ESLint+Prettier / gofmt / equivalent)
- [ ] Pre-commit hooks: tests with minimum coverage gate
- [ ] Pre-commit hooks: build verification
- [ ] Pre-commit hooks: secrets and security scan (detect-secrets, semgrep)
- [ ] Trunk-based development pattern in operation
- [ ] CI re-checks all of the above on every push

## Class 2, Analyzer suite
- [ ] Architecture analyzer configured and runnable on engagement repo
- [ ] Code-quality analyzer (Ruff / Lizard / jscpd / equivalent) configured
- [ ] Security analyzer (Semgrep / detect-secrets / equivalent) configured
- [ ] Performance analyzer configured
- [ ] Root-cause analyzer configured
- [ ] Recent baseline assessment artefacts available or scheduled

## Class 3, Execution-plan tooling
- [ ] Task decomposition tooling configured (execution-plan generation)
- [ ] Execution plans created for first-milestone tasks
- [ ] Acceptance criteria explicit per task

## Class 4, KB chain (spec and PRD generation)
- [ ] Knowledge-base repository configured for spec generation
- [ ] Lean canvas tooling available
- [ ] PRD creator tooling available (BDD-style, stable requirement IDs)
- [ ] Spec impact analysis available
- [ ] KB code-drift detection available

## Class 5, Codification (confidence input, not mandatory)
- [ ] Git-history mining or pattern codification
- [ ] PR review codification
- [ ] Session codification

## Class 6, Context capture and health
- [ ] Cross-platform agent context retrieval configured
- [ ] Environment health-check tooling in place
- [ ] Per-platform context capture tested

## Cross-cutting
- [ ] Approved AI tooling list confirmed with client (per agent if more than one)
- [ ] Dev environments allow required CLI / extension installs
- [ ] AI-generated code policy understood (IP, security review, approval flow)
- [ ] Token usage and AI cost tracking configured
- [ ] Cost ceiling and review cadence agreed
- [ ] Reporting line for AI tooling spend confirmed

## Coverage and scope
- [ ] All target languages have class 1 and 2 configuration
- [ ] All in-scope coding agents have adapter setup if multiple

## Confidence note
Any unticked item must be reflected in the confidence table for "AI tooling and workflow maturity" and "AI-native uplift". Class 1 unticked invalidates AI-native calibration entirely until established.
```
