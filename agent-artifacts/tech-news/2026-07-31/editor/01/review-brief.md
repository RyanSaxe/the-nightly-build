# Editor brief — tech-news/2026-07-31 (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate on a daily technology
BRIEF. Three ordered reads (skeptic, cut, reader). Direct cuts/small fixes in the
HTML; larger writing to the writer; evidence gaps to the researcher. Approve only
with `DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/tech-news/2026-07-31/`)
- `agent-artifacts/tech-news/2026-07-31/editorial-direction.md`
- `agent-artifacts/tech-news/2026-07-31/writer/01/brief.md` (EXACT writer brief)
- `agent-artifacts/tech-news/2026-07-31/writer/01/draft-handoff.md`
- `agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md`
- `agent-artifacts/tech-news/2026-07-31/writing-coach/01/voice-guide.md`
- The article: `library/tech-news/2026-07-31.html`

## The three reads (brief)
1. **Skeptic.** For EACH of the 4 items (Ruflo/RufRoot RCE, Gemini Robotics 2,
   EU AI Gigafactory, HRL silicon quantum processor), confirm against the evidence
   record: the development is real and correctly stated; the verified number leads
   the vendor framing; each caveat is carried (multi-finger success-rate range;
   EU funding-commitment gap and non-EU chip suppliers; the "patch doesn't undo
   compromise" distinction and Ruflo's vendor-adjacent scale claims; HRL not sole
   entrant and trailing on qubit scale). Confirm the writer correctly OMITTED the
   unread "100,000 chips per site" figure. Each item = exactly 1 primary + ≥1
   independent secondary with honest `data-nb-kind` (the writer reclassified item
   1 to a single GHSA primary — verify that holds).
2. **Cut.** Remove hype adjectives, "why it matters" scaffolding, closers that
   hand the point back, hedged-contrast deks, manufactured punchlines. Each item
   stands alone and adds what the headline dropped.
3. **Reader.** Item headlines vary in shape; selection is sound (4 consequential,
   nothing padded); no overlap with Paper of the Day's emergence topic or a
   US-policy story. Retest the night's title/dek vs `spec/headlines.md`. Judge voice.

## After edits
Re-run and confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```
Must remain BLOCK: 0.

## Output
`agent-artifacts/tech-news/2026-07-31/editor/01/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/tech-news/2026-07-31/editor/01/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
