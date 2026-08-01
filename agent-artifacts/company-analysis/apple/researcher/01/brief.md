# Researcher brief — company-analysis/apple (01)

## Your job
Read and verify Apple's fiscal Q3 2026 record from the filings themselves, then
write the evidence record the writer uses to answer the market question
(services compounder vs hardware-cycle company). Min_sources 8.

## Exact inputs (start here)
- `agent-artifacts/company-analysis/apple/commission.md`
- `agent-artifacts/company-analysis/apple/editorial-direction.md`

## Read the primary first (series consult)
Apple CIK 0000320193 on SEC EDGAR (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=8-K&dateb=&owner=include&count=40)
and Apple newsroom (https://www.apple.com/newsroom/2026/07/apple-reports-third-quarter-results/).
Pull, exactly, for the quarter ended 2026-06-27:
- Total net sales; Products vs Services split; **product-line revenue** (iPhone,
  Mac, iPad, Wearables/Home/Accessories); YoY growth for each.
- Gross margin (total, and Products vs Services margins if disclosed);
  operating income; net income; diluted EPS.
- **The tariff-refund impact** — find Apple's own disclosure/CFO commentary
  quantifying the EPS (~$0.11) and gross-margin (~2pt) effect; quote it. If
  Apple did not itself quantify it and the figure is analyst/press-derived, say
  so and classify accordingly.
- Operating cash flow; any capital-return / buyback figures.
- Guidance commentary (the "supply constraints" note), quoted.
Prefer the 10-Q for the quarter if filed; otherwise the 8-K exhibit financial
statements + press release. Give exact URLs and the statement/line each number
comes from.

## Also capture (secondary, for the estimate/miss)
- The Services analyst-expectation figure (~$31.2B) and that Services missed —
  from reputable reporting (e.g., CNBC/Yahoo/Variety). Quote it with URL. This is
  an estimate vs actual; classify the estimate source as secondary.
- Recent-quarters Services revenue and YoY growth (last ~6–8 quarters) so the
  writer can chart the deceleration — pull each quarter's actual from Apple's
  prior releases/filings (primary). Provide a clean table of {quarter, Services
  revenue, YoY%} with per-figure sources for a `nb chart` provenance script.

## Deliverable
`agent-artifacts/company-analysis/apple/researcher/01/evidence.md`:
- Numbered evidence entries: claim, exact figure/quote, source publisher+title+
  URL, statement/line locator, primary/secondary + reason.
- A clean data table (with sources) ready for a chart provenance script.
- Contradictions/uncertainties (e.g., whether the tariff-refund quantification is
  Apple's or press-derived; any figure you could not confirm to a filing).
- Discarded sources. 8+ solid entries.

## Constraints
- Read the filings; do not trust a headline's number. A paywall/403 is gated —
  SEC EDGAR is open; use it. Never record an unverified URL.
- Begin with the named inputs; focused research only, no repo/archive tour.
- Missing context: `REQUEST researcher <one-sentence need>`.

## Report
End with: `DONE researcher agent-artifacts/company-analysis/apple/researcher/01/evidence.md`
