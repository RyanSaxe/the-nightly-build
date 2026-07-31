# Editor brief — current-events/2026-07-31 (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate on a daily news BRIEF.
Three ordered reads (skeptic, cut, reader). Direct cuts/small fixes in the HTML;
larger writing returns to the writer; evidence gaps to the researcher. Approve
only with `DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/current-events/2026-07-31/`)
- `agent-artifacts/current-events/2026-07-31/editorial-direction.md`
- `agent-artifacts/current-events/2026-07-31/writer/01/brief.md` (EXACT writer
  brief — check for instruction leakage)
- `agent-artifacts/current-events/2026-07-31/writer/01/draft-handoff.md`
- `agent-artifacts/current-events/2026-07-31/researcher/01/evidence.md`
- `agent-artifacts/current-events/2026-07-31/writing-coach/01/voice-guide.md`
- The article: `library/current-events/2026-07-31.html`

## The three reads (brief)
1. **Skeptic.** For EACH of the 4 items, confirm against the evidence record: the
   development is real and correctly stated; the number/caveat is accurate ($1.776B
   settlement figure; the Q2 GDP 3.9%/1.7% real-final-sales divergence; the Iran
   item's casualty claim marked unconfirmed); the Trump Truth Social quote is
   attributed to NPR's reporting, not presented as directly-read primary. Confirm
   **each item carries 1 primary + at least 1 independent secondary** with honest
   `data-nb-kind`, and that the Fed rate decision is NOT re-reported here (Unbiased
   owns it). Every source URL should resolve (the proof checks links).
2. **Cut.** Remove any sentence that recaps rather than adds, hands the point back
   to the reader, or reads as feed voice / "why it matters" scaffolding. Each item
   stands alone; the prose adds what the headline dropped.
3. **Reader.** Do the item headlines vary in shape (not all actor-verb-object)?
   Is the selection judgment sound (4 consequential items, nothing padded)? Retest
   the night's title and dek vs `spec/headlines.md` (commit, no hedged-contrast
   mold). Judge voice vs the guide.

## After edits
Re-run and confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/current-events/2026-07-31/library/current-events/2026-07-31.html \
  --series current-events --library /home/user/library
```
Must remain BLOCK: 0.

## Output
`agent-artifacts/current-events/2026-07-31/editor/01/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/current-events/2026-07-31/editor/01/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
