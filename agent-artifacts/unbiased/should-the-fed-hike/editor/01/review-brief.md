# Editor brief — unbiased/should-the-fed-hike (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate on a STRICT two-position
piece. Three ordered reads (skeptic, cut, reader). Direct cuts/small fixes in the
HTML; larger writing to the writer; evidence gaps to the researcher. Approve only
with `DONE` and no required change. Fairness is the load-bearing standard here.

## Begin with these exact inputs (under `.nb-work/unbiased/should-the-fed-hike/`)
- `agent-artifacts/unbiased/should-the-fed-hike/editorial-direction.md`
- `agent-artifacts/unbiased/should-the-fed-hike/writer/01/brief.md` (EXACT writer
  brief — note it corrects Powell→Warsh; check for instruction leakage)
- `agent-artifacts/unbiased/should-the-fed-hike/writer/01/draft-handoff.md`
- `agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md` (14
  read sources; the Warsh-not-Powell correction; Logan/raise, Warsh+Zandi/Yellen/hold)
- `agent-artifacts/unbiased/should-the-fed-hike/writing-coach/01/voice-guide.md`
- The article: `library/unbiased/should-the-fed-hike.html`

## The three reads (unbiased, strict)
1. **Skeptic.** Verify the event facts against the evidence record: the July 29
   2026 hold, target range, 9-3 vote, dissenters Hammack/Kashkari/Logan favoring a
   hike, **Kevin Warsh as Chair (not Powell)**, inflation-above-target and the
   tariff-vs-energy attribution. Each position must be represented by a direct,
   cited statement from a named holder who actually holds it (Logan for "raise";
   Warsh and/or Zandi/Yellen for "hold" — confirm the sharper supply-shock argument
   is NOT misattributed to Warsh). Both cases held to the SAME scrutiny; no support
   the record does not hold; each steelmanned. Audit `data-nb-kind`; confirm strict
   floors (≥10 sources, ≥4 primary, ≥3 secondary).
2. **Cut.** Remove any smuggled conclusion or tell that tips the house's hand,
   false-symmetry filler, component-vocabulary headings, hedged-contrast dek,
   manufactured punchlines, signposts. The paper takes no side and adds no house
   conclusion.
3. **Reader.** Are the two sides genuinely the strongest cases, distinct in
   reasoning (not mirrored outlines)? Does orientation arm without pre-judging?
   Retest the neutral-question title and the no-side dek vs `spec/headlines.md`.
   Judge voice.

## After edits
Re-run the strict proof and confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```
Must remain BLOCK: 0.

## Output
`agent-artifacts/unbiased/should-the-fed-hike/editor/01/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/unbiased/should-the-fed-hike/editor/01/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
