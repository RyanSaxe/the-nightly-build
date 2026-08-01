# Draft handoff — company-analysis/apple (writer, round 01)

## Original work

The article decomposes Q3 FY2026's revenue and margin record into its
cyclical and one-time drivers (an iPhone upgrade cycle, Products' own
margin expansion, and a tariff refund) versus the recurring Services
engine, and it computes — from Apple's own category dollars, a step no
single cited source performs — that revenue mix actually moved *toward*
the lower-margin Products segment this quarter (70.8% to 71.9% of net
sales; Services fell 29.2% to 28.1%). That finding is read together with
the Services deceleration and consensus miss to answer, on the terms the
evidence supports and without a buy/sell/allocation call, whether the
quarter's record supports or undercuts the "services compounder" framing.

## Paths changed

- `library/company-analysis/apple.html` — full article, replacing the
  initialized skeleton.
- `library/company-analysis/apple/chart-1.py` / `chart-1.png` — Services
  YoY growth, 7 quarters.
- `library/company-analysis/apple/chart-2.py` / `chart-2.png` — net sales
  by category, Q3 FY2025 vs. Q3 FY2026.
- `library/company-analysis/apple/chart-3.py` / `chart-3.png` — gross
  margin by segment, with the tariff-refund-adjusted blended margin
  marked.
- `agent-artifacts/company-analysis/apple/writer/01/draft-handoff.md` —
  this file.

All three charts were rendered with `nb chart` (Chrome/Kaleido installed
via `scripts/install-charts.sh`) and inspected as PNGs before embedding;
each script's docstring documents the exact filing(s) and accession
numbers behind every data point, per docs/charts.md.

## Proof

`nb check library/company-analysis/apple.html --series company-analysis --repo /home/user/the-nightly-build`
(cwd `.nb-work/company-analysis/apple/`, link-checking on) →
**BLOCK: 0, WARN: 0, PUBLISHABLE.**

Words: 1,873 (band 1500–4000). Sources: 13 (8 primary — Apple's own 8-K
exhibits and 10-Qs; 5 secondary — Yahoo Finance, Variety, Tech Times, Six
Colors, 9to5mac), min_sources 8. No warnings left standing; earlier
sentence-density and self-count warnings were fixed by splitting the
flagged sentences and syncing `nb-meta.words` to the counted total.

## Fact/estimate/synthesis handling

- Tariff-refund quantification (~$0.11 EPS, ~2pt gross margin) is cited to
  the 8-K press release (Apple's own disclosure), with a separate sentence
  noting the 10-Q does not restate the precise figures — matching the
  evidence record's flagged distinction.
- The Services consensus estimate (~$31.2B) and the stock's after-hours
  move are attributed to analysts/market reaction via two independent
  secondary outlets, never stated as Apple's own figures.
- Q4 FY2026 guidance (revenue growth, margin range, tariff/supply
  language) is sourced only to the two independently agreeing call
  transcripts (Six Colors, 9to5mac) and explicitly marked as call-only,
  distinct from the 10-Q's qualitative, non-quantified "supply
  constraints" disclosure, which is cited separately as primary.
- The quarterly (non-cumulative) operating cash flow figure from the
  evidence record is a flagged synthesis (subtracting two cumulative
  filings) and was **omitted** rather than used — it doesn't bear on the
  services/hardware question and wasn't worth carrying the caveat for.
- The Products/Services revenue-mix shift (70.8%→71.9% / 29.2%→28.1%) is
  presented as the writer's own computation from Apple's primary category
  dollars, not as an Apple-stated figure.

## Open items

None outstanding. No editorial-review round exists yet (this is round
01). No further researcher or writing-coach questions.
