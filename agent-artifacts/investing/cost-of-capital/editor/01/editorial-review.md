# Editorial review: investing/cost-of-capital (editor/01)

## Skeptic

Thesis: cost of capital is the opportunity-cost hurdle a company's return on
invested capital must beat; it is built from an after-tax cost of debt and an
*estimated* (not observed) cost of equity, blended by market-value weights into
WACC, and it differs sharply by business, so the same ROIC means different
things depending on what financed it. The four load-bearing claims are (1) the
after-tax mechanic of debt, (2) cost of equity as a required return that cannot
be observed, only estimated, (3) WACC as the market-value-weighted blend, and
(4) the value-creation test (ROIC above cost of capital) generalizing beyond
any one company.

Every number reconciles with the evidence record and the two figures compute:

- Utility WACC: 5.02% x 0.5510 + 3.55% x 0.4490 = 4.36%. Semiconductor WACC:
  10.72% x 0.9747 + 3.97% x 0.0253 = 10.55%. Both match the table and the
  claimed "more than double" (10.55 / 4.36 = 2.4x). Cost-of-equity, after-tax
  cost-of-debt, and equity-weight cells all match the evidence record's fetched
  figures.
- Intel FY2025: $14.6B gross capex (additions to PP&E), full-year net loss
  ($(0.06) EPS), $46.6B debt ($2,499M + $44,086M) all match the primary. The
  review-brief's central instruction holds: the anomalous 98.3% effective tax
  rate is **not** used anywhere. The after-tax-cost-of-debt step uses an
  explicit hypothetical ("Say you can borrow today at 6 percent... 25 percent"),
  correctly labeled as an assumption, so no false precision is imported.
- The as-of caveat the evidence demanded is present twice: the cost-of-debt
  mention and the table caption both state "fetched August 2, 2026" and warn a
  later reader sees different numbers. Publication date is the same day, so no
  drift.
- CAPM is described correctly (required return = risk-free + beta x the market
  premium). The Fama-French verdict, the 8.3% premium with a 3.5-13.1% two-SE
  range, and the "seductive simplicity... probably invalidate its use" quote all
  match the source. The FERC four-model episode and the Hope Natural Gas quote
  (320 U.S. 591, 603) match verbatim. The intellectual-honesty spine the brief
  asked me to confirm holds: cost of equity is presented as estimated, backed by
  Fama-French's self-indictment and FERC's live non-convergence, and closed on
  the Hope opportunity-cost standard.

Display text: headline figures are true and the actors named. Section subheads
are all argument steps, each a defensible claim. `data-nb-kind` audit: all
eleven sources are marked primary and each is defensible per the evidence record
(company filing, statute, agency order, court opinion, the authors' own papers,
Damodaran's own dataset, McKinsey's own framework/study). No secondary mislabeled
as primary; no hidden missing independent source. Recent-pattern check passed:
no Costco default in the body (the Costco title appears only as a Background link
to the prior lesson), AEP absent from headline and dek, headings and dek avoid
the banned molds.

Two skeptic findings routed to the writer (below), both in display/quoted text:
the dek's "that gap" and one altered word inside the book-value quotation. One
break I could not fix by cut because it needs the meta synced; the other is a
quotation-accuracy fix.

## Cut

Nine surgical cuts made (all pure deletion or period-for-semicolon repair; no
new prose):

- Self-reference: removed "whose framework anchors most of what follows" from
  the Damodaran introduction ("what follows" is the flagged self-narration
  pattern).
- Self-grading in the Why-this-matters bookend: removed "It is also honest about
  what that hurdle cannot do:" so the sentence states the claim directly rather
  than praising the lesson's own candor. This was also the clearest echo of the
  writer brief's "be honest that cost of equity is estimated" instruction, i.e.
  a mild prompt-leak tell.
- Redundancy: trimmed "despite everything else about the two industries pricing
  differently" (the paragraph opener already established the contrast).
- Repeated formula: the WACC-section close repeated the orientation's "let alone
  ... its lenders and shareholders were actually charging it" almost verbatim.
  Cut the trailing clause so the section ends on the sharper beat, "a return
  that did not clear zero."
