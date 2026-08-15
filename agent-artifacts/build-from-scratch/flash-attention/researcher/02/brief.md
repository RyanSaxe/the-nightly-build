# researcher brief: build-from-scratch/flash-attention (02)

Inputs:
- editorial-direction.md — citation standard, declared reader
- researcher/01/evidence.md — your prior record (preserve all valid work)
- editor/01/editorial-review.md — the sources-floor finding routed to you

Output: researcher/02/evidence.md (a complete new record preserving 01's work
and adding the new sources; do not overwrite 01)

The editor did not approve under the series floor of eight sources and identified
that legitimate, readable sources own claims the article already makes. Add real
claim-owners, each opened and confirmed, so the writer can cite them at existing
claim sites (no new claims, no padding):
- Vaswani et al., "Attention Is All You Need" (arXiv:1706.03762) — the scaled
  dot-product attention the piece rebuilds.
- A GPU memory-hierarchy primary for the HBM-is-slow / SRAM-is-fast facts the
  argument uses (for example an NVIDIA architecture whitepaper or the CUDA
  programming guide's memory-hierarchy section, or a peer-reviewed GPU
  microbenchmarking paper). Record the exact figures it owns.
- The shipped implementation for the real-kernel comparison (the Dao-AILab
  flash-attention repository README, or PyTorch's scaled_dot_product_attention /
  FlashAttention backend docs).
- Optional: a safe-softmax numerical-stability reference for the max-subtraction
  step.

Read each source, confirm its URL resolves to its own page, and record for each
exactly which claim already in the article it owns. Report which sources you
added and the claim each supports.
