# Editorial review: current-events/2026-08-07 (editor/01)

## Skeptic

A brief has no single thesis; its argument is the selection, and each item is a
small claim about what a development changes. I took the five item headlines and
deks as claims and tested each against its owning primary, opening every printed
`href`.

Item 1 (Anthropic settlement). Claims: $1.5B fund; 482,460 works eligible,
440,490 (about 91%) claimed; ~$3,000 per work; final approval and judgment by
Judge Araceli Martínez-Olguín on 2026-07-20; case Bartz v. Anthropic, N.D. Cal.,
No. 3:24-cv-5417; first payments estimated around August 10; largest US copyright
class action. The Authors Guild final-approval post (s2) confirms the judge,
date, court, $1.5B, and ~$3,000. The Authors Guild claim update (s3) confirms
440,490 of 482,460 (91.3%) and the $2,931.62 base that rounds to $3,000. The
docket number 3:24-cv-5417 in the rs-docket matches the administrator's own
rendering, so it is not an error. All hold.

The one break is the payout timing, and it is load-bearing because the whole
lead item and the dek stand on it. The lead's "the administrator estimates the
first payments will go out around August 10" and the item headline "days from
its first payments" both cite s1, the settlement site's `/dates` page. I opened
`/dates`: it lists only the passed procedural dates (opt-out, objection,
re-inclusion, claim deadline, the May 14 fairness hearing) and the generic
"payments will only be made if the Court approves the Settlement and any appeals
are resolved." It carries no August date. The ~August 10 estimate is real and
reachable — it lives on the settlement FAQ and is corroborated by outside
coverage — but the printed citation lands on a page that does not support the
claim tagged to it. A reader clicking [1] to check "August 10" finds nothing
about August 10. This routes to the writer.

The dek compounds it. "The largest copyright case in U.S. history starts writing
checks" asserts that payments are being issued now; the body is careful that the
administrator only *estimates* first payments around August 10, contingent on the
judgment becoming effective and appeals resolving. As of the paper's own date,
2026-08-07, no check has been written. Display text is the costliest place to
overstate. This routes to the writer alongside the citation.

Item 2 (wind injunction). Claims: 125+ utility-scale wind projects across 25
states frozen; Judge Karin Immergut (Trump appointee, D. Or.); preliminary
injunction ordering DoD to resume reviews with 30-day status reports; missed
review deadlines; APA violation; plaintiff coalition; "Doppler interference"
defense. The primary (CourtListener docket, s5) and the Washington Times (s7)
both return HTTP 403 — the gated state the brief anticipated, which the link
proof treats as alive; the docket slug matches the case caption. NOTUS (s6) is a
readable, independent account carrying every fact in the item, so the per-item
gate (primary + independent account) is met on NOTUS even with the two gated
sources. I pressed the one phrase that looked like it might outrun its source:
"the deadlines Congress set for the reviews," where NOTUS says only "regulatory
deadlines." Courthouse News's fuller account resolves it — the review deadline is
statutory (the law gives DoD 75 days for the preliminary review), so "Congress
set" is accurate for the review deadline the injunction turns on. It holds.

