# New Hampshire — New Hampshire Lottery Commission (NHLC) / Gaming Regulatory Oversight Authority (GROA)

**Code:** NH · **Products:** sportsbook (online + limited retail) · **Key authority:** RSA 287-I (Sports Betting, esp. 287-I:1, 287-I:7, 287-I:8); NH Lottery Commission administrative rules (Lot chapters); operator agreement between NHLC and its sole selected mobile agent (DraftKings)

## Payments-relevant requirements

### Licensing & change management

- RSA 287-I structures NH as a **state-lottery monopoly model**, not a multi-operator license regime: the commission may contract with "agents" to conduct sports books, with a statutory ceiling of **no more than 5 mobile sports wagering agents** and **no more than 10 retail locations** in operation at any time (RSA 287-I:7) — but the commission ran a single RFP in 2019 and selected **DraftKings as the sole mobile/online agent**, so in practice all payments logic is built against one contracted operator's platform, not a competitive multi-license market like CO/MD/NJ (MEDIUM-HIGH — statute ceiling confirmed; sole-operator fact widely reported but not itself a numbered RSA cite).
- RSA 287-I:8 (Sports Wagering Supervision) requires each agent to submit a **responsible gaming plan** for NHLC review/approval before conducting any wagering and **annually thereafter** — the closest analog to CO/MD's platform-certification and change-management cadence, but framed around RG program renewal rather than lab-certified software releases (MEDIUM — no independent-testing-lab certification requirement was located in RSA 287-I itself, unlike CO Rule 7.6/MD COMAR 36.10.18.03; verify whether NHLC rules or the DraftKings contract impose one).
- No dedicated "Sw" (Sports Wagering) admin-rule chapter was found — the "Sw 3000" NHLC rule chapter that surfaces in search results governs **Powerball**, not sports betting; sports-betting-specific administrative rules appear thinner than CO's 1 CCR 207-2 or MD's COMAR 36.10, with much of the operational detail likely living in the non-public NHLC–DraftKings operator agreement (LOW-MEDIUM — could not locate a public NH sports-wagering-specific rule chapter; flag for compliance/legal to confirm via the operator contract).

### Deposits & permitted payment methods

