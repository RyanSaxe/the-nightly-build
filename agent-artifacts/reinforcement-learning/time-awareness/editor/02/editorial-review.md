# Editorial review: reinforcement-learning/time-awareness (editor/02)

## Correct

Thesis, unchanged: when a time limit belongs to the task, the moves left are part
of the state, so the agent has to observe them and the last move is a
termination. The reader's restatement carries every part of the main-idea
sentence in writer/01/draft-handoff.md: moves left in the state, exact values by
backward induction, a real termination on the last move, and Q-learning reaching
the optimum only with the moves left in its observation. There is no mismatch.
The weak link was the "so" in the sentence: the page never said why the moves
left belong in the state, and never said whether the terminated flag mattered.
Places 1 and 2 of the report are those two gaps.

How the claims held on this pass:

1. Cell 5's best move flips between two and three moves left, and cell 10
   mirrors it. Held. Unchanged from editor/01, and the printed output still
   shows it.
2. The pair with no moves left is terminal. Held, and the page now says what
   depends on the moves made. The slip rule and rewards never do; whether a
   move ends the episode does. I checked this against lesson 1's statement of
   the property (the next state depends on the history only through the current
   state and action) and against termination-and-truncation's "same future at
   any time", which held there because that limit sat outside the task.
3. With the pair observed, Q-learning reaches 0.66 in every run. With the cell
   alone it earns 0.20 to 0.35. Held, but the page's account of where the
   shortfall came from did not add up, as the reader found. "Loses about 2.4
   from that start" covers only the starts in cells 5 and 10, which make up
   0.18 to 0.34 of a 0.31 to 0.46 gap. I wrote a check (code/checks/where_lost.py)
   that gives cells 5 and 10 backward induction's moves and leaves every other
   cell's move as the cell-only table chose it. The gap closes to 0.0000 in
   all 16 runs I tried: seeds 0 to 9 at ε 0.5, and seeds 0 to 2 at ε 0.2 and
   at 1.0. In every run, cells 5 and 10 are the only cells whose one move is
   wrong for some number of moves left. The rest of the gap comes from episodes
   that start elsewhere and pass through those two cells. Cell 9, between them,
   loses most. I put this removal test into moves_left.py as a printed column
   and rewrote the paragraph from its numbers. This narrows the claim to what
   the run shows, and the run supports it fully; nothing here is thin.
4. The cell-only runs learn, entry for entry, the mistaken loop's table. Held.
   The page asserted it and the evidence sat in collapsed output. moves_left.py
   now also prints each cell's largest estimate, averaged over the runs. All 16
   cells match the "cut is terminal" grid that termination-and-truncation
   printed (read with `nb history --show`). The reader's −1.53 against −1.57 is
   two different averages: −1.53 averages each run's larger entry, and run 0's
   larger entry at cell 5 is up while the other four runs' is left. The page now
   says so in one sentence.

The flag question (place 2). I reran p2.py: from a zero start, reporting the
last move as truncated and bootstrapping gives the time-aware return of 0.66.
From a start of 5 it falls to −0.03. code/checks/p2_same.py confirms the
zero-start tables are bit-identical to the terminated ones for seeds 0 to 2. The
bootstrapped term reads a row no update touches, so the equality holds for any
seed. The page now states this in the main text, leaves the working to Problem
2, and says terminated gives the right target whatever the table holds.

The discount (place 5). control.py and estimators.py both use γ = 0.9, and
termination-and-truncation's printed target uses 0.9. The page now gives it in
the first paragraph.

Citations. The Hopper case and the wrapper paragraph are gone, so their
citations went too: s1's Section 2.4 locator, s1's right-column locator, s1's
Section 2 cite in the random-ending passage, and s5, s6 and s7. s8 (Harada) is
now s5. The remaining five hrefs are unchanged from editor/01, and the proof's
link check passes them. I opened the Gymnasium TimeAwareObservation page that
now sits in Go deeper. It returns 200 and carries the anchor and the summary
line the row paraphrases. All five `data-nb-kind="primary"` labels hold as
editor/01 audited them. editor/01's open item about the MIT Press href (s2)
stands as that review left it.

