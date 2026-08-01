# Researcher brief — paper-of-the-day/grokking (01)

## Your job
Read and verify the sources for a paper-reconstruction of Power et al. 2022
"Grokking," and write the exact evidence record the writer and editor use. Read
the focal paper closely; verify every follow-on claim against the paper that
owns it. Min_sources 8.

## Exact inputs (start here)
- `agent-artifacts/paper-of-the-day/grokking/commission.md`
- `agent-artifacts/paper-of-the-day/grokking/editorial-direction.md`

## Must capture (verbatim / exact)
1. **Paper card data.** From arXiv:2201.02177: exact title as published, full
   author list, venue (ICLR 2022 Workshop / arXiv), year, canonical link, and
   the **abstract verbatim** (exact text, for the paper card blockquote). Note
   the venue precisely (it was a workshop paper; get it right).
2. **The core result, exactly.** The modular-arithmetic task setup (operations,
   modulus p, train fraction), the "generalize long after overfitting" curves,
   and the paper's own reported dependence on weight decay / dataset fraction /
   optimization. Record specific figures, section numbers, and any exact numbers
   the article will use (e.g., the modulus, the step counts, train fraction
   thresholds). Quote key sentences where display-worthy.
3. **Nanda et al. 2023 mechanistic account.** "Progress measures for grokking
   via mechanistic interpretability" (ICLR 2023; arXiv:2301.05217). Verify: the
   one-layer transformer on modular addition implements it as rotation via
   discrete Fourier components; the three phases (memorization, circuit
   formation, cleanup); the "progress measures" idea. Get authors, venue, link,
   and the exact claims with locators.
4. **At least one interpretation-changing follow-on.** E.g., Liu et al.
   "Omnigrok: Grokking Beyond Algorithmic Data" (get exact cite), and/or a
   2024–2026 result on grokking's fragility / weight-decay dependence / edge of
   numerical stability. Verify what each actually claims and how it changes the
   reading of the 2022 paper. Read them; do not trust titles.
5. **Verdict inputs.** What the 2022 paper measured vs. what it left unexplained;
   what the after-record settled vs. left open. Seek disagreement/criticism, not
   just confirmation.

## Deliverable
`agent-artifacts/paper-of-the-day/grokking/researcher/01/evidence.md`:
- The paper card block (title/authors/venue/year/link/abstract-verbatim) clearly
  set apart for the writer to paste, with the abstract quoted exactly.
- Numbered evidence entries: claim, exact quote/figure/number, source
  publisher+title+resolvable URL, `data-nb-locator` suggestion (section/figure),
  and primary/secondary classification with reason (the paper making a claim is
  primary for it).
- Contradictions/uncertainties (e.g., competing explanations of grokking's
  cause; anything you could not pin down).
- Discarded sources (blog restatements without primary grounding, etc.).
- 8+ solid entries so the writer clears min_sources with real, read sources.

## Constraints
- Cite only what you read. arXiv HTML/PDF both work; if one route 403s, use the
  other. Never record an unverified URL.
- Begin with the named inputs; focused verification only, no repo/archive tour.
- Missing context: `REQUEST researcher <one-sentence need>`.

## Report
End with: `DONE researcher agent-artifacts/paper-of-the-day/grokking/researcher/01/evidence.md`
