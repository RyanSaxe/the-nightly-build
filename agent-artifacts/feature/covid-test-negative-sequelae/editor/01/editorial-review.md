# Editorial review: feature/covid-test-negative-sequelae (editor/01)

## Correct

Thesis, from the draft alone: run on the same claims, the PNAS paper's
unrestricted design attributes hundreds of later outcomes to COVID-19 and its
test-based design attributes almost none, and the placebo and negative-control
results put most of the unrestricted count on the comparison group. Claims
under it: (1) the counts are 262/286/369 against 43/5/0, and the designs differ
in cases and enrollment date as well as controls; (2) the unrestricted design
measures contact with care, shown by the cerebral palsy pre-trend, the visit
gap, the placebo run and 53.1% of negative controls flagged; (3) test-negative
controls bias toward the null, through collider bias and later infection;
(4) the replica's failure does not transfer to the VA papers, which passed
their own negative controls, and test-anchored designs still find later
effects.

All four held against the paper (PMC full text, reread past the quoted
passages), CIDRAP 2023 and 2026, and the EurekAlert! copy of the Stanford
release. Every figure matches its owner and window. Breaks and fixes:

- Headline (focus 1). "Enrolling everyone at a PCR test" is defensible: the
  paper names the design by that rule ("Enrolling all participants at the time
  of their first PCR test"), CIDRAP describes it the same way, and the rule is
  what restricts the cases and controls to tested people. The first section
  states all three differences. The break was "long COVID's second-year
  outcomes", which calls the 369 long COVID's own outcomes when the piece
  argues most are not. Now "the second-year outcomes attributed to COVID".
- RECOVER's "Toward the null" (focus 2). Nothing in the record measures it, and
  the PNAS Discussion argues the opposite way about RECOVER: per-protocol
  testing of symptom-free volunteers is "less subject to test-seeking
  selection". Replaced with "Not measured; volunteers tested per protocol"
  (s1, in the caption). The VA row's "Up from care-seeking" is PNAS's argument,
  not a VA finding, and now says "per PNAS". Maccabi's "Toward the null" stays:
  its controls are defined by negative tests, which Ayoubkhani's statement
  covers by its own wording.
- Uncited statements (focus 3). "Nobody has rerun the VA data with a test-based
  design" had no source and is cut; the paragraph already says the replica is
  not the VA data. "No researcher outside the team has commented publicly yet"
  stays: it is a dated absence, and CIDRAP's 9 November report, which I read,
  quotes only the authors. Moved ahead of the authors' quote so the piece ends
  on its conclusion. A third uncited absence, "Nobody has measured by how
  much", became "give no figure for how much", which is checkable against the
  paper.
- "Concedes the point and measures it" overstated the paper: it reports two
  signs of the bias (2 of 49, the 20.2% curve), not its size. Now "concedes the
  mechanism".
- "The test-based design also misses ... fatigue or cognitive symptoms":
  uncoded symptoms are a limit of claims, not of one design. Recast, with the
  1.1 threshold cited to s1.
- "Flags half its negative controls" now gives the figure, 53.1%.
- Dek: "almost as harmed ... against the broader design's comparison group"
  left "broader design" undefined for a link reader and did not say the match
  holds in the first window only (placebo 54.8% against 85.0% in year two).
  Rewritten with the window and the comparison group named.
- s2's href pointed at `#supplementary-material`, which is not an id on the PMC
  page; the block is `#supplementary-material1`. Fixed. The PDF itself sits
  behind a bot challenge, so the anchor is the stable landing.
- s4 (Ayoubkhani) was marked secondary. It is cited only for its own
  methodological argument, which it owns, so it is primary for that claim.
  No independence is claimed from it either way.

Links opened as printed: PMC, both CIDRAP pages, eClinicalMedicine DOI,
Nature 2021, Nature Medicine DOI, EurekAlert! all land on the source. The BMJ
and JAMA DOIs resolve to the correct publisher article pages and return 403 to
a script, which is a bot block, not a wrong address. Al-Aly's two quotes match
CIDRAP word for word.

## Reads well

- "They do." after the placebo prediction reproduced the Data Colada "And they
  do." beat from the voice guide. The point is the article's own, so I rewrote
  the answer in its words: within 0.2 percentage points over days 30 to 119.
- "That does not carry over to the VA papers by arithmetic" was a vague verdict;
  now "That result belongs to the replica", followed by the design difference.
- "Adult cerebral palsy is a condition COVID-19 cannot cause" reordered to lead
  with the claim; "filed" claims corrected to "had" (providers file them).
- "Diagnoses" became "outcomes" so one word names one idea throughout.
- The 40-word Maccabi/middle-window sentence split in two.
- The semicolon in the no-comment sentence became a period.

Against the recent record: no "By X's arithmetic" dek, the headline is a
positive finding and not "X did not Y", the first heading does not narrate
setup, no heading is a triad, and the close is a conclusion, not a "what X can
rule out" section. The edges otherwise passed the placeholder test; the last
sentence states a checkable rule the piece derived, and stays.

## The experience

The page leads with the counts chart, then a drawn comparison of who sits in
each group, then the contamination strip and the design table, which is the
order the argument needs. I changed no figure; the edited table and header were
captured at 390px light and 1280px dark with no horizontal page scroll and no
overlap. Fig. 2's caption already says it shows SI shares without a
significance filter.

What it gives beyond its sources: it lines up the paper's two designs, its
placebo run and the VA, Maccabi and RECOVER studies by which way each
comparison group pushes the estimate, and uses negative controls to separate
what the claims establish from what they do not. That matches the writer's
original-work sentence.

## Edits

- Headline (title, meta, h1): "long COVID's second-year outcomes" to "the second-year outcomes attributed to COVID".
- Dek rewritten to name the comparison group and the first-four-months window.
- Orientation: "614 diagnoses" to "614 outcomes".
- Cerebral palsy sentence reordered; "filed" to "had".
- "They do." replaced with the 0.2-percentage-point result over days 30 to 119.
- "concedes the point and measures it" to "concedes the mechanism".
- Threshold and uncoded-symptom sentence recast and cited to s1 and s6; "Nobody has measured by how much" to "give no figure for how much".
- Table, VA row: added "per PNAS" to the care-seeking direction.
- Table, RECOVER row: "Toward the null" to "Not measured; volunteers tested per protocol".
- "flags half" to "flags 53.1% of".
- "That does not carry over ... by arithmetic" replaced; replica and VA entry requirements merged into one sentence.
- Cut "Nobody has rerun the VA data with a test-based design."
- Maccabi and middle-window sentence split in two.
- No-comment sentence moved ahead of the authors' quote; semicolon removed.
- s2 href fragment to `#supplementary-material1`.
- s4 data-nb-kind secondary to primary.
- Restamped: 1189 words, 10 sources, 5 minutes.

## Decision

approve: every required change was made directly, and the proof passes with
no blocks or warnings at 1189 words.
