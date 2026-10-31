# Reinforcement Learning

Build a daily course that starts from no reinforcement learning and ends with
designing environments and training agents in them, first for control and games
and then for language models. The destination is reinforcement learning with
verifiable rewards (RLVR): reading its literature critically, writing an
environment and a verifier for a language model, and training on them. A package
such as `verifiers` is a good place to practice, and the lessons teach what would
survive a change of package.

The course starts from no reinforcement learning. Math and code run at full
difficulty, and every reinforcement learning idea, including bandits, UCB, and
regret, is taught when the course first needs it. No lesson says or implies what
anyone already knows or has studied.

## Curriculum

Work through these stages in order. Read the published lessons to see how far the
course has come, teach what it needs next, and build on earlier lessons instead of
repeating them. Within a stage, split, merge, or reorder topics as the teaching
requires. Teach a missing foundation first when one appears, and give new research
a lesson once its prerequisites have been taught. A custom environment with an
off-the-shelf agent training on it should arrive by about lesson 5, with the
library treated as a black box that later lessons open. The course should finish
Designing environments by about lesson 25.

1. **Environments and the RL problem.** The agent-environment loop, Markov decision
   processes and the Bellman equations, the Gymnasium contract and a first custom
   environment, training an off-the-shelf agent on it, value iteration and policy
   iteration.
2. **Learning from samples.** Monte Carlo and temporal-difference prediction, SARSA
   and Q-learning, exploration from bandits and UCB to optimism in MDPs, n-step
   returns and TD(λ), function approximation and the deadly triad.
3. **Deep value methods.** DQN, Double DQN through Rainbow, debugging with probe
   environments, reporting results across seeds.
4. **Policy gradients.** The policy gradient theorem and REINFORCE, baselines and
   actor-critic, generalized advantage estimation, natural gradients and trust
   regions, PPO from scratch and the implementation details that decide whether it
   works, continuous actions and maximum entropy RL.
5. **Designing environments.** Observations and partial observability, action spaces
   and masking, reward design and potential-based shaping, hard exploration, fast
   vectorized environments, generalization and curricula, and one complete project
   on a new environment.
6. **Games.** Zero-sum Markov games and self-play, Monte Carlo tree search as bandits
   in a tree, AlphaGo through AlphaZero built small, planning with learned models,
   imperfect information and exploitability, counterfactual regret minimization
   through superhuman poker, populations and leagues, and self-play in a custom
   game.
7. **Language models.** The model as a policy and fine-tuning as behavior cloning,
   reward models from human preferences, RLHF and how its reward models break,
   verifiable rewards, GRPO, the reasoning-model recipe from DeepSeek-R1, environments
   and verifiers, multi-turn and tool-using environments, reward hacking, training
   infrastructure, and one complete project that trains a model in a custom
   environment.

## Each lesson

Open Why this matters on the particular problem this lesson's idea solves, with one
real case where it is at work, in ordinary sentences. Leave out lists of what the
lesson will enable and claims about how much later work depends on it.

Give the math in full, including the derivations. Whenever a concept can be drawn,
draw it before explaining it. A learning curve shows that an agent improved, so go further
and show what it learned: value functions as heatmaps, policies drawn on the grid,
trajectories, search trees, whatever fits the idea.

Link the papers that introduced each idea, and use the Go deeper band to say which
part of each paper to read next and why.

Write the code as Python files with inline script metadata, so that
`uv run file.py` works with no other setup. Run every listing as printed before the
lesson publishes, and report only what the run produced. A later lesson may import a
file from an earlier one, and it links that lesson when it does. Keep one small custom
environment in use through the control lessons and grow it as the course needs, so
results stay comparable and the code accumulates into one project. Scale every run to
finish within a few minutes on a laptop CPU. When an idea truly needs a GPU, give the
recipe and say on the page that it was not run.

End the body with an `nb-note` of two or three problems answerable from the lesson
alone, with each answer and its working inside a `details` element.
