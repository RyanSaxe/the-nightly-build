# editor brief: reinforcement-learning/action-masking-in-q-learning (02)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/editorial-direction.md (section 5, "Reader check", governs this round)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/commission.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/writer/01/brief.md (the exact writer brief)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/writer/01/draft-handoff.md (holds the main-idea / original-work sentence)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/editor/01/editorial-review.md (your first review)
- The article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/library/reinforcement-learning/action-masking-in-q-learning.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/editor/02/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/library/reinforcement-learning/action-masking-in-q-learning.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

The orchestrator accepts both W-CITE-DENSITY warnings (resting-point, orientation) under the series direction.

This round answers the reader check below (a fresh agent given only the page text and images, the five linked earlier lessons and the reader background). Compare its restatement with the main-idea sentence; a mismatch means the page changes. For each place, first ask whether the passage can be cut; add explanation only where the main idea needs it. Record your action on each place in the review. Say explicitly whether your response changes the central explanation or rewrites a whole section (that triggers a second check). Any listing you change must be rerun exactly as printed with uv run and the page updated to its output. Then nb stamp, full proof to BLOCK: 0, and a rendered check at phone and desktop width, light and dark.

## Reader check report (verbatim)

### 1. Main idea

When legal actions change with the state, Q-learning has to restrict its max to the legal actions as well as its choice of move. If only the choice is masked, illegal moves are never taken, so their estimates keep their initial value Q0. The max in the target still reads those estimates, so the agent ends up solving a different puzzle, one where every state also has a "stop and collect Q0" move. On the four-disk Hanoi puzzle with Q0 = 0, that clamps every legal estimate nine or more moves from the goal at −1, and the greedy agent loops. Two things fix it: masking the max too, or starting every estimate at or below the worst possible value (−10).

### 2. Where I got lost (worst first)

1. Two Gymnasium Taxi documents that seem to disagree. "Gymnasium 1.4.0's Taxi documentation skips that step in its Q-value example, which masks only the choice. The main branch has since fixed the index, though not the target." A paragraph later: "Gymnasium's tutorial on masking in Taxi names the three places: the random choice, the greedy choice and the max in the update." Go Deeper then recommends the Taxi tutorial and adds "Read the main-branch version, whose update also runs on an episode's last step." I can't tell whether the "documentation" and the "tutorial" are different pages, which one masks the target, or what "also runs on an episode's last step" refers to. Nothing in the lesson sets that last point up.
2. The constant step size. "The step size is a constant 0.5, which suits a puzzle with no chance in its moves or rewards." The SARSA/Q-learning lesson said convergence needs step sizes with an infinite sum and a finite sum of squares, and it used N(s,a)^−0.7. A constant 0.5 breaks that condition. The lesson never explains why removing chance makes that acceptable.
3. Fig. 1 uses the label "1 → 0" for two different things. The move being updated is 1 → 0 from state 1. The "max over all six" outline sits on the 1 → 0 column of state 0, which is an illegal move there. The next paragraph says the second target "raises the estimate from −5.88 to −3.44", but the only −5.88 shown is state 0's 0 → 2. On first reading I thought the outlined box or the 0 → 2 box was the estimate being updated, not Q(state 1, 1 → 0).
4. The pessimistic-start rows are left unexplained. "Both learn more slowly than the agents that start at 0, for reasons this lesson doesn't take up." The lesson offers −10 as a way to make the never-updated estimates harmless. Yet those agents end 0.47 from q* and take the fewest moves from only 70.4 of 80 starts, and the takeaway doesn't mention them. I can't tell whether this is a recommended fix, a curiosity, or a warning.
5. A compressed contraction step. "Taking the larger of Q0 and each of two numbers never moves them further apart." I had to rebuild |max(Q0,x) − max(Q0,y)| ≤ |x − y|. "Each of two numbers" reads ambiguously. The value-iteration lesson's non-expansion argument covers the idea, but the sentence doesn't point back to it.
6. Terms the reader never meets: "MaskablePPO, in the sb3-contrib library…", "PettingZoo's classic games…", "Taxi treats a move into a wall the same way, and a pickup or drop-off in the wrong place as a no-op that pays −10", and "the Hanabi Learning Environment's fork of Dopamine". Neither the lesson nor the earlier ones introduce Taxi, PPO, PettingZoo, Hanabi or Dopamine.
7. "Two places" becomes "three places". "Q-learning needs that set in two places" (the choice and the target). Later: "names the three places: the random choice, the greedy choice and the max." I had to reread.
8. The loop is asserted, not traced. "np.argmax breaks a tie toward the first legal move. From the start, that rule leads into the loop." One sentence tracing the four moves would let the reader check it.

### 3. Sections I could skip

- Most of "The environment sends a fresh mask with every observation": the info versus action_masks() conventions (MaskablePPO, PettingZoo), the Taxi comparison, and the int8 versus bool detail in sample(mask=...). The main idea needs only "the environment returns a mask, and step accepts illegal moves as no-ops".
- The Gymnasium Taxi docs aside in "With only its choice masked…" (the index bug and the pull request).
- The OpenSpiel and Hanabi/Dopamine citations, in "Why this matters" and after the masked-target equation.
- The −10 initialization paragraph, as an aside to the main fix.

### 4. Results reported without saying what they mean

- "Ten more seeds solve the start just as fast, though one of those runs takes a move too many from one other start." It doesn't say why, or whether it matters.
- The init −10 rows: error 0.47, fewest 70.4. Called "more slowly" with the reason deferred; not said whether 70.4/80 is a failure or unfinished training.
- The "error rest" column for the target="legal" rows (0.08, 0.47) equals "error q*". Right because the masked target's resting point is q*, but the lesson never says so.
- The hanoi.py output line "sample(mask=...): [1, 1, 1, 0, 0, 0, 0, 0]" is printed with no comment.
