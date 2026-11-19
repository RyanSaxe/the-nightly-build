# Editorial review: reinforcement-learning/specification-gaming (editor/03)

This answers the second and last reader check by cutting and correcting text.
No new experiment ran. For place (a) I ran a throwaway value-iteration check
on race.py as printed, as the brief asks. Saved as
`code/checks/check_low_discounts.py`, with its output beside it.

## Correct

The restatement matches the main-idea sentence. It has the reward as written,
the repeatable checkpoint making the loop optimal, the window, Q-learning
reaching the same loop, and the separate task measure. Nothing in the main
idea needed to change.

**(a) Whether the window is about cell 2 or the whole policy.** This was a
correctness fault, and the page now says exactly what is true. The check gives
value iteration's move in every cell at 15 discounts from 0.1 to 0.99, and
whether the greedy agent from cell 0 finishes:

- Cells 0 and 1 point forward at every discount checked. They have to: from
  either, moving back only delays what moving forward collects.
- Inside the window (0.515, 0.6, 0.9, 0.93, 0.937) every cell points
  forward, and the agent from cell 0 finishes.
- Near the lower edge (0.2 to 0.514) only cell 2 points back, and cells 3 to
  6 head for the finish. At 0.1, cells 2 and 3 point back.
- Just above the upper edge (0.938) only cell 2 points back. Cells 2 and 3
  point back at 0.95, and cells 2 to 6 at 0.99.
- Outside the window the agent from cell 0 never finishes at any discount
  checked.

So the window is cell 2's, and it decides the start-state outcome, because
every agent from cell 0 reaches cell 2. Corrections:

- Section title: "The finish wins inside a window of discounts" is now
  "Cell 2 heads for the finish inside a window of discounts".
- The derivation now opens with why cell 2 decides: cells 0 and 1 point
  forward at every discount, so an agent from cell 0 always reaches cell 2,
  and its move there decides whether it ever finishes.
- The limits now say "makes looping optimal from cell 2" and "from cell 2 the
  loop wins there too". A sentence states the low-discount fact the reader
  could not get from Fig. 1: near the lower edge only cell 2's arrow turns
  back, cells 3 to 6 still head for the finish, and an agent from cell 0
  never gets past cell 2.
- Window statement: "finishing from cell 2 is optimal in a window of
  discounts", and "no discount makes finishing from cell 2 optimal" for the
  checkpoint worth 2.
- Fig. 2: the caption now reads "Finishing from cell 2 is optimal above the
  dashed line". The band label in the SVG changed from "finishing is optimal"
  to "finish from cell 2", and the aria-label says the same. Both changes went
  through `figs.py`, regenerated, so figs.html and the page match. Fig. 1's
  caption already said only what holds (each cell's move and value at two
  discounts) and needed no change.
- Takeaway: "finishing is optimal only for discounts between 0.514 and 0.937"
  is now "an agent starting in cell 0 finishes only for discounts between
  0.514 and 0.937, because its move in cell 2 decides". Its "At 0.99, value
  iteration's policy loops from every cell past the checkpoint" holds as
  written.
- The headline is about 0.99, where cells 2 to 6 all loop, so it holds as
  written.

**(b) The forward reference to the pays-once flag.** Cut. The rule function's
docstring in race.py defines the flag. The removal-test paragraph explains it
where it is used: the payment is recorded in the state so the state stays
Markov.

**(c) The reduction to loop or finish.** Corrected in place. The
policy-iteration sentence now draws its conclusion: an optimal policy that
picks one move per cell exists, so comparing those is enough. The case list
missed cell 2 back with cell 1 back, which sits in cells 0 and 1 earning 0.
"or cycles in cells 2 to 6 without crossing anything" is now "or never crosses
again", which covers that case too.

**(d) The constant step size.** I cut the explanation the runs cannot support.
"That condition is there to average out noise in the targets" and the
determinism argument after it are theory the course never taught and the runs
do not show. What remains is what the page can stand behind: learn.py uses a
constant 0.1, which does not meet the proof's condition, so the error column
is the evidence for how close the estimates get. That also removes "lets the
estimates settle", which sat badly beside the third row's 0.116.

**(e) Why the greedy policy ever chose back in cell 0 after the payment.**
Corrected. Q starts at zero, `argmax` breaks the tie toward index 0, and
race.py's BACK is 0. The existing check (check_error_state.out.txt) shows
the greedy choice last taking that move in episode 59 to 508. The sentence
now says the greedy policy takes the move at first, because a tie between two
zero estimates goes to back, and drops it within a few hundred episodes.

**(f) The cell 1 sentence.** Rewritten to say what it explains: in both rows
the values dip from cell 1 to cell 2, because cell 1's forward move collects
the checkpoint.

Sections the reader could skip:

- CoastRunners. Kept, for the reasons in editor/02: it is the commission's
  case, and it shows the published account that the lesson's exact solve
  completes. Its point is no longer left half-said: "That the boat's loop was
  optimal is DeepMind's inference" comes before the sentence on what the race
  can show (evidence record, contradiction 4).
