# Evidence: paper-of-the-day/flash-attention

Each claim carries the URL it was read at and the passage that supports it.

## The paper and its central claim

- **Verbatim abstract.** "Transformers are slow and memory-hungry on long
  sequences ... Approximate attention methods have attempted to address this
  problem by trading off model quality to reduce the compute complexity, but
  often do not achieve wall-clock speedup. We argue that a missing principle is
  making attention algorithms IO-aware ... We propose FlashAttention, an IO-aware
  exact attention algorithm that uses tiling to reduce the number of memory
  reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM ...
  15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to
  the MLPerf 1.1 training speed record, 3x speedup on GPT-2 (seq. length 1K), and
  2.4x speedup on long-range arena (seq. length 1K-4K) ... 0.7 better perplexity
  on GPT-2 ... Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256
  (seq. length 64K, 63.1% accuracy)."
  https://arxiv.org/abs/2205.14135

- **Authors / venue.** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra,
  Christopher Ré. NeurIPS 2022. arXiv:2205.14135 (May 2022).
  https://arxiv.org/abs/2205.14135

## The memory-IO bottleneck

- **Memory hierarchy, A100 (Figure 1 left).** SRAM 19 TB/s, ~20 MB; HBM 1.5 TB/s,
  40 GB; CPU DRAM 12.8 GB/s, >1 TB. SRAM is ~13x the bandwidth of HBM and orders
  of magnitude smaller. Read from Figure 1 on page 2.
  https://arxiv.org/pdf/2205.14135 (page 2)

- **Attention is memory-bound (Figure 1 right).** The GPT-2 runtime breakdown
  shows the standard PyTorch attention spends most of its time in the
  memory-bound ops (dropout, softmax, masking) that surround the two matmuls;
  FlashAttention fuses them into one kernel. "FlashAttention does not read and
  write the large N x N attention matrix to HBM, resulting in an 7.6x speedup on
  the attention computation."
  https://arxiv.org/pdf/2205.14135 (page 2, Figure 1 caption)

- **The three round-trips.** Standard attention computes S = QK^T, P = softmax(S),
  O = PV, materializing the N x N matrices S and P in HBM between each step.
  Read on page 2.
  https://arxiv.org/pdf/2205.14135

## Tiling and the online softmax

- **Tiling (Figure 1 / §3.1).** Outer loop over blocks of K and V loaded to SRAM;
  inner loop over blocks of Q loaded to SRAM; the block of the attention matrix is
  computed on-chip and never written to HBM; only the output O is written back.
  Block sizes B_c = ceil(M/4d) for K,V and B_r = min(ceil(M/4d), d) for Q, the 4
  accounting for holding inputs, S/P, and outputs in SRAM at once.
  https://arxiv.org/pdf/2205.14135 (page 2, Figure 1)

- **Online normalizer precursor (Milakov & Gimelshein 2018).** Single-pass
  softmax keeps a running max m_j and running denominator d_j updated as
  d_j = d_{j-1} * e^{m_{j-1} - m_j} + e^{x_j - m_j}. FlashAttention builds on this.
  https://arxiv.org/abs/1805.02867

- **FlashAttention's online-softmax update (Algorithm 1, lines 10-12).**
  m_i^new = max(m_i, m~_ij);
  l_i^new = e^{m_i - m_i^new} l_i + e^{m~_ij - m_i^new} l~_ij;
  O_i <- diag(l_i^new)^{-1} ( diag(l_i) e^{m_i - m_i^new} O_i
         + e^{m~_ij - m_i^new} P~_ij V_j ).
  The old output accumulator is rescaled to the new running max and renormalized,
  so the block-wise result equals the exact softmax attention.
  https://ar5iv.labs.arxiv.org/abs/2205.14135

- **Exactness precursor (Rabe & Staats 2021).** "a very simple algorithm for
  attention that requires O(1) memory with respect to sequence length and an
  extension to self-attention that requires O(log n) memory," exact, time still
  O(n^2); a memory-efficient exact-attention line FlashAttention makes fast on
  GPUs.
  https://arxiv.org/abs/2112.05682

## The IO-cost argument

