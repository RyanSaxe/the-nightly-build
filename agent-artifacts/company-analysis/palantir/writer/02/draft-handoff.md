# Draft handoff: company-analysis/palantir (writer 02)

Revision applying the three required fixes in editor/01. No figures, tables,
stat strip, chart, GAAP/adjusted separation, or sourcing content was disturbed;
the claim set is unchanged.

## Original work (one sentence — unchanged, still holds)

The piece converts Palantir's ~45x forward EV/sales into the concrete revenue
path the price requires — total revenue roughly tripling over several years with
the stock returning nothing, merely to grow into today's ~$365B enterprise value
at a still-premium terminal multiple — then tests that required path against the
record's actual engine (a U.S.-only acceleration, RDV +124% front-running
revenue) and against the pre-print ~40% drawdown that undercuts the reflexive
"priced for perfection" read. The act is the price-to-required-revenue conversion
(the § "What 45 times sales requires" table and the falsification list), which
the evidence supplies figures for but does not itself perform.

## Editorial requests resolved (one line each)

- **Headline (editor: reframe off the 149% rate the body refutes).** Retitled to
  "Palantir's price bets on four more years of 40 percent revenue growth" — the
  requirement the table actually proves (total revenue ~tripling over ~4 years at
  ~40% with the stock flat), not the U.S. commercial +149% quarter. Changed in all
  three surfaces: `<title>`, nb-meta `title`, and the `<h1>`.
- **Dek (editor: tripling is TOTAL revenue, not U.S. commercial).** Deleted
  "U.S. commercial" so the dekline now reads "…the price still needs revenue to
  roughly triple…", matching the table, pull quote, and close (total revenue from
  the $8.15B guide). nb-meta `dek` corrected in concert and kept byte-identical to
  the rendered dekline.
- **Closing coda + citation.** Cut the three self-grading / prompt-leaking
  sentences ("The commission was to weigh…", "The requirement is now stated as
  arithmetic:", "The breakage is stated as its negation…"). Kept the falsification
  handoff: the "What would settle it" note stands, and the piece now closes on
  "…Which way the reader leans is the reader's to decide." The recast final
  paragraph opens "The price is buying one thing:" and carries the substantive
  restatement (revenue roughly triples, stock flat, U.S.-led demand wave) as
  argument rather than method-summary. The orphaned CNBC citation (s11) was
  **dropped** rather than relocated: the after-hours pop and guidance raise it
  corroborated are already carried by s4 (INDmoney) and s1 (the release), so no
  claim is left unsupported, and dropping the last-numbered source keeps
  first-citation order intact with no cascade renumbering of s1–s10. `nb stamp`
  recomputed the count to 10.

## Proof result

`./nb check … --series company-analysis --library <scratchpad>/library`
(links included): **BLOCK: 0, WARN: 0 — PUBLISHABLE.** No warnings left standing.

Display-text pass re-run: headline and dek now state the requirement the body
proves (~40% total, revenue roughly triples), not the 149% / U.S.-commercial
rate the body refutes; nb-meta `dek` and the rendered dekline are identical;
nb-meta harness "claude-code-routine" / model "Opus 4.8" unchanged. Word count
2899; sources 10 (6 primary filings + 4 secondary), floor 8 satisfied.

## Open questions

None blocking. Same standing judgment call as writer/01: the enterprise-value
arithmetic leads on the Aug 6 settled close ($155.92, secondary), with the ~41x
at the ~$144 after-hours reaction cited as the range's low end; both dated prices
are shown and the range is stated as price-sensitive and point-in-time.
