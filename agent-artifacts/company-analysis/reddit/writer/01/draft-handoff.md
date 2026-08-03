# Draft handoff: company-analysis/reddit (01)

## Original work

This article recasts Reddit's "beat-and-raise, stock down 21 percent" quarter as
a single expectations subtraction: it isolates US DAUq as the one forward signal
the price was underwriting, and then shows, with charts built from the primary
quarterly series, that even the raised Q3 guide encodes the slowest year-over-year
growth in the five-quarter run. The paradox resolves into a rule the reader can
carry to the next company: price moves on the change in the forward signal, not
the level of the reported result. The piece steelmans both the rational-re-rating
and the overreaction reads and issues no buy/sell/allocation call.

## Proof result

`nb check` (links on, against the library checkout) reports **BLOCK: 0, WARN: 0**;
verdict PUBLISHABLE. Word count 1685 (band 1500-4000), 9 sources (floor 8),
6 primary / 3 secondary. No warnings were intentionally left.

Three charts were built only from the researcher's verified series with
`nb chart`, each `chart-N.py` committed beside the article, and the rendered PNGs
and full page inspected via `nb preview`:
- Fig. 1 (chart-1): US DAUq by quarter, sequential dip and 53.98M consensus marked.
- Fig. 2 (chart-3): issued guidance band vs actual, showing Reddit beats its own guide.
- Fig. 3 (chart-2): revenue level rising while YoY growth steps down to 61%.

## Deviations and sourcing decisions the editor should see

- `nb stamp` does not accept the `--series` flag written in the brief's stamp
  command (`stamp.py` takes only the file). I ran `./nb stamp <file>` without it;
  the counts were written correctly. The `nb check` command was run exactly as
  briefed, links included.
- I did not cite two sources the evidence record supplied, to keep every listed
  source cited and every figure resolvably sourced:
  - The Q2 2026 Form 8-K wrapper (event/date). The July 30 report and all
    financials are carried by the press-release exhibit (s1), which I cite; the
    bare 8-K would have sat uncited, so it was dropped.
  - The Zacks Q3 2025 comparison, and with it the "same-size US miss, opposite
    reaction" counterexample. The evidence's ~14% Q3 2025 stock-reaction figure
    is researcher context, not a claim owned by an openable source I read, so I
    cut the counterexample rather than assert an unsourced reaction.
- I did not state the LSEG numbers (~$730M Q2 revenue consensus, ~$828M Q3 Street
  estimate). Their owning source (CNBC) was gated/discarded and I did not open it.
  The Q2 beat is attributed to the openable Zacks consensus (s3); the provider
  spread is noted qualitatively; the Q3 raise is stated as the primary guide range
  (s1) "above what analysts had modeled," corroborated by The Motley Fool (s9),
  and its implied ~48% YoY growth is computed from the primary series.
- The ~21% close-to-close figure ($178.04 to $140.67, -20.99%) is stated per the
  research correction; -13% is noted only as the after-hours way-station.

## Open questions

None blocking. If the editor wants the Q3 2025 counterexample restored or the
exact LSEG consensus figures cited, that needs a new researcher artifact opening
a resolvable source for the Q3 2025 stock reaction and the LSEG estimates.
