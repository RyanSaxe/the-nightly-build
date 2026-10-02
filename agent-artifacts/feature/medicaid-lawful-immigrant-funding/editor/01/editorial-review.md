# Editorial review: feature/medicaid-lawful-immigrant-funding (editor/01)

## Correct

The thesis, stated from the draft alone: Section 71109 of P.L. 119-21 ended the
federal Medicaid and CHIP match for a defined set of lawfully present groups on
1 October 2026; it did not cancel coverage; each state now decides whether to
pay for those groups with its own money, and the answers diverge. Four claims
carry it: (1) the statute restricts payment to the state, not eligibility, and
the dropped groups are found by subtraction; (2) CMS will not require states to
fund the dropped groups and does not treat state-only coverage as Medicaid; (3)
the loss falls on non-pregnant adults, because the CHIPRA 214 option keeps the
match for children and pregnant people; (4) "the state decides" spans a statute
cutoff, a lapse, a continuation, and a time-limited continuation, shown with six
states' own documents.

I reopened the three linchpin primary sources and read past the quoted
passages. In the statute (PLAW-119publ21) the new section 1903(v)(5) reads
"Notwithstanding the preceding paragraphs of this subsection, beginning on
October 1, 2026, except as provided in paragraphs (2) and (4), in no event shall
payment be made to a State ... unless such individual is" a citizen/national,
LPR, Cuban/Haitian entrant or COFA migrant. That confirms both the operative
restriction and the paragraph (2)/(4) carve-outs the article leans on, and
section 71110 ("EXPANSION FMAP FOR EMERGENCY MEDICAID") confirms the emergency
cap. In SHO #26-001 every quoted string is verbatim: "will not require states to
provide state-only funded health coverage," "would not consider health coverage
that a state opts to continue to provide with 100 percent state-only funds to be
Medicaid," the "clear Congressional intent" reasoning on p. 7, the 39
states/DC/three territories 214 count, "approximately $1.8B in questionable
expenditures" across "eight states," "separate and distinct contract and
payment," the "may, in fact, experience an overall total increase" on the
emergency cap, Brillman's title, the SPA deadlines (31 December 2026, 30
November 2026), and the "90-day reasonable opportunity period." In CRS R48633 the
summary row for section 71109 reads "Outlays: -$6,211," attributed to Evelyne P.
Baumrucker, effective 1 October 2026.

I tried to break each claim and could not. The hardest one to keep is "the state
decides," because North Carolina shows it is not always a live choice: S.L.
2026-1 wrote the federal floor into G.S. 108A-54.3A(c) effective 1 October, and
S.L. 2026-41 restored only the 214 population. The article already carries this
as a statute-forced cutoff rather than a discretionary one, so the claim holds
in the form the piece states it. The second hardest is "keeps covering," against
CMS's position that state-only coverage is not Medicaid; the article resolves it
by reserving "Medicaid" for federally matched coverage and saying for New Mexico
and California in terms that the continuing coverage is not Medicaid.

Every figure recomputes against its denominator and period. The 1.4 million is
labeled a Georgetown cross-program figure (Medicaid/CHIP, Marketplace, Medicare),
and the article shows the four CBO components summing to it, with 100,000 as the
Medicaid and CHIP piece; it is never presented as a Medicaid count. The 100,000
and $6.2 billion are attributed to CBO through KFF and CRS with their scope and
window. Washington's ~14,000 is marked the state's own eligibility estimate with
no method or reference date. The article states plainly there is no primary
national count. The California figure is given both ways with owners ($364.9M
Department of Finance, $303.1M Assembly floor report) and the documents' failure
to reconcile is stated, not smoothed.

Headline, dek and subheads check against the documents. The headline says
"Federal Medicaid matching ... ended," not "Medicaid ended," and scopes to
non-pregnant adult refugees and asylees. The New York court ruling is attributed
to KFF throughout, with a note that the ruling is not cited and the state's page
does not mention it; it is never asserted. No sentence claims an observed
1-October outcome, and the conclusion says no cited document reports what
happened on the day, giving the latest document's date (22 September 2026) as
the checkable limit.

