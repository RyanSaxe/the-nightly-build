# writer brief: parenting-research/infant-flu-vaccine (02)

Inputs:
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/editor/01/editorial-review.md  — the required changes (Skeptic + Required work)
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/researcher/02/evidence.md  — the corrected evidence (Hoberman both seasons well matched; swing = low-incidence imprecision; CDC owns the general match point)
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writer/01/draft-handoff.md  — your prior draft
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writing-coach/01/voice-guide.md
  Article to edit: /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/library/parenting-research/infant-flu-vaccine.html  (already carries the editor's 2 direct edits)

Output:
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writer/02/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/parenting-research/infant-flu-vaccine/library/parenting-research/infant-flu-vaccine.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/42af37e2-ce88-5a16-a49b-bb7fb5609b03/scratchpad/library

Apply the editor's required change using researcher/02's corrected evidence.
Redraft exactly three places and touch nothing else settled:
1. The section-2 swing explanation: remove the antigenic-match framing ("one winter
   the strain resembled the vaccine, the next it did not"). The corrected account:
   both seasons were well matched with the vaccine strains; little influenza
   circulated the second season (placebo attack rate 3.3% vs 15.9% the first), so
   very few cases produced an imprecise, near-null, zero-crossing estimate
   (-7%, 95% CI -247% to 67%, on 4 placebo cases). The swing shows how uncertainly
   direct efficacy is pinned down in the youngest age band, not a demonstrated match
   difference.
2. The verdict line ("a poorly matched one, as in 2000-01, can erase it") is
   factually wrong (2000-01 was well matched). Recast around incidence/imprecision.
3. The closer's "how well this year's strains match the vaccine": either drop the
   match framing, or keep a general year-to-year-effectiveness point ONLY if cited
   to CDC (researcher/02's CDC source) and detached from the Hoberman example.

Do not introduce new claims beyond researcher/02's record. Preserve all other
settled prose and the table/chart. If a source is added (CDC), number it in
first-citation order with correct data-nb-kind and update nb-meta counts via nb
stamp. Re-run the full proof to BLOCK: 0. Add one line per editorial request
resolved in the handoff.
