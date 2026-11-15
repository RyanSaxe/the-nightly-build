# Editorial review: feature/us-measles-elimination-lost (editor/01)

## Correct

Thesis, from the draft alone: the one transmission chain the public record shows
running past 12 months is Utah's, from June 2025. The West Texas origin that most
coverage assumes rests on ProPublica's reading of genomes, which federal officials
disputed and the Texas laboratory left open. The claims under it:

1. PAHO's test is one chain of the same genotype and lineage running 12 months.
   It held against the 2 March 2026 release. The draft said PAHO revokes status
   "on one finding", while PAHO's 14 October notice says no single source of
   evidence determines a classification. The section 3 sentence quoting that
   notice read as a contradiction of the opener. I recast the opener as the
   condition for losing status and kept the notice's line.
2. Utah's outbreak dates from June 2025 and passed 12 months in June 2026. It held
   against the Utah HAN 06202025 (summary, p. 1), the Utah response page (725, 528,
   one in three weeks, updated 10 November) and Brewer in STAT ("apparently has
   gone on for more than 12 months, the main criterion for loss of elimination").
   One break: the preprint abstract finds several introductions into Utah, one of
   them accounting for most cases, and CNN says the dominant strain moved from
   southwest to central Utah. The 19 June case was in Utah County. So the record
   does not show that this case started the chain that crossed 12 months. The
   section heading "Utah's clock starts on 19 June 2025" and the dek's "runs from
   one unexplained Utah case" both claimed it did. I retitled the heading to the
   month Brewer gives, added the abstract's finding on introductions, and
   rewrote the dek. That narrows the claim to what the record supports. It does
   not hide a gap: the gap is now stated in the piece. The commission's framing
   of the Utah outbreak as dating from 19 June still stands. The HAN date is the
   outbreak's earliest public record, and the piece keeps it as that.
3. The Texas-to-Utah link is genomic, made public by ProPublica and disputed.
   It held against ProPublica (nearly 16,000 letters, 12 differing, five shared
   by May 2025, the four states, the CDC spokesperson's words), NBC (O'Neill),
   AP via PBS (HHS: no evidence of a single year-long chain) and EID 32(10)
   ("heterogeneous phylogenetic placement", "prevented definitive inference").
   The draft's "it is ProPublica's, not a health department's" was an antithesis,
   and the record also holds a reported CDC call that linked the strains. I
   narrowed it to "the published case ... is genomic, and it is ProPublica's".
4. The CDC report is confidential and its chain is not public. It held. The
   draft said a source "told Reuters". The Reuters copy relays the Journal and
   does not say which outlet the source spoke to, so it now reads "Reuters
   quotes a source familiar with the CDC's findings".

Further breaks and fixes:

- "PAHO has published nothing: its news index carries no measles item after 14
  October." Page 1 of the index runs only 9 to 13 November, and PAHO published
  Situation Report 15 on 6 November. Narrowed to "announced no decision" plus
  what page 1 shows.
- "For the United States that window opened on 20 January 2025, the first known
  rash onset in West Texas" was cited only to PAHO, which says "onset of the
  reported outbreaks". Adding AP put source 17 ahead of source 2 and broke the
  numbering rule, so the sentence now says what PAHO's release says.
- "Those totals are why the review happened" had no source. PAHO's review is
  annual and keyed to outbreak onset. Cut.
- "Joint investigation" in Fig. 2, its alt text and the table rested on the
  August Utah HAN, which the article does not cite. The cited Mohave release says
  the outbreak was "connected to Arizona-Utah border communities". Labels now say
  that.
- The Fig. 2 caption's "the four outbreaks under review" said the commission
  reviewed exactly these four. No source says so. Changed to "Four outbreaks".
- The table caption cited no source for "crossed 12 months" or for the Arizona
  link. Brewer (s10) and Mohave (s13) were added.

Headline, dek and subheads: dates, counts, roles and places all checked against
their owning documents. Every printed href was opened: 18 returned the page
directly, and the three that refuse curl (CDC data page, CDC Stacks, Utah response
page) load in a browser with the cited figures visible. `data-nb-kind` audit: the
secondaries are Reuters, CNN, KFF, ProPublica, NBC and AP. Reuters and CNN are
read through republishers, which are credited to the original authors and not
counted as independent. Brewer's STAT piece is primary for his committee's role
and his own judgment, and the piece cites it for nothing else. The kinds are
correct.

## Reads well

Cut because it said nothing:
- "West Texas is where most accounts start." With placeholders it reads "X is
  where most accounts start". It is also a vague attribution.
- "...the condition the 12-month test exists to catch." A trailing appositive
  that grades the sentence before it. What remains, "has recorded transmission
  nobody saw", is Branswell's move and stands alone.
- "A CDC spokesperson gave ProPublica the limit" became "told ProPublica".
  "The limit" announced the quote's job.

Cut for repeating material in the piece: the list of what the commission weighs
(coverage, surveillance, laboratory) in section 3, and Utah's three-week count in
section 2, which now appears once, in the close.

Moved: Fig. 1's caption read "the 1,274 of 2019 did not end elimination", which
is interpretation. The caption is now a cited label. The point moved into prose,
in place of the cut "totals" sentences.

Recent record: the draft dek was a two-clause ", and" sentence opening on the
same PAHO status as the body, with the dangling referent "the decision". The new
dek opens on a participle and adds the Texas dispute that the headline leaves
out. The headline does not open on a number or a named organization. The body
opens on PAHO's test, not on a figure. Neither banned dek mold appears. Nothing
from the voice guide's quoted passages surfaced in the prose.

Flat spot: the close ("Utah's is the outbreak that has to go that long without a
case, and no public document says what started it") claimed Utah's is the chain
PAHO acted on, which the section above it says is not public. It also ended on
a gesture. The close now ends on PAHO's own delay-adjusted national reproduction
number, 1.49 (credible interval 1.42 to 1.57), with transmission highest in
northeastern states. That gives what the reverse clock faces, from the document
that owns it.

## The experience

Situation Report 15 earns its place back in the close. It is primary, it was
opened and checked (footnote 6, p. 8; p. 5), and it is the only figure in the
piece about whether the US can start the 12 months back. Its bullet on
coordinating messaging about the commission's conclusions stayed out because
the band had no room.

The table was the weak spot on a phone. At 390px only "Chain" and "Dates" showed,
and "What joins it", the column that grades each link, sat off-screen with no
cue to scroll. The dates already appear in Fig. 2. Each date now opens its text
cell and the row labels are shorter, so the table fits a phone (349 of 348px)
without horizontal scrolling. Fig. 1, Fig. 2 and Fig. 3 were rechecked at 390
and 1280px in both themes after the label change: no collisions, no console
errors, no horizontal page scroll.

What the piece gives beyond its sources: it puts the four health departments'
dates on one timeline and grades each link by who made it (a state laboratory, a
border health department, or a newsroom's genomic inference). No single source
does that, because the CDC's report is confidential and each public document
covers one outbreak. That matches the handoff's original-work sentence. The
headline, read last as the largest claim, is defensible as worded. It says Utah's
is the chain that ran a year, which the record shows, and not that PAHO acted on
Utah's.

## Edits

- Dek rewritten in the body and in nb-meta.
- Opener recast as the condition for losing status.
- 20 January sentence attributed to PAHO's own wording.
- "Published nothing" narrowed to "announced no decision" and what the news index shows.
- "Totals" sentences replaced with the 2019 point. Fig. 1 caption reduced to a label.
- Section 2 heading: "Utah's outbreak has run since June 2025".
- "The condition the 12-month test exists to catch" cut.
- Preprint finding on several introductions added. "Utah's own laboratory" became "Utah's laboratory".
- Utah three-week count removed from section 2.
- Fig. 2: "joint investigation" became "one border outbreak" in the label and alt text. Caption changed to "Four outbreaks".
- "West Texas is where most accounts start" cut. "Not a health department's" antithesis narrowed.
- "D8 genomes" became "genomes of genotype D8".
- "Gave ProPublica the limit" became "told ProPublica".
- Commission's list of evidence types cut.
- Reuters source attribution narrowed. "Neither account names the chain" added.
- Table reduced to two columns with dates in the text cells. Labels shortened. Arizona row reworded. Citations s10 and s13 added to the caption.
- Close rewritten on Situation Report 15. Source s21 added. nb-meta set to sources 21, words 1,192.

## Decision

approve. Every break was fixable from the record and the opened sources, the
argument stands as drafted, and the proof passes at 1,192 words with no block or
warning.
