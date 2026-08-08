# Draft handoff: company-analysis/palantir (writer 01)

## Original work (one sentence)

The piece converts Palantir's ~45x forward EV/sales into the concrete revenue
path the price requires — a roughly three-to-fourfold rise over several years,
with the stock returning nothing, merely to grow into today's ~$365B enterprise
value at a still-premium terminal multiple — then tests that required path against
the record's actual engine (a U.S.-only acceleration, RDV +124% front-running
revenue) and against the pre-print ~40% drawdown that undercuts the reflexive
"priced for perfection" read. The act is the price-to-required-revenue conversion
(the § "What 45 times sales requires" table and the falsification list), which the
evidence supplies figures for but does not itself perform.

## Proof result

`./nb check … --series company-analysis --library <scratchpad>/library`
(links included): **BLOCK: 0, WARN: 0 — PUBLISHABLE.** No warnings left standing.

Chart provenance: `library/company-analysis/palantir/chart-1.py` (committed beside
`chart-1.png`) builds the five-quarter U.S. commercial vs. U.S. government series
(306→764 vs 426→809, US$ millions) from the release-owned figures; rendered PNG
inspected — both series on one zero-based scale, distinguished by color and by
dash/marker, government dashed. Caption cites the five owning releases.

## How the evidence corrected the commission (followed the evidence)

- Report date is **August 3, 2026** (release/8-K), not "August 5"; used Aug 3.
- **No "triple-digit P/E."** Valuation anchored on forward **EV/sales ~45x** at the
  Aug 6 close ($155.92) / ~41x at the ~$144 after-hours reaction, computed from the
  10-Q share count and net cash. Forward P/E ~85x appears once, explicitly labeled
  secondary/analyst-derived, against the ~19x software median — as context, not anchor.
- Acceleration is **U.S.-only**: international +34%, share 27%→19% — stated plainly
  and made central to the "narrow footing" bear read.
- **GAAP net income is tax-flattered** (1.42% effective rate; a 21% rate would cut
  ~$200M) and **adjusted net income to common ($1,047.0M) sits below GAAP ($1,061.9M)**;
  both shown in the GAAP-vs-adjusted table and the surrounding prose. GAAP and adjusted
  kept distinct throughout.
- **~40% pre-print drawdown** engaged directly: it is the hinge that keeps both reads
  live and is used to complicate, not ignore, the "one stumble away" premise.
- **NDR not cited** (absent from both filings). **RPO $4.9B (Note 3)** and U.S.
  commercial **RDV $6.238B** kept as different measures; RDV labeled the company's
  non-GAAP figure including optional/cancelable amounts.

## Requirements met

- 2,949 words (band 1500–4000); 11 sources (floor 8): 6 primary filings + 5 secondary.
- **No buy/sell/allocation call.** Close names the falsification tests and hands the
  decision back (voice guide's "falsification close in place of a verdict").
- Business taught where numbers need it (Gotham/Foundry/AIP; government vs. U.S.
  commercial), not in a boxed overview.
- Dek breaks the recent CA molds (no "X masks Y," "A not B," "X rises as Y falls,"
  no semicolon reversal / suspended question / comma triad); two clauses only.
- Furniture carries evidence: stat strip (headline numbers), the segment chart, the
  required-revenue table, the GAAP-vs-adjusted table, one pull quote (the implied-
  assumption sentence), one note (the falsification test). No article-authored scripts
  or styles; house furniture only.
- nb-meta harness = "claude-code-routine", model = "Opus 4.8".

## Open questions for editor / evidence

None blocking. One judgment call worth a look: I led the enterprise-value arithmetic
on the **Aug 6 settled close ($155.92, stockanalysis, secondary, search-surfaced in
the evidence)** for the headline ~45x and cited the ~41x at the after-hours ~$144
(indmoney) as the range's low end. The brief did not call for a WebFetch to confirm
the price, so I did not add one; both dated prices are presented and cited, and the
~41–45x range is stated as price-sensitive and point-in-time. If the editor wants a
single hard-confirmed as-of price, that is the one input to re-verify. No peer-multiple
chart was built (evidence has no clean single-as-of-date peer set); the valuation-in-
context point is made in prose + the required-revenue table instead, per the brief.
