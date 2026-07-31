# Writer brief — tech-news/2026-07-31 (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft the brief from the exact brief,
voice guide, and evidence record; carry it through the proof to BLOCK: 0.

## Begin with these exact inputs (under `.nb-work/tech-news/2026-07-31/`)
- `agent-artifacts/tech-news/2026-07-31/editorial-direction.md`
- `agent-artifacts/tech-news/2026-07-31/commission.md`
- `agent-artifacts/tech-news/2026-07-31/writing-coach/01/voice-guide.md`
- `agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md`
  (4 verified items, each primary + independent secondary; honest drops)
- The initialized article: `library/tech-news/2026-07-31.html`
- Generated context: `.nb-context/` (brief contract, furniture).

## What to write
`library/tech-news/2026-07-31.html`. Template `brief`, **4-6 items** (the record
supports 4 solid ones — write those 4; do not pad). The four items:
1. **Google DeepMind "Gemini Robotics 2"** — from DeepMind's own blog (primary) +
   independent secondary. State the actual capability (the three-model suite) and
   the one technical caveat; separate verified result from vendor framing.
2. **EU AI "Gigafactory" call** — European Commission release (primary) +
   secondary. The real figures (public/total funding, sites, chip counts).
3. **Ruflo/RufRoot RCE flaw** — Noma Security disclosure + the GitHub Security
   Advisory (primary) + independent secondary. State the flaw precisely and its
   scope.
4. **HRL Laboratories' silicon quantum processor** — the arXiv preprint of the
   Nature paper (primary) + secondary. The result and what it measures.

Each item = a `nb-brief-item` (topic tag, headline linking to the primary, 1-3
sentences carrying the technical number/caveat the headline dropped). Per-item:
**1 primary + at least 1 independent secondary**, cited inline, `data-nb-kind`
honest. Where a claim is a capability/benchmark, prefer the independent number
and note any vendor-vs-independent gap. AI-central but significance decides the
mix; no hype adjectives; each item stands alone; no closer that hands the point
back.

## Permitted changes / decisions you own
- The night's `title` (lead framed as a headline) and `dek` (through-line, no
  hedged-contrast mold). Vary item order/framing. Topic tags short and honest
  (e.g. "AI", "robotics", "compute", "security", "quantum").
- Preserve fixed engine assets/classes/labels/required HTML. No added
  scripts/styles/iframes/forms/handlers/external images.

## Metadata (`nb-meta`)
Real values: `series: "tech-news"`, `slug: "2026-07-31"`, `template: "brief"`,
`mode: "rolling"`, `order: null`, `date: "2026-07-31"`, honest `tags`, measured
counts, `dek`, `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```

## Also write
`agent-artifacts/tech-news/2026-07-31/writer/01/draft-handoff.md`: the selection
judgment (why these 4), counts, unresolved WARNs.

## Request, don't guess
Missing/weak evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/tech-news/2026-07-31/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work; the evidence record is your source of truth.
Do not tour the repo/archive.
