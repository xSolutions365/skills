# Card-network gambling programs & transaction integrity (Visa/Mastercard)

**Lane:** CARDNET · **Authority:** Visa Core Rules + Visa Global Gambling Merchant program; Mastercard Rules + gambling registration · **Researched:** Aug 2026

Private card-network rulebooks, contractually binding on the acquirer/merchant. Distinct from PCI-DSS (data security) and from state credit-card bans (state skill). Governs how gaming card transactions are coded, registered, and processed.

## Key requirements

- **Gambling merchant registration:** Visa Global Gambling Merchant registration / Mastercard gambling registration required; unregistered gambling volume is a violation.
- **MCC accuracy:** correct **MCC 7995** (betting/lottery) and, for licensed US online gambling/sports, **7801/7802/7803**; accurate merchant descriptors. Mis-coding (e.g. as retail) is a serious violation and also breaks issuer blocking.
- **Quasi-cash / cash-advance treatment:** gambling deposits treated as quasi-cash — cash-advance rules/disclosures.
- **AFT (Account Funding Transactions):** Mastercard/Visa AFT for funding a wallet — correct AFT MCC/message-format so issuers can apply gambling controls.
- **OCT (Original Credit Transactions):** payouts to card ("push to card") use OCT — with limits, MCC, and fast-funds rules.
- **3-D Secure / SCA:** where required (esp. EU/UK and increasingly issuers), 3DS on card deposits; AVS on card deposits (note that some jurisdictions/programs may require stricter AVS handling — verify with compliance).
- **Chargeback/dispute program limits** (see chargeback-disputes lane).

## Code review focus

- Where is **MCC** set/sent on card auth? Grep `MCC`, `7995`, `7801`, `merchantCategory`, `descriptor`. Is it correct per product (sportsbook vs casino vs DFS) and per gateway (Fiserv/Paysafe)?
- **AFT vs OCT** — are funding transactions flagged as AFT and payouts as OCT? Grep `AFT`, `OCT`, `accountFunding`, `originalCredit`, `pushToCard`.
- **AVS / 3DS** — is the AVS response captured and used (not just logged)? Grep `avs`, `AddressVerification`, `3ds`, `threeDSecure`, `cavv`. (Some jurisdictions require full AVS — verify per state.)
- **Quasi-cash / cash-advance disclosure** on card deposits.

## Test coverage focus

- **Unit** tests asserting the correct MCC per product/gateway, and AFT-on-funding / OCT-on-payout flagging (pure mapping logic).
- AVS-failure handling asserted (deposit blocked or name-verified on AVS mismatch) — not just AVS captured.
- Note if card tests are happy-path auth only, never exercising MCC/AFT/AVS branches.

## Sources & confidence

- Visa Core Rules & Product/Service Rules (gambling merchant reg, MCC 7801/7802/7995); Mastercard Rules (gambling registration, AFT/OCT). Rulebooks are semi-public PDFs.
- Confidence: HIGH on MCC/AFT/OCT existence; MEDIUM on current program names/thresholds and 3DS mandate scope for US gaming — pull latest (networks update rules ~twice/year; SCA/3DS expansion ongoing).
