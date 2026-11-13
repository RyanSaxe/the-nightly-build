# Editorial review: reinforcement-learning/observation-scale (editor/02)

This round answers the reader check. The page has no other open item: source 1
stays as the commission's last decision rules.

## Correct

Main idea, from draft-handoff.md: one step size must suit the largest-scale
input, so the units set how slowly the rest learns, and standardizing each
component removes that dependence. The reader's restatement matches it: the
eigenvalues of A = E[xxᵀ], the 2/λmax cap, κ setting the slowest weight's pace,
c² from a change of units, standardization, and the PPO statistics saved and
frozen with the agent. No mismatch, so the central explanation stays as it was.

The headline and the takeaway, against the removal tests. The units rows (raw
metres against raw millimetres, all else equal) and the normalization rows are
manipulations, so a claim that the units cause PPO's blindness to velocity is
tested. What the page leaves open is the mechanism (conditioning, tanh
saturation or Adam). Two faults followed from that:

- The headline said "Reporting position in millimetres keeps PPO from using a
  cart's velocity". Table 2's normalized-millimetre row (56 to 100%) contradicts
  that as written, because with VecNormalize the environment still reports
  millimetres. It now reads "Reporting position in raw millimetres keeps PPO from
  using a cart's velocity", which is exactly what the units rows show and what
  the normalization rows remove. The title, nb-meta title and h1 all changed.
- The body ended "leave the cause open", which reads as a hedge on the
  headline's causal claim when it means the mechanism. It now ends "show what
  the units do to PPO without showing why". The takeaway's PPO sentence now says
  the runs measure the effect of the units without explaining it. The dek names
  the linear learner as its subject and needed no change.

Checks this round, all rerun as printed from a fresh folder:

- dock.py and linear.py as published reproduced their outputs exactly. After my
  edits to both (below), agents.py, rerun with the new dock.py, reproduced its
  output byte for byte in 3 min 33 s on four cores. The six listings and outputs
  on the page are identical to `editor/02/code/`.
- The millimetre position weight. At 2/(λmin + λmax) the largest eigenvalue's
  factor is −(κ − 1)/(κ + 1), the same size as the smallest's. With κ = 9.15
  million, both shrink to about 0.80 of their error after 10⁶ steps, and the
  output agrees: the velocity weight reaches 3.803 of 19.57 and the position
  weight 0.003922 of 0.02097, each about a fifth of the way.
- The 77.5 prediction: ln 100 / −ln 0.9424 = 77.6 from the printed κ of 33.7;
  the script's unrounded κ gives 77.5. Each step multiplies ‖w − w*‖ by at most
  that factor because I − αA is symmetric.
- The bounce. `editor/02/code/checks/bounce_check.py` pushes right from 2,000 of
  Dock's starts: every start docks, after 9 to 16 bounces (mean 9.3). Every
  bounce returns the cart slower, 89% of them by exactly one push of 0.05 m/s,
  and every two bounces by at least 0.05 m/s. A cart pushed from rest reaches
  0.5 m/s before the dock, so it loses one push per bounce from there. The cause
  is the discrete step: Dock adds the push before it moves the cart, so the trip
  back from the dock ends one push slower. This also explains the always-right
  baseline (127 steps, 100% docked).
