# writer brief: current-events/2026-08-06 (01)

Inputs:
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/editorial-direction.md
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/commission.md  (selection standard, per-item source floor, sibling-brief lane split)
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/writing-coach/01/voice-guide.md
- .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/researcher/01/evidence.md  (six sourced candidates; the only claim set)
- .nb-work/current-events/2026-08-06/library/current-events/2026-08-06.html  (the initialized brief to edit in place)
- .nb-work/current-events/2026-08-06/.nb-context/  (effective template contract, furniture catalogs)

Output: .nb-work/current-events/2026-08-06/agent-artifacts/current-events/2026-08-06/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-06/library/current-events/2026-08-06.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then links-included until BLOCK: 0)

Commission decisions resolved (the evidence record flagged these — apply exactly):
- DATELINE: 2026-08-06 is the reporting day and no fresher 08-06 wire had posted
  at research time; the six candidates are dated 2026-08-03..05. That is
  acceptable for this rolling dated brief. Select the 4-6 strongest. Before
  finalizing, verify against the three prior editions (nb history --structure
  current-events/2026-08-03, 08-04, 08-05) that you are not re-covering an item
  already run there; the researcher confirmed none duplicates those editions'
  leads, but check the item lists too.
- LANE: keep the Abbott Texas data-center grid-connection pause here (a
  governor's regulatory action is public-consequence news) and keep the NIOSH
  black-lung finding here (public health). The sibling tech-news brief has been
  told not to cover the Abbott grid action.
- LINK INTEGRITY: the researcher flagged three primary URLs still needing
  confirmation (the NIOSH AJRCCM DOI, the Ogles House impeachment-resolution
  number, the Michigan SOS canvassed totals). The proof checks links: confirm
  each primary href resolves to the source's own page, or cut/replace that item.
  Every item needs exactly one owning primary plus at least one independent
  account.

The researcher's recommended core if cutting to four: Oath Keepers dismissal,
Abbott data-center pause, HHS migrant-children contract, black lung; Michigan
Senate primary and Somalia TPS/impeachment are the swing items. Selection is
yours within the evidence; do not add a story the record does not carry.

Form: itemized brief, 4-6 items (nb-brief-item each). Each item headline is a
full-sentence claim that says why it matters; then explain it, pressing the
consequence exactly as far as the item's primary+independent sources jointly
hold (voice guide). Use nb-stat / nb-table / rs-docket only where an item's
evidence has that shape (e.g. the black-lung prevalence trend).

Recent-pattern habits to break (full list in commission.md):
- Deks: no "from X to Y" span or comma-triad shape (headlines guide bans it);
  the lead dek commits to one stance.
- Vary item-headline cadence; do not stack same-shaped clauses.
Required furniture (nb-brief-item, Sources) is not a habit to avoid.
