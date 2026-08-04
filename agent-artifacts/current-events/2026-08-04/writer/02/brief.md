# writer brief: current-events/2026-08-04 (02) — repoint two citations per editor/01

Inputs:
- ../../editorial-direction.md — citation standard
- ../01/brief.md — the original writer brief (scope, boundaries)
- ../../writing-coach/01/voice-guide.md — voice guide (unchanged)
- ../02/../researcher/02/evidence.md — the NEW re-sourcing evidence (round 02); combine with ../researcher/01/evidence.md for everything else
- ../../editor/01/editorial-review.md — the two required items to resolve
- the article: .nb-work/current-events/2026-08-04/library/current-events/2026-08-04.html (edit in place)
Output: .nb-work/current-events/2026-08-04/agent-artifacts/current-events/2026-08-04/writer/02/draft-handoff.md
Proof: ./nb check .nb-work/current-events/2026-08-04/library/current-events/2026-08-04.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/2d5b8802-c025-5b79-bf1d-234ffd5a3463/scratchpad/library-checkout

Apply exactly the two editor-required repairs, using researcher/02's verified primaries. Change nothing else in the prose (the editor already read the rest clean); preserve the article's structure, item selection, and all other citations.

1. Item 1 (SCOTUS mail-ballot/citizenship EO):
   - Repoint the Sauer quotation to the owning primary: the government's Application for a Stay in SCOTUS docket 26A124, at
     https://www.supremecourt.gov/DocketPDF/26/26A124/417370/20260727144320600_Trump%20v.%20California%20Application%20and%20Appendix.pdf
     (data-nb-kind="primary"; locator: printed page 5). CORRECT THE WORDING: it is "preempts the Executive's DELIBERATIVE policymaking" — not "deliberate". File the exact string: "It impedes the President's ability to direct his subordinates and preempts the Executive's deliberative policymaking." Do NOT conflate it with the nearby "irreparably and impermissibly impedes..." sentence.
   - Repoint the "Justice Jackson … called for that response" clause to the docket page itself:
     https://www.supremecourt.gov/docket/docketfiles/html/public/26A124.html
     (data-nb-kind="primary"). The docket entry: "Response to application (26A124) requested by Justice Jackson, due by 4 p.m. (EDT) on August 3, 2026"; the California response was filed Aug 3. Keep the display text consistent with this (state-of-play, not a predicted ruling).
   - You may keep SCOTUSblog as an additional secondary for the item if its live page still supports what it is cited for; if not, drop it. The item must still have exactly one primary + at least one independent secondary.

2. Item 2 (Blanche / anti-weaponization fund):
   - Repoint the rescission quotation and the "May 18, 2026" order date to the DOJ's own signed order:
     https://www.justice.gov/ag/media/1455261/dl?inline=
     (data-nb-kind="primary"). Exact string: "The Attorney General's May 18, 2026 Order establishing the Anti-Weaponization Fund ('Fund') is rescinded and shall have no force or effect." The order is dated August 2, 2026, signed Todd Blanche, Acting Attorney General. Do NOT conflate the rescinded May 18 fund-establishing order with the separate May 19, 2026 mutual-release order.
   - Keep NPR as an independent secondary only if its live page still supports the non-quoted framing it carries; otherwise repoint that framing to what resolves. Preserve the one-primary + one-independent-secondary composition.

After repointing: re-run the FULL proof WITH links until BLOCK: 0, and redo the display-text self-test on the two changed items (quotes/dates/kinds/hrefs). Write draft-handoff.md with one line per editor item resolved and the final proof result. Do not push to git.
