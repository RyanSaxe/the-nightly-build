# review-brief: word-of-the-day/ultracrepidarian (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editorial-direction.md — governing standard, `word` identity, series prompt, declared reader (read the voice guide first, this second as needed)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writing-coach/01/voice-guide.md — voice guide (read FIRST)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/researcher/01/evidence.md — the evidence record
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/01/draft-handoff.md — handoff + original-work sentence + open questions
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (this editor stage is REQUIRED per production policy).

Recent-pattern notes (compare against, break any formula):
- Several recent word-of-the-day entries are eponyms; the coach retired the "here is the person behind the word" opener. Confirm the piece does NOT open on the eponym and that its opener/closer/headings are not a stamped word-desk shape. Check the dek against recent word-of-the-day deks (a quick `nb history --structure word-of-the-day/<a-recent-slug>`), for the banned molds.

This round's focus:
- **Accuracy is the whole risk on this piece.** Verify against the evidence's primaries: (a) the piece says "first recorded/printed use," NOT "Hazlitt coined it" (Charles Lamb attribution is live; Hazlitt's "well called" implies an already-circulating epithet) — a claim that Hazlitt coined it is a required fix; (b) Pliny's Latin is *supra crepidam* (printed correctly), with the later *ultra crepidam* named as the reshaped proverb English took its prefix from — check the Latin glyph-for-glyph against the evidence (NH 35.85); (c) Merriam-Webster is NOT cited (it 404s); the definition rests on a resolving dictionary page; (d) no source whose href 403/404s is printed (Baptist News must be absent; the Salon usage via Dictionary.com is the modern-use ground).
- Open every citation href as printed — each must land on the source's own page and resolve.
- Writer's two open questions to rule on: (1) the card pronunciation respelling is grounded in Dictionary.com but not read glyph-for-glyph — verify it or request it dropped/softened; (2) the 1819 attestation rests on Word Histories (resolves), not OED — the brief permitted a resolving secondary; decide whether the page needs OED named. Neither should block if honestly handled; rule and record.
- Hold the tight 550-800 band: cut anything that does not earn its place; do not add prose (past a clause, route to the writer). After any direct cuts, run `nb stamp` so counts stay honest (the writer runs the full proof).
- Third read: does the piece give the reader the distinction (opining beyond one's competence) that the sources alone would not, and is the prose closer to the voice-guide exemplars than a median summary? Reread the headline as the largest claim.
- Decision: approve or revise, naming each required item's owner (researcher/writer/orchestrator).
