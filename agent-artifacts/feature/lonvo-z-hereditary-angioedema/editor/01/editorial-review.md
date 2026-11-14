# Editorial review: feature/lonvo-z-hereditary-angioedema (editor/01)

## Correct

Thesis: of the three percentages Intellia attaches to lonvo-z, only HAELO's 87%
has a placebo arm. On that endpoint one infusion matches lanadelumab every two
weeks and garadacimab monthly. The ACAAI 81% and 89% are comparisons within the
same patients, and the 89% rests on few patients past one year. The claims under
it:

1. HAELO: 0.26 v 2.10 attacks a month, weeks 5 to 28, 52 v 28, -87% (78 to 93).
   Held. I checked it against the NEJM abstract (Europe PMC, PMID 42294842).
2. The comparators' primary endpoints sit on one axis with lonvo-z. Held for the
   five plotted trials. I checked them against the DailyMed SPL text: TAKHZYRO
   Table 3 (87, 76 to 93; rate per 4 weeks), ORLADEYO Table 3 (44.2, 23.0 to
   59.5), ANDEMBRY Table 4 (89.2, 75.6 to 95.2), DAWNZERA Table 4 (-81, -89 to
   -65). Two breaks are fixed below.
3. The 81% and 89% have no placebo arm. Held. The deck (SEC Exhibit 99.1, read
   with WebFetch) confirms N=35/52, the 90-day patient-reported window, the
   100-day prior-LTP definition, "Median total follow-up: 7.6 months" on slide 29
   and "Mean (range) ... 7.6 (0.3-46.5)" on slide 33.
4. Nex-z sequence. Held exactly. I reopened the 8-Ks of 27 Oct 2025, 29 Oct 2025,
   9 Jan, 27 Jan and 2 Mar 2026: the patient was dosed 30 Sep, the report came
   24 Oct, dosing paused 27 Oct, FDA gave verbal hold notice 29 Oct, the patient
   died 5 Nov, and the cause was septic shock from a perforated duodenal ulcer in
   a course that included acute liver injury. The piece states no causation and
   says that no filing gives one. The section takes about a sixth of the article,
   in line with the commission.

Breaks and fixes:

- **The derived C1-INH SC point (Fig. 2) is removed.** The HAEGARDA label does
  support both inputs exactly: "0.52 attacks per month compared to 4.03". But it
  also states COMPACT's own percentage, a median per-patient reduction of 95%
  (79, 100), and reports the primary result as a within-subject difference
  (-3.5). So a plotted 87% sat beside an owner-stated 95% that a reader would
  find on opening the label, and it came from a crossover trial whose placebo
  rate is twice the others'. The point and its caption sentence are gone. The
  caption now says COMPACT reports no rate ratio, and the chart-1.py docstring
  records why.
- **COMPACT row, patients column.** "90" was the whole trial across both doses.
  The 60 IU/kg row is 45 sequences (label Table 4, N = 45), now "45, crossover".
- **"Every comparator counts from the first dose."** This is false for COMPACT,
  whose label says "Efficacy was evaluated for the last 14 weeks of each
  treatment period". The sentence now says "the parallel-group comparators".
- **"After plasma kallikrein reached steady state."** The cited deck (s3) does not
  say this. The phrase comes from the June 8-K exhibit, which the article does not
  cite. The sentence now says only what s1 and s3 show: HAELO counts from week 5
  and skips the four weeks in which the infusion lowers kallikrein (deck slide
  30).
- **"More than in any comparator but APeX-2."** COMPACT's prior-prophylaxis share
  is not in the record, so the claim could not be checked. It now reads "against
  18% to 75% in the comparators that report it".
