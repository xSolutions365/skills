# Tax withholding, information reporting & debt offsets on payouts

**Lane:** TAX · **Authority:** IRC §3402(q), §6041/6050, §3406; state tax + debt-intercept statutes · **Researched:** Aug 2026

Applies to the **withdrawal/payout** path. Tax/debt-offset handling is often owned by a dedicated tax system, but the payout flow must still trigger/hold funds correctly and integrate with any upstream withholding/offset decisions.

## Key requirements

- **W-2G reporting (§6041, gambling):** report winnings at thresholds (e.g. $600 and 300×, $1,200 slots/bingo, $1,500 keno, $5,000 poker; sports/pari-mutuel per rules) — collect TIN.
- **Regular gambling withholding (§3402(q)):** 24% federal withholding on certain proceeds over $5,000 (type-dependent).
- **Backup withholding (§3406):** 24% when TIN missing/invalid (B-notice) — a withholding trigger on payout.
- **1099-K (§6050W):** third-party network payout reporting thresholds (the $600 threshold saga — confirm current year's phase-in).
- **State income-tax withholding** on winnings (varies) and **state debt / child-support intercept**: several states require intercepting withdrawable winnings for owed child support or state debt before payout (lien/offset check at withdrawal).
- **TIN collection & validation (W-9 / TIN matching)** as a gating input.

## Code review focus

- On the withdrawal path, is there any **withholding calculation or hold** (24% federal, state)? Grep `w2g`, `withholding`, `backupWithholding`, `1099`, `tin`, `taxHold`, `offset`, `childSupport`, `lien`, `intercept`. Likely upstream tax system — confirm boundary.
- **Debt/child-support intercept**: any pre-payout check that can divert/hold funds? If absent and states require it, that's a gap (or an ownership item).
- TIN presence gating a payout (backup-withholding trigger).

## Test coverage focus

- **Unit** tests on any withholding/threshold math (boundary at $5,000, 24% rate, per-type W-2G thresholds) if computed in code.
- If tax is entirely upstream, one finding stating so + an ownership-map recommendation; don't fabricate controls here.

## Sources & confidence

- IRC §3402(q), §3406, §6041/§6050W; IRS Pub 3079 (tax-exempt gaming) / instructions for W-2G. State child-support intercept + debt-offset statutes vary widely.
- Confidence: HIGH on federal thresholds/rates (verify current-year 1099-K phase-in and any sports-betting-specific W-2G guidance); LOW on which states the operator must honor debt intercept — route to tax/legal. Pull latest for annual threshold changes.
