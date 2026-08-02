# Writer handoff: parenting-research/infant-iron (02) — dek precision fix

## What changed

Only the dek, in both required places, plus the `nb-meta` `words` count
(the editor's four direct body cuts had already lowered it; this pass just
re-measures and records the true number). Nothing else in the article was
touched.

**Old dek (conflated two findings):**
> The same trial's ten- and sixteen-year follow-ups found the fortified
> group scored worse on cognitive and visual-motor tests and better on
> adaptive behavior, a split that tracks how much iron each baby already
> had at six months.

**New dek:**
> Baseline iron status splits the cognitive and visual-motor scores, a
> pattern that held at sixteen years, while a separate ten-year analysis
> found the same infants had better adaptive behavior across the whole
> group, not broken out by baseline status.

## Why the new dek is precise

Checked against the evidence record (sources 6-8 in the article's own
numbering: s6 = Lozoff 2012, 10-yr cognitive/visual-motor; s7 = East 2023,
16-yr; s8 = Lozoff 2014, 10-yr adaptive behavior):

- **Adaptive-behavior benefit is now pinned to the ten-year analysis only.**
  The old dek's "ten- and sixteen-year follow-ups ... better on adaptive
  behavior" attributed the benefit to both timepoints. The new dek states
  the adaptive-behavior finding as "a separate ten-year analysis," matching
  s8 (Lozoff 2014), which the article body already cites correctly for
  this claim and only this claim.
- **The sixteen-year follow-up is now described as extending the cognitive
  pattern, not the adaptive one.** The new dek's "a pattern that held at
  sixteen years" refers back to the cognitive/visual-motor split, matching
  s7 (East 2023), which measured visual-motor integration and quantitative
  reasoning only, never adaptive behavior. The article body already scopes
  this correctly (`the-trial` section); the dek now agrees with it.
- **Baseline-hemoglobin dependence is no longer assigned to the
  cognitive-vs-adaptive domain split.** The old dek's closing clause, "a
  split that tracks how much iron each baby already had," read as covering
  both outcome domains. The new dek confines the baseline-status language
  to the cognitive/visual-motor sentence and explicitly says the
  adaptive-behavior finding held "across the whole group, not broken out by
  baseline status" — the sign-flip by baseline Hb (s6) is a separate axis
  from the cognitive-vs-adaptive domain split, and the dek now keeps them
  separate the way the body already does.

No new claims were introduced; every fact in the new dek was already
stated, correctly scoped, in the article body before this revision.

## Editor's direct edits preserved

Confirmed all four of the editor's cuts are intact and untouched: the
"Both rates run roughly triple" → "The iron-deficiency rate runs roughly
triple" narrowing (orientation), the cut trial-section closer ("The same
formula, the same trial, the same follow-up..."), the cut "a decade after
the ten-year data showed the same pattern" clause, and the cut
self-referential starting-solids sentence in what-changes-at-home. The
sign-flip chart, the Verdict note, the guidance table, all 15 sources and
their `data-nb-kind` labels, and every other settled sentence are
unchanged.

## Proof result

`/home/user/the-nightly-build/nb check
/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html
--series parenting-research --library /home/user/library` → **BLOCK: 0,
WARN: 0**, verdict PUBLISHABLE.

`nb-meta` `words` updated from 2875 to 2821 (measured via the article
parser after the editor's cuts and the dek rewrite); `reading_minutes`
unchanged at 14 (2821/200 rounds the same as before); `sources` unchanged
at 15. The dek now matches exactly between `nb-meta` and the rendered
`<p class="nb-dekline">`.

## Remaining questions

None. This was a display-text-only fix; no researcher gap.
