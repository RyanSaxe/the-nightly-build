# Commission — build-from-scratch/speculative-decoding

## Assignment
One Build From Scratch on the `article` template (1500–4500 words). Rebuild
**speculative decoding** from scratch, with real code (`nb-code`) and a run of
it, so the reader could implement it themselves. min_sources 8.

## The idea to expose by rebuilding
Speculative decoding accelerates autoregressive generation by having a small,
cheap **draft** model propose several tokens, then having the large **target**
model verify them in a single parallel forward pass. The non-obvious, load-
bearing insight: a **modified rejection-sampling** accept/reject step makes the
output distribution *provably identical* to sampling from the target model alone.
The speedup is free of any quality change when done correctly. Rebuilding the
accept/reject math is what a summary hides — show that the acceptance criterion
(accept token x with prob min(1, p_target(x)/p_draft(x)), and on rejection sample
from the normalized positive residual (p_target − p_draft)_+) yields exactly the
target distribution, and demonstrate it empirically.

## The build (smallest design that demonstrates it)
Start from the smallest setup that proves the claim, not a full LLM stack:
- A minimal but real demonstration where `p_target` and `p_draft` are explicit
  distributions (e.g., small autoregressive/char-level or n-gram models, or even
  toy per-step categoricals) so the accept/reject step is visible and the
  exact-distribution property is checkable.
- Implement standard autoregressive sampling, then the draft-then-verify loop
  with the rejection step, in `nb-code`.
- **Run it** and show output: empirically confirm the speculative sampler's
  output distribution matches the target's (e.g., match sampled frequencies to
  target probabilities over many draws), and report the expected accepted-tokens-
  per-step / speedup as a function of draft-target agreement.
Then compare the prototype to the real systems: what changes at LLM scale (KV
cache, batched verification, the draft-model choice), and where the wins and
limits come from (acceptance rate, memory-bandwidth-bound decoding).

## Intended reader / contribution
House reader (math/CS, ML-eng). Assume transformers, autoregressive sampling,
temperature/top-k. The contribution: the reader leaves able to implement
speculative decoding and to reason about when it pays (acceptance rate vs draft
cost), having seen the exact-distribution proof made concrete in runnable code —
not just the "small model drafts, big model checks" slogan.

## Source obligations
- Template `article`, min_sources 8. Cite, having read them: the two founding
  papers — Leviathan, Kalman, Matias, "Fast Inference from Transformers via
  Speculative Decoding" (ICML 2023; arXiv:2211.17192); Chen et al. (DeepMind),
  "Accelerating Large Language Model Decoding with Speculative Sampling"
  (arXiv:2302.01318) — for the algorithm and the correctness proof. Add
  interpretation-relevant follow-ons only where they change the picture (e.g.,
  Medusa, EAGLE, self-speculative/lookahead decoding, a production writeup with
  measured speedups). Verify the acceptance rule and the distribution-equivalence
  claim against the papers' own statements; quote the key lemma.
- Any speedup number cited must come from a primary source or from the article's
  own committed run — do not repeat vendor marketing figures unverified.

## Furniture / code
The argument is carried by `nb-code` (a code listing) plus the run's output. Use
an equation for the acceptance rule and the residual distribution. Show the
empirical distribution-match result as a small table or figure from the run
(honest, cited to the committed script). Furniture carries reasoning, not decoration.

## Relevant prior coverage / habits not to inherit
Recent Build From Scratch: byte-pair-encoding (tokenization, 2026-07-25). Do NOT
reuse its "train a tiny X on N bytes and reproduce Y" opener verbatim; find this
piece's own way in. No colon-subtitle headline. Vary section shapes.

## Neighboring articles tonight (edition cohesion)
Tonight also runs paper-of-the-day on grokking (optimization/generalization) and
tech-news (may mention frontier-model releases). Keep this in the inference-
systems lane; do not overlap grokking's territory. Inference economics is the
timely frame; don't turn it into a market piece.

## Output paths
- Article: `.nb-work/build-from-scratch/speculative-decoding/library/build-from-scratch/speculative-decoding.html`
- Assets / chart or code provenance under `library/build-from-scratch/speculative-decoding/`
- Role artifacts under `agent-artifacts/build-from-scratch/speculative-decoding/`

## Harness / model
- harness `claude-code`; writer runtime `claude-sonnet-5` (capable/medium);
  editor opus/high (required).
