# writer brief: parenting-research/infant-iron (02) — targeted revision

Inputs:
  ../../editorial-direction.md
  ../../writing-coach/01/voice-guide.md
  ../../researcher/01/evidence.md
  ../../editor/01/editorial-review.md          apply its Required-work items exactly
  ../01/draft-handoff.md
  the article: .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html
Output: agent-artifacts/parenting-research/infant-iron/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Apply ONLY the editor's three required items (the editor already made all direct cuts and
re-stamped; do not redo them or expand the claim set):
1. Headline overclaim: the headline "no measured benefit to infant development" is too broad —
   "development" includes behavior, and the piece's own 2026 follow-up reports a MEASURED
   behavioral benefit (P=.006). Narrow "development" → "cognitive" so the headline matches
   what the evidence supports. Sync the change across the <h1>, the <title>, and the nb-meta
   JSON (title/headline) so all three are identical; the dek already says "no cognitive gain",
   so keep the dek consistent with the narrowed headline.
2. Thin the over-used "X, not Y" antithesis close: recast 2-3 paragraph endings that reuse
   that shape, keeping only the two load-bearing ones. Cuts/recasts only; do not add claims.
3. Re-run `nb stamp` and the full proof with links until BLOCK: 0.

Confirm nb-meta dek and the rendered dekline stay identical. Write writer/02/draft-handoff.md
with one line per required item resolved and the final proof result.
