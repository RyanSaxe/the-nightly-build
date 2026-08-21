# Draft handoff: investing/capital-allocation (01)

## Original work

The article turns nine scattered filings and letters into one traceable
company-window: everything in the orientation table and the reinvestment,
acquisition, and debt paragraphs is drawn from the same Berkshire 10-Q
(source 1) covering the first half of 2026, so a reader can open one
document and check four of the five uses at once. No source states the
buyback identity as an equation; the derivation (V' = (VS - C)/(S - C/P),
with the sign of V' - V determined entirely by whether P is below or above
V) is this article's own algebra, built to formalize the qualitative rule
every primary source states in words ("value is destroyed when purchases
are made above intrinsic value"), verified by substitution before it was
set as the annotated equation. The framing device, that Berkshire's 21-month
buyback halt and resumption is the same test binding in real time rather
than a textbook illustration, is also original: no single source narrates
it that way end to end; it required combining the 2018 policy-change filing,
the 2026 10-Q's current wording, and the two Motley Fool pieces on the halt
and its dollar figures into one continuous timeline showing the standard's
wording get more literal (formula, then discretion, then a named
decision-maker) while never changing its substance.

## Proof result

`./nb check .nb-work/investing/capital-allocation/library/investing/capital-allocation.html --series investing --library /home/user/library-checkout --check-links`: **BLOCK: 0, WARN: 0 — PUBLISHABLE.** Stamped
words=2170, reading_minutes=9, sources=9 (6 primary, 2 secondary counted by
`data-nb-kind`, plus the derived-equation citation carried by the Damodaran
primary). Two rounds of `W-SENTENCE-DENSITY` and one `W-CITE-ORDER` warning
were raised and cleared: three long sentences were split (verified against
the engine's own `sentence_density` heuristic directly, not just by manual
recount), and the BNSF/2012-letter citation pair was renumbered into
first-appearance order. A `W-PLACEHOLDER` warning on the table's all-caps
caption and headers was also cleared by resetting them to sentence case,
matching the published library's own tables rather than the furniture
catalog's caps-as-placeholder sample text.

## Scope honored

The evidence record's caution about the H1 2026 buyback total is respected:
the article anchors on the 10-Q's own cash-flow-statement figure (roughly
$4.4 billion) rather than the Motley Fool quarter-by-quarter figures, which
do not sum to the same total, and states only the qualitative "most of it in
the second quarter" rather than a precise split the sources do not agree on.
The acquisition-test quote from the 2012 letter is applied to OxyChem only
as a statement that the standard has not moved, not as a claim that
management explicitly recalculated it for that deal, per the researcher's
flagged distinction. Debt paydown is written as two segments moving in
opposite directions in the same half, not collapsed into one number that
would misstate what the filing shows.

## Open questions

- **Furniture (non-blocking):** the buyback equation was rendered as an
  annotated `nb-math` figure (four colored terms plus the intrinsic-value
  output) rather than a plain table, per the commission's instruction to use
  an equation where the quantitative relationship is the point. A table
  carries the four filed dollar figures instead, in the orientation section.
  Chrome is absent in this environment, so the equation was checked against
  the furniture catalog's exact `\htmlClass{nb-mc1..5}` syntax and the
  structural proof, not visually rendered; flagging for the editor's own
  render pass.
- The Mauboussin/Callahan capital-allocation paper and one CNBC piece on the
  buyback halt both returned fetch errors (403/403) and were not opened, so
  not cited; the researcher's evidence record names both and the claims they
  would have supported are independently carried by sources that were read
  in full (Damodaran for the framework, the two Motley Fool pieces for the
  halt). No action needed unless the editor wants either substituted.
- No open voice question. The bookends address the reader under the
  template's license ("you have learned," "by the end you will be able
  to"); the body speaks to no one, never narrates the lesson, and the word
  "leverage" appears exactly once, inside the direct Owner's Manual quote,
  to stay under the press's one-use limit.
