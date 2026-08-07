# editor review-brief: paper-of-the-day/bert (editor/01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../writer/01/brief.md                — the exact writer brief (leakage check)
  ../../writing-coach/01/voice-guide.md   — craft (reviewer cross-examining tables)
  ../../researcher/01/evidence.md         — the evidence record
  ../../writer/01/draft-handoff.md        — original-work sentence + open questions
  ../../../../library/paper-of-the-day/bert.html   — the article to review
  ../../../../.nb-context/                 — effective template contract + furniture
Output: editor/01/editorial-review.md

Round focus (a false central claim is the top risk):
- NSP framing: confirm the "NSP unnecessary" claim is cited to RoBERTa TABLE 2
  (matched-data isolation), NOT the five-change headline model, and that the
  input-format confound (BERT's own No-NSP kept segment-pair input) is stated;
  ALBERT's 52.0% sentence-order probe supplies the mechanism. Confirm the
  bidirectionality claim rests on the LTR&No-NSP collapse.
- NUMBER HYGIENE: confirm BERT dev vs test/leaderboard numbers are never mixed;
  the Table-1 8-task average (82.1) is labeled distinct from the 80.5 leaderboard
  figure. Recompute/spot-check the chart numbers against the evidence (Table 5:
  MRPC 86.7→77.5, SQuAD 88.5→77.8; RoBERTa Table 2; ELECTRA GLUE-vs-FLOPs) and
  read each of the 3 reconstructed charts as a reader (axes, log scale, honest).
- Verify the writer's two open questions: (1) the GPT source href resolves to a
  stable page; (2) the abstract card's verbatim SQuAD 93.2 / 83.1 sentence
  matches the source — check display text descriptor by descriptor.
- MLM objective set as math and operated on (the ~15%-supervision fact ELECTRA
  attacks); both-sided vs GPT left-only factorization stated correctly.
- Charts are original reconstructions (no arXiv images lifted); each caption
  cites its data source. Verdict before Sources. Formula/display: no author
  roll-call opener; headline off the recent paper-of-the-day molds; check deks
  vs the recent library.
Make surgical cuts directly; run ./nb stamp after direct cuts. Route new prose,
charts, markup, or proof to the writer. Decide approve | revise.
