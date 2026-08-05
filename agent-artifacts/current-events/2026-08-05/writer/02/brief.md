# writer brief: current-events/2026-08-05 (02) — revision

Apply the one required item in the editor's review, nothing else. Preserve settled work.

Inputs:
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/editor/01/editorial-review.md — the review to apply (Decision: revise)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/researcher/02/evidence.md — the Spokane primary's exact wording (arrest/booking on suspicion)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/library/current-events/2026-08-05.html — the article to fix
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writer/01/draft-handoff.md — prior handoff

Output: /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writer/02/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/library/current-events/2026-08-05.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Required item (from editor/01), owner: writer — Correct the Spokane arson item's legal status in DISPLAY TEXT:
- The item headline currently says "Spokane charges a man with arson" and the lead says investigators "charged Aaron F. Farinacci, 37, with first-degree arson." The Sheriff's Office PRIMARY records an **arrest and jail booking on SUSPICION** of Arson 1st Degree ("Investigators Arrest Old Trails Fire Arson Suspect"; "booked into the Spokane County Jail for Arson 1st Degree") — investigators ARREST and BOOK, they do not "charge," and the status is suspicion, not a filed prosecutorial charge and not guilt.
- Fix the item headline and the lead to arrest/booking-on-suspicion framing (consistent with the item's own dek which already says "arson arrest"). Imply no conviction. Keep the $1M bond and the Aug-4 court appearance attributed to NPR/Spokesman-Review (s8), not to the Sheriff primary.
- Change ONLY this legal characterization (headline + lead); do not alter the other three items or settled work.

Redo the display-text pass on the corrected Spokane headline/lead (every characterization against the primary), then run `nb stamp` and the exact proof to BLOCK: 0, links included. Add one line to draft-handoff.md recording the fix.
