# writer brief: current-events/2026-08-02 (02) — targeted revision

Inputs:
  ../../editorial-direction.md
  ../../writing-coach/01/voice-guide.md
  ../../researcher/03/evidence.md              CURRENT evidence record (item 5 dead-end documented; 4 items valid)
  ../../editor/01/editorial-review.md          apply its Required-work items exactly
  ../01/draft-handoff.md
  the article: .nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html
Output: agent-artifacts/current-events/2026-08-02/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

The editor already made two direct cuts (removed "which reflects the Supreme Leader's office"
and "that tested the same terms") and re-stamped — do NOT reintroduce them. Apply these
required items:

1. CUT item 5 (the Minnesota prediction-market injunction). Researcher round 3 exhausted every
   route and the order is genuinely unreadable; its holding exists only in secondaries, which
   fails "cite only what you have read" and the per-item primary policy. Four items remain
   (Iran, water-system cyberattacks, Spokane wildfire, visa-bond rule) — that satisfies the
   4-6 band. Remove item 5 cleanly and renumber sources/citations so numbering stays in
   first-citation order with no orphans.
2. Item 1 Saudi sentence: recast to NPR's ACTUAL language — MBS "spoke with" Trump and
   "emphasized ... prioritizing dialogue to de-escalate tensions" — NOT "phoned him urging the
   cancellation." (New prose, sourced to NPR per researcher/03.)
3. Item 2 note (the s4 data-nb-note): the PSA text WAS decodable and supports every claim cited
   to it, so correct/soften the note that says its text "could not be decoded directly." Keep
   the item's data-nb-kind="primary" (the editor accepted it).
4. Leave the Iran mirror-as-primary (s1) and the all-caps "OPENING OF THE HORMUZ" verbatim
   quote AS IS — the editor accepted both.

Then run `nb stamp` and the full proof with links until BLOCK: 0. Confirm nb-meta dek ==
rendered dekline, and (if the lead/headline referenced 5 items or item 5) that display text
still matches the 4-item article. Write writer/02/draft-handoff.md with one line per item
resolved and the final proof result.
