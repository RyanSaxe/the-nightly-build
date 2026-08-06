# Editorial review: parenting-research/teething (editor/01)

## Skeptic

Thesis: teething itself is a mild, mostly local event, so the harm worth a
household's attention lives in the remedies, two of which the FDA had to act
against. The headline states that inversion plainly and the piece earns it.

Load-bearing claims and how each held:

1. **Teething is tied to a small temperature rise, never a true or high fever.**
   This is the gate claim and it is stated precisely: the piece never writes
   "teething causes no fever." It says a tooth can "nudge a baby's temperature a
   fraction of a degree" and "a true fever is not something a tooth does." The
   contrary evidence is steelmanned, not buried. Ramos-Jorge's day-of-eruption
   rise (P = .004, max 36.8 C tympanic, inside normal range) and Nemezio's
   rectal-subgroup association are both given, then weighed. I recomputed the
   figures against the evidence record: Nemezio overall OR 1.32 (95% CI
   0.88-1.96) and rectal-subgroup OR 2.82 (95% CI 1.55-5.14) match exactly, as
   do Ramos-Jorge's P value and 36.8 C maximum. The article's caveat is also
   logically correct: it attributes "still crosses one" to the *overall*
   estimate (whose CI does include 1) and "rests on a handful of studies" to the
   rectal subgroup (which the authors flag for few studies). The two caveats are
   not conflated. Claim survives.

2. **Ramos-Jorge's diarrhea/rash association is the internal contradiction, and
   the better-powered work wins.** The piece names it openly rather than hiding
   the disagreement, and resolves toward Macknin and the AAP without claiming
   unanimity. Matches the evidence record's Contradictions section. Holds.

3. **Effect sizes are real and small.** Macknin's "no symptom in more than 35%
   of teething infants; none more than 20% more often than non-teething days" is
   reported accurately, and the base-rate reasoning (a tooth is "in window" most
   days, so drool predicts almost nothing) is the piece's strongest original
   move. Holds.

4. **Benzocaine: 119 methemoglobinemia cases, four deaths (incl. a four-month-old
   teething infant), 116 serious, no demonstrated benefit (FDA, May 23 2018).**
   Every figure matches the FDA letter as recorded in evidence. Used firmly, with
   the mechanism named. Holds; this is the piece's one hard imperative ("Do not
   put benzocaine on a teething baby's gums"), correctly the loudest sentence.

5. **Belladonna: Class I requested recall, "serious health hazard," "no known
   safe or toxic dose in children."** Rests only on the two FDA letters and the
   FDA-hosted recall page that were actually opened. Confirmed: NO ~99-FAERS /
   infant-death / seizure body count appears, and NO non-resolving FDA URL is
   cited (the discarded 404 press-announcement and lab-analysis pages are absent
   from the source list). The report is firm through the FDA record, with no
   imperative, which is the correct calibration for a hazard carried by the
   regulator's own action.

**Display-text audit (descriptor by descriptor).** Headline is a defended claim,
not a colon template or Betteridge question. Dek adds specifics without restating
the headline and is not a comma-triad or hedged-contrast mold; its two numbers
(119 cases, four deaths) and "serious health hazard" all check against the FDA
letters. Every subhead is a concrete argument step in the piece's own nouns; a
reader skimming only headings reconstructs the argument. No quantity, name, date,
or role in display text is wrong.

**data-nb-kind audit.** All nine are `primary` and each is defensible: Macknin,
Massignan, Ramos-Jorge, Nemezio own their studies; the three FDA documents and
the FDA consumer page are agency-authored; s9 is the company recall announcement
FDA hosts, cited for the recall fact and FDA's quoted determination, which the
page owns. No secondary is mislabeled as primary, and no independent-source gap
is hidden behind a label.

**Citation href audit (opened every href as printed).** s1 (FDA consumer), s3
(AAP HealthyChildren), s5 (Ramos-Jorge PubMed), s6 (Nemezio PubMed), s9 (FDA
recall page) return 200 and land on the correct source with matching content. s7
and s8 return 200 and download the correct FDA PDFs (benzocaine letter metadata
confirmed "FDA Letter Regarding Benzocaine," May 2018; recall letter is
media/104395), content primary-verified in the evidence record. s2 and s4 (both
publications.aap.org) return 403 to automated clients — a WAF/bot block on the
Silverchair journal platform, not a dead link: these are the canonical
DOI-backed Pediatrics article pages, they resolve for a human clicking them, the
paper's own link check passed all nine, and PubMed independently confirms both as
the correct articles. Not a broken-link failure; recorded here for transparency,
not blocking.

