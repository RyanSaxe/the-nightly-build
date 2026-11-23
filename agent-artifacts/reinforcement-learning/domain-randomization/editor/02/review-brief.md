# editor brief: reinforcement-learning/domain-randomization (02)

Inputs: as in /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/01/review-brief.md, plus
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/01/editorial-review.md — your first review
- the reader-check report, copied below
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/02/editorial-review.md (a new review; do not append to 01)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Where something you need is missing, ask me.

Follow the "Reader check" section of press/templates/lesson/identity.md (in
the editorial direction). Compare the reader's restatement with the main-idea
sentence; for each place, first ask whether the passage can be cut, add
explanation only where the main idea needs it, and record the action on every
place in the review. You may rerun the lesson's code but start no new
experiments; cut any explanation the existing runs cannot support. Pay
particular attention to item 1 (undiscounted return: give the reason the
existing runs support, or cut the uniqueness claim), item 4 (the --no-limit
removal test is commissioned as the check on the causal claim; keep a removal
test but make the page say plainly what it does and does not show), and the
cut-off output line. Stay inside the template's prose band. Restamp and rerun
the proof to BLOCK: 0, and look at the rendered page again.

## Reader-check report

# Reader report: "A cart that can't see its load brakes for the heaviest one"

## 1. Main idea in my own words

Suppose a physical parameter is drawn again at every reset and the observation leaves it out. Then a policy of the observation has to make one move per observation for every value of the parameter. In LoadedDock the load's mass never changes the motion. It changes only the reward at the dock, where the cart crashes if ½mv² > 0.5 J. The path distribution is the same for every mass, so the return averaged over masses equals the return in one ordinary MDP, the "averaged Dock". Its docking reward is the probability-weighted average of the per-mass rewards. That MDP's optimal policy is the best a mass-blind policy can do, which is the middle term of the held-out-levels bound. Here the policy docks at the heaviest training load's safe speed. Lighter loads therefore lose time (0.22 s at 1 kg), and loads heavier than the training range crash. A policy that sees the mass gets each load's own optimum, the right-hand term. Tabular Q-learning with the mass hidden ends on the averaged Dock's policy. The mass can't change which states get visited, so every share in equation (4) is fixed at ¼, and equation (4) becomes the averaged Dock's Bellman optimality equation.

## 2. Where I got lost (worst first)

**1. Dropping the discount removes the only uniqueness argument I have.**
"The return drops the discount: it is minus the seconds until the episode ends…" / "…the averaged Dock's optimal policy, and value iteration finds it." / "…so its estimates rest at the averaged Dock's optimal action values, as Q-learning's did on the grid of the SARSA and Q-learning lesson."
- The lesson gives no reason for dropping the discount. The action-frequency lesson set the discount per second. Pitch dropped it because its episodes end within nine steps, but Dock episodes can run to the 20 s limit.
- The SARSA and Q-learning lesson argued that q* is the *only* resting point because the backup "shrinks gaps by γ". With γ = 1 that argument no longer holds, and this lesson doesn't replace it. So I can't confirm that value iteration finds the averaged Dock's optimum, or that Q-learning has only one place to rest.
- The earlier lessons only name value iteration, as "value iteration's backup", and never describe it. exact.py, the script that runs it, is collapsed on the page.

**2. The held-out masses aren't held out in the earlier lesson's sense.**
"Here the policy is safe only up to the heaviest load it was built from, so a held-out range of masses tests it, as held-out levels tested a policy trained on levels."
Held-out levels came from the same generator as the training levels, so held-out return estimated return on the training distribution. 5 kg and 6 kg lie outside the 1–4 kg range, so this tests extrapolation, which is a different question. The "as" comparison doesn't hold. The result is also known before anything runs: the policy arrives at 0.49 m/s, and the table's limit column gives 0.45 and 0.41.

**3. "Best for all" means two different things a few lines apart.**
"so the best policy of (x, v) for all four loads is the averaged Dock's optimal policy" means best *average* return. "It is zero at every load only if one policy is best for all of them" means best for *each* load separately. On first reading I took the first sentence to say one policy is best for every load, which the next section contradicts.

**4. The --no-limit run can't come out any other way.**
"Without the rule, LoadedDock's mass changes nothing at all."
loads.py uses the mass only in the crash check. With `limit=False` the mass is unused, so every row has to be identical. I can't say why this run is there. If it is meant to show the opening's claim ("gives up return at a value only where the best move depends on the parameter"), it doesn't. That would need a case where the mass still changes the reward but not the best move. Removing the mass's only effect doesn't show that.