- **"The 0% holds by definition."** The 0% referred to something the article
  never introduced (slide 60's 62% v 0% attack- and treatment-free row). I cut it
  for length rather than add the row.
- **"Many of whom had stopped it."** Slide 27 gives the placebo arm's prior-LTP
  subgroup as 22 of 28, so the sentence now says "22 of whom".
- **"With no concurrent comparator and no blinding."** HAELO was double-blind
  through week 28, so the 0.22 was collected blind. "No blinding" read as if it
  covered both periods. I cut it. The baseline is now labelled as patient-reported
  and recorded on prophylaxis, which is what the slide says.
- **10-Q quotation.** The article had the 10-Q warning that "permanent editing
  effects" may make adverse events irreversible. The filing says "potentially
  permanent nature of genome editing effects", and the quotation now matches.
- **APeX-2 arms.** "120 in three arms" is now "40 v 40" (150 mg v placebo), read
  from the ORLADEYO label's Table 3 column N. This is a figure from a cited source
  that the record does not carry; the orchestrator should confirm it against the
  JACI paper if it wants a second reading.
- **Rate units.** HELP's "monthly" rate is attacks per 4 weeks under its label.
  The table caption now says so.
- **Hold lifted on 2 Mar 2026.** The date was printed with only the 27 Jan 8-K
  linked. I added the 2 Mar 8-K as s16, renumbered the 10-Q to s17 and corrected
  s15's label.
- **Headline "CRISPR".** The body never said it. The NEJM abstract and the release
  ("Based on Nobel Prize-winning CRISPR/Cas9 technology") support it, and the
  opener now names it.
- **Fig. 1, C1 inhibitor.** "HAE patients lack it" became "In HAE it is missing or
  faulty". The TAKHZYRO label reads "C1-inhibitor (C1-INH) deficiency or
  dysfunction".

Fig. 3: the chart, its subtitle, its data labels (now "~0.3", "~0.2" and so on)
and the caption all say the rates were read by eye from slide 31. The at-risk
counts are exact. The prose cites no rate from the curve. It uses only the 89%,
the 3.3 baseline in the alt text and the at-risk counts, so nothing leans on the
approximated values.

Hrefs. All five DailyMed lookup URLs return 200 with the right drug title. The
three DOIs redirect to nejm.org and linkinghub.elsevier.com, which put bot walls
in front of curl, as expected. Every sec.gov href opened through WebFetch and
held the passage cited. sec.gov returns 403 to curl without a declared contact
address. I did not send one. **One href is unverified:** s2, the GlobeNewswire
release, returns an Akamai 403 to curl and to WebFetch, and a search turned up
no independent copy of release ID 3401802. The text it cites matches the
syndicated wire copy (manilatimes.net), which I read. My assumption is that the
URL is right. The orchestrator should open it in a browser before the PR. If it
does not land, the fix is to swap the href, and the citation does not change.

Kinds: all 17 are `primary`. Every one is the trial's own report, the FDA label
or Intellia's own filing or release, and no secondary carries a figure.

## Reads well

What went:

- "That is this article's inference, and patient-level data would test it." The
  piece was narrating itself. It is replaced by "may read smaller" in the claim
  and "No published analysis tests it", which says what went unmeasured.
- "'Up to four years' rests on the right half of Figure 3." This pointed at a
  figure instead of saying what it shows. It now gives the at-risk counts (24 at
  month 12, 10 at month 36, 4 at month 41), as the commission asks wherever
  durability is claimed.
- "Sebetralstat ... was tested on time to symptom relief and has no attack rate"
  was trimmed to the reason it is left out of the comparison, for length.
- "The span from berotralstat to garadacimab", which I had added myself, was cut
  for length. Fig. 2 shows the span.

Grammar: "Randomised within the same subgroup ..., the rate ratio was" had a
dangling modifier and is rewritten. The 40-word safety sentence the proof flagged
is split.

Headings: "On the placebo-controlled endpoint, lonvo-z overlaps the best chronic
drugs" became "Against placebo, lonvo-z matches lanadelumab and garadacimab". It
uses the piece's own nouns, and "best" was a ranking the section does not argue.
"Nex-z's liver hold" became "clinical hold", because the FDA's reasons are not
public. Only one heading leads with a figure ("The 81% and 89% ...").

Closer: "at month 36 the uncontrolled record holds 10 patients" is replaced by
Intellia's own claim ("intended to permanently lower kallikrein", from the
release) set beside the 24-week controlled count. That ends on what the article
established and not on a pending dataset. The 10-patient figure moved into the
ACAAI section.

