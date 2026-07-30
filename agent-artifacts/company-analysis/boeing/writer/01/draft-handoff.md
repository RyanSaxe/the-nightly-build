# Draft handoff — company-analysis/boeing (writer invocation 01)

Production: single-context, no isolation.

(The harness exposed no child-agent/subagent spawn tool, so the desk ran the full
role chain — writing-coach, researcher, writer, editor — in one context, in
sequence, each following its SKILL.md, with every artifact preserved. Degraded
mode is the same chain in one context, not a shorter one.)

## Original-work sentence
This article reconciles Boeing's reported swing to positive operating cash flow to
the single cash-flow-statement line that produces it — the $4,660 million rise in
customer advances — and shows that with that financing inflow set aside the
business consumed roughly $3.5 billion of cash in the first half while free cash
flow stayed negative $823 million: a reconciliation the filings report piecemeal
but never assemble.

## Article and assets changed
- `library/company-analysis/boeing.html` — authored from the initialized skeleton
  (nb-meta filled with measured values; orientation anchor + four flex sections +
  sources; stat strip, comparison table, waterfall figure, one Verdict note).
- `library/company-analysis/boeing/chart-1.py` — provenance for the cash-bridge
  waterfall; every value primary (Q2 2026 10-Q and Q2 2026 release) or a stated
  identity plug ("all other operating" +819).
- `library/company-analysis/boeing/chart-1.png` — rendered from chart-1.py;
  inspected as an image (bars honest, y-axis labeled "US$ millions", no misleading
  scale).

## Proof result
`nb check … --series company-analysis` → **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**.
First proof returned BLOCK 0 with three warnings, all cleared: two
W-SENTENCE-DENSITY (split the two 42/43-word sentences) and one W-SELF-COUNT
(nb-meta words corrected to the counted total; reading-minutes and byline updated
to match). All nine source URLs are network-checked and resolve. No warnings left
standing.

## Editorial requests addressed
First writer round; no editorial-review yet. (Editor read follows.)

## Source kinds
Six primary (S1 Q2 2026 release; S3 Q2 2026 10-Q; S4 Q2 2025 release; S5 Q1 2026
10-Q; S6 Q1 2026 release; S7 FY2025 release) and two secondary (S2 AeroTime,
recovery framing tested in the piece; S8 FlyingMag, the FAA 737 production cap as
context). No Boeing financial figure is attached to a secondary. GAAP
working-capital lines cite the 10-Q; the non-GAAP free-cash-flow figures cite the
releases that define and report them.

## Remaining evidence / voice questions
None. The 10-Q MD&A production-rate narrative did not survive document conversion,
so the 737 rate ceiling (38 -> 42) is carried by the secondary S8 as context only,
not as a Boeing primary statement; the argument does not depend on it. The FY2025
net-income line was deliberately excluded as load-bearing (see evidence Discarded);
the piece relies on no FY2025 net-income figure.
