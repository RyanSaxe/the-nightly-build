# Researcher brief: paper-of-the-day/flash-attention

## Assignment
Assemble the evidence to reconstruct FlashAttention and weigh it against the
after-record. Every claim carries a resolving URL and a passage read there.
Primary sources lead; the focal paper owns its own claims. Full detail and
passages are in evidence.md.

## Sources opened (all resolve, min 8)
1. Dao, Fu, Ermon, Rudra, Ré, "FlashAttention" (arXiv:2205.14135, NeurIPS 2022).
   Primary, focal. Abstract, Figure 1, Figure 2 table, Theorem 2, Algorithm 1
   online-softmax update, backward recomputation, block sizes.
2. Milakov & Gimelshein, "Online normalizer calculation for softmax"
   (arXiv:1805.02867, 2018). Primary. The single-pass running-max/normalizer
   recurrence FlashAttention builds on.
3. Rabe & Staats, "Self-attention Does Not Need O(n^2) Memory"
   (arXiv:2112.05682, 2021). Primary. Exact attention in O(1)/O(log n) memory,
   the memory-efficient-exact line.
4. Dao, "FlashAttention-2" (arXiv:2307.08691, 2023). Primary. ~2x, occupancy and
   work partitioning.
5. Shah et al., "FlashAttention-3" (arXiv:2407.08608, 2024). Primary. Hopper
   asynchrony and FP8.
6. Wang et al., "Linformer" (arXiv:2006.04768, 2020). Primary. Low-rank
   approximate attention, O(n).
7. Kitaev, Kaiser, Levskaya, "Reformer" (arXiv:2001.04451, 2020). Primary.
   LSH approximate attention, O(L log L).
8. "Accelerated PyTorch 2 Transformers" (pytorch.org/blog/accelerated-pytorch-2).
   Secondary. FlashAttention as the first SDPA fused kernel.

## Figures captured (beside the article, validated)
- asset-1.png: Figure 1 (page 2) — memory hierarchy + tiling diagram + GPT-2
  runtime breakdown.
- asset-2.png: Figure 2 comparison table (page 6) — GFLOPs, HBM R/W, Runtime for
  Standard vs FlashAttention.

## Arithmetic cross-checks
- HBM traffic: 40.3 / 4.4 = 9.2x fewer. Runtime: 41.7 / 7.3 = 5.7x faster. GFLOPs
  75.2 > 66.6, confirming FlashAttention does more arithmetic. All from Figure 2.
- SRAM/HBM bandwidth gap: 19 / 1.5 = ~13x. From Figure 1.
- The IO ratio: standard N^2 vs FlashAttention N^2 d^2 / M; the speedup factor is
  ~ M / d^2, which for M ~ 100 KB and d = 64 is many-fold.
</content>