## Reads well

What went, and why:

- The Hopper anecdote in Why this matters. The reader could skip it, and it
  needed a citation. The template's furniture rules say bookends carry none.
  The opening now goes from the kind of task straight to the Markov property.
- The wrapper half of the demo, its paragraph and its output lines. The reader
  could skip it, and its conclusion ("has to count its own moves") overstated
  the case, since a wrapper could remap the flag. TimeAwareObservation is now a
  Go deeper row, which says its inner TimeLimit still reports truncated.
- "Its estimates end 0.11 from the exact values on average." It gave a number
  with nothing to compare it to, and Fig. 2 already shows the estimates beside
  the exact values. The script no longer prints it.
- The random-ending sentences in the closing paragraph: "Seen through the cell
  alone...", the Pardo cite and the link to the equation. The reader could skip
  them, and the entry-for-entry claim does not need them.
- "Here the missing part is the count of moves, which exists only because the
  task has a four-move rule." The new mechanism sentences say the same thing
  exactly, and this sentence descended from the commission's wording.
- The dependency sentence in the runs section's first paragraph. It moved into
  a caption on the moves_left.py listing, inside the collapsed details, beside
  the code it helps run.

What I lifted: the Markov paragraph now works through cell 5. Up lands in cell 1
at any time, but with one move left the agent arrives in a terminal state, and
with three it does not. Problem 1's premise now agrees with the body. The
results now come in the order a reader asks about them: what each observation
earns, why the cell alone can't do better (Fig. 2), where the loss falls, and
what table the cell-only learner built.

Where it still runs against the guide: the shortfall paragraph carries five
numbers (0.20, 0.35, 0.66, 0.34, 0.12). The reader needed them to add up, so
they stay.

No new sentence fails the placeholder test. Headline, dek and headings are
unchanged, so editor/01's comparison with the recent record still applies.

## The experience

The reader check, place by place:

1. What breaks the Markov property: explanation added, three sentences in
   the backward-induction section, plus a clause in Why this matters and the
   takeaway's first sentence. The main idea depends on this step.
2. Whether terminated matters: explanation added, two sentences after the
   target equation. Problem 2 still holds the working. Its question now asks
   why the runs would learn "the same estimates", not "the exact values".
3. Cell-only losses don't add up: rewritten from a new removal test printed in
   moves_left.py. "That start" and "each one makes the move..." are gone.
4. Equivalence asserted: the page now gives the mechanism, the rerun, the
   −1.53 match and the reason it differs from Fig. 2's means.
5. The discount is never given: one sentence in the first paragraph.
6. Fig. 1 appears before its method: moved into the backward-induction section,
   after the sweeps are explained, with the cell 10 mirror sentence. The
   caption no longer says "below".

The skippable passages and the results without meaning are handled under Reads
well and Correct: the wrapper, the Hopper and 0.11 are cut, the dependency
sentence moved, the random-ending sentences cut, the 4–1 split now carries each
choice's return, and the shortfall and the equivalence are now explained.

I built the page with `nb preview` and read it at 390 px in the light theme
through headless Chrome. Fig. 1 now sits under the paragraph that explains
sweeps. Both SVGs are byte-identical to the versions editor/01 and the writer
checked in both themes at both widths, so I did not repeat the dark-theme
captures.

Prose, counted on the rendered page per the lesson identity with editor/01's
counter: 2,183 words with the headline and dek, 2,147 without (editor/01: 2,139
and 2,103). `nb stamp` reads 3,917 words, 17 minutes, 5 sources.

