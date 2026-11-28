# editor brief: reinforcement-learning/time-awareness (02)

Inputs: the same as editor/01/review-brief.md, plus
- agent-artifacts/reinforcement-learning/time-awareness/editor/01/editorial-review.md (your previous review)
- the reader-check report below
Output: agent-artifacts/reinforcement-learning/time-awareness/editor/02/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/time-awareness/library/reinforcement-learning/time-awareness.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This is the lesson identity's reader check, round 1. Compare the reader's restatement with the main-idea sentence in writer/01/draft-handoff.md; a mismatch means the page changes. For each place, first ask whether the passage can be cut; add explanation only where the main idea needs it; record your action on each place in the review. Any number you add or change comes from a rerun (interpreter: /tmp/claude-0/-home-user-the-nightly-build/5b359343-5f83-54c8-830a-95e63a934217/scratchpad/rlenv/bin/python). Keep prose under about 2,200 words. Tell me in your report whether your response changed the lesson's central explanation or rewrote a whole section (that triggers a second reader check).

## Reader report (verbatim)

### 1. Main idea
When the time limit is part of the task (earn as much as possible in four moves), the number of moves left is part of the state. Backward induction gives the exact values. The last move is a real termination. Tabular Q-learning reaches the optimal return only if its observation includes the moves left. With the cell alone, one table entry has to stand for four different values, and the agent picks the wrong move at cells 5 and 10.

### 2. Where I got lost (worst first)
1. What exactly breaks the Markov property is never stated. "So the state is the pair (cell, moves left), and the cell alone breaks the property." Problem 1 then says "The slip rule and the rewards don't depend on the moves left". The two-flags lesson argued the opposite: "an agent in S_T faces the same future at any time". If neither the slip rule nor the rewards depend on time, what does? The only thing that depends on time is whether the episode ends. Lesson 1 states the property in terms of the next state, so the lesson needs one sentence saying that "the episode ends here" is part of the next state's distribution, and that this is what the cell cannot predict.
2. Why the terminated flag matters is left unclear. "A pair with no moves left is terminal" and the wrapper paragraph ("To report it as terminated, the environment has to count its own moves") present terminated as essential. Problem 2 then asks: if the last move came back truncated and the learner bootstrapped, "Why would the runs still learn the exact values". The answer is collapsed, so the main text never settles whether the flag is required or just good practice (guess: it works only because zero-moves-left rows stay at 0).
3. The cell-only losses don't add up. "Each one makes the move that is best with one or two moves left at cell 5, cell 10 or both, and loses about 2.4 from that start." Losing 2.4 at one or two of 14 starts costs 0.17–0.34 of mean return, but the gap from 0.66 to 0.20–0.35 is 0.31–0.46. The stationary cell-only policy also errs when episodes from other starts pass through cell 5 or 10 with few moves left; never said. The run that picks up at cell 5 contradicts "each one makes the move that is best with one or two moves left". "that start" is ambiguous.
4. The equivalence with the mistaken loop is asserted, not shown. "The cell-only runs learn, entry for entry, the table the mistaken loop learned..." No numbers compared (the two-flags lesson printed cell 5's largest estimate −1.53; here left −1.57).
5. The discount is never given. −0.86 only comes out at γ = 0.9. The lesson never says the four-move task is discounted or at what rate; an undiscounted sum would be the natural reading.
6. "Fig. 1 … from backward_induction in moves_left.py below" points to a collapsed listing two sections later; the figure shows backward-induction results before backward induction is explained.

### 3. Skippable / results without meaning
Skippable: the Gymnasium wrapper half of the demo (TimeAwareObservation(TimeLimit(...)) lines, last two output lines, the paragraph "The last two lines of output come from…"; its conclusion "has to count its own moves" is overstated — you could remap the flag); the Hopper anecdote in Why this matters; the file-dependency/runtime sentence; the closing "grid that ends at random" paragraph.
Results without meaning: "Its estimates end 0.11 from the exact values on average" (over which pairs? is that close?); "Four runs choose left and one chooses up" (cost of each?); "The runs that see only the cell earn 0.20 to 0.35" (shortfall unexplained, see 3); "entry for entry" claim has no evidence (see 4).
