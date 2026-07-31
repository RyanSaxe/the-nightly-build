# Writer brief — current-events/2026-07-31 (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft the brief from the exact brief,
voice guide, and evidence record; carry it through the proof to BLOCK: 0.

## Begin with these exact inputs (under `.nb-work/current-events/2026-07-31/`)
- `agent-artifacts/current-events/2026-07-31/editorial-direction.md`
- `agent-artifacts/current-events/2026-07-31/commission.md`
- `agent-artifacts/current-events/2026-07-31/writing-coach/01/voice-guide.md`
- `agent-artifacts/current-events/2026-07-31/researcher/01/evidence.md`
  (4 verified items, each with primary + independent secondary; honest flags)
- The initialized article: `library/current-events/2026-07-31.html`
- Generated context: `.nb-context/` (brief contract, furniture).

## What to write
`library/current-events/2026-07-31.html`. Template `brief`, **4-6 items** (the
record supports 4 solid ones — write those 4; do not pad to hit a higher count).
Each item = a `nb-brief-item` (topic tag, a headline linking to the primary, and
1-3 sentences carrying the number/caveat the headline dropped). The four items:
1. **Blanche AG nomination revolt** (lead) — Senate Judiciary vote postponed;
   Cornyn/Tillis withhold support over the DOJ/IRS settlement; Trump signals he
   might withdraw the nominee. Note the researcher's honesty flag: the Trump Truth
   Social quote was verified only via convergent secondary (platform 403) — attribute
   it carefully to the reporting, do not present it as directly read primary.
2. **Rushdie federal terrorism conviction** — the exact charge/verdict/court from
   the evidence record.
3. **Q2 2026 GDP report** — the fresh economic-data item (outside the Fed-hold
   AVOID zone; do NOT drift into the rate-decision, which Unbiased owns tonight).
4. **Iran conflict widening** — treat as a development OF prior coverage: say the
   exchange has widened (US-Saudi strikes on Iraqi militias; first strike on
   Egyptian soil) and build on what current-events already reported (7/26-30),
   rather than restating the whole thread. This is the least-certain item on the
   consequence bar (researcher's flag); keep it tight and factual.

Per-item citations: each item carries **1 primary + at least 1 independent
secondary**, cited inline, `data-nb-kind` honest. Wire-service register: add what
the headline dropped; each item stands alone; do not close an item on a line that
hands the point back to the reader.

## Permitted changes / decisions you own
- The night's `title` (lead framed as a headline) and `dek` (the night's
  through-line in one sentence, no hedged-contrast mold). Vary item order/framing;
  do not let every item repeat the actor-verb-object headline shape (coach flag).
- Topic tags: short, honest (e.g. "Justice", "Congress", "Economy",
  "Foreign policy").
- Preserve fixed engine assets/classes/labels/required HTML. No added
  scripts/styles/iframes/forms/handlers/external images.

## Metadata (`nb-meta`)
Real values: `series: "current-events"`, `slug: "2026-07-31"`,
`template: "brief"`, `mode: "rolling"`, `order: null`, `date: "2026-07-31"`,
honest `tags`, measured counts, `dek`, `harness: "claude-code"`,
`model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/current-events/2026-07-31/library/current-events/2026-07-31.html \
  --series current-events --library /home/user/library
```
The per-item primary+secondary requirement is gated; clear every BLOCK.

## Also write
`agent-artifacts/current-events/2026-07-31/writer/01/draft-handoff.md`: the
selection judgment (why these 4), counts, and unresolved WARNs.

## Request, don't guess
Missing/weak evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/current-events/2026-07-31/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work; the evidence record is your source of truth.
Do not tour the repo/archive.
