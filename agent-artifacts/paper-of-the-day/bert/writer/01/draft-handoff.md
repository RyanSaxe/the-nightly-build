# Draft handoff: paper-of-the-day/bert (01)

## The one act of original work
The piece separates BERT's two pretraining claims by reading BERT's own Table 5
forward: the No-NSP row barely moves while the "LTR & No NSP" row collapses MRPC
(86.5 to 77.5) and SQuAD (87.9 to 77.8), isolating bidirectional masking as the
choice the recipe depends on; it then pins the NSP refutation to RoBERTa's
matched-data Table 2 rather than its five-change headline model, converting the
common "RoBERTa proved NSP useless" shorthand into the narrower claim the
evidence actually supports (the loss is unnecessary once the input format is
fixed), with ALBERT supplying why (a plain NSP head scores 52.0% on order, near
chance). The reconstruction is visible in three original house charts and the
dev/test separation is held throughout.

## Framing-precision flags (all held as instructed)
- NSP claim cited to RoBERTa Table 2 (matched data), not the headline model;
  the segment-pair vs Full/Doc-Sentences confound is stated explicitly in the
  "second-claim-fails" section and in chart 2 (all four input rows retained).
- BERT dev vs test kept strictly separate and labeled: the GLUE test table uses
  the printed 8-task Average column (74.0 / 75.1 / 79.6 / 82.1) with a caption
  noting it is a different aggregation from the 80.5 leaderboard figure; all
  ablation and RoBERTa/ELECTRA numbers are labeled development set and never
  compared across the line.
- The LTR & No-NSP collapse is used to isolate bidirectionality (chart 1).
- MLM objective set inline as annotated math and operated on: the sum over the
  masked set forces the ~15%-supervision fact that ELECTRA's efficiency section
  (chart 3) later spends; the both-sided conditioning set is contrasted with
  GPT's left-only factorization set inline.

## Charts (3 built, all original reconstructions from the evidence series)
- chart-1: BERT Table 5 ablation (bidirectionality collapse). Inspected.
- chart-2: RoBERTa Table 2 input-format / NSP, all four rows. Inspected.
- chart-3: ELECTRA GLUE-vs-FLOPs efficiency curve, log-x. Inspected; relabeled
  once to clear an overlapping-label cluster in the top-right.
No arXiv figure images were lifted. The abstract card is the only verbatim
reproduction.

## Proof
`./nb check ... --series paper-of-the-day --library /home/user/library-checkout`
(links included): BLOCK: 0, WARN: 0, PUBLISHABLE. Stamped: 2609 words, 8
sources (all primary), 11 min. Zero em-dashes; banned-term counts clear.

## Open questions for the editor
- GPT source (s2) uses the OpenAI CDN PDF URL. It resolved in the link proof,
  but the researcher's evidence noted the fetcher received it as binary and read
  the text from a UBC mirror; if the CDN link is ever flaky, the mirror
  (https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf) is
  the fallback.
- The template-mandated abstract card reproduces BERT's published abstract
  verbatim. The evidence record preserved its load-bearing figures (80.5 GLUE,
  +7.7, MultiNLI 86.7, eleven tasks) but not the full abstract string; the
  SQuAD v1.1 93.2 / v2.0 83.1 sentence is reproduced from the paper's own
  abstract text and is worth a final glance against the source.
