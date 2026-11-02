# editor review-brief: daily-brief/2026-11-02 (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/daily-brief/2026-11-02/editorial-direction.md
- Commission (holds the hard exclusions and recent-brief patterns): .../commission.md
- The exact writer brief: .../writer/01/brief.md
- Evidence: .../researcher/01/evidence.md
- Voice guide (read first): .../writing-coach/01/voice-guide.md
- Draft handoff: .../writer/01/draft-handoff.md
- Article to judge/edit: /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-02/library/daily-brief/2026-11-02.html

Output: editorial-review.md in .../editor/01/

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-02/library/daily-brief/2026-11-02.html --series daily-brief --repo /home/user/the-nightly-build

Decide whether this brief publishes, and edit it until it can.

Correct: six items, each 2-3 sentences, each cited; the word card carries a definition authority and an independent history. Verify every item is a real 1-2 November 2026 development, correctly attributed, with the source landing on the record. Open every citation href. Check the word's origin facts against the authority. ENFORCE the hard exclusions: no DOJ Alaska/California ballot litigation, no Q3 GDP/PCE, no VA loans, no DC arch, no Nordhaus, NO Binance hack anywhere (the feature owns it), and none of the already-covered tech items (Mistral Large 4, robots.txt draft, VOLTA, Cursor extension). Confirm the word is neither eggcorn nor bafflegab and has not run before. If any item violates an exclusion or cannot be confirmed as 1-2 Nov, that is a required change.

Reads well / slop: hold every item to spec/slop.md, hardest on the lead and each item's last sentence. Check the lead headline + dek against spec/headlines.md: finding-stating, no colon-subtitle, no question mark, no negative-parallelism dek mold. Compare against the two prior briefs (10-31 lead "Judge bars DOJ from threatening California election officials..."; 11-01 lead "Justice Department says it now seeks only to segregate Alaska ballots"): do not lead on the same DOJ/election-litigation beat a third day unless a genuinely new dominant development demands it, and vary the word-card phrasing.

Strict mode: the word band 300-700 and the exact six-item count are hard limits; nb check enforces them.

Write editorial-review.md in the skill's shape (Correct / Reads well / The experience / Edits / Decision). After direct cuts, if the proof needs only a restamp I (orchestrator) will run nb stamp and nb check. Report the review path and the decision.
