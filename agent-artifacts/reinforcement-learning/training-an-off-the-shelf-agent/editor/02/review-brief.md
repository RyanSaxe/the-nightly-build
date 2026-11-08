# editor brief: reinforcement-learning/training-an-off-the-shelf-agent (02)

Inputs:
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editorial-direction.md: the standing directions, including the lesson template's Reader check section
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/commission.md: the assignment and its decisions
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/writer/01/brief.md and writer/01/draft-handoff.md: the writer's brief and handoff, with the main-idea sentence
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editor/01/editorial-review.md: your first review
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/writing-coach/01/voice-guide.md: how it sounds
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/researcher/01/evidence.md: the claim set
- library/reinforcement-learning/training-an-off-the-shelf-agent.html: the lesson you edit in place

Output: agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editor/02/editorial-review.md, and the edited lesson
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/library/reinforcement-learning/training-an-off-the-shelf-agent.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This round answers the first reader check, copied below exactly as the reader returned it (the page images were too small for the reader to read, so it worked from the visible text). Follow the template's Reader check section: compare the reader's restatement with the main-idea sentence, and a mismatch means the page changes. For each place, first ask whether the passage can be cut; add explanation only where the main idea needs it; record your action on every place in the review. Hold the page near 2,200 words of prose, cutting whole ideas rather than thinning explanations. You may rerun and change the code in /tmp/claude-0/rl-editor/ and update the page to match, but do not start new experiments for this round beyond what an answer to a place strictly needs. Run `nb stamp` and the proof until BLOCK: 0. Say in the review whether your response changes the lesson's central explanation or rewrites a whole section, because that decides whether a second reader check runs.

Preview: `/home/user/the-nightly-build/nb preview --preview <workspace> --out <scratch-dir>`, then `cd /tmp && node /home/user/the-nightly-build/.nb-work/tools/capture.cjs <scratch-dir> library/reinforcement-learning/training-an-off-the-shelf-agent.html <shots-dir>`.

All relative paths are under /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/.

## Reader check report 1 (verbatim)

The worst problem is that "training curve" means two different numbers and the lesson never says which one Table 1 uses. Second, the recipe for your own environment depends on baseline values that only an exact solve provided. Third, the advice on how many evaluation episodes to run stops before it gives a usable rule.

I worked from the text file. Both page images are shrunk too far to read (1280x9565 shown at 268x2000, 390x13291 at 59x2000), so I read the figures from the text in visible-text.txt.

### 1. The main idea, in my own words

PPO learns a stochastic policy and plays its training episodes by sampling from it. The training curve averages those episodes, so it measures the sampling policy. It does not measure the policy you would deploy: the frozen network taking its most probable move in each cell (the greedy policy).

On SlipperyGrid every policy's value can be solved exactly, so the lesson shows the gap directly:
- For five seeds, the sampled policies are worth 1.36 to 1.43, about what the hand-drawn policy earns.
- The greedy policies of the same networks are worth 1.51 to 1.61. Three are optimal and two are one arrow short.

