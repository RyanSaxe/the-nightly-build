# Editorial review: paper-of-the-day/flash-attention (editor 01)

Decision: **APPROVED**. Direct edits only; no writer round needed.

Proof: `BLOCK: 0 / WARN: 2 / PUBLISHABLE`. Both warnings are W-SENTENCE-DENSITY on
the verbatim abstract — its capabilities sentence (48 words, Path-X/Path-256
parentheticals) and its speedup sentence (45 words, the 15%/3x/2.4x figures).
Neither can be split without misquoting, and no other sentence in the piece
trips the heuristic. Both figure assets validate (asset-1.png, asset-2.png).

## Correctness of the reconstruction

- **Online-softmax recurrence.** The running max, running normalizer, and
  output-accumulator rescaling match Algorithm 1 (lines 10-12) and the evidence
  record. The annotated equation's three terms are correct: renormalize by the
  updated normalizer; un-normalize the old accumulator and re-anchor it to the
  new max; add the new block's values weighted at the new max. Terms (m_i, l_i,
  m~_ij, l~_ij) are defined in the sentence before the equation. Sound.
- **IO cost.** Theta(Nd + N^2) vs Theta(N^2 d^2 / M) matches Theorem 2, and the
  ratio ~M/d^2 is stated correctly. Figure 2's numbers are faithful: GFLOPs
  66.6 -> 75.2, HBM 40.3 -> 4.4 GB (~9x), runtime 41.7 -> 7.3 ms (~5.7x). The
  dek's "ninefold" and the caption's "nine times less / 5.7 times faster" are
  right, and each caption says what its figure settles.
- **Exactness framing.** Fixed two overclaims. The piece asserted the output was
  "bit-for-bit the same function" and recovered the speedup "without changing a
  single output value." Both claim numerical bit-identity, which is stronger
  than the paper's "exact" (the algorithm computes the exact softmax attention;
  floating-point reduction order still differs). Reworded to the exact-not-
  approximate claim the paper actually earns.
- **After-record.** FA-2's work-partitioning/occupancy fix (~2x, 50-73% of A100
  peak), FA-3's Hopper asynchrony and FP8 (~75% H100 util, ~1.2 PFLOPs/s), the
  PyTorch SDPA default, and the exact-vs-approximate placement (Linformer/
  Reformer approximate to cut complexity; FlashAttention is exact and IO-bound,
  no lower asymptotic compute) all check against the evidence and are not
  overclaimed.

## Edits made

- Dek (meta + dekline): "keeping the attention matrix in on-chip SRAM" implied
  the N x N matrix is held whole. Changed to "computing the attention matrix in
  on-chip SRAM one block at a time," which matches the headline and the body's
  care that the matrix is never materialized.
- Fig. 1 caption: 20 MB against 40 GB is ~2000x, not "a thousand times smaller";
  changed to "thousands of times smaller."
- Online-softmax closer: removed the "bit-for-bit" overclaim and the comma
  splice; restated as exact softmax attention computed in a different order.
- After section: replaced the alliterative "compose rather than compete" tail
  with the concrete fact it was gesturing at — the paper's block-sparse variant
  is an approximate method built on the same IO-aware tiling.
- Verdict: "without changing a single output value" -> "without approximating
  the attention it computes."

## Molds and slop

Compared against the recent paper-of-the-day record. The piece breaks the molds
the brief named: it opens on the memory-IO bottleneck rather than a baseline-to-
overturn lede; it carries a single Verdict note, not the holds-up grid plus
verdict that DPO and PPO both close on; it avoids the "no later work overturns"
tic and the "got X right / Y wrong" concession dek; headings are argument steps
in the paper's nouns with no semicolon-contrast or wh-clause forms. Section edges
read clean after the edits above.