Item 3 (DOE FOIA). Claims: Judge Amy Berman Jackson vacated DOE's "Still
Interested" inquiry on August 5; the policy required requesters with requests
filed before October 1, 2024 to reconfirm interest; the quoted holding;
plaintiff American Oversight. Federal News Network (s9) confirms the judge, the
date, the October 1, 2024 cutoff, the exact quoted language ("does not authorize
... reiterate their interest in pending requests"), and the plaintiff. The
Federal Register notice (s8) is the genuine policy document the court vacated and
is honestly labeled primary. One note, not a break: the primary linked is the
underlying policy, not Jackson's order, so the ruling itself — the actual news —
rests on two secondaries. The item still carries an honest primary plus
independent accounts and clears the gate; a docket link to the order would be a
stronger, more parallel primary (see Required work, optional).

Item 4 (productivity). Claims: nonfarm productivity +1.4%, real hourly
compensation −3.1%, unit labor costs +1.3%, manufacturing ULC flat with a 1.9%
pay gain matched by 1.9% output, labor share ~53% and a record low since 1947.
The BLS release (s11) confirms +1.4%, −3.1%, +1.3%, and manufacturing +1.9% /
0.0%; the manufacturing "pay gain matched by output" is a sound reading of the
ULC identity. On the labor-share claim I found the article had understated its
own sourcing: the record low is stated verbatim in the BLS release itself ("The
labor share ... was 52.9 percent ... the lowest level in the series which begins
in the first quarter of 1947"), not merely inferred. The draft framed it as "by
one reading of the same release," a hedge that both misdescribes a flat primary
statement and reads as self-reference. I fixed it directly (see Edits). Market
Business News (s12) independently reports the same 52.9% and the 1947 record, so
it remains a valid secondary; the weak-outlet worry is moot because the primary
owns the claim.

Item 5 (ISM Services). Claims: 25th straight month of expansion; PMI 54.1% (up
0.1 from June's 54.0%); business activity 59.1% (up 3.7 points); employment 47.4%
(contraction, after 51.2% in June); prices 70.3% (above 60% for 20 months). The
ISM release (s13) confirms 54.1%, the 25th month, 59.1% and the 3.7-point move,
70.3%, and the 20-month streak; Brisk Markets (s14) owns and confirms the 47.4%
employment reading and the June 51.2%. All numbers hold. One clause outran the
evidence: "the stretch over which tariffs have worked their way through supplier
costs" attributes a 20-month price elevation to tariff pass-through, but 20
months back from July 2026 begins in late 2024, before the tariffs it names. I
cut it (see Edits).

## Cut

Three surgical changes, all cuts or clause-level repairs; no rewrites.

The worst tell was item 4's "By one reading of the same release," which dressed
the BLS release's own flat statement as an interpretive move and softened a hard,
primary-owned number. Removing the hedge and restoring the exact 52.9% is both a
slop fix and an accuracy fix.

Item 2 carried a semicolon splicing two independent clauses (the Pentagon's
defense and the order's effect) where the editorial direction wants the period
that a spliced thought is usually avoiding; I made it a period.

Item 5's tariff clause was an unsupported nonessential causal claim, cut per the
skeptic's standing license.

On formula: the five entry moves are otherwise well varied — a status/where-it-
stands lead, a counterfactual ("Until Thursday ... were stranded"), a rule
("A federal agency cannot ..."), a subject-reversal ("produced more ... took home
less"), and a figure-with-caveat. The one soft spot is the 4→5 adjacency: both
economic items open on a "good news, but a catch" contrast, and item 5's lead
("expanded for a 25th consecutive month ... though not on every front") is the
most recap-like of the set, deferring its real consequence (services running hot
on prices while shedding jobs) to later sentences. It clears the bar but sits
closest to it; noted for the writer, not routed.

Furniture earns its place. The rs-docket on item 1 sets the standing case facts
apart so the prose can argue the benchmark point, and every figure in it is cited
in nearby prose. The stat strip on item 5 carries three heterogeneous headline
numbers, each cited. Neither reads as decoration. No component is missing where
prose is hiding a shape.

## Reader

Read straight through as the paper's declared reader, the brief gives more than
its sources: the per-work ~$3,000 reframed as the first court-approved price for
training copies and a benchmark for the licensing fights ahead (the sources give
only a fund, a claim rate, and a per-work estimate); the labor-share record low
as the frame on a productivity gain workers did not keep; the services reading as
busier-but-pricier-while-shedding-jobs; and the FOIA ruling as the closing of a
quiet backlog-clearing route. The draft-handoff's original-work sentence — the
per-work figure as the settlement's lasting mark — is genuinely present in item
1's close and is the writer's synthesis, not a restatement. The prose sits closer
to the voice-guide exemplars (Semaform's separate analytical beat, consequence-
first leads) than to a median summary. The piece is not a redraft candidate. Its
one real weakness is that the lead item's marquee framing is pinned to timing its
own citation does not carry.

## Edits

- Item 2: changed the semicolon before "the order lets the projects advance" to a period (comma-splice/semicolon repair).
- Item 4: replaced "By one reading of the same release, labor's share of what it produces fell to about 53 percent, the lowest since the series began in 1947." with "Labor's share of what it produces fell to 52.9 percent, the lowest since the series began in 1947." (cut self-referential hedge; restored the primary's exact figure; s12 citation retained, still valid).
- Item 5: cut the clause ", the stretch over which tariffs have worked their way through supplier costs" (unsupported, temporally incoherent causal claim); citation to s13 retained.
- Ran `./nb stamp` after the cuts (words 897, reading 4 min, sources 14).

## Required work

- **writer** — Item 1 payout-timing citation. The lead ("first payments ... around
  August 10") and the item headline ("days from its first payments") cite s1, the
  settlement `/dates` page, which carries no August date. Re-point that claim to
  the source page that actually carries the ~August 10 estimate (the settlement
  FAQ, which is reachable and independently corroborated) and confirm the printed
  `href` resolves to it, or soften the claim to what `/dates` supports. Do not
  leave a load-bearing lead claim citing a page that omits it.
- **writer** — Item 1 dek accuracy. "starts writing checks" asserts payments are
  being issued; the established fact is an *estimate* of first payments around
  August 10, contingent on the judgment becoming effective and appeals resolving,
  and none has issued as of 2026-08-07. Align the dek (both the `nb-meta` `dek`
  and the rendered dekline) to what the sources establish, then re-run
  `./nb stamp` and the proof.
- **writer** (optional, non-blocking) — Item 3 would carry a stronger, more
  parallel primary if it linked Judge Jackson's order/docket rather than only the
  vacated Federal Register notice; the item clears the gate as-is.

## Decision

revise — the lead item's marquee payout timing is pinned to a citation that does
not carry it and a dek that overstates an event the sources place three days out
and contingent; both are writer fixes.
