# Legislation lanes index

One requirements reference per payment/financial-services legislation lane. Each lane file
ends in a **Code review focus** and a **Test coverage focus** list, was researched Aug 2026,
and carries its own confidence + "pull latest" note. The default scope of a run is *every*
lane below; a run may also target a single lane (e.g. Nacha R01-vs-R10, Reg E disputes, OFAC
on payouts, AFT/OCT/MCC, W-2G, DFS/FMX).

## Lanes

- [EFTA / Regulation E](lanes/efta-reg-e.md) — electronic fund transfers, error resolution, disclosures
- [Nacha / ACH](lanes/nacha-ach.md) — ACH return codes, R01-vs-R10, risk-management rules
- [Tax withholding & offsets](lanes/tax-withholding-offsets.md) — W-2G, backup withholding on payouts
- [Card-network programs](lanes/card-network-programs.md) — AFT/OCT, MCC, gambling-transaction rules
- [Money transmitter & stored value](lanes/mtl-stored-value.md) — MTL, prepaid/stored-value obligations
- [Sanctions / OFAC](lanes/sanctions-ofac.md) — OFAC screening on deposits and payouts
- [AML / BSA depth](lanes/aml-bsa-depth.md) — BSA/FinCEN CTR and SAR, casino recordkeeping
- [Privacy & data rights](lanes/privacy-data-rights.md) — data-subject rights, retention, deletion
- [DFS fantasy fund types](lanes/dfs-fantasy.md) — daily-fantasy fund-type handling
- [FMX / CFTC exchange segregation](lanes/fmx-cftc-exchange.md) — CFTC segregation of customer funds
- [Chargeback disputes](lanes/chargeback-disputes.md) — dispute handling and representment
- [Prohibited-state geofencing](lanes/prohibited-state-geofencing.md) — money-movement geofencing

## Repos in scope

The payments bounded context spans multiple repos; a lane must look across all that are
present: the payments business-logic library, the customer-facing deposit/withdraw/refund API,
the processor API (webhooks + back-office + papercheck CSV), the wallet ledger
(system-of-record), and the integration-test (`fast`) repo. Some obligations are genuinely
owned upstream (accounts/KYC, RG service, finance for reserve, a tax/AML system) — mark those
`not_found` with an external-ownership note rather than fabricating a control.

## Legislation refresh (the re-run feature)

Payment law changes. On any run the bundled references can be refreshed before reviewing:

- With web access ON, each lane subagent spends a few searches confirming whether its key
  rules changed since the reference's "Researched" date, and records changes in
  `legislation_refreshed` plus its findings (citing the new rule, not blindly trusting either
  source).
- To durably update a lane, edit `lanes/<lane>.md` in place (bump its "Researched" date and
  sources) — that improves every future run.
- With web access OFF (fast/deterministic), lanes rely on the bundled references and carry
  their stated confidence.

## Adding a lane

Drop a new `lanes/<lane>.md` (copy an existing one's shape: Scope, Key requirements +
citations, Code review focus, Test coverage focus, Sources, Confidence) and add it to the list
above. It is picked up automatically next run. Good candidates as the product grows: Reg Z/TILA
(if credit is ever enabled), UDAAP, crypto-MSB/Travel-Rule depth, open-banking/CFPB-1033
(partially in nacha-ach), accessibility.
