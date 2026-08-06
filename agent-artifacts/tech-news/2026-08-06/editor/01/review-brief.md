# editor review-brief: tech-news/2026-08-06 (01)

Inputs (read in the order your skill names):
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/editorial-direction.md
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writing-coach/01/voice-guide.md
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writer/01/brief.md  (the exact writer brief — instruction-leakage checks)
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/researcher/01/evidence.md
- .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/writer/01/draft-handoff.md  (open on the third read)
- .nb-work/tech-news/2026-08-06/library/tech-news/2026-08-06.html  (the brief; 4 items, has a role-mapping table)
- .nb-work/tech-news/2026-08-06/.nb-context/  (template contract, furniture)

Output: .nb-work/tech-news/2026-08-06/agent-artifacts/tech-news/2026-08-06/editor/01/editorial-review.md

After any direct prose cuts, run `nb stamp`. The writer owns proof and markup; route those back.

Recent-pattern notes (verify, don't reintroduce):
Recent editions all led with a frontier-lab AI model release/capability claim;
this one deliberately leads by significance with a science result — confirm that
holds and reads naturally. Don't re-cover a story from the 08-01..05 editions.
Vary item-headline/dek cadence.

This round's focus:
- SOURCING GATE: each of the 4 items needs EXACTLY one owning primary + at least
  one independent account, correct data-nb-kind. Open every href as printed.
  Note: the OpenAI primary returns 403 to scripted fetchers (bot-fingerprinting,
  not dead) and is corroborated by two openable independents (Axios, SC Media);
  the link-checker treats 403 as non-blocking and a human opens it normally —
  confirm this is acceptable and the two independents are real and openable.
- CLAIMS vs FACTS: every interested-party/benchmark number must carry its
  verification status in the clause (the SK hynix per-watt figure as "it says";
  the OpenAI coordination/swarm detail as OpenAI's self-report, postmortem
  pending, not independently confirmed). Confirm the anellovirus lead states
  correlation-not-causation.
- The role-mapping table (Hassabis/Jeff Dean) must map to the primary memo with
  EXACT titles — check every title/role against the owning source; a wrong title
  in display text is the costliest error.
- Confirm no overlap with the current-events brief (that brief owns the Abbott
  data-center grid pause; this one must not duplicate it) and no duplication of
  the InstructGPT longread's RLHF/alignment territory.
- Item headlines must be claims about the world; press significance only as far
  as primary+independent sourcing licenses (voice guide).
