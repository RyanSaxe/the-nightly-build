# writer brief: word-of-the-day/luddite (02)

Single-owner repair applying editor round 01's one required item.

Inputs:
- .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/editor/01/editorial-review.md  (the required item)
- .nb-work/word-of-the-day/luddite/library/word-of-the-day/luddite.html  (the article)

Output: .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/writer/02/draft-handoff.md

Required item to apply (only this; change nothing else, do not expand the claim set):
- The dek pinned the York executions on "the framework knitters" (the Nottingham
  framework-knitting trade), but the York hangings were Yorkshire croppers /
  West Riding Luddites. Replace "the framework knitters" with "the Luddites" in
  BOTH the nb-dekline prose and the nb-meta `dek` JSON (they must stay identical).

Proof: ./nb check .nb-work/word-of-the-day/luddite/library/word-of-the-day/luddite.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run `nb stamp` then the proof links-included until BLOCK: 0)
