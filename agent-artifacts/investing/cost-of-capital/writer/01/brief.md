# writer brief: investing/cost-of-capital (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       angle, the prerequisite it builds on, boundaries
  ../../writing-coach/01/voice-guide.md     lesson craft and licenses (worked-case walkthrough)
  ../../researcher/01/evidence.md           the evidence record; the only claim set available
  the initialized article and its .nb-context (lesson template contract + furniture catalogs)
Output: agent-artifacts/investing/cost-of-capital/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Article to edit:
  .nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html
Lesson template: opens on "Why this matters", closes on "The takeaway" (both written after
the body); band 1200-2200 words; per-section citations (bookends exempt). Iterate proof
with --no-check-links, finish with links.

This round's focus (grounded in the evidence record):
- Teach cost of capital as the opportunity-cost hurdle ROIC must beat, closing the gap the
  prior return-on-capital lesson opened. Build cost of debt (after-tax; 26 U.S.C. §163
  deductibility), cost of equity (required return; CAPM as the standard taught tool), and
  WACC as the blend.
- Be honest that cost of equity is estimated, not observed: Fama & French (2004) find
  CAPM's empirical problems "probably invalidate its use in applications" even as it stays
  standard; the FERC order running four models on the same utilities and averaging them is
  a concrete live instance. Tie the hurdle back to the "what regulators call fair" callback
  via the Hope Natural Gas opportunity-cost standard.
- Example handling: there is NO single clean company that gives real debt, weights, and a
  WACC walk-through without an anomaly. Intel FY2025 shows the hurdle biting (full-year net
  loss against $14.6B capex) but its 98.3% effective tax rate is a one-time outlier —
  do NOT use it for the after-tax-cost-of-debt step. For a numeric low-risk vs high-risk
  contrast use Damodaran's industry-average table (Utility vs Semiconductor), noting it is
  a continuously updated dataset with no visible "as of" date. Keep the teaching transferable,
  not a company tour; do not default to Costco (the recent lessons' running example).
- Set nb-meta harness and writer model = sonnet. Outline the reasoning before naming
  flexible sections so no prior lesson's shape becomes this one's template.
