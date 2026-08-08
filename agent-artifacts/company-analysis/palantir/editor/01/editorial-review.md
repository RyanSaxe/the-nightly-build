# Editorial review: company-analysis/palantir (editor/01)

## Skeptic

Thesis: a ~45x forward EV/sales price on Palantir is a specific forecast — total
revenue must roughly triple over several years while the stock returns nothing,
merely to fall to a still-premium multiple — and the record supplies two honest,
opposed reads of whether that path holds, which the pre-print ~40% drawdown
sharpens rather than settles. The load-bearing claims: (1) the enterprise trades
near 45x this year's guided revenue; (2) at 30-40% growth that valuation implies
revenue tripling over ~3-4.5 years with the stock flat; (3) the acceleration is
U.S.-commercial-led and internationally thin; (4) reported GAAP net margin is
flattered by a ~1.4% tax rate; (5) the drawdown complicates the "priced for
perfection" shorthand. Each was tested against the primaries.

I recomputed every figure. All of them hold:
- Revenue $1.935B, +93% (1,935,464 / 1,003,697 = +92.8%). U.S. commercial $764M
  +149% (764/306 = +149.7%). U.S. government $809M +90%. Rest-of-world +34%
  (362,417/271,105), share 27%->19%. U.S. revenue $1.573B +115%, 81% of total.
  All match the releases and 10-Q Note 12.
- Valuation: 2.403B basic shares x $155.92 = $374.6B; less $9.41B net cash =
  $365.2B EV; / $8.154B guide = 44.8x (~45x). At ~$144: $336.6B EV / $8.154B =
  41.3x (~41x). Consistent with the evidence's 41.4x and honestly range-bounded.
- The required-revenue table reconciles at all three rows: EV $365B held flat,
  10x -> $36.5B (4.5x FY26, ~4.5 yrs at 40%); 15x -> $24.3B (3.0x, ~3.2 yrs);
  20x -> $18.3B (2.2x, ~2.4 yrs). Year counts check to the logarithm.
- Margins: GAAP op $912.0M / 47%; adjusted op $1,194.5M / 62% = 912.0 + 265.2
  SBC + 17.3 payroll tax. SBC 13.7% of revenue, down from 15.9%. Diluted shares
  +0.2% YoY. Net income $1,066.0M, 55% margin > 47% op because interest $77.5M +
  other $91.8M and tax of only $15.4M on $1,081.3M pretax (1.42%); at 21% the
  tax is ~$227M and net ~$854M, ~$212M lower. Adjusted net to common $1,047.0M
  sits below GAAP net to common $1,061.9M via the ~$297M normalized tax. Both
  diluted EPS $0.41. FCF $1.22B/63%; OCF 6mo $2.1B vs $22M capex; Rule of 40 =
  93 + 62 = 155. Every one matches.

The five evidence hazards are all handled correctly: GAAP and adjusted stay
distinct and the tax-flattering is stated plainly; adjusted-below-GAAP is stated;
RPO ($4.9B, GAAP) and U.S. commercial RDV ($6.238B, non-GAAP incl. optional/
cancelable) are kept as different measures; NDR is never cited; the ~34%
international line is explicitly separated from the U.S. acceleration, not
conflated. Report date is August 3, 2026 (not Aug 5) throughout. No buy/sell/
allocation call anywhere; the close hands the decision back. I confirmed the two
secondary prices by WebFetch (stockanalysis.com: Aug 6 close $155.92, Aug 3
close $125.65), so the headline anchor is sound and dated; no re-verification is
needed. data-nb-kind labels are correct (the three price/estimate sources are
secondary; the six filings primary). The chart's committed script matches the
verified series exactly; the rendered PNG is honest (zero baseline, both segments
on one scale, commercial solid / government dashed), and its caption is factual
and cited to the five owning releases.

Where the skeptic read breaks the piece is not in a number but in the display
text, which labels the analysis with a figure the analysis does not use:

