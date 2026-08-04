# Draft handoff: paper-of-the-day/generative-adversarial-networks (01)

## Original work

The piece separates the paper's two distinct, self-declared limits — Prop. 2's
function-space / optimal-inner-loop assumption and Section 3's swap to the
non-saturating loss — and shows the after-record's famous "JS gives a vanishing
gradient" line indicts only the minimax loss the paper set aside, while the loss
GANs were actually trained on is diagnosed by a separate result (an unstable,
infinite-variance gradient on KL − 2·JSD); the evidence supplies both halves,
but no single source foregrounds which after-record theorem indicts which loss.

Visible in the "Where the generator's gradient goes" section, whose last two
paragraphs draw the vanishing-vs-unstable distinction explicitly and tie both
flaws to the same disjoint-support fact, and it is the hinge the headline, dek,
and verdict all turn on.

## Proof result

`./nb check … --series paper-of-the-day --library <checkout>` (links included):
**BLOCK: 0, WARN: 4, PUBLISHABLE.**

All four warnings are W-SENTENCE-DENSITY on 40–41-word sentences with at most one
clause join, left intentionally: each is a single controlled thought (the
minimax-substitution setup, the Prop. 2 assumptions, the Earth-Mover topology
claim, one caption) set against short sentences on either side, which the house
standard admits as craft. The denser 49–70-word sentences and both 2-clause-join
sentences flagged in the first pass were split. Links all resolve; banned-term
counts are zero (em-dash 0, mechanism 0, leverage 0, load-bearing 0).

Display-text self-test passed: every date, number, name, and title in headline,
dek, and subheads checked against evidence (−log 4, D* = 1/2, JS = log 2,
M·ε/(1−ε), Parzen 225 ± 2 / 2057 ± 26, DCGAN ~18 months); each claim attributed
to its owner (instability to Arjovsky & Bottou, EM fix to WGAN, mode collapse to
Salimans, "overly restrictive" to Fedus); headline carries no colon subtitle and
no eponym open, dek is not a comma-triad, neither reuses a recent paper-of-the-day
mold; nb-meta `dek` is byte-identical to the rendered dekline.

## Open questions

None blocking. Two notes for the editor:

- No Chrome was available in this environment, so `nb render-check` skipped the
  in-browser probe. KaTeX rendering was instead confirmed structurally: nb.js
  typesets `.nb-math-eq`, `.nb-math-in`, and `.nb-math-term`, and every TeX
  string uses only KaTeX-supported commands (the annotated equation's `\htmlClass`
  is the one trusted command the runtime enables). The three captured assets were
  inspected as images and are correct (Fig. 1 four-panel schematic, Algorithm 1
  box with the k = 1 header line, MNIST panel with its nearest-neighbor column).
- Article figure numbering is sequential (Fig. 1 schematic, Fig. 2 Algorithm 1,
  Fig. 3 MNIST samples); each caption still cites the paper's own locator
  ("Algorithm 1 · §3", "Fig. 2 · §5"), so the renumbering is transparent, not a
  mismatch.
