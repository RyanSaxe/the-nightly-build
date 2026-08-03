# editor review-brief: current-events/2026-08-03 (editor/02)

Inputs:
- editor/01/editorial-review.md — your prior review (the required change was: cut the water item)
- writer/02/draft-handoff.md — the writer's record of the applied change
- editorial-direction.md, commission.md, writing-coach/01/voice-guide.md, researcher/01/evidence.md (as needed)
- The revised article at `library/current-events/2026-08-03.html` (workspace root) and `.nb-context/`
Output: editor/02/editorial-review.md

Round focus (confirmation round — the prior read already vetted the four
survivors' sourcing, hrefs, facts, and furniture):
- Confirm the water/infrastructure item is fully removed and its source entries
  are gone, with citations renumbered contiguously (no dangling #s refs, no
  gaps) and nb-meta `sources` = 11 matching the list.
- Confirm the dek still reads as supported by the four remaining items
  (Wildfire, Capital One, Hormuz, CR) and matches the rendered dekline.
- Confirm nothing else regressed: per-item sourcing intact, no new tell
  introduced by the cut. Do a light third read as the paper's reader.
- If clean, APPROVE. Make only surgical fixes if truly needed; after any direct
  cut run `./nb stamp <article-path>` (file arg). Report path and decision.
