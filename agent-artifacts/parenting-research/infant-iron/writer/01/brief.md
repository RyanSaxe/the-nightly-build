# Writer brief: parenting-research/infant-iron (01)

## Your job
Draft the evidence `article` on infant iron at ~six months (1200-3000 words),
then prove it to `BLOCK: 0`. Draft only from the evidence record and voice guide.
Do original analysis (weigh the evidence); do not summarize guidelines.

## Begin with these exact inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set and
  its caveats — obey every one).
- Initialized article:
  `/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html`
  (edit; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (article geometry: orientation
  anchor + 2-6 flex sections, per-section citation; furniture catalogs).

## The argument to build (all verified in the evidence record)
The spine is the tension between **association** and **trial** evidence.
1. **Why six months / the physiology** (well-established): ~80% of a term baby's
   iron is accreted in the third trimester; stores last ~4-6 months; breast milk
   is iron-poor; formula is fortified (so exclusively breastfed infants are the
   group of concern). Delayed cord clamping raised 4-month ferritin ~45% and cut
   iron deficiency (Andersson 2011: 0.6% vs 5.7%, NNT 20) — an earlier lever that
   changes the starting point.
2. **The association** (Lozoff 1991, NEJM — observational cohort): infants with
   moderate/severe IDA scored lower years later, even after SES adjustment. State
   plainly it is observational: it cannot separate "iron deficiency causes worse
   outcomes" from "what caused the deficiency (poverty, nutrition, environment)
   also caused them."
3. **The trials** (the reversal): the Chilean RCT (Lozoff 2012 10-yr / East 2023
   16-yr) randomized 6-month-olds to iron-fortified vs low-iron formula. In
   infants already **iron-replete** at 6 months, supplementation was associated
   with *lower* cognitive/visual-motor scores (high-Hb subgroup 10-yr effect sizes
   0.85-1.36, persisting at 16 yr), while **low-Hb** infants benefited (ES
   0.22-0.36). CRUCIAL honesty (evidence Contradiction #2): the SAME trial found
   the supplemented group had *better* social-emotional/adaptive behavior (ES
   0.14-0.36). Do NOT report the Chilean trial as unqualified "harm" — it is a
   mixed, domain-dependent, baseline-status-dependent pattern; the
   cognitive/visual-motor harm signal is the larger and the one that replicated.
   For infants who already have IDA, the Cochrane review (Wang 2013) found no
   clear short-term cognitive benefit from treatment (different population — say
   so).
4. **Why the guidance disagrees**: AAP 2010 (universal 12-mo screen; 1 mg/kg/day
   from 4 mo) → AAP 2026 (feeding-stratified screening: breastfed 9-12 mo,
   formula-fed 15-18 mo; supplement by 4 mo or optionally delay to 6 mo when
   iron-rich foods start). USPSTF's 2015 "I statement": evidence *insufficient* to
   judge screening 6-24 mo at all. WHO: *targeted* supplementation for higher-risk
   (preterm/LBW) infants, and even iron-fortified early complementary foods don't
   reliably prevent IDA in high-risk populations. USDA DGA: "routine iron
   supplementation of all breastfed infants may not be advisable." These bodies
   disagree about whether to screen and whether to supplement universally — name
   the disagreement, don't paper over it.
5. **What it might change at home** (the close): iron-rich complementary foods
   from ~6 months (meat/fish/egg, iron-fortified cereal) as the mainstream,
   lower-risk lever; the household's actual decision. Boundary, stated plainly
   (not hedged): a preterm or low-birth-weight baby, suspected anemia, or a
   restrictive diet is a clinician's call; this desk explains research and does
   not replace individual medical care.

## Caveats from the evidence record (obey)
- AAP 2026 report was read via secondary quotation (primary gated); its figures
  are corroborated across two independent secondaries + AAP's own consumer arm —
  reliable, but attribute carefully and do not quote a primary passage you cannot
  cite as read.
- No verified US prevalence figure specific to <12 months exists — do NOT state a
  first-year-specific prevalence number. Use NHANES 1-2 yr (Gupta 2016: iron
  deficiency 13.5%, IDA 2.7%) and note the age-band gap. If you use the FITS
  intake-adequacy numbers, label them as dietary-intake-below-EAR, not biomarker
  prevalence. Do NOT use the unverified "18%" DGA figure or the un-located 2003
  Chilean paper's own numbers (cite the 2012/2023 follow-ups instead).

## Furniture (plan with the prose)
Strong chart candidate: the Lozoff 2012 subgroup **sign-flip** (harm in the
high-Hb subgroup, benefit in the low-Hb subgroup, small whole-sample effect) —
this carries the article's central finding. If you build it with `nb chart`, use
only the evidence record's verified series, KEEP ALL THREE subgroups together
(showing only the harm bars would misrepresent it), label axes/effect sizes, and
cite the source in the caption; inspect the rendered image. A "who recommends
what, by age" comparison table for the guidance divergence is also well-justified.
No decoration; no article-authored scripts/styles/iframes/forms/external images.

## Universal rules
Minimum 8 sources; per-section citation; carry evidence-record kinds into
`data-nb-kind` (trials/reviews/guideline documents = primary for their own
claims; news/explainers = secondary). Number sources in first-citation order; add
`data-nb-locator`/`data-nb-url` only where supplied. Keep reported fact, estimate,
and synthesis distinct; give every number a comparison and a CI where it matters.
Fill `nb-meta`: series parenting-research, slug infant-iron, template article,
mode open, order null, date 2026-08-02, tags (accurate, e.g.
["nutrition","infant-health","evidence"]), measured sources/words, a real dek (a
stance true to the association-vs-trial tension, not an effect-size hook or
comma-triad), harness "claude-code", model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html --series parenting-research --library /home/user/library`
Treat warnings as revision notes. Use `nb preview` if you add a chart/table and
inspect the render.

Write `draft-handoff.md` here: original-work sentence, paths changed, proof
result and warnings left, any remaining evidence/voice questions. Return
`DONE writer <path>` after `BLOCK: 0`, or a REQUEST/BLOCKED line.
