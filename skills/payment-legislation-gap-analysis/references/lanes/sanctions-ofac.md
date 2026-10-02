# Sanctions screening — OFAC (US) + FINTRAC/SEMA (Canada)

**Lane:** SANCTIONS · **Authority:** OFAC (31 CFR 500s; IEEPA); Canada SEMA/UN Act + FINTRAC (PCMLTFA) · **Researched:** Aug 2026

Sanctions screening on the money path is a commonly missing control. Strict-liability regime — a single blocked-party transaction is a violation regardless of intent.

## Key requirements

- **Customer + counterparty screening (OFAC SDN + consolidated lists):** screen at onboarding AND on deposit/withdrawal counterparties (bank/card/payee). Block and hold, don't reject-and-return, on a true match.
- **Ongoing rescreening:** re-screen against list updates (SDN changes frequently), not just at signup.
- **Blocked-property reporting:** report blocked/rejected transactions to OFAC within 10 business days; annual report.
- **PEP + adverse-media** (risk-based, part of CDD/EDD — overlaps AML lane).
- **Geographic sanctions:** embargoed jurisdictions (overlaps prohibited-state/geo, but country-level).
- **Canada:** SEMA/UN sanctions lists + FINTRAC (LCTR/EFT reporting, STRs) for the Ontario/CAD flows; include large-cash and large-EFT reporting where applicable (verify current thresholds and product applicability).

## Code review focus

- Is there ANY sanctions/OFAC screening on deposit or withdrawal? Grep `ofac`, `sanction`, `sdn`, `blocked`, `screen`, `watchlist`, `pep`, `fintrac`, `sema`. Likely upstream (KYC/onboarding) — confirm whether **payout-counterparty** screening happens on the payments path specifically.
- **Block-and-hold vs reject** semantics on a match (must hold blocked funds, not just decline).
- **Cross-border (US↔CA) fund-flow reporting** hooks — capturing originating/receiving institution country/branch (a FINTRAC EFT-reporting requirement for the Canada/Ontario flows).
- Rescreening trigger on list updates.

## Test coverage focus

- **Unit** tests asserting a matched party is **blocked-and-held** (not returned) on deposit and payout — the failure mode matters.
- Cross-border >$10K flow flagged for EFT/LCTR reporting (boundary test at $10,000).
- If screening is entirely upstream, one finding + ownership item; verify the **payout counterparty** angle isn't missed by an onboarding-only control.

## Sources & confidence

- OFAC regulations & FAQs (Treasury); 50%-rule; reporting 31 CFR 501.603/604. Canada: SEMA, Special Economic Measures regs, PCMLTFA/FINTRAC guidance.
- Confidence: HIGH on OFAC obligations; MEDIUM on where the operator performs payout-counterparty screening (onboarding vs payments) — verify. Pull latest for new sanctions programs and FINTRAC 2026 reporting changes.
