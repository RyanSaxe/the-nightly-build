# Writer brief — current-events/2026-08-01 (01)

## Your job
Write the news brief from the commission, voice guide, and evidence record, then
prove it to BLOCK: 0. The researcher already selected/verified the items; write
them, dropping the weakest if more than 6 were supplied.

## Exact inputs (start here)
- `agent-artifacts/current-events/2026-08-01/commission.md`
- `agent-artifacts/current-events/2026-08-01/editorial-direction.md`
- `agent-artifacts/current-events/2026-08-01/writing-coach/01/voice-guide.md`
- `agent-artifacts/current-events/2026-08-01/researcher/01/evidence.md`
- Initialized article: `library/current-events/2026-08-01.html`
- `.nb-context/` (template contract, runtime assets, furniture)

## Write
1. `library/current-events/2026-08-01.html`:
   - `brief` geometry: **4–6** `nb-brief-item`s in the `items` section + `Sources`.
     Each item: a topic tag, a headline that names the development (fresh verb,
     surprise first, no colon subtitle) linking to its **primary** source, a cite,
     and 1–3 sentences carrying the number/caveat the headline dropped. Each item
     cited; each stands alone.
   - Per-item sources: exactly **1 primary + ≥1 independent secondary** (from the
     evidence record). Number sources in first-citation order; honest
     `data-nb-kind`. Only items the evidence verified; every URL resolves.
   - Do NOT center the mail-in voting executive order (Opinion owns it tonight).
   - `nb-meta` ACTUAL values: title, dek (the night's real center of gravity or
     plain — no forced theme, no hedged-contrast mold), date `2026-08-01`, mode
     `rolling`, order null, tags, measured sources/words/reading_minutes, harness
     `claude-code`, model `claude-sonnet-5`.
2. `writer/01/draft-handoff.md`: what judgment each item carries beyond the
   headline (the original editorial work), warnings resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/current-events/2026-08-01.html --series current-events --repo /home/user/the-nightly-build` → **BLOCK: 0**.

## Rules
- Documented furniture only; no active content; preserve fixed engine
  assets/classes/labels. Begin with named inputs; `REQUEST researcher` for a
  missing/weak item rather than invent one. No repo/archive tour.

## Report
End with: `DONE writer library/current-events/2026-08-01.html`
