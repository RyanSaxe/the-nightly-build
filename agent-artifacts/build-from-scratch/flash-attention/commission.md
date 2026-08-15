# Commission: build-from-scratch/flash-attention

## Subject and the insight to expose

Rebuild the online-softmax core of FlashAttention from scratch, in pure Python
or NumPy, and show that exact attention never needs to hold the full N-by-N
score matrix in memory. The headline descriptions of FlashAttention are about
IO-awareness and a fused GPU kernel. The mathematical core that makes any of it
possible is the online (streaming) softmax: a running maximum and a running
normalizer that let you consume keys and values block by block and still return
the identical output. That core can be built and proven equivalent without a
single GPU kernel, and building it is what exposes the insight a summary hides.

## What the reconstruction must do

Start from one attention head and the smallest design that demonstrates the
idea. Build two implementations:

1. Naive attention that forms `S = Q K^T`, softmaxes the full matrix, and
   multiplies by `V`. Its score matrix is O(N^2) in memory.
2. Streaming attention that tiles K and V into blocks and maintains, per query,
   a running max `m`, a running denominator `l`, and a running output
   accumulator `o`, rescaling the accumulator when a new block raises the max.

The experiment carries the argument, so it must run in `nb-code` and show its
output: assert the two outputs match to floating-point tolerance across sizes;
measure how the naive score matrix grows against the streaming buffers as N
increases; and show what the running max buys by exhibiting the overflow the
naive-but-unshifted softmax hits where the streaming version stays stable.

Then compare the prototype to the real system honestly. The real kernel adds
GPU SRAM tiling, a fused softmax that never writes S to HBM, and a backward pass
that recomputes S from the saved statistics. The prototype keeps the exact math
and omits the hardware and IO layer, so it cannot show the wall-clock speedup,
which is the real kernel's actual product. Say that plainly.

## Sources to begin from (researcher confirms and reads)

- Dao, Fu, Ermon, Rudra, Ré, "FlashAttention: Fast and Memory-Efficient Exact
  Attention with IO-Awareness," arXiv:2205.14135 (primary; the tiling and the
  recomputation-in-backward claims).
- Milakov and Gimelshein, "Online normalizer calculation for softmax,"
  arXiv:1805.02867 (primary; the running-max/running-sum recurrence itself, the
  actual origin of the trick FlashAttention reuses).
- Rabe and Staats, "Self-attention Does Not Need O(n^2) Memory,"
  arXiv:2112.05682 (primary; the O(1)/O(log n) memory argument for exact
  attention).
- Dao, "FlashAttention-2," arXiv:2307.08691 (primary; only for the honest
  comparison to the shipped system, not the core math).

The claim rests on the math and the runnable experiment, so the citations that
matter most are the two equations (online softmax) and the code's own measured
output. Verify the arithmetic of the recurrence against Milakov and Gimelshein.

## Furniture opportunities

The runnable prototype is `nb-code` and it is the argument, not decoration. The
online-softmax recurrence is the one equation the piece is really about: set it
as the annotated `nb-math` (at most one annotated equation). A `nb-figure` chart
of peak score-matrix memory against N, drawn by `nb chart` from the experiment's
own measured numbers, earns its place if the code produced those numbers. A
short `nb-table` contrasting naive and streaming on memory and number of passes
may help. Furniture carries evidence, never fills a quota.

## Habits to break (from the recent build-from-scratch record)

The rotary-position-embeddings piece (2026-08-08) closed on the heading "What
relative position does not buy" and landed a closing `nb-note` verdict. A
closing "what X does not buy" or "what would have to change" heading, and a
closing `nb-note-strong` verdict box, are both recurring across recent pieces in
several series. Do not reach for either by default. End on the conclusion the
experiment earned, in prose, and vary how the section headings are built. Recent
build-from-scratch headings are declarative claims; keep that quality without
copying the shape. No colon-subtitle headline.

## Reader, boundaries, record

Reader: the paper's declared audience, ML engineers with mathematics and CS
backgrounds. Assume attention, softmax, and big-O; teach the online-softmax
recurrence and the equivalence proof from first principles. Word band 1500-4500,
2 to 6 flex sections, at least 8 sources. Do not drift into a survey of every
attention variant; the subject is the online-softmax core and its exact
equivalence.

Cross-article: no overlap with the other six articles in this edition.

Models and effort actually used (Agent runtime; effort is not separately
settable through it, so intended effort is recorded and the model tier plus
prompt emphasis carry it): writing-coach — capable tier (sonnet), intended
effort low; researcher — capable tier (sonnet), intended effort high; writer —
capable tier (sonnet), intended effort medium; editor — inherited model (opus),
intended effort high, required stage.
