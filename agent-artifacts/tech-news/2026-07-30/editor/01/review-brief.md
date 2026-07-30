# Editor review brief — tech-news/2026-07-30 (invocation 01)

## Task
Give the drafted brief three ordered reads (skeptic, cut, reader). Make surgical
cuts and small fixes directly; return prose past a word/clause to the writer and
evidence gaps to the researcher. Approve only on DONE with no required change.

## Inputs
- editorial-direction.md; commission.md
- writer/01/brief.md (the exact writer brief — check for prompt leakage)
- writing-coach/01/voice-guide.md
- researcher/01/evidence.md
- writer/01/draft-handoff.md (open the original-work sentence only on the third read)
- Article: .nb-work/tech-news/2026-07-30/library/tech-news/2026-07-30.html

## Points to test hardest
- Item 1 numbers and scope: 2^64→2^38, 60 hours, ~$100k, 200–800×, 7-of-10
  rounds, >400 octillion messages, and the "no production software has to change"
  caveat. The AES result must not read as a break of full AES.
- data-nb-kind on all ten sources; each item exactly one primary + one independent
  secondary; numbering in first-citation order.
- Items 4–5 primaries return 403 (gated): confirm the claim is carried honestly
  from the verified secondaries and nothing is invented (esp. no named
  semiconductor material for item 4).
- Selection against neighbors: no current-events/economic story, no Nvidia lead,
  no paper-explainer shape.
- Headlines/dek against the floor: no colon subtitle, no triad, no self-grading.

## Proof of record
Writer reports `./nb check … --series tech-news --repo . --library ../library` →
BLOCK: 0, WARN: 0. Re-run if any edit changes prose or counts.
