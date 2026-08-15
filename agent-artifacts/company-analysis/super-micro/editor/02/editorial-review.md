# Editorial review: company-analysis/super-micro (editor/02)

This is a confirmation read after the three-fix repair (writer/02, with
researcher/02 supplying the conduct-window source). It verifies only what
changed and that nothing settled in editor/01 regressed. It does not reopen the
arithmetic, the cash-conversion spine, the slop passes, or the reader read,
which held in editor/01 and are untouched by these fixes. The sensitive DOJ
passage is held to exactly the standard editor/01 set, no more.

## Skeptic

The three repaired items, checked at their sources.

1. DOJ citation split. The resignation clause now reads "a departure the company
   stated was 'not the result of a disagreement with the Company'" and cites
   source 17, the 8-K's Item 5.02 body (smci-20260320.htm). I opened that href as
   printed: it returns 200 and carries the sentence verbatim -- "Mr. Liaw's
   resignation was not the result of a disagreement with the Company." The clause
   lands on the document that owns it. Source 16 (Exhibit 99.1, a991.htm,
   renumbered from the old 15) I opened as printed: it carries "not named as a
   defendant," "a contravention of the Company's policies and compliance
   controls," and "maintains a robust compliance program," and it does not carry
   the resignation phrase. Its list description was narrowed to match; it is now
   cited only for what it contains. The landing failure editor/01 found is
   resolved, and no new one was introduced by the renumber.

   The sensitive passage as a whole still meets the standard. The charges are
   attributed to the three named individuals (Liaw, Chang, Sun); the piece states
   Super Micro was not named as a defendant; the company's victim statement is
   present ("a victim of the scheme itself," source 18); and the closing
   disclaimer still ties nothing in the export-control matter to the reported
   revenue, inventory, or margin figures. Attribution, victim statement, and
   firewall all intact.

2. Conduct-window citation. The "between 2024 and 2025" clause now carries source
   14 (Al Jazeera) and source 15 (Gizmodo, secondary, newly added). I opened
   Gizmodo as printed: it returns 200 and states "the Southeast Asian company
   allegedly purchased roughly $2.5 billion worth of servers between 2024 and
   2025" verbatim, names all three individuals, and reports Super Micro was not
   named as a defendant. The date wording is now owned by a source that actually
   prints it, which was the defect editor/01 flagged and researcher/02 confirmed
   (Al Jazeera is silent on the range). The sentence reads as the charge an
   unsealed indictment makes, reported by two secondary outlets -- "unsealed an
   indictment charging three people with conspiring to route..." It is not
   overstated into fact and does not claim primary confirmation; justice.gov
   stayed gated through both research rounds, and the claim rests on secondary
   reporting, which the framing matches.

3. Chart 1 label. The Q4 FY25 point now reads 9.5%, matching the stat strip and
   the orientation prose. I re-read the PNG: the eight labels are 13.1, 11.8, 9.6,
   9.5, 9.3, 6.3, 9.9, 17.5, and the whole series is otherwise unchanged from the
   verified evidence-record values. I checked the re-rendered provenance
   (chart-1.py): it now holds each quarter's filed net-sales and gross-profit
   dollars and computes the label from the exact fraction with Decimal, rounded
   half-up to one decimal, rather than re-rounding a pre-rounded 2-decimal figure.
   Q4 FY25 is 544,102 / 5,756,911 = 9.4514%, which rounds to 9.5%; the earlier
   9.4% was the double-rounding-plus-float artifact the writer describes. The fix
   is at root, not a hand-patched label, and it reproduces every other quarter's
   correct label (e.g. Q3 FY26 9.9451% -> 9.9%).

Sources count. nb-meta now reads 18, and the list carries s1-s18. The two added
entries (Gizmodo, Item 5.02 body) are accounted for.

## Cut

No new cut pass this round; the slop, edge, delete-test, leakage, and
recent-pattern reads were completed in editor/01 and are not reopened. The
citation restructuring added no body prose (word count held at 2389), so there
was no new prose to test. My three editor/01 direct edits all remain in the
current article: the replacement outlier line ("A single quarter above a range
the business held for two years does not by itself establish a new level"), the
cut of the nb-note's "Treat it as reported, not filed," and the semicolon-to-
period repair before "A full-text search." None regressed.

## Reader

Unchanged and not reopened. The synthesis editor/01 confirmed -- the headline
margin jump and the 78% revenue growth did not become cash, and 17.5% is one
mix-driven quarter at the end of a two-year decline -- is not touched by three
citation-and-label fixes. The repairs strengthen the reader's footing on the one
passage most likely to be clicked through, since the resignation and
conduct-window claims now land on documents that carry them.

## Edits

- None. This round required no direct edits; all three fixes belong to the writer
  (citations, chart provenance) and were verified as applied, not authored here.

## Required work

- None blocking. The proof passes (`./nb check`, links included: BLOCK 0, WARN 0,
  PUBLISHABLE). The researcher item from editor/01 (source 14 conduct window) is
  resolved by researcher/02 and the citation repointed. Any residual is the
  orchestrator's normal stamp before the PR.

## Decision

Approve. The three fixes hold at their sources: the resignation clause and the
Exhibit 99.1 quotes each land on the document that owns them, the "2024-2025"
window now cites a source that prints it and reads as secondary reporting of the
indictment, and the Q4 FY25 chart label reads 9.5% from a root-cause provenance
fix. The sensitive DOJ passage keeps its attribution, victim statement, and
firewall; my editor/01 edits stand; the gate is met and no buy/sell/allocation
call appears.
