# writer brief: current-events/2026-08-06 (02)

Purpose: apply editor round 01's required writer items using researcher/02's
corrected Michigan sourcing. Not a rewrite.

Inputs:
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/researcher/02/evidence.md  (CURRENT complete claim set; item 4 corrected)
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/editor/01/editorial-review.md  (the required items)
- .nb-work/current-events/2026-08-06/library/current-events/2026-08-06.html  (your draft to edit in place; editor already fixed items 1,2,3,5)
- writer/01/draft-handoff.md, editorial-direction.md, commission.md, writing-coach/01/voice-guide.md, .nb-context/

Output: .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-06/library/current-events/2026-08-06.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root; --no-check-links while iterating, then links-included until BLOCK: 0)

Apply exactly these (from the editor review), nothing else:
(1) Item 4 (Michigan) primary href: there is NO official MI SoS statewide
    election-night results page (researcher confirmed; electionresults.michigan.gov
    does not resolve). AP is the owning count authority. Print, as the item's
    primary (data-nb-kind="primary"), a results page that RESOLVES and lands on
    this Senate race carrying the AP count — the fetch-verified options are
    https://www.nbcnews.com/politics/2026-primary-elections/michigan-senate-results
    or https://www.clickondetroit.com/news/local/2026/08/05/abdul-el-sayed-wins-2026-michigan-us-senate-democratic-primary-election-ap-projects/
    (exact AP counts). If you can confirm the AP projects page
    (https://apnews.com/projects/election-results-2026/michigan/) resolves and
    lands on the Senate view for a reader, that is the cleanest primary. Keep a
    SEPARATE independent newsroom account as the secondary. Replace the invalid
    MVIC href in BOTH the item-4 headline <a> and source entry s10.
(2) Report the vote figures precisely from whichever results page you print,
    with the % of precincts reporting and "unofficial, pending canvass" (e.g.
    El-Sayed ~48% / Stevens ~48% / McMorrow ~4%). Keep the ~9:1 ad-spending /
    ~$65M outside-money context as a SEPARATE secondary-sourced number, distinct
    from the count.
(3) Recast the item-4 verdict: stop asserting an unsupported causal magnitude
    ("moved the result by roughly a point"); state the supportable read — a ~9:1
    ad-spending advantage failed to prevent a ~1-point loss.
(4) Recast the dek: drop the self-referential "front page" framing and the
    "held to account vs spared" theme (items 3 and 4 don't support it); make a
    claim about the day itself. Sync the nb-meta `dek` and the nb-dekline
    (identical). Check it against the banned dek molds (no comma-triad, no
    hedged contrast, no self-grading).
(5) Re-run `nb stamp` and the links-included proof until BLOCK: 0.

Keep items 1,2,3,5 and the editor's direct fixes intact; do not expand the
claim set. Record changes + final proof in writer/02/draft-handoff.md. No git.
