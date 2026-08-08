# Draft handoff: paper-of-the-day/neural-machine-translation-attention (writer 01)

## Original work (one sentence)
The piece makes explicit that the "attention is / is not explanation" dispute
(Jain & Wallace; Wiegreffe & Pinter) was run on later BiLSTM classification and
QA models and never on Bahdanau's 2015 translation model, so applying it to
Figure 3's alignments is the article's own inference rather than a claim either
2019 paper makes about this paper — and it holds Bahdanau's own plausibility
claim ("agree well with our intuition") apart from the stronger explanation
reading that inference invites. This reasoning is carried visibly in the
"Scope" note and the bounded verdict.

## Proof result
`./nb check ... --series paper-of-the-day --library <scratchpad>/library`,
links included: **BLOCK: 0**, verdict PUBLISHABLE.

One warning left intentionally:
- **W-SOURCES-MIN — 4 sources; series floor is 8.** The researcher's evidence
  record supplies exactly four sources (Bahdanau 1409.0473; Vaswani 1706.03762;
  Jain & Wallace 1902.10186; Wiegreffe & Pinter 1908.04626) and names no others
  it opened. I did not add sources to game the count, per the standard that
  source composition is an evidence requirement and that a writer cites only
  what was read. The warning is non-blocking under this series' `strict: false`.
  This is the open question below.

The earlier W-SENTENCE-DENSITY (a 47-word sentence in the Scope note) was fixed
by splitting; no density or banned-term warnings remain (mechanism/em-dash/
leverage counts are 0).

## Both figures captured as source assets
Fig. 1 (BLEU vs. sentence length) and Fig. 2 (four alignment matrices) were
rasterized from the primary PDF (arXiv:1409.0473, pp. 5 and 6) via `nb asset`,
inspected, and cited with the paper's verbatim captions preserved in
`data-nb-note`. Panel (a)'s European-Economic-Area / zone-economique-europeenne
reordering is legible.

## Open question for the orchestrator (evidence)
The paper template floor is 8 sources (series.yaml `min_sources: 8`); the
evidence record delivers 4. The article's argument is fully supported by those
four, but the floor warning will persist until the researcher supplies at least
four more genuinely-read sources. Natural, in-scope candidates the evidence
already alludes to but did not open: the prior fixed-vector encoder-decoders the
paper improves on (Cho et al. 2014, arXiv:1406.1078; Sutskever et al. 2014,
arXiv:1409.3215) and later attention-interpretability follow-ups. If the floor
must be met for this edition, this needs a new researcher artifact — I did not
expand the claim set independently. Please advise whether to (a) accept the
publishable draft with the standing W-SOURCES-MIN warning, or (b) route back to
the researcher for additional sources.
