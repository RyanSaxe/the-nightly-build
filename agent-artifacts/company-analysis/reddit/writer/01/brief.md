# writer brief: company-analysis/reddit (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `article` template identity, series prompt
- commission.md (artifact root) — the market question AND the "Research correction" section (read it: the drop is ~-21%, and the cause is a US DAUq miss + first sequential decline). Research governs.
- writing-coach/01/voice-guide.md — the voice, licenses (expectations-gap, three-number discipline, chart-inflection), and do-not-reuse list
- researcher/01/evidence.md — the ONLY claim set available; use its Numbers/Sources/Contradictions exactly, including the full quarterly series for charts
- The initialized article at `library/company-analysis/reddit.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/company-analysis/reddit/library/company-analysis/reddit.html --series company-analysis`
  `./nb check .nb-work/company-analysis/reddit/library/company-analysis/reddit.html --series company-analysis --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- The angle: a real beat-and-raise (rev $804.9M +61%, EPS $1.25, Q3 guide above
  Street) sold off ~21% close-to-close because a forward signal the headline
  hides turned down — US DAUq missed AND fell sequentially for the first time in
  the five-quarter series, with management citing "choppy" Google search
  referrals. Teach how price reacts to the change in expectations, not the level
  of results. Steelman both reads (rational durability re-rating vs. overreaction).
  No buy/sell/allocation call.
- Charts (chart-forward desk): build ONLY from the researcher's verified series
  with `nb chart`, commit each `chart-N.py` beside the article, inspect the
  rendered PNG. Strong candidates: US DAUq by quarter with the sequential dip
  marked; revenue with YoY growth; issued guidance vs. consensus. Label axes,
  cite the data source in the caption.
- Sourcing honesty: Reddit's SEC-filed releases own the financials/guidance
  (primary). Consensus estimates and the stock price are secondary/reported —
  attribute them as such; note the consensus spread by provider and that the
  close price is a market-data aggregator. No named analyst target cuts are
  available (sources gated); do not invent them.
- State the ~-21% close-to-close figure; you may note -13% as the after-hours
  way-station. Give every big number a comparison the reader knows.
- Article template: `orientation` required + 2-6 flexible sections + Sources.
  Word band 1500-4000. min 8 sources. A stat strip and a beat-vs-guide table fit.
