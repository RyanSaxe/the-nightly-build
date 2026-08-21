# Writer brief: paper-of-the-day/flash-attention

## Shape
Template paper, 1800-3400 words. Abstract card + paper link up front, verbatim
abstract. Orientation plus four flex sections, each cited, the last landing the
verdict. Sources last.

## Section plan (argument-step headings in the paper's nouns)
1. **orientation** — "Where attention spends its time." Open on the memory-IO
   bottleneck: the GPU finishes the matmuls fast and waits on HBM. SRAM ~13x the
   bandwidth of HBM and tiny. Standard attention round-trips the N x N matrix
   (S = QK^T, softmax, PV) through HBM three times. No baseline-to-overturn lede.
2. **tiling** — "The matrix that never gets written." Keep K/V and Q blocks in
   SRAM, compute each block of the attention matrix on-chip, write only the
   output O. Figure 1 (asset-1). Define materializing, tiling.
3. **online-softmax** — "A softmax that never sees the whole row." The obstacle:
   softmax needs the row max and sum, but a block sees only part of the row. The
   running max m and running normalizer l (Milakov recurrence, cite s2), then the
   output-accumulator rescaling as the ONE annotated equation. Stress: exact, not
   approximate.
4. **io-cost** — "Counting memory, not arithmetic." Theorem 2:
   Theta(N^2 d^2 / M) vs Theta(Nd + N^2). Figure 2 table (asset-2): more GFLOPs,
   ~9x less HBM traffic, ~5.7x faster. Then backward recomputation: store O, m, l
   and recompute S, P; memory linear in N.
5. **after** — "Exact attention and the ceiling it still lives under."
   FlashAttention-2 (occupancy/partitioning, ~2x), FlashAttention-3 (Hopper
   async + FP8), PyTorch SDPA adoption. The exact-vs-approximate distinction:
   Linformer/Reformer approximate to cut complexity; FlashAttention is exact and
   IO/hardware-bound, does not lower asymptotic compute. One Verdict note.

## Furniture
- Abstract card (chrome).
- asset-1 in tiling; asset-2 in io-cost.
- Display eq: S = QK^T, P = softmax(S), O = PV (standard attention).
- Display eq: Milakov running max/normalizer recurrence.
- Annotated eq (the one): the online-softmax output-accumulator update, three
  colored terms (renormalize; rescaled old accumulator; new block contribution).
- Display eq: the IO-cost comparison Theta(Nd+N^2) -> Theta(N^2 d^2 / M).
- One strong Verdict note at the end.

## Patterns to break
- Open on the bottleneck, not a baseline. No "got X right, Y wrong" dek, no "the
  record after it." No holds-up grid; one Verdict note. No semicolon-contrast or
  wh-clause headings. No "no later work overturns" line — say what FA-2 fixed.

## Citations / source order (first appearance)
s1 FlashAttention, s2 Milakov, s3 Rabe&Staats, s4 FA-2, s5 FA-3, s6 Linformer,
s7 Reformer, s8 PyTorch blog. Number the source list in this order.
</content>
