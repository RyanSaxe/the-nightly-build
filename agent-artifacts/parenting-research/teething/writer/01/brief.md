# writer brief: parenting-research/teething (01)

Inputs:
- .nb-work/parenting-research/teething/agent-artifacts/parenting-research/teething/editorial-direction.md
- .nb-work/parenting-research/teething/agent-artifacts/parenting-research/teething/commission.md  (the two questions, the safety framing)
- .nb-work/parenting-research/teething/agent-artifacts/parenting-research/teething/writing-coach/01/voice-guide.md
- .nb-work/parenting-research/teething/agent-artifacts/parenting-research/teething/researcher/01/evidence.md  (the only claim set; both questions primary-verified)
- .nb-work/parenting-research/teething/library/parenting-research/teething.html  (the initialized article to edit in place)
- .nb-work/parenting-research/teething/.nb-context/  (effective template contract, furniture catalogs)

Output: .nb-work/parenting-research/teething/agent-artifacts/parenting-research/teething/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/parenting-research/teething/library/parenting-research/teething.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then links-included until BLOCK: 0)

Commission decisions resolved (the evidence record flagged these — apply exactly):
- FEVER, STATED PRECISELY: do NOT write an absolute "teething never causes
  fever." The defensible, evidence-backed claim is: teething is associated with
  a small temperature rise but not a true or high fever (>38.9 C / >101 F), and
  a high fever or serious illness must never be attributed to teething. Steelman
  the contrary evidence in the prose: Nemezio et al. 2017 found no overall fever
  association (OR 1.32, 95% CI 0.88-1.96) but a significant association in the
  rectal-temperature subgroup (OR 2.82, 95% CI 1.55-5.14, only 6 studies), and
  Ramos-Jorge found a real day-of-eruption temperature rise (max 36.8 C, within
  normal range) and associated diarrhea/rash, which contradicts Macknin and AAP.
  Weigh these, do not hide them. The coach's calibrated-firmness license applies:
  a flat "no association found" and a hard safety imperative must read at
  visibly different weights.
- BELLADONNA CITATION: rest the belladonna case on the two FDA documents the
  researcher actually opened (the April 2017 Class I recall documents and the
  identified hazard / forced recall). The widely-quoted counts (~99 FAERS
  cases, 10 infant deaths, seizures) live only on FDA pages that now 404 and are
  blocked on archive: do NOT cite a non-resolving FDA URL. You may state those
  counts ONLY if an openable secondary (AAP or a reputable newsroom whose href
  resolves) carries them, attributed explicitly as secondary; otherwise omit the
  body count and let the Class I recall + identified hazard carry the point.
- ACETAMINOPHEN: do not print an exact infant dose (the AAP weight-based dosing
  table was not opened). Frame relief dosing as weight-based and
  clinician/label-directed rather than giving numbers from an unopened source.
- BENZOCAINE is primary-verified (FDA May 23 2018 letter: 119 methemoglobinemia
  cases Feb 2009-Oct 2017, 4 deaths incl. a teething infant, no demonstrated
  benefit) — use it firmly.

Form: article template, series word band 1200-3000, flex sections 2-6. End with
what the evidence changes at home and where a symptom is a safety matter
requiring a pediatrician (the red-flag list: high fever, lethargy, etc. = "not
teething"). The desk does not stand in for individual medical care. Use
furniture where evidence has a shape prose would hide (e.g. a table separating
teething-attributable from not-attributable signs, or the effect sizes);
furniture carries evidence, not decoration.

Recent-pattern habits to break (full list in commission.md):
- Do not open with the trial's bottom line as sentence one; do not use the
  hedged-contrast / "does one thing not the other" dek mold or a comma-triad dek.
- Do not reuse the "where AAP and ESPGHAN part ways" (nb-position) section shape
  or a "back to the [object]" closer.
Required furniture and the Sources section are not habits to avoid.
