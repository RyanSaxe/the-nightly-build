# writer brief: tech-news/2026-08-06 (02)

Purpose: apply editor round 01's required writer items using the corrected
sourcing from researcher/02. Not a rewrite.

Inputs:
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/researcher/02/evidence.md  (CURRENT complete claim set; lead item's independent accounts added)
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/editor/01/editorial-review.md  (the required items)
- .nb-work/tech-news/2026-08-06/library/tech-news/2026-08-06.html  (your draft to edit in place)
- writer/01/draft-handoff.md, editorial-direction.md, commission.md, writing-coach/01/voice-guide.md, .nb-context/

Output: .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-06/library/tech-news/2026-08-06.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root; --no-check-links while iterating, then links-included until BLOCK: 0)

Apply exactly these (from the editor review), nothing else:
(a) Item 1 (anellovirus) sourcing: the owning primary is the Nature paper
    itself. Add a truly independent account — use GEN
    (https://www.genengnews.com/topics/coronavirus/covid-19-reactivates-dormant-viruses-offering-new-clues-to-long-covid/)
    and/or NPR (https://www.npr.org/2026/08/05/g-s1-137479/long-covid-19) as
    secondary independent, with data-nb-kind="secondary". Relabel Medical Xpress
    (Boston Children's press release) and UT Dell Med (authoring institution) as
    NOT independent: they are not secondary independent accounts, so set their
    data-nb-kind correctly (they are extensions of the primary/authoring party,
    not independent) or drop them if redundant. Fix the item-1 prose that
    currently calls a press release "an independent science-news account" — it
    must name the genuinely independent outlet (GEN/NPR).
(b) Dek: recast it. The current dek ("The day's firmest new result is a
    long-COVID immunology paper rather than an AI model...") grades the
    edition's own selection instead of making a claim about the world, and
    "rather than an AI model" is the banned hedged-contrast mold. Write a dek
    that makes a claim about the anellovirus finding itself (its who/what and
    the one identifying detail), no self-reference, no hedged contrast. Sync the
    nb-meta `dek` and the nb-dekline (identical).
(c) Re-run `nb stamp` and the links-included proof until BLOCK: 0.

Keep items 2-4 and the editor's direct cuts intact; do not expand the claim set.
Record in writer/02/draft-handoff.md the changes made and the final proof result.
No git.
