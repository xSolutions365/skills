# EFTA / Regulation E — electronic fund transfer consumer protections

**Lane:** EFTA · **Authority:** Electronic Fund Transfer Act (15 USC 1693) + Reg E (12 CFR 1005) · **Researched:** Aug 2026

Applies to consumer electronic fund transfers — ACH/e-check deposits (Trustly), debit-card, and arguably the stored-value wallet. Financial-services consumer law, distinct from gaming rules. Whether the *operator* is the "financial institution" for a given transfer is a legal call (often the processor/bank is) — but error-resolution, disclosure, and authorization obligations flow through the product.

## Key requirements

- **Error resolution (1005.11):** on a consumer notice of an error/unauthorized EFT, investigate within 10 business days (or provide **provisional credit** and take up to 45 days); report results; recredit if unauthorized. Notice window is 60 days from statement.
- **Unauthorized transfer liability caps (1005.6):** consumer liability limited ($50 / $500 tiers by reporting timeliness). The dispute/recredit path must honor these.
- **Authorization for recurring/one-time debits (1005.10):** consumer authorization records for preauthorized EFTs; ability to stop payment.
- **Disclosures (1005.7):** terms, fees, error-resolution rights at enrollment; change-in-terms notice.
- **Receipts / periodic statements (1005.9):** transaction confirmation + periodic statement (overlaps the gaming per-state statement matrix but is a distinct federal basis).
- **Compulsory-use / preauthorized transfer limits:** cannot require preauthorized EFT as sole payment option in some contexts.

## Code review focus

- Is there any **consumer dispute / error-resolution** flow (unauthorized ACH deposit, wrong amount) with a provisional-credit timer and 10/45-day deadlines? Grep `dispute`, `unauthorized`, `provisionalCredit`, `errorResolution`, `chargeback` (Reg E ≠ card chargeback but adjacent). Likely upstream (support/ops) — confirm the boundary.
- ACH authorization records for Trustly deposits — is the authorization captured/stored and voidable where supported by the rail/provider (e.g., via a cancel API)?
- Stop-payment / cancel on preauthorized transfers.

## Test coverage focus

- Unit tests on any deadline/liability math (10-business-day, 45-day, $50/$500 caps) if that logic lives in code.
- Failure-mode: an unauthorized-EFT claim must recredit; a test asserting "refund only on original deposit" is not Reg-E coverage.
- If error-resolution is upstream, note that no test here can cover it — flag as ownership-map item.

## Sources & confidence

- [Reg E, 12 CFR 1005 eCFR](https://www.ecfr.gov/current/title-12/chapter-X/part-1005) · error resolution 1005.11 · liability 1005.6 · authorization 1005.10.
- Confidence: HIGH on the rule text; MEDIUM on operator-vs-processor "financial institution" applicability for gaming wallets — route to legal. Pull latest for any CFPB Reg E amendments and the 2024+ larger-participant / 1033 open-banking interplay.
