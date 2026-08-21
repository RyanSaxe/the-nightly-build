# Commission: paper-of-the-day/flash-attention

## Assignment
Reconstruct **Dao, Fu, Ermon, Rudra, and Ré (2022), "FlashAttention: Fast and
Memory-Efficient Exact Attention with IO-Awareness"** (NeurIPS 2022). The
central claim to rebuild: standard attention is bottlenecked not by arithmetic
but by reading and writing the N×N attention matrix to and from GPU high-
bandwidth memory (HBM); FlashAttention computes the *exact* same attention
without ever materializing that matrix, by tiling Q, K, V into blocks small
enough to live in on-chip SRAM and combining the per-block partial results with
the online (streaming) softmax recurrence, then recomputing the matrix in the
backward pass rather than storing it. The payoff is memory linear in sequence
length and a wall-clock speedup that comes from fewer HBM accesses, with no
change to the output and no change to the asymptotic FLOP count.

(This replaces tonight's first paper choice, "chinchilla", which the proof
correctly blocked as already published on 2026-07-22. flash-attention is
confirmed unpublished.)

## What to rebuild, and with what
- Why standard attention is memory-bound: the S = QKᵀ, softmax, and P·V steps
  each round-trip the N×N matrix through HBM; contrast HBM vs SRAM bandwidth and
  capacity so the reader sees where the time goes.
- The online-softmax recurrence: the running max m and running normalizer l, and
  how the output accumulator is rescaled as each new K/V block arrives, so the
  block-wise computation yields the exact softmax. Set this math with the
  equation furniture instead of paraphrasing it; cite the online-normalizer
  precursor (Milakov & Gimelshein 2018) where you lean on it.
- The IO cost: standard attention's Θ(Nd + N²) HBM accesses versus
  FlashAttention's Θ(N²d²/M) with SRAM size M, and why that is the speedup.
- Backward-pass recomputation: storing only the softmax normalizers and
  recomputing blocks, trading extra FLOPs for far less memory traffic.
- Bring the paper's own figures in as source assets via `./nb asset`: Figure 1
  (the GPU memory-hierarchy + tiling diagram and the runtime breakdown), and a
  results figure/table where it settles a specific claim. Each asset gets a
  caption saying what it settles. A reconstruction that only describes the
  figures underuses them.

## Weigh it against the record after publication
This is what makes the paper worth a piece, not an announcement:
- FlashAttention-2 (Dao 2023): better parallelism and work partitioning across
  warps/thread-blocks, roughly 2x over v1 — i.e. v1 left GPU utilization on the
  table. FlashAttention-3 (2024): Hopper-specific asynchrony and FP8. Adoption
  as a default kernel (PyTorch scaled_dot_product_attention, and the wider
  stack).
- The honest nuance: the algorithm is *exact*, so it is not on the accuracy
  frontier the approximate-attention methods (Reformer, Linformer, Performer)
  were chasing; its benefit is hardware- and IO-bound and depends on the
  SRAM/HBM gap and the sequence length, and it does not lower asymptotic compute.
  Say what FlashAttention does and does not settle about "efficient attention".

## Boundaries
- Template `paper`: 1800-3400 words, 2-8 flex sections, per-section citation,
  minimum 8 sources. The abstract card and the paper link go up front.
- Sources: the FlashAttention paper (primary), FlashAttention-2 and -3 (primary),
  the online-softmax precursor, the PyTorch SDPA documentation, and an
  approximate-attention baseline you actually read for the contrast. Cite figures
  to the paper you captured them from. Every URL must resolve.

## Production record
- Correspondent (coach + research + draft + self-proof): model `claude-opus-4-8`
  (raised from the balanced default for the math reconstruction and figure
  capture; recorded as a deviation the run owns), high effort.
- Editor (fresh eyes, required): model `claude-opus-4-8`, high effort.
- nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date
  `2026-08-21`.
- Proof: `nb check .nb-work/paper-of-the-day/flash-attention/library/paper-of-the-day/flash-attention.html --series paper-of-the-day --library /home/user/library-checkout`

## Recent patterns to break
- Dek: avoid the "got X right and Y wrong" / "proved A … though the record after
  locates B" concession mold and the phrase "the record after it".
- Opener: open on the memory-IO bottleneck, not on a baseline-before-twist frame
  (no "attention was X; FlashAttention made it Y" lede).
- Do not inherit the "What holds up / What to be careful about" box plus
  "Verdict" mold shared across recent paper and expert-tools pieces. Let the
  reconstruction and the after-record choose the sections.
- Headings: avoid semicolon-contrast headings and "What the experiments actually
  settle" wh-clause headings. Write argument-step headings in the paper's nouns.
- Avoid the standing "no later work overturns" / self-reported-benchmark tic;
  state plainly what FA-2 improved on and what remains hardware-bound.
