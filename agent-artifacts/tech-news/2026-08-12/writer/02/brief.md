# writer brief: tech-news/2026-08-12 (02)

Inputs:
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/commission.md
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/researcher/03/evidence.md  — the current, complete claim set; supersedes 01/02
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/writer/01/draft-handoff.md  — your prior round's notes
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/library/tech-news/2026-08-12.html  — your prior draft, edit it in place
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/.nb-context/  — effective template contract

Output:
  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-12/agent-artifacts/tech-news/2026-08-12/writer/02/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/tech-news/2026-08-12/library/tech-news/2026-08-12.html --series tech-news --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

This round resolves the round-01 block. The evidence now supports a three-item
edition, each item carrying one primary AND one independent secondary. Do this:
- Run exactly these three items, from researcher/03/evidence.md, each honestly
  dated:
  1. The 12 August total solar eclipse and the coordinated NASA/ESA coronal-science
     campaign (NASA primary + AFP/phys.org secondary). It genuinely lands on the
     12th but is an observing campaign, not a same-day result; say so.
  2. Dyna-1 reading protein motion from missing NMR peaks (Nature, 10 Aug; primary
     + CBIRT and Kiin Bio secondaries). Note honestly that the independent write-ups
     are preprint-era (the result circulated from March 2025).
  3. Anthropic marks Claude's text output (~11 Aug; Anthropic support-page primary +
     TechCrunch secondary). Frame it as the technical AI development, and state
     plainly what Anthropic disclosed (a mark that survives copy-paste and some
     editing; C2PA signed metadata for images; models launched on/after 2 Aug mark
     at launch; a detected mark is non-conclusive) and what it did not (how the
     text mark is constructed; how much editing removes it). Do not overclaim.
- Drop the azine C-H coupling item entirely: no independent secondary exists, so it
  cannot meet the per-item rule. Remove it from the article and the Sources list.
- The 3-item count is below the 4-item band floor. That is expected and acceptable:
  it yields a W-LENGTH-LOW warning, not a block. Leave that warning standing rather
  than padding with a misdated, product, markets, or aggregator item. Record it as
  intentionally left in the handoff.
- The lead item and dek must name the day's real through-line honestly: a quiet
  window for model releases, with the movement in the lab and the sky. Attribute
  every lab claim as a self-report where it is one; give figures with scope.
- nb-meta: harness "claude-code-routine", model "claude-opus-4-8"; dek identical to
  the rendered dekline. Run nb stamp, then the full proof until BLOCK: 0 (WARN may
  remain 1 for length).
