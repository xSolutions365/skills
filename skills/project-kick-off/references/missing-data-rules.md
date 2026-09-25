# Missing Data Rules

## Objective

Never invent a fact. Label every gap, turn each gap into a question for someone who can answer it, and decide whether the gaps are too large to share the client pack.

## Required actions

1. Label gaps using these three labels only:
   - `TO CONFIRM`: a specific fact is unknown or only inferred. Add the question to ask and who can answer it: `pitch lead`, `account lead`, `casting`, or `client`.
   - `LOW CONTEXT`: a whole section rests on an input category that is missing or partial. Put it next to the section heading, followed by the missing input, e.g. `LOW CONTEXT: no early client calls`.
   - `DEFAULT`: a value taken from the engagement shape guide rather than the inputs.
2. Keep `TO CONFIRM` on every inferred value, for example a date counted back from week one, until someone confirms it.
3. Rate each input category as `present`, `partial`, or `missing`, and add `LOW CONTEXT` to every section that category feeds:
   - signed SoW or proposal: feeds deliverables, plan, RACI, and playback
   - casting with allocation, start dates, and leave: feeds plan and ownership
   - pitch and internal calls: feed the story, expectations, and growth map
   - client scope or discovery calls: feed expectations, drift, and stakeholders
   - client materials and data: feed baselines, prerequisites, and glossary
   - engagement playbook or method: feeds plan detail and week-one design
4. When someone's start date, allocation, or leave is unknown:
   - mark each unknown `TO CONFIRM` for `casting`
   - write `Lead: TO CONFIRM (candidate: <name>)` instead of naming a firm lead
   - report the unknowns in the availability check (V6); unknowns never count as a pass
5. When pitch or scope calls are `missing`, add up to 12 discovery questions to `internal/pitch-lead-questions.md`, about a 15-minute conversation. Cover how the work was won, what each stakeholder expects, what was promised outside the SoW, the known risks, and adjacent opportunities.
6. Turn every gap into an ask:
   - a `TO CONFIRM` the client can answer becomes a prerequisite row, a kick-off question, or both
   - a `TO CONFIRM` someone at CreateFuture can answer goes into `internal/pitch-lead-questions.md`, grouped by who answers
7. Check these critical facts:
   - the scope and deliverables as signed
   - the client sponsor
   - objectives and success measures
   - the week-one start date
   - the client decision-maker for week one
   - the final audience
   - the research participant route, when the engagement includes research
8. Give exactly one readiness verdict:
   - `READY`: no critical fact is `TO CONFIRM`.
   - `READY WITH GAPS`: critical facts are `TO CONFIRM`, but only the client can answer them, and each one is already in the prerequisites or the kick-off questions.
   - `HOLD`: a critical fact that someone at CreateFuture could answer is still `TO CONFIRM`, and it would change what the client pack commits to. Name the questions that clear the hold.

## Done when

- No name, date, figure, or commitment appears unless it is sourced or labelled.
- Every input category has a coverage rating, and every affected section carries `LOW CONTEXT`.
- Every `TO CONFIRM` appears either in the client asks or in the pitch-lead questions.
- The evidence ledger records exactly one readiness verdict.
