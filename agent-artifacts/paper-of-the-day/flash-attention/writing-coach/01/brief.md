# Writing-coach brief: paper-of-the-day/flash-attention

## The piece this has to be
A reconstruction of FlashAttention (Dao et al. 2022) for a reader with a
machine-learning background who has used attention but may never have asked where
its time actually goes. The reader knows attention is O(N^2). What they may not
hold: that the quadratic cost that hurts on a GPU is memory traffic, not
arithmetic, and that you can compute the identical attention while never writing
the N x N matrix to HBM.

The article rebuilds four mechanisms and then weighs the result:
1. The memory-IO bottleneck: SRAM is ~13x the bandwidth of HBM and tiny; standard
   attention round-trips the N x N matrix through HBM three times.
2. Tiling: stream K/V and Q in blocks that fit in SRAM, compute each block of the
   attention matrix on-chip, write only the output.
3. The online softmax: a running max and running normalizer let block-wise
   partial results be combined into the exact softmax, rescaling the output
   accumulator as each block arrives.
4. The IO cost: Theta(N^2 d^2 / M) versus standard Theta(Nd + N^2), and backward
   recomputation that trades extra FLOPs for far less memory traffic.

Then the after-record: FlashAttention-2 and -3 pushing GPU utilization, adoption
as PyTorch's default kernel, and the exact-vs-approximate distinction that places
FlashAttention off the axis the approximate methods were racing on.

## What the reader should be able to do at the end
- Explain why a kernel that does MORE floating-point work runs several times
  faster: it moves far less data.
- Sketch the online-softmax recurrence and say why the block-wise result is exact,
  not an approximation.
- State the IO bound and say when the win shrinks: small sequences, or a shrinking
  SRAM/HBM gap.
- Separate FlashAttention (exact, hardware-bound) from Linformer/Reformer
  (approximate, complexity-bound).

## Register and traps
- House voice: calm, first-principles, each term built before it is spent. Define
  HBM, SRAM, IO-aware, tiling, and the online softmax at first use.
- The easy version says FlashAttention "made attention linear." It did not lower
  asymptotic FLOPs; memory is linear in N, compute is still quadratic. Keep the
  three quantities distinct: FLOPs, HBM accesses, wall-clock.
- FlashAttention-2 is not a correction of a bug; v1 left GPU occupancy on the
  table. Report what v2 partitioned better, not a concession framing.
</content>
