# Writer brief — parenting-research/nirsevimab (invocation 01)

## Inputs (begin here)
- `editorial-direction.md`; `commission.md`; this brief.
- `writing-coach/01/voice-guide.md` (reread before drafting).
- `researcher/01/evidence.md` (the complete claim set; use the Numbers table
  exactly; address the Contradictions).
- Initialized article: `library/parenting-research/nirsevimab.html`.
- Chart already rendered: `library/parenting-research/nirsevimab/chart-1.py` and
  `chart-1.png` (absolute risk with vs without nirsevimab, from verified counts).
- Template context under `.nb-context/` (article: words 1200–3000, flex 2–6,
  anchors orientation + sources, cite per-section).

## Outputs (write only these)
- The article HTML (edit in place; replace every placeholder/sample).
- `writer/01/draft-handoff.md`.

## The argument (name flex sections for THIS spine, not a generic outline)
evidence → strength → limits → the choice. Concretely:
1. orientation — what RSV does to a healthy infant, the baseline risk, and what
   nirsevimab is (a monoclonal antibody, one seasonal dose), before any claim.
2. what the three trials counted — MELODY (healthy term), Griffin (preterm),
   HARMONIE (hospitalization); endpoints and counts, precisely.
3. the same result in relative and absolute terms — the core contribution: ARR
   and a worked NNT; healthy-term vs preterm; the chart.
4. where the evidence runs out — MELODY hospitalization not significant in the
   healthy cohort; real-world 90% but wanes; mortality not demonstrable; supply.
5. one route, not two — nirsevimab vs maternal RSVpreF vaccine (either/or), and
   the timing/eligibility/high-risk questions that belong to the pediatrician.

## Hard requirements
- Every load-bearing number pairs a relative figure with its absolute twin and a
  denominator + window. Show the NNT arithmetic once.
- Report MELODY's non-significant healthy-cohort hospitalization endpoint
  honestly. Do not claim MELODY "proved" a hospitalization benefit in term
  infants; that comes from HARMONIE + surveillance.
- Make the nirsevimab-vs-maternal-vaccine choice explicit and state plainly the
  desk does not replace individual medical care; the choice and any risk-factor
  infant belong with a pediatrician.
- Headline: subject-verb-surprise, no colon subtitle, no Betteridge question.
  Dek: one lean sentence, no banned mold.
- Sources numbered in first-citation order; every `data-nb-kind` honest (all
  primary here); no invented locators. Preserve fixed head assets, body class,
  labels, Sources section.
- No active content. Furniture only from documented catalog; each with a clear
  purpose (planned: stat strip, trials table, chart figure, holds-up grid +
  one Verdict note, routes handling, clinician note).

## Proof (run to BLOCK: 0; treat WARN as revision notes)
    export PATH="/root/.local/bin:$PATH"
    ./nb check .nb-work/parenting-research/nirsevimab/library/parenting-research/nirsevimab.html \
      --series parenting-research --repo . --library ../library

## nb-meta actuals
protocol 1.1 · series parenting-research · slug nirsevimab · template article ·
mode open · order null · date 2026-07-30 · harness claude-code ·
model claude-opus-4-8 · tags [] ok · sources/words/reading_minutes measured.
