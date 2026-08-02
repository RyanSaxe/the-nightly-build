# writer brief: parenting-research/infant-iron (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       angle, boundaries, the central honesty about effect size
  ../../writing-coach/01/voice-guide.md     evidence-communication craft and licenses
  ../../researcher/01/evidence.md           the evidence record; the only claim set available
  the initialized article and its .nb-context (article template contract + furniture catalogs)
Output: agent-artifacts/parenting-research/infant-iron/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Article to edit:
  .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html
Article template; band 1200-3000 words; min 8 sources. Iterate proof with
--no-check-links, finish with links.

This round's focus (grounded in the evidence record):
- The spine is the record's central honesty: treating an infant who is ALREADY anemic
  reliably reverses concurrent developmental delay (Idjradinata 1993), but PREVENTIVE
  supplementation in iron-replete/average-risk infants — the decision most households
  actually face — shows no measurable cognitive benefit in the largest meta-analysis
  (Pasricha 2013, n=42,306) and the closest-matched RCT (Chmielewska/Svensson, JAMA
  Pediatrics 2024), even as it reliably reduces anemia. The June-2026 3-year follow-up
  found a behavioral benefit but at 40% attrition and the authors call for replication —
  keep "no effect" open, not closed. Name study design in the same sentence as its finding
  (per the voice guide).
- CAVEAT to honor: the researcher could NOT read the AAP 2026 clinical report itself (403
  everywhere); it is the current US standard superseding the 2010 report. Claims sourced
  only to the 2026 report rest on AAP's own consumer restatement + an independent summary —
  attribute those precisely and do not overstate them as the report's graded evidence. If
  you can fetch the 2026 report with different tooling, do so and cite it directly; if not,
  keep the caveat visible.
- Put clinician-boundary language to work at the exact decision fork (dosing, diagnosed
  anemia, preterm/LBW infants — the AAP gives preterm a different regimen), not as a closing
  disclaimer. The malaria-context safety trial (Sazawal 2006) is bounded as inapplicable to
  this reader; use only to show iron is not universally benign.
- End on what the evidence might change at home (iron-rich/iron-fortified first foods; the
  screening context) vs what belongs to a pediatrician. Do not reuse the desk's recent
  relative/absolute sentence mold or the "in the population actually tested" opener.
- Set nb-meta harness and writer model = sonnet.
