# state-compliance-gap-analysis

## Overview

Runs a jurisdiction-by-jurisdiction gaming compliance gap analysis of a payment gateway codebase
— all 50 US states + DC plus Ontario and Alberta, Canada — with one parallel subagent per
jurisdiction and a federal lane per country, then condenses everything into a RAG decision matrix
(.xlsx) and an executive summary. It classifies test coverage precisely (unit vs
integration/FAST), optionally attributes each gap to Create Future or client authorship via git
blame, and keeps the named attribution in a separate internal-only workbook. It is the per-state
gaming complement to the federal `payment-legislation-gap-analysis` skill.

## When to use it

- You want to analyse the operator codebase against state or provincial gaming regulations.
- You want to review jurisdictions in parallel, or build/refresh the compliance decision matrix.
- You want to check one jurisdiction, e.g. "check Michigan withdrawals" or "does this cover
  Ontario or Alberta".
- You want to know what a jurisdiction requires (AGCO/iGO, AGLC/AiGC, PCMLTFA/FINTRAC), or who
  wrote or last touched the code behind a gap.

## Example prompts

- "Run `state-compliance-gap-analysis` on this codebase for nj, pa, mi as a pilot."
- "Does the code cover Ontario and Alberta correctly, or is it reviewing Ontario against BSA?"
- "Refresh the gap-analysis matrix and split the new findings by Create Future vs client."

## References

- Main workflow: [SKILL.md](SKILL.md)
- Jurisdiction catalogue + federal baselines: [references/jurisdictions-index.md](references/jurisdictions-index.md)
- Review method: [references/review-checklist.md](references/review-checklist.md)
- Findings contract: [references/findings-schema.md](references/findings-schema.md)
- Fan-out orchestration: [references/orchestration.md](references/orchestration.md)
- Code-origin attribution: [references/attribution.md](references/attribution.md)
- Condense and deliver: [references/condense-and-deliver.md](references/condense-and-deliver.md)
