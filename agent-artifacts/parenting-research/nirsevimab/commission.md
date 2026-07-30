# Commission — parenting-research/nirsevimab

## Assignment
Explain the evidence on **nirsevimab (Beyfortus), the long-acting monoclonal
antibody against RSV**, for a healthy, term infant — framed for the household
following a child born **February 2026**, who faces the fall/winter 2026–27 RSV
season as the decision comes due. Answer three questions the desk always asks:
what does the evidence establish, how strongly, and what can it not establish?

## What the evidence must cover (read the trials themselves)
- Efficacy RCTs: Hammitt et al., **MELODY** (NEJM 2022) in late-preterm/term
  infants; Griffin et al. (Phase 2b, NEJM 2020); **HARMONIE** (Drysdale et al.,
  NEJM 2023) pragmatic trial for hospitalization. Report endpoints precisely:
  medically-attended RSV LRTI vs. hospitalization vs. very-severe disease.
- Give **absolute** risk reduction and number-needed-to-treat alongside the
  headline relative-risk figures; a season's baseline hospitalization risk for a
  healthy term infant is the comparison the reader needs.
- Real-world effectiveness (2023–24, 2024–25 seasons): CDC/MMWR and national
  studies; contrast with RCT conditions.
- Recommendations and their basis: AAP and CDC/ACIP infant RSV guidance, and the
  maternal RSV vaccine (Abrysvo) as the alternative route — one or the other,
  not both — so the family understands the actual choice.
- Limits: mortality is not demonstrable in high-income settings (already very
  low), long-term outcomes, supply/access and cost history, and that healthy
  term infants have lower baseline risk than the preterm/high-risk groups where
  benefit is largest.

## Reader / register / safety
House reader, but written so any well-read parent could be handed it. Calm,
precise, evidence-first. End with what the evidence might change at home and
where the decision is a clinician's: **state plainly the desk does not replace
individual medical care; the nirsevimab-vs-maternal-vaccine choice and any
infant with risk factors belong with a pediatrician.**

## Mode / template / geometry
- mode `open` · template `article` · order null.
- words 1200–3000; flex_sections 2–6, each cited; anchors orientation, sources.
- Name flex sections for this argument (evidence → strength → limits →
  what-it-changes), not a generic outline.

## Source obligations
- min_sources 8. Primary = the trial papers, the guidance documents (AAP/CDC),
  and datasets that own each number. Read the primary; verify secondary numbers
  against it. Record primary/secondary kind + locator per citation. A paywall/
  403 is gated, not dead — do not record an unverified URL.

## Prevent repetition (recent parenting-research)
Off-limits subjects and their shapes: sleep-training (2026-07-28), early-
allergen-introduction (2026-07-26), starting-solids (2026-07-23). All three lean
on a "the trial built to catch X measured Y, in the infants it actually tested"
move — do not inherit that exact opener/spine as a template even though the
"who was actually studied" discipline is the desk's method. Fresh opener and
section shapes. No colon-subtitle, no Betteridge question headline.

## Tonight's neighbors (avoid collision)
boeing, current-events, tech-news, paper-of-the-day (knowledge-distillation),
word-of-the-day (bowdlerize). This is the only health/parenting piece tonight.

## Output paths
- Article: `.nb-work/parenting-research/nirsevimab/library/parenting-research/nirsevimab.html`
- Artifacts: `.nb-work/parenting-research/nirsevimab/agent-artifacts/parenting-research/nirsevimab/`

## Runtime for nb-meta
harness `claude-code` · writer `claude-opus-4-8` (capable, high) · editor
inherited `claude-opus-4-8`, high, required.

## Required contribution
The reader can distinguish a large relative-risk reduction from a small absolute
one for a healthy term infant, understand the single real choice (nirsevimab vs.
maternal vaccine), and know exactly which parts are a clinician's call. A chart
(absolute risk with vs. without, or NNT) is welcome only if built from verified
trial numbers via `nb chart`.
