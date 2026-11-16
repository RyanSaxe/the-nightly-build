# Editorial review: feature/toolturns-multi-turn-agents (editor/01)

## Correct

Thesis, from the draft alone: in ToolTurns, every model completes more whole
dialogues than independent requests would give, so outcomes cluster within a
dialogue, and the shortcut of cubing the opening-request rate lands close only
because two effects offset. Claims under it:

1. All nine models complete 5.8 to 8.4 points above the product of their three
   position rates. Held. I recomputed every product, difference and ratio from
   Tables 3 and 4 (opened at arxiv.org/html/2611.14925v1). All match the
   article, Fig. 3 and Table 1 to one decimal. Opus 4.8: 74.7 x 65.4 x 68.6 =
   33.5 against 39.8. The paper's own 0.696^3 is 33.7, which the article
   prints as "about 34%". The sampling error at n = 2,620 near 40% is 0.96
   points.
2. Every model scores lower on both follow-ups than on the opening request.
   Held (Table 4; the paper says so in 4.1.3). The averages 67.9 and 59.4 and
   the 1.9 to 15.0 range in Fig. 2's label recompute. The paper's caveat that
   the decline does not isolate a cost of conversational dependence is stated.
   I checked it against 4.1.3 and F.3, problem 1515.
3. Rubric rank and task-success rank disagree, mostly through GPT-5.4-mini.
   Held at the strength the decisions log set: Spearman 0.233 reproduced, 0.64
   without GPT-5.4-mini, exact two-sided permutation p = 0.552 (all nine
   factorial orderings enumerated). Every slope in Fig. 4 matches the ranks.
4. Cubing the opening rate lands within 3.3 points of observed completion for
   eight of nine models, because the follow-up factor (0.59 to 0.94) and the
   clustering factor (1.19 to 1.51) offset. Held. Cube x follow-up factor x
   clustering factor reproduces observed completion exactly in every row,
   GPT-5.4-mini is 6.9 low, and the largest gap among the other eight is 3.3
   (Gemma 4).

Breaks and fixes:

- The opener said "repeating it for every model" after the paper's pooled-rate
  cube. The 5.8 to 8.4 range comes from the product of the three position
  rates, not the pooled rate cubed. With the pooled cube the range would be
  5.6 to 8.1. Rewritten to name the product of each model's three per-request
  rates.
- BFCL: the draft said BFCL "stops a task at its first failed turn". The blog
  stops a task only when a turn is force-terminated after more than 20 steps
  ("Step Limit Force Termination"). An ordinary failed turn moves on to the
  next turn. The clause is cut. What remains is within what BFCL owns: the
  all-turns rule, no per-turn rates, the single-turn range and the FC/Prompt
  gap. I recomputed the 75 entries at 80% or more non-live accuracy (80.81 to
  90.65) and their multi-turn range (0.38 to 77.38) from data_overall.csv,
  and the Opus 4.5 rows (88.58/68.38 FC, 89.65/16.12 Prompt). "All 75 score
  lower" was dropped. A harder task set scoring lower shows nothing. The
  spread is the claim the record assigns.
- tau-bench: the draft read pass^8 as only an upper bound ("below 25%") and
  concluded tau-bench "cannot test clustering". The paper's introduction gives
  the value, "drops rapidly, to as low as 25% for pass^8 on retail" (section
  1, paragraph beginning "Our experiments reveal"), and the abstract gives
  "<25%". About 25% against 1.9% for independent trials shows tau-bench's
  outcomes clustering by task across trials that share no context. That is a
  precedent for the paper's first explanation (shared difficulty), set beside
  Laban et al.'s precedent for the second (carry-over). The sentence now says
  so, adds the section 1 locator, and ends "Neither shows which operates here".
  The tables still cannot say why. This is a reading of a printed figure, not
  a new number, and the citation still covers the same passage. The
  orchestrator should confirm it (question 1 below).
- Laban et al.: "report the second" claimed more than the abstract does. Laban
  et al. report carry-over of a wrong turn, not the paper's success-side
  phrasing. Recast as "found carry-over in text tasks", with the abstract's
  words quoted. Nothing in the piece now says failures cascade in ToolTurns.
- Rubric explanation: "the paper traces it to API calls" compressed the paper
  wrongly. Section 4.1.3 traces GPT-5.4-mini's lead to the efficiency and
  consistency aspects, which reward few, coherent calls "whether or not the
  answer is what the user asked for". It gives the 3.6 calls as evidence.
  Rewritten to that, with the 4.1.3 locator added.
- tau2-bench: 40% and 47%, 12% and 13% critical, checked in section 4.3. The
  sentence uses them only as measured simulator error elsewhere, not as a
  ToolTurns rate and not for clustering.
- Fig. 2 caption "is also the judge model": the paper's Table 3 footnote on
  the GPT-OSS row reads "GPT-OSS is also the judge model". Kept as printed.

