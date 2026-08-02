# Draft handoff: parenting-research/infant-iron (writer/01)

## Original work

The draft's one act of original work: it maps the record's entire relevant
RCT evidence — the diagnosed-anemia treatment trial, the two prevention
trials, the largest meta-analysis, and the 2026 behavioral follow-up — onto
the exact decision fork a six-month-old's household actually faces (already
diagnosed anemic vs. iron-replete), showing that the same body of trials
supports two different, non-contradictory verdicts depending which infant is
being asked about, and uses that split (not a single pooled "iron
works/doesn't work" verdict) to draw the line between what a family decides
at the spoon and what a pediatrician decides at dosing, diagnosis, and
preterm status. The comparison table and the single "Verdict" note carry
this directly; the AAP/ESPGHAN position cards and the guideline-vs-guideline
material show the same split reproduced at the level of clinical policy, not
just trial results.

## Proof result

Final command (as specified in the brief), run from repo root:

```
./nb check .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html \
  --series parenting-research \
  --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. Link checking was
included in this final run (not `--no-check-links`); no source resolved to a
404/410 or an unresolving domain. `nb stamp` was run beforehand: 2,986
words (within the 1200-3000 band), 16 sources (floor is 8), 13-minute read.

No warnings were intentionally left. The draft went through several rounds
of trimming and sentence-splitting to clear an initial `W-LENGTH-HIGH` (the
first full draft ran to 3,222 words) and ten `W-SENTENCE-DENSITY` warnings;
all were fixed by cutting redundant restatement (chiefly numbers that the
comparison table already carries) and splitting overloaded sentences, not by
dropping evidence or citations.

## AAP 2026 report: direct fetch attempted, not available

Tried WebFetch against the report's own DOI (resolves via 302 to the live
article page), the direct `publications.aap.org` article URL, and the AAP
Journal Blog post about the update: all three returned HTTP 403. A fourth
route, the Medscape write-up, returned HTTP 402 (paywalled). This matches
the researcher's own access log exactly — the report is gated, not broken or
fabricated. The article keeps the caveat visible in the body (the
"Where AAP and ESPGHAN part ways" section): the 2026 screening ages, the
unchanged breastfed dose, and the preterm regimen are attributed to the
AAP's own consumer restatement and an independent guideline digest that
cross-checks against it, with an explicit note that the report's own
evidence grading was not confirmed by direct reading.

## Notes on furniture and citations

- Furniture used with a specific purpose each: one stat strip (the 0.27→11
  mg/day requirement jump), one table (the four-trial treatment-vs-prevention
  comparison — this is where the record's central contradiction is made
  visible rather than argued in prose alone), one `nb-note-strong` Verdict
  (used once, as required), and a pair of `nb-position` cards for the
  AAP/ESPGHAN split. No chart or source asset was captured this round; the
  table already carries the comparison the evidence record flagged as the
  strongest visual candidate, and the two prevalence/food-content source
  assets in the evidence record were judged lower priority than clearing the
  word band and sentence-density warnings within a medium-effort round.
- All 16 sources are cited in first-citation order with `data-nb-kind`
  carried over exactly from the evidence record's own Kind label (14
  primary, 2 secondary — the AAP healthychildren.org restatement and the
  Guideline Central digest).
- The Idjradinata/treatment-anemia paragraph, the preterm-dosing sentence in
  the guideline section, and the exceptions list in the closing section each
  place the clinician-boundary language at the exact decision it bounds
  (diagnosis, dosing, preterm status), per the voice guide, rather than as a
  closing disclaimer.

## Open questions

None blocking. One editorial judgment call worth flagging for the editor: the
draft keeps the desk's "recently used, do not reuse" molds out of the
headline and dek (no relative/absolute single-clause pairing, no "in the
population X actually tested" opener), but reuses the underlying honesty
about effect size and population through a different construction (fractions
— "1 in 4" vs "roughly a quarter" — instead of the retired percentage-pair
shape). Worth a second read against the two prior pieces' actual sentences
if the editor wants to confirm the shape reads as sufficiently different, not
just differently worded.
