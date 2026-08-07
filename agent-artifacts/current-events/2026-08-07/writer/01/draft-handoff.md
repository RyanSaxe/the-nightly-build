# draft-handoff: current-events/2026-08-07 (writer 01)

## Original work
The article's one act of original work: it converts the day's marquee number,
Anthropic's $1.5 billion settlement, into a per-work price of about $3,000
across 440,490 claimed works, and names that figure the first court-approved
rate for books copied to train a model and a benchmark for the licensing fights
ahead. The owning sources report only a fund total, a claim rate, and a
per-work estimate; the reading that the per-work figure is the settlement's
lasting mark is the writer's, and it is visible in item 1's closing sentence and
the docket's "Stakes" row.

## Proof result
`./nb check ... --series current-events --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0 — PUBLISHABLE.** No warnings left standing.

Final slate (5 items, each: exactly 1 primary + >=1 secondary, per the series'
`per_item_sources`):
1. Anthropic $1.5B copyright settlement enters distribution / payouts (Copyright)
2. Immergut (D. Or.) preliminary injunction forcing DoD to resume wind-project
   reviews (Energy)
3. Judge Amy Berman Jackson vacates DOE's "Still Interested" FOIA policy
   (Transparency)
4. BLS Q2 2026 productivity: real hourly compensation -3.1% as productivity
   +1.4% (Economy)
5. ISM Services PMI July 2026: 54.1%, prices 70.3%, employment 47.4%
   contraction (Prices)

Furniture: one `rs-docket` (Bartz v. Anthropic) on the lead item; one
`nb-stat-strip` (ISM sub-indexes 59.1 / 47.4 / 70.3) on item 5. No charts or
assets (evidence located no renderable primary visual for the court orders; the
brief's numbers carry in prose and the stat strip).

## Evidence corrections honored
- Anthropic framed as the distribution / imminent-payout phase (final approval
  and judgment 2026-07-20; payouts est. ~08-10), NOT as the stale approval.
  Counts WORKS, not authors: 482,460 eligible / 440,490 claimed / ~$3,000 each.
  No author count printed.
- **July jobs figures: NOT printed.** Verified myself at draft time — the BLS
  Employment Situation URL still serves the June 2026 release (+57,000, 4.2%),
  so the actual July figures were unverifiable. Per the brief, omitted every
  July number and led the economic slots with the verified Q2 productivity
  (BLS, 08-06) and July ISM Services (08-05) releases instead.
- DC Circuit clean-energy-FUNDING ruling NOT run (reserved to the unbiased
  piece). The wind item is the district-court APA permitting-review injunction
  only. No tech-field items; one AI-adjacent legal item (the ceiling).

## Sourcing notes (worth an editor's eye)
- The series contract requires each item to carry its own primary + an
  independent account. The evidence record was short three of these, so I
  sourced them myself and verified each resolves and matches:
  - **Wind primary:** the CourtListener docket, *Renewable Northwest v.
    Hegseth*, No. 3:26-cv-01092 (D. Or.) — the docket order page the brief
    directed me to link. It returns HTTP 403 (gated), which the link proof
    treats as alive, not dead; the substantive findings are carried by NOTUS
    and the Washington Times.
  - **Productivity secondary:** Market Business News (2026-08-06) — matches the
    BLS figures and adds the labor-share-of-output record low (~53%, cited).
  - **ISM secondary:** Brisk Markets (2026-08-05) — matches 54.1 / 70.3 / 47.4
    and owns the June employment reading (51.2%) I use.
- Display-text pass done: every number/name/title/date in the title, dek, and
  item headlines checked against its owning primary. nb-meta `dek` and the
  rendered dekline are identical.

## Open questions
- None blocking. One judgment call for the editor: the wind item's primary is a
  gated docket (no readable order text was available to the researcher or to me
  at draft time); its factual claims rest on two independent newsrooms plus the
  docket record. If a readable order surfaces, the locator can be tightened.
- The dek says the settlement "starts writing checks"; the body is precise that
  the administrator *estimates* first payments around August 10. Framing follows
  the brief's instruction to treat the 08-07 hook as the payout phase beginning.
