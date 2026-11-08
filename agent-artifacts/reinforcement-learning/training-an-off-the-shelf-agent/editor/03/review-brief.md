# editor brief: reinforcement-learning/training-an-off-the-shelf-agent (03)

Inputs:
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editorial-direction.md: the standing directions, including the lesson template's Reader check section
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/commission.md: the assignment and its decisions, including "Decisions after editor/02"
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editor/02/editorial-review.md: your previous review
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/writing-coach/01/voice-guide.md: how it sounds
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/researcher/01/evidence.md: the claim set
- library/reinforcement-learning/training-an-off-the-shelf-agent.html: the lesson you edit in place

Output: agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editor/03/editorial-review.md, and the edited lesson
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/library/reinforcement-learning/training-an-off-the-shelf-agent.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This round answers the second and last reader check, copied below exactly as the reader returned it. The reader's restatement matches the main-idea sentence in the commission. Under the template's rule for a second report, answer it by cutting or correcting text. You may rerun the lesson's existing code in /tmp/claude-0/rl-editor/, but start no new experiment, and cut any explanation the existing runs cannot support. For each place, first ask whether the passage can be cut. Record your action on every place in the review. Two places need a correctness decision, not only clarity: place 1 (whether "target policy", as the Q-learning lesson defines it, is the right term for the greedy policy of an on-policy learner like PPO) and place 4 (whether the 10,000-episode figure follows from the paragraph's own rule for an environment where the baseline is also estimated). Bring the prose back toward 2,200 words. Run `nb stamp` and the proof until BLOCK: 0.

Preview: `/home/user/the-nightly-build/nb preview --preview <workspace> --out <scratch-dir>`, then `cd /tmp && node /home/user/the-nightly-build/.nb-work/tools/capture.cjs <scratch-dir> library/reinforcement-learning/training-an-off-the-shelf-agent.html <shots-dir>`.

All relative paths are under /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/.

## Reader check report 2 (verbatim)

READER REPORT: "PPO's greedy arrows outscore the sampled moves its training curve averages"

Files read: visible-text.txt, all 7 page tiles, reader-background.md, and the earlier lessons. I read checking-a-custom-environment, termination-and-truncation, epsilon-greedy-exploration and sarsa-and-q-learning in full. I only searched finding-optimal-policies and the rest for specific terms.

### 1. Main idea in my own words

PPO trains by sampling each move from a stochastic policy, so its logged training curve (mean return of the last 100 training episodes) measures that noisy sampling policy. Once training stops, you would deploy the frozen network's most probable move in each cell, the greedy policy, and that is a different and better policy. On SlipperyGrid both can be solved exactly. Five seeds' sampled policies are worth about the hand-drawn baseline (1.36–1.43). Their greedy policies are near or at optimal (1.51–1.61). The curve is also too noisy (SE 0.86) to say even that.

So the lesson's advice is to evaluate the greedy policy in a separate environment, per seed, next to random and scripted baselines. Choose the number of episodes from the smallest gap you need to resolve, n ≥ (3σ/d)². Ten episodes (SE 2.7) cannot separate hand-drawn from optimal. Even 10,000 episodes (SE 0.09) put a one-arrow-short seed above an optimal one, because that gap (0.06) needs about 180,000 episodes.

### 2. Where I got lost (worst first)

**1. "Target policy" contradicts the earlier lesson.**
> "The policy optimization view scores the agent's target policy in an evaluation kept apart from learning"

The Q-learning lesson defines the target policy as the policy the agent learns about, and says on-policy methods learn about the policy that makes the moves. Nothing here says whether PPO is on- or off-policy. If PPO is like SARSA, its target policy is the stochastic sampling policy, which is Table 1's middle column, not the greedy column the lesson calls the target. The link "target policy" sends me to a definition that points to the other column. I can't tell why the greedy policy counts as PPO's target policy, or why the greedy policy rather than the sampled one is "the one put to use".

**2. Does the curve score the frozen sampling policy or not?**
> "Training episodes are played with sampled moves, so their average return tends to the sampled policy's value. PPO updates its network once per batch of 2,048 training steps, and in every seed the last 100 training episodes fall inside the last batch, played by the network before PPO's final update. Table 1's other two columns solve the frozen network itself, so the gap between them does not rest on the curve."

- The first sentence supports the headline claim.
- The second sentence says the curve's episodes came from a *different* network (before the final update). That seems to weaken the claim, but the lesson never says by how much.
- I can't say why the third sentence is there. Which "gap between them"? Sampled vs. greedy? Then why mention the curve at all?

Meanwhile Table 1 does not obviously match "the curve tends to the sampled value". Seed 1's curve is 0.45 against a sampled value of 1.41. Seed 4's is 1.94, above even its greedy 1.61. The next paragraph blames noise. But the lesson promised that "the warning can be checked here", meaning SB3's warning that the curve "underestimates the agent's true performance". It never says whether the check passed. With seed 4 above the greedy value, I can't tell what the verdict is.

