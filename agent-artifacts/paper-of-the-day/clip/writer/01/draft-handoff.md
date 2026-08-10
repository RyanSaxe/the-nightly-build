# Draft handoff: paper-of-the-day/clip (writer 01)

## Original work

The article reconciles CLIP's Section 3.3 hedge with the after-record: it reads
the paper's own adaptation experiment (Figure 14) as evidence CLIP itself
supplied against the zero-shot reading, so the follow-on (Fang et al.) lands as
confirming the training-data cause CLIP had floated rather than overturning a
claim CLIP made. The evidence record holds these as separate facts; the article
assembles them into that single reading, visible in the robustness section and
in the closing re-reading of Section 3.3.

## Proof result

`./nb check ... --series paper-of-the-day --library /home/user/library-checkout`
(links included): **BLOCK: 0**, verdict PUBLISHABLE, WARN: 1.

- The one remaining warning is **W-SENTENCE-DENSITY, "41 words, 4 clause joins,
  punctuation score 73."** It is a false positive on the required annotated
  objective equation: the density heuristic skips `<math>`, `<code>`, and
  `<blockquote>`, but not the KaTeX `nb-math-eq` div, so it reads the equation's
  TeX source (`\mathcal{L} = ...`) as a 41-word prose sentence. Left in place
  intentionally; there is no prose to split. Any `nb-math` annotated equation in
  this engine trips it.
- The six sentence-density warnings from the first proof were real prose and are
  fixed (prompt-gain chain, the five-cause list, the Fang conclusion, the Nguyen
  finding, the Cherti scaling sentence, the bias probe, the Fig. 14 adaptation
  sentence, the encoder pipeline, and the classifier-framing sentence all split).

## Furniture / assets note for the editor

- Three source assets captured from the CLIP PDF (arXiv:2103.00020): Fig. 1
  method summary (all three panels), Fig. 13 robustness plot (left scatter +
  right "banana" panel), Fig. 14 "Adapt to ImageNet" per-dataset bars. Each was
  inspected as rendered.
- The Fig. 13 right "banana" panel is captioned explicitly as a single-class
  illustration, per the evidence record's caution, so its +74.4% / +51.2%
  deltas are not read as the averaged headline result. Please confirm that
  framing reads unambiguously.

## Open questions

- **Editor check on one earned contrast.** The verdict ends "its data, not its
  captions, is what made that classifier hold up." This is a named-misconception
  contrast (the language-supervision reading the piece corrects), not a slop
  negative-parallelism, but it sits in the article's last sentence, so it is
  worth the explicit check.
- **Bias figure restraint.** I used only the claim the evidence record marked
  safe (Black faces into a non-human category at 14.4% vs. <=7.6% for other
  groups, and the label-set sensitivity) and did not quote the per-age child
  cells the researcher flagged as needing Table 6-7 re-verification. If the
  editor wants a specific child-age figure, it needs that verification first.
- **Live-DOM render not run.** The headless-Chrome preview could not install its
  browser in this environment (network timeouts on the download), so CI
  `render-check` is the first live-DOM pass. The equation uses only standard
  KaTeX commands matching the furniture sample, and the three asset PNGs were
  inspected directly, so no rendering problem is expected.
