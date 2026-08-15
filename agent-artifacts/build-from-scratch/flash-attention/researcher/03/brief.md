# researcher brief: build-from-scratch/flash-attention (03)

Inputs:
- editorial-direction.md — citation standard
- researcher/02/evidence.md — your prior record (now 7 sources; preserve all)
- editor/01/editorial-review.md — the sources-floor finding

Output: researcher/03/evidence.md (new record preserving 02's seven sources and
adding at least one more genuine claim-owner to reach the floor of eight; do not
overwrite 02)

Round 02 reached seven real sources. Find at least one more legitimate,
readable source that owns a claim the article already makes, so no padding is
needed. Two strong untried candidates:
- The safe-softmax numerical-stability claim (subtract the max before exponentiating)
  that the article's overflow experiment rests on: a standard reference that owns
  it independently of Milakov-Gimelshein (for example Goodfellow, Bengio and
  Courville, "Deep Learning" (2016), the numerical-computation section on softmax
  overflow/underflow). Open it and record the exact passage and locator.
- PyTorch's scaled_dot_product_attention documentation, which owns the "shipped as
  a framework's fused attention backend" claim in the closing comparison, distinct
  from the Dao-AILab repository already added. Open it and record what it states.

Add whichever genuinely resolve and own a claim in the piece; if both do, add
both. Confirm every URL resolves. Report which source(s) you added, the claim each
owns, and the resulting total count.
