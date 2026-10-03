# Editorial review: feature/ai-economy-atlas (editor/01)

## Correct

The thesis is readable from the draft alone: each ATLAS headline number measures
a particular quantity its own data dictionary defines, and reading one as a
measure of how much work AI does, or how much time it saved, swaps in a
different quantity. Four claims carry it.

1. The work "shares" are shares of conversational-request volume within a
   geography, not of jobs, task-help, or labour hours. Held. The draft sources
   the denominator to the dataset README ("relative volume of conversational AI
   queries"), the methodology note, the report's Section 2.3 ("measures
   behavioral interactions, not definitive productivity outcomes"), and the
   AI-in-Science footnote 14 ("we also do not see task completion or saved
   time"). All four match the evidence record. The draft never lets a share
   stand as a share of jobs, hours, or task-help; the India 19% line even says
   so in the negative ("not that AI does 19% of creative work").

2. The 30% is the report's and the interactive's published figure; the released
   dataset reproduces it only as 20.06%. Held. The draft attributes the 30% to
   Figure 1 and the announcement, labels 20.06% as the public-dataset sum of the
   U.S. computer-and-mathematical broad groups, and explains the gap with the
   README's "All Other" exclusion. The rest-of-world ~15% is stated as a
   back-calculation from "double," not as a published number. Nothing is
   presented as independently recomputed except the 20.06%, which is.

3. Usage-volume share and task-saturation depth are two measurements, and the
   second is shallow. Held. The draft separates size (volume) from position
   (depth) from the interactive's own two axes, gives median 21% of tasks, 68.5%
   with any use, 3% above three-quarters, and automation under 10% of
   non-routine-cognitive conversations. All match the record. The chart carries
   the depth axis the 30% is not on.

4. The ~6.9 hours saved is a self-reported belief, bounded but not refuted by
   independent work. Held. The draft keeps "~6.9 hours saved" distinct from the
   "~7 hours spent on data analysis" (the evidence flags this as the one
   conflation risk, and the draft names both and says which is which), carries
   the survey's limits (n=637, unweighted, not representative, selection bias the
   authors say over-estimates both adoption and savings), and uses METR and
   Humlum-Vestergaard to bound the self-report-to-economic-gain step, saying
   twice that neither studies scientists and neither refutes the survey. METR's
   February-2026 follow-up is flagged as having found different results, which is
   fair to it.

Breaks found. One was a real label error. The chart's figure caption cited
`href="#s5"` (the dataset, the correct owner of the CSV series) but displayed
the superscript number **3** instead of 5 — a wrong citation number every reader
of the figure would see. Fixed to 5.

Attribution and kind audit otherwise clean: the announcement (s3) is the only
`data-nb-kind="secondary"`, correct since the blog is secondary to its own data;
METR (s8) and Humlum-Vestergaard (s9) are primary for their own results and
independent of Google, as the record has them. Every figure in the body, the
table, the headline, and the dek traces to the evidence record; I found no
number, title, date, or quotation that departs from it, and recomputed nothing
the record had not already recomputed.

Citation hrefs: all nine resolve as printed (the proof link-check blocks on
404/410 and passed; I additionally confirmed the three load-bearing PDFs/dataset
by HTTP). Source 5's served path
(`/economy/atlas/embed-report-2026/data/atlas_v1_public_data.zip`) returns 200;
the top-level `/economy/atlas/data/...zip` path redirect-loops, so the writer's
switch was correct, lands on the same owning dataset, and changed no claim.

## Reads well

The draft was already close to the register the voice guide sets: it names the
target of inference, then the quantity the instrument produces, and commits where
the data commits. I cut three things and left the middles alone.

- "The science strand rests on a different instrument" — "rests on" is the
  abstraction-acting form `spec/slop.md` lists. A strand does not rest on
  anything. Changed to "comes from a different instrument," which states the
  same transition (logs to survey) without the figure.
- "Both numbers measure what they measure" — the opener of the final paragraph,
  and a tautology at the article's most-scrutinised position. It reduces to "X
  measures what X measures." Deleted, not repaired; the fairness it gestured at
  (the numbers are valid for their own quantity) is already carried by the
  sentence that follows, which names each quantity. The piece now lands on its
  earned close: "an account of AI at work that quotes either one as a measure of
  work done has changed the quantity without saying so."
- A body semicolon in the felt-vs-measured opener ("so neither refutes the
  survey; they set the bounds...") became a period, the plainer mark the
  editorial standard prefers. The one remaining semicolon ("Position is depth
  inside a job; size is the share of the usage pool") earns its place as a tight
  parallel and stays.

Headline, dek, headings. The headline states the finding with the surprise
first and no colon subtitle. The dek adds the specific figure and the 20.06%
recomputation without restating the headline, and avoids the three recent-desk
dek molds the brief named (no dependency-clause tail, no semicolon reversal, no
comma-triad close). The six headings each name a step of this argument in the
piece's own nouns and are built differently from one another; none is a
scaffolding slot. The piece does not drift into the recent audit-trail feature's
measurement-governance frame; it does arithmetic on a dataset, as commissioned.

I read the first and last sentence of every section and the article's last
sentence on their own. After the three cuts they report rather than fill.

## The experience

Read top to bottom, the page earns the chart and the table. The denominator
table pairs five headline figures with the quantity each counts and its source,
which reads faster than five prose restatements would. The chart (14 of the 22
major groups, the subset the record verifies) carries the depth axis the 30%
headline is not on: it shows saturation topping out near 46% for any use and
staying well under half even for the group that sends the most work queries,
which is the visual the volume-vs-depth distinction needs. It earns its place,
so I kept it rather than cutting it, and did not invent the volume series the
record withholds.

I rewrote its caption, which had been doing interpretation the editor skill
reserves for prose. The old caption said "each major occupation group" (it
charts 14 of 22) and called computer-and-mathematical "the largest single share
of the usage pool" while foregrounding its "intensive use on 30%" — a 30% that
is task saturation, not the volume 30% the whole piece is about, and so a live
conflation risk sitting in a caption. The new caption is a factual cited label:
the subset is stated as "14 of the ATLAS's 22 major occupation groups," the two
series are defined as the dataset's saturation thresholds, and the interpretation
(the biggest-volume group is mostly un-saturated) stays in the surrounding prose,
where it already was.

What the piece gives beyond its sources: it pins each headline figure to the
denominator its own data dictionary assigns, recomputes the release to 20.06%
against the 30%, and turns the shares into a checkable statement of what each
number does and does not establish about AI at work. That matches the writer's
original-work sentence in draft-handoff.md. Both survive; this is not a restated
source set.

## Edits

- Figure caption: corrected the citation number from 3 to 5 (href was already
  `#s5`, the dataset that owns the series).
- Figure caption: replaced the interpretive text ("each major occupation
  group... the largest single share of the usage pool... intensive use on 30%")
  with a factual cited label stating the 14-of-22 subset and defining the two
  saturation-threshold series; moved no new claim in, removed the volume/30%
  conflation risk.
- Self-report opener: "rests on a different instrument" to "comes from a
  different instrument" (abstraction-acting form).
- Felt-vs-measured opener: changed the semicolon after "neither refutes the
  survey" to a period.
- Final paragraph: deleted the tautological opener "Both numbers measure what
  they measure."
- Re-stamped (words 1831 to 1815) and ran the exact `nb check`: BLOCK 0, WARN 0,
  PUBLISHABLE.

## Decision

approve — the measurement spine holds, every figure traces to the record with
exact attribution, and the remaining problems (a wrong citation number and an
interpretive, subset-blind, conflation-prone chart caption) were editable in
place rather than being an argument no edit could reach.
