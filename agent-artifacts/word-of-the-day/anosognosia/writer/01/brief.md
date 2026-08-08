# writer brief: word-of-the-day/anosognosia (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the word, the angle, boundaries, recent shapes to break
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this piece
  ../../researcher/01/evidence.md           the complete evidence record; the only claim set available
  the initialized article and its .nb-context (word template contract + furniture catalogs)
Output: agent-artifacts/word-of-the-day/anosognosia/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/word-of-the-day/anosognosia/library/word-of-the-day/anosognosia.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/word-of-the-day/anosognosia/library/word-of-the-day/anosognosia.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus (550-800 words; the paper's smallest read):
- Handle the evidence record's flagged precision limits exactly: write "June 1914" (not
  "11 June 1914" — the exact day rests only on a gated secondary); do not print the OED
  "1915 Medical Record" first-English-attestation as hard fact unless its URL resolves —
  the OED entry is login-gated, so either omit the precise attestation or attribute it
  carefully to a resolving source; and for prevalence use StatPearls' 50-90% range, not
  the unverified Amador "57% of 412" figure.
- Land the one bright, sourced distinction the coach names: anosognosia (organic
  unawareness of a deficit) vs. denial vs. Dunning-Kruger (metacognitive miscalibration
  in the healthy) — one sentence, cited, never a detour into Dunning-Kruger.
- The definition card carries the rs-word-card first with no heading; the flexible
  sections tell the origin (Babinski, June 1914, Société de Neurologie de Paris) and the
  widening into the modern psychiatric sense, landing on why the word still earns space.
- Break the recent word-desk headline mold (single restated etymology fact; "coined it in
  YEAR for…"). Commit to a claim about the sense the word preserves.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8".
