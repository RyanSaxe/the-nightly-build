# Draft handoff: paper-of-the-day/neural-machine-translation-attention (writer 02)

## Original work (one sentence)
Unchanged from writer/01 and still carried visibly in the Scope note and the
bounded verdict: the piece makes explicit that the "attention is / is not
explanation" dispute (Jain & Wallace; Wiegreffe & Pinter) was run on later
BiLSTM classification and QA models and never on Bahdanau's 2015 translation
model, so reading it onto Figure 2's alignments is this article's own inference
rather than a claim either 2019 paper makes about this paper, and it holds
Bahdanau's modest "agree well with our intuition" apart from the stronger
explanation reading that inference invites.

## What this revision did
Sole required change: close W-SOURCES-MIN (series floor 8) by integrating the
four newly-read predecessor/refinement sources from researcher/02 where they
genuinely bear. The focal equations, both captured figures, the Table 1 numbers,
the nb-meta dek, and the explanation-debate verdict were left untouched. Source
numbers are re-assigned in first-citation order, so the three prior secondary
sources shifted (Vaswani 2→6, Jain 3→7, Wiegreffe 4→8).

## Sources added and where
- **[2] Cho et al. 2014 (arXiv:1406.1078)** — orientation ("One vector for the
  whole sentence"). Names the concrete predecessor: the RNN Encoder-Decoder
  whose single summary vector c conditions every decoder step, the fixed-vector
  design Bahdanau replaces. Locator Sec. 2.1-2.2.
- **[3] Cho, Bahdanau et al. 2014 (arXiv:1409.1259)** — long-sentence section
  opener. The same group's firsthand measurement that a fixed-length
  encoder-decoder degrades rapidly with sentence length and unknown-word count,
  i.e. the degradation curve Figure 1 answers directly. Locator Abstract.
- **[4] Sutskever, Vinyals, Le 2014 (arXiv:1409.3215)** — new bounded paragraph
  closing the long-sentence section. Handled honestly per the evidence's
  Contradictions: their reversed-input LSTM "did not have difficulty on long
  sentences", so the degradation is attributed specifically to the RNN
  Encoder-Decoder line, not to every fixed-vector model. The paragraph states
  the two results do not collide (different architectures) and explicitly
  declines to compare BLEU across the setups. Bahdanau's contribution is framed
  as removing the fixed vector outright, robust to whichever baseline one starts
  from. Locator Sec. 1.
- **[5] Luong, Pham, Manning 2015 (arXiv:1508.04025)** — after-record, as the
  immediate refinement before the Transformer paragraph: global/local attention,
  the three cheaper score functions (dot, general/bilinear, concat), input
  feeding, the shortened path, and the En-De result of its moment. En-De is
  flagged implicitly as a different pair; no head-to-head with Bahdanau's En-Fr
  numbers. Locator Sec. 3.1-3.3.

The claim set was not otherwise expanded; no focal claim, equation, figure,
table figure, or verdict was disturbed.

## Proof result
`./nb check ... --series paper-of-the-day --library <scratchpad>/library`,
links included: **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. Sources: **8**
(W-SOURCES-MIN cleared).

One intermediate W-SENTENCE-DENSITY warning (an 80-word Luong list sentence) was
fixed by splitting it into single-purpose sentences; no warnings remain. em-dash,
mechanism, and leverage counts are all 0. nb-meta dek is identical to the
rendered dekline.

## Open questions
None. The writer/01 open question (source floor) is resolved by this round.
