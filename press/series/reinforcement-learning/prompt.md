# Reinforcement Learning

The course runs daily and assumes no knowledge of reinforcement learning. It ends with designing
environments and training agents in them, first for control and games and then for language models.
The last topic is reinforcement learning with verifiable rewards (RLVR). Someone who finishes can read
the RLVR literature critically, write an environment and a verifier for a language model, and train the
model in that environment. A package such as `verifiers` is a good place to practice, but teach what
would still be true if the package changed.

Don't simplify the math or the code. Teach each reinforcement learning idea when the course first needs
it. For reinforcement learning, a lesson can rely only on what earlier lessons taught. For everything
else, it can rely on the background in `press/editorial.md`. Never treat a reinforcement learning topic
outside the course as already studied.

## The first three lessons

The first three lessons were written under older instructions. They are
`environments-and-the-rl-problem`, `finding-optimal-policies`, and `learning-values-from-samples`. Read
them to learn what the course has taught and to reuse their environment and code. Don't copy their
length, structure, voice, or the way they refer to each other. Where they disagree with these
instructions about how to write, follow these instructions.

## Curriculum

Work through the stages below in order, with one exception. You can alternate between stages 1 and 2,
because stage 1's topics from the Gymnasium contract onward don't depend on stage 2.

Read the published lessons to see how far the course has come, and teach what it needs next. Each topic
below is at least one lesson. A topic that holds more than one idea becomes several lessons. You can
split, merge, or reorder topics within a stage. If a lesson needs a foundation the course hasn't taught,
teach the foundation first. Give new research a lesson once its prerequisites have been taught.

The stages set the order of dependencies, and they don't assign topics to lesson numbers. The one target
on timing is that the reader trains an off-the-shelf agent on a custom environment within the first few
weeks. Use the agent's library without explaining its algorithm until a later lesson teaches that
algorithm.

Don't give a "Mention only" topic its own lesson. If it helps the main idea, give it a sentence and a
pointer.

Tools and recipes change quickly, especially in stage 8. Check each one when you write the lesson,
because these names date from November 2026.

### 1. Environments and the RL problem

- The agent-environment loop, Markov decision processes, and the Bellman equations
- Value iteration and policy iteration
- The Gymnasium contract, including termination and truncation
- A first custom environment, checked with the environment checker, random actions, a
  hand-written policy, play by hand, and a look at the scale of observations and rewards
- Training an off-the-shelf agent on it, with a separate evaluation environment, several
  seeds, and random and scripted baselines

Mention only: CleanRL as reading material, PufferLib as a source of practical advice, and
JAX environments.

### 2. Learning from samples

- Monte Carlo and temporal-difference prediction
- Action values from samples and generalized policy iteration
- Why greedy learning stalls, and epsilon-greedy exploration
- SARSA and Q-learning
- On-policy and off-policy learning, with importance sampling
- N-step returns
- Function approximation with semi-gradient updates
- The deadly triad, with its statement and one example of divergence

Mention only: Expected SARSA, backward-view eligibility traces, Gradient-TD, and
Emphatic-TD.

### 3. Designing environments

- Observation contents, scale, and normalization
- The Markov property, with history, frame stacking, and time awareness
- Action spaces, including removal, discretization, factoring, and action frequency
- Action masking in Q-learning and in an off-the-shelf agent
- Reward specification, reward scale, and specification gaming
- Potential-based shaping and the limits of its guarantee
- Held-out levels, procedural generation, domain randomization, and checks for memorized
  behavior
- A small project that changes one design choice at a time and measures each change
  across seeds

Mention only: sim-to-real as an example under domain randomization, and Procgen's way of generating
levels, without installing its package.

### 4. Deep value methods

- DQN with replay and target networks, on small environments
- Double Q-learning and multi-step targets
- What Rainbow's ablation found about its parts
- Small test environments that expose bugs in value learning, and a tabular cross-check
- Reporting results with individual runs, interval estimates, and enough seeds for the
  claim being made

Mention only: dueling networks, distributional RL, noisy nets, and Atari as a benchmark.

### 5. Policy gradients

- Policies for discrete and continuous actions
- The policy gradient theorem and REINFORCE
- Baselines and actor-critic
- Generalized advantage estimation through the λ-return
- The vector environment contract and autoreset
- The importance-sampled surrogate objective and limiting policy change by KL
- PPO built against a reference run, and the implementation details that decide whether
  it works
- Small test environments that expose bugs in policy learning, and diagnostics such as
  entropy, KL, and explained variance
- Hyperparameter search with separate tuning and evaluation seeds
- Soft actor-critic and maximum entropy RL

Mention only: natural gradients, the Fisher matrix, TRPO, monotonic improvement theory,
DDPG, TD3, and offline RL.

### 6. Harder environments

- Bandits, UCB, and regret, as the exploration problem in its simplest form
- Optimism in MDPs through count bonuses and random network distillation, with the limits
  of bonuses
- Partial observability with recurrent policies
- Masking in policy gradients and why the gradient stays valid
- Fast environments, with speed measured on the laptop CPU the course uses
- Curricula through level prioritization
- One complete project on a new environment, trained with an implementation already known
  to work

Mention only: ICM, Go-Explore, HER, PAIRED and unsupervised environment design, and speed
claims measured on GPUs.

### 7. Games

- Normal-form games, mixed strategies, best response, minimax, Nash equilibrium in the
  zero-sum case, and exploitability
- Turn-based games, negamax, and a multi-agent environment contract with turn order,
  per-agent observations, masks, and a way to simulate from any state
