# Editorial review: feature/mlperf-grpo-post-training (editor/01)

## Correct

Thesis, from the draft alone: in MLPerf Training v6.1's GRPO benchmark the
quality gate never ended a run, so each score is the wall time of a fixed number
of GRPO steps with the whole loop on the clock. Three claims sit under it.

1. The whole loop is timed and the clock stops at the first passing checkpoint.
   Held. I reopened the rules (training_rules.adoc on master: eval-start formula
   line 510, offline-eval appendix line 678, sandbox-CPU clause in the line-411
   row, staleness line 408, "late eval to hide variance" footnote line 575) and
   the reference README (700 training tasks, leave-one-out baseline, no KL,
   1,004 trajectories per evaluation, "first scheduled validation" and "latent
   crossing-step variance" at lines 754–756). All match the article.
2. Every run passed at the first eligible step. Held. The table's arithmetic
   checks: ⌈2.5 + 3,840/GBS⌉ gives steps 18, 10, 7 and 6 and 4,608, 5,120,
   7,168 and 6,912 trajectories. 0.69 × 251 rounds up to 174, and 0.7131 and
   0.7849 of 251 are 179 and 197.
3. Scale buys speed at a steep accelerator cost, and the vendor comparisons
   leave backend, submitter, batch size, sandbox CPUs and staleness uncontrolled.
   Held, with one fix to the numbers (below). Every ratio in the vendor table
   recomputes: 1.32, 1.26, 1.38, 1.43, 1.32.

Breaks and fixes:

- Accelerator-minutes (brief item 1). I cloned training_results_v6.1 and
  recomputed run_start→run_stop for all ten Fig. 2 entries. The record's figures
  are the unrounded median minutes × count (13.7827 × 1,024 = 14,113), so the
  record is right about its own quantity. A reader who multiplies the printed
  score gets a different number, and the article defines accelerator-minutes as
  "the score times the accelerator count". I changed every printed and plotted
  figure to the printed score × count, rounded: 14,113 → 14,111, 10,696 →
  10,691, 11,206 → 11,203, 7,433 → 7,434, 5,149 → 5,148, 3,669 → 3,668, 1,659
  → 1,660. 2,719, 2,060 and 1,594 were already reproducible. The 6.7× ratio
  still holds (10,691 / 1,594 = 6.71). The chart's docstring states the rule.
- The rollout paragraph claimed more than the record supports. It set up "if
  rollout dominated the minutes" and answered "Both happen", using the
  start-of-run buffer fill as evidence. That wait happens under any asynchronous
  design, so it cannot show dominance. When I read the per-step tracked_stats in
  the same NVIDIA logs, policy training took most of each later step (about 185
  of 200 s at 64 GB300 TRT-LLM, step 1), and training's wait on generation
  ranged from about 5 s to over 3 minutes from step to step. I narrowed the
  paragraph to what the record supports. Training cannot start until the first
  rollouts return, and that wait was 10.4 of 35.84 minutes at 64 GPUs and 4.0 of
  12.93 at 1,024, about 30% of the clock in both. The per-step breakdown is not
  in the record and I did not print it. That was an edit to fit the evidence,
  not cover for thin reporting. If the orchestrator wants the piece to say which
  stage dominates the steps after the fill, that needs a researcher pass over
  tracked_stats across entries.
- "The fastest result in the round" was ambiguous, because the round has other
  benchmarks. It now reads "on the benchmark".
- The heading "The first allowed checkpoint always passes" stated a general rule
  from one round. It now reads "passed every time".
- Fig. 1 named Apptainer for every entry, but Google's sandboxes ran as GKE pods.
  The box now says "in a sandbox", and the caption says the stages follow the
  reference implementation, which accounts for the Megatron label.
- Group size 16 comes from the rules, so the GRPO sentence now cites [2] as well
  as [4].

Display text: the headline's claim (every clock stopped at the earliest allowed
step) holds for all 87 scored runs. The new dek's "16 times the GB300 GPUs cut
that time only threefold" is the GB300 vLLM series (42.48 / 13.78 = 3.08).

