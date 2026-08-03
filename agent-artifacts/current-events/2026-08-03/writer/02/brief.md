# writer brief: current-events/2026-08-03 (02)

Inputs:
- editor/01/editorial-review.md — the required change to apply (decision: revise, owner: writer)
- writer/01/draft-handoff.md — your prior handoff
- researcher/01/evidence.md — the claim set (unchanged)
- writing-coach/01/voice-guide.md, editorial-direction.md, commission.md (artifact root)
- The article at `library/current-events/2026-08-03.html` (workspace root) and `.nb-context/`
Output: writer/02/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/current-events/2026-08-03/library/current-events/2026-08-03.html`   (file arg only)
  `./nb check .nb-work/current-events/2026-08-03/library/current-events/2026-08-03.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Run until `BLOCK: 0`.

Apply the editor's required change, nothing more:
- CUT the water/infrastructure item — it fails the "newly-owned development
  dated 2026-08-03" bar (its sources are dated 07-22 to 08-01; nothing moved on
  8/3). Four items remain (wildfire, Capital One suit, Iran/Hormuz talks, and
  the CR), within the 4-6 floor.
- Renumber the remaining sources contiguously in first-citation order (the
  editor notes s6->s4 ... s13->s11) and remove the now-orphaned source entries
  for the cut item. Update the nb-meta `sources` count and let `nb stamp`
  recompute words/reading time.
- Confirm the dek still reads as supported once the water item is gone
  (Capital One and Hormuz remain as the contested counterparts). Adjust the dek
  only if the cut makes it unsupported; keep it a stance in one sentence and
  avoid the banned dek molds.
- Preserve all other settled prose. Re-run the full proof (links on) until
  BLOCK: 0. Write writer/02/draft-handoff.md with one line per change.
