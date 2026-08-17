# writer brief: company-analysis/peloton (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md (house standard, press voice, series prompt, article-template identity)
- commission.md            ../../commission.md (market question, boundaries, recent-pattern habits)
- voice-guide.md           ../writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- evidence.md              ../researcher/01/evidence.md (complete claim set; read Numbers and Contradictions closely)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/company-analysis/peloton/library/company-analysis/peloton.html
- effective contract       /home/user/the-nightly-build/.nb-work/company-analysis/peloton/.nb-context

Output: /home/user/the-nightly-build/.nb-work/company-analysis/peloton/agent-artifacts/company-analysis/peloton/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/company-analysis/peloton/library/company-analysis/peloton.html --series company-analysis --library /tmp/claude-0/-home-user-the-nightly-build/b3d5d9d7-6994-5933-851f-0ef1bb302a4b/scratchpad/library-checkout

This round's focus (decisions the evidence carries and must not be lost):
- The argument is earnings quality and durability, not price. No buy/sell/hold/allocation call. The disagreement is internal to Peloton's own FY2026 filing: management frames the year as an "improved revenue trajectory" while the same statements show revenue falling (-1.8% to $2,446.0M; hardware -5.7%) and FY2027 guidance calling for a further ~4% decline.
- Show, do not assert, where the first full-year GAAP net income ($63.2M) came from: the ~$197M swing to operating profit was ~$178M cost reduction versus only ~$18M gross-profit gain, with negligible tax. So the profit is real, not a tax artifact, and it came mainly from cost-out amid contraction.
- Handle free cash flow with its reconciliation shown, not as clean earnings: FCF +17% to $377.6M leans on a $198.6M stock-comp add-back and an $81.3M inventory drawdown that cannot recur. The durable side is also real and sourced: subscription gross margin 73.6% and rising; subscription revenue roughly flat while paid connected-fitness subscribers fell 8.8% to 2.553M (a pricing/ARPU effect, but note Peloton discloses no clean connected-fitness subscription ARPU, so keep that point directional); adjusted EBITDA +16% to $468.2M; churn up to 2.2% from 1.8%.
- Note the concentration: roughly $61.6M of the $63.2M full-year profit landed in Q4, which also absorbed a $23.8M one-time legal charge, so the first three quarters were near breakeven. This bears directly on how durable one profitable year is.
- Give the post-earnings stock move as a sourced range (~11% to ~15.6%), not a single figure, and do not pin it to a primary market feed the evidence does not have.

Furniture: this is chart-forward. Build committed charts only from the evidence record's verified multi-period series (revenue by stream over time, the path to operating profit, connected-fitness subscribers/churn, free cash flow with its add-backs), per spec/charts.md; use `nb chart`, inspect the rendered image, commit provenance. Charts carry evidence, not decoration.

Recent habits to break: do not open on a valuation reveal or the "reported $X, but this metric was $Y" headline mold, and do not walk the cash-flow statement to stage a reveal the way recent pieces have. Outline the reasoning from this article's own question. Teach the business from zero where the reader first needs it, not in a fixed overview. Source floor: at least 8 sources, Peloton's SEC filings first. Fill nb-meta harness and writer-model fields; nb stamp writes counts.
