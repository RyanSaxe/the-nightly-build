# editor brief: reinforcement-learning/domain-randomization (03)

Inputs: as in /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/01/review-brief.md, plus
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/02/editorial-review.md — your second review
- the second (final) reader-check report, copied below
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editor/03/editorial-review.md (a new review)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Where something you need is missing, ask me.

This is the second and last reader check; no further check runs. Per the
template's Reader check section, answer this report by cutting or correcting
text. You may rerun the lesson's code but start no new experiment, and cut any
explanation the existing runs cannot support. Record the action on every place.
Orchestrator decisions:
- Item 1: value iteration's convergence without a discount is not established
  by the uniqueness paragraph. Either state the step the page can support from
  its own facts (finite reachable states, every move costs 0.1 s, so every
  policy that ends episodes has finite value), or narrow "value iteration finds
  it" to what the run shows (it settled, and its fixed point solves the equation,
  which has one solution). Tighten or cut the uniqueness paragraph so every step
  it uses is on the page.
- Item 2: the commission's removal test may be reduced to a sentence plus the
  flag and its printed line if that is all it supports; cutting the separate
  section is acceptable.
- Item 4: say in a sentence why the hidden agent's entry is not the average of
  the per-load entries, linking the frame-stacking lesson's point, or cut the
  invitation to compare them.
Stay inside the template's prose band. Restamp and rerun the proof to BLOCK: 0
and look at the rendered page again.

## Reader-check report (second)

# Reader report: "A cart that can't see its load brakes for the heaviest one"

## 1. The main idea, in my words

Domain randomization draws a simulator parameter at every reset. Here the parameter is the load's mass, 1 to 4 kg, and the agent can't observe it, so its policy has to make one move per (x, v) for every mass. In LoadedDock the mass doesn't change the motion. It only decides whether the dock crashes the cart: above 0.5 J of kinetic energy, the arrival costs −2. A policy of (x, v) therefore produces the same paths for every load, and averaging the reward over the loads turns the problem into one ordinary MDP, the "averaged Dock". Its optimal policy is the best policy that can't see the mass, which is the middle term of the held-out-levels bound.

That policy only loses return at states where the best move depends on the mass. On this task it brakes for the 4 kg load, which costs the 1 kg load 0.22 s and the 4 kg load nothing. Q-learning without the mass ends on the same policy. Because the mass never changes where the cart goes, equation (4)'s shares are fixed at ¼ under any policy, so the equation where its estimates rest is exactly the averaged Dock's Bellman optimality equation. An agent that sees the mass gets each load's own optimum.

## 2. Where I got lost, worst first

**1. The paragraph on the undiscounted Bellman equation.**
> "With no discount, the backup no longer shrinks gaps by γ ... The cost of time takes its place. In any solution, a value equals its best move's reward plus the next value, so values rise by 0.1 along best moves. Those moves never revisit a state, so they end the episode, and each value is one path's return. The equation also puts each value at or above every finished path's return, so only the optimal values solve it."

- "The cost of time takes its place" doesn't state a step. I only understood it after reading the next three sentences.
- Three steps are left out:
  - "never revisit a state" needs the values to strictly increase along best moves.
  - "so they end the episode" needs a finite set of reachable states. That fact only appears a paragraph later ("exact.py lists every state the cart can reach").
  - "at or above every finished path's return" comes from V(s) ≥ r + V(s′) for every move, added up along the path. The paragraph doesn't say so.
- **The larger gap:** the paragraph shows the equation has only one solution, but the sentence before it says "value iteration finds it." The value-iteration lesson's only reason for convergence was the γ-contraction, and this paragraph says that contraction is gone. Having a single solution doesn't show that value iteration converges to it. The only support offered is "Its values stop changing long before the 500th sweep."
- The paragraph never says what it's for. Its result is used two sections later ("the equation's one solution"). It is also proved for state values and then applied to action values without comment.

**2. The `--no-limit` paragraph.**
> "It can't show that a mass changing the reward but not the best move costs nothing, since removing the rule removes both. That rests on the derivation..."

- I can't tell what "both" refers to. I think it means the mass's effect on the reward and its effect on the best move.
- The paragraph has just said "this run could come out no other way," so I couldn't say what the run adds beyond checking the code.
- The section's title, "Only the buffer's rule makes the light loads pay," is true by construction: the first section already said "the mass never changes how the cart moves." So the section reads as a demonstration of one of the lesson's own premises.

**3. Why the policy that can't see the mass brakes at (0.605, 0.9).**
> "Following the 4 kg load's path instead costs the 1 kg load 0.22 s and the 2 kg and 3 kg loads less, so the better move is to brake."

