# review-brief: paper-of-the-day/neural-machine-translation-attention (editor/01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../writer/01/brief.md                  the writer's round-1 brief (for prompt-leak detection)
  ../../writing-coach/01/voice-guide.md     reconstruction craft and licenses (read first)
  ../../researcher/02/evidence.md           the CURRENT evidence record (8 sources) — use this, not 01
  ../../writer/02/draft-handoff.md          original-work sentence + what round 2 changed (open on third read)
  the article: .nb-work/paper-of-the-day/neural-machine-translation-attention/library/paper-of-the-day/neural-machine-translation-attention.html
  the .nb-context/ paper template contract + furniture catalogs

Recent-pattern notes (break formulas):
- The paper desk's recent deks open on author surnames + verb and close on an "after-record
  narrows/reframes it" clause. Confirm the headline/dek and section headings do not reuse
  that skeleton.

This round's focus (full three-read gate; this is the first editorial read of this article):
- Skeptic: verify the reconstruction math (context vector c_i = sum_j alpha_ij h_j, the
  softmax alignment weights, the additive score) is correct and correctly located, and that
  every Table 1 BLEU figure (e.g. RNNsearch-50 26.75/... vs RNNenc) matches the paper's own
  table. Verify the two captured source assets (Fig. 2 BLEU-vs-length; Fig. 3 alignment
  matrix) show what the prose says they settle; captions factual and cited.
- The central analytic bridge must be explicit and honest: the "attention is/ is not
  explanation" debate (Jain & Wallace; Wiegreffe & Pinter) was run on later classification/
  QA models, NOT on Bahdanau's 2015 translation model. Confirm the piece states this as its
  own reasoning, never as a claim either 2019 paper makes about the focal paper.
- New this round: the four integrated predecessor/refinement sources (Cho 1406.1078; Cho/
  Bahdanau 1409.1259; Sutskever 1409.3215; Luong 1508.04025). Confirm each is cited where it
  genuinely bears, not padded; that the long-sentence bottleneck is attributed to the RNN
  Encoder-Decoder line; that Sutskever's contrary "no difficulty on long sentences" result
  is acknowledged; and that no cross-setup BLEU is compared head-to-head as if comparable.
- Reader: what does the piece give beyond the sources? Compare with the original-work
  sentence. Reread the headline as the largest claim.
- Open every citation href as printed; audit data-nb-kind labels.

After any direct cuts, run `nb stamp` (the writer runs the full proof). Route new-prose or
new-evidence needs to the writer/researcher with the exact finding named.
