# Step 3 Workflow: Apply natural-language review and revision

## Objective

Use judgment-based review questions to decide whether the prose is ready, then revise until the answer is a real pass.

## Required actions

1. Run a binary gate in this order and stop at the first failure:
   - `G1` Context binding: the draft fails the subject-swap test and every major claim is traceable to supplied material.
   - `G2` Length and verbosity discipline: the draft fits the preset's word range or compression target, and no paragraph survives the deletion test as obvious padding.
   - `G3` Structural authenticity: the opening gets to the point, the layout matches the preset's scan pattern, and no repetitive paragraph or sentence-opening pattern dominates the piece.
   - `G4` Preset fidelity: the tone, sentence length, paragraph plan, and ending are visibly those of the selected preset rather than an adjacent one.
   - `G5` Redraft integrity: for redraft runs only, meaning, scope, evidence limits, and commitment level stay intact.
2. Record one line of evidence for each gate you evaluate.
3. Ask these questions while evaluating the gates:
   - Does the first paragraph earn the reader's attention or waste it?
   - If I delete any paragraph, does the argument materially weaken?
   - Are banned terms, hollow framing phrases, or mechanical transition crutches present?
   - Does the structure visibly match the preset's intended length and scan pattern?
   - Are paragraph openings, sentence openings, or paragraph lengths becoming repetitive?
   - Has stronger prose come at the cost of factual precision or honest uncertainty?
4. If any gate fails, revise against the failed gate first, then rerun the full gate sequence.
5. Escalate to a stricter second pass when the audience is executive, procurement-aware, sensitive, or high-consequence.
6. Repeat revision until the draft can pass the full gate without caveat.

## Done when

- The draft passes the gate sequence without hedging.
- Redraft integrity is preserved when source text was supplied.
- The prose is stronger in clarity, flow, and specificity than the previous pass.
