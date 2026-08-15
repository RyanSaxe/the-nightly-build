# editor review-brief: build-from-scratch/flash-attention (editor/02)

Confirmation read after the sources-floor repair. In editor/01 you completed the
full three reads and approved the argument, the math, the code's numbers, and the
chart; the only open item was the source floor. Since then: writer/02 added five
sources (Vaswani, PyTorch SDPA docs, a GPU-microbenchmarking primary, Deep
Learning Sec 4.1 for safe-softmax, the flash-attention repo) at existing claim
sites, and writer/03 renumbered all nine sources into first-citation order.

Inputs (same as editor/01, plus):
- editor/01/editorial-review.md — your prior review
- researcher/02/evidence.md and researcher/03/evidence.md — the added sources and
  the scaled/unscaled trap flagged twice
- writer/02/draft-handoff.md and writer/03/draft-handoff.md
- the article: .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html

Write your review to: editor/02/editorial-review.md (do not overwrite editor/01)

Round's focus: confirm only what changed.
- Open each of the five new citations as printed and confirm each lands on a
  source that owns the claim it is attached to, and that data-nb-kind is honest.
- Confirm the scaled/unscaled trap is honored: Vaswani and the PyTorch docs are
  cited for the general attention shape, never on the article's own unscaled
  S = QK^T formula as though it implements the scaled Equation 1.
- Spot-check the renumber: superscripts, hrefs, and the Sources list are internally
  consistent and in first-citation order; nothing else changed; your editor/01
  edits still stand. If it holds, approve.