**5. The opening's motivation is never demonstrated.**
"No one knows a real cart's load exactly, and a policy tuned to one guess can fail with another. One answer is to train on a range of values."
The lesson compares the randomized policy only with policies that see the mass. It never shows a policy tuned to one mass failing on the others. For example, the 1 kg policy arrives at 0.91 m/s and would crash the 2–4 kg loads; the table shows this, but the text never says it. So the lesson states what randomization costs but not what it buys.

**6. Why the observation has to be exact integers is left unstated.**
"The observation reports the exact state as two integers, and a table keyed on it has one entry per state."
I had to work out two reasons:
- qlearn.py's `key()` applies `int()` to each component, which would truncate a float position.
- With one entry per (x, v), the only states behind an entry are the four masses. That is what lets equation (4) reduce to the averaged Dock later. In the action-frequency lesson, each cell averaged over many states.

The Q-learning section depends on this, so the sentence should say it.

**7. Skipped steps at the fork (section 1).**
- "If it pushes right, the 4 kg load can't slow from 1 m/s to 0.5 m/s in the 0.3 m left." I had to compute this myself: one push from (0.605, 0.9) gives (0.7, 1.0), and braking to 0.5 m/s needs 0.375 m.
- "If it brakes, and goes on braking for the 4 kg load…" The 4 kg path pushes once more near the dock, so "goes on braking" isn't literal. It means "follows the 4 kg path".
- "Losing 0.22 s with one load costs far less than a crash with the other" weighs two loads, but the real draw has four.

**8. Minor wording and labels.**
- **Terms introduced and never used.** "Moving a policy from simulation to a robot is called sim-to-real transfer" is never used again in the body. "Drawing a physical parameter like this mass at every reset is called domain randomization" repeats the definition already given in "Why this matters".
- **Move names switch.** Section 1 says "The 1 kg load's best move is right, and the 4 kg load's is left". The rest of the lesson, train.py's output and Fig. 3 use "push" and "brake". That brake means pushing left comes only from the answer to the action-frequency lesson's Problem 1.
- **The "arrives" column has no unit.** In exact.py's output it is arrival speed (1 kg: 0.91, docking at 1.29 s). In the --no-limit table it reads 1.26 next to prose saying "docks after 1.26 s". Speed and time coincide from rest at 1 m/s², so I briefly couldn't tell which one the column was.
- **Fig. 3 caption and colors.** The caption says "The solid bar in each pair is the entry's greedy move", but every bar is filled; the greedy one is just darker. Nothing says that blue means brake and brown means push.
- **Cut-off output line.** In the page-06 screenshot, train.py's line "…and runs that brake" stops at "runs that br" because the code block overflows.

## 3. Sections I could skip and still explain the main idea

- The history paragraph: Tobin, Rajeswaran, Sadeghi and Levine, Peng, and sim-to-real.
- The loads.py listing and its "check_env passed" output. The prose already gives every rule the lesson uses. Only one sentence is needed, on exact integer observations.
- The --no-limit run and its table (item 4).
- The paragraph and rows on the 5–6 kg held-out masses. The main idea doesn't need them, though the takeaway repeats them.
- Mostly, the mass-observed half of train.py. exact.py already gives each load's own best, so this half confirms rather than adds.

## 4. Results reported without saying what they mean

- **"check_env passed for both observations."** Nothing says what passing establishes. The background lesson's title, "Gymnasium's environment checker passes a grid with a backward slip", suggests passing says little about the dynamics.
- **"Following the 3 kg load's path instead would bring every load in 0.08 s sooner and crash the 4 kg load, and that crash costs 2 once in every four episodes."** The comparison is left to the reader: +0.08 per episode against −0.5 per episode on average, so braking for 4 kg wins. That conclusion is the paragraph's point, and the paragraph doesn't state it.
- **exact.py's held-out cost column, 1.96 and 1.91.** These values are never explained. Each is the crash penalty of 2 minus the 0.04 s or 0.09 s by which the averaged policy arrives sooner than that load's own best. The column mixes seconds with the crash penalty without saying so.
- **"The hidden agent's and the 4 kg entry's estimates for pushing differ from exact.py's values by up to 0.09. Pushing is the wrong move at both, and the agents push there only when they explore."**
  - Pushing is also wrong at 3 kg and gets explored just as rarely, yet that estimate matches exactly (−2.36 against −2.36). The stated cause doesn't explain the difference.
  - The two errors also go in opposite directions: the hidden agent's −1.51 is below −1.47, and the 4 kg entry's −2.27 is above −2.36.
  - The text doesn't say whether the errors matter beyond the ranking of the two moves being right.
