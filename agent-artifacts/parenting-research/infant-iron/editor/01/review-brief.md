# Editor review-brief: parenting-research/infant-iron (01)

## Your job
Give this drafted evidence `article` the three ordered reads (skeptic, cut,
reader) and either approve it (`DONE editor`, no required change) or route
numbered repairs. Cuts/small fixes go directly; new prose past a word/clause
returns to the writer; evidence gaps to the researcher.

## Begin with these exact inputs
- This brief; `../../editorial-direction.md`; the exact writer brief
  `../../writer/01/brief.md` (prompt-leakage detection); voice guide
  `../../writing-coach/01/voice-guide.md` (read first); evidence record
  `../../researcher/01/evidence.md`; draft handoff `../../writer/01/draft-handoff.md`;
  article `/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html`;
  template context `../../../../.nb-context/`.

## What to check hardest (this article's risk surface)
- **The association-vs-trial spine, stated without overclaim.** Lozoff 1991 is
  observational (say so; cannot separate deficiency from its causes). The Chilean
  RCT must NOT be reported as unqualified "harm": it is mixed and baseline-
  dependent — cognitive/visual-motor harm in the *iron-replete* (high-Hb) subgroup
  (ES up to 0.85-1.36 at 10 yr, persisting at 16 yr), benefit in the low-Hb
  subgroup, AND a social-emotional *benefit* in the same trial (ES 0.14-0.36).
  Confirm all three directions are present and not collapsed into one.
- **The subgroup sign-flip chart** (chart-1.py/png): verify it was built only from
  the evidence record's verified series, keeps ALL THREE subgroups together
  (showing only the harm bars would misrepresent it), labels axes/effect sizes,
  and cites the source in the caption. Inspect the rendered image — labels,
  scale, and legend must be honest. Chart corrections return to the writer.
- **Numbers recomputed against the owning primary** (with CIs where they matter):
  the physiology (~80% iron accreted 3rd trimester, stores ~4-6 mo), Andersson
  cord-clamping (+45% ferritin, 0.6% vs 5.7%, NNT 20), the Chilean effect sizes,
  NHANES prevalence (1-2 yr iron deficiency 13.5%, IDA 2.7%). CONFIRM no
  first-year-specific prevalence number is asserted (none was verified); the "18%"
  DGA figure and the un-located 2003 Chilean paper's own numbers are ABSENT; the
  AAP 2026 report is attributed as read-via-secondary, not quoted as primary.
- **Guidance divergence** (AAP 2010→2026, USPSTF I-statement, WHO targeted, USDA
  "may not be advisable") stated as genuine disagreement, not smoothed. Confirm
  the comparison table (if present) is honest.
- **Care boundary**: the "see a clinician" boundary (preterm/LBW, suspected
  anemia, restrictive diet) reads as care advice stated plainly, and the science
  is not hedged into mush. Reported fact, estimate, and synthesis kept distinct.

## Standards to apply in the cut
Full house prose/punctuation floor. Compare opener, headings, and dek against the
recent parenting library (the striking relative-vs-absolute-number opener, the
effect-size headline, the "trials built to catch harm found none" shape,
comma-triad deks). Cut prompt leakage and self-grading.

## Output
Write `editorial-review.md` here with the three required lines, direct edits,
required work by owner, final decision. If you edit prose, note whether a re-proof
is needed
(`nb check .../infant-iron.html --series parenting-research --library /home/user/library`);
chart/asset/markup fixes return to the writer. Return `DONE editor <path>` only if
no redraft is required, else a `REQUEST writer/researcher <one-sentence>` line.