- Self-play, non-stationarity, cycling, and how to measure progress against fixed baselines
- Decision-time planning and UCT
- Policy-value networks and PUCT
- AlphaZero's self-play loop, built small on a board an exact solver can check
- Models learned from samples, model error, and MuZero built small
- External regret, regret matching, and why no-regret self-play reaches equilibrium
- Extensive form, information sets, and why a state has no value of its own under hidden
  information
- Counterfactual regret minimization on small poker, checked against a reference
- Sampling with Monte Carlo CFR
- Superhuman poker as a case study in abstraction and subgame solving
- Regularized self-play with policy gradients, and the 2026 results built on it, such as Ataraxos
- Populations through double oracle and PSRO, with leagues as a case study
- General-sum and cooperative games, as the place where zero-sum guarantees stop
- Self-play in a custom game

Mention only: AlphaGo's pipeline as history, Markov games and minimax-Q, Gumbel search,
EfficientZero, Sampled and Stochastic MuZero, NFSP, Deep CFR, DREAM, ESCHER, ReBeL, Student
of Games, Obscuro, CTDE, MAPPO, Hanabi, Cicero, correlated equilibrium, and PPAD.

### 8. Language models

- The model as a policy, with tokens as actions and one reward spread across a sequence
- Fine-tuning as behavior cloning and as a warm-up for RL
- Reward models from human preferences, RLHF, and why its KL penalty exists
- Overoptimization of a proxy
- Reward sources across exact checks, solvers, tests, judges, and learned models
- A first environment and verifier, validated with a known solution and a no-op, with a
  baseline evaluation before any training
- GRPO derived from PPO by removing the critic and taking the baseline from the same prompt
- A small run and what to watch during it
- How much a result depends on the base model, and controls such as random rewards and
  held-out shift
- Rollout reuse, the trainer and inference split, and what PPO's importance ratio and clip do when rollouts are reused
- What GRPO's variants change about length, normalization, and clipping
- The DeepSeek-R1 recipe as a dated example, and current recipes built on specialists and
  distillation
- The verifier as a proxy with an error rate
- Multi-turn and tool-using environments
- Rendering prompts so that the trained tokens match the sampled tokens
- Reward hacking, measured against a true-task metric
- Detection, monitorability, and keeping the reasoning trace out of the reward
- Whether hacking spreads into wider misalignment, and what mitigates it
- Asynchronous training, staleness, and what a run costs
- One complete project that trains a model in a custom environment and audits its results
  for hacks

Mention only: DPO, rejection sampling, active querying, distributional methods,
language-model self-play, evaluation awareness, and the catalog of training frameworks.

## Each lesson

The commission names the topic, the one idea, and the case to start from. It leaves the experiments, the causes
to test, and the page's structure to the writer.

Draw a concept when a drawing shows a structure, a path, or a pattern that a sentence can't show easily, and put
the drawing next to the words that explain it. Show what the agent learned as well as whether it improved. A
learning curve only shows improvement, so go further with value functions as heatmaps, policies drawn on the grid,
trajectories, search trees, or whatever fits the idea. When a lesson walks through a process, the same diagram can
return at each step with the current part marked, so its notation needs teaching only once. Draw charts of the
lesson's own runs as inline SVG, because they then follow the light and dark themes and need no outside source.

When the main result can be derived, derive it in full, and use a run to check the derivation. Put each equation
next to the words or figure it belongs to.

Cite what the lesson takes from someone else. A derivation or a run printed on the page is its own evidence, so a
section made of them can go without a citation, and `W-CITE-DENSITY` needs no action there. Link the paper that
introduced an idea when one clearly did. Don't add a sentence only to hold a citation. In the Go deeper band, say
which part of each paper to read and why, in one line.

Keep one small custom environment through the control lessons, and change it only when an idea needs it, so results
stay comparable. Link the lesson that introduced its rules. A lesson on continuous actions can add a second small
environment, because a grid can't exercise continuous actions.

The writer writes and runs the lesson's code, and its printed output counts as evidence alongside `evidence.md`. The
editor can change the code and rerun it, and the page then changes with it.

Write the code as Python files with inline script metadata, so that `uv run file.py` works with no other setup apart
from copying any linked file. Run every listing exactly as printed before the lesson publishes. A published lesson can
include only images and chart files, so print every code file in full. A later lesson may import a file printed in an
earlier lesson if it links that lesson. Put a long experiment script and its output inside a `details` element. Scale
each experiment to finish within a few minutes on a laptop CPU. When an idea truly needs a GPU, give the recipe and say
on the page that it wasn't run.

Every number from a run appears in the printed output of a listing on the page. Keep an experiment script to about 100
lines, and have it print only the numbers the page uses. A longer script usually means the lesson is reporting too much.

Report only the results that teach the main idea. There are usually one or two. Check each result before you report it,
with code that doesn't need to appear on the page:

- Rerun the experiment with seeds you haven't used. The conclusion has to survive. Give a noisy number at the precision
  it repeats at, and state its spread.
- When the lesson says something causes an experimental result, remove that cause in the code and rerun. If the result
  survives, rewrite or cut the explanation.
- If a result comes from one cell or one seed, check other cells or seeds before you generalize from it.

A sentence that a check supports states its conclusion without the check's numbers. If those numbers teach the main idea,
add the check to the listing and say on the page how it ran.

End the body with an `nb-note` of two or three problems that can be answered from the lesson and the course so far. At
least one problem asks about a case the lesson didn't work. One problem can bring back an earlier idea, with a link to the
lesson that taught it. Put each answer and its working inside a `details` element.