- Seeds 5 to 9 (writer's out.txt): raw millimetres use velocity at 0 to 2% of
  grid positions, normalized runs at 24 to 100%, seed 7 docks 0% and 1% after
  normalized training, and seed 8 docks 67% on fresh statistics against 88%
  with its own. The page's new wording covers each of these.
- The "uses velocity" definition, from agents.py: a grid position counts when
  the 11 moves in its column (velocities +0.5 to −0.5 m/s) are not all the same.
- Problem 2's block form: with standardized components, E[1·zᵢ] = 0 and
  E[zᵢzⱼ] is the correlation, so A is 1 for the constant beside the 2 × 2
  correlation matrix. Eigenvalues 1, 1.9 and 0.1 stand.

No fact was added that the evidence record or a rerun does not support. No
number, quotation or citation purpose changed. Source 10 went with the
paragraph it supported.

## Reads well

Each reader place, with my action:

1. Millimetre row, position weight (worst). Added two sentences: the position
   weight is no further along, because its direction has the largest eigenvalue
   and at this step size its factor is −(κ − 1)/(κ + 1). The main idea needs
   this, since the largest-scale input is the one pinned at the stability edge.
   The cut-off columns were real at desktop width: the output was 97 characters
   and the box shows 93. I reformatted linear.py's second table to 85
   characters (same numbers) and split dock.py's one 103-character line into
   two, so "19 steps" is visible too.
2. "Bound" with two meanings. The output's step-count column was labelled
   "bound"; it is now "predicted", and the prose says "prediction". "Bound" now
   means only 2/λmax. The prose gives the factor (κ − 1)/(κ + 1) = 0.94, so the
   reader can check 77.5 without opening the code.
3. "That sample's error". Now "that sample's residual G − v̂". The paragraph
   stays because the commission requires saying which bound a run tests.
4. Raw metres against PPO. Cut "Raw runs in metres vary more" and the two
   numbers after it. The point moved into the mechanism paragraph and now says
   what it implies: the linear learner converges in metres in 76 steps, yet
   PPO's raw policies there use velocity at as few as 2% of grid positions
   against at least 83% normalized, so the linear κ does not predict PPO.
5. How a cart pushed right docks. One clause: a start right of the centre docks
   after about nine bounces, since in Dock's 0.1 s steps a cart pushed right
   returns from each bounce about one push slower. Cutting the sentence would
   have left the always-right baseline with the same puzzle.
6. Title against hedge. See Correct.
7. "Averaged over the starts". The eigenvalue section now says "averaged over
   the states it updates". The linear.py paragraph says the script fits only
   each episode's start, leaving out the states visited after it, and that the
   starts are why the features are close to uncorrelated. It does not describe
   the earlier lesson.
8. "Bordered by a 1". Rewritten in the eigenvalue section and in Problem 2's
   answer: a 1 for the constant, zeros beside it, the correlation matrix in the
   rest.
9. "Uncorrelated means a mean of zero". Added E[xᵢ · 1] = E[xᵢ].
10. Table 2's "Uses velocity". The caption now names the grid, 41 positions
    from −1 to +1 m and 11 velocities from −0.5 to +0.5 m/s, and the test: the
    move varies over the velocities.
11. "Seeds 5 to 9, from uv run agents.py 5". The sentence now says the argument
    is the first seed and gives the conclusion without the grid count.
12. NormalizeObservation and obs_rms. Cut the paragraph and source 10. The main
    idea does not need a second library, the commission ranked this paragraph
    first to go, and the reader could skip it.

The reader's skippable sections: the per-sample paragraph stays (commission
decision). Seeds 5 to 9 shrank to two sentences in the PPO section and one in
the statistics section. The Problems and dock.py stay, as the orchestrator
directs. Fig. 1 stays: it is the only drawing of the track, buffer and dock,
which Fig. 3 and the PPO prose rely on, and Table 1 has no geometry.

Results the reader found reported without meaning:

- "Seed 2 is the weakest in both" now ends "so a normalized run's result depends
  on its seed whatever the units".
- The seeds 5 to 9 normalized failure now says it fails in metres and in
  millimetres alike, which carries the same point.
- "Four of the five networks ... fail the same way" now adds that the fifth
  docks less often than with its own statistics.
- Raw metres against normalized metres: item 4.
- The millimetre position weight: item 1.
- Seed 1 now reads as a choice of one move per side: the four other raw
  millimetre policies split the track at its centre and pick one move for each
  side, and seed 1 pushes toward the centre from both, so its cart never
  reaches the dock.

