# Editorial review: company-analysis/spacex (editor/01)

## Skeptic

Thesis: SpaceX's first public quarter shows Starlink (Connectivity) earning the
revenue and the newly acquired AI unit spending the capital, so most of the
roughly $1.75 trillion market cap is a claim on the unprofitable AI segment and
on unquantifiable Starship optionality, not on the profitable business the
filings document.

The claims it stands on, tested:

1. The 10-Q reports three segments, Space, Connectivity, and AI, and Starship is
   not a reporting unit. Primary (s2, 10-Q). The evidence record carries the
   segment-note quote verbatim; the article states Starship "sit[s] blended
   inside the Space segment and cannot be pulled out," which the record confirms
   (no Starship revenue, R&D, or capex line). Held.

2. Connectivity carries the revenue ($4,291M of $7,814M) and AI carries the
   capital ($15,828M of $18,369M, 86%). Primary (s4, earnings release). I
   recomputed the split: segment revenue 962 + 4,291 + 2,561 = 7,814 (matches
   total); capex 1,174 + 1,367 + 15,828 = 18,369 (matches total); 15,828 / 18,369
   = 86.2%, so "86%" is right. Consumer $2,485M + Enterprise/government $1,806M =
   $4,291M. Held.

3. The company is GAAP-unprofitable (operating loss $143M, net loss $541M) under
   a $3.5B adjusted-EBITDA headline. Primary (s2, s4). Matches the record. The
   article defines EBITDA in the sentence it first appears and names what the
   $3.5B-to-$(541)M gap is made of. Held.

4. The market cap is contested, roughly $1.75T basic to ~$2.3T diluted. Computed
   plus secondary (s3, s6). I recomputed: 13,181,779,945 basic shares (Class A
   7,696,293,669 + Class B 5,485,486,276) times ~$133 = $1.753T. The Sacra
   diluted figure ~$2.3T is labeled an independent estimate. Held.

5. The decomposition: Connectivity accounts for a tenth to a fifth of the price;
   the residual rests on AI and Starship. I recomputed every step. Run-rate =
   Q2 revenue times four: Connectivity 4,291 x 4 = $17.2B (~$17B), AI 2,561 x 4 =
   $10.2B (~$10B), Space 962 x 4 = $3.8B (~$4B), whole company 7,814 x 4 = $31.3B
   (~$31B). Price of revenue: $1.75T / $31B = 56.5x; $2.3T / $31B = 74.2x — the
   article's "about 56 and 74 times revenue" is correct. Connectivity at 10x =
   $170B and 20x = $340B; $170B / $1.75T = 9.7% (a tenth), $340B / $1.75T = 19.4%
   (a fifth) — "between a tenth and a fifth" is correct, and "at most a fifth" is
   the 20x high end. Growth checks: total 7,814 / 4,071 = +92%; Connectivity
   4,291 / 2,588 = +66% ("about two-thirds"); early-release trigger $135 x 1.30 =
   $175.50. All arithmetic holds.

Writer flag 1, the "at most a fifth" bound and the Sacra dependency. My decision:
adequately hedged, no researcher route required. The quantitative bound does not
rest on Sacra's operating-profit estimate. It rests on Connectivity's
filing-disclosed segment revenue (~$17B run-rate, a primary figure) times an
explicitly illustrative multiple. Sacra's claim that Starlink is the only segment
earning an operating profit supports only the framing (why Connectivity earns a
"generous" multiple), and the article quarantines it twice: "Sacra, whose figures
are independent estimates and not the company's," and "the record does not confirm
it breaks out profit by segment, so that profitability cannot be checked against
the 10-Q itself." That states the uncertainty plainly, as the numbers section of
the editorial standard requires, and the thesis holds a fortiori at the higher
$2.3T denominator. A primary segment-profit figure would only tighten the range,
not repair a break, so I am not blocking on it. I record it below as an optional
later-round improvement for the researcher, not required work.

