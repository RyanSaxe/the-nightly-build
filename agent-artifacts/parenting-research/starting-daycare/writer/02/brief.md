# writer brief: parenting-research/starting-daycare (02)

Inputs:
- ../01/draft-handoff.md and the article as the editor left it (edit in place)
- ../../editor/01/editorial-review.md — the three required source-metadata items
- ../../researcher/02/evidence.md — the corrected citations and the s8 content flag

Output: draft-handoff.md (this directory, writer/02)

Apply exactly these, nothing more:

1. Fix the three printed source entries to the citations researcher/02 verified:
   - s2 → de Hoog MLA, Venekamp RP, van der Ent CK, et al., BMC Medicine
     2014;12:107 (journal was wrong; URL and figures unchanged).
   - s3 → Hullegie S et al., "First-year Daycare and Incidence of Acute
     Gastroenteritis," Pediatrics 2016;137(5):e20153356 (lead author and journal
     were wrong; URL and figures unchanged).
   - s8 → Vandell DL, Burchinal M, Pierce KM, "Early Child Care and Adolescent
     Functioning at the End of High School," Developmental Psychology
     2016;52(10):1634-1645 (URL kept; author/journal/year corrected).
2. The s8 outcome is measured at the end of high school (mean age ~18), not age
   15. Change every "at age 15" (and any age-15 framing tied to s8) in the body
   and any display text to end of high school (~age 18).
3. Drop the claim that more hours of care predict more risk-taking or impulsivity
   at 15. The resolved s8 paper found no significant hours-to-behavior
   association, so that claim is no longer sourced. Keep the quality-to-cognition
   magnitudes (d = .08 to .16) and the correlational caveat, which the resolved
   paper owns verbatim. Do not re-source the dropped claim to s8; if you retain
   any hours-to-behavior point, it must be accurately attributed to a source that
   owns it at the age it states, or cut.

Do not change other claims or items. Then run the display-text pass on what you
changed, `nb stamp`, and the exact proof with links until BLOCK: 0:

./nb check .nb-work/parenting-research/starting-daycare/library/parenting-research/starting-daycare.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

Write one line per editor item resolved in draft-handoff.md, and note the dropped claim.
