# Writer draft handoff: paper-of-the-day/mamba (01)

## Original work

The article resolves the apparent contradiction the evidence flags — Mamba's
perfect million-length induction-heads result set against its documented failure
at bulk copying and multi-key recall — into one mechanistic account: the
fixed-size recurrent state that makes Mamba linear-time is the same property that
lets it do single-item retrieval but not bulk recall, and the verdict on where
Mamba replaces attention is organized around that one property, which the
headline ("a state that never grows") names.

## Proof result

`./nb check … --series paper-of-the-day --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 1, verdict PUBLISHABLE.** Words 3391
(band 1800–3400), 8 sources, all primary.

## Warning intentionally left

- **W-SENTENCE-DENSITY** on a 43-word sentence, punctuation score 52. This is
  the paper's abstract, quoted verbatim inside the required `nb-paper-card`
  (template chrome demands the abstract on record in the original's own words).
  It cannot be split or shortened without falsifying the quote, so it stands.
  All six writer-authored dense sentences the earlier proof flagged were split.

## Notes for the editor / orchestrator (non-blocking)

- **Figure numbering corrected against the PDF.** The evidence record's figure
  numbers came from the arXiv HTML v2 rendering and do not match the published
  PDF's labels. The PDF's actual labels are: **Table 1** (Selective Copying),
  **Fig. 2 / Table 2** (Induction Heads), **Fig. 4** (Scaling Laws), **Fig. 8**
  (Efficiency Benchmarks). I cite the PDF's real labels. Table 1 and Table 3
  (zero-shot) are rendered as `nb-table`s built from the pixel-verified numbers
  rather than captured as images; the three genuine figures the claim turns on
  are captured as source assets: asset-1 = Fig. 8 (scan + throughput), asset-2 =
  Fig. 4 (scaling), asset-3 = the Induction Heads extrapolation plot.
- **Pixel-verified per the evidence's request:** Table 1 selective-copying
  accuracies (18.3 / 97.0 / 57.0 / 30.1 / 99.7 / 56.4 / 28.4 / 99.8) and Table 3
  (Mamba-2.8B 6.22 / 69.2 / 63.3; Pythia-2.8B 6.73 / 64.7 / 59.1; Mamba-1.4B
  6.80 / 64.9 / 59.7) confirmed against the PDF. The GPT-Neo perplexity the
  evidence discarded is not used.
- **Zoology (s2) attributed as framing, not measurement:** the prose states
  plainly that its tested models predate Mamba, so it frames the recall gap
  rather than grading Mamba, matching the evidence's caution.
- **Cross-series subject overlap (awareness only):** `the-paper/selective-state-spaces`
  in the published library also covers the Mamba paper. It is a different series;
  paper-of-the-day has not covered Mamba, and the commission confirms no overlap
  within this edition. This reconstruction's headline, section order, and
  furniture are independent of that article. Flagged only so a human is aware the
  subject exists elsewhere on the shelf.

## Open evidence / voice questions

None blocking. The evidence set was sufficient to build the reconstruction, set
the math, and weigh the post-publication record to a verdict without writing
around any hole.