Links: the mlcommons.org, results-explorer, NVIDIA and Google hrefs return 200.
The sandbox proxy blocks direct GitHub page fetches, so I cloned the four GitHub
repositories and confirmed that every cited path exists on the printed branch
(master or main). Source kinds: all eleven are correctly primary. Vendor
documents are cited only for their own claims or their own submissions, and the
piece claims no independent secondary source.

## Reads well

Cut:

- The closing sentence "A v6.1 GRPO score is the wall time one machine took to
  generate, sandbox, reward and train on a fixed set of episodes." It restated
  the opener and the dek. The closer now ends on the comparison rule and names
  both unrecorded quantities, the sandbox CPUs and staleness. The draft had named
  only the CPUs.
- "Who ran a system matters far less than its size" became "Submitter matters
  less than size", and the paragraph now gives its evidence: the four 64-GPU
  GB300 TensorRT-LLM submitters fall within 8% of each other, against a
  1.7%–14.2% spread among the runs of a single entry.
- "Left free" in the heading, the table column and the body was the voice
  guide's instruction wording. A reader would stop on it. It now reads "not held
  constant" throughout.

Dek: the draft's dek repeated the headline ("cleared the bar at the first
checkpoint" after "stops every clock at the earliest step"). The new dek
supplies what the headline leaves out: the round, the model, what a score is,
and the scale cost. It names no person and has no contrast clause, so it does
not follow the recent dek pattern. The headline does not use the "X
averages/reveals N of M" frame, and the opener states the finding first. The
section headings are built differently from each other.

Brief item 2: the README's "140 to 160 minutes" did not get a sentence. That
span includes inline evaluation and comes from a BF16, staleness-1 setup.
Explaining it would take a new source (rcp_logs) and about 40 words, and the
article sits at 1,197 of 1,200. The piece never sends a reader to that figure.

I found no borrowed exemplar phrasing. The register already matches the voice
guide: Fig. 2 is read with the computation written out, and each comparison
states the quantity it does not hold constant.

## The experience

I captured the page with Playwright after nb preview at 390 px and 1,280 px, in
light and dark. Neither width scrolls the page horizontally. The vendor table
scrolls inside its own wrapper on a phone. Fig. 1 has no overlapping labels and
every arrow reaches its box in both themes. Fig. 2 renders on its light panel in
both themes. Its labels can be read at phone width, and the 512 tag sits clear
of the crossing lines. No component was added or removed: each section already
sits under a visual.

Beyond the sources: the piece sets the rules' earliest-evaluation formula
against every run's stopping step to show that a v6.1 GRPO minute times fixed
work, then prices scale and each vendor headline in accelerator-minutes and in
what it leaves uncontrolled. None of the sources makes that reconciliation. It
matches the original-work sentence in draft-handoff.md.

## Edits

- Dek (dekline and nb-meta): rewritten as above.
- Orientation: "how much hardware" → "the hardware and software".
- GRPO sentence: added citation [2].
- Fig. 1 SVG: "repo in an Apptainer box" → "repo in a sandbox".
- Fig. 1 caption: "Conceptual" replaced by "with stages as in the reference implementation".
- Rollout paragraph: rewritten to the record's buffer-fill figures (10.4/35.84, 4.0/12.93, about 30%); the dominance claim was removed.
- Heading and section id: "always passes" → "passed every time".
- Fig. 2 alt text, chart-1.py data and docstring, and chart-1.png re-rendered with nb chart: accelerator-minutes = printed score × count.
- Fig. 2 caption: "derived" replaced by "score × GPU count".
- Scale prose: 14,113 → 14,111 and 10,696 → 10,691; "in the round" → "on the benchmark".
- Submitter paragraph: rewritten with the 8% spread against the 1.7%–14.2% within-entry spread [3].
- Vendor section heading, id, column and body: "leave free" → "do not hold constant".
- Google row: "which Google's footnote labels 6.1-0017" → "Google's footnote gives the ID as 6.1-0017".
- Closer: restating sentence cut; the last sentence now names the sandbox CPUs and staleness.
- Restamped: 1,197 words, 11 sources, 5 min. Proof: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The argument holds against the rules, the logs and the results table,
and the fixes this review lists are all edits made in place.
