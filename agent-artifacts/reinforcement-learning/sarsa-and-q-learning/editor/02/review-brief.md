# editor brief: reinforcement-learning/sarsa-and-q-learning (02)

Inputs:
- Everything in editor/01's review-brief.md (same files), plus
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/editor/01/editorial-review.md — your first review
- the reader report below — the template's reader check, verbatim (a fresh
  agent given only the built page's text and images, the five earlier lessons'
  text, and press/editorial.md)
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/library/reinforcement-learning/sarsa-and-q-learning.html (source: /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/scratch/article.src.html, built with scratch/build.py)
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/editor/02/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/library/reinforcement-learning/sarsa-and-q-learning.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Follow the lesson template's Reader check section: compare the restatement with
the main-idea sentence, then for each place first ask whether it can be cut, add
explanation only where the main idea needs it, and record the action on each
place. Check why a citation renders as "167". Orchestrator decision on the MIT
Press link: keep it (lessons 3–5 use it; the 403 is a scripted-client block and
the proof's link check passes). Re-run the proof and render at phone and desktop
width in both themes after changes. Say in the review whether your changes
rewrite the central explanation or a whole section (that triggers a second check).

## Reader report (reader check 01, verbatim)

READER REPORT: "Moving at random half the time, Q-learning still learns the optimal arrows"

1. Main idea
SARSA and Q-learning use the same per-move TD update on action values. They differ only in which next-cell estimate goes into the target: SARSA uses the move the agent will actually make, and Q-learning uses the largest estimate. So SARSA's estimates can only settle at the values of the ε-greedy policy it follows, which is the best ε-soft policy and is not optimal at ε = 0.5. Q-learning's estimates can only settle at q*, whatever the agent does. That makes Q-learning off-policy: it learns about the greedy policy while acting ε-greedily, and its own random-moving agent earns slightly less.

2. Where I got lost, worst first
- "Sutton and Barto's pseudocode also orders one step differently ... Rerunning Q-learning in the book's order changed none of the conclusions below." Nothing explains why the timing of the draw could matter: the draw only changes which Q the next choice sees. I can't tell what I'm meant to worry about, and the claim comes with no numbers.
- "Putting π's average itself in the target ... gives Expected SARSA, which George John introduced in 1994 and van Seijen and colleagues named in 2009." The method is named and then dropped. I can't say why it is in a section about resting points, and nothing later uses it. The citation also prints as "167".
- The earnings paragraph: "so the direct solve gives its value exactly." The direct solve I know is for a one-move-per-cell policy on the real grid. The jump to "an ε-greedy policy is the arrows on the P̃ grid, so solve that grid" is only implied. Then "the two runs that aim cell 10 wrong account for the rest": the rest of what? I had to work out that it means the remaining 0.01 of a 0.2 gap.
- "Mean error against q̃ ... 0.08 / 4.92." The metric is never defined (mean absolute? RMS?), so I can't judge whether 0.08 is small.
- "both turn it right when run for longer." "Right" could mean correct or the move right. At cell 10 they happen to be the same move, which makes it more confusing, not less. "Longer" is also unquantified.
- "since an ε-greedy average of four numbers moves by no more than the largest of them moves." The earlier lesson showed only that max is a non-expansion. The step that (1−ε)·max + (ε/4)·sum is also one is left for me to fill in. It's short but terse.
- "Watkins and Dayan prove ... if every pair is updated infinitely often." The lesson never says that the fixed ε = 0.5 behavior policy guarantees this here. I assumed it.
- "For a fixed π the equation has one solution ... So SARSA's estimates can rest only at the action values of the policy that makes its moves." Here π depends on Q itself, so "fixed π" briefly reads as circular. The next paragraph resolves it, but I stumbled first.
- Minor: the headline says Q-learning "still learns the optimal arrows", but Table 1 shows 18 of 20 runs.

3. Skippable sections
- The book-order paragraph about when each method draws its next move.
- The Expected SARSA paragraph, plus the history sentences (Rummery and Niranjan, Watkins 1989).
- Most of "Q-learning's estimates describe an agent that never moves at random". The takeaway's one line, that its agent earns less, is enough. The −7.10, −7.30 and −7.11 counterfactual arithmetic isn't needed for the main idea.
- The Singh et al. and Watkins–Dayan convergence-scope sentences. I can explain where each method rests without them.
- Background and Go Deeper, as labeled.

4. Results reported without saying what they mean
- "Rerunning Q-learning in the book's order changed none of the conclusions below": no numbers, and no reason the order could have mattered.
- "Averaged over the 14 starting cells the gap shrinks to a few hundredths per episode." It doesn't say whether this makes the two methods practically equal or which one is better overall.
- "On seeds 20 to 39 every SARSA run ends on the best ε-soft arrows and every Q-learning run on the optimal ones." It's implied but not stated that this shows the two failures in seeds 0 to 19 were slow convergence, not a different resting point.
- "Its own agent's episodes from cell 9 return about −7.3." It's left to me to see the point: about 6.3 below Q-learning's own estimate of −0.98, so Q-learning's estimates don't predict its own agent's returns. The heading hints at this, but the paragraph never says it.
- Table 1's error rows mean nothing until the next paragraph, and even then the unit is unclear (see item 2).