- The window.py paragraph. Kept. It is the run that checks the derivation,
  which the series direction requires, and Fig. 2's band edges come from it.
  It now explains the 42: the grid points from 0.52 to 0.93, inside
  0.514–0.937.
- The step-size paragraph. Cut to two sentences, see (d).
- The race.py listing. Kept. window.py and learn.py import it, and the series
  direction requires printing every file the listings need.

Results reported without saying what they mean:

- "42 of 99". Explained, as above.
- 1.86 > 1. The window sentence now begins "Because the peak is above 1", so
  the checkpoint-2 contrast (peak 0.93) reads as the case with no window.
- The 50 set by the cap. Corrected: each agent crosses on every second move
  until the 100-move limit cuts the episode, so it scores 50.
- CoastRunners' sourcing difference. Explained, as above.

## Reads well

Every change was a cut or a correction to an existing sentence. The added
words make a statement exact or say what a sentence is for, and none
announces or grades itself. The new section title keeps the piece's nouns. It
avoids the "X never/still/only" mold, and its shape differs from the other
three headings.

## The experience

Fig. 2 changed, so I rebuilt the page with nb preview and checked it with
Playwright at 390 and 1280 px in light and dark. "finish from cell 2" sits
between the 0.514 and 0.937 labels without touching either at both widths.
Nothing overflows the page horizontally. Six of six inline math spans render,
with no KaTeX errors. The contents list shows the new title.

Prose on the rendered page is 2,120 words, counted as before. That is up from
2,029, mostly the cell-2 corrections, and under the 2,200 ceiling. Stamp:
4,247 words, 18 minutes, 2 sources.

## Edits

- Orientation: "In both rows cell 1 is worth more than cells 0 and 2, because its forward move collects the checkpoint" to "In both rows the values dip from cell 1 to cell 2, because cell 1's forward move collects the checkpoint".
- Orientation: deleted "A state is the cell plus 8 times a flag that records whether a checkpoint that pays only once has paid. The flag stays 0 until the last row of learn.py tests that checkpoint."
- Discount-window title: now "Cell 2 heads for the finish inside a window of discounts".
- Discount window: added "Cells 0 and 1 point forward at every discount, because moving back from either only delays what moving forward collects. An agent from cell 0 therefore always reaches cell 2, and its move there decides whether it ever finishes."
- Discount window: "still ends at an optimal one, so comparing those policies is enough" to "still ends at an optimal policy, so an optimal policy of that kind exists and comparing those policies is enough".
- Discount window: "or cycles in cells 2 to 6 without crossing anything" to "or never crosses again".
- Discount window: "makes the loop optimal" to "makes looping optimal from cell 2"; "so the loop wins there too" to "so from cell 2 the loop wins there too".
- Discount window: added "Near this lower edge only cell 2's arrow turns back. Cells 3 to 6 still head for the finish, but an agent from cell 0 never gets past cell 2."
- Discount window: "Finishing is optimal only where the curve is above 1, for discounts between 0.514 and 0.937" to "Because the peak is above 1, finishing from cell 2 is optimal in a window of discounts, from 0.514 to 0.937"; "no discount makes finishing optimal" to "no discount makes finishing from cell 2 optimal".
- Fig. 2 caption: "Finishing is optimal above the dashed line" to "Finishing from cell 2 is optimal above the dashed line".
- Fig. 2 SVG, via code/figs.py and regenerated: band label "finishing is optimal" to "finish from cell 2"; aria-label "where finishing is optimal" to "where finishing from cell 2 is optimal".
- window.py paragraph: added "It does at 42 of them, the grid points from 0.52 to 0.93."
- Q-learning step-size paragraph: replaced with "learn.py uses a constant step size of 0.1, not the shrinking N(s, a)^−0.7 used earlier. A constant step does not meet the convergence proof's condition that the squares of the step sizes have a finite sum, so the error column in the output is the evidence for how close the estimates get to q*."
- Q-learning results: "Each one crosses the checkpoint 50 times in its 100 moves and scores 50" to "Each one crosses the checkpoint on every second move until the 100-move limit cuts the episode, so it scores 50".
- Removal test: "a move the greedy policy stopped choosing within a few hundred episodes and only random moves have updated since" to "The greedy policy takes that move at first, because a tie between two zero estimates goes to back, and drops it within a few hundred episodes. Since then only random moves have updated it."
- CoastRunners: added "That the boat's loop was optimal is DeepMind's inference."
- Takeaway: "finishing is optimal only for discounts between 0.514 and 0.937" to "an agent starting in cell 0 finishes only for discounts between 0.514 and 0.937, because its move in cell 2 decides".
- Added code/checks/check_low_discounts.py and check_low_discounts.out.txt.
- Listings unchanged; reran race.py, window.py and learn.py as printed, and each output matches the page.
- Reran nb stamp: words 4247, reading_minutes 18, sources 2.

Proof after the last edit: BLOCK 0, WARN 2, PUBLISHABLE. Both warnings are
W-CITE-DENSITY, on discount-window and q-learning. Those sections hold only a
derivation or the lesson's own runs, which the series direction exempts.

## Decision

approve: every place in the second report is cut or corrected, the
low-discount statements now match value iteration cell by cell, and the
writer has no required change. Per the template, no further reader check
follows.
