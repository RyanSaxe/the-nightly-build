# Editor review brief — current-events/2026-07-30 (brief template)

## Inputs (begin here)
- editorial-direction.md (governing stack) — this artifact dir.
- The exact writer brief: writer/01/brief.md (for prompt-leakage detection).
- voice-guide.md — writing-coach/01/.
- evidence.md — researcher/01/.
- draft-handoff.md — writer/01/ (open the original-work sentence only on the
  third read).
- Article: .nb-work/current-events/2026-07-30/library/current-events/2026-07-30.html
- Template context: .nb-work/current-events/2026-07-30/.nb-context/.

## Standards to apply
- Brief geometry: 4-6 items; each item exactly ONE primary + at least ONE
  independent secondary; source numbering in first-citation order; honest
  data-nb-kind. Every cited URL resolves.
- Each item is a judgment about why it matters, not a recap. No self-grading,
  no revelation frames, no line handing the point back to the reader, no colon-
  subtitle headline, no hedged-contrast or comma-triad dek.
- Verify every number and quote against the primary that owns it. Check
  directions (dissents were for a hike; present-situation index fell; CMS
  premium effect is a likelihood, not a set figure; Iran attack July 28
  intercepted, US strikes July 29).
- Confirm the piece gives something beyond the sources (the front-page
  synthesis) and that the voice matches the wire exemplars, not median AI.

## Three ordered reads
Skeptic, then Cut, then Reader. Make cuts and small prose fixes directly. Past a
word or clause, return new writing to the writer; evidence gaps to the
researcher. Record the three required lines and the decision in
editorial-review.md.

## Proof
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/current-events/2026-07-30/library/current-events/2026-07-30.html --series current-events --repo . --library ../library
Only an editor DONE with no required change approves.
