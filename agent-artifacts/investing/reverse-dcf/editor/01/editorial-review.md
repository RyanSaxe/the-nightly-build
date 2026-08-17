# Editorial review: investing/reverse-dcf (editor/01)

## Skeptic

Thesis: invert the DCF the course already built, hold a company's price fixed,
and solve for the free-cash-flow growth the price must assume; that implied
growth is never one number but a function of the discount rate, terminal rate,
horizon, and the cash-flow base, so it must always be quoted with its frame. For
Mastercard at $569 the frame-attached bar is about 8.8 percent growth for a
decade, which sits below the company's recent record, turning the reader's
question from "is the stock cheap" into "can a business this large sustain that
pace."

Claims it rests on, and how each held:

1. Reverse DCF is the standard DCF run backward (Rappaport and Mauboussin).
   Opened s1 and s10: the authors' own site carries the exact "market's own
   pricing model, the discounted cash flow model, with an important twist" and
   the two-skills framing (read the implied expectations, then anticipate
   revisions). Held.
2. Mastercard's $569 implies 8.8 percent decade growth at a 9 percent cost of
   equity and 4 percent terminal rate. Recomputed against the chart script and
   the evidence series: base $16,433M = OCF 17,648 - capex 489 - capitalized
   software 726; 876.0M shares; $569.29 close; market cap 876.0 x 569.29 =
   ~$498.7B, matching the aggregator. The crossing sits at 8.8 percent. Held.
3. The implied number swings with assumptions (5.5% single-stage, 10.5% at 3%
   terminal, 10.1% at 9.5% discount, 7.4% at 8.5%). Every table cell matches the
   evidence's derived series. Held.
4. Terminal value is ~two-thirds of value, so the growth assumption carries more
   weight (Damodaran Myth 5.5), and terminal growth is capped by the economy
   (Myth 5.4). Opened s7 and s8: both sentences are near-quotes of the primary.
   Held.
5. The FCF base is itself contestable (FCF lesson). Held, but the sentence that
   quantified the swing was wrong (see the break below).
6. The 8.8% bar sits below realized FY23-25 growth (rev 14.3%, NI 15.6%, FCF
   22.8%). Recomputed all three two-year CAGRs from the 10-K figures in the
   evidence; each matches. Held.

Break found and fixed: the which-cash-flow section read "Leave both out and the
base rises from $16,433 million to $17,159 million." Only one lever produces
$17,159M: leaving the $726M of capitalized software in (17,648 - 489). The
stock-comp add-back moves the base the other way, since removing it (treating
share pay as a real cost) lowers the base, which the two sentences before this
one establish. Attributing the rise to "both" is arithmetically wrong and
contradicts the section's own setup, and the declared quantitative reader would
catch it on the first read. Fixed in place with content already at hand: leaving
the software in raises the base to $17,159M; stripping the stock-comp add-back
lowers it. No number was invented (the evidence records $17,159M as the
capex-only base and does not quantify the SBC line, so the downward move is
stated directionally only).

Display text audited descriptor by descriptor. Headline states the method as a
finding, no colon subtitle. Dek reveals the $569-to-growth inversion and
attaches the caveat ("a number that shifts with every assumption behind it"), so
it does not present implied growth as a figure the market quotes, and it avoids
the recent "at $X, company is Y" mold. Every subhead names a step in the piece's
own nouns. The three Background link texts were checked against the linked
lessons themselves: each matches the prior lesson's exact title.

data-nb-kind audit: nine primaries and one secondary. The secondary
(stockanalysis, s2) is an aggregator used only for the market quote, correctly
labeled; its reported market cap ($498.70B) matches. The SEC filings (s3 10-Q,
s4 10-K), Damodaran blog posts (s6-s9), FRED series (s5), and the authors' site
(s1, s10) are each the owning primary for what they support. No mislabel.

Every citation href opened as printed. s1, s2, s3 (Q2 2026 10-Q), s4 (FY2025
10-K), s6, s7, s8, s9 (the slug's "ddiscount" typo is the real Damodaran URL and
resolves), s10, and both Go-deeper links resolve and land on the source. The
2026 ERP figures on s6 (4.23% start of 2026, 4.37%-4.51% early March) support
the article's "4.2 to 4.5 percent for 2026." s5 (FRED DGS10) returned a 403 to
the automated fetcher, which is bot mitigation on FRED, not a broken link: it is
the canonical DGS10 series identifier and resolves for a human reader, and it is
the correct owning series for the dated Treasury yield.

