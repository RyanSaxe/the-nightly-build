# Editorial review — company-analysis/apple (editor, round 01)

## Decision
**Approve.** No redraft required. All required changes were fixable within editor
scope (cuts and phrase-level corrections). `nb check` holds at BLOCK: 0, WARN: 0,
PUBLISHABLE after my edits.

## The three reads

Skeptic: thesis "Apple's record June quarter was carried by non-recurring drivers
(an iPhone upgrade cycle, Products' own margin expansion, and a one-time tariff
refund) while the recurring Services engine the compounder thesis depends on
decelerated and missed consensus"; tested 8 load-bearing claims; broke: none on
the numbers. Two labels were wrong and I fixed them (see below).

Cut: 2 sentences; worst tell: a redundant hedged-contrast summary ("The evidence
here is about the rate of growth, not the quality of it") restating the sentence
before it.

Reader: this gives me a decomposition no single source performs — that revenue
mix moved *toward* lower-margin Products this quarter (70.8%→71.9%; Services
29.2%→28.1%), so the blended-margin expansion happened *despite* an unfavorable
mix, driven by Products' own margin gain plus the tariff refund. That matches the
writer's original-work claim in draft-handoff.md and reads in the first-principles
register of the Damodaran/Thompson exemplars, not a median summary.

## Figures recomputed against Apple's filings (all verify)
From the 8-K Exhibit 99.1 (accession 0000320193-26-000018) and 10-Q
(0000320193-26-000020), and the Services time-series filings:
- Total net sales +16.4% ($109,417M/$94,036M); iPhone +21.7% ($54,252/$44,582,
  ~half of total at 49.6%); Mac +28.7%; iPad −5.9%; Wearables +6.5%;
  Services +12.1% ($30,739/$27,423). All match the prose.
- Revenue mix: Products 71.9%/Services 28.1% (FY26) vs 70.8%/29.2% (FY25) — the
  writer's own computation, verified exact.
- Gross margin 50.1% vs 46.5% (+3.6pt); Products 40.1% vs 34.5% (+5.6pt);
  Services 75.6% flat; segment-margin gap 35.5pt ("roughly 35 points"); Services
  worth 1.885× a Products dollar ("nearly twice"). All verify.
- Services miss ~1.5% ((31.22−30.739)/31.22 = 1.54%). Verify.
- Seven-quarter Services YoY series (13.9/11.6/13.3/15.1/13.9/16.3/12.1) matches
  chart-1 exactly; peak-to-current step −4.2pt. Verify.

## Brief-mandated sourcing checks
- **Tariff-refund attribution — correct.** The ~$0.11 EPS / ~2pt gross-margin
  figure is cited to source 1 (8-K Exhibit 99.1) and the prose states it is
  "attributed to Apple, not to any analyst," with a separate sentence noting the
  10-Q does not restate the precise numbers. This is Apple's own disclosure, not
  press-derived. Matches the evidence record.
- **Quarterly operating cash flow — omitted.** The flagged synthesis (implied
  Q3 OCF from subtracting two cumulative filings) does not appear anywhere in the
  article. Correct handling.
- **Q4 guidance — marked as call-remarks (secondary).** "The specific numbers for
  next quarter come only from the earnings call, not from any filing," cited to
  sources 12 (Six Colors) and 13 (9to5mac), both secondary. The 10-Q's qualitative,
  non-quantified "supply constraints" disclosure is cited separately to source 2
  (primary) and explicitly called qualitative ("no number attached, no quarter
  named"). Primary/secondary split is honest.
- **Fact / estimate / synthesis kept distinct** across the piece (filing facts in
  plain past tense; estimates attributed to "analysts had modeled" / consensus;
  synthesis marked as reasoning).
- **No buy/sell/allocation call.** Closing commits to a mechanism ("The compounder
  is still the larger, higher-margin half of the business... It just was not the
  half that produced this record"), not an instruction.

## data-nb-kind audit (all correct)
s1, s2, s6, s7, s8, s9, s10, s11 = Apple 8-K exhibits / 10-Qs, labeled **primary**.
s3 (Yahoo Finance), s4 (Variety), s5 (Tech Times), s12 (Six Colors), s13 (9to5mac)
= third-party reporting/analyst-estimate/transcript, labeled **secondary**. Every
label matches the evidence record; source numbering is first-citation order.

## Charts (each inspected against provenance script + rendered PNG)
- **chart-2.py → Fig. 1 (net sales by category).** Numbers (iPhone 44.582→54.252,
  Mac 8.046→10.352, iPad 6.581→6.191, Wearables 7.404→7.883, Services
  27.423→30.739) match source 1. Y-axis starts at 0. Caption cites s1. Honest.
- **chart-3.py → Fig. 2 (gross margin by segment).** Products 34.5→40.1, Services
  75.6→75.6, blended 46.5→50.1, with a labeled diamond marker at 48.1 for the
  ex-tariff blended margin ("Apple's approx."). Matches source 2 + the source-1
  tariff quantification. Y-axis 0–85. Caption cites s1+s2 and flags the
  approximation. Honest.
- **chart-1.py → Fig. 3 (Services YoY, 7 quarters).** Series matches the evidence
  table exactly; Q3 FY26 bar highlighted; caption says "computed from Apple's own
  quarterly SEC filings" (honest, since YoY is derived) and cites the underlying
  filings. Y-axis 0–19, starts at 0. Honest. No axis is truncated or misleading;
  no caption narrates the chart's shape.

## Direct edits made (prose/structure only)
1. Orientation: "an iPhone upgrade cycle and a **tax refund**" → "a **tariff
   refund**" — the established term is "tariff refund"; "tax refund" both broke
   name-consistency and was looser than the filing's wording.
2. Section heading: "A margin lifted by **mix** and a one-time refund" → "A margin
   lifted by **Products** and a one-time refund" — the section's own finding is
   that the revenue mix moved *against* the blended margin; crediting "mix" in the
   heading contradicted the body and used "mix" in the opposite sense from the
   paragraph's "unfavorable mix shift."
3. Margin section: cut the gross-margin definition sentence ("Gross margin is
   what's left of each sales dollar... before operating expenses."). The declared
   reader (math/CS, ML-eng, well-read) holds the term; the voice guide bars
   explaining quantitative basics, the delete test loses no reasoning step (the
   segment-margin mechanic is taught later), and the sentence carried a
   comma-spliced semicolon.
4. Services section: factual correction — "**two years ago**" (twice) misdated the
   11.6% Services low. That is Q2 FY2025, quarter ended March 29, 2025 (~5 quarters
   / ~15 months before this June-2026 quarter). Rewrote to name "the March 2025
   quarter" and, on the second reference, "that low," removing the error and a
   repetition.
5. Services section: cut "The evidence here is about the rate of growth, not the
   quality of it." — a redundant hedged-contrast summary of the sentence before it
   ("did not touch the segment's unit economics").

## Word count
Cuts reduced the counted total from 1873 to **1820** (still well inside the
1500–4000 band). Synced `nb-meta.words` to 1820 to keep the declared count honest.

## Proof after edits
`nb check library/company-analysis/apple.html --series company-analysis
--repo /home/user/the-nightly-build` → **BLOCK: 0, WARN: 0, PUBLISHABLE.**

## Work returned to other roles
None. No researcher or writer redraft required.
