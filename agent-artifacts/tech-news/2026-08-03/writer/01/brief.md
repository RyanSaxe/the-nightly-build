# writer brief: tech-news/2026-08-03 (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `brief` template identity, series prompt
- commission.md (artifact root) — what the brief is, per-item sourcing, coordination, shapes to break
- writing-coach/01/voice-guide.md — compression standard, licenses (consequence line, buried figure, through-line dek), do-not-reuse list
- researcher/01/evidence.md — the ONLY claim set available; use its per-item primary+secondary, Numbers, and Contradictions exactly
- The initialized article at `library/tech-news/2026-08-03.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/tech-news/2026-08-03/library/tech-news/2026-08-03.html --series tech-news`
  `./nb check .nb-work/tech-news/2026-08-03/library/tech-news/2026-08-03.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- Build the 4 researched items (each with exactly one primary in the headline
  link + at least one independent secondary): (1) Anthropic's three real-world
  cyber-eval incidents; (2) DeepSeek-V4-Flash-0731; (3) Thinking Machines
  Inkling-Small; (4) statin muscle pain via the NLRP3 inflammasome. These are
  confirmed non-overlapping with tonight's Current Events brief. Do not add the
  Google Earth item (it was not researched; no primary read).
- Accuracy cautions from the evidence, do not miss them:
  - Anthropic: frame as a MISCONFIGURATION that wrongly connected eval machines
    to the internet, not a containment "escape"; the behavioral divergence
    across models is the real story.
  - DeepSeek: the card says ~304B params and omits active/context/pricing; the
    284B total / 13B active / 1M context and pricing come from secondaries —
    attribute them as such and note the 304-vs-284 gap. Use "frontier-adjacent
    at a fraction of the cost," not "Opus-level."
  - Inkling-Small: it beats its teacher on five of six benchmarks but NOT on
    AIME 2026 (95.5% vs 97.1%) — state the exception.
- Each item's prose leads on the technical consequence, not the recap; commit,
  don't hedge into "could transform." No "Why it matters:" label furniture.
- Dek is the night's through-line in one sentence, a stance; avoid the banned
  dek molds and the paired-adjective-triad headline.
- Brief template: 4-6 `nb-brief-item` blocks + Sources. Shortread. min 5 sources
  overall (the per-item primary+secondary rule is the real constraint).
