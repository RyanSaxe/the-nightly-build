# writer brief: current-events/2026-08-08 (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the day, the selection standard, boundaries
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this brief
  ../../researcher/01/evidence.md           the verified slate and the only claim set available
  the initialized article and its .nb-context (brief template contract + furniture catalogs)
Output: agent-artifacts/current-events/2026-08-08/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-08/library/current-events/2026-08-08.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/current-events/2026-08-08/library/current-events/2026-08-08.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus (4-6 items; each item exactly one primary + at least one independent
secondary, per the brief template contract):
- Use the researcher's verified five-item slate. Each item opens on its consequence, not a
  recap. Carry the `data-nb-kind` labels straight from the evidence record (a different
  website is not an independent author).
- Two evidence cautions to obey: (1) the precision-missile-stockpile item is an ATTRIBUTED
  DISPUTE, not established fact — the depletion claim has no public government primary and
  may trace to overlapping leaks; write it as report-vs-denial with both sides attributed,
  and do not state depletion as fact. (2) The birthright-citizenship executive order was
  signed Aug 6 per the White House primary (some outlets say Aug 7) — use the primary's
  date.
- The Right to Worship Act item is reported NEUTRALLY here; today's opinion desk argues it.
  Do not editorialize or preview that argument.
- Headline names the day's single most consequential development as a claim, not a date
  label. Avoid the comma-triad dek mold; vary item lead shapes.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8".
