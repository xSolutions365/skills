# Step 4 Workflow: Draft the reference docs

## Objective

Generate focused `docs/references/*.md` files only where deeper detail is justified.

## Required actions

1. Create a separate reference file only when the README would become overloaded without it.
2. Pick the matching template based on the topic archetype:
   - `../assets/templates/reference-catalog-template.md`
   - `../assets/templates/reference-comparison-template.md`
   - `../assets/templates/reference-lexicon-template.md`
   - `../assets/templates/reference-walkthrough-template.md`
   - `../assets/templates/reference-workflow-template.md`
3. Keep one topic per file and one clear reader question per document.
4. Use tables, examples, and sub-sections only when they materially improve comprehension for that topic.
5. Keep commands, config fragments, and paths evidence-backed and scoped to the doc's single purpose.
6. Avoid duplicating the README. A deeper doc should add detail, nuance, examples, or operational steps the README intentionally omits.
7. Prefer a small set of high-value reference docs over a sprawling documentation tree.

## Done when

- Each deeper doc has one clear purpose.
- Each deeper doc is justified by the evidence inventory and Step 2 split.
- The combined doc set adds depth without sacrificing onboarding flow.
