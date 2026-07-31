# Editor brief — investing/return-on-capital (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate on a course LESSON.
Three ordered reads (skeptic, cut, reader). Direct cuts/small fixes in the HTML;
larger writing to the writer; evidence gaps to the researcher. Approve only with
`DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/investing/return-on-capital/`)
- `agent-artifacts/investing/return-on-capital/editorial-direction.md`
- `agent-artifacts/investing/return-on-capital/writer/01/brief.md` (EXACT writer
  brief — check for instruction leakage)
- `agent-artifacts/investing/return-on-capital/writer/01/draft-handoff.md`
- `agent-artifacts/investing/return-on-capital/researcher/01/evidence.md`
- `agent-artifacts/investing/return-on-capital/writing-coach/01/voice-guide.md`
- The article: `library/investing/return-on-capital.html`

## The three reads (lesson)
1. **Skeptic.** Recompute the numbers against the evidence record: Costco
   invested capital ($5,788M debt + $29,164M equity − $14,161M cash = $20,791M),
   NOPAT ($10,383M × (1−0.2513) ≈ $7,773M), ROIC ≈ 37.4%, and the honest
   alternates. Check the AEP contrast (ROIC ~4.9-6.4% across tax conventions vs
   its 9.25-10.9% allowed ROE; the sector WACC flagged as secondary). Is the
   invested-capital convention stated as a convention (not the one true formula)?
   Is WACC/valuation honestly deferred? Audit `data-nb-kind` and that every figure
   is sourced.
2. **Cut.** Remove padding, talking-down, "the takeaway is…" self-grading,
   signposts, manufactured punchlines, scaffold headings. A lesson teaches; every
   paragraph passes the "does the reader already have every piece this uses?" test
   (from this lesson or a Background link).
3. **Reader.** Do the two bookends work read back-to-back as setup and resolution,
   about THIS lesson's particulars, carrying no citations and teaching nothing new?
   Does the Background band link the three prior lessons and does the lesson work
   for a reader who opens none? Is the teaching complete (invested capital → ROIC
   → cost-of-capital test) rather than six things in passing? Retest headline/dek
   vs `spec/headlines.md`. Judge voice.

## After edits
Re-run and confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/investing/return-on-capital/library/investing/return-on-capital.html \
  --series investing --library /home/user/library
```
Must remain BLOCK: 0.

## Output
`agent-artifacts/investing/return-on-capital/editor/01/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/investing/return-on-capital/editor/01/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
