# Draft handoff: company-analysis/super-micro (writer round 02)

## Original work

Unchanged from writer/01: the piece cross-reads five of Super Micro's own
quarterly filings against each other to show the fiscal 2026 fourth-quarter
margin spike sits at the end of a five-quarter decline rather than a stable
base, and that the $9.0 billion gap between net income and operating cash
flow is the same story, quarter by quarter, as the inventory build and the
first-half/second-half accounts-payable reversal, which no single filing
states as one connected argument. Neither fix below touches that synthesis;
they correct where three citations land.

## Fixes applied

1. **DOJ passage citation (blocker).** Fetched both documents directly
   (SEC-compliant User-Agent, both resolve 200). Confirmed Exhibit 99.1
   (a991.htm) carries "not named as a defendant," "a contravention of the
   Company's policies and compliance controls," and "maintains a robust
   compliance program," but contains no resignation language at all -- and
   that Exhibit 99.2 (the March 20 resignation press release) doesn't carry
   the "not the result of a disagreement" phrase either. That exact phrase
   lives only in the 8-K's own Item 5.02 body (smci-20260320.htm): "Mr.
   Liaw's resignation was not the result of a disagreement with the
   Company." Added that document as new source 17 and repointed the
   resignation sentence to it. Source 15 (now renumbered 16, same href,
   a991.htm) keeps the "not a defendant" / "contravention" / "robust
   compliance program" material it actually contains; its list description
   was narrowed to match (it no longer claims to cover the resignation).
2. **Conduct-window citation.** Per researcher/02, Al Jazeera (s14) does not
   state "2024-2025" anywhere on the page; Gizmodo does, verbatim ("between
   2024 and 2025"), attributed to the indictment. Fetched Gizmodo directly to
   confirm it resolves (200) and carries the exact wording. Added it as new
   source 15 (`data-nb-kind="secondary"`) and split the compound sentence so
   the conduct-window clause carries its own citation to s14+s15, while the
   individuals-naming clause that follows keeps s14 (which does name all
   three, matching Al Jazeera's own text) plus the renumbered SEC exhibit
   (now s16).
3. **Chart 1 label consistency.** The bug was double rounding compounded by
   binary-float imprecision: the script formatted the evidence record's
   already-2-decimal figure (9.45) with `f"{v:.1f}%"`, and 9.45 is not exactly
   representable in binary floating point -- it stores fractionally below
   9.45, so Python's default rounding produced "9.4%" against the stat
   strip's and prose's "9.5%". Rewrote the script to hold each quarter's raw
   filed dollar figures (net sales, gross profit) and compute the label from
   the exact fraction via `Decimal` arithmetic, rounded half-up to one
   decimal, rather than from a pre-rounded intermediate. Verified this
   reproduces every other quarter's existing correct label too, including
   Q3 FY26 (9.9451% -> 9.9%, not the 10.0% a naive re-round of the
   pre-rounded 9.95 would give). Re-rendered with `nb chart` and inspected
   the PNG: Q4 FY25 now reads 9.5%, matching the stat strip and prose, and
   the rest of the series is unchanged.

nb-meta `sources` updated from 16 to 18 for the two added sources (Gizmodo,
Item 5.02 body). Word count and reading time were unaffected by `nb stamp`
(2389 words / 10 min, unchanged from round 01) since the citation
restructuring didn't add or remove body prose.

## Proof result

`./nb check --series company-analysis
.nb-work/company-analysis/super-micro/library/company-analysis/super-micro.html
--library /home/user/library-checkout`, links included, after `nb stamp`:
**BLOCK: 0, WARN: 0.** No warnings left intentionally.

## Open question

None blocking. The editor's low-priority research item (confirm source 14's
conduct-window wording) came back resolved by researcher/02: Al Jazeera does
not state a date range at all, which is why the citation was repointed to
Gizmodo rather than left on Al Jazeera with a corrected date. Neither outlet
independently confirms the "2024-2025" window against the DOJ's own document
-- justice.gov remained gated through both research rounds -- so the window
still rests on secondary reporting of the indictment, same as before, just
now attributed to the source that actually states it.