Hrefs: all five land on the source (arXiv abs pages 200; BFCL blog 200;
data-nb-url leaderboard 200). Kinds: all five are primary for the claims
they carry. tau-bench and tau2-bench share Sierra authors (Narasimhan). They
carry different claims and neither corroborates the other, so no
independence is claimed.

Evidence-record slip, not in the article: Contradiction 10 says problem 2610
has "seven of nine models fail the opening request and pass a later one".
Table 9 as transcribed has seven failing the opening, and six of them passing
a later request (GPT-OSS fails all three).

## Reads well

Cut:
- "Both have a precedent outside ToolTurns", which I wrote myself in a pass. It
  said nothing the next two sentences did not show.
- "not a rate for ToolTurns" after "That is another simulator on other tasks".
  It restated the first half.
- "It does show how little a single-turn score says about that rule". The
  referent was vague, and the point is now made directly by the 0.4 to 77.4
  range.
- "The disagreement rests on GPT-5.4-mini". An abstraction acting, and the
  0.64-without-it figure already shows it. The p-value sentence now carries the
  conclusion.

Recast:
- The orientation heading duplicated the independence section's heading. Both
  said the observed rate beats independence. It now gives the scoring rule the
  section and Fig. 1 explain: "A dialogue counts only if all three requests
  pass".
- ToolTurns was not identified as a benchmark until paragraph two. The first
  sentence now says "the ToolTurns tool-use benchmark".
- "checker-fixer" was used before anyone was told there is a simulated user.
  It is now glossed in a clause.
- The last section's heading said "two errors cancel". The two terms are
  effects the cube leaves out, not errors, so it now says "two effects
  offset".
- The closer said "an opening-request score sees neither effect" two
  paragraphs after the effects were named, with BFCL in between. It now names
  the follow-up decline and the clustering, then gives the recommendation. The
  closer does not end on a limit of the record, and the opener states the
  finding with no definition. Both break the recent pattern the brief flagged.
- Three sentences over the proof's density threshold were split.

Nothing came from the briefing or the voice guide's exemplars. I checked the
commission's angle sentences and the Yan, Huyen and Husain passages against
the prose and found no borrowed clause. The dek and headline differ from the
recent molds. The register is consistent and plain, and "my arithmetic" marks
every derived figure.

## The experience

All four inline SVGs and the table were rendered with nb preview and Playwright
at 390 px and 1280 px, light and dark. No page-level horizontal scroll at
either width, no clipped labels and no overlaps. GLM-5.2's two follow-up
markers coincide in Fig. 2 because both values are 64.8, and Qwen3.5's nearly
coincide (57.8, 57.5). That is the data. Table 1 scrolls inside its card on a
phone, as the runtime intends. No component added or removed. Each section
already has its visual, and the word ceiling leaves no room.

What the piece gives beyond its sources: it extends the paper's one-model
independence check to all nine models, then shows that the opening-rate
shortcut evaluators would use comes close only because the follow-up decline
and the clustering offset, and it sets the rubric disagreement at its actual
strength. That matches the original-work sentence in draft-handoff.md. The
headline, the piece's largest claim, says failures cluster and makes no claim
about cause. The body supports that.

## Edits

- Orientation h2: "The drop is smaller than three independent passes predict" became "A dialogue counts only if all three requests pass".
- Opener: "in ToolTurns" became "on the ToolTurns tool-use benchmark".
- Opener: "Repeating it for every model puts all nine above independence, by 5.8 to 8.4 points" became "Against the product of each model's three per-request rates, all nine complete 5.8 to 8.4 points more".
- Orientation: the checker-fixer sentence now glosses it as rewriting flawed simulated-user turns.
- Orientation: cut "not a rate for ToolTurns".
- Follow-ups: "The paper does not call this a measured cost of carrying context" became "The paper says the decline does not isolate a cost of carrying context".
- Independence: the Laban sentence was recast as carry-over, with the abstract quoted.
- Independence: the tau-bench sentence was rewritten as clustering by task across context-free trials (about 25% against 1.9%), with the section 1 locator added. Added "Neither shows which operates here."
- Rubric: the "rests on" sentence was cut. The p-value sentence now ends "so it is not distinguishable from zero". The API-calls explanation was rewritten to the paper's efficiency and consistency explanation, with the 4.1.3 locator added.
- Last h2: "two errors cancel" became "two effects offset".
- BFCL: cut the false "stops a task at its first failed turn" and "All 75 ... score lower". The paragraph now gives the 0.4% to 77.4% spread directly, split into two sentences.
- Closer: rewritten to name both effects, then the recommendation.
- nb stamp: 1,197 words, 5 min, 5 sources. Proof: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

Approve. The argument holds on the paper's tables, and every break was fixable
from the sources and the record.

## Questions for the orchestrator

1. tau-bench: I read "drops ... to as low as 25% for pass^8" (section 1) as the
   value, not only the abstract's "<25%" bound, and the sentence now reports
   clustering by task in tau-bench. If you would rather keep tau-bench to the
   narrower bound reading, revert to "below 25%" and drop the comparison with
   1.9%. The rest of the paragraph stands either way.
