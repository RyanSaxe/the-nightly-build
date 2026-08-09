# Draft handoff: current-events/2026-08-09 (writer 01)

## Original work

The one act of original work: this brief selects and orders the day's four
federal-power stories so a single question carries the edition — who gets to
decide — leading on the Senate handing the Justice Department to the president's
own former criminal-defense lawyer by one vote, and giving the ballroom ruling a
docket that states the Property Clause question the event coverage files under
"construction halted." It is visible in the lead choice, the item order, and the
`rs-docket` on the ballroom item.

## Proof

`./nb check ... --series current-events --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

No warning left standing. The three density warnings that surfaced during
iteration were all fixed by splitting: the ballroom lede, the birthright EO
sentence (quote preserved verbatim), and the jobs revision sentence (the
per-month figures now live only in the table, which is where that
before/after shape belongs).

## Items run (4, within the 4-6 band; 8 sources, floor 5)

1. Blanche confirmation (lead) — primary Senate roll call + secondary NPR.
2. D.C. Circuit ballroom ruling — primary panel opinion + secondary NPR; `rs-docket`.
3. July jobs print (body item, not lead, per brief) — primary BLS + secondary NBC; `nb-table` of the May/June revisions.
4. Birthright-citizenship executive order — primary White House + secondary NPR.

Caveats honored: BLS post-revision figures govern the payroll numbers (May
+63,000, June +20,000, combined −103,000), not NBC's transcription; no hard page
count printed for the D.C. Circuit opinion; the "People's House" / "temporary
tenant" / "Executive self-help" language is attributed to the opinion, not to the
newsroom that reports it; the 90,000-sq-ft / 1,000-seat figures are attributed to
the administration. Dek is one lean sentence naming the actor, with no
comma-and-"and" triad and no "same day, also" second clause.

## Open evidence / voice questions

- **VA union-contract order dropped for want of an openable primary.** The brief
  named a VA caveat (attribute the "employees covered" figure to the AFGE
  filing), which signaled the item was expected, and the researcher listed it
  among the four strongest. But the evidence record opens no resolvable primary
  for it: the D.R.I. order (Judge DuBose, 7 Aug) is named as the primary in the
  record's prose, yet only Government Executive (secondary) and Federal News
  Network (secondary/background) were actually opened. The proof enforces exactly
  one primary per item (`B-SOURCE-KIND`), so the item cannot ship at BLOCK: 0
  without a resolvable order URL. Precise researcher request to add VA in a
  revision: supply a resolvable locator for the D.R.I. order in
  *AFGE v. VA* (D.R.I., order dated 7 Aug 2026) — a CourtListener/RECAP docket
  entry or a court media URL — and confirm the "over 300,000 employees covered"
  figure against the order or attribute it to the AFGE filing.

- **D.C. Circuit primary URL substituted within the record's own options.** The
  evidence listed the opinion's primary URL as `media.cadc.uscourts.gov` with the
  docket "via" CourtListener `docket/72028010`. The CourtListener URL returns 404
  to the proof's link check (it is gated, but the checker sees a hard 404 and
  blocks). `media.cadc.uscourts.gov` resolves 200, so the source entry and the
  item headline link now point there. This is the record's stated primary host,
  not a new source; flagging only because it differs from the docket URL the
  record foregrounded.