## Cut

The piece is already lean and disciplined; the register holds the voice guide's
calibration (deflation flat, comfort measures dull, benzocaine loud). Four
surgical fixes:

- Cut a method signpost: "and the disagreement is worth spending rather than
  smoothing." The following two paragraphs *do* the spending; telling the reader
  the method in advance is the self-referential move the editorial direction
  bans. The section now opens on the clean claim.
- Cut a self-grading tag: ", which is the point." "The measures that carry no
  such record are dull by comparison" already carries the calibration argument;
  "which is the point" grades the sentence's own stakes, the "that's the whole
  point" family the direction names.
- Two reflex semicolons repaired to the plainer period ("both reject; on the
  systemic..." and "not the freezer; frozen..."). In both, a period reads
  cleanly and does not over-separate, so under the punctuation standard the
  period wins.

Worst tell found: the "worth spending rather than smoothing" signpost, mild and
now gone. No repeated rhetorical shape against the recent-pattern notes: the
piece opens on the coincidence mechanism (not a trial bottom line), the dek
avoids the hedged-contrast and comma-triad molds, there is no nb-position "where
X and Y part ways" section, and the closer is not a "back to the [object]" line.
Furniture earns its place: the symptom-attribution table renders Macknin's own
associated/not-associated split (verified row by row against the evidence), the
six-event timeline carries the belladonna regulatory sequence with a citation on
every event, and the "Not teething" note concentrates the red-flag list. None is
decorative; none is a formula.

## Reader

Read straight through as the declared reader (a data-literate parent at the
crib): what the piece gives beyond its sources is a single decision rule none of
the sources assembles. It fuses attribution bias, Macknin's base rate, the
steelmanned fever disagreement resolved to "small rise, not fever," and the FDA
drug-safety record into one household default (cold and pressure, skip the
cabinet) plus a named "not teething, call the pediatrician" list. The
draft-handoff's original-work sentence claims exactly that fusion, and it
survives: Macknin, Nemezio, and the FDA letters each do one part; only the
article does all four toward a decision. The prose sits with the voice-guide
exemplars, not a median summary: hazard separated from magnitude (Spiegelhalter),
the effect-size deflation carried by a base rate (Oster), firmness tuned to
documented harm (Carroll). The headline reads true as the largest claim.

## Edits

- the-thermometer: removed the method signpost "and the disagreement is worth spending rather than smoothing."
- the-thermometer: changed the semicolon in "both reject; on the systemic signs..." to a period.
- remedies-fda-moved-against: removed the self-grading ", which is the point."
- remedies-fda-moved-against: changed the semicolon in "not the freezer; frozen..." to a period.
- Ran `nb stamp`: words 1731 -> 1718, reading_minutes 8 -> 7, sources 9 (unchanged).

## Required work

None blocking.

- Optional (writer, non-blocking): if the paper's link policy prefers citation
  hrefs that resolve for automated checkers as well as humans, s2 and s4 could
  point at the PubMed or DOI records instead of the publications.aap.org landing
  pages. Not required: the current URLs are the canonical primary pages, they
  load for a human reader, and the proof passed them. Do not route this back
  unless the orchestrator wants the platform swap.
- Note (researcher, only if reopened): the belladonna body count remains
  deliberately absent. The piece does not need it, and it must not be added
  without a new researcher artifact sourcing the counts to an openable primary or
  attributed secondary. No action requested this round.

## Decision

approve — the health/safety precision gate is met on every point (fever stated
as a small rise not a true fever with the contrary evidence steelmanned and the
CIs/ORs verified, belladonna resting only on opened FDA documents with no 404 and
no unverified body count, benzocaine firm and exact, no printed acetaminophen
dose, calibrated firmness, and the red-flag close intact), citations resolve to
the correct sources, furniture is honest evidence, and the four remaining prose
tells were cut directly.
