# writer brief: investing/cost-of-capital (02) — targeted revision

Inputs:
  ../../editorial-direction.md
  ../../writing-coach/01/voice-guide.md
  ../../researcher/01/evidence.md
  ../../editor/01/editorial-review.md          apply its Required-work items exactly
  ../01/draft-handoff.md                        the prior handoff
  the article: .nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html
Output: agent-artifacts/investing/cost-of-capital/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Apply ONLY the editor's two required fixes (no other changes; the editor already made all
other cuts directly and re-stamped):
1. Dek antecedent: remove "that gap, " so the dek no longer conflates the industry gap with
   the ROIC hurdle. Make the edit in BOTH the visible dek line AND the nb-meta `dek` string,
   and confirm the two are identical (the proof checks this).
2. Quotation accuracy: the book-value quote currently reads "but comes with problems"; the
   source reads "but come with problems" — correct it (or bracket) to match the source exactly.

Then run `nb stamp` and the full `nb check` (links included) until BLOCK: 0. Do not expand the
claim set or re-litigate settled cuts. Write writer/02/draft-handoff.md with one line per
required item resolved and the final proof result.
