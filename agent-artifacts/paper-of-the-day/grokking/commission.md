# Commission — paper-of-the-day/grokking

## Assignment
One Paper of the Day on the `paper` template (1800–3400 words). Focal paper:
**"Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets,"
Power, Burda, Edwards, Babuschkin, Misra (OpenAI), arXiv:2201.02177, 2022.**

## Angle
Grokking is the delayed-generalization result everyone can restate and few can
explain: a small transformer memorizes a modular-arithmetic table to 100%
training accuracy, sits at chance on held-out data for tens of thousands of
optimizer steps, then abruptly generalizes. Reconstruct the exact claim and,
crucially, weigh it against the public record it produced. The paper reported a
phenomenon without a mechanism; the article's contribution is to separate what
the 2022 paper actually established (the phenomenon, its dependence on
regularization/weight decay and dataset fraction) from what later work
supplied — Nanda et al.'s 2023 mechanistic account (the network learns modular
addition as rotation via discrete Fourier components; training splits into
memorization, circuit formation, cleanup) and the 2024–2026 line arguing
grokking is fragile, conditional, and tied to weight decay and numerical
regime. Land a reviewer's verdict: what the original measured, where the claim
stops, and what the after-record settled and left open.

## Intended reader
House reader (math/CS, ML-eng). Assume comfort with SGD, transformers, train/val
curves, weight decay, and modular arithmetic. Define grokking-specific terms
(the modular-addition task setup, "progress measures," the memorize→generalize
phases) at first use. Teach by rebuilding, not by summarizing the abstract.

## Contribution (what this piece adds beyond its sources)
A clean separation of phenomenon from mechanism: the 2022 paper is a careful
demonstration with no explanation, and reading it *through* Nanda's reverse-
engineering and the later fragility results is what makes the claim usable. The
reader should leave knowing what grokking is, what actually causes it on the
modular-addition task, and how much of the original's framing survived scrutiny.

## Source obligations
- Template `paper`, min_sources 8. The focal paper owns its claims; another
  source earns a slot only when it changes the interpretation.
- The `abstract` section must carry the paper card with the abstract **verbatim**
  from arXiv, authors, venue/ID, year, and a working link. Researcher supplies
  exact text.
- Cite, having read them: the focal paper (2201.02177); Nanda et al. "Progress
  measures for grokking via mechanistic interpretability" (ICLR 2023); at least
  one follow-on that changes interpretation (e.g., Liu et al. "Omnigrok"; a
  2024–2026 fragility/weight-decay/edge-of-numerical-stability paper). Verify
  every figure/claim against the paper that owns it; primary = the paper making
  the claim.
- Anchor turning-point claims on the citation itself via `data-nb-locator` /
  `data-nb-note` where a section/figure number pins the claim.

## Furniture guidance
Reconstruct with an equation where it clarifies (modular addition a+b mod p; the
Fourier/rotation formulation) and a worked example (p = 113 modular addition).
Do **not** fabricate a grokking accuracy curve: a chart is allowed only from
real, transcribed, cited data points via `nb chart` with committed provenance;
otherwise describe the curve precisely in prose. Furniture carries reasoning,
never decoration.

## Relevant prior coverage / habits not to inherit
Recent Paper of the Day covered surprising-curve results heavily (emergent
abilities, chain-of-thought, chinchilla, double-descent-adjacent). Do NOT frame
grokking as "another surprising curve" or reuse the "rescoring/replotting turns
X into Y" opener from the emergent-abilities piece (2026-07-31). The distinct
hook here is phenomenon-without-mechanism and what the after-record supplied.
Avoid colon-subtitle headlines and the "a single X breaks Y" opener used by the
adam-optimizer piece. Vary section shapes.

## Neighboring articles tonight (edition cohesion)
Tonight also runs build-from-scratch on speculative decoding (a systems/
inference piece) and word-of-the-day/zugzwang. Keep this piece in the
optimization/generalization lane; no forced ties. Do not overlap with the
speculative-decoding piece's territory.

## Output paths
- Article: `.nb-work/paper-of-the-day/grokking/library/paper-of-the-day/grokking.html`
- Role artifacts under `agent-artifacts/paper-of-the-day/grokking/`

## Harness / model
- harness: `claude-code`
- writer runtime recorded in nb-meta: `claude-sonnet-5` (capable tier, medium effort)
- editor: opus tier, high effort (required)
