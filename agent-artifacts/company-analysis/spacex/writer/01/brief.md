# writer brief: company-analysis/spacex (01)

Inputs:
- `agent-artifacts/company-analysis/spacex/editorial-direction.md` — house standard, press voice, series prompt, declared reader
- `agent-artifacts/company-analysis/spacex/writing-coach/01/voice-guide.md` — how this piece should sound
- `agent-artifacts/company-analysis/spacex/researcher/01/evidence.md` — the complete claim set available to you
- `.nb-work/company-analysis/spacex/library/company-analysis/spacex.html` — the initialized article to edit in place
- `.nb-work/company-analysis/spacex/.nb-context/` — effective template contract, runtime assets, furniture catalogs

Output: `agent-artifacts/company-analysis/spacex/writer/01/draft-handoff.md`
Proof: `./nb check .nb-work/company-analysis/spacex/library/company-analysis/spacex.html --series company-analysis --library /home/user/library-checkout`

Focus this round: follow the commission's "Recast from research" section — the
filing reports three segments, not two. Decompose the contested market
capitalization across what the reported segments support (Space with Starship
inside it; Connectivity/Starlink carrying the revenue; AI carrying the spending
after the Feb 2026 xAI combination), and state what each part must assume — above
all how much of the price rests on the profitable-at-EBITDA Connectivity business
versus the AI unit that consumed 86% of last quarter's capital with no profit
record. Teach the business where it clarifies the argument. Treat Starship as an
unquantified sub-item of Space. Do not issue a buy/sell/allocation call. Honor
every caveat in the recast: state the market cap as a range, attribute lock-up
figures as reported (the prospectus body could not be read), and reconfirm any
single load-bearing GAAP line before it headlines. A revenue-by-segment or
capex-by-segment chart (the 86%-of-capex-in-AI concentration is a striking,
chartable fact) is likely the right furniture if the evidence supplies a verified
series.

Recent habits to break (see commission): do not open on an `nb-stat`/`nb-stat-strip`
block, do not use the "what the price has paid for" / "the quarter the price has
to justify" heading mold, and do not close on a "two ways to read it" section.
Build a chart only from a verified series in the evidence record.
