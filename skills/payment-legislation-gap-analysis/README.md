# payment-legislation-gap-analysis

## Overview

Sweeps the operator payments codebase (payments library, deposit/withdraw/refund + webhook APIs,
wallet ledger) against US and Canada payment / financial-services legislation, one subagent per
legislation lane, and condenses the result into a RAG decision matrix and executive summary. For
every requirement it assesses both whether the code implements it correctly and whether the
correct behavior (and its failure mode) is actually tested — preferring unit-level assertions
over integration ones. It is the financial-services-law complement to the per-state gaming skill
`state-compliance-gap-analysis`.

## When to use it

- You need a payment-law / financial-services compliance review of the payments code.
- You want to re-run the legislation sweep or pull the latest payment legislation.
- You want to add a new legislation lane, or check just one area (Nacha R01-vs-R10, Reg E
  disputes, OFAC on payouts, AFT/OCT/MCC, W-2G, DFS/FMX).
- You need to know whether a money-movement control is present, and whether it is unit-tested.

## Example prompts

- "Use `payment-legislation-gap-analysis` to review the payments code against Reg E and Nacha."
- "Re-run the payment legislation sweep and lead with what changed since last time."
- "Add an OFAC-on-payouts lane and run just that one against the code."

## References

- Main workflow: [SKILL.md](SKILL.md)
- Lane catalogue: [references/lanes-index.md](references/lanes-index.md)
- Review method: [references/review-checklist.md](references/review-checklist.md)
- Findings contract: [references/findings-schema.md](references/findings-schema.md)
- Fan-out orchestration: [references/orchestration.md](references/orchestration.md)
- Condense and deliver: [references/condense-and-deliver.md](references/condense-and-deliver.md)
