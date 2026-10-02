# Money transmission & stored-value / prepaid-access

**Lane:** MTL · **Authority:** State money-transmitter laws + Money Transmission Modernization Act (MTMA model); FinCEN 31 CFR 1010 (MSB / prepaid access) · **Researched:** Aug 2026

The unified player wallet holds customer funds = potential **stored value / money transmission**. Whether the operator needs MTLs or relies on a licensed processor/bank partner is a legal structuring question — but the code determines fund custody, transfer, and segregation behavior that the licensing rests on.

## Key requirements

- **Money-transmitter licensing:** holding/transmitting customer funds may require state MTLs (or reliance on a partner's). The MTMA is standardizing definitions/exemptions across states — "gaming" and "agent of payee" exemptions vary.
- **Permissible investments / safeguarding:** licensed transmitters must hold permissible investments ≥ outstanding obligations (overlaps reserve/segregation — state skill).
- **FinCEN prepaid access rule (31 CFR 1010.100(ff)(4)):** prepaid/stored-value programs can make the provider/seller an MSB with BSA obligations; thresholds ($1,000/day load/withdraw) and closed-loop exemptions matter.
- **No P2P transfer / no negative balance / adjustments logged:** stored-value integrity (Ontario mandates these explicitly; general prudential expectation).
- **Cross-border fund flows** (US↔Canada wallet) implicate transmission + reporting (see aml/sanctions lanes).

## Code review focus

- Wallet fund model: is value **stored** (balance persists) vs pass-through? Confirm **no player-to-player transfers** (grep `transfer`, `p2p`, account-to-account) and **no negative balance** (wallet enforces — verify). Both are MTL/stored-value integrity controls.
- **Closed-loop vs open-loop** funding (gift cards / promo) — segregation of stored-value balances (grep `giftCard`, `storedValue`, `closedLoop`, `segregat`).
- Adjustments to balances restricted to authorized roles + logged reasons (cf. NJ wash report).
- Cross-wallet (US/CA) movement controls.

## Test coverage focus

- **Unit** tests asserting no-P2P and no-negative-balance invariants (the wallet's `TransactionSaverValidator`-style guards — these ARE unit-testable and high value).
- Stored-value segregation (gift-card/promo funds distinct from cash) asserted.
- Note licensing itself isn't code-testable — it's an ownership/legal item; flag it.

## Sources & confidence

- State money-transmitter statutes + MTMA model law (CSBS); FinCEN 31 CFR 1010 prepaid-access rule; FinCEN administrative rulings on gaming.
- Confidence: MEDIUM overall — MTL applicability to gaming wallets is a live legal/structuring question (partner-licensed vs direct); route to legal. Code-level invariants (no-P2P, no-negative, segregation) are HIGH-confidence checkable. Pull latest for MTMA state adoptions.
