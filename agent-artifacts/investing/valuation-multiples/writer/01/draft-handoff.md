# Draft handoff: investing/valuation-multiples (01)

## The one act of original work

The lesson runs the justified forward-P/E formula on each company's own
filing-derived return on equity, and in doing so makes a judgment the evidence
supplies the parts for but does not itself make: it spends the single-stage
formula on the two stable businesses (Coca-Cola near 30, Verizon near 14, both
close to the market's quote) and deliberately refuses to plug NVIDIA's 65%
growth into it, diagnosing NVIDIA's multiple instead through the gap between its
trailing (34x) and forward (22x) P/E as the fingerprint of the two-stage growth
the stable formula cannot hold. That sorting of the three companies into "the
formula explains this" and "the formula would misprice this" is the article's
own work on the evidence.

## Proof

Exact brief command, links included:

`./nb check .nb-work/investing/valuation-multiples/library/investing/valuation-multiples.html --series investing --library <library-checkout>`

Result: **BLOCK: 0, WARN: 0** (PUBLISHABLE). No warning left standing.

Stamped: 2196 words (band 1200-2200), 6 sources (floor 6; five primary, one
secondary), 10 min. Four W-SENTENCE-DENSITY warnings from the first draft were
resolved by splitting the sentences, not by repunctuating them.

## Evidence and voice notes for the editor

- **The r and g in the two worked plugs are owned as estimates, in prose.** The
  Coca-Cola (g 4%, r 7%) and Verizon (g 2.5%, r 8.5%) inputs are the researcher's
  clearly-labeled estimates, not figures any filing owns; the draft states this
  and notes a point either way moves the answer. ROE, the multiples, and every
  fundamental trace to a filing or to the market-data source. This follows the
  evidence's instruction to own r and g rather than present them as fact.

- **Both evidence cautions are carried in the prose, not left for the editor.**
  The denominator is named on every printed multiple, including in the stat
  strip, the table's two P/E columns, the opener, and the takeaway; the
  justified-versus-observed caution closes the "cheap is not cheap" section as
  the lesson's narrow, safe claim (different fundamentals justify different
  multiples; a low multiple is a hypothesis to test, not a verdict).

- **No chart was built, by choice.** The verified series is three companies, a
  thin scatter, and the one genuinely teachable curve (forward P/E against g)
  would have to be drawn from the estimated r and g the evidence says not to
  print as fact. The three-company table plus the annotated equation carry the
  contrast without a chart standing on estimates. No source asset was used: the
  evidence marks none worth lifting for the core numeric contrast.

- **Open item, environment only:** `nb render-check` reported "no Chrome in this
  environment; skipped," so the annotated equation's colored terms and legend,
  the table, and the stat strip were not eyeballed in a browser. The TeX and
  markup follow the furniture contract (one annotated equation, `nb-mc1..3`
  legend terms repeating their TeX), and the deterministic proof passes. If the
  editor has Chrome, a look at the two math figures would close this.
