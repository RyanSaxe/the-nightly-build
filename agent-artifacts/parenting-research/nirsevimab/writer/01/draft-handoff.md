# Draft handoff — parenting-research/nirsevimab (writer, invocation 01)

Production: single-context, no isolation.
(The harness exposed no child-agent/subagent tool. Per PROTOCOL, the full
chain — writing-coach, researcher, writer, editor — was run by one context in
the required numbered sequence; every artifact is preserved. This is degraded
isolation, not a shortened chain.)

## Original-work sentence
The article takes the trials' headline relative-risk reductions (74–84%) and
re-expresses each as the absolute risk it is a ratio of and the number needed to
treat it implies for a *healthy term* infant (≈26 to prevent one
medically-attended RSV case; ≈100 for a hospitalization), then sets that against
the preterm baseline (NNT ≈15) and the either/or choice with the maternal
vaccine — a translation the sources report piecewise but never assemble for a
low-risk family's decision.

## Where the original work is visible
- Section "The same result in relative and absolute terms": the worked NNT
  arithmetic (5.0% − 1.2% = 3.8 points; 100/3.8 ≈ 26), the "The arithmetic" note,
  and the preterm contrast.
- Fig. 1 (chart-1): absolute risk per 100 with vs without nirsevimab across five
  trial endpoints, built from the registered counts — every bar short, which is
  the visual argument.
- Section "Where the evidence runs out": names MELODY's non-significant
  healthy-cohort hospitalization endpoint and the waning of the 90% real-world
  figure — the honest limits the relative headlines hide.
- Section "One route, not two": the nirsevimab-vs-maternal-vaccine choice stated
  as either/or, with the timing/eligibility/high-risk questions handed to the
  pediatrician.

## Files changed
- `library/parenting-research/nirsevimab.html` (authored from skeleton).
- `library/parenting-research/nirsevimab/chart-1.py` + `chart-1.png` (provenance
  committed; data are the registered trial counts).

## Proof result
`./nb check … --series parenting-research --repo . --library ../library`
→ **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Preview site builds; chart copies
and the figure renders. Four initial W-SENTENCE-DENSITY warnings were cleared by
splitting long sentences (orientation antibody sentence; the CDC-surveillance
sentence; the maternal preterm-signal sentence; the pediatrician-questions
sentence; the Griffin baseline sentence; the clinician's-call note).

## Meta
sources 10 (all primary: trial registries, CDC/ACIP MMWRs, CDC burden/HAN, AAP
HealthyChildren), words 1650 (measured body ≈1611), reading_minutes 8, mode open,
date 2026-07-30, harness claude-code, model claude-opus-4-8.

## Evidence/voice questions still open
- HARMONIE: registry posts 64 control events / 84.0% efficacy; the NEJM primary
  paper reports 60 / 83.2% (analysis-set difference). Article says "near 84%" and
  the table uses the registry counts; flagged for the editor as a knowing choice,
  not an error.
- NEJM/Lancet/Pediatrics full texts are gated (403); every trial count is cited
  to the ClinicalTrials.gov registered results that own it and was verified there.
  If the editor wants the NEJM DOIs named in prose (not as the linked source),
  that is a small addition available on request.
