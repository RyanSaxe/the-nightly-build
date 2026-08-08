# researcher brief: build-from-scratch/rotary-position-embeddings (01)

Inputs:
  ../../editorial-direction.md
  ../../commission.md
Output: researcher/01/evidence.md

Research questions (read the primary artifacts, not summaries of them):
- RoFormer (Su et al., 2021, arXiv:2104.09864): the exact RoPE construction —
  the 2-D rotation applied to query/key pairs, the frequency schedule
  `theta_i = 10000^(-2i/d)`, and the relative-position property they prove
  (`<R_m q, R_n k>` depends only on `n - m`). Capture the precise equations and
  where in the paper they appear (locators). Note what they claim empirically.
- The base/frequency constant (10000) and the half-split vs interleaved
  application convention, verified against a real reference implementation or a
  published open-weight model config (e.g. a Llama-family `rope_theta`). Record
  the exact address of the config/implementation.
- Context extension: the NTK-aware scaling primary write-up and/or YaRN
  (Peng et al., arXiv:2309.00071) — what single change to the frequencies
  extends usable context, and the honest claim about how far. Verify numbers
  against the primary.
- One or two authoritative statements of the problem RoPE solves (self-attention
  is permutation-equivariant / needs position injected) and the two prior
  families named for contrast (learned absolute; sinusoidal additive from
  "Attention Is All You Need"). Enough to cite, not a survey.

Deliver a "Numbers" section with any figures the code demonstration will state
(e.g. the base constant, dimensions, a decay example) traceable to their owner.
Source assets: name any figure from RoFormer/YaRN worth reproducing, or write
`None found` — the demonstration here is expected to be the article's own code
output, not a captured paper figure. min_sources 8. Contradictions: note any
dispute about why RoPE extrapolates (the community has competing explanations)
and record it honestly. Resolve every URL to the document's own page (arXiv abs
page, not a PDF endpoint).
