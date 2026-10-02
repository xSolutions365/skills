# FMX / CFTC-regulated exchange — fund segregation & settlement

**Lane:** FMX · **Authority:** Commodity Exchange Act; CFTC regs 17 CFR (esp. §1.20-§1.30 segregation); NFA rules · **Researched:** Aug 2026

The operator operates (or is acquiring) a CFTC-regulated event/prediction exchange (FMX). Under CFTC segregation rules, an **FCM (Futures Commission Merchant)** must segregate customer futures funds. This is **federal financial-market** law, orthogonal to gaming.

## Key requirements

- **Customer-fund segregation (CEA §4d; 17 CFR 1.20-1.30):** FCM customer funds for futures MUST sit in a segregated account, never commingled with the operator's or with non-futures (gaming) balances. Full ledger separation of balances AND transaction histories per product.
- **No cross-use:** funds deposited/traded on the exchange cannot be used on the operator and vice versa, regardless of playthrough; interim controls may fully restrict a user from one side in some jurisdictions.
- **Settlement & fee rules:** cancelled/tie outcomes have prescribed payout math (e.g. VWAP for cancels; a fixed per-contract amount for ties) and fee refund/no-refund rules — must match the exchange's published settlement rules.
- **Customer-facing wording** on inter-wallet movement; back-office guardrails for CFTC-exposed cash.
- **NFA** reporting/recordkeeping, capital, disclosure.

## Code review focus

- **Ledger separation:** are exchange vs operator balances + histories fully separated (distinct wallets/products), with no code path moving funds between them? Grep `FMX`, `fmx`, `exchange`, `segregat`, `walletSeparation`, `productType`. If the wallet already carries product/fund-type metadata, confirm the exchange is a hard boundary, not a shared balance.
- **Settlement math** for cancels/ties + fee refund rules, if implemented here.
- **Cross-wallet movement** controls + mandated wording.

## Test coverage focus

- **Unit** tests asserting no code path lets exchange funds settle to the operator (or vice versa) — a hard-boundary invariant.
- Settlement-math unit tests for cancel (VWAP) / tie (fixed per-contract, no fee refund) edge cases.
- Note most FCM/NFA obligations are entity-level (legal/finance), not code — flag ownership.

## Sources & confidence

- CEA §4d; CFTC 17 CFR Part 1 (segregation), Part 22 (cleared swaps); NFA rules; the operator's internal fund-segregation design docs.
- Confidence: HIGH that segregation is mandatory; MEDIUM on how much settlement logic lives in these repos vs the exchange platform — confirm scope. Pull latest — CFTC's treatment of event/prediction contracts is actively evolving (2025-26 rulemakings/litigation).