Writer flag 3, the display-text market cap. My decision: the single $1.75T in the
headline honors the "state the contested market cap as a range" caveat, no change.
$1.75T is the lower-bound, basic-shares, primary-anchored denominator, and the
thesis is strictly stronger at the higher figure, so the headline takes the
conservative anchor. The body states the range every time it does arithmetic ("The
honest denominator is a range, roughly $1.75 trillion to $2.3 trillion"; "$1.75 to
$2.3 trillion... between about 56 and 74 times revenue") and devotes a section to
the contest. The caveat governs how the analysis treats the cap, which is as a
range; a headline leads with one concrete figure, and the headline standard prefers
that over a clumsy range. Honest and internally consistent.

Display text audited descriptor by descriptor: headline (claim the piece defends,
actor named, figure earns its spot), dek (a claim about the world, not a
method-grade; 86% and "without a profit to show" both check), and all six
subheads. Every named figure, date, and the xAI $1T/$250B Feb 2026 marks check
against the record. No wrong labels.

data-nb-kind audit: all eleven labels correct. The four SEC filings (s1 index, s2
10-Q, s4 earnings release EX-99.1, s7 pricing FWP) are primary; CNBC quotes/
reporting, techjournal, Sacra, Motley Fool, and Investing.com are secondary. The
lock-up is correctly labeled secondary and the article states the prospectus body
could not be read, honoring the recast caveat. Source count 11 meets the minimum-8
policy. I could not independently open the future-dated primary SEC hrefs in this
environment; the segment structure and revenue were cross-corroborated across two
independent primary documents (10-Q and earnings release) in the evidence record,
and the figures are internally consistent (segments sum to totals), so I do not
block on link resolution, which is the researcher/writer's domain.

## Cut

The prose is clean and sits in the calm plain-sentence register the voice guide
sets. One edge sentence failed the slop test: "It sits behind a second number
worth pausing on," where "worth pausing on" is throat-clearing that directs
attention rather than doing work. Deleted per the delete-don't-repair rule; the
paragraph now opens on the GAAP-loss fact, which is stronger.

Sentences I tested and kept: the negative-parallelism constructions ("The segment
that earns the most revenue is not the segment that spends the most capital"; "not
paying for this year's business. It is paying for a much larger business") each
correct a real, named misconception and are cashed out with figures, so they are
earned contrasts, not invented strawmen. The imperative transitions ("Start with
where the money comes in," "Put the pieces back together") organize the
revenue-then-capital and reassembly structure and read as the Buffett-style plain
directive the voice guide models, not empty signposts. The closer, "That is a
question about an AI company, asked of a company most people think of as a rocket
company," survives the slop test because it depends on the nouns and states the
reframe the argument built. No borrowed distinctive phrasing from the voice-guide
exemplars: the Damodaran/Buffett idea that quantifying uncertainty does not remove
it is expressed in the article's own words ("Putting a number on the AI segment or
on Starship does not make either one more certain"), not lifted.

No prompt leakage: the "profitable Connectivity" and "86% of capital" framings are
sourced facts, not lifted commission instructions. Punctuation holds: zero
em-dashes, and the two semicolons ("Starlink earns; the AI unit spends,"
"Connectivity brings in the money; AI... consumes it") are tight balanced
antitheses, the rare case the standard permits.

Formula check against the recent-pattern notes: the recast produced its own
structure. The piece does not open on an nb-stat/nb-stat-strip block (it opens on
the filing-sequence fact), uses none of the "what the price has already paid for"
/ "the quarter the price has to justify" heading molds, and closes on a verdict
about where the price rests, not a "two ways to read it" section. The dek avoids
the semicolon-reversal, suspended-question, and comma-triad molds. No formula flag.

## Reader

What the piece gives beyond its sources: a reader who has read only this article
knows that most of SpaceX's ~$1.75T price is a bet on the AI unit it acquired from
xAI in February 2026, a segment with no profit record that consumed 86% of last
quarter's capital, while the profitable Starlink business can account for only a
tenth to a fifth and Starship is unmeasurable from the filing. The raw sources (a
10-Q, an earnings release, a quote page) do not hand over that decomposition; the
article constructs it from disclosed segment revenue, the February deal marks, and
an explicit revenue-multiple bound. The original-work sentence in the draft
handoff makes the same claim, and it survives the comparison. The prose sits
closer to the voice-guide exemplars than to a median AI summary: numbers ride
inside ordinary sentences and the segment arithmetic, not the vocabulary, does the
persuading.

## Edits

- Deleted the signpost sentence "It sits behind a second number worth pausing on."
  at the head of the profitability paragraph in the "Starlink earns; the AI unit
  spends" section.

## Required work

None blocking.

- (Optional, researcher, later round) If the 10-Q Segment Information note in fact
  discloses operating income or loss by segment under ASC 280, a later round could
  replace Sacra's secondary operating-profit estimate with the primary figure and
  tighten the "tenth to a fifth" range. Not required: the current bound rests on
  disclosed segment revenue times an explicitly illustrative multiple, and the
  article states plainly that segment profit cannot be checked against the filing.

## Decision

approve. The recast holds against the evidence, the decomposition arithmetic is
correct, all three writer flags resolve without a change to any number, name, or
quotation, and the one slop edge was cut directly.