The equity-side consistency holds: the equation discounts firm-level FCF at the
cost of equity against equity value (market cap), and the piece notes debt is
small enough that WACC lands near the cost of equity, which the evidence
sanctions. A defensible lesson-level simplification, not routed.

## Cut

One arithmetic-driven prose fault (the FCF-base sentence) is recorded under
Skeptic. The dedicated slop pass found two sentences to cut and no repeated
pattern.

Cut 1, a signpost: "Reading the same price through different model structures
makes the range concrete." It reduces to a generic method-benefit sentence and
its only added content ("makes the range concrete") grades the upcoming table
rather than reasoning. The table's caption already frames it, and the surviving
lead, "A simple perpetuity asks least; a longer forecast with a lower terminal
rate asks most," carries the content.

Cut 2, a decorative tail in the takeaway: "...to 5.5 percent as a simple
perpetuity, which is the discipline the method asks for." The "which" clause
labels rather than adds a fact, and the next sentence states the discipline
plainly ("Quote the implied number with the assumptions that produced it, never
on its own"). Removed the tail; the sentence now closes on the figures.

Negative-parallelism sweep: every "not X" construction in the piece corrects a
misconception the piece itself names (the implied rate is a testable statement
"not a verdict"; the growth assumptions carry more weight "not less," a
near-quote of Damodaran; the bar is "not this year's growth rate" but a decade
of it; the question is "not whether the company is fast enough today but whether
it can hold that pace"). Each is an earned contrast against a real, named
misconception, so each stays. Punctuation is clean: no em-dashes, colons used
for payoff/definition, and the few semicolons bind tight antitheses. No
prompt-leakage: no planning labels, no assignment-fulfilled claims, and no
clause order lifted from the commission or briefs. No borrowed phrasing from the
voice-guide exemplars (the piece works Mastercard's own numbers, not the $1,000
factory, the $1 test, or $500,000-beside-$153,000). The two bookend cards
address the reader as the template allows; judged as prose, each sentence says
something particular to this lesson.

The known W-SENTENCE-DENSITY warning is confirmed as the documented
`nb-math-eq` equation false-positive: the density heuristic reads the two-stage
reverse-DCF LaTeX as a 47-word sentence because `nb-math-eq` is not in its skip
tags. The markup is the documented equation furniture, and every genuine prose
sentence clears the heuristic. Treated as a known engine false-positive, not a
prose defect.

## Reader

Read straight through as the course's quantitative reader, what I have that the
sources alone would not give me: a repeatable move for turning any current price
into the growth it assumes, worked once end to end on a real company, plus the
discipline of never stating that growth without its frame and the reframed
question of durability at scale. The original-work sentence claims exactly this
(assembling the verified series and model-structure swings into one framed bar
and a reframed durability question), and the article delivers it in the
conditional-answer section, the chart, and the verdict. Both answers survive, so
the piece teaches rather than restating its sources. The prose sits with the
voice-guide exemplars, letting the numbers carry the explanation, not a median
summary. The headline read as the largest claim holds: the piece does run the
valuation backward and read the priced-in growth.

## Chart

chart-1.py provenance matches the evidence exactly: FCF0 16433, SHARES 876.0,
R 0.09, N 10, PRICE 569.29, terminal curves at 4% and 3%, marker at (8.8, 569).
Read as a reader: axes labeled with units, linear scale, honest legend, and the
4% curve crosses the $569 line at 8.8% while the 3% curve crosses near 10.5%,
matching the caption and alt text. No correction needed.

## Edits

- which-cash-flow: "Leave both out and the base rises from $16,433 million to $17,159 million" -> "Leave it in and the base rises from $16,433 million to $17,159 million; strip out the stock-comp add-back instead and it falls" (fixes the arithmetic attribution; only the software lever produces $17,159M, and the stock-comp lever moves down).
- which-assumptions: cut the signpost "Reading the same price through different model structures makes the range concrete."
- takeaway: cut the decorative tail "...which is the discipline the method asks for," closing the sentence on the figures.

## Required work

- writer: re-run the proof (`nb check`, links included) on the edited article so
  BLOCK stays 0 and the word/reading counts refresh; the only expected WARN is
  the known W-SENTENCE-DENSITY equation false-positive. No content change is
  requested.
- orchestrator: re-stamp counts after the edits before preparing the PR. If the
  publication date slips materially past the labeled as-of dates, the price and
  Treasury-yield refresh is a writer/orchestrator prepare-PR step, not an
  editorial change.

No researcher work: no evidence gap, no broken central claim, no source-policy
failure.

## Decision

approve — the thesis and every load-bearing claim held against the sources and
the recomputed arithmetic, and the one factual fault plus two slop sentences were
fixable in place with content already in hand.
