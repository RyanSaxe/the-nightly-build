# writer brief: unbiased/iran-war-powers (02) — repoint one citation per editor/01

Inputs:
- ../01/brief.md — original writer brief (scope, strict rules, voice)
- ../../writing-coach/01/voice-guide.md — voice guide (unchanged)
- ../../researcher/02/evidence.md — the round-02 verification (the resolving Van Hollen page + attribution advice); researcher/01/evidence.md still holds for everything else
- ../../editor/01/editorial-review.md — the one required item (and note the editor already made two direct cuts + stamped)
- article: .nb-work/unbiased/iran-war-powers/library/unbiased/iran-war-powers.html (edit in place)
Output: .nb-work/unbiased/iran-war-powers/agent-artifacts/unbiased/iran-war-powers/writer/02/draft-handoff.md
Proof: ./nb check .nb-work/unbiased/iran-war-powers/library/unbiased/iran-war-powers.html --series unbiased --library /tmp/claude-0/-home-user-the-nightly-build/2d5b8802-c025-5b79-bf1d-234ffd5a3463/scratchpad/library-checkout

Apply exactly this one repair; change nothing else the editor left settled (including the editor's two cuts).

- The Position B champion quote "The Constitution gives Congress – and Congress only – the power to declare war" was cited to s17 but does NOT resolve there. Repoint it to the owning primary where it is verbatim:
  https://www.vanhollen.senate.gov/news/press-releases/van-hollen-statement-on-war-powers-resolution
  (data-nb-kind="primary"; Van Hollen's own Senate office statement, dated February 13, 2020, on S.J.Res.68, 116th Cong.).
- CRITICAL attribution fix: because this is a 2020 statement, the surrounding prose must present the line as Van Hollen's STANDING constitutional position in his own words — NOT as something he said about the 2026 strikes or the S.J.Res.180 vote. Adjust the framing sentence minimally so it is honest about that (e.g., attribute it as his long-held constitutional principle), without implying a 2026 date. Do not fabricate a date.
- If s17 was ALSO used elsewhere for the 2026 event framing (the cosponsor push / "illegal war of choice" line), you may keep s17 as a secondary for THAT 2026 framing if the live page supports it; otherwise leave the 2026 framing to sources that resolve. Preserve the strict composition (total >=10; primary >=4; secondary >=3). This is a like-for-like primary swap.

Then re-run the FULL proof WITH links until BLOCK: 0, and redo the display-text self-test on the changed citation (exact quote, kind=primary, href resolves, attribution not tied to 2026). Write draft-handoff.md with the one item resolved and the final proof result. Do not push to git.
