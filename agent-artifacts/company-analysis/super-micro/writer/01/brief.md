# writer brief: company-analysis/super-micro (01)

Inputs:
- editorial-direction.md — house/press/series standard, declared reader
- commission.md — the market question, what the analysis must resolve, and the
  "Habits to break"
- writing-coach/01/voice-guide.md — how this analysis should sound
- researcher/01/evidence.md — the verified primary financials, the durability and
  cash-conversion findings, and the recorded thin spots and scope flag
- the initialized article at
  .nb-work/company-analysis/super-micro/library/company-analysis/super-micro.html
  and its contract under .nb-work/company-analysis/super-micro/.nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check --series company-analysis .nb-work/company-analysis/super-micro/library/company-analysis/super-micro.html --library /home/user/library-checkout

This round's focus: the argument the verified primary supports. The cash-conversion
finding is the spine: FY2026 net income of $2.23B against operating cash flow of
negative $6.81B, driven by the inventory and receivables build and financed by new
debt and preferred stock, is the answer to whether an assembler's growth turns
into cash. Build it from the filing's own cash-flow statement. On durability, the
verified eight-quarter gross-margin series (falling before the Q4 spike) is your
primary evidence that 17.5% reads as a single-quarter event, not a step change;
the management Q1 FY2027 guidance near 10.4-10.8% is the strongest one-off signal
but the researcher found it only in secondary earnings-call transcripts, so verify
it against a company-published transcript or on-record source before using it, and
if you cannot, attribute it plainly as reported guidance and note it is absent
from the filing while leaning on the verified series.

Orchestrator ruling on the March 2026 DOJ indictment of a cofounder (flagged in
the evidence's Contradictions): include it only if you can open and cite a
resolvable primary or fully on-record source; attribute it precisely to the named
individuals (not the company, which states it considers itself a victim); and do
not imply it explains the reported inventory or revenue, since nothing in the
record ties it to the numbers. If you cannot source it to a resolvable primary,
leave it out. The article's argument stands on the verified financials either way.

Build charts with `nb chart` from the verified series only, and commit provenance.
No buy, sell, or allocation call. Habits to break: no colon "two numbers, same
quarter" heading, no "what would have to change" closer, no closing
`nb-note-strong` verdict box.
