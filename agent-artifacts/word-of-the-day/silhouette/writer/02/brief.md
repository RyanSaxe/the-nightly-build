# writer brief: word-of-the-day/silhouette (02)

Inputs:
- editor/01/editorial-review.md — the required fix to apply (decision: revise, owner: writer)
- researcher/01/evidence.md — the claim set (check which source owns the 1798 date)
- writer/01/draft-handoff.md, editorial-direction.md (artifact root)
- The article at `library/word-of-the-day/silhouette.html` (workspace root)
Output: writer/02/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/word-of-the-day/silhouette/library/word-of-the-day/silhouette.html`   (file arg only)
  `./nb check .nb-work/word-of-the-day/silhouette/library/word-of-the-day/silhouette.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Run until `BLOCK: 0`.

Apply the editor's one required fix, nothing more:
- The present-use sentence claims "the OED and etymonline place it at 1798, in
  The Monthly Review." Etymonline (s4) does NOT own the 1798 date — it dates the
  English portrait sense to 1792 (French 1766). Remove etymonline from the 1798
  clause. The 1798 date is owned by the OED / Monthly Review (s5). Keep the
  first-use range as MW 1783 (s1) vs OED 1798 (s5).
- If removing that reference leaves etymonline (s4) still cited elsewhere (e.g.
  for the 1792 date), keep it and do not renumber. If s4 becomes entirely
  unused, remove its source entry and renumber contiguously; update nb-meta
  `sources` accordingly.
- Preserve all other settled prose. The byline already reads "3 min read"
  (correct) — leave it. Re-run the full proof (links on) until BLOCK: 0. Write
  writer/02/draft-handoff.md with one line describing the fix.
