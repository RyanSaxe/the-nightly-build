# Writer brief — paper-of-the-day/knowledge-distillation (01)

## Your task
Draft the article into the initialized skeleton, then carry it to `BLOCK: 0`.
Record the original-work sentence and proof result in `draft-handoff.md`.

## Exact inputs
- `editorial-direction.md` (governing stack).
- `writing-coach/01/voice-guide.md` — reread before drafting.
- `researcher/01/evidence.md` — the complete claim set. Do not add claims it
  does not contain; request new evidence if you hit a hole.
- The initialized article:
  `library/paper-of-the-day/knowledge-distillation.html`.
- Template context under `.nb-context/` (paper contract; furniture catalogs:
  engine base + press shared + paper-template `nb-paper-card`).
- This brief.

## Outputs (only these)
- `library/paper-of-the-day/knowledge-distillation.html`
- chart provenance + PNG under `library/paper-of-the-day/knowledge-distillation/`
  if you build the chart.
- `writer/01/draft-handoff.md`.

## Shape (paper template: anchors abstract + orientation + sources; 2–8 flex)
- **abstract** (anchor): `nb-paper-card` with the real title, authors, "NIPS
  2014 Deep Learning Workshop · arXiv:1503.02531 · 2015", link to
  https://arxiv.org/abs/1503.02531, and the verbatim abstract from evidence [S1],
  cited [1].
- **orientation** (anchor): the deployment problem (ensembles/large nets too
  costly to serve) and the reframing of "knowledge" as a learned input→output
  mapping, not the weights; one-sentence shape of the answer. Cite [1].
- **flex** (name each in the piece's own nouns; each cited): reconstruct
  (1) dark knowledge / relative probabilities of wrong classes; (2) the
  temperature softmax — use the KaTeX equation furniture for Eq. (1), and the
  two-objective training with 1/T^2 scaling; fold in "matching logits is a
  special case"; (3) what the mechanism buys — MNIST 67/146/74, the omitted-3
  result, the speech Table 1 (rebuild as `nb-table`), soft-targets-as-regularizer;
  then turn to the review: (4) the fidelity measurement — Stanton's
  fidelity-vs-generalization split, LeNet 99% vs ResNet mid-80s%, the
  optimization diagnosis; (5) the verdict — DistilBERT/Beyer successes, Müller's
  label-smoothing caveat, Born-Again reframed, and a `Verdict` note
  (`nb-note-strong`, at most one) landing when distillation moves a distribution
  vs merely a smaller working model. Merge or resplit as the argument needs; keep
  it a continuous article, not a stack of blocks.
- **sources** (anchor): number in first-citation order. Expected order given the
  draft plan: [1] Hinton S1, [2] Stanton S2, then the follow-ons as first cited
  (likely [3] DistilBERT S3, [4] Born-Again S4, [5] Müller S5, [6] Beyer S8,
  [7] Ba & Caruana S7, [8] Buciluǎ S6) — renumber to match your actual citation
  order. All eight are `data-nb-kind="primary"` per the evidence record.

## Furniture guidance
- One annotated KaTeX equation at most (the temperature softmax is the natural
  choice — color T and the logits). A second bare/│captioned equation for the
  logit-matching limit is fine if it carries reasoning.
- The speech results are a clean `nb-table` (3 rows). A soft-vs-hard contrast can
  ride in prose or a small table — your call, only if it carries reasoning.
- One `nb chart`: test top-1 agreement across settings (evidence "CANDIDATE
  CHART SERIES"). Build only from verified numbers; label axes; cite [2] with
  locators; inspect the PNG.
- At most one pull quote; at most one `nb-note-strong` Verdict.
- Add `data-nb-locator` / `data-nb-note` only where the evidence supplies it
  (it supplies page/section/figure locators and verbatim quotes for the turning
  points — use them on the cites that carry the argument).

## Decisions reserved to you
- Headline (NO colon subtitle; state the finding, actors named) and dek (one
  sentence, a claim about the world, none of the banned molds). The commission's
  required contribution: the reader leaves knowing when distillation transfers a
  distribution vs merely a smaller working model, and why the 2015 intuition and
  the 2021 measurement disagree.
- Section names and order; where each equation/table/chart lands.

## Constraints
- Word band 1800–3400. Keep fixed engine assets, `<body class="nb-article">`,
  the `<h2>Sources</h2>` label, and required HTML exactly.
- No active content; no external images; charts only via `nb chart`.
- Fill `nb-meta` with actual values: title, dek, tags (array; [] ok), measured
  sources and words, reading_minutes, date "2026-07-30", harness "claude-code",
  model "claude-opus-4-8", protocol "1.1", series "paper-of-the-day", slug
  "knowledge-distillation", template "paper", mode "open", order null.

## Proof (run to BLOCK: 0; clear WARN you can)
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/paper-of-the-day/knowledge-distillation/library/paper-of-the-day/knowledge-distillation.html --series paper-of-the-day --repo . --library ../library

## Return
`DONE writer <draft-handoff-path>` after BLOCK: 0, or a `REQUEST …`.
