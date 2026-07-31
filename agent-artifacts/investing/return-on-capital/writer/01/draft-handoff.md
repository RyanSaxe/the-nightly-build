# Writer handoff — investing/return-on-capital (01)

## Original-work sentence

The article takes three things the evidence record supplies separately —
Costco's balance-sheet debt/equity/cash lines, its income-statement operating
income and tax provision, and AEP's equivalent figures under a stated
convention — and fuses them into one argument the evidence itself does not
make: that a single worked ratio (ROIC) turns three statements' worth of
numbers into one comparable judgment, and that judgment only means something
once it is set against a cost-of-capital yardstick, which is why Costco's 37.4
percent and AEP's 4.9–6.4 percent land on opposite sides of the value-creation
line even though both are "profitable" companies.

## Article path

`.nb-work/investing/return-on-capital/library/investing/return-on-capital.html`
(no source assets or chart provenance used — the two contrast tables are
built entirely from the evidence record's own worked numbers, not captured
visuals or rendered charts).

## What the lesson teaches, in order

1. **Invested capital** (orientation section, "The money behind the profit"):
   defined from the balance sheet already taught in this course, worked as
   debt + equity − cash for Costco ($5,788M + $29,164M − $14,161M =
   $20,791M), shown in an `nb-table`. The convention (cash-only netting,
   year-end balance, no lease capitalization) is stated explicitly, with the
   three honest alternates and their actual swung numbers (39.5%, 22.2%,
   38.5%) named in one clause each rather than relitigated.
2. **ROIC = NOPAT / invested capital** ("Thirty-seven cents on the dollar"):
   NOPAT defined against ordinary net income, then worked once end to end for
   Costco as a plain sentence per the voice guide — $10,383M operating income
   × (1 − 0.2513) ≈ $7,773M NOPAT, divided by $20,791M ≈ 37.4% ROIC — with no
   boxed equation and no restating sentence after the number.
3. **The value-creation test** ("The number growth has to clear"): the
   ROIC-vs-cost-of-capital principle from Damodaran, then AEP worked the same
   way under three tax-rate conventions (a new `nb-table`, since three rows
   of one shape is the furniture catalogue's own trigger for a table rather
   than a semicolon-chained sentence), landing in the 4.9–6.4% band regardless
   of tax convention. The contradiction the evidence flagged — Damodaran's
   sector WACC (4.36%) and AEP's own regulator-approved ROE (9.25%–10.9%)
   point in different directions about whether AEP clears its cost of capital
   — is addressed directly in prose: the regulatory ROE is used as the primary
   yardstick (same question ROIC asks, about this specific company), the
   sector WACC is kept as a named secondary reference, per the evidence
   record's own recommended framing. WACC's precise computation and full
   valuation are explicitly left to a later lesson.

## Word / source counts (measured, not targets)

- Words: 2,027 (`nb-meta`), within the 1200–2200 band.
- Sources: 7 (all read by the researcher; 3 primary — Damodaran's ROIC paper,
  Costco's 10-K, AEP's 10-K — plus Damodaran's sector WACC dataset as a 4th
  primary; 3 secondary — Wall Street Prep, Corporate Finance Institute,
  Enerdynamics). All 7 are cited in first-citation order; none are decorative.
- Reading minutes: 10.

## Proof result

```
./nb check .nb-work/investing/return-on-capital/library/investing/return-on-capital.html \
  --series investing --library /home/user/library
```
`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. No warnings left unresolved —
the initial run flagged one `W-SELF-COUNT` (nb-meta words placeholder) and
seven `W-SENTENCE-DENSITY` findings (several long semicolon/colon-chained
sentences, including a three-way tax-rate list that read as a run-on); the
words field was corrected and the dense sentences were split or, in the
tax-rate case, converted into the `nb-table` the furniture catalogue calls
for when three rows share one shape. Final proof carries zero findings.

## Remaining evidence or voice questions

None. The evidence record's own recommended framing for the AEP contradiction
(regulatory ROE as the primary yardstick, sector WACC as a flagged secondary
reference) was followed as written, and the voice guide's specific
instructions (division as a clean sentence, not a boxed equation; conventions
disclosed in one clause each, not relitigated; headings named for this
lesson's own argument steps) were followed throughout. No researcher or
writing-coach request was needed.