I audited every `data-nb-kind`. The statute, the CMS letter and press release,
and all six states' notices, statutes, budget documents and plan amendments are
`primary`; KFF (two posts), Georgetown CCF and CRS are `secondary`. All correct.
I opened all 19 printed hrefs: every one resolves to its specific document, none
to a homepage. The CMS letter 403s only to a browser user-agent and serves the
PDF to a plain request, so it is gated, not dead; `nb check --check-links` agrees.

The group-status table does not overreach. It names only the groups the statute
and the letter's own examples support (citizens/nationals, LPRs with the wait,
Cuban/Haitian and COFA migrants, the refugee/asylee/parolee/trafficking example
set, and the 214 children/pregnant row) and claims no row-by-row values for the
other Appendix A categories the writer did not read. Reproducing Appendix A as an
asset would add groups the record does not carry, so I left it out.

## Reads well

One sentence went, the orientation closer, which narrated the article twice
("this article says the state keeps covering these adults, and it uses
'Medicaid' only for coverage that draws the federal match"). That is
self-reference under `spec/slop.md`: the point is a terminology stipulation the
reader needs, but it belongs stated as a fact about the coverage, not as the
article describing its own word choice. I rewrote it to carry the same
distinction without narrating the piece: "So where a state keeps paying, these
adults stay covered, but not by Medicaid, which is the coverage that draws the
federal match." I kept the single term-introduction earlier ("This article calls
it the federal match"), which is a glossary stipulation a lay reader needs once.

Nothing else failed the tests. The edges and the last sentence of every
paragraph and section carry specific, cited content; none survives the
placeholder test as a filled-in pattern. The repeated "cited here" / "the
documents cited here" is a precision device marking the evidence boundary, not a
tic, and one term for one idea is the house preference. The four parallel "In
[state] it is ..." sentences in the conclusion carry the argument rather than a
cadence: each clause states a different instrument (a statute subsection, a
General Fund line with a date, an unnamed-funding program, a court ruling), and
removing the nouns leaves nothing. I checked for borrowed phrasing from the
commission and the voice guide and found none lifted: the "eligibility question
becomes a budget question" framing is the piece's own thesis, stated in its own
words, and no clause is taken from the Howe, Bagley or Frakt passages.

Against recent-patterns.md: the closer is not an "X remains Y rather than Z"
antithesis and not a line built to be quoted; it ends on the piece's own
three-step structure. The dek commits to one concrete claim (three states, three
answers) and is not a suspended qualifier. The headings are each a step in the
piece's nouns, built differently from one another, with no comma-and-"and" or
semicolon two-clause mold. The careful-status work states checkable limits (what
a document does not define, does not date, does not reconcile), not the writer's
own care.

The draft was not running flatter than the guide, so I lifted nothing. The
register already matches the Howe model: cite, quote the operative words, say
what they do.

## The experience

The rendered page reads top to bottom as a documents piece. The two tables earn
their place: the group table shows the match status faster than prose could, and
the six-state table holds the grid so the prose can spend itself on the
reasoning, which is what the voice guide asks. No chart is warranted, because no
verified series shares a unit or scope, and the article builds none. No captured
asset was needed; the quoted strings do the work Appendix A would.

What the piece gives beyond its sources: it separates the three things the
coverage runs together, the statute, the guidance, and the coverage outcome, and
then shows with six states' own documents exactly where an eligibility question
becomes a state budget question, in four different instruments, while refusing
the national count no primary source supports. That matches the writer's
original-work sentence. The sources alone, read separately, do not do this.

## Edits

- Orientation, final paragraph: replaced "this article says the state keeps
  covering these adults, and it uses 'Medicaid' only for coverage that draws the
  federal match" with "these adults stay covered, but not by Medicaid, which is
  the coverage that draws the federal match" (cut self-reference; kept the
  terminology stipulation as a statement about the coverage).

## Decision

approve. It is correct against the primary record, holds the federal-match /
coverage distinction precisely throughout, and does original work the sources do
not; the single slop edit is made and the proof returns BLOCK: 0, PUBLISHABLE.
