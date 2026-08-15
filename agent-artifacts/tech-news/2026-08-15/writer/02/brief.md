# writer brief: tech-news/2026-08-15 (02)

Inputs:
- editorial-direction.md, commission.md, writing-coach/01/voice-guide.md
- researcher/02/evidence.md — the corrected record with the three fixes
- editor/01/editorial-review.md — the findings routed to you (and the editor's
  own already-applied direct edits, which you preserve)
- the article (already partly edited by the editor) at
  .nb-work/tech-news/2026-08-15/library/tech-news/2026-08-15.html
- writer/01/brief.md and the contract under
  .nb-work/tech-news/2026-08-15/.nb-context/

Output: writer/02/draft-handoff.md (do not overwrite writer/01)

Proof: ./nb check --series tech-news .nb-work/tech-news/2026-08-15/library/tech-news/2026-08-15.html --library /home/user/library-checkout

Apply exactly the editor's three routed findings using researcher/02 evidence,
preserving the editor's already-applied direct edits and not expanding the claim
set:
1. Replace the DeepSeek misquotation with the verbatim source sentence and the
   corrected locator the evidence now records.
2. Re-cite the Gemini GDPVal-AA figures (1,525 / +103 and the three rival scores)
   to the leaderboard page the evidence resolved
   (artificialanalysis.ai/evaluations/gdpval-aa), keeping the Intelligence Index
   page as the source only for its own figures.
3. Replace the weak science item with the fresher, primary-readable AMOC item
   (van Westen et al., Nature Climate Change, about August 13) the evidence
   recommends, written from the evidence record. If you instead keep the fuel-cell
   item, apply every correction the evidence records (first author Gao, platinum
   loading kept high at about 40 wt% rather than reduced, and 82.5% retention not
   85%). The AMOC replacement is preferred for freshness and significance.

Rerun the full proof (links included), `nb stamp` before the final check, until
BLOCK: 0. Write writer/02/draft-handoff.md with one line per resolved item.