- **Headline.** "Palantir's price bets on four more years like its 149% quarter"
  attaches the required path to the quarter's flashiest rate, U.S. commercial
  +149%. The article's own arithmetic requires ~40% *total* revenue growth
  (30-40%) for ~3-4.5 years. Four years at anything near 149%, or even the 93%
  total, overshoots the table by an order of magnitude. The single most-read line
  states a required growth rate the body spends four sections refuting. A true
  duration ("four more years") is welded to a false rate ("like its 149%
  quarter"). This is display-text and belongs to the writer.

- **Dek.** "the price still needs U.S. commercial revenue to roughly triple"
  misattributes the tripling to the U.S. commercial line. The table, the pull
  quote ("Palantir's revenue roughly triples"), and the close all make it *total*
  revenue tripling from the $8.15B guide. For total to reach ~$24.3B, U.S.
  commercial would have to grow far more than 3x, so the dek is not merely
  imprecise, it is the wrong subject. The fix is a deletion ("U.S. commercial"),
  but the dek is mirrored in the `nb-meta` block and should be corrected in
  concert with the headline; routed to the writer to keep both display surfaces
  consistent.

## Cut

The prose is disciplined and I found little slack to trim; the earns-its-place
test passes almost everywhere. The genre temptations the voice guide warns about
are largely resisted: "priced for perfection" appears only as the shorthand the
piece then complicates with the drawdown, which is the licensed use, and the
required-revenue conversion is exactly the Damodaran/Gurley move the guide
licenses.

The worst tell is a self-grading, prompt-leaking coda that opens the final
paragraph: "The commission was to weigh what a valuation this large requires and
what would break it, and to stop there. The requirement is now stated as
arithmetic: ... The breakage is stated as its negation, in figures the coming
quarters will report." "The commission was to ..." lifts a word from the briefing
stack and claims the article fulfilled its assignment; "is now stated as
arithmetic" and "is stated as its negation" narrate the article's own method
instead of arguing. The editorial standard bans self-reference and prompt
leakage, and the cut read bans method-summary. This coda must go, leaving the
licensed falsification handoff ("Which way the reader leans is the reader's to
decide") as the close.

I did not cut it directly because the CNBC citation (s11) currently sits on that
final sentence, where it supports nothing ("the reader's to decide" is not a CNBC
claim). Removing the coda would orphan a declared source and drop the count from
11, which is markup/citation work. So the recast and the citation relocation go
together to the writer rather than a half-cut that breaks the proof.

Two lighter notes, neither blocking and neither cut: "That collision is the only
question worth asking about Palantir today" leans on unearned scope, and "A
multiple is not a verdict; it is a forecast wearing a single number" spends its
one hedged-contrast license on a faintly ornamental image. Both clear the bar as
written; I flag them only so the writer sees them while reworking the close.

No repeated structural formula across the piece: the five headings are argument
steps in the piece's own nouns, and the dek avoids the flagged CA molds (its only
defect is the accuracy one above).

## Reader

Read straight through as the paper's numerate, company-blind reader, the piece
delivers what the sources alone do not: a price decomposed into the concrete
forward revenue path it embeds, then that path tested against the actual engine
(a U.S.-only wave, RDV front-running revenue) and against the drawdown that
undercuts the reflex bear case. The required-revenue table and the falsification
list are genuine original analysis; the evidence supplies the inputs but performs
neither. That matches the draft-handoff's original-work sentence, and the answer
survives. The prose sits clearly closer to the Damodaran/Gurley exemplars than to
a median summary: it converts the multiple into checkable assumptions and refuses
the verdict. The one failure the reader meets is that the headline and dek out
front advertise a different, wrong claim (149% / U.S. commercial triples) than the
strong analysis behind them (~40% total, revenue triples). The body earns
publication; the display text mislabels it.

## Edits

None made directly. Every defect is display-text (headline, dek, both mirrored in
`nb-meta`) or a closing recast entangled with citation s11, all of which are the
writer's to fix; no clean editor-only cut was available, so no `nb stamp` was run.

## Required work

- **writer — headline.** Reframe so the most-read line states the requirement the
  article actually proves: total revenue must roughly triple over ~4 years at
  ~40% (with the stock flat), not "four more years like its 149% quarter." Do not
  anchor the headline on the U.S. commercial 149% rate the body refutes.
- **writer — dek.** The tripling is *total* revenue, not U.S. commercial. Correct
  "U.S. commercial revenue to roughly triple" (the deletion of "U.S. commercial"
  is the minimal fix) and mirror the change in the `nb-meta` dek so both surfaces
  agree with the table and pull quote.
- **writer — closing coda + citation.** Remove the self-grading / prompt-leaking
  sentences that open the final paragraph ("The commission was to weigh ...";
  "The requirement is now stated as arithmetic:"; "The breakage is stated as its
  negation ...") and let "Which way the reader leans is the reader's to decide"
  close the piece. Relocate the CNBC citation (s11) to a sentence it actually
  supports — the beat / guidance-raise / after-hours context in the orientation —
  or drop it and update the source count in `nb-meta`.

No researcher work: the evidence is solid, the two secondary prices are confirmed,
and no new evidence is needed. No orchestrator work.

## Decision

revise — the numbers, chart, sourcing, and argument are publication-grade, but the
headline and dek label the analysis with a growth rate (149% / U.S. commercial)
the body refutes, and a self-grading coda leaks the assignment; all three are the
writer's to fix.
