# Draft handoff: company-analysis/super-micro (writer round 01)

## Original work

The piece cross-reads five of Super Micro's own quarterly filings against
each other, something no single filing or press release does, to show two
things the evidence record states as separate facts but does not itself
assemble into an argument: the fiscal 2026 fourth-quarter margin spike sits
at the end of a five-quarter *decline*, not a stable base, which is the
strongest evidence available against "durable step"; and the $9.0 billion
gap between fiscal 2026 net income and operating cash flow is functionally
identical, quarter by quarter, to the inventory build shown on the balance
sheet and the first-half/second-half reversal in accounts payable, which the
filings never state as a single connected story. Chart 1, Chart 2, and the
financing table are built to carry that synthesis rather than to illustrate
numbers already argued in prose.

## Scope ruling resolved: the March 2026 DOJ indictment

Per the orchestrator's ruling, I attempted to open a resolvable primary or
fully on-record source before deciding whether to include this. The
researcher could not reach justice.gov (401/403). I found and opened a
different primary source the researcher's evidence record does not contain:
Super Micro's own Form 8-K, Item 5.02 and Exhibit 99.1 (accession
0001375365-26-000011, filed 2026-03-20), fetched and read directly (both the
main document and the exhibit, via a SEC-compliant User-Agent). It is
source 15 in this draft. It independently confirms the three individuals
charged and their roles, that Super Micro is not a defendant, Liaw's board
resignation and its stated reason, and the company's own "contravention of
policies" / "robust compliance program" language, all attributed to the
named individuals and the company, not implied as connected to the reported
financials, per the ruling. The $2.5 billion scheme figure and mechanics
still rest on the researcher's secondary source (Al Jazeera, source 14),
since that detail is not in the primary filing.

## Proof result

`./nb check --series company-analysis
.nb-work/company-analysis/super-micro/library/company-analysis/super-micro.html
--library /home/user/library-checkout`, links included, after `nb stamp`:
**BLOCK: 0, WARN: 0.** No warnings left intentionally; none remained after
the sentence-density and placeholder-label fixes made during drafting.

## Open question

None blocking. One judgment call for the editor to weigh: the Q1 FY2027
gross-margin guidance (10.4%-10.8%) and the 75/25 mix-versus-tariff
breakdown are carried only as attributed, call-reported figures (marked off
in an `nb-note`, sourced 7-8), per the brief, since I could not find or
verify a company-published transcript either. The durability argument in
"Why the fourth quarter reads as an outlier" leans primarily on the verified
eight-quarter series and treats that guidance as corroborating rather than
as a claim the argument itself rests on, which I believe matches the
brief's instruction but is worth the editor's independent read.
