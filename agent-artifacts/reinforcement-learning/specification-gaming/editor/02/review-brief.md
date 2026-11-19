# editor brief: reinforcement-learning/specification-gaming (02)

Inputs:
- every input of editor/01/review-brief.md, plus your editor/01/editorial-review.md
- The reader check report below (first check; reader saw the rendered page with collapsed
  sections closed, the five linked earlier lessons, and press/editorial.md only)
Output: editor/02/editorial-review.md beside this brief
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/library/reinforcement-learning/specification-gaming.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Follow the lesson template's Reader check: compare the restatement with the main-idea
sentence; for each place, first ask whether the passage can be cut; add explanation only where
the main idea needs it; record the action on each place in the review. Keep prose under the
template's ceiling. Rerun listings after any code change, re-stamp and re-prove. If your
response changes the central explanation or rewrites a whole section, say so plainly at the top
of the review, since that triggers a second check.

## Reader check report (verbatim)

READER REPORT: "Looping through a checkpoint worth 1 beats a finish worth 10 once the discount passes 0.94"

1. MAIN IDEA, IN MY OWN WORDS
Value iteration and Q-learning maximize the reward exactly as it is written, not the task the designer meant. In an eight-cell race, a checkpoint that pays every time it is crossed lets the agent bounce back and forth forever. That loop is worth γr/(1−γ²), against γ⁴F for finishing. With r = 1 and F = 10, finishing is optimal only when the discount is between about 0.514 and 0.937. At γ = 0.99 the exact optimal policy is the loop, and Q-learning correctly learns that same loop. That is specification gaming, and you can only catch it with a measure of the task that is separate from the return. Paying the checkpoint only once removes the loop.

2. WHERE I GOT LOST (worst first)

(a) The time-limit paragraph after window.py. I can't tell why it is there, and one claim seems to contradict the table that follows.
"Neither the loop's value nor the finish's contains the race's time limit. The runs below cut episodes at 100 moves with TimeLimit, which is a truncation, and a target that bootstraps there learns the values of the race with no limit, as termination and truncation showed. The discount alone weighs the loop against the finish. With γ = 1 the loop's value is infinite. The loop never ends, and only a policy that never ends needs a discount."
- I can't tell what worry this answers. My guess is "doesn't the 100-move cap limit the loop?", but the lesson never says so.
- "The discount alone weighs the loop against the finish" seems to clash with learn.py's table. There the undiscounted score within 100 moves also favors the loop, 50 against 11. So the loop wins without any discount too, as long as the horizon is long enough.
- The last two sentences jump to γ = 1 and to the earlier lesson's "needs a discount" idea. They don't say what that changes about the race. Is it that the window analysis has no meaning at γ = 1? Or that the comparison only makes sense with γ < 1?

(b) The constant step size in learn.py.
"The race has no randomness, so each target moves only as the estimates do, and a constant step size of 0.1 lets them settle."
- The earlier lessons used N(s,a)^−0.7. They also stated Watkins and Dayan's conditions: the step sizes must have an infinite sum and a finite sum of squares, and a constant step fails the second one.
- The step from "no randomness" to "a constant step is fine" is not explained. I had to work it out myself: the transitions are deterministic and the max-target ignores which move the behavior policy picks, so the target has no sampling noise to average out. The lesson should say this, because it breaks the rule I was taught.

(c) The Krakovna and Turner paragraph. Several sentences leave their point unstated.
"So a run that finishes doesn't show that the optimal policy finishes. The exact solve does. Turner argues that a trained deep RL agent need not pursue its reward, since general agents fail the convergence theorems' conditions, such as trying every action. On the race every move keeps being tried in every cell."
- I can't say why Turner is brought in. The final sentence only hints at the conclusion: Turner's caveat does not apply to this tabular case, so here the agent really does pursue the reward. The lesson should state that.
- "So a run that finishes…" is only a weak consequence of "a weaker algorithm might miss an intricate solution". It also reads as a side point, away from the lesson's argument.

(d) The forward reference to the flag in the state.
"A state is the cell plus 8 times a flag that stays 0 until a test later in the lesson."
- I could not tell what the flag is for or what "a test" means. That only became clear at the third row of learn.py, many screens later.
- One clause such as "(it records whether a pay-once checkpoint has paid; used later)" would fix it.

(e) The peak location is given without the step behind it.
"In between, the left side peaks where γ² = (D − 2)/D, and the peak is 1.86 for this race."
- Setting the derivative of γ^(D−2)(1−γ²) to zero gives this. That step is easy, but it is not shown or even named, so the number appears from nowhere.

(f) Restricting to three options from cell 2.
"The optimal policy picks one move per cell, as value iteration's greedy policy does, so from cell 2 it either loops, finishes, or cycles in cells 2 to 6…"
- The earlier lessons show the greedy policy is deterministic. They never say an optimal policy can always be taken as deterministic and stationary.
- The lesson also doesn't show that the 1↔2 back-and-forth is the only cycle that pays. That holds because a deterministic policy has one move per cell, but I had to check it myself.

(g) Notation switches between the text and Fig. 2.
- The derivation and the legend use γ^(D−2), and the Fig. 2 caption writes γ³. They are the same with D = 5, which the reader has to notice.
- The takeaway likewise writes γ⁴F where the text wrote γ^(D−1)F.

(h) The Popov reference in Problem 1 is unexplained.
"Like the grasping reward that kept Popov and colleagues' simulated arm from stacking a brick, it pays for being partway there."
- Neither this lesson nor the earlier ones say what that grasping reward did or how it stopped the stacking. The comparison means nothing without that.

3. SECTIONS I COULD SKIP AND STILL EXPLAIN THE MAIN IDEA
- "Positive-reward cycles in CoastRunners and on a bicycle". The whole section is illustration and history. The only term it adds is "positive-reward cycle", and the main idea doesn't need it.
- The Krakovna and Turner paragraph inside the Q-learning section, from "Krakovna and colleagues trace such behavior…" to "…in every cell."
- The window.py paragraph and its output. They confirm the formula against value iteration, but Fig. 2 and the derivation already carry the idea.
- The Sutton and Barto chess paragraph at the end. It is a pointer to a later lesson.

4. RESULTS REPORTED WITHOUT SAYING WHAT THEY MEAN
- The third row's largest error: "The third row's largest error, 0.116, is in cell 0 after the payment, reached only by backing past the checkpoint." The lesson says where the error is, but not why that state lags (it is rarely visited, so it gets few updates) or why it doesn't matter (the greedy moves still match q* in 5 of 5 runs). The reader is left to decide whether 0.116 is a problem.
- Fig. 1 at γ = 0.99, cells 0 and 1 (49.75 and 50.25), and at γ = 0.9, cell 1 being worth more than cell 2 (6.90 against 6.56). The page prints these without a word on why the values aren't monotone along the lane. The reason is that the crossing pays 1.
- learn.py "largest |Q − q*| 0.000" in the first two rows. The text says "within 0.001 of q*" but doesn't say which states that maximum covers. The paid-flag states are included in the third row, and it is unclear whether they are in the first two.
- The headline threshold, "once the discount passes 0.94". The lesson also finds that the loop wins below 0.514, and the headline never says that. The takeaway gives the full window, but the headline result alone suggests one threshold.