- Punctuation: converted six independent-clause semicolons to periods
  (the 163(j) cap sentence, the worked-example "not 6 percent" line, the
  debt-vs-equity contract sentence, the FERC "true one" line, the
  utility-vs-semiconductor financing sentence, and the table caption). The
  editorial direction makes the period the default and the semicolon rare; six
  in one piece is not rare, and each reads cleanly as two sentences.

Worst tell found: the self-grading "It is also honest about what that hurdle
cannot do" in the opener, which doubled as prompt leakage. The one repeated
shape ("let alone ... charging it") was broken by cutting the second instance.
Furniture is all load-bearing (the WACC equation, the two-industry table, the
Hope blockquote); nothing survives on habit and nothing obvious is missing.

## Reader

Read straight through as the paper's declared reader (numerate, well-read, new
to this subject): the piece gives an argument the sources do not. Damodaran
defines the term, Fama-French indict CAPM, FERC shows the estimate failing to
converge, and McKinsey quantifies the spread; none of them, alone, says "the
hurdle is estimated, differs by financing, and the size of the gap is what
tracks value creation." The draft welds them into that one throughline and
anchors it in a concrete failing company (Intel) plus population-level data
(McKinsey's firm-size spread), which is exactly what the original-work sentence
claims and what the voice guide's population-evidence license asks for. The
prose sits closer to the exemplars than to a median summary: it opens on the
cost of a wrong hurdle, converges on the definition from three real questions,
uses the second-person walkthrough once inside the worked case as licensed, and
is candid about the method's limits. The headline, reread as the largest claim,
holds.

## Edits

- Removed ", whose framework anchors most of what follows" from the Damodaran introduction (orientation).
- Removed "It is also honest about what that hurdle cannot do:" and recapitalized "Cost of equity is estimated..." (Why this matters bookend).
- Trimmed "close together despite everything else about the two industries pricing differently" to "close together" (cost-of-debt).
- Cut ", let alone whatever its lenders and shareholders were actually charging it for the capital" so the WACC section ends on "did not clear zero."
- Semicolon to period: "highly indebted company; most large" (cost-of-debt).
- Semicolon to period: "is not 6 percent; it is" (cost-of-debt worked example).
- Semicolon to period: "Equity has no such contract; a shareholder" (cost-of-equity).
- Semicolon to period: "pick the \"true\" one; it was to average them" (cost-of-equity, FERC).
- Semicolon to period: "cheap debt; semiconductor companies" (WACC).
- Semicolon to period: "fetched August 2, 2026; a later reader" (table caption).
- Ran `nb stamp`: words 2190 -> 2150, reading_minutes 10 -> 9, sources 11 (unchanged); still inside the 1200-2200 band.

## Required work

- **writer** - Dek fix. The dek reads "Cost of capital sets that gap, the hurdle
  a company's return on invested capital has to beat...". "That gap" has no
  antecedent for a front-page reader (a dek must stand alone), and the nearest
  available referent is the headline's chipmaker-vs-utility difference, which is
  the wrong thing: the hurdle is each firm's own cost of capital, not the gap
  between two industries'. Minimal fix is to delete "that gap, " so it reads
  "Cost of capital sets the hurdle a company's return on invested capital has to
  beat for growth to create value instead of destroying it." This must be
  applied in **both** the visible `nb-dekline` (line ~41) and the `nb-meta`
  `dek` string (line 29) so they stay in sync. I did not touch it myself because
  the meta is a script block outside my prose remit.
- **writer** - Quotation accuracy. The book-value quote reads "...but comes with
  problems that can be insurmountable"; Damodaran's text is "...but come with
  problems that can be insurmountable" (subject "Book value weights", plural).
  Either bracket the inflection ("but [come] with problems") or restructure the
  lead-in so the quotation is exact. Minor, but it is an altered word inside
  quotation marks.
- **writer** - Run the full proof (`nb check ... --series investing`) after the
  two fixes above to confirm links, banned terms, dek match, and counts pass.
  My cuts were deletions and punctuation only, so no new-prose proof is owed
  beyond the two named fixes.

## Decision

revise - the article is sound and I approved its substance after direct cuts,
but the dek carries a standalone-antecedent conflation in the paper's second
most-read line and needs a writer fix synced to the meta, plus one minor
quotation correction; no new prose is owed beyond those two items.
