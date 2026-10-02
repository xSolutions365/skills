# Delaware — Delaware State Lottery Office / Division of Gaming Enforcement (DSL/DGE)

**Code:** DE · **Products:** sportsbook, iGaming (online casino) · **Key authority:** 29 Del.C. Ch. 48 (§§4825, 4825A, 4826, 4826A — Lotteries); 10 Del. Admin. Code 206 (Internet Lottery Rules and Regulations, eff. 11/10/2014, **amendments proposed Dec. 2025**); 10 Del. Admin. Code 204 (Sports Lottery Rules and Regulations); 10 Del. Admin. Code 203 (Video Lottery and Table Game Regulations, cross-referenced by 206's pending self-exclusion amendment)

## Payments-relevant requirements

### Licensing & change management

- State-run lottery model, not a private-license market: the DSL Director licenses "agents" (Delaware's 3 video lottery facilities — Delaware Park, Bally's Dover, Harrington Raceway), technology providers, and service providers (206 §§4.0-6.0). A single statewide RFP ("Internet Wagering System and Services Solution," issued 1/12/2023) selected one vendor to run online casino **and** sports wagering for all three agents; that contract is expressly exempted from Title 29 Ch. 69 procurement rules. Rush Street Interactive (BetRivers) has held this contract since the Jan. 2024 relaunch and remains Delaware's only licensed online sportsbook/casino brand through 2026. (HIGH)
- Technology provider license term is 3 years and application fee is $4,000 under the current text; a **Dec. 2025 proposed amendment** to 206 §§5.13/5.15.1 would raise the fee to $5,000 and formalize the 3-year term (previously omitted). All Internet lottery system/equipment changes require Director pre-approval through the MICS change-control process (§§9.0, 11.0) — no assembly/operational change without prior notice, justification, and documentation to the agency.
- Delaware HB 365 (152nd General Assembly), which would have authorized the Lottery to license up to 5 mobile sportsbook operators (each paying a $500,000 annual fee, 15% GGR tax, NJ-style RG provisions), stalled and did not become law; Delaware remains a single-operator market as of Aug. 2026 (MEDIUM — confirm current-session status before relying on this for a multi-operator design).

### Deposits & permitted payment methods

- 206 §13.24 (iGaming/"Internet lottery" — ticket games, video lottery, table games): funds may be deposited **only** by (1) credit card, (2) bank transfer, or (3) other Director-approved means. **No credit-card deposit ban in Delaware** — this is the opposite posture from CO's 2026 SB 26-131 ban; §13.24 is not among the sections the Dec. 2025 proposed amendment touches, so this list appears stable through 2026. (HIGH)
- Separately, secondary sources describe a broader permitted-funding list for Internet **sports** lottery accounts — cash; credit/debit/prepaid/gift card; bank draft, money order, personal/traveler's/cashier's check; electronic bank/funds transfer; bonuses/promotions; digital/mobile payment systems; or other Director-approved means. This was not confirmed against the verbatim current text of 10 Del. Admin. Code 204 in this review (the fetched 204 excerpts covered only ticket/credit-slip redemption) — treat as MEDIUM and verify the exact section number before citing it as authority.
- No credit may be extended to players by an agent, and negative account balances are prohibited outright (§13.23.1-.2).

### Withdrawals & payout timelines

- 206 §13.25: withdrawals only by (1) bank transfer, (2) bank draft, or (3) other Director-approved means — there is no card-based payout rail, consistent with the no-credit-to-player rule.
- No numeric online-withdrawal payout SLA (e.g., "within N days") was located in 206 or in the 204 excerpts reviewed. The one payout timing rule found is for **retail** sports lottery paper tickets/credit slips: redeemable up to 1 year from the date of the last wagered event, after which unredeemed funds escheat to the State Lottery Fund (204 §7.x). Confidence LOW on whether an online SLA exists elsewhere (e.g., in the non-public MICS) — flag for verification with DSL/compliance rather than assuming no SLA applies.

### Player funds segregation / reserve

- Distinctive to Delaware's state-lottery model: **the agency (DSL) itself**, not the private operator or technology provider, "will maintain a separate bank account to hold funds deposited into registered player's accounts" (206 §16.3). Segregation is a state/agency-held function; net proceeds (net of amounts returned to players) are swept at least monthly into the licensed agents' designated accounts (§16.4).
- The definitions of "net internet table/video lottery game proceeds" (§2.0) explicitly carve out amounts held in reserve for large/progressive prizes not yet won, implying a reserve concept exists for progressive jackpots specifically, but no operator-side dollar-floor reserve requirement (of the kind seen in CO's Rule 6.9 or MD's $500k-plus-liability rule) was located in the primary law reviewed. LOW confidence that Delaware has no such requirement at all — verify against non-public MICS before treating this as settled, since Delaware's structure (state holds the money) may simply make an operator-side reserve calculation moot rather than absent.

### Responsible gambling

- Self-exclusion tiers: 1 year, 5 years, or lifetime (206 §13.14.2, current text). DSL maintains the single statewide self-exclusion list and must notify every licensed agent of additions/deletions; each agent must sync its own copy and notify staff within 48 hours (§§13.15-13.16).
- **Pending change, not yet confirmed final as of this review:** a Dec. 2025 proposed amendment package (public comment closed 12/31/2025) would harmonize online self-exclusion with 10 DE Admin. Code 203 §7.0 (the in-person Video Lottery/Table Game self-exclusion form), **drop the photo/physical-description requirement** for online self-exclusion (repealing old §§13.13-13.14 and 13.16.6-.7), and let players request **removal** from the list virtually instead of appearing in person (amended §13.21). If this shipped, it changes both the self-exclusion intake flow and the removal flow for the online product. Confirm the final register entry/adoption date before building against either the old or new flow. (MEDIUM)
- No explicit deposit-limit, spend-limit, or time-limit mandate for online play was located in 206 beyond the self-exclusion program itself; such RG controls, if required, likely live in the non-public MICS/internal-control submissions rather than in public regulation (LOW — verify).

### KYC / age / geolocation

- Real-money play requires 21+, full name, address, cellular phone number, email, DOB, and SSN (US residents) or other government ID (non-US residents); identity and age verification are mandatory before real-money registration completes (§§13.4-13.5). Free/social play needs only a DOB affirmation and self-verification — no automated ID check required (§§13.2-13.3).
- One active real-money account per player per agent; cross-agent and cross-player fund transfers are both prohibited (§13.8).
- Geolocation gates **play**, not deposits: real-money wagering is permitted only when the system reasonably determines the player is in Delaware or a compact jurisdiction, and access is blocked outright when location can't be determined (§13.22). Deposits, by contrast, are explicitly permitted "from any geographic location" once real-money registration is complete (§13.6) — geofencing and funding are not the same gate in this regulation.

### AML overlays

- §16.7 (echoing §3.1.7) requires agents and technology providers to keep records sufficient for federal BSA financial recordkeeping (citing 31 CFR 103, a since-renumbered cite — treat as a stale citation, not evidence of a DE-specific AML program). No Delaware-specific CTR/SAR regime beyond federal BSA was identified in the primary law reviewed (MEDIUM).

### Records, reporting & data

- All gaming records retained a minimum of 5 years (§15.6); internal-audit reports also retained a minimum of 5 years and made available to the Director on request (§17.1.1).
- Agents file weekly, monthly, quarterly, and annual financial/statistical reports to DSL, plus an independent-CPA-audited annual financial statement (§16.8).
- Inactive/abandoned player accounts: reported annually (by Nov. 10, as of the prior June 30) to the State Escheator and escheated under Title 12 Ch. 11 Subchapter II (§§13.26-13.27).
- Semi-annual vulnerability scans and annual penetration testing of the external website interface, with reports to the Director within one month of each (§17.2).
- Player data ownership sits with the agents, not the technology/service providers: agents retain full ownership of all customer data (including deposit/withdrawal and fraud data); technology providers are barred from selling or retaining customer data once their contract ends (§14.7).

## Code review focus

- Deposit method allow-list for DE must match §13.24 exactly (credit card, bank transfer, Director-approved) for the iGaming product. If the sportsbook product is coded against the broader secondary-source list (cash, prepaid/gift card, checks, digital wallets), confirm which list the live BetRivers/RSI unified platform actually implements for DE before assuming both products share one config — don't guess parity between the two product lines.
- Withdrawal rails restricted to bank transfer/bank draft/Director-approved — flag any code path that would let a DE payout settle back to a card.
- No-negative-balance / no-credit-to-player logic (§13.23.1-.2) must be enforced pre-authorization on every wager, not just at deposit time.
- Self-exclusion integration: confirm against DSL's single statewide list (agency-maintained, not operator-maintained), the 48-hour agent-sync SLA on additions/removals, and — pending confirmation of final adoption — whether the online removal flow still requires an in-person visit or has moved to virtual self-service per the Dec. 2025 proposal. A hard-coded "in-person only" removal flow may already be stale.
- One-account-per-agent and no-fund-transfer enforcement, both cross-agent and cross-player (§13.8).
- Geolocation gate should apply to wager placement, not to deposits — verify the code doesn't over-geofence deposit-only flows, since §13.6 explicitly allows funding from any location once real-money registration is complete.
- Escheatment sweep: confirm a scheduled Nov. 10 inactive-account report/payment job exists against the State Escheator rather than a manual process, and that "inactive" is keyed off the Title 29 §4826(c)(4) definition, not an internal proxy.
- Delaware's segregation model puts the player-funds bank account at the **agency** level (§16.3), not the operator. If the operator's compliance code models a CO/MD-style operator-side reserve calculation for DE, that's the wrong mental model here — check whether DE even needs an operator reserve computation, or whether the state-held-account structure makes that requirement inapplicable.

## Sources & confidence

- [10 DE Admin. Code 206 — Internet Lottery Rules and Regulations, eff. 11/10/2014 Delaware Lottery, PDF](https://delotterywebcontent.blob.core.windows.net/delottery-site-assets/assets/internet-lottery/InternetlotteryRules.pdf)
- [Proposed amendments to 10 DE Admin. Code 206 — Dec. 2025 Register of Regulations, comment period closed 12/31/2025](https://regulations.delaware.gov/api/register/december2025/1665aa19-badb-4a11-a469-4aaa77912676)
- [10 Del. Admin. Code § 204-7.0 — Sports Lottery Cornell LII](https://www.law.cornell.edu/regulations/delaware/10-Del-Admin-Code-SS-204-7.0) · [Delaware Regulations, Title 10 Ch. 204 hub](https://regulations.delaware.gov/AdminCode/title10/204)
- [29 Del. Code Ch. 48 — Lotteries Delaware Code Online](https://delcode.delaware.gov/title29/c048/sc01/)
- [Rush Street Interactive / Delaware Lottery online sportsbook + casino relaunch announcement, Jan. 2024](https://ir.rushstreetinteractive.com/news/news-details/2024/Delaware-Lottery-Launches-Online-Sports-Betting-With-The-Transition-To-BetRivers-Powering-The-States-New-Online-Casinos--Online-Sportsbooks/default.aspx)
- [Delaware HB 365 152nd General Assembly — stalled mobile-sports-expansion bill](https://legis.delaware.gov/BillDetail?LegislationId=21016)
- Confidence: HIGH on deposit/withdrawal method lists, self-exclusion tiers (current text), single-operator/state-run structure, records retention, and the play-vs-deposit geolocation distinction — all read directly from primary regulation text (10 DE Admin. Code 206) and corroborated news sources. MEDIUM on: the Dec. 2025 self-exclusion amendment's final-adoption status (public comment closed 12/31/2025; final register entry/effective date not confirmed as of this review — verify before building against the "virtual removal" flow); whether the broader sports-lottery deposit-method list is current verbatim 204 text versus a secondary-source paraphrase; and whether a DE-specific AML overlay exists beyond federal BSA. LOW on: any numeric online-withdrawal payout SLA (none located in public regulation — likely lives, if at all, in non-public MICS/internal controls); and whether an operator-side dollar-floor reserve requirement exists at all, given Delaware's unusual agency-held-funds structure (§16.3) versus the operator-reserve model used in NJ/PA/CO/MD. Web search and WebFetch were both available and used throughout this research.
