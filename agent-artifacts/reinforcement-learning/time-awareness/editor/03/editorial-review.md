# Editorial review: reinforcement-learning/time-awareness (editor/03)

## Correct

Thesis, unchanged: when a time limit belongs to the task, the moves left are
part of the state, so the agent has to observe them and the last move is a
termination. The brief reports that the second reader's restatement matches the
main-idea sentence in writer/01/draft-handoff.md. I confirm the page still
carries every part of that sentence after this round's cuts. The Markov
paragraph, backward induction, the terminal pair and the two kinds of run are
untouched. Only the material around the results changed.

How the claims held on this pass:

1. Cell 5's best move is left with one or two moves left and up with three or
   four, and cell 10 makes the same change with down and right. Held. The
   printed exact output shows both, and figures.py regenerates Fig. 1 from it.
2. A pair with no moves left is terminal. Held. Nothing in this round touched
   the argument. Only the sentence about a learner that bootstraps anyway was
   cut, and Problem 2 still covers that case.
3. With the pair observed, Q-learning earns 0.66 in every run. With the cell
   alone it earns 0.20 to 0.35, and all of the shortfall comes from cells 5
   and 10. Held. I reran seeds.py on seeds 5 to 9. Every time-aware run earns
   0.66, and the cell-only runs earn 0.20 to 0.38. where_lost.py on the same
   seeds leaves a gap of 0.0000 once cells 5 and 10 get backward induction's
   moves, and in every run those are the only cells whose one move is wrong.
   Two sentences are new. The first, "the most any policy can earn", holds
   because 0.66 is the mean of v_4. The second says that cells 5 and 10 are
   the only cells in Fig. 1 where no single move is best with every number of
   moves left. I checked it against backward_induction's best-move sets for
   all 14 cells. Every other cell has a move in all four sets.
4. The cell-only runs learn the mistaken loop's table entry for entry. This no
   longer appears on the page. The claim held when editor/01 and editor/02
   reran it, and I cut it because the main idea does not need it (see place 1
   below). This narrowing is for focus. The reporting behind the claim was not
   thin.

Fig. 2's rings, place 8. In seeds 0 to 4 the time-aware runs' estimates of up
with three moves left are −1.3, −1.24, −1.04, −0.95 and −0.95. Their mean is
the printed −1.1, against the exact −0.86. On seeds 5 to 9 the same estimate is
−0.99, −1.29, −1.12, −0.36 and −0.79. Up's estimates spread widely at every
number of moves left, so the low mean in the printed five runs does not repeat
as a bias. The page now gives that conclusion without these numbers, as the
series allows for seed checks. Fig. 2's aria-label said the rings sit "on or
near" the exact values. It now names this ring and its value, in figures.py
and on the page.

Citations. No href changed. Cutting the Pardo framing removed s1's Abstract
locator and made Sutton and Barto the first source cited. I renumbered them:
Sutton and Barto is now s1 and Pardo is s2, with every inline cite updated. The
orientation section now has no citation, and the proof warns W-CITE-DENSITY.
That section is a hand calculation plus a value from the printed run, and the
series direction says the warning needs no action there. All five
`data-nb-kind="primary"` labels stand as editor/01 audited them. editor/01's
open item on the MIT Press href stands as that review left it.

## Reads well

The second reader check, place by place, with the action on each:

1. The entry-for-entry paragraph: cut. The reader could skip it, and
   reconciling its "grid that ends at random" reading with Fig. 2's would have
   needed a new explanation. With it went the takeaway's two sentences on the
   mistaken loop, the largest-estimate grid and the cut_is_terminal rerun in
   moves_left.py, and Background row 01's "loop that wrongly stops its target".
   That row now names the target that bootstraps after a cut, which the body
   and Problem 2 use.
2. "A learner that bootstrapped there anyway…": cut, along with "With
   terminated, the target is right whatever the table holds." That sentence
   only pointed at the cut one. The paragraph now ends "Here nothing follows
   the fourth move." Problem 2 keeps the case as an exercise with its working.
3. The 0.20 against 0.35 and "All five go down at cell 10": cut. "Whichever
   move a run picks is wrong for two of the four" implied the two moves cost
   the same. It now reads "Neither move is best with every number of moves
   left, so whichever move a run's table prefers at cell 5 is wrong with some
   of them." The page no longer reports which choice earns more, so nothing is
   left unexplained.
4. The 0.34/0.12 split: cut, along with its two printed columns. The removal
   test ("5, 10 fixed") stays, because it is what makes the causal claim
   checkable. Its paragraph now opens with why those two cells are the ones
   to fix.
5. 0.66: defined at first use as the mean of v_4 over the 14 start cells and
   the most any policy can earn. The dek and the runs heading now say "the
   optimal return" instead of the bare number. I added no cell-only baseline.
   The best one-move-per-cell policy exists only in the writer's off-page
   stationary.py, and printing it would add a result. The removal test already
   gives the comparison the page needs.
6. The mirror sentence: corrected to name the moves. "Cell 10, below the pit,
   makes the same change with down in place of left and right in place of
   up," after a sentence that states cell 5's moves.
7. "Lands between" and −1.69/−1.57: cut from the prose. The page now says
   only that each move gets one estimate for its four values, as the ball's
   cell got one entry for both speeds, with the link to frame-stacking's
   averaging section. The two means stay in the printed output and in Fig. 2's
   dashed lines.
