# writer brief: paper-of-the-day/neural-machine-translation-attention (02)

Inputs:
  ../../editorial-direction.md
  ../../writing-coach/01/voice-guide.md
  ../../researcher/02/evidence.md           the NEW record (8 sources); use this, not 01
  ../../writer/01/draft-handoff.md          prior handoff
  the article: .nb-work/paper-of-the-day/neural-machine-translation-attention/library/paper-of-the-day/neural-machine-translation-attention.html
Output: writer/02/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/neural-machine-translation-attention/library/paper-of-the-day/neural-machine-translation-attention.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

Reason for this round: close the W-SOURCES-MIN warning (the series floor is 8) by
integrating the four newly-read predecessor/refinement sources where they genuinely bear —
not as padding citations. Preserve all settled work from writer/01.

Integrate from researcher/02:
- The fixed-vector bottleneck the paper answers: cite Cho et al. 2014 (arXiv:1406.1078, the
  RNN Encoder-Decoder whose single summary vector c conditions every output step, and the
  GRU) and Cho/Bahdanau et al. 2014 (arXiv:1409.1259, which documents firsthand the rapid
  degradation on long sentences that Fig. 2 answers). Attribute the long-sentence bottleneck
  specifically to the RNN Encoder-Decoder line.
- Handle the new tension honestly (the evidence's Contradictions): Sutskever et al. 2014
  (arXiv:1409.3215) explicitly claim their LSTM "did not have difficulty on long sentences"
  (crediting reversed inputs). Acknowledge this contrary result rather than implying all
  fixed-vector seq2seq degrades; the point is architecture-specific. Cross-paper BLEU is not
  head-to-head — do not compare BLEU across these different setups as if it were.
- After-record: cite Luong, Pham, Manning 2015 (arXiv:1508.04025) as the immediate
  refinement of Bahdanau's attention (global/local, score functions, input feeding).

Do not expand the claim set beyond what these sources support, do not disturb the focal
equations, the captured Fig. 1/Fig. 2 assets, Table 1 figures, or the explanation-debate
verdict — all still valid. Keep nb-meta dek identical to the rendered dekline; harness
"claude-code-routine" / model "Opus 4.8". Re-run the full proof to BLOCK: 0 with
W-SOURCES-MIN cleared (>= 8 sources). Note in the handoff exactly which sources you added
and where.
