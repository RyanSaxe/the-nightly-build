# writer brief: tech-news/2026-08-09 (02)

Inputs:
- ../01/draft-handoff.md and the article as you left it (edit in place)
- ../../editor/01/editorial-review.md — the required items
- ../../researcher/01/evidence.md — the verified record

Output: draft-handoff.md (this directory, writer/02)

The orchestrator has made the selection decision the editor routed. Apply exactly this:

1. Drop the Qwen3.8-Max item entirely. The daily paper already led on it on 08-05
   with the full specs; its only new element is thin and its timing hook ("that
   week has arrived and the weights have not") is false as of this Sunday edition
   (the promised window opens Monday, 10 August). Remove the item and its
   now-unused sources.
2. Keep the Astra item, but reframe it as an explicit build-on of the paper's
   08-04 coverage. Lead the item with the genuinely new development, not the
   original announcement: the first outside read of the proofs (Thomas Bloom's
   independent verification) and the sharper refereeing status (still not
   peer-reviewed). One clause should make clear this continues the earlier
   coverage rather than re-reporting it from scratch. Do not restate the full
   original specs as if new; assume the reader has the prior edition.
3. Leave the graphene lead, the GPT-4 social-science-forecasting item, and the
   Langflow RCE item as they stand (the editor already approved them and cut one
   signpost). The edition lands at four items, within the 4-6 band and above the
   5-source floor.

Then run the display-text pass on what you changed (the item count and the
Astra reframe touch the dek/headline if they referenced Qwen), `nb stamp`, and
the exact proof with links until BLOCK: 0:

./nb check .nb-work/tech-news/2026-08-09/library/tech-news/2026-08-09.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

Write one line per editor/orchestrator item resolved in draft-handoff.md.
