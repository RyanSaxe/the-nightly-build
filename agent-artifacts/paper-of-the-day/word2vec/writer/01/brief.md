# writer brief: paper-of-the-day/word2vec (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the paper, the angle, boundaries, recent shapes to break
  ../../writing-coach/01/voice-guide.md     the craft standard and licenses for this piece
  ../../researcher/01/evidence.md           the complete evidence record; the only claim set available
  the initialized article and its .nb-context (template contract + furniture catalogs)
Output: agent-artifacts/paper-of-the-day/word2vec/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/word2vec/library/paper-of-the-day/word2vec.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

The article file to edit is at:
  .nb-work/paper-of-the-day/word2vec/library/paper-of-the-day/word2vec.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus:
- The evidence record surfaces a genuine complication for the standard telling: the
  King−Man+Woman≈Queen vector-offset example is attributed by word2vec's own paper to
  Mikolov, Yih & Zweig 2013 (NAACL), a paper on RNN LM embeddings that predates
  CBOW/skip-gram. Give this its due weight; it is a strong candidate for the piece's
  spine.
- Treat every original Google-News accuracy figure as the paper's own report, not a
  verified reproduction (the corpus/vectors were never released) — say so where you lean
  on such a number. The Levy open-corpus retrains are the closest to independent.
- Address the live three-paper disagreement (Baroni 2014 vs Levy & Goldberg CoNLL 2014,
  with Levy/Goldberg/Dagan 2015 as one lab's resolution) rather than treating 2015 as the
  final word.
- Set nb-meta harness and writer model = sonnet. Fill the required paper-template sections
  once; outline the reasoning before naming any flexible sections so no prior paper-desk
  outline becomes this one's template.
