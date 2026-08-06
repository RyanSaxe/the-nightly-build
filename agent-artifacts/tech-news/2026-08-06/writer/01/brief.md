# writer brief: tech-news/2026-08-06 (01)

Inputs:
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/editorial-direction.md
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/commission.md  (selection standard, per-item source floor, sibling-brief lane split)
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writing-coach/01/voice-guide.md
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/researcher/01/evidence.md  (5 date-verified candidates + a documented dating audit; the only claim set)
- .nb-work/tech-news/2026-08-06/library/tech-news/2026-08-06.html  (the initialized brief to edit in place)
- .nb-work/tech-news/2026-08-06/.nb-context/  (effective template contract, furniture catalogs)

Output: .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-06/library/tech-news/2026-08-06.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then links-included until BLOCK: 0)

Commission decisions resolved (the evidence record flagged these — apply exactly):
- LEAD BY SIGNIFICANCE, NOT AN AI QUOTA: the day's firmest genuinely-fresh
  result is science/health (the Nature anellovirus / long-COVID paper, online
  08-05) and hardware (the HBF OCP spec at FMS 2026). Let significance set the
  lead there; do not force an AI model release into the lead. The marquee AI
  items this day are industry/governance/security, not research breakthroughs.
- LANE: the OpenAI evaluation-agents / Black Hat security debrief stays in THIS
  brief (an AI-behavior/evaluation finding for an ML-engineering reader), NOT
  current-events — current-events is not covering it. BUT it re-treads the
  AI-agent-security theme of recent editions (08-01 Claude crypto weakness,
  08-03 misconfigured multi-model test); include it only if it adds something
  genuinely new beyond those, and only with caveats (it is OpenAI's self-report,
  postmortem pending).
- DATELINE HONESTY: most "August 6 Nature" hits are online June-July papers
  anthologized in the print issue — they are NOT 08-06 news and the researcher
  correctly moved them to Discarded. Do not resurrect them. Use only the
  date-verified candidates.
- SELF-REPORTS ARE CLAIMS: mark lab benchmark scores (e.g. K-EXAONE) as
  self-reported claims, not verified results. K-EXAONE is the weakest candidate
  (stale, re-treads open/closed-weights which the 08-05 edition already led);
  prefer stronger items.
- LINK INTEGRITY: every item needs exactly one owning primary plus at least one
  independent account, and every href must resolve for a clicking reader. The
  OpenAI primary page is 403-gated to some fetchers; if its href does not
  resolve to the source's own page, corroborate via an openable primary or drop
  the item. The proof checks links.

Researcher's recommended core (selection is yours within the evidence; do not
add a story the record does not carry): anellovirus/long-COVID (lead-worthy),
HBF OCP memory spec, Hassabis/DeepMind leadership change + Jeff Dean departure,
OpenAI eval-agents security (optional, caveated), K-EXAONE (weakest/optional).
Select 4-6.

Form: itemized brief, 4-6 items (nb-brief-item each). Each item headline is a
full-sentence claim that says why it matters; press significance exactly as far
as primary+independent sourcing licenses (voice guide), understatement carrying
confidence. Use nb-table/nb-stat only where an item's evidence has that shape
(recent editions used a small comparison table). Do not duplicate the
InstructGPT longread's RLHF/alignment territory.

Recent-pattern habits to break (full list in commission.md):
- Do not re-lead a story already covered on 2026-08-01..05; do not default to a
  frontier-lab model release as the lead when the firmest result is science.
- Vary item-headline and dek cadence.
Required furniture (nb-brief-item, Sources) is not a habit to avoid.
