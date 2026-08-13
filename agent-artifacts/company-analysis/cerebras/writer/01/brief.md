# writer brief: company-analysis/cerebras (01)

Inputs:
- editorial-direction.md (house standard, slop, headlines, press voice, article
  template identity, series prompt) — at the artifact root
- commission.md (the market question, teach-the-business, chart-forward desk, the
  no-buy-sell-call boundary) — at the artifact root
- writing-coach/01/voice-guide.md (how this piece should sound)
- researcher/01/evidence.md (the complete set of claims; use its Numbers section
  exactly; preserve full series for charts)
- the initialized article: library/company-analysis/cerebras.html
- template context under .nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/company-analysis/cerebras/library/company-analysis/cerebras.html --series company-analysis --library /home/user/library-checkout

The market question and the substance (from the evidence record): Cerebras is
public (Nasdaq CBRS, IPO May 2026), and its Q2 2026 10-Q was filed 2026-08-12. Two
findings sharper than a flat "concentration and margins" read, both fully
traceable in the filing: (1) customer concentration did not ease so much as
ROTATE — the historically dominant related-party pair fell from ~88% of H1
revenue in 2025 to ~59% in H1 2026, but a single new customer took roughly
20-32% of quarterly revenue, so total top-few concentration barely moved; (2) the
same quarter's gross margin tells opposite stories under GAAP (fell to ~14.2%)
and the company's own "core" non-GAAP (rose to ~41%), a gap fully traceable to
specific disclosed items (a one-time IPO stock-comp catch-up, ~$1.1B of customer
warrants amortized against revenue through 2031, an inventory charge). The $25.4B
RPO backlog is the third thread; the filing says "a significant amount" traces to
the largest customer's agreement but does not quantify the per-customer share —
report that as the limit it is. Honor these record limits: customers are labelled
A/B/C/D in the 10-Q and not named, so any named attribution (G42, MBZUAI, OpenAI)
must be flagged as inference/secondary, not stated as the filing's own; and the
earnings-call transcript was inaccessible, so do not attribute management color.
Do not issue a buy, sell, or allocation call.

Build charts only from the evidence record's verified series via `nb chart`
(candidates: revenue by quarter; GAAP vs core gross margin; concentration share
over time) — inspect each rendered image and commit its provenance. Meet the
series source floor of 8 with primaries you actually cite (10-Q, IPO/pricing
filings, 8-K/press materials) plus verified secondaries — never pad.

Recent shapes to break (from the commission): recent company pieces (SpaceX,
Palantir) headline on price, open with "the quarter the price has to justify,"
run a valuation-multiple middle, and close on a "where the two reads part"
verdict. Turn this piece on the business question (concentration rotation, the
contested margin, backlog quality) rather than a pure price-versus-multiple
frame, and keep the opener, section order, and closer off those molds.

nb-meta: date "2026-08-13", harness "claude-code-routine", model "claude-sonnet".
Run `nb stamp` before the final links-checked proof.