- RSA 287-I does not appear to statutorily enumerate permitted funding instruments for online/mobile wagering accounts (no CO-style Rule 7.6(5)-(6) list, no MD-style COMAR 36.10.18.05(H) list located) — payment-method rules are set at the operator level (LOW — this is an apparent gap versus other states' regs rather than a confirmed absence; verify with NHLC/legal that no such rule exists).
- In practice, the sole operator (DraftKings) supports credit/debit cards, PayPal, online banking/ACH, and wire transfer for NH accounts, plus in-person cash deposits at a small set of retail cage locations (The Brook–Seabrook, Revo Casino & Social House–Dover/Manchester, Gate City Casino–Nashua) (LOW — sourced from consumer/affiliate sites, not a primary regulatory or NHLC document; do not treat as a compliance floor, only as current operational behavior to compare against).
- Unlike Colorado's 2026 credit-card ban (SB 26-131) or Maryland's cash-advance-acknowledgment rule (COMAR 36.10.13.28), **no NH-specific statutory restriction on credit-card funding or deposit frequency was found** (LOW-MEDIUM — absence of evidence, not evidence of absence; re-check each NHLC rulemaking cycle and the 2027 legislative session).

### Withdrawals & payout timelines

- **No statutory payout/withdrawal SLA was located in RSA 287-I** — no CO-style 24-hour "bona fide demand" rule, no MD-style 7-day rule (LOW — this looks like a genuine regulatory gap relative to CO/MD rather than a search miss, but flag for verification against NHLC rules and the DraftKings operator agreement, which may impose an SLA contractually even without a public rule).
- Operator-reported withdrawal speeds (PayPal ~3-5 days, ACH/e-check ~3-5 days, wire ~24-48 hours, cage cash up to ~$100k within an hour) are DraftKings' own published consumer terms, not a regulatory requirement, and may not be NH-specific (LOW).

### Player funds segregation / reserve

- RSA 287-I:8-adjacent accounting-control provisions require agents' internal controls to include, at minimum: (a) a process for documenting/verifying the beginning-of-day cash balance; (b) processes for recording collection of wagers, payment of wagers, and cancellation of wagers; (c) cash-handling processes at retail locations including segregation of duties for counting/storage of cash; and (d) **establishment of a segregated account related to NH sports wagering activity** (MEDIUM — content corroborated across independent search passes, but exact RSA subsection/lettering could not be independently confirmed via direct statute fetch; verify precise citation).
- Agents must maintain a **cash reserve available to pay wagers "as determined by the commission"** — i.e., no fixed statutory floor (contrast MD's $500,000-or-liability-whichever-is-greater rule); NHLC apparently sets/approves the reserve amount administratively rather than by a numeric rule (MEDIUM — same sourcing caveat as above).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- RSA 287-I:8 requires the annually-renewed responsible gaming plan to include: problem-gambling postings/materials; resources for bettors expressing concern; **house-imposed player limits** (daily/weekly/monthly wager amounts consistent with problem-gambling best practices); and a **voluntary self-exclusion program** allowing patrons to exclude themselves for set periods (HIGH — corroborated across multiple independent search passes).
- No explicit statutory cooling-off period or reverse-withdrawal rule was located (LOW — verify against the RG plan itself, which is agent-drafted and NHLC-approved rather than fully codified). In practice DraftKings' NH app exposes deposit/loss/wager limits, cooling-off timeouts, and self-exclusion consistent with its multi-state responsible-gaming toolkit (LOW — operator-level, not a distinct NH statutory requirement).
- New Hampshire Council on Problem Gambling (603-724-1605) and the national 1-800-522-4700 / NCPG line are the referenced support resources (MEDIUM).

### KYC / age / geolocation

- **Minimum age is 18, not 21 — this is a genuine, confirmed outlier versus most sports-betting states and is directly payments-relevant for age-gating logic.** RSA 287-I:1 defines "authorized sports bettor" as an individual **18 years of age or older** physically present in NH; a person under 18 is prohibited from creating a wagering account, wagering, or collecting winnings (HIGH — confirmed via the statute definition and cross-checked against 2025-2026 legislative history below).
- **2025-2026 change attempt, defeated — flag for awareness, no code change needed:** HB 83 (2025 session) would have raised the minimum age from 18 to 21, effective 1/1/2026, amending RSA 287-I:1, II. The House Ways & Means Committee voted 11-7 "inexpedient to legislate" (1/27/2025); the full House rejected the bill 215-140 (2/6/2025); the bill was indefinitely postponed. **NH's sports-wagering age remains 18 as of August 2026.** (HIGH — corroborated by SBC Americas, Yogonet, and RG.org's August 2025 NH revenue report explicitly noting "18+ Betting Age." Some secondary/affiliate sources incorrectly state the age changed to 21 effective 1/1/2026 by confusing the *bill's proposed* effective date with actual enactment — treat any source claiming NH is now 21+ as stale/wrong unless it cites a 2026-session bill that actually passed.)
- Age/identity verification must block wagers by under-18 persons, via secure online database checks or photo-ID examination (MEDIUM — corroborated across search passes but exact RSA subsection not independently re-verified via primary fetch).
- Mobile wagers must be initiated and received within NH's geographic borders and may not be intentionally routed outside the state; the commission/agents may not accept wagers from persons physically outside NH at the time of the wager (RSA 287-I:7-adjacent) (MEDIUM-HIGH).

### AML overlays (state-specific, beyond federal BSA)

- No NH-specific AML statute (CTR/SAR-style reporting, benefits-card blocking, etc.) beyond the general internal-control/segregated-account/cash-handling provisions above was located in RSA 287-I (LOW-MEDIUM — could be a real gap or an artifact of the state-lottery structure).
- **Notable, payments-relevant nuance to flag for compliance/legal:** industry commentary indicates mobile sports betting conducted through **state lotteries** (as opposed to licensed casino operators) may fall outside the BSA's "financial institution" definition that triggers CTR/SAR obligations for casinos with >$1M gross gaming revenue — several states plus DC are cited as examples of this treatment. Whether NH's lottery-run model is among them, and what that means for BSA-driven controls layered on top of NH transactions in a multi-state ledger, should be confirmed with legal/compliance rather than assumed (LOW — general industry-commentary sourcing, not NH-specific primary confirmation).

### Records, reporting & data

- Internal-control records (beginning-of-day cash balances, wager collection/payment/cancellation logs, segregated-account records) must be maintained per the RSA 287-I:8-adjacent accounting-control provisions (MEDIUM, same citation caveat as the segregation section above).
- The responsible gaming plan is filed with and approved by NHLC annually (HIGH, per RSA 287-I:8).
- Tier II/III wager data-source must be publicly disclosed (RSA 287-I:11-adjacent); no explicit record-retention period (e.g., CO's 3-year rule) was located for NH (LOW — verify).

## Code review focus

- **Age gate must enforce 18+, not 21+, for NH** — if age-gating logic is centralized/shared across states, confirm NH is not accidentally inheriting a 21+ default; this is the single highest-value NH-specific check given how easily "sports betting = 21" is hard-coded elsewhere.
- Re-verify the age gate against the 2027 legislative session before assuming this is permanently settled — HB 83-style bills have been introduced before and could resurface.
- Because NH runs a single contracted mobile agent, confirm whether payment-method allow-lists, deposit limits, and payout timing in the codebase are driven by an NH-specific config or are silently inheriting defaults from another state's ruleset — the statute itself is thin on payment-method and payout-SLA specifics, so a shared/default codepath is more likely to be "correct by accident" here than to reflect an actual NH requirement.
- No statutory withdrawal SLA was found for NH — do not assume CO's 24h or MD's 7-day rule applies; if a payout-timeliness check is shared code, ensure NH either has its own (possibly contract-derived, non-public) SLA wired in or is explicitly exempted rather than silently inheriting another state's number.
- Segregated-account and commission-set cash-reserve requirements (no fixed statutory dollar floor) — confirm any reserve/liability calculation feed treats NH's reserve as "commission-approved amount" rather than hard-coding a dollar floor borrowed from another state.
- Self-exclusion and house-imposed wager-limit hooks from the RG plan should map to deposit/wager authorization checks, per RSA 287-I:8.
- Geolocation gate on wager placement for patrons physically located in NH; block if routed/attempted from outside the state.
- Flag AML/CTR-SAR logic that assumes casino-style BSA "financial institution" status applies uniformly across all states — verify whether NH's lottery-run structure changes that assumption before applying a blanket BSA control set to NH transactions.

## Sources & confidence

- **Research note:** Direct WebFetch access to the primary statute pages (gc.nh.gov RSA 287-I chapter/section pages, law.justia.com NH statute pages) returned HTTP 403 for every attempt in this research pass. Findings below rely on WebSearch's synthesized snippets of those same primary pages (cross-checked across multiple independent query angles) plus secondary/affiliate reporting for operational (non-regulatory) detail. Anything not independently re-confirmable via a direct primary-source fetch is marked MEDIUM or LOW below — **compliance/legal should re-pull the primary RSA 287-I text directly (e.g., via a non-blocked mirror or gc.nh.gov in a standard browser) before relying on exact subsection numbers.**
- [RSA Chapter 287-I — Sports Betting NH General Court, merged text](https://gc.nh.gov/rsa/html/XXIV/287-I/287-I-mrg.htm)
- [RSA 287-I:1 — Definitions](https://gc.nh.gov/rsa/html/XXIV/287-I/287-I-1.htm) · [Justia mirror, 2025 statutes](https://law.justia.com/codes/new-hampshire/title-xxiv/chapter-287-i/section-287-i-1/)
- [RSA 287-I:7 — Mobile Sports Wagering Authorized Justia, 2025 statutes](https://law.justia.com/codes/new-hampshire/title-xxiv/chapter-287-i/section-287-i-7/)
- [RSA 287-I:8 — Sports Wagering Supervision NH General Court](https://gc.nh.gov/rsa/html/XXIV/287-I/287-I-8.htm)
- [NH Lottery Commission rules index, Lot 3000 NH General Court](https://gc.nh.gov/rules/state_agencies/lot3000.html) · [NH Lottery Commission Rules & Regulations hub](https://www.compliance.lottery.nh.gov/rules-regulations)
- [HB 83 2025 bill text — proposed age 18→21 LegiScan](https://legiscan.com/NH/text/HB83/id/3037287)
- [New Hampshire Won't Raise Sports Betting Age Limit From 18 SBC Americas, 1/27/2025](https://sbcamericas.com/2025/01/27/new-hampshire-wont-raise-betting-age/)
- [New Hampshire lawmakers reject proposal to raise sports betting age from 18 to 21 Yogonet, 1/30/2025](https://www.yogonet.com/international/news/2025/01/30/93536-new-hampshire-lawmakers-reject-proposal-to-raise-sports-betting-age-from-18-to-21)
- [New Hampshire Sports Betting Revenue – August 2025: 18+ Betting Age confirmed in market commentary RG.org](https://rg.org/news/gambling-industry/new-hampshire-august-2025-sports-betting-revenue)
- [NH Sports Betting Delivers Record-Breaking $39 Million to Education, FY2025 NH Lottery](https://www.nhlottery.com/news/NH-Sports-Betting-Delivers-Record-Breaking-39-Million-to-Education-in-Fiscal-Year-2025)
- Confidence: HIGH on the 18+ age rule and its 2025 legislative history (multiple independent primary/secondary confirmations); MEDIUM on RG plan content, geolocation, age/ID verification mechanics, and the internal-control/segregated-account/reserve language (consistent across search passes but exact RSA subsection numbering not independently re-verified via primary fetch); LOW on payment-method specifics, withdrawal SLA (likely a genuine gap vs. CO/MD), AML/BSA treatment of the lottery model, and record-retention period — **all LOW items should be re-verified directly against RSA 287-I and the NHLC–DraftKings operator agreement before being treated as compliance findings.**
