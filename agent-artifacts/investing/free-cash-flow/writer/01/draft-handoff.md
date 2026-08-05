# Draft handoff: investing/free-cash-flow (writer/01)

## Original work (one sentence)
This lesson constructs, from Apple's own FY2024 and FY2025 cash-flow-statement
lines, the two-year free-cash-flow bridge the filing never reports as a line,
showing free cash flow falling about 9% while net income rose about 19%, and
uses that constructed divergence to teach that free cash flow is a measure the
reader builds and must interrogate, not a number to look up. The work is visible
in the worked-calculation table and the section that reads the two years against
each other.

## Proof result
`nb check … --series investing --library <library-checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings intentionally left. All
six source URLs resolved under link-checking. `nb preview` builds the article
cleanly; the worked table and the FCFF/FCFE `\begin{aligned}` equation render.

## What the lesson teaches (three ideas, taught completely)
1. Free cash flow is a constructed, non-GAAP measure with no uniform definition
   (SEC C&DI 102.07) — the standard construction is operating cash flow minus
   capex, answering what net income cannot. Builds on `profit-versus-cash`
   (linked in Background, not re-taught).
2. How to build it, line by line, with the verified Apple FY2025 worked example:
   net income 112,010, add-backs (D&A 11,698, SBC 12,863), ~$25B of working-
   capital and other adjustments → OCF 111,482; less capex 12,715 → FCF 98,767.
   Statement structure anchored to IAS 7. Capex is not split maintenance/growth,
   flagged as analyst judgment.
3. The honest trap: FCF fell ~9% (108,807 → 98,767) while net income rose ~19%
   (93,736 → 112,010), driven by higher capex and a ~$27B working-capital swing;
   and "free cash flow" names more than one construction (SEC OCF−capex vs
   Damodaran FCFF vs FCFE), which start from different lines and are not conflated.

## Sourcing notes for the editor
- `min_sources: 6` met with six primaries, each carrying a distinct load: SEC
  C&DI (s1, the non-GAAP/no-uniform-definition point), IAS 7 (s2, the three-
  category structure), Apple 10-K filing (s3, fiscal-year/filing-date identity),
  Apple Consolidated Statements of Cash Flows / R8 (s4, every figure and the
  table), Damodaran Little Book cash-flows chapter (s5, FCFF/FCFE definitions),
  Damodaran FCFF primer PDF (s6, that FCFF adds back only depreciation, not SBC).
  Both Damodaran entries were opened by the researcher; they are split by claim,
  not padded. Only sources the evidence opened are cited — the voice guide's
  Damodaran blogspot exemplar is deliberately not cited.
- Every Apple figure is the evidence's re-read primary. FCFF/FCFE Apple dollar
  amounts are intentionally not stated: the evidence verified the SEC OCF−capex
  number only, so the variants section stays qualitative (as the brief directs).
- Go deeper points at the Damodaran primer PDF and the SEC C&DI page. Both are
  also cited sources; they are the natural deeper reading beyond this paper. If
  the editor prefers Go-deeper targets distinct from the source list, that is the
  one easy swap — no evidence beyond what the researcher opened is available for
  it.

## Open questions for the orchestrator
None blocking. Optional: whether Go-deeper rows should avoid overlapping the
source list (see above). The lesson stands for a reader who opens no Background
or Go-deeper link.