Recent-pattern check: the dek does not open with a prepositional frame, does not
join clauses with ", and" and does not use "arithmetic". The opener is the drug
and its trial, not a timestamp or journal frame. The headline has one number and
no number-pair. The "excludes the benefit" phrasing does not appear.

Edges read alone: each section's first and last sentence now carries a figure or
a named document. The register matches the voice guide: glosses are short, and
each denominator and period sits in the sentence that carries its number.

## The experience

Fig. 2 is cleaner without a hollow marker that needed its own caption footnote.
Both charts had type around 4 to 5 px on a 390 px phone. I raised their fonts,
which put them at about 8 to 9 px on a phone. They are now readable, still small,
and limited by the engine's fixed 1200 px export width. In chart-1, the Lonvo-z
"87" was clipped at the top once the font grew, so I set cliponaxis=False and
added top margin. In chart-2, the bar labels shrank unevenly, and constraintext
is now off. Neither page has horizontal overflow at 390 px or 1,100 px in either
theme. The table scrolls inside its card on a phone. Fig. 2 and Fig. 3 render on
light chart paper in dark mode, which is engine behaviour.

What the piece gives beyond its sources: it sets HAELO's 87% on the same axis as
four approved prophylactics' primary endpoints, with each trial's window, arm
sizes and prior-prophylaxis share. It shows that the sponsor's 81% sits beside a
randomised 92% in the same 35 patients, and that the 89% thins to 10 patients by
month 36. This matches the writer's original-work sentence once the derived
C1-INH point is removed. The headline holds as the largest claim: 87% for one
infusion against 87% for lanadelumab every two weeks, both against placebo.

## Edits

- Opener: "single intravenous CRISPR gene-editing infusion".
- Stat strip: added "weeks 5 to 28" to the 81% and "up to 4 years, uncontrolled" to the 89%.
- Pathway prose: bradykinin "which causes the swelling" (TAKHZYRO 12.1), and added s4 to the lanadelumab citation.
- Sebetralstat sentence shortened.
- Fig. 1 SVG and aria-label: C1 inhibitor "missing or faulty". Caption trimmed.
- Section 3 heading retitled.
- Lancet sentence tightened.
- Fig. 2: derived C1-INH point removed from chart-1.py and re-rendered. Alt text and caption updated.
- Table caption: 4-week months for HELP and OASIS-HAE.
- Table: APeX-2 "40 v 40". COMPACT "45, crossover", window "last 14 of 16 weeks".
- Window sentence rewritten without "steady state". It covers parallel-group comparators only and cites s1 and s3.
- Prior-prophylaxis sentence: "against 18% to 75% in the comparators that report it".
- Slide 60 sentence: dangling 0% sentence cut.
- 81% paragraph: "no blinding" cut, "on prophylaxis" added, dangling modifier fixed, "22 of whom", self-reference cut.
- 89% paragraph: endpoint and window stated, follow-up sentence split, at-risk counts added with a citation.
- Fig. 3: labels marked "~", subtitle and caption name slide 31, fonts enlarged, bar text fixed.
- Safety heading: "clinical hold". Timeline: "liver transaminases". Hold-lift event now cites s15 and s16.
- Grade 3 sentences recast. "No cited source ties ..." tightened.
- 10-Q quotation corrected to the filing's wording.
- Closer rewritten from the release's "intended to permanently lower kallikrein" and the 24-week count, citing s1, s2 and s3.
- Sources: s15 relabelled "8-K, 27 Jan 2026". New s16 (8-K, 2 Mar 2026). 10-Q is now s17. s2 locator now names the "About lonvo-z" passage.
- chart-1.py: larger fonts, top margin, cliponaxis=False. Re-rendered with nb chart.
- `nb stamp`: 1,198 words, 17 sources, 5 min.

Proof (exact brief command): BLOCK: 0, WARN: 0, PUBLISHABLE.

## Decision

approve. The argument stands, and every break was fixable from the record and
the cited documents. One condition remains before the PR: someone opens the s2
GlobeNewswire href in a browser and confirms it lands.
