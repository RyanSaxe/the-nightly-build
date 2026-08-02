# Evidence: paper-of-the-day/generative-adversarial-networks (researcher/02)

Narrow follow-up to close one gap: `researcher/01/evidence.md` (same commission, same
folder tree, path
`.nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/researcher/01/evidence.md`)
remains the full, still-valid evidence record — equations, theorems, numbers, contradictions,
source assets, and eight classified sources. It did not capture the GAN paper's own abstract
text verbatim, which the `paper` template's abstract anchor requires word-for-word. This file
supplies only that.

## Sources

### 1. Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville, Bengio,
"Generative Adversarial Nets," arXiv:1406.2661
URL: https://arxiv.org/abs/1406.2661
**Primary** — the paper's own words, reproduced verbatim below. Not a paraphrase: pulled
directly from the raw page HTML rather than through a summarizing fetch, and cross-checked
against two independent copies embedded in the same page — the visible abstract blockquote
and the `citation_abstract` metadata tag arXiv generates for indexing — which read
identically. URL confirmed resolving: `curl -o /dev/null -w '%{http_code}'` returned `200` at
verification time. Locator: arXiv abstract page for 1406.2661, the "Abstract:" block
(`<blockquote class="abstract mathjax">`), same page also mirrored at
https://ar5iv.labs.arxiv.org/html/1406.2661 (both are arXiv's own hosting of the same
submission; only the arxiv.org/abs page was used for this verbatim transcription, since it is
the canonical source and the one that resolved directly to raw HTML).

**Abstract, verbatim:**

> We propose a new framework for estimating generative models via an adversarial process, in
> which we simultaneously train two models: a generative model G that captures the data
> distribution, and a discriminative model D that estimates the probability that a sample
> came from the training data rather than G. The training procedure for G is to maximize the
> probability of D making a mistake. This framework corresponds to a minimax two-player game.
> In the space of arbitrary functions G and D, a unique solution exists, with G recovering the
> training data distribution and D equal to 1/2 everywhere. In the case where G and D are
> defined by multilayer perceptrons, the entire system can be trained with backpropagation.
> There is no need for any Markov chains or unrolled approximate inference networks during
> either training or generation of samples. Experiments demonstrate the potential of the
> framework through qualitative and quantitative evaluation of the generated samples.

**Transcription caveats:**
- The abstract as arXiv renders it is a single unbroken paragraph; no internal line breaks or
  paragraph divisions exist in the source, so none were introduced here.
- The abstract contains no mathematical notation (no LaTeX/MathJax spans), so there is no
  symbol-rendering ambiguity to flag — "1/2" appears as plain text in the source, not as a
  rendered fraction, and is reproduced that way above.
- No footnote markers, citations, or ellipses appear in the abstract itself; the text above is
  complete, start to finish, with nothing omitted.

## Contradictions

None found. This entry adds one verbatim text block; it does not bear on any disputed claim
in `researcher/01/evidence.md`.

## Numbers

None new. See `researcher/01/evidence.md` for the full numbers table.

## Source assets

None found beyond what `researcher/01/evidence.md` already records (the paper's Figure 1
schematic and Table 2/Table 5 comparison tables from other sources). The abstract itself is
text, not a visual asset.

## Discarded

None. This follow-up made one successful fetch against one already-verified URL.
