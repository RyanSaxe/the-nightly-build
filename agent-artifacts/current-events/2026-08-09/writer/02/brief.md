# writer brief: current-events/2026-08-09 (02)

Inputs:
- ../01/draft-handoff.md and the article as you left it (edit in place)
- ../../editor/01/editorial-review.md — the required writer item
- ../../researcher/02/evidence.md — the resolved primary URL and confirmed passage

Output: draft-handoff.md (this directory, writer/02)

Apply exactly the editor's writer item, nothing more:

- Replace the s3 href with the resolved court-hosted opinion URL (https://media.cadc.uscourts.gov/opinions/docs/2026/08/26-5123-2187096.pdf) in both the ballroom item's headline link and the s3 source entry. Keep s3's locator honest to the opinion (Part I.A.1, pp. 7-8).
- Re-cite the sentence stating the majority's Property Clause and 1912-statute (40 U.S.C. Sec. 8106) reasoning to s3 (the opinion) instead of s4 (NPR), per researcher/02's confirmed passage.

Do not expand the claim set or touch other items. Then run the display-text pass on anything you changed, `nb stamp`, and the exact proof with links until BLOCK: 0:

./nb check .nb-work/current-events/2026-08-09/library/current-events/2026-08-09.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

Write one line per editor item resolved in draft-handoff.md.