8. The ring for up at three moves left: one sentence says it is the farthest
   from its exact value and still above left's. Another says it varies
   between runs and lands above the exact value on other seeds.
9. "Time-aware" is now used in the body, where see_time is described. The
   two-arrow cell already has its explanation in Fig. 1's caption, and I added
   no prose for it. Fig. 1 carries no numbers: no action, because the values
   the argument uses are in the text and in Fig. 2.

The reader's skippable list: the Pardo "two kinds of time limit" framing is
cut, because the Why this matters card already defines a limit that belongs to
the task, and the terminal-pairs section makes the contrast with the earlier
lesson. I kept the four_moves.py demo and its paragraph. Its output is the
page's one printed step showing terminated True and truncated False on the
last move, which is the main idea's last clause, and its observation 77 shows
the pair encoding.

Edges: "Here nothing follows the fourth move" and the takeaway's new last
sentence both state a fact from the page. Neither fails the placeholder test.
Against the recent record, the new dek is one sentence with no comma-and join
and no "settle". The new runs heading does not open with "The" and carries no
number.

## The experience

The runs section is now shorter, and its paragraphs come in the order a reader
asks: what each observation earns, why one estimate per move fails (Fig. 2),
then which cells the loss comes from. The section ends on the removal test, not
on a comparison with another lesson.

I built the page with `nb preview` and read it at 390 px in the light theme
through headless Chrome, from the header to the sources. Playwright is not
installed. Both SVGs differ from the versions the writer checked in both themes
only in Fig. 2's aria-label, so I did not repeat the dark-theme captures.

Prose, counted on the rendered page per the lesson identity with editor/02's
rules (inline code excluded, which reproduces editor/02's 2,183): 1,980 words
with the headline and dek, 1,947 without. `nb stamp` reads 3,539 words, 15
minutes, 5 sources.

What it gives beyond its sources: the four-move task's exact time-indexed
values on a grid the reader knows. It finds two cells, 5 and 10, where no
single move is best with every number of moves left. It builds an environment
that reports the task's own limit as terminated. And a removal test shows that
a cell-only learner loses all of its return at those two cells. The handoff's
original-work sentence also claimed the entry-for-entry identity with the
earlier lesson's mistaken table. That part is now off the page, as recorded
under Correct, and the rest survives. The headline's claim still matches the
hand calculation.

## Edits

- Dek (nb-meta and dekline): "reaches the optimal mean return of 0.66" became "earns the optimal return".
- Background row 01: "the loop that wrongly stops its target at a time limit" became "the target that bootstraps after a time-limit cut".
- Orientation: cut the four Pardo sentences on two kinds of time limit, with the s1 Abstract cite and the termination-and-truncation link.
- Backward induction: the mirror sentence became two sentences naming cell 5's moves and cell 10's.
- Terminal pairs: cut "A learner that bootstrapped there anyway…" and "With terminated, the target is right whatever the table holds."
- Terminal pairs: see_time sentence became "With see_time the agent is time-aware: its observation is cell + 16 × moves left, one integer for each pair."
- Runs heading: "earn the optimal 0.66" became "earn the optimal return".
- Runs: "the settings of the earlier runs under a four-move limit" became "as the runs under the four-move cut did", linked to termination-and-truncation#runs.
- moves_left.py caption: "about half a minute" became "under half a minute" (22 s here).
- Runs, results: 0.66 defined as the mean of v_4 over the 14 start cells and the most any policy can earn.
- Runs, Fig. 2 paragraph: cut the −3.71 to −0.45 range, "lands between", and the −1.69/−1.57 sentence. Link text became "got one entry for both of its speeds". Added "Neither move is best…" and three sentences on the rings.
- Runs, removal paragraph: cut the 0.20/0.35 sentence, the cell 10 sentence and the 0.34/0.12 sentences. Opened with "Cells 5 and 10 are the only cells in Fig. 1 where no single move is best…".
- Runs: cut the entry-for-entry paragraph.
- Takeaway: cut the two sentences on the mistaken loop. Its last sentence now places the shortfall at cells 5 and 10 and gives the reason.
- moves_left.py: removed the TimeLimit and SlipperyGrid imports, the shortfall and others columns, the largest-estimate grid and the cut_is_terminal comparison. Now 85 lines. Output regenerated, every remaining number unchanged.
- Fig. 2 aria-label (page and figures.py): "sit on or near the exact values" became "sit near the exact values, farthest off for up with 3 moves left, at −1.1 against −0.86".
- Sources: swapped s1 and s2 so they number in order of first citation. Inline cites updated.
- Ran `nb stamp` (words 3,917 to 3,539, 17 to 15 minutes).
- Workspace: code/moves_left.py, code/moves_left.out and code/figures.py synced to the page. fig1.svg and fig2.svg regenerated.

Reruns: both listings extracted from the final page and run in a clean folder
with the earlier lessons' files gave output identical byte for byte to the
printed output. figures.py gave SVGs identical to the page's. I also ran
seeds.py 5 10 0.5, where_lost.py 5 10 0.5, and the time-aware estimates at cell
5 per run for seeds 0 to 9. No new experiment.

Proof: `nb check` gives BLOCK 0, WARN 1 (W-CITE-DENSITY on orientation, no
action per the series direction), PUBLISHABLE.

## Decision

approve. Every claim on the page held on rerun, and the second reader's places
are answered by cuts and corrections, with no explanation the existing runs
cannot support.