**3. The Machado quote is never answered.**
> "It can also give a high score to an agent that explores throughout training and exploits only when it is evaluated."

This is a criticism of exactly the protocol the lesson then recommends: train stochastically, evaluate greedily. The lesson quotes Machado, picks Henderson's other view, and never says why the criticism doesn't apply or when it does. I can't say why the paragraph is there, other than as a counterpoint that is left hanging.

**4. The episode-count rule doesn't follow from what came before.**
> "The lesson on checking a custom environment flagged a gap once it passed 3 standard errors... so a gap d needs n ≥ (3σ/d)² episodes, twice that when both means are estimated. Telling an optimal seed from the hand-drawn policy here means a gap of 0.25, which takes (3 × 8.5 / 0.25)², about 10,000 episodes"

- The paragraph is about "an environment of your own, with no exact solve". There the hand-drawn baseline is also played, so by the lesson's own clause the answer should be about 20,000, not 10,000. The 10,000 fits only the SlipperyGrid case, where hand-drawn is exact.
- σ = 8.5 is the greedy policy's spread. The earlier lesson measured the hand-drawn policy's sd as 8.79.
- In the earlier lesson, the 3-SE rule was a threshold for flagging a mismatch. Here it is reused as a sample-size rule. If the true gap is exactly 3 SE, the observed gap clears 3 SE only about half the time. Nobody explains why this threshold is enough to "tell" two policies apart.

**5. Why a separate environment?**
> "Because most algorithms use exploration noise during training, you need a separate test environment"

Exploration noise is a property of the policy, and the greedy policy already removes it. On SlipperyGrid the environment's only state is its random number generator. I can't see what a second SlipperyGrid with its own seed protects against, and the quoted reason doesn't supply the step.

**6. Fig. 1's numbers in tied cells.**
> "number: the probability that a sampled move is optimal ... up and right tie for best in cells 9 and 12"

It isn't said whether 0.57 in cell 9 is P(up) or P(up) + P(right). The legend also encodes one quantity twice: the number, and shading of "the share of sampled moves that are not optimal", which is just 1 minus the number.

**7. A sentence with no clear job.**
> "How much probability PPO leaves on other moves depends on its update, which a later stage builds, and this lesson does not vary its budget."

The "budget" (50,000 steps) was mentioned once. Is the point that longer training would sharpen the policy and shrink the gap? It isn't stated, so I can't say why the sentence is there.

**8. A missed explanation for the wrong arrows.**
Seed 3 aims cell 9 left, and seed 2 aims cell 8 right. The ε-greedy lesson showed that a policy which keeps moving at random prefers cell 9 left or down once ε ≥ 0.33, and the SARSA lesson showed that on-policy learners settle there. Seed 3's cell 9 puts only 0.36 on optimal moves. I expected the lesson to connect the two: does PPO optimize its stochastic policy's value, and land on "safe" arrows the way SARSA does? It says nothing about why seeds end one arrow short.

**9. Smaller points.**
- "Every value is an average over starts drawn uniformly from the 14 cells reset uses, the units in which the course solved its baselines". Calling an averaging convention "units" made me stop.
- "though nothing links the two policies". I can't tell why this clause is there. Is it saying the 1.36 to 1.43 match is coincidence?

### 3. Skippable sections, and results reported without their meaning

**Skippable:**
- **"PPO as a library call" (including agent.py).** Apart from "gamma = 0.9" and "greedy = argmax of the move probabilities", nothing there is needed for the main idea. That covers Monitor vs. Returns, model.predict, the uv/PyTorch notes, and the one-hot remark.
- **The Machado paragraph.** As written it adds a counterargument the lesson never uses (see point 3).
- **The seeds 5–9 paragraph.** It repeats the seeds 0–4 finding.

**Results without their meaning:**
- **Table 1, training-curve column vs. sampled column.** The promised check of SB3's "underestimates" warning is never concluded (point 2).
- **"no more than 0.07 above the hand-drawn policy, though nothing links the two policies".** The number is given, but not what it means.
- **"The order is still wrong. Seed 3 scores 1.59 and seed 4 scores 1.50"** comes as a surprise. The lesson doesn't say right there that this is expected, since SE 0.09 is larger than the true 0.06 gap. That explanation only arrives three paragraphs later in the sample-size formula.
- **Seeds 5–9:** "Both its 10 and its 10,000 evaluation episodes rank it above a seed whose arrows are all optimal". No numbers are shown (seeds.py output is collapsed), and nothing says whether this was within noise.
- **The standard deviations 8.6 (training) and 8.5 (evaluation)** are stated with no source on the visible page.
- **Fig. 1's per-cell probabilities.** Only cell 9's 0.57 is discussed. The figure doesn't say what the other values (0.82 in cell 0, 0.90 in cell 4) mean for the 1.36 sampled value.