- **Theorem 2.** "Let N be the sequence length, d be the head dimension, and M be
  size of SRAM with d <= M <= Nd. Standard attention (Algorithm 0) requires
  Theta(Nd + N^2) HBM accesses, while FlashAttention (Algorithm 1) requires
  Theta(N^2 d^2 M^{-1}) HBM accesses." For d = 64-128 and M ~ 100 KB, d^2 is many
  times smaller than M, so FlashAttention makes many times fewer HBM accesses.
  Proposition 3 gives a matching lower bound: no exact attention algorithm beats
  Theta(N^2 d^2 M^{-1}) for all M.
  https://ar5iv.labs.arxiv.org/abs/2205.14135 (page 6)

- **Figure 2 table (page 6), GPT-2 medium, seq 1024, head dim 64, 16 heads, batch
  64, A100.** GFLOPs: Standard 66.6, FlashAttention 75.2 (MORE arithmetic). HBM
  R/W (GB): Standard 40.3, FlashAttention 4.4 (~9x fewer). Runtime (ms): Standard
  41.7, FlashAttention 7.3 (~5.7x faster). This is the whole thesis in one table:
  more FLOPs, far less memory traffic, much faster.
  https://arxiv.org/pdf/2205.14135 (page 6, Figure 2)

- **Backward recomputation (§3.1 / Figure 2 left).** The backward pass stores only
  the output O and the softmax statistics (m, l), each O(N), and recomputes the S
  and P blocks in SRAM from Q, K, V. "Even with the increased FLOPs due to
  recomputation, our algorithm both runs faster ... and uses less memory—linear
  in sequence length." Memory drops from quadratic to linear in N.
  https://arxiv.org/pdf/2205.14135 (page 2)

## The record after publication

- **FlashAttention-2 (Dao 2023).** ~2x over FlashAttention, 50-73% of theoretical
  peak FLOPs/s on A100, up to 225 TFLOPs/s (72% model FLOPs utilization). Root
  cause named: "the inefficiency is due to suboptimal work partitioning between
  different thread blocks and warps on the GPU, causing either low-occupancy or
  unnecessary shared memory reads/writes." Fixes: fewer non-matmul FLOPs;
  parallelize across the sequence-length dimension (not just batch and heads);
  better warp-level partitioning.
  https://arxiv.org/abs/2307.08691

- **FlashAttention-3 (Shah et al. 2024).** Hopper (H100) asynchrony via
  warp-specialization (Tensor Core + TMA overlap) and FP8. 1.5-2.0x over
  FlashAttention-2 in FP16, up to 740 TFLOPs/s (75% H100 utilization); ~1.2
  PFLOPs/s in FP8 with 2.6x lower numerical error than a baseline FP8 attention.
  Addresses FlashAttention-2's ~35% H100 utilization.
  https://arxiv.org/abs/2407.08608

- **Adoption in PyTorch.** scaled_dot_product_attention dispatches to fused
  kernels; "the first custom kernels included with the PyTorch 2.0 release are the
  Flash Attention kernel (sdpa_flash, for 16-bit floating point training and
  inference on Nvidia GPUs with SM80+ architecture level)" and the xFormers
  memory-efficient kernel, with a math fallback.
  https://pytorch.org/blog/accelerated-pytorch-2/

- **Exact vs approximate contrast.** Linformer (Wang et al. 2020): "the
  self-attention mechanism can be approximated by a low-rank matrix," reducing
  O(n^2) to O(n) in time and space, an approximation. Reformer (Kitaev et al.
  2020): locality-sensitive hashing cuts complexity "from O(L^2) to O(L log L),"
  also approximate. FlashAttention is exact, so it is not on the quality/complexity
  tradeoff those methods chase; its win is IO- and hardware-bound and does not
  lower asymptotic FLOPs.
  https://arxiv.org/abs/2006.04768 ; https://arxiv.org/abs/2001.04451

## Figures captured
- asset-1.png: Figure 1 (page 2). Memory-hierarchy triangle, the tiling diagram,
  and the GPT-2 runtime breakdown. Settles that attention is memory-bound and that
  tiling avoids materializing the N x N matrix.
- asset-2.png: the Figure 2 comparison table (page 6). Settles that FlashAttention
  does more arithmetic (75.2 vs 66.6 GFLOPs) yet cuts HBM traffic ~9x (4.4 vs 40.3
  GB) and runs ~5.7x faster (7.3 vs 41.7 ms).
</content>
