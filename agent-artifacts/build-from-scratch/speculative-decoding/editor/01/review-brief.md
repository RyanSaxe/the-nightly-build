# Editor review-brief — build-from-scratch/speculative-decoding (01)

## Your job
Give this drafted article three ordered reads and settle it. You are the fresh-
eyes gate at **high effort**. Make cuts and small prose fixes directly; anything
past a word or clause returns to the writer, evidence returns to the researcher.
Only your `DONE` with no required change approves the piece.

## Exact inputs (start here)
- `agent-artifacts/build-from-scratch/speculative-decoding/editorial-direction.md`
- `agent-artifacts/build-from-scratch/speculative-decoding/commission.md`
- The **exact writer brief**: `agent-artifacts/build-from-scratch/speculative-decoding/writer/01/brief.md`
  (read it so copied instructions / prompt leakage into the prose are detectable)
- The draft: `library/build-from-scratch/speculative-decoding.html`
- Evidence: `agent-artifacts/build-from-scratch/speculative-decoding/researcher/01/evidence.md`
- Voice guide: `agent-artifacts/build-from-scratch/speculative-decoding/writing-coach/01/voice-guide.md`
- The writer's `writer/01/draft-handoff.md`

## The three reads (PROTOCOL)
1. **Skeptic.** State and try to break the thesis and the claims it depends on.
   Reopen the cited sources, recompute every figure, and audit each
   `data-nb-kind` (primary/secondary) against the actual source. A number that
   does not check, a claim not supported by its cite, or a misclassified source
   is a required change.
2. **Cut.** Remove sentences doing no fact/claim/reasoning work: self-grading,
   stock revelations, signposts, instruction leakage, manufactured punchlines,
   hedged contrast, self-reference, em-dash reflex, scaffolding headings, and
   any structure repeated out of habit not required by this template.
3. **Reader.** Identify what the article gives beyond its sources; compare it to
   the writer's original-work claim in draft-handoff.md; judge the voice against
   the guide; retest the headline and dek against `spec/headlines.md`.

## What you fix vs. return
- Fix directly: cuts, word/phrase-level prose, punctuation, a mislabeled kind you
  can correct from the evidence, headline/dek tightening.
- Return to **writer** (new numbered brief needed): new writing past a clause,
  structural changes, markup/furniture/asset/proof problems.
- Return to **researcher**: a claim whose evidence is missing, wrong, or
  unverifiable.
- Verify the accept/reject rule in the code and equation matches the papers exactly (min(1,p/q) + normalized residual). Re-run or inspect the committed script's output; confirm the empirical distribution-match is real and the reported speedup/acceptance numbers come from the run or a primary, not invented. Confirm no active content in the HTML.
## Prove it after your edits
Re-run: `/home/user/the-nightly-build/nb check library/build-from-scratch/speculative-decoding.html --series build-from-scratch --repo /home/user/the-nightly-build` and confirm **BLOCK: 0** still holds.

## Output
Write `agent-artifacts/build-from-scratch/speculative-decoding/editor/01/editorial-review.md`: the record
of the three reads, every direct edit you made, every source you re-checked and
its result, and your decision.

## Report
- If no required change remains: `DONE editor library/build-from-scratch/speculative-decoding.html`
- If a redraft is required: `REQUEST writer <one-sentence need>` or
  `REQUEST researcher <one-sentence need>` (be specific; the correspondent routes it).
