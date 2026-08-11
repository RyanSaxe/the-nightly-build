# Draft handoff: current-events/2026-08-11 (writer 01)

## Original-work sentence

The article turns the evidence record's flagged contradictions into the
reader's takeaways: it states the vaccine cut with both the 17- and 18-disease
denominators and the RSV distinction that separates them, and it sets the D.C.
Guard deployment's property-crime drop beside its violent-crime rise and the
task force's inability to tie either result to the troops, so each disputed
figure arrives already weighed rather than left for the reader to reconcile.

## Proof result

`BLOCK: 0` with links included (full brief command). `verdict: PUBLISHABLE`.

Warning intentionally left:

- **W-LENGTH-LOW — brief expects 4-6 items; found 3.** The evidence record
  supports exactly three developments that carry both a resolving primary and an
  independent secondary with matching `data-nb-kind`: the childhood-vaccine
  executive order, the D.C. Circuit ballroom ruling, and the D.C. National Guard
  one-year figures. The remaining candidates cannot make a per-item primary that
  the `per_item_sources` block (`primary: [1,1]`) requires and the proof enforces
  as `B-SOURCE-KIND`: the Lisa Cook removal item has only a secondary
  (SCOTUSblog) in the record with no resolving primary URL, and the Alabama
  special primary has no verified result (its owning returns were still coming in
  on election night). Padding the vaccine order into two items or attaching an
  absent/unverified primary would break either the editorial standard or the
  proof. Per the brief's own instruction to "drop any candidate whose sourcing
  the evidence record marks unverified... rather than running it thin," I ran the
  three fully-sourced items and left this warning rather than fabricate a fourth.

## Items run (3)

1. **Childhood-vaccine executive order** (lead) — primary s1: White House fact
   sheet; secondary s2: NPR. Carries the 11-disease universal tier, the 17-vs-18
   denominator made explicit (RSV monoclonal antibody counted), the 1980-vs-2024
   dose history, autism attributed to Trump's signing remarks (not the order),
   and the AAP rejection. Stat strip carries the three thesis numbers (11 / 84+ /
   23), each cited in prose.
2. **D.C. Circuit ballroom ruling (7 Aug)** — primary s3: the D.C. Circuit
   opinion (No. 26-5123); secondary s4: CBS News. 2-1 holding with Rao's dissent
   noted, the 90,000-sq-ft / $400M project, the National Trust suit, the 14-day
   stay and promised SCOTUS appeal, and the majority's "temporary tenant" line.
3. **D.C. National Guard one-year mark (11 Aug)** — primary s5: the Senate HSGAC
   report (executive summary); secondary s6: Stars and Stripes. Troop counts,
   the CBO/Pentagon/Niskanen cost figures, and the mixed crime record with the
   causation caveat.

## Open sourcing note for the editor

Two item primaries (s3 the D.C. Circuit opinion PDF, s5 the HSGAC report PDF)
are records the researcher confirmed resolve as live documents but could not
parse to text; their substance is carried entirely by the cited secondary in
each item (s4 CBS, s6 Stars and Stripes), which read and reported it. This
mirrors the pattern the evidence record itself endorses for the ballroom
opinion. No exact language, locator, or figure is attributed to an unread
document: the "temporary tenant" quotation is cited to CBS, and every National
Guard figure is cited to Stars and Stripes. No `data-nb-locator` was added for
s3 or s5 because the record supplies none.

Date frame: the lead (10 Aug) and the National Guard mark (11 Aug) sit at the
front of the few-day frame; the ballroom ruling (7 Aug) is flagged here as
genuine recent movement, not backfill.
