# writer brief: build-from-scratch/flash-attention (02)

Apply the sources-floor item from editor/01/editorial-review.md, using the new
evidence (inputs and standard unchanged from writer/01/brief.md; the editor's
direct edits are already in the article, including the corrected Fig. 4 buffer
formula, and must be preserved).

Inputs for the new sources:
- researcher/02/evidence.md — Vaswani et al. (attention shape the piece rebuilds),
  Jia et al. GPU microbenchmarking (HBM-slow/SRAM-fast facts with measured
  numbers), Dao-AILab flash-attention repo (shipped kernel).
- researcher/03/evidence.md — Goodfellow/Bengio/Courville Deep Learning Sec 4.1
  (the safe-softmax max-subtraction the overflow experiment demonstrates), PyTorch
  scaled_dot_product_attention docs (FlashAttention-2 as an auto-selected framework
  backend).

Cite these five at the existing claim sites only. Add no new claims or sections.
Honor the scaled/unscaled trap the evidence flags twice: cite Vaswani and the
PyTorch docs for the shape of attention, and do not phrase any citation as though
the article's naive implementation computes the scaled softmax(QK^T/sqrt(d_k))V of
Vaswani's Equation 1 — the piece's code is unscaled, matching FlashAttention's own
formulation. Keep every existing citation and number intact.

Update the nb-meta sources count (from 4 to the new total). Rerun the full proof
(links included) with `nb stamp` before the final check, until BLOCK: 0; the
W-SOURCES-MIN warning should now clear. Output: writer/02/draft-handoff.md.

Proof: ./nb check --series build-from-scratch .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html --library /home/user/library-checkout
