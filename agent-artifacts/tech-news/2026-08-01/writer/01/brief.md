# Writer brief — tech-news/2026-08-01 (01)

## Your job
Write the technology brief from the commission, voice guide, and evidence record,
then prove it to BLOCK: 0. The researcher selected/verified the items; write
them, dropping the weakest if more than 6 were supplied.

## Exact inputs (start here)
- `agent-artifacts/tech-news/2026-08-01/commission.md`
- `agent-artifacts/tech-news/2026-08-01/editorial-direction.md`
- `agent-artifacts/tech-news/2026-08-01/writing-coach/01/voice-guide.md`
- `agent-artifacts/tech-news/2026-08-01/researcher/01/evidence.md`
- Initialized article: `library/tech-news/2026-08-01.html`
- `.nb-context/` (template contract, runtime assets, furniture)

## Write
1. `library/tech-news/2026-08-01.html`:
   - `brief` geometry: **4–6** `nb-brief-item`s + `Sources`. Each item: topic tag,
     a headline naming the real development (fresh verb, no colon subtitle, no
     "faster/cheaper/smarter" triad) linking to its **primary** source, a cite,
     and 1–3 sentences adding the number/benchmark caveat/architectural detail —
     a judgment, not a spec-sheet recap. Each item stands alone.
   - Per-item sources: exactly **1 primary (vendor card/announcement/paper) + ≥1
     independent secondary** (from the evidence record). Number sources in
     first-citation order; honest `data-nb-kind`. Only verified items; URLs resolve.
   - Mix beyond a models-only monoculture where the evidence supports it (systems/
     hardware + at least one science/health result).
   - `nb-meta` ACTUAL values: title, dek (the night's real through-line or plain),
     date `2026-08-01`, mode `rolling`, order null, tags, measured
     sources/words/reading_minutes, harness `claude-code`, model `claude-sonnet-5`.
2. `writer/01/draft-handoff.md`: the judgment each item carries, warnings
   resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/tech-news/2026-08-01.html --series tech-news --repo /home/user/the-nightly-build` → **BLOCK: 0**.

## Rules
- Documented furniture only; no active content; preserve fixed engine
  assets/classes/labels. Begin with named inputs; `REQUEST researcher` for a
  missing/weak item rather than invent. No repo/archive tour.

## Report
End with: `DONE writer library/tech-news/2026-08-01.html`