The curve is also noisy. Its standard error over 100 episodes is 0.86, so its end ranks the seeds badly. Playing the greedy policy in a separate evaluation environment is better, but it takes many episodes:
- Ten episodes (SB3's default) give a standard error of 2.7, more than ten times the 0.25 band between the hand-drawn and optimal values.
- Even 10,000 episodes (standard error 0.09) put seeds 3 and 4 in the wrong order.

The lesson's recommendation: train several seeds, freeze each greedy policy, evaluate it in its own environment, report each seed's number against baselines, and choose the episode count from the gap you need to resolve.

### 2. Where I got lost, worst first

**1. "Training curve" refers to two different quantities.**
> "Its training curve averages the return of the agent's last 100 training episodes. Every return in this lesson is discounted at GAMMA = 0.9 ... In those units seed 0's curve ends at 1.01."

and later:

> "SB3's logged training curve, rollout/ep_rew_mean, averages Monitor's sums over the last 100 episodes. Returns, the wrapper in agent.py, records the same episodes' returns at GAMMA instead."

The title, the opening and Table 1 all say "training curve", and the lesson then explains that SB3's actual logged curve is undiscounted. I have to guess that the 1.01 and Table 1's first column come from the Returns wrapper, not from rollout/ep_rew_mean. The lesson never says so, and it never shows the value SB3 itself logged. So I can't tell whether "the curve scores the sampling policy" is about the curve a practitioner would actually look at, or about a quantity the course built. SB3's warning that the curve "underestimates" performance is about the undiscounted curve, but the lesson tests it against the discounted one.

**2. The recipe for your own environment needs baselines it can't get.**
> "That leaves a recipe for an environment of your own with no exact solve: several seeds, a frozen greedy policy for each, and enough evaluation episodes to place each one between two baselines."

and

> "with each result set between baselines whose values are known."

On SlipperyGrid the baselines (−10.90, 1.36, 1.61) come from exact_value. Without an exact solve I don't know where they would come from. Random moves can be estimated by playing, but there is no hand-drawn policy or optimal value to compare against. The earlier "checking a custom environment" lesson also took its baseline values from the exact solve. So the step from "on SlipperyGrid" to "on your own environment" does not follow.

**3. The episode-count advice stops short.**
> "On an environment without an exact solve, choose the number of evaluation episodes from the gap the comparison has to resolve. Here 10,000 episodes bring the standard error to about a third of the 0.25 band and still cannot tell seed 3 from an optimal seed."

This says what failed, not how to choose the count. The gap that matters here is about 0.06 (seed 3's 1.55 against 1.61). With a standard deviation of 8.5, telling those apart takes on the order of 10^5 or more episodes, and the lesson never does that arithmetic. It also never says whether "the gap" means the 0.25 band or the 0.06.

**4. Why does PPO's network stay so stochastic?**
> "Seed 0's network makes an optimal move the most probable one in every cell, yet in cell 9 a sampled move is optimal only 0.57 of the time."

Fig. 3 shows 0.31 and 0.36 in some cells. The whole lesson rests on the sampling policy staying far from deterministic after 50,000 steps. The lesson says PPO's internals don't matter, but never says why a return-maximizing learner keeps that much probability on non-optimal moves, or whether it depends on the training budget or the defaults. The ε-greedy lesson gives a related picture (the price of exploration), but this lesson doesn't connect to it. As written, the gap looks like an accident of this budget.

**5. The step from Table 1 to "the curve tends to the sampled policy's value" skips a point.**
> "Training episodes are played with sampled moves, so their average return tends to the sampled policy's value and not to the greedy policy's."

The last 100 training episodes were played by the networks of those moments, not by the frozen final network in column 2. The lesson doesn't say whether the network still changed over those episodes, or whether that matters. The spread of the curve's ends (0.45 to 1.94) is put down to noise alone.

**6. I can't say why the DummyVecEnv paragraph is there.**
> "DummyVecEnv steps a list of environments, here a list of one, and resets each one as soon as its episode ends. A later lesson teaches that interface, and none of the code below calls it."

Nothing later uses the auto-reset fact. Background item 08 points to an external SB3 document, not a lesson. Of the Monitor details, only "undiscounted" matters, and only because of problem 1 above.

**7. "Offline" is never explained.**
> "evaluation is performed using a target policy in an offline manner"

"Target policy" is defined in the SARSA/Q-learning lesson, but "offline" is new. A reader with ML background may read it as offline RL, learning from a fixed dataset, which is not what is meant here.

**8. "The policy optimization view" is named in the opening and explained three sections later.**
This is minor, but on first reading it is an unexplained label.

**9. "The last loop of seeds.py aims that one cell up" points at code the reader can't see.**
seeds.py is in a collapsed section. The claim still follows, but the reference is to something not on the visible page.

**10. Problem 1 points the reader to the wrong tool.**
> "SB3's DQN takes a uniformly random move with probability 0.05 ... Start from the price of ε, then solve it with exact_value."

DQN is only named in earlier lessons, never taught. "The price of ε" in the ε-greedy lesson is the loss of the best ε-soft policy. This problem needs the value of the ε-greedy policy around fixed optimal arrows, which the SARSA/Q-learning lesson computes with value_of. The price-of-ε table also has no row for ε = 0.05. A reader may start from the wrong quantity.

### 3. What I could skip, and results reported without their meaning

**Sections I could skip and still explain the main idea:**
- Most of "PPO as a library call": the torch, CUDA, Apple-silicon and thread-count paragraph; the DummyVecEnv paragraph; the Monitor details, except the note that SB3's curve is undiscounted. From the agent.py listing, only move_probs and greedy_moves are needed.
- Background item 08 (VecEnv API vs Gym API).
- The Henderson TRPO/HalfCheetah paragraph. It repeats "seeds differ", which Table 1 already shows.
- The Machado quotes. The two views can be stated without them; they mainly set up problem 2.

**Results reported without saying what they mean:**
- "the same seed trained with one thread and with four ended on different networks": the lesson doesn't say how different (other arrows? other values?) or whether it changes any conclusion.
- "Seeds 5 to 9 ... also end mostly on the optimal arrows, with one seed an arrow short": it doesn't say which seed or cell, the value, or whether evaluation also put that seed in the wrong order.
- "The sampled policies are worth 1.36 to 1.43, about what the hand-drawn policy earns": it doesn't say whether matching the hand-drawn value is a coincidence or means something.
- Henderson's "statistically different" learning curves: no size is given, and nothing ties it to the size of the effects here.
- Seed 3 at 1.59 against seed 4 at 1.50 after 10,000 episodes: the lesson says the order is wrong but not what would fix it, and the takeaway mentions only the 10-episode failure.
- Problem 2 (the highest of EvalCallback's 30 means) points at a bias the main text never discusses. Only Go Deeper item 03 mentions it.