- The comparison that makes this "so" follow is left to me: pushing costs an expected 1 in crashes, while braking costs at most 0.22 s per load.
- The costs for the 2 kg and 3 kg loads (0.14 and 0.08 s) only appear later, in exact.py's table.
- The argument covers push against brake at one state only. It never says why the averaged policy doesn't crash just the 4 kg load instead: a ¼ chance of −2 is 0.5 on average, still more than 0.22 s.
- As a result, "the policy brakes for the heaviest" in the next section is read off the table, not explained.

**4. The estimates for the agent that can't see the mass are not the average of the per-load estimates (train.py output, Fig. 3).**

- Fig. 3 puts the single entry of the agent that can't see the mass next to the four per-load entries, which invites reading the first as the average of the others. It isn't:
  - For brake, the entry is −0.61, but the per-load entries average −0.52.
  - For push, exact.py gives −1.47, but the per-load values average −1.40.
- I had to work out the reason myself. After the move, the agent that can't see the mass follows one shared policy, the averaged Dock's, not each load's own best. This is the frame-stacking lesson's point that equation (4) is not the share-weighted average of the hidden states' values, but this lesson never connects to it.

**5. The estimates that miss exact.py's values.**
> "Two estimates for pushing miss exact.py's values by up to 0.09, the hidden agent's low and the 4 kg entry's high, and these runs don't show why."

- "the hidden agent's low and the 4 kg entry's high" is hard to parse. It means the estimate for pushing is 0.04 too low for the agent that can't see the mass, and 0.09 too high in the 4 kg entry of the agent that can.
- The sentence comes right after the claim that the estimates "can rest only at" the exact values. It doesn't say whether the misses mean the runs haven't converged on a move that only exploration tries, or something else.
- The 3 kg and 4 kg entries for pushing share an exact value (−2.36) and the same motion, yet only the 4 kg entry misses. The lesson doesn't comment.

**6. "Its values stop changing long before the 500th sweep."**
The number 500 appears nowhere else on the visible page, because exact.py is collapsed. I inferred that the script runs a fixed 500 sweeps.

**7. "Arriving at 0.63 m/s pays −1 there on top of the time."**
At this point I don't know why the example uses 0.63. It turns out to be the 2 kg load's own best docking speed, which only appears in the table further down.

**8. "...two integers, which survive the int() that qlearn.py's key() applies."**
The lesson doesn't say why this matters. Dock's float observations would be cut by `int()` to 0 or 1 and collapse the table into a few shared entries. I had to recall `key()`'s code from the frame-stacking lesson to see it.

**9. Minor wording:**
- "That policy gives up return at a value only where..." In an RL lesson, "a value" first reads as a value function. It means a value of the parameter.
- Problem 2's "1/m m/s²" puts the mass m and the unit m (metres) side by side.

## 3. Sections I could skip and still explain the main idea

- **The history paragraph** (Tobin; Rajeswaran; Sadeghi and Levine; Peng). It also interrupts the argument, sitting between the reasoning at (0.605, 0.9) and the code.
- **The loads.py material:** the paragraph on the 5 mm grid, `int()` and the seed, the code itself, and the `check_env` output.
- **The `--no-limit` run and its output.** The lesson itself says it "could come out no other way."
- **"Training on a single light guess would be worse..."** It is good motivation but not needed for the argument.

## 4. Results reported without saying what they mean

- **"Two estimates for pushing miss ... and these runs don't show why."** The lesson gives the discrepancy and explicitly doesn't interpret it. That leaves the reader unable to square it with "can rest only at the averaged Dock's optimal action values."
- **"Its values stop changing long before the 500th sweep."** Convergence is asserted, but no sweep count or remaining change is shown. The lesson also doesn't say what this tells us about value iteration without a discount, the one thing the theory paragraph above it didn't establish.
- **In the train.py table, the exact values for the agent that can't see the mass** (brake −0.61, push −1.47) are used only to rank the two moves. The lesson never says what −1.47 is: a push followed by the averaged Dock's best continuation, which still crashes the 3 kg and 4 kg loads. It also never says why −0.61 equals the 4 kg entry.
- **The `--no-limit` table.** The lesson says the run confirms "nothing else in the code makes the loads pay." That is a check on the code. The same paragraph says the run can't test the lesson's claim, so I'm left unsure what the result means for the main idea.
- **The exact.py table's own-best speeds** (0.91, 0.63 and 0.57 m/s, against limits of 1.00, 0.71 and 0.58). The gap below each limit is never explained. I assume it comes from deciding only every 0.1 s.
