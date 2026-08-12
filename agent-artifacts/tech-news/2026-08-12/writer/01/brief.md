# writer brief: tech-news/2026-08-12 (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/commission.md  — the frame, boundaries, and coverage already spent
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/writing-coach/01/voice-guide.md  — how this piece should sound
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/researcher/01/evidence.md  — the complete claim set; treat as evidence, not prose
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/library/tech-news/2026-08-12.html  — the initialized article to edit in place
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/.nb-context/  — effective template contract and runtime assets

Output:
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/tech-news/2026-08-12/library/tech-news/2026-08-12.html --series tech-news --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

nb-meta: set harness to "claude-code-routine" and model to "claude-opus-4-8"; fill
dates; nb stamp writes the counts.

This round's focus, from the evidence record:
- The date-window decision is made: anchor the edition on 12 August 2026 but draw
  the strongest verifiable results from the immediately preceding day or two, the
  way prior quiet-day editions of this brief did. Date every item honestly to when
  its result was published; do not present a 10 or 11 August result as same-day.
- Do not pad to six. The band is 4-6; four strong, honestly dated items beats six
  with filler. Use the researcher's verified set (e.g. the 12 August total-eclipse
  coronal-science campaigns, framed as an observing campaign not a same-day lab
  result; Dyna-1 reading protein motion from missing NMR peaks, Nature 10 Aug;
  phosphine-mediated azine C-H coupling, Nature 11 Aug) and any other item the
  record verifies firsthand.
- Respect the boundaries the record already applied: the Anthropic-watermarking
  story is compliance/public-reaction and belongs to Current Events, so decline
  it here; keep markets/business items out; do not center mixture-of-experts (the
  Paper desk's subject) and drop the mis-dated aggregator items the record lists
  under Discarded.
- Where a claim is a lab self-report, attribute it as such; where a figure carries
  an item, give it with its scope from the owning primary.
