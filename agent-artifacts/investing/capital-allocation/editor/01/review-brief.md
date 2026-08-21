# Editor review brief: investing/capital-allocation (01)

Inputs:
- `../../editorial-direction.md` — the governing standard, including the lesson
  template identity (opens on "Why this matters", closes on "The takeaway"; the
  two bookend cards may address the reader — the one allowed self-reference —
  while the body may not).
- `../../commission.md` — the assignment (teach capital allocation as the next
  cumulative lesson), the instruction to rely on already-taught concepts rather
  than reteach them, boundaries, and the recent patterns to break.
- `../../writer/01/brief.md` and `../../writer/01/draft-handoff.md`.
- `../../researcher/01/evidence.md` — the sourced record; the Berkshire figures
  rest on its 10-Q and letters.
- The article: `.nb-work/investing/capital-allocation/library/investing/capital-allocation.html`.

Proof: `./nb check .nb-work/investing/capital-allocation/library/investing/capital-allocation.html --series investing --library /home/user/library-checkout`

## Recent patterns to catch (a formula shows only across issues)
Compare against recent investing lessons (`NB_LIBRARY=/home/user/library-checkout ./nb history --series investing`):
- Dek: reject the numeric-contrast-"at once" mold.
- "Why this matters": reject a sweeping generalization opener.
- Reject a separate "Verdict" section stacked on "The takeaway"; the takeaway is
  the close. Reject an imperative-aphorism final sentence.
- The body must not reteach return-on-capital / cost-of-capital / value-of-growth
  from scratch; it should lean on them.

## Round focus
Fresh-eyes read at high effort. This is a teaching piece: verify each section
builds on the last and the reader finishes able to judge whether a company's
capital-allocation choices add or destroy value. Check the buyback identity is
derived correctly and its terms defined where first used, and that the Berkshire
figures match the cited filings. Confirm the transferable lesson is not buried
under one company's history. Cut slop, hold headline/dek/headings to
spec/headlines.md. Fix prose, structure, and the equation/table furniture in
place; route to the writer only for something needing new evidence or a
corrected derivation.