What it gives beyond its sources: the four-move task's exact time-indexed
values on a grid the reader knows, a cell whose best move flips at three moves
left, and two facts about the cell-only learner. It reproduces an earlier
lesson's mistaken table exactly, and all of its loss sits at the two cells
whose best move depends on the moves left. That matches the handoff's
original-work sentence and adds to it. The headline's claim still matches the
hand calculation.

## Edits

- Why this matters: cut the two Hopper sentences and their s1 cite. "the moves already made change the future" became "whether the next move ends the episode depends on the moves already made".
- Background row 01: "the equation for a grid that ends at random" became "the loop that wrongly stops its target at a time limit".
- Orientation: added "Rewards keep the discount of the earlier lessons, γ = 0.9."
- Orientation: moved Fig. 1 and the cell 10 mirror sentence into the backward-induction section.
- Backward induction: cut "and its greedy moves are Fig. 1's arrows". Added "Fig. 1 draws each sweep's greedy moves. Cell 10, below the pit, mirrors cell 5 across the diagonal through the goal and the pit." before Fig. 1.
- Fig. 1 caption: "in moves_left.py below" became "in moves_left.py".
- Backward induction, Markov paragraph: replaced "the number of moves already made is one of those aspects" with the four sentences on what depends on the moves made, worked through at cell 5. Cut the "count of moves ... four-move rule" sentence.
- Terminal pairs: added two sentences on bootstrapping the last move and on terminated.
- Terminal pairs: "It counts the moves left." became "It counts the moves left and returns terminated on the last move."
- four_moves.py: removed the TimeAwareObservation(TimeLimit(...)) demo and its import. Output lost its last two lines.
- Terminal pairs: cut the paragraph on Gymnasium's wrappers (cites s5, s6, s7, s1).
- Runs: moved the dependency sentence into a figcaption on the moves_left.py listing.
- moves_left.py: replaced the "loss from start 2, 7, 5, 10" columns with "shortfall: starts 5, 10", "others" and "5, 10 fixed". Added `fixed()`. Added the printed grid of each cell's largest estimate. Removed the mean |Q − exact| line. 100 lines.
- Runs, results paragraph: cut the 0.11 sentence and the 2.4 sentence. It now ends "The runs that see only the cell earn 0.20 to 0.35."
- Runs, Fig. 2 paragraph: now opens "Fig. 2 shows why, at cell 5" and ends "Whichever move a run picks is wrong for two of the four numbers of moves left."
- Runs: new paragraph after Fig. 2 with each choice's return, the removal test, and the 0.34 / 0.12 split.
- Runs, closing paragraph: cut the random-ending sentences and the s1 cite. Added the mechanism, the rerun and the −1.53 match with its explanation.
- Problem 2: "learn the exact values" became "learn the same estimates".
- Takeaway: added the reason the moves left are state. The cell-only sentence now says where it lost.
- Go deeper: added row 03, Gymnasium 1.4.0 TimeAwareObservation. sb3-contrib is now 04.
- Sources: removed s5, s6, s7, renumbered s8 to s5, set nb-meta sources to 5.
- Ran `nb stamp` (words 3,892 to 3,917).
- Workspace: synced code/four_moves.py, code/moves_left.py and their .out files to the page. Added code/checks/where_lost.py and code/checks/p2_same.py.

Reruns: both listings extracted from the final page and run in a clean folder
with the earlier lessons' printed files; output byte-identical to the printed
output. figures.py: identical SVGs. where_lost.py: seeds 0 to 9 at ε 0.5 and
0 to 2 at ε 0.2 and 1.0. p2.py and p2_same.py: seeds 0 to 2.

Proof: `nb check` with links: BLOCK 0, WARN 0, PUBLISHABLE.

For the orchestrator: these edits extend the lesson's central explanation (the
Markov step and the flag's status are new text no reader has seen) and rewrite
most of the runs section's prose. No section was replaced whole.

## Decision

approve. Every claim held on rerun, and the reader's six places are answered by
cuts, one removal test the page now prints, and explanation added only where the
main idea needed it.
