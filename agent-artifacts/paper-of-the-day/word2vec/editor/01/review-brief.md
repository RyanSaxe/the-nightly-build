# review-brief: paper-of-the-day/word2vec (editor/01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../writer/01/brief.md                  the exact writer brief (for prompt-leak detection)
  ../../writing-coach/01/voice-guide.md     reconstruction craft and licenses (read first)
  ../../researcher/01/evidence.md           the evidence record (open as the skeptic requires)
  ../../writer/01/draft-handoff.md          original-work sentence (open on the third read)
  the article: .nb-work/paper-of-the-day/word2vec/library/paper-of-the-day/word2vec.html
  the .nb-context/ paper template contract + furniture catalogs

Recent-pattern notes (break formulas):
- The paper desk's recent deks/headlines follow a strong "Paper X's own result was really
  about Y" single-reversal mold, often an em-dash reversal. The underlying reckoning shape
  is the series identity, but the sentence mold is repeating — check the headline/dek do not
  reuse that exact cadence, and check the section headings against any prior paper-desk
  outline.

This round's focus (skeptic read, push hardest here):
- The spine is a strong, checkable claim: the King−Man+Woman≈Queen demo is attributed by
  word2vec's OWN paper to Mikolov, Yih & Zweig 2013 (NAACL), an earlier RNNLM model. Verify
  this against the evidence (and the cited primary if needed) — it is the piece's headline
  claim and must be exactly right.
- Verify the three mechanisms are correct, not just plausible: negative sampling as the
  softmax-cost fix; 3CosAdd and its exclusion of the query words (and the measured effect of
  that exclusion); the implicit shifted-PMI factorization (including Levy & Goldberg's own
  qualification that it is an idealized-optimum result). Confirm the piece does not overclaim
  the mechanism.
- Confirm every original Google-News accuracy figure is caveated as the paper's own
  self-report (never independently reproduced), and that the Baroni-2014-vs-Levy&Goldberg
  predict-vs-count dispute is presented with Levy/Goldberg/Dagan 2015 as one lab's account,
  not the final word.
- A WARN:1 (W-SENTENCE-DENSITY, 44 words) is intentionally left on a verbatim quote of the
  paper's own King/Queen sentence — splitting it would misquote the primary. Judge whether
  that verbatim quote earns its place; if it does, the warning stands (it is a warning, not
  a block).
- Non-blocking notes from the writer to adjudicate: (1) the abstract card anchors on
  "Efficient Estimation" alone, with "Distributed Representations" carrying negative sampling
  in its own section; (2) the verbatim abstract text was verified directly and is not stored
  as a quote in the evidence record — decide whether to request the researcher amend the
  record for the production trail.
- Audit every data-nb-kind; a different website is not an independent author.

After any direct cuts, run `nb stamp` (the writer runs the full proof). Route new-prose or
new-evidence needs to the writer/researcher with the exact finding named.
