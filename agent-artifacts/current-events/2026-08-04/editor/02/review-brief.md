# review-brief: current-events/2026-08-04 (editor/02) — confirm the two required repairs + re-homed facts

Inputs:
- ../../editorial-direction.md — governing standard, brief identity
- ../01/editorial-review.md — your prior review (the two required re-sourcing items)
- ../../researcher/02/evidence.md — the resolving primaries (SCOTUS 26A124 stay application; DOJ rescission order) with exact strings/locators
- ../../writer/02/draft-handoff.md — what the writer changed, including a forced structural change (see below)
- ../../writer/01/brief.md — writer brief (leakage checks)
- article: .nb-work/current-events/2026-08-04/library/current-events/2026-08-04.html
Output: .nb-work/current-events/2026-08-04/agent-artifacts/current-events/2026-08-04/editor/02/editorial-review.md

Context on the forced change: the per-item contract is primary:[1,1] (exactly one primary per item), so the writer could NOT add a second primary. It kept each flagged quote on its owning primary as the item's single primary and re-homed the displaced facts to secondaries. Confirm this is done honestly.

Verify these deltas and that nothing regressed:
1. Item 1 (SCOTUS EO): the Sauer quote now cites the government's Application for a Stay in docket 26A124 (data-nb-kind=primary, locator "printed page 5"), wording corrected to "preempts the Executive's DELIBERATIVE policymaking." Open the href; confirm the exact string resolves there.
   - Re-homed facts — OPEN each new secondary and confirm it actually carries the claim on its LIVE page (this is the same live-drift failure you caught in round 01): the Jackson response-call + the Aug. 3 California filing now cite Votebeat (s3); the party count / "twelve states led by Alabama" now cites SCOTUSblog (s2). If either secondary does not carry its claim, that is a required item.
   - Confirm the editor/01 semicolon you flagged is now split into two clean sentences.
2. Item 2 (Blanche/fund): the rescission quote + "May 18, 2026" date now cite the DOJ signed order (data-nb-kind=primary, locator "Paragraph A"); open it and confirm the exact string. Confirm the May 18 fund-establishing order is kept distinct from the separate May 19 mutual-release order. The committee-vote fact now cites the Washington Post (s6) — open it and confirm it carries that fact; NPR (s5) kept as independent secondary for the framing it still supports.
3. Each item still has exactly one primary + at least one independent secondary; data-nb-kind labels honest; source numbering unchanged; items 3-5 untouched. Open every changed href (must resolve to the source's own page).
If all hold, approve. Otherwise name the precise fix and owner (researcher if a claim needs a source that carries it; writer to repoint).

End with Decision: approve | revise.
