# Editorial review: investing/free-cash-flow (editor/01)

## Skeptic

Thesis: free cash flow is not a figure you look up but one you construct, so a
reader has to know how it was built before trusting it — and once built from
the cash-flow statement it can move opposite to profit, as Apple's own two
years show. The load-bearing claims:

1. **Headline — "Apple's profit rose while its free cash flow fell."** Recomputed
   against the FY2025 10-K cash-flow statement (R8.htm), every figure re-read
   from the primary, not a summary. Net income rose from 93,736 to 112,010, up
   19.5% ("nearly a fifth" / "about 19 percent" — correct). Free cash flow fell
   from 108,807 to 98,767, down 9.2% ("nearly a tenth" / "about 9 percent" —
   correct). Periods are the fiscal years ended September 27, 2025 and
   September 28, 2024, USD millions, both stated correctly. The headline is the
   direction and magnitude the filing supports, in the right periods, with the
   right denominators. Held.

2. **The worked build: OCF 111,482 − capex 12,715 = FCF 98,767.** Arithmetic
   confirmed and each input confirmed against R8.htm (net income 112,010; D&A
   11,698; SBC 12,863; OCF subtotal 111,482; "Payments for acquisition of PP&E"
   12,715). FY2024 mirror: 118,254 − 9,447 = 108,807, confirmed. The
   intermediate claims also check: capex rose ~3.3B (3,268), capex − D&A =
   1,017, the "other current and non-current liabilities" line swung from
   +15,552 to −11,076 (~$26.6B, printed as "near $27 billion" — fair rounding),
   and the ~$25B working-capital-and-remainder subtraction reconciles OCF to the
   add-backs. Held.

3. **FCF is a constructed non-GAAP measure with no uniform definition.** The SEC
   quote is reproduced verbatim from C&DI Question 102.07 (s1), and the piece
   frames the measure exactly as the guidance does — voluntary, outside GAAP,
   OCF minus capex. Held.

4. **FCFF and FCFE are distinct constructions, not the OCF−capex number.** The
   variants section keeps them cleanly separate: FCFF from after-tax operating
   income, FCFE from net income, neither conflated with the reported-OCF-minus-
   capex figure. Matches Damodaran (s5/s6). No Apple dollar amount is asserted
   for the variants, which is correct — the evidence verified only the SEC
   number. Held.

Display text checked descriptor by descriptor: dek makes a claim about the world
(FCF is self-built and rule-free), not a method grade; "Aswath Damodaran, a
finance professor at NYU" is correct; the filing date (October 31, 2025) and
both fiscal-year-end dates are correct; the table caption's periods are correct.
Every `data-nb-kind="primary"` is defensible — SEC guidance, the IFRS Foundation's
own IAS 7 page, Apple's own filing and its rendered cash-flow statement, and
Damodaran on his own pages. All six citation hrefs open to the source itself and
resolve (SEC pages return 200 with a compliant User-Agent; IAS 7 and both
Damodaran links return 200). The three Background links resolve against the
published `library` branch. IAS 7 carries the three-category structure; no
non-resolving FASB/ASC 230 href is printed, as required. No break found.

## Cut

Two direct cuts, both clear standard violations:

- Removed "The table's second column carries the sharpest point." — a self-grade
  that announced the point's importance instead of making it. The section now
  opens directly on the FY2024 figures, which is stronger.
- Removed "And notice what his reinvestment term does to Apple." — a lecturing
  opener from the banned Note/Consider/Imagine family. The capex-minus-
  depreciation calculation now stands on its own; the reader already holds the
  reinvestment definition from the FCFF formula two paragraphs up.

Prose is otherwise clean. No semicolon chains and no em-dashes in the body (the
raw semicolons are all in the font-URL head). Terms are defined at first use in
one motion with their Apple figures — capex, working-capital change, the D&A and
SBC add-backs, FCFF, FCFE, reinvestment — the voice guide's signature move,
executed. The "not X, you-look-up" contrasts are earned (each corrects a real
misreading the lesson is about), within tolerance. The recent-pattern shapes are
broken: no paradox opener, no colon-definition, no generalizing-takeaway closer,
no paired-heading callback. Furniture earns its place: the two-year bridge table
carries the fall (numbers verified against the primary) and the FCFF/FCFE
equation carries the "different starting lines" reasoning, not decoration. No
prompt leakage — the piece reads as teaching, not as a fulfilled assignment.

Left standing on purpose: "Profit up by nearly a fifth, free cash flow down by
nearly a tenth: the same company, the same two years, two numbers pointing in
opposite directions" is the section's earned climax (its cargo is the framing,
not a restatement), and "So the first thing to know…" / "One honest caveat…" are
teaching transitions, not self-grades worth a rewrite. Editing further would
regress the voice.

## Reader

What the reader gets beyond the sources: the constructed two-year free-cash-flow
bridge that Apple's filing never prints as a line, showing FCF down ~9% while
profit rose ~19%, then decomposed into a heavier capex year and a working-capital
swing — plus the operating test (which construction, and read across years) that
turns the case into a judgment the reader can now make on any company. No single
source hands you that bridge or that decomposition; the draft-handoff's original-
work sentence claims exactly this and the article delivers it. The prose sits on
the voice-guide-exemplar side, not the median-summary side: plain, first-
principles, definition-and-figure in one breath, a teacher at the spreadsheet.
The headline reread as the largest claim holds — subject, verb, surprise in the
first words, actors named, and true.

## Edits

- Cut "The table's second column carries the sharpest point." (self-grade) from the profit-up-cash-down section.
- Cut "And notice what his reinvestment term does to Apple." (lecturing opener) from the which-variant section.
- Ran `nb stamp`: words 2101 → 2084, reading_minutes 9, sources 6.

## Required work

None blocking. One item ruled and closed, not routed:

- Writer's open question (Go-deeper rows overlap the source list): ruled
  acceptable. Both Go-deeper rows point beyond this paper (the Damodaran primer
  and the SEC C&DI page), which is all the furniture requires; the deepest
  further reading legitimately is the primary itself. No change needed.

Writer still owns the final proof run (`nb check … --links`) after these cuts, as
the standing division of labor requires — this is the routine post-edit proof,
not a blocking defect.

## Decision

approve — every Apple figure matches the FY2025 primary, the headline is the
exact ~19% up / ~9% down the filing supports, all hrefs resolve, the lesson gates
and furniture pass, and the two prose tells are cut.
