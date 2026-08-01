# Researcher brief — build-from-scratch/speculative-decoding (01)

## Your job
Read the founding speculative-decoding papers closely, verify the acceptance
rule and the distribution-equivalence proof, and write the evidence record the
writer uses to rebuild the algorithm correctly. Min_sources 8.

## Exact inputs (start here)
- `agent-artifacts/build-from-scratch/speculative-decoding/commission.md`
- `agent-artifacts/build-from-scratch/speculative-decoding/editorial-direction.md`

## Read and pin, exactly
1. **Leviathan, Kalman, Matias 2023** (arXiv:2211.17192, ICML 2023). Capture: the
   exact algorithm (draft γ tokens, one target forward pass, accept/reject), the
   **acceptance probability** min(1, p(x)/q(x)) (state p=target, q=draft precisely),
   the **residual/adjusted distribution** on rejection ((p−q)_+ normalized), the
   theorem that the resulting samples are distributed exactly as the target, and
   the expected-accepted-tokens / speedup analysis (the α acceptance-rate result).
   Quote the key lemma/theorem verbatim with locators.
2. **Chen et al. 2023** (arXiv:2302.01318, DeepMind). Capture its "speculative
   sampling" statement of the same accept/reject scheme and its correctness
   argument; note any differences in framing/notation. Quote the algorithm box.
3. **Follow-ons that change the picture** (pick the ones that matter): Medusa
   (multiple decoding heads), EAGLE (feature-level drafting), self-speculative /
   lookahead decoding, and/or a production writeup with **measured** speedups.
   For each, capture what it changes and one concrete measured number with source.
4. **The correctness math, restated cleanly** so the writer can prove it in the
   article: show algebraically why accept-with-min(1,p/q) + residual sampling
   reproduces p(x) exactly. Provide the derivation steps with the source that
   supports each.

## Deliverable
`agent-artifacts/build-from-scratch/speculative-decoding/researcher/01/evidence.md`:
- Numbered entries: claim, exact quote/equation/number, source publisher+title+
  URL, locator (section/eq/theorem number), primary/secondary + reason (the
  algorithm's paper is primary for it; measured speedups from the party that ran
  them are primary for that measurement).
- A clean statement of the acceptance rule + residual distribution + the
  equivalence proof steps, ready for the writer to turn into an equation and code.
- Contradictions/uncertainties (notation differences; any speedup that is
  workload-specific — flag it as not general).
- Discarded sources (marketing pages without measured detail). 8+ solid entries.

## Constraints
- Verify the math yourself against the papers; the writer's code must match the
  proven rule exactly. arXiv HTML/PDF both work; if one 403s use the other. Cite
  only what you read; never record an unverified URL.
- Begin with the named inputs; focused research only, no repo/archive tour.
- Missing context: `REQUEST researcher <one-sentence need>`.

## Report
End with: `DONE researcher agent-artifacts/build-from-scratch/speculative-decoding/researcher/01/evidence.md`
