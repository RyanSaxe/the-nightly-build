# Draft handoff: current-events/2026-08-15 (writer 01)

## Original work

Beyond what the evidence record supplied, this draft independently resolved
which candidate items could actually carry a primary source (the series
requires exactly one per item): it opened the Tohono O'odham memorandum
opinion itself (D.D.C., 26-2127) via the court's public-opinion endpoint,
verified two quotes evidence had flagged as paraphrase-with-quotation-marks
against that primary text, found and cited a fourth item (the CFTC's
emergency order against Kalshi's New York suit) that is not in the evidence
record at all, and dropped every item whose primary stayed unreachable after
its own retry, rather than mislabeling secondary reporting as primary to hit
the count.

## Proof result

`./nb check --series current-events
.nb-work/current-events/2026-08-15/library/current-events/2026-08-15.html
--library /home/user/library-checkout` (links included, after `nb stamp`):
**BLOCK: 0, WARN: 0** — no warnings intentionally left.

## Departures from the brief, and open questions

- **Nevada fake-elector item dropped.** The brief asked me to favor this item
  as one whose primary was confirmed, but evidence.md's own primary note says
  the researcher could not open Clark County's order, and I could not either
  after several routes (docket search, AG press room, DocumentCloud, Justia).
  The series config requires exactly one primary source per item
  (`per_item_sources.primary: [1, 1]`), enforced as a hard block, so three
  strong independent secondary accounts were not enough to run it. Same
  outcome, same reason, for Mangione's plea and the Kennedy Center vote — I
  re-attempted the DOJ and Kennedy Center primaries myself (401/403 both
  times) before leaving them out, per the brief's instruction.
- **Fourth item substituted.** To reach the four-item floor without those
  three, I sourced a story outside the evidence record: the CFTC's August 11
  emergency order keeping Kalshi operating against New York's $36B suit,
  primary at cftc.gov, independent account at PYMNTS. Its anchor date (Tuesday,
  August 11) sits a little further from the 15th than the other three items.
  I judged it in bounds as the freshest dated action in a live, consequential
  jurisdictional fight, distinct from the "mention markets" thread evidence.md
  correctly set aside as too soft — but an editor should weigh whether that
  dateline is too old for this series.
- **Two quotes cut, not carried.** Evidence attributed "novel case with novel
  issues" and "without congressional authority" to Judge Leon in quotation
  marks. Neither phrase appears in the memorandum opinion's text (I searched
  all 18 pages). I used only language I could verify directly in the opinion
  and left those two out; they may be accurate renderings of something Leon
  said from the bench at the July 22 hearing rather than the written order,
  but I have no transcript to confirm that.
- Voice guide and headline/dek: no open question. All four items lead on a
  named actor and a specific fact per the voice guide's model, and the dek
  was checked against the banned dek molds in spec/headlines.md.
