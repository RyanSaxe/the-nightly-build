# Draft handoff: investing/reverse-dcf (01)

## Original-work sentence

The article converts Mastercard's market capitalization into a single
stated-frame implied-growth bar (about 8.8% free-cash-flow growth for a decade
at a 9% discount rate and a 4% terminal rate), then weighs that bar against the
company's own realized FY2023-2025 growth to recast the investment question from
whether the stock is cheap into whether a business already generating $16 billion
of free cash flow can sustain high-single-digit growth for ten years at that
scale. The evidence record supplies the verified series and the model-structure
swings as separate figures; assembling them into that framed bar and that
reframed question is the article's own work, and it is visible in the
conditional-answer section, the sensitivity chart, and the verdict.

## Proof result

`./nb check ... --series investing --library <checkout>` (links included):
**BLOCK: 0**, verdict PUBLISHABLE.

One WARN left standing, on purpose:

- **W-SENTENCE-DENSITY** ("sentence is 47 words with 4 clause joins, punctuation
  score 87"). This is not a prose sentence. The density heuristic reads the
  annotated equation's raw LaTeX source as a sentence: `nb-math-eq` divs are not
  in `SENTENCE_SKIP_TAGS` (which skips only real `<math>`, `<code>`, `<pre>`,
  `<blockquote>`), so the TeX tokens count as words and its braces and parentheses
  drive the punctuation score to 87. The article carries exactly one annotated
  equation, the two-stage reverse DCF the whole lesson turns on, authored in the
  documented markup. There is no way to "split" required equation TeX, and every
  genuine prose sentence in the draft clears the heuristic. The warning is a
  furniture false positive and stands.

## Notes for the editor

- Every dated input is labeled as of its date, per the brief: the $569.29 close
  as of Friday 2026-08-14, the 4.69% ten-year Treasury as of 2026-08-17, the
  4.2-4.5% equity risk premium as of 2026. If publication slips past these dates
  the price and yield should be refreshed; the arithmetic (implied 8.8% at the
  stated frame) moves with the price.
- The sensitivity chart (`chart-1.py`/`chart-1.png`) is my own computation from
  the verified inputs, reproduced independently and matching the evidence
  record's series exactly (single-stage 5.5%, two-stage 8.8% at 4% terminal,
  10.5% at 3% terminal, plus the 9.5%/8.5% discount-rate points in the table).
  The script is committed beside the article as its provenance.
- The negative-parallelism in the takeaway ("not whether the company is fast
  enough today but whether it can hold that pace") corrects a misconception the
  body names explicitly (the "tempting read" that a bar below recent growth means
  the stock is cheap), so it is an earned contrast rather than an invented
  strawman.

## Open evidence / voice questions

None blocking. The one soft spot is inherited from the evidence and handled in
prose rather than resolved: the implied-growth number is conditional on the
discount rate, terminal rate, and horizon, so the article states it only with its
frame attached and never as a figure the market "quotes." No researcher request
is needed.
