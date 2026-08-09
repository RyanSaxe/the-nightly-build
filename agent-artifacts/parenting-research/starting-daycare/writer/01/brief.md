# writer brief: parenting-research/starting-daycare (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, article template, series prompt
- ../../commission.md — the decision, the evidence tiers, and the desk close
- ../../writing-coach/01/voice-guide.md — how this appraisal should sound
- ../../researcher/01/evidence.md — the verified studies, effect sizes, contradictions, and cautions
- article: .nb-work/parenting-research/starting-daycare/library/parenting-research/starting-daycare.html (initialized; edit it)
- template context: .nb-work/parenting-research/starting-daycare/.nb-context/ (contract, runtime assets, furniture)

Output: draft-handoff.md (this directory)

Proof: ./nb check .nb-work/parenting-research/starting-daycare/library/parenting-research/starting-daycare.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

The evidence revised the commission's angle in three ways the piece must follow. Write to the evidence, not to the commission where they differ:

1. The near-term infection effect is real for respiratory illness and otitis media (respiratory IRR falls from 1.61 in early care to 0.79 later; otitis 1.62 to 0.57), but the gastrointestinal effect is small and net-neutral over years (first-year IRR 1.13, no six-year excess, null in Côté). Do not present a large, near-certain GI effect. The honest near-term claim is more respiratory infections and ear infections early, with the excess narrowing later.
2. The "more early wheeze, maybe less later asthma" reading does not survive. The asthma protection is a narrow ages-3-5 window that dissolves by school age (Caudri aOR 0.99; Swartz pooled OR 0.98, not significant). Carry the finding as a shift in the timing of wheeze, not a durable change in asthma risk, and say what the design cannot establish (all observational, bounded by family selection; no randomized evidence exists at any tier).
3. The desk-close safety flag as the commission worded it is not supported: no accessible pediatric-body guidance advises high-risk infants to avoid group care in RSV season. Build the close on what the AAP guidance actually says (risk factors, breastfeeding, hygiene) and route the individual high-risk decision (an immunocompromised or premature infant) to the pediatrician, without inventing a guideline.

This round's focus:
- 1200 to 3000 words, min 8 sources. Steelman the contested claims before weighing them; the evidence's Contradictions section carries four. Give each effect size a comparison the reader can picture, and mark the randomized-vs-observational line.
- Where a shape helps (an infection rate ratio that reverses over age, or the asthma OR by age band), a table or `nb chart` earns its place, built only from the evidence's verified series; inspect and cite it.
- Do not open on the desk's recent "the dangerous part of X is Y" reversal mold; write one lean dek that commits to the piece's actual finding and does not use the three-clause comma-and-"and" form. Name the article's one act of original work in the handoff. Run the display-text pass, then `nb stamp` and the exact `nb check` (links included) until BLOCK: 0.
