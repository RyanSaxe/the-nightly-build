# Writer brief — company-analysis/apple (01)

## Your job
Draft the chart-forward analysis from the commission, voice guide, and evidence
record, then prove it to BLOCK: 0.

## Exact inputs (start here)
- `agent-artifacts/company-analysis/apple/commission.md`
- `agent-artifacts/company-analysis/apple/editorial-direction.md`
- `agent-artifacts/company-analysis/apple/writing-coach/01/voice-guide.md`
- `agent-artifacts/company-analysis/apple/researcher/01/evidence.md`
- Initialized article: `library/company-analysis/apple.html`
- `.nb-context/` (template contract, runtime assets, furniture)

## Write
1. `library/company-analysis/apple.html`:
   - `article` geometry: `orientation` + 2–6 flex sections you name + `Sources`.
     Words **1500–4000** (measured). Every section cited.
   - Answer the market question (services compounder vs hardware-cycle company).
     Teach the segments and margin mechanics where they clarify the argument, not
     in a stock overview. Separate the one-time (iPhone upgrade cycle, tariff
     refund) from the recurring (Services), and read what the Services deceleration
     + miss mean for the compounder thesis. **No buy/sell/allocation call.** Keep
     reported fact / estimate / synthesis distinct.
   - **Charts**: build with `nb chart` from the evidence record's verified numbers,
     committing the `chart-N.py` provenance beside the article (see docs/charts.md
     and `/home/user/the-nightly-build/nb chart --help`). Good candidates: Services
     YoY growth decelerating; revenue mix by segment; the quarter's margin bridge.
     Honest axes; caption cites the data source. Do not fabricate points. A stat
     strip may carry the headline numbers.
   - `nb-meta` ACTUAL values: title, dek, date `2026-08-01`, mode `open`, order
     null, tags e.g. `["equity"]`, measured sources/words/reading_minutes, harness
     `claude-code`, model `claude-sonnet-5`.
   - Number sources first-citation order; honest `data-nb-kind` (Apple filings =
     primary; analyst-estimate reporting = secondary). Only verified sources; URLs
     resolve.
2. `writer/01/draft-handoff.md`: the visible original work (the one-time-vs-
   recurring decomposition and what it says about the thesis), any chart
   provenance notes, warnings resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/company-analysis/apple.html --series company-analysis --repo /home/user/the-nightly-build` → **BLOCK: 0**.
Preview to inspect charts render correctly.

## Rules
- Documented furniture only; no active content; preserve fixed engine
  assets/classes/labels. Charts are PNGs from committed scripts, never inline
  script blocks or hand-drawn images. Begin with named inputs; `REQUEST
  researcher` for a missing number rather than estimate it. No repo/archive tour.

## Report
End with: `DONE writer library/company-analysis/apple.html`
