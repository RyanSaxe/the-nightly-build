# review-brief: current-events/2026-08-05 (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/editorial-direction.md — governing standard, `brief` identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writer/01/brief.md — the exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writing-coach/01/voice-guide.md — voice guide (read FIRST)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/researcher/02/evidence.md — the COMPLETE evidence record (round-02 formalizes the 3 writer-opened sources; supersedes 01 for those)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writer/01/draft-handoff.md — handoff + original-work sentence
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/library/current-events/2026-08-05.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (REQUIRED stage).

Recent-pattern notes:
- Recent current-events briefs are consecutive dailies; check `nb history --structure current-events/2026-08-04` for the recent lead/dek shapes and confirm this brief breaks them. Watch the dek for the banned molds (comma-triad; semicolon reversal; suspended question) and scaffolding subheads.

This round's focus — sourcing precision is the core risk (researcher/02 formalized three writer-opened sources with SCOPE LIMITS you must enforce):
1. **Cyclosporiasis item:** the CDC surveillance page is the SOLE owner of the national figures (10,468 cases / 517 hospitalizations / 47 states / 2 deaths). **NBC News does NOT carry those national figures** — NBC corroborates only the two deaths and the Michigan location (its own numbers are Michigan-only, 11,000+/193, and an earlier "45 states" snapshot). Verify the article cites CDC for the national counts and does NOT lean NBC as their source; NBC is the independent secondary for the deaths + Michigan location only. The Michigan death-location is owned by the Michigan Dept of Health and Human Services (via NBC) — confirm that attribution, not CDC.
2. **Spokane arson item:** the Sheriff's Office primary records an **arrest and jail booking on suspicion of Arson 1st Degree (Aaron F. Farinacci, 37), dated Aug 3** — NOT a prosecutor's filed charge and NOT guilt. Confirm the article reports a booking/arrest on suspicion, not a conviction, and that the $1M bond / Aug 4 court appearance are attributed to NPR/Spokesman-Review (they are NOT in the Sheriff primary). An accusation reported as fact is a serious error.
3. **Trade deficit item:** BEA owns the figures; the "revised" qualifier on the May $77.6B belongs to BEA (Transport Topics/Bloomberg does not carry "revised") — confirm attribution.
- Audit each item's data-nb-kind: exactly 1 primary + ≥1 INDEPENDENT secondary; a different outlet is not automatically independent authorship. Open every citation href as printed — each must land on the source's own page.
- Verify every number/name/title/date in display text against the owning primary (the headline and any stat strip are display text — the costliest surface).
- Confirm only ONE of the Aug-3 Democratic-state-vs-Trump legal actions is filed (the Section 301 suit) so the front page does not read as one story; confirm Iran is absent.
- Second read (cut): enforce prose/punctuation; the leads should fuse finding+stake per the voice guide, not assert a through-line as a graded thesis. Third read: what does the ordered/cross-linked front page give beyond the items (the original-work synthesis), and is it closer to the voice-guide wire exemplars than a summary?
- After any direct cuts run `nb stamp`. Decision: approve or revise, naming each required item's owner (researcher for new evidence; writer for prose/attribution fixes).
