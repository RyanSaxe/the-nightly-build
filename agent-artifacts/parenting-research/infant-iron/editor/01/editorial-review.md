# Editorial review: parenting-research/infant-iron (01)

## Three required reads

**Skeptic:** thesis "the *sign* of iron-fortified formula's effect on a healthy
six-month-old flips with baseline hemoglobin status (and with the outcome domain
measured); the association evidence cannot establish cause, the one RCT that
tests the reverse question shows a mixed, baseline-dependent pattern, and that is
why the guidance bodies genuinely disagree." Tested the four load-bearing claims
(physiology/why-six-months; Lozoff 1991 as observational-only; the Chilean
subgroup sign-flip with its social-emotional counter-finding; the guidance
divergence). Broke: one display-text claim — the **dek** (see writer request).
Everything else held on recomputation.

- Numbers recomputed against the owning primary and all match the evidence
  record: ~80% iron accreted in the third trimester (s1); Andersson cord-clamping
  +45% ferritin, 117 vs 81 µg/L, CI folded into prose as 23-71% at P<0.001, ID
  0.6% (1) vs 5.7% (10), NNT 20 (s2); NHANES 1-2 yr iron deficiency 13.5% (CI
  9.8-17.2, n=643) and IDA 2.7% (CI 1.2-4.2) (s3); Chilean whole-sample 1.4-4.6
  pts lower / ES 0.13-0.21, high-Hb (>12.8) 10.7-19.3 pts lower / ES 0.85-1.36,
  low-Hb (<10.5) 2.6-4.5 pts higher / ES 0.22-0.36 (s6); 16-yr N=562, d 0.16-0.26
  (s7); adaptive-behavior benefit ES 0.14-0.36, all P<0.05 (s8); Cochrane MDI CI
  -1.3 to +3.4 (s9); USPSTF I-statement and the AHRQ Bayley 0.6-0.7/0.2-0.7 and
  Griffiths 5.4-pt figures (s11, s12).
- Association-vs-trial spine is stated without overclaim. Lozoff 1991 is labeled
  observational and its confound named; the Chilean RCT is labeled a within-trial
  subgroup finding "suggestive of a dose-by-status relationship, not proof," never
  unqualified harm; all three directions are present (high-Hb cognitive harm,
  low-Hb cognitive benefit, whole-sample social-emotional benefit). The Verdict
  note weighs the two cognitive-vs-adaptive findings against each other rather
  than picking one.
- `data-nb-kind` audit: all 15 labels match the evidence record's own
  classification. The lone secondary (s13, the USDA DGA finding via its PMC
  explainer) is correctly marked; AAP 2026 (s10) is attributed "via Guideline
  Central" as read-through-secondary, consistent with the record's flagged access
  gap.
- Excluded material confirmed absent: no first-year-specific prevalence number is
  asserted (the orientation section states the <12-mo gap plainly); the unverified
  "18%" DGA figure, the FITS intake numbers, and the un-located 2003 Chilean
  paper's own numbers do not appear; 835/design and the harm signal are pinned to
  the 2012 and 2023 follow-ups (s6, s7) as directed.

**Cut:** 4 sentences/clauses removed (~40 words). Worst tell: the self-referential
newsroom signpost "This desk's earlier piece on starting solids settled the
six-month timing question; this one is about what gets added to the plate, not
when" — narrates the paper and grades the article's own scope; cut whole.

**Reader:** this gives me a working frame for *why* "more iron is better" is wrong
for an already-replete infant, why five guidance bodies split, and a concrete,
honest at-home line — with the genuinely original distinction that the Chilean
trial randomized a measured *formula dose*, not food, so its harm signal does not
transfer to iron-rich first foods. Both this answer and the draft-handoff's
original-work sentence survive; the prose reads to the voice-guide exemplars
(association-vs-cause, hold two true numbers apart), not a median summary. The
headline reads as an honest, subgroup-specific claim the body defends.

## Chart (Fig. 1) inspected

Provenance (`chart-1.py`) and the rendered PNG both check out and need no
correction: built only from the evidence record's verified series, all three
subgroups kept together, honest zero line and un-truncated linear scale (-22 to
8) that shows the sign flip, both axes labeled, effect sizes annotated per bar,
colors assigned by direction, source cited in the caption. Values match the
record exactly (whole -4.6..-1.4, high-Hb -19.3..-10.7, low-Hb +2.6..+4.5).

## Direct edits made (prose/structure only)

1. Orientation: "Both rates run roughly triple..." → "The iron-deficiency rate
   runs roughly triple..." — the IDA point estimate at ages 3-5 is suppressed for
   imprecision in the owning primary (s3), so only the iron-deficiency rate has a
   verifiable ~3x comparator.
2. Trial section: cut the redundant closer "The same formula, the same trial, the
   same follow-up: it helped the infants who needed iron and set back the infants
   who didn't." — restates the two sentences before it and duplicates the "same
   X, same Y, same Z" shape reused two paragraphs later; delete test lost no fact.
3. Trial section: cut "a decade after the ten-year data showed the same pattern"
   from the 16-year sentence — imprecise (16 yr is 6 years past the 10-yr
   assessment) and adds no fact beyond "performed worst overall."
4. What-changes-at-home: cut the self-referential "This desk's earlier piece on
   starting solids..." sentence (newsroom narration + scope self-grading).

## Required work by owner

**Writer — the dek (publication-blocking, display text).** Current dek: "The same
trial's ten- and sixteen-year follow-ups found the fortified group scored worse on
cognitive and visual-motor tests and better on adaptive behavior, a split that
tracks how much iron each baby already had at six months." Two problems:
(a) it attributes the adaptive-behavior *benefit* to both the ten- and
sixteen-year follow-ups, but that benefit is a 10-year finding only (s8); the
16-year study (s7) measured neurocognitive outcomes and did not report adaptive
behavior; (b) it pins the cognitive-vs-adaptive *domain* split to baseline iron
status ("a split that tracks how much iron each baby already had"), but what
tracks baseline hemoglobin is the cognitive sign-flip within the high-/low-Hb
subgroups (s6); the adaptive-behavior benefit (s8) is reported across the
supplemented group, not split by baseline Hb. Rewrite the dek so the 10-yr
adaptive finding is not attributed to the 16-yr follow-up and the baseline-status
dependence is not misassigned to the domain split. Fix is past a clause and lives
in display text, so it returns to the writer, not the editor.

**Re-proof required.** My four cuts changed the body (~40 words); `nb-meta`
`words` (2875) is now slightly high. The writer should recompute it and re-run
`nb check .../infant-iron.html --series parenting-research --library
/home/user/library` to BLOCK:0 after fixing the dek (the dek also lives in both
`nb-meta` and the `<p class="nb-dekline">` and must match in both places).

No researcher gap: the evidence record fully supports a correct dek.

## Decision

Not approved this pass. One publication-blocking writer fix (the dek) plus a
re-proof. Everything else — spine, numbers, kinds, chart, excluded figures,
prose floor — passes after the four direct edits above.