Nothing in the new text came from the briefing or the voice guide's passages.
I read the edges of every changed paragraph alone. The new section closer is a
qualification you can check (which mechanism went unmeasured). Of my first
drafts, one sentence failed the placeholder test ("Outside SB3 the statistics
need the same care") and was deleted before the paragraph went. Another,
"sets the same trap", leaned on a word the page never uses and was rewritten.

## The experience

I rebuilt the page with nb preview and captured it with Playwright at 390 and
1280 px in light and dark. The page never scrolls sideways. At 1280 px the
dock.py and linear.py outputs now fit their boxes with no hidden columns. At
390 px every code box scrolls sideways, as before. Table 2 still scrolls inside
its wrapper on a phone, with "Uses velocity" in the second column. The
reformatted output keeps w and w* in one column, and the changed paragraphs
render cleanly in both themes.

Word count on the rendered page, by the same rule as before (cards, captions,
table cells, problems and answers in; code, output, equations, drawings, bands
and sources out). My counter includes the headline, dek and summary labels. On
the page as editor/01 left it, it gives 2,263 words containing a letter and
2,521 tokens, against editor/01's reported 2,210 and 2,490. On this page it
gives 2,385 and 2,671. The net rise is about 120 words, so the lesson is about
2,330 by editor/01's measure, over the 2,200 threshold. Where the explanations
added for items 1, 2, 4, 5, 7 and 10 cost words, I cut a whole idea
(NormalizeObservation), the raw-metres sentences and most of the seeds 5 to 9
detail. Every remaining addition answers a place where the reader could not
follow the main idea or a result. The next cut would remove the per-sample
bound or the centring sentence, which the commission requires, or a Problem,
which the orchestrator protects.

What the page gives beyond its sources is unchanged from editor/01, and still
matches the writer's original-work sentence. It derives the c² shift from a
change of units and checks it on an environment whose units can be switched.
It measures PPO's velocity-blind policy in raw millimetres and the
normalization that removes it. It now says plainly that the linear derivation
explains the linear learner and not PPO. Reread last, the headline claims what
the units rows show and the normalized rows remove.

## Edits

- Headline (title, nb-meta, h1): "in millimetres" to "in raw millimetres".
- Eigenvalues: "Averaged over the starts" to "Averaged over the states it updates".
- Eigenvalues: added "E[xᵢ · 1] = E[xᵢ], so" before "uncorrelated means a mean of zero".
- Eigenvalues: "correlation matrix bordered by a 1" rewritten as the block form.
- Eigenvalues: "that sample's error" to "that sample's residual G − v̂".
- dock.py: final print split into two lines; output updated; rerun.
- Linear runs: linear.py paragraph says the fit uses each episode's start only.
- linear.py: second table reformatted to 85 columns; "bound" column renamed "predicted"; variable renamed; rerun, numbers unchanged.
- Linear runs: pace paragraph gives (κ − 1)/(κ + 1) = 0.94, calls 77.5 and 21 million predictions, and explains the millimetre position weight.
- PPO: Table 2 caption defines the velocity grid and the test.
- PPO: seed 0 paragraph reordered, the bounce explained, seed 1 named; raw-metres sentences cut.
- PPO: seed 2 sentence given its meaning; seeds 5 to 9 cut to their conclusion, with the argument explained.
- PPO: mechanism paragraph adds the raw-metres comparison and ends "without showing why".
- Statistics: seeds 5 to 9 sentence names the fifth network.
- Statistics: NormalizeObservation paragraph and source 10 cut.
- Problem 2 answer: block form in place of "bordered by a 1".
- Takeaway: PPO sentence says the runs measure the effect of the units without explaining it.
- `editor/02/code/`: current listings, outputs and the bounce check.
- nb stamp (words 5140, sources 9); proof BLOCK 0, with the one W-CITE-DENSITY the commission kept.

The edits change no part of the central explanation and rewrite no whole
section. The largest changes are four paragraphs in the PPO section and one in
the linear-runs section.

## Decision

approve: the reader's restatement matches the main idea. Every place the reader
marked is fixed or cut. The headline and takeaway now claim only what the units
and normalization rows show.
