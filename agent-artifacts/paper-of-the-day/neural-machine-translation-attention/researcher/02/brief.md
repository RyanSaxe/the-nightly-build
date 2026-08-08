# researcher brief: paper-of-the-day/neural-machine-translation-attention (02)

Inputs:
  ../../editorial-direction.md
  ../../commission.md
  ../../researcher/01/evidence.md           the prior evidence record — preserve all still-valid work
Output: researcher/02/evidence.md  (a complete new record that preserves 01's findings and adds the below)

Reason for this round: the series source floor is min_sources 8 (paper template); the 01
record supplies 4 read sources. Do NOT pad. Genuinely read the following in-scope sources —
each is part of this paper's own record (the encoder-decoder predecessors it builds on and
the fixed-vector bottleneck it fixes, plus the immediate attention refinement) — and add
them with full Sources entries, classification, locators, and any figure/number they own:

- Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk, Bengio (2014), "Learning
  Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
  (arXiv:1406.1078) — the RNN Encoder-Decoder + GRU that Bahdanau's model extends; the
  fixed-length context vector it later replaces.
- Sutskever, Vinyals, Le (2014), "Sequence to Sequence Learning with Neural Networks"
  (arXiv:1409.3215) — the other fixed-vector seq2seq predecessor and its long-sentence
  behavior (note the reversed-input trick and BLEU).
- Cho, Bahdanau, et al. (2014), "On the Properties of Neural Machine Translation:
  Encoder-Decoder Approaches" (arXiv:1409.1259) — documents the encoder-decoder's
  degradation on long sentences, the exact motivation Fig. 2 answers.
- Luong, Pham, Manning (2015), "Effective Approaches to Attention-based Neural Machine
  Translation" (arXiv:1508.04025) — global vs. local attention, the immediate refinement of
  Bahdanau's mechanism; part of the honest after-record.

For each: read the paper (not a summary), record what it establishes firsthand, precise
locators, and any figure or BLEU number the article might use. Update the Numbers and
Contradictions sections if these sources bear on them (e.g. Sutskever's reversed-input BLEU;
whether 1409.1259's long-sentence finding is by the same group). Keep every 01 entry that
remains valid. Resolve every URL to the document's own arXiv abs page. Target: >= 8 total
genuinely-read sources in the record. Report the new total and anything that changes the
01 interpretation.
