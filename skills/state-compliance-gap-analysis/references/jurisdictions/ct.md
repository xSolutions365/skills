# Connecticut — Dept. of Consumer Protection, Gaming Division (DCP)

**Code:** CT · **Products:** sportsbook (the operator operates online sports wagering under the CT Lottery master-wagering-license structure; online casino limited to the two tribal operators) · **Key authority:** CGS Ch. 229a §§ 12-850 to 12-871 (PA 21-23); Conn. Agencies Regs. §§ 12-865-1 to 12-865-33

## Payments-relevant requirements

### Licensing & change management

- Online gaming/wagering platform components and games require independent-lab testing and DCP approval before offering, incl. technical documentation and software validation/authentication methods (Regs. 12-865-15 framework; sportsbook platform approvals analogous — confidence MEDIUM on exact section for sportsbook).
- Soft-launch testing of platforms required before public offering; quarterly information-system audits and cybersecurity insurance required (Regs. 12-865-3(z), (h)).

### Deposits & permitted payment methods

- Permitted funding: ONE credit card OR one debit card held in the patron's name at a time (patron may swap cards by deleting the active card), plus electronic/ACH transfers, wire, certified/travelers checks, winnings, complimentaries (Regs. 12-865-11(f)(2)). Credit cards allowed but single-card-on-file constraint is distinctive.
- One account per platform per patron (Regs. 12-865-3(a)).

### Withdrawals & payout timelines

- Withdrawals payable via cash-out back to the funding card or direct transfer to the patron's individual bank account, or documented operator adjustment (Regs. 12-865-11(g)). No fixed day-count timeline stated in 12-865-11 — verify SLA in DCP-approved internal controls.

### Player funds segregation / reserve

- Operator must maintain a reserve sufficient to secure funds held on behalf of patrons; acceptable form includes cash/cash equivalents in a U.S. bank account segregated from operational funds (Regs. 12-865-11(k), (k)(1)).
- Reserve must cover patron balances including pending withdrawals, pending wagers, funds transferred to a game not yet wagered, and pending wins (Regs. 12-865-11(l)(2)-(3)).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Easy and obvious patron self-limitation tools required: deposit caps, individual and cumulative wager maximums, time-based limits; limits effective immediately (or at patron-specified time) and may only be loosened after 24 hours' notice (Regs. 12-865-11(t), (t)(3)).
- **Lifetime-deposit acknowledgment: Regs. Conn. State Agencies §12-865-13(u)** — when a patron's **lifetime deposits exceed $2,500**, block wagering until the patron acknowledges (1) meeting the $2,500 lifetime gaming-deposit threshold, (2) the ability to set RG limits or close the account, and (3) a problem-gambling message; items (2)-(3) must be **reconfirmed every 6 months** after the threshold is met. (HIGH — validated.)
- Account balance and session-time display required (12-865-11(t)); DCP runs a statewide voluntary self-exclusion program (enrollment via DCP online portal; 1-year/5-year/lifetime tiers) — description-level, confidence MEDIUM on tier details.
- No explicit reverse-withdrawal provision found in 12-865-11.

### KYC / age / geolocation

- Identity verified per Regs. 12-865-12 approved remote authentication before play; minimum legal age verified (21 for sports wagering) (Regs. 12-865-11(c)(3), (c)(5)).
- Accounts must be suspended when location data indicates likely unauthorized access or use of proxies/VPNs/spoofing to disguise identity or location (Regs. 12-865-3(q)).

### AML overlays (state-specific, beyond federal BSA)

- Suspicious activity must be reported to DCP within 24 hours via the licensed compliance manager (Regs. 12-865-3(c)) — a state reporting overlay on top of federal SAR timelines.

### Records, reporting & data

- Quarterly information-system audits; DCP access to platform records; consumer disclosures per Regs. 12-865-30. Retention specifics not confirmed — verify.

## Code review focus

- Enforce single active card-on-file: linking a second credit/debit card must require deletion of the first; card name must match account holder.
- **Lifetime-deposit-ack gate ($2,500, semiannual re-confirm):** block wagering until acknowledged; re-prompt the RG-limit/close + PG items every 6 months (§12-865-13(u)).
- Withdrawal routing restricted to the original funding card or a bank account in the patron's own name (closed-loop enforcement).
- Reserve calculation includes pending withdrawals and funds-in-flight to games — wallet states must be enumerable for the 12-865-11(l) computation.
- Limit engine: decreases take effect immediately; increases/removals gated behind a 24-hour delay.
- VPN/proxy/spoofing detection wired to automatic account suspension, not just wager blocking.
- 24-hour SAR-to-DCP escalation hook from payments fraud/AML monitoring.

## Sources & confidence

- [Regs. Conn. State Agencies § 12-865-11 LII](https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-12-865-11)
- [§ 12-865-11 Justia](https://regulations.justia.com/states/connecticut/title-12/subtitle-865/section-12-865-11/) · [§ 12-865-3 Justia](https://regulations.justia.com/states/connecticut/title-12/subtitle-865/section-12-865-3/) · [§ 12-865-15 Justia](https://regulations.justia.com/states/connecticut/title-12/subtitle-865/section-12-865-15/) · [§ 12-865-13 lifetime-deposit ack LII](https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-12-865-13)
- Confidence: HIGH on single-card funding, reserve/segregation, self-limit mechanics, VPN suspension, 24h suspicious-activity reporting; MEDIUM/LOW on withdrawal SLAs, self-exclusion tiers, retention periods — verify with DCP-approved internal controls. **Lifetime-deposit-ack $2,500/semiannual HIGH (§12-865-13(u), validated).**
