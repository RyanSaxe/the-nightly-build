# researcher brief: paper-of-the-day/neural-machine-translation-attention (01)

Inputs:
  ../../editorial-direction.md
  ../../commission.md
Output: researcher/01/evidence.md

Read the primary paper in full before anything else: Bahdanau, Cho, Bengio,
"Neural Machine Translation by Jointly Learning to Align and Translate"
(arXiv:1409.0473, ICLR 2015).

Research questions:
- The exact model: the additive alignment score, the context vector
  `c_i = sum_j alpha_ij h_j`, the softmax alignment weights, and the bidirectional
  encoder. Capture the equations verbatim enough to set them, with section
  locators.
- The two figures the claim turns on: Fig. 2 (BLEU vs sentence length,
  RNNsearch vs RNNenc, the fixed-vector degradation) and Fig. 3 (the
  English-French alignment matrices, including the documented non-monotonic
  adjective-noun reordering). Record exactly where each lives in the paper and
  what it shows, as a Source asset entry (what a crop must retain/omit).
- The headline results in the paper's tables: BLEU for RNNsearch-50 vs RNNenc,
  behavior on long sentences. Verify each number against the paper's own table.
- The after-record: (a) that attention became the core of the Transformer
  ("Attention Is All You Need," 2017) — one or two sentences, cited, not a
  survey; (b) the explanation debate — Jain & Wallace, "Attention is not
  Explanation" (NAACL 2019, arXiv:1902.10186) and Wiegreffe & Pinter, "Attention
  is not not Explanation" (EMNLP 2019, arXiv:1908.04626). Read each far enough to
  state precisely what each claims about whether attention weights explain a
  model's output, and where they disagree.

Numbers section: every BLEU/length figure the article may state, traced to its
owner. Source assets: Fig. 2 and Fig. 3 of Bahdanau et al., described for
capture. Contradictions: the alignment-as-explanation dispute is the central
one; record both sides fairly. min_sources 8. Resolve every URL to the
document's own page (arXiv abs pages, ACL Anthology pages), never a PDF fetch
endpoint.
