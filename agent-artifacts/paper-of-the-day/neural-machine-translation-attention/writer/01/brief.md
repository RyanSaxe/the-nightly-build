# writer brief: paper-of-the-day/neural-machine-translation-attention (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the paper, the angle, boundaries, recent shapes to break
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this piece
  ../../researcher/01/evidence.md           the complete evidence record; the only claim set available
  the initialized article and its .nb-context (paper template contract + furniture catalogs)
Output: agent-artifacts/paper-of-the-day/neural-machine-translation-attention/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/neural-machine-translation-attention/library/paper-of-the-day/neural-machine-translation-attention.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/paper-of-the-day/neural-machine-translation-attention/library/paper-of-the-day/neural-machine-translation-attention.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus:
- Set the additive-attention math as objects the prose reasons from (context vector,
  softmax alignment weights, the additive score), not restated in words. Use the evidence
  record's verbatim equations and locators.
- Bring in Fig. 2 (BLEU vs sentence length) and Fig. 3 (the alignment matrix) as source
  assets via `nb asset`, captured from the primary, with factual cited captions that say
  what each settles. Inspect the captured asset and the rendered page. No external image
  URLs; no invented figures.
- Handle the central analytic nuance the evidence flags: the "attention is/ is not
  explanation" debate (Jain & Wallace; Wiegreffe & Pinter) was run on later BiLSTM
  classification/QA models, NOT on Bahdanau's 2015 translation model. Applying it to
  Fig. 3's alignments is an analytic bridge the piece must state explicitly as its own
  reasoning, never as a claim either 2019 paper makes about this paper. This honesty is
  the piece's original work; make it visible.
- Keep the paper's own generalization honest: one language pair (En->Fr, WMT'14), an RNN
  encoder-decoder later superseded. The verdict commits and marks its own boundary.
- Break the recent paper-desk dek mold (author-surnames + verb opener; "the after-record
  narrows/reframes it" closer). Find this piece's own claim. Outline the reasoning before
  naming flexible sections so no prior paper-desk outline becomes this one's template.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8"; fill the required
  paper-template sections (abstract card + orientation + sources) once.
