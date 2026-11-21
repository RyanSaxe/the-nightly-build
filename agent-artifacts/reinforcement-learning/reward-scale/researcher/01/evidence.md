# Evidence: reinforcement-learning/reward-scale (researcher 01)

The sources support every outside claim the commission needs, and the lesson's
two central results rest on its own derivations, as the commission intends. Ng,
Harada and Russell (1999) state that rescaling rewards by a fixed positive
factor preserves optimal policies (footnote 3) and that any change that is not a
potential difference can produce suboptimal policies in some MDP (Theorem 1).
Sutton and Barto pose the shift result as Exercises 3.15 and 3.16 on p. 61 and
print no answer, so the shift derivation on the page is its own evidence. Mnih
et al. (2015) give DQN's clipping and its stated cost in the Methods paragraph
"Training details". Engstrom et al. (2020) and Huang et al. (2022) describe
dividing rewards by the standard deviation of a rolling discounted sum, without
subtracting the mean. Current code agrees: Gymnasium 1.4.0's `NormalizeReward`
and Stable-Baselines3 2.9.2's `VecNormalize(norm_reward=True)` both divide each
reward by the square root of a running variance of a discounted reward sum. SB3
then clips the result to ±10 by default, so its normalizer contains a clipping
step. An OpenAI Baselines issue thread gives the reason the mean is not
subtracted: rewards that are all 1 make the agent want to live, and rewards that
are all 0 do not. The evidence is thin in one place. No source analyses whether
normalizing by a running statistic changes the optimal policy, so the page has
to reason it out. The scaling result has one scope limit. It holds for the
expected-return objective the course has defined, and Soft Actor-Critic (2018)
shows reward scale changing the learned policy under an entropy-regularized
objective, which the course has not taught.

## Sources

### 1. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed.

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (book page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary for its own definitions, examples and exercises, since the
             authors own that text. Secondary for its account of DQN in
             Section 16.5, which reports DeepMind's work from outside DeepMind.
Establishes: firsthand that the book poses the constant-shift question for a
             continuing task (Ex. 3.15) and for an episodic task (Ex. 3.16), with
             no printed answer. Ch. 3 contains no statement that multiplying
             rewards by a positive constant preserves optimal policies (searched
             the whole book for "positive constant", "affine", "positive
             linear", "scal" near "reward": no hit). Section 16.5 repeats DQN's
             reward handling.
Paraphrase:  Section 3.2 (p. 53): a maze-escape robot is often given a reward
             of -1 for every step before escape, which encourages escaping as
             quickly as possible. Section 3.2 (p. 54): the reward signal tells
             the agent what to achieve, not how. Exercise 3.7 (p. 56): a maze
             robot paid +1 on escape and 0 otherwise, undiscounted, shows no
             improvement; the exercise asks what is wrong. (Every escaping
             policy then returns 1, so moving the per-step reward from -1 to 0
             removes the preference for escaping quickly. This is the shift
             effect in an undiscounted episodic task; the book poses it as a
             question and gives no answer.) Section 3.4 (p. 57): episode
             termination is treated as entering an absorbing state that
             generates only rewards of zero; eq. (3.11) allows T = infinity or
             gamma = 1 "(but not both)". Exercise 3.15 and 3.16 (p. 61, in
             Section 3.5): quoted below. Section 2.6 (p. 34): initial
             estimates of +5 are "wildly optimistic" because the true values
             in the testbed are drawn from a normal distribution with mean 0
             and variance 1; initial estimates "provide an easy way to supply
             some prior knowledge about what level of rewards can be expected".
             Section 16.5 (p. 439): DQN's reward was +1 when the score
             increased, -1 when it decreased, 0 otherwise, which "standardized
             the reward signal across the games and made a single step-size
             parameter work well for all the games despite their varying
             ranges of scores."
Locators:    2018 edition, 2020 PDF printing. PDF page = printed page + 22 in
             these chapters (printed 34 = PDF 56; 53 = 75; 56 = 78; 57 = 79;
             61 = 83; 439 = 461). Minus signs dropped by text extraction were
             confirmed on rendered pages 53 and 439.
Quote:       Exercise 3.15 (p. 61): "In the gridworld example, rewards are
             positive for goals, negative for running into the edge of the
             world, and zero the rest of the time. Are the signs of these
             rewards important, or only the intervals between them? Prove,
             using (3.8), that adding a constant c to all the rewards adds a
             constant, v_c, to the values of all states, and thus does not
             affect the relative values of any states under any policies. What
             is v_c in terms of c and γ?"
             Exercise 3.16 (p. 61): "Now consider adding a constant c to all
             the rewards in an episodic task, such as maze running. Would this
             have any effect, or would it leave the task unchanged as in the
             continuing task above? Why or why not? Give an example."
             Section 3.2 (p. 53): "In making a robot learn how to escape from
             a maze, the reward is often −1 for every time step that passes
             prior to escape; this encourages the agent to escape as quickly as
             possible."
```

The answer to Ex. 3.15 is not printed. From (3.8), adding c to every reward of
a continuing task adds c·Σγ^k = c/(1−γ) to every return, so v_c = c/(1−γ). That
is the researcher's working and the lesson's to derive.

### 2. Ng, Harada and Russell, "Policy invariance under reward transformations: Theory and application to reward shaping", ICML 1999

```text
URL:         https://ai.stanford.edu/~ang/papers/shaping-icml99.pdf
Kind:        primary. The authors own the theorem and the footnote.
Establishes: firsthand that rescaling by a fixed positive factor and adding a
             potential difference preserve optimal policies, and that any
             shaping term that is not a potential difference can yield
             suboptimal policies for some MDP.
Paraphrase:  Authors as printed: Andrew Y. Ng, Daishi Harada, Stuart Russell,
             Computer Science Division, University of California, Berkeley.
             Abstract (p. 1): besides the positive linear transformation
             familiar from utility theory, one can add a reward that is the
             difference of a potential function between states; this is also
             necessary, in that any other transformation may yield suboptimal
             policies unless more is assumed about the MDP. Introduction
             (p. 1): in utility theory, single-step decisions under uncertainty
             allow only positive linear transformations (von Neumann and
             Morgenstern 1944). Introduction (p. 2): Randløv and Alstrøm's
             bicycle agent rode in tiny circles near the start state because it
             was rewarded for progress toward the goal and not penalized for
             riding away. Section 2.1 (p. 3): the undiscounted case assumes an
             absorbing state s0 that ends rewards, and proper policies.
             Footnote 3 (p. 3): quoted below. Theorem 1 (p. 4): F is
             potential-based if F(s,a,s') = γΦ(s') − Φ(s) for all s in
             S − {s0}, a, s'; potential-based F is necessary and sufficient for
             guaranteeing that optimal policies of M' = (S,A,T,γ,R+F) are
             optimal in M. Necessity bullet: if F is not potential-based, there
             exist proper transition functions T and a reward function R such
             that no optimal policy in M' is optimal in M. Proof (p. 5): for
             γ = 1, Φ(s0) can be set to 0 without loss of generality.
             Corollary 2 (p. 5): Q*_{M'}(s,a) = Q*_M(s,a) − Φ(s).
Locators:    the PDF carries no printed page numbers; pages are PDF pages 1-5.
             Text extraction of this PDF is garbled (Type 3 fonts); every
             passage here was read on rendered page images.
Quote:       Footnote 3 (p. 3): "...if we are to give optimality guarantees
             similar to those we will give here, then the only additional
             freedom this gives us in choosing shaping rewards is it allows us
             to rescale rewards by any fixed positive factor."
             Abstract (p. 1): "Furthermore, this is shown to be a necessary
             condition for invariance, in the sense that any other
             transformation may yield suboptimal policies unless further
             assumptions are made about the underlying MDP."
```

Researcher's derivation from Theorem 1, not printed in the paper, for the one
sentence linking back to the shaping lesson. The editor should re-derive it
before it appears on the page.

- Continuing, discounted task: a constant shift c on every reward is
  potential-based, with Φ ≡ −c/(1−γ), since γΦ − Φ = (1−γ)·c/(1−γ) = c. Corollary
  2 then gives V' = V + c/(1−γ), which matches Ex. 3.15's v_c.
- Episodic task, where the terminal state pays nothing further: the transition
  into the terminal state needs γΦ(s0) − Φ(s) = c with Φ(s0) = 0, so Φ(s) = −c
  for every non-terminal s. A transition between non-terminal states then pays
  γ(−c) − (−c) = (1−γ)c, not c, unless c = 0. A constant per-step shift is
  therefore not potential-based in an episodic task. The necessity half of
  Theorem 1 then says some episodic MDP exists where the shift changes the
  optimal policy, and the courier grid is built to be one.
- The potential-based term closest to a constant shift, Φ ≡ −c on non-terminal
  states, pays (1−γ)c per non-terminal step and c on the step into termination.
  At γ = 1 that is nothing per step and +c once at the end, which every
  terminating policy collects exactly once.

### 3. Mnih et al., "Human-level control through deep reinforcement learning", Nature 518, 529–533 (2015)

```text
URL:         https://www.nature.com/articles/nature14236
Kind:        primary. The authors (Volodymyr Mnih and 18 co-authors, Google
             DeepMind, as printed) own DQN and its training choices.
Establishes: firsthand that DQN clipped rewards during training only, the two
             reasons given (error-derivative scale, one learning rate across
             games) and the cost the authors state.
Paraphrase:  Methods, "Training details", first paragraph: 49 Atari 2600 games,
             one architecture, learning algorithm and hyperparameter setting
             across all of them. Rewards were changed during training only.
             Because the scale of scores varies greatly between games, positive
             rewards were clipped at 1 and negative rewards at -1, with 0 left
             unchanged. The stated benefits are a limited scale of error
             derivatives and an easier shared learning rate. The stated cost is
             that the agent "cannot differentiate between rewards of different
             magnitude". Methods, "Algorithm": γ = 0.99 throughout. Figure 2
             caption (p. 530): "Note that Q-values are scaled due to clipping
             of rewards (see Methods)."
Locators:    Methods section, subsection "Training details", paragraph 1.
             doi:10.1038/nature14236. The nature.com page is gated (paywall);
             its free HTML does not carry Methods. The text was read in the
             Nature-typeset PDF that DeepMind distributes
             (storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf,
             PDF p. 6). That address is the reading route, not the URL of
             record. The minus sign, which text extraction renders as "21",
             was confirmed on the rendered page.
Quote:       "While we evaluated our agents on unmodified games, we made one
             change to the reward structure of the games during training only.
             As the scale of scores varies greatly from game to game, we
             clipped all positive rewards at 1 and all negative rewards at −1,
             leaving 0 rewards unchanged. Clipping the rewards in this manner
             limits the scale of the error derivatives and makes it easier to
             use the same learning rate across multiple games. At the same
             time, it could affect the performance of our agent since it
             cannot differentiate between rewards of different magnitude."
```

### 4. van Hasselt, Guez, Hessel, Mnih and Silver, "Learning values across many orders of magnitude", NIPS 2016

```text
URL:         https://proceedings.neurips.cc/paper/2016/hash/5227b6aaf294f5f027273aebf16015f2-Abstract.html
             (preprint: https://arxiv.org/abs/1602.07714)
Kind:        primary for its own argument and its Double DQN experiments.
             It is not independent of Mnih et al. 2015 on what DQN did:
             Volodymyr Mnih is a co-author and both papers come from Google
             DeepMind (as printed).
Establishes: firsthand the claim that clipping changes the objective, with
             Atari instances in both directions.
Paraphrase:  Section 1 (p. 1): Pong rewards lie in [-1, 1]; in Ms. Pac-Man one
             ghost can be worth up to +1600. DQN clipped rewards and TD errors
             to [-1, 1]. Clipping makes the learner optimize the frequency of
             rewards, not their sum, and changes the objective. Section 4
             (p. 7): clipping is harmless in Pong, where no reward lies outside
             [-1, 1], and makes DQN blind to the difference between eating a
             ghost and eating a pellet in Ms. Pac-Man. Without clipping or
             Pop-Art, median gradient norms across games spread over more than
             six orders of magnitude, so no single step size suits all games.
             With Pop-Art in place of clipping, the Ms. Pac-Man agent hunts
             ghosts, while the clipped agent does not care more about ghosts
             than pellets (p. 7). Section 4 (p. 8): in Time Pilot the clipped
             agent shoots anything that moves and, over the long run, scores
             more. Pop-Art is at least as good as clipped Double DQN on 32 of
             57 games.
Locators:    proceedings PDF (9 pages): Section 1, paragraph 3, p. 1;
             Section 4, paragraphs 1 and 3, p. 7; Section 4, the two
             paragraphs after Figure 2, p. 8. The arXiv v2 wording of the
             Section 1 passage differs slightly, and arXiv numbers the
             score-difference figure as Figure 1; the quote and figure number
             here are from the proceedings PDF.
Quote:       Section 1, p. 1: "Clipping results in optimizing the frequency of
             rewards, rather than their sum. This is a fairly reasonable
             heuristic in Atari, but it does not generalize to many other
             domains. Second, and more importantly, the clipping changes the
             objective, sometimes resulting in qualitatively different policies
             of behavior."
```

### 5. Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph and Madry, "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO", ICLR 2020

```text
URL:         https://arxiv.org/abs/2005.12729
             (ICLR 2020 publication page https://openreview.net/forum?id=r1etN1rtPB
             is behind a browser-verification wall: gated, not dead. The arXiv
             v1 PDF is headed "Published as a conference paper at ICLR 2020".)
Kind:        primary for its ablation study. Secondary for what OpenAI
             Baselines' PPO2 code does, which it reports from outside OpenAI
             (affiliations as printed: MIT; Two Sigma).
Establishes: firsthand that reward scaling changed PPO's results in their
             Humanoid-v2 and Walker2d-v2 ablation. Repeats, from reading the
             code, how the scaling works.
Paraphrase:  Section 3, list item 2 (p. 3): PPO's implementation divides each
             reward by the standard deviation of a rolling discounted sum of
             rewards, without subtracting and re-adding the mean. List item 5
             (p. 3): it also clips rewards, usually to [-5, 5] or [-10, 10].
             Appendix A.2, Algorithm 1 (p. 12): R_t ← γR_{t-1} + r_t; add R_t
             to running statistics; return r_t divided by their standard
             deviation. (The procedure is labelled "SCALE-OBSERVATION" though
             its input is a reward, and it shows no reset at episode ends.)
             Figure 1 caption (p. 4): reward normalization, Adam annealing and
             network initialization each significantly changed the reward
             landscape over hyperparameters and were needed for the highest
             PPO reward in the tested grid.
Locators:    arXiv 2005.12729v1, Section 3 list items 2 and 5 (p. 3); Figure 1
             (p. 4); Appendix A.2, Algorithm 1 (p. 12).
Quote:       Section 3, item 2: "Reward scaling: Rather than feeding the
             rewards directly from the environment into the objective, the PPO
             implementation performs a certain discount-based scaling scheme.
             In this scheme, the rewards are divided through by the standard
             deviation of a rolling discounted sum of the rewards (without
             subtracting and re-adding the mean)—see Algorithm 1 in Appendix
             A.2."
```

### 6. Huang, Dossa, Raffin, Kanervisto and Wang, "The 37 Implementation Details of Proximal Policy Optimization", ICLR Blog Track, 25 March 2022

```text
URL:         https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
Kind:        secondary. It reports what OpenAI Baselines' ppo2 (commit ea25b9e)
             does, from outside OpenAI. Its reward-scaling sentence is a
             near-verbatim retelling of Engstrom et al.'s, so the two count as
             one origin for the description.
Establishes: repeats the reward-scaling description and adds code locators in
             Baselines (common/vec_env/vec_normalize.py#L28 for scaling, #L32
             for clipping). Firsthand only for the authors' own remark that
             there is no clear evidence clipping after scaling helps.
Paraphrase:  Section "9 details for continuous action domains (e.g. Mujoco)",
             detail 8 "Reward Scaling": VecNormalize divides rewards by the
             standard deviation of a rolling discounted sum of rewards,
             without subtracting and re-adding the mean, and Engstrom et al.
             recommend it. Detail 9 "Reward Clipping": the scaled reward is then
             clipped, usually to [-10, 10]. Section "9 Atari-specific
             implementation details", "The Use of ClipRewardEnv": the wrapper
             bins rewards to {+1, 0, -1} by sign, following Mnih et al. 2015.
Locators:    section and detail headings as named; the page has no paragraph
             numbers.
Quote:       Detail 9: "There is currently no clear evidence that Reward
             Clipping after Reward Scaling can help with learning."
```

### 7. Gymnasium 1.4.0, `gymnasium.wrappers.NormalizeReward`

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/reward_wrappers/
             (rendered source: https://gymnasium.farama.org/v1.4.0/_modules/gymnasium/wrappers/stateful_reward/;
             release: https://pypi.org/project/gymnasium/1.4.0/)
Kind:        primary. The Farama Foundation's documentation and code own the
             wrapper's behaviour.
Establishes: firsthand the current wrapper name, signature, defaults and the
             statistic it divides by.
Paraphrase:  Gymnasium 1.4.0 is the latest release on PyPI, uploaded
             2026-10-05; tag v1.4.0 resolves to commit 8ba8c3a6. Signature:
             NormalizeReward(env, gamma=0.99, epsilon=1e-8). Docstring:
             "Normalizes immediate rewards such that their exponential moving
             average has an approximately fixed variance." On each step the
             wrapper sets discounted_reward = discounted_reward·gamma·
             (1 − terminated) + reward, updates a RunningMeanStd with it, and
             returns reward / sqrt(return_rms.var + epsilon). It does not
             subtract the mean, and it does not clip. A docstring note: "The
             scaling depends on past trajectories and rewards will not be
             scaled correctly if the wrapper was newly instantiated or the
             policy was changed recently." A separate wrapper,
             gymnasium.wrappers.ClipReward(env, min_reward, max_reward), clips
             (added in v1.0.0). Vector versions of both exist.
Locators:    docs page, NormalizeReward entry; source file
             gymnasium/wrappers/stateful_reward.py, NormalizeReward.step. Read
             in the 1.4.0 wheel from PyPI and confirmed against the v1.4.0
             docs and rendered source pages.
Quote:       code comments in NormalizeReward.step, because they record the
             maintainers' own reasoning:
             "# We don't (reward - self.return_rms.mean) see
             https://github.com/openai/baselines/issues/538"
             "# Using the `discounted_reward` rather than `reward` makes no
             sense but for backward compatibility, it is being kept"
```

### 8. Stable-Baselines3 2.9.2, `VecNormalize` and `ClipRewardEnv`

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/vec_envs.html
             (rendered source: https://stable-baselines3.readthedocs.io/en/v2.9.2/_modules/stable_baselines3/common/vec_env/vec_normalize.html;
             release: https://pypi.org/project/stable-baselines3/2.9.2/)
Kind:        primary. The SB3 documentation and code own the wrapper's
             behaviour.
Establishes: firsthand the current signature, defaults, the statistic it
             divides by, and the clip it applies afterwards.
Paraphrase:  SB3 2.9.2 is the latest release on PyPI, uploaded 2026-10-26; tag
             v2.9.2 resolves to commit 0cdcd200. Signature: VecNormalize(venv,
             training=True, norm_obs=True, norm_reward=True, clip_obs=10.0,
             clip_reward=10.0, gamma=0.99, epsilon=1e-08, norm_obs_keys=None).
             When training, each step sets returns = returns·gamma + reward and
             updates ret_rms with it; returns are reset to 0 for environments
             that are done, and SB3's vector environments set done =
             terminated or truncated. normalize_reward returns
             clip(reward / sqrt(ret_rms.var + epsilon), −clip_reward,
             +clip_reward). No mean is subtracted. The docstring describes
             clip_reward as "Max value absolute for discounted reward", but the
             code clips the normalized per-step reward.
             stable_baselines3.common.atari_wrappers.ClipRewardEnv returns
             np.sign(reward), documented as "Clip the reward to {+1, 0, -1} by
             its sign."
Locators:    docs page, "VecNormalize" section; source file
             common/vec_env/vec_normalize.py, __init__, step_wait,
             _update_reward, normalize_reward; common/atari_wrappers.py,
             ClipRewardEnv.reward; common/vec_env/dummy_vec_env.py line 63.
             Read in the 2.9.2 wheel from PyPI and confirmed against the
             v2.9.2 docs and rendered source pages.
Quote:       none needed.
```

### 9. OpenAI Baselines issue #538, "Gamma in VecNormalize for rms updates." (August 2018)

```text
URL:         https://github.com/openai/baselines/issues/538
Kind:        primary for the stated reason Baselines' VecNormalize does not
             subtract the mean, given in the repository's own issue thread by
             GitHub user unixpickle, one of the two assignees (the other is
             joschu). Gymnasium 1.4.0's code cites this issue for the same
             choice.
Establishes: firsthand that the people answering for the code chose not to
             subtract the mean because a constant shift changes what the agent
             wants. It is a statement, not a proof.
Paraphrase:  The issue (opened 24 August 2018 by pisiiki, closed 14 September
             2018) asks why VecNormalize's statistics use a discounted return.
             unixpickle (26 August) answers that returns drive the value
             function and policy, so returns are what should be normalized.
             andytwigg (28 August) notes the code divides by the standard
             deviation without subtracting the mean, while the result is
             clipped symmetrically around 0. unixpickle (29 August) says the
             gamma should match the algorithm's discount factor, and that
             subtracting the mean would change the dynamics of the environment:
             rewards that are all 1 make the agent want to live, rewards that
             are all 0 make it indifferent to living or dying.
Locators:    unixpickle's comment of 29 August 2018, part "Regarding 2)".
             The github.com page returned 403 through this session's proxy to
             plain requests; the quotes were returned as verbatim excerpts by a
             page-fetch tool in two separate requests, not read in a browser.
             Reopen before quoting on the page.
Quote:       "Regarding 2), subtracting the mean from the rewards would change
             the dynamics of the environment." "For example, if your rewards
             are all 1, that is very different than if your rewards are all
             0." "In the former case, the agent wants to live; in the latter,
             it doesn't care if it lives or dies."
```

### 10. Haarnoja, Zhou, Abbeel and Levine, "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor", ICML 2018

```text
URL:         https://proceedings.mlr.press/v80/haarnoja18b.html
Kind:        primary for its own reward-scale ablation.
Establishes: firsthand that under SAC's entropy-regularized objective, reward
             scale changes the learned policy. This marks the scope of the
             lesson's scaling result rather than material for the page.
Paraphrase:  Section 5.2, "Reward scale." paragraph: SAC is particularly
             sensitive to reward scale because the scale plays the role of the
             temperature of the energy-based optimal policy and so controls its
             stochasticity. Small reward magnitudes give a nearly uniform
             policy; large ones a nearly deterministic policy stuck in poor
             local minima. The authors call reward scale the only
             hyperparameter that needed tuning, interpretable as the inverse
             temperature.
Locators:    Section 5.2, paragraph "Reward scale.", PMLR PDF p. 7 (also
             arXiv 1801.01290v2 p. 7); Figure 3(b).
Quote:       "Soft actor-critic is particularly sensitive to the scaling of the
             reward signal, because it serves the role of the temperature of
             the energy-based optimal policy and thus controls its
             stochasticity."
```

## Contradictions

- **Clip or sign.** Mnih et al. (Methods) clip positive rewards at 1 and
  negative at −1. Sutton and Barto (p. 439), Huang et al. and SB3's
  `ClipRewardEnv` describe or implement the sign of the reward. The two agree on
  Atari, where score changes are integers. They differ on any reward strictly
  between −1 and 1 other than 0: clipping leaves 0.3 at 0.3, sign maps it to 1.
  If the courier grid's per-step reward is fractional (for example −0.1),
  "clip to [−1, 1]" and "sign" give different environments, and the page must
  say which it applies.
- **"Positive linear transformation" in Ng et al.'s abstract.** The abstract
  credits utility theory with the positive linear transformation. A von
  Neumann–Morgenstern utility is unique up to a·u + b with a > 0, an added
  constant included (standard result, not checked against a source in this
  record). The paper does not define the phrase inline. Its
  footnote 3 restricts the extra freedom to "rescale rewards by any fixed
  positive factor", and Theorem 1's necessity half covers an added per-step
  constant in an episodic task (derivation under source 2). Cite footnote 3 for
  the scaling result. The abstract does not license a per-step shift.
- **Reward clipping range in PPO implementations.** Engstrom et al.: "usually
  [−5, 5] or [−10, 10]". Huang et al.: "usually [−10, 10]". SB3 2.9.2 default:
  clip_reward = 10.0. Gymnasium 1.4.0 `NormalizeReward`: no clipping.
- **When the running sum resets.** Gymnasium multiplies the accumulator by
  γ(1 − terminated), so truncation does not reset it. SB3 resets it on done,
  which includes truncation. Engstrom et al.'s Algorithm 1 shows no reset. The
  issue thread (source 9) records a proposal to reset on terminal states. None
  of this changes what the page can say: "divided by the standard deviation of a
  running discounted sum of rewards" is true of all three.
- **Gymnasium doubts its own statistic.** Its code comment calls tracking
  `discounted_reward` rather than `reward` something that "makes no sense but
  for backward compatibility, it is being kept". The issue thread gives the
  opposite reasoning for the same choice: returns, not rewards, drive learning.
  Don't present the statistic as settled design.
- **Does clipping hurt?** van Hasselt et al. report clipping harmless in Pong
  and, in Time Pilot, report the clipped agent scoring more over the long run,
  which they attribute partly to both agents being myopic at γ = 0.99. With
  Pop-Art in place of clipping, results were at least as good on 32 of 57 games,
  with median +0.4% and mean +34%. The sources support "clipping can change the
  optimal policy" and do not support "clipping makes agents score worse".
- **Normalization by a running statistic.** Every source describes it as
  division by a positive number without mean subtraction, so with the statistic
  frozen it is a positive scaling and leaves the optimal policy of the reward it
  divides unchanged. No source says so; this is the researcher's reading of the
  code. Three qualifications from the primaries: the divisor moves during
  training (Gymnasium's docstring note); SB3 clips after dividing, so a scaled
  reward beyond ±10 has its ratios changed; and the issue thread says
  subtracting the mean, which would be a shift, was rejected because it changes
  what the agent wants.
- **Scope of the scaling result.** It holds for the expected discounted return.
  Haarnoja et al. show reward scale changing the learned policy under an
  entropy-regularized objective. The course has not taught entropy bonuses, so
  the page should state the result for the objective the course defined and
  should not reach for SAC.
- **Against the commission's practical point.** No source contradicts it. Mnih
  et al. (learning rate), Sutton and Barto p. 439 (one step size across games)
  and p. 34 (initial estimates as prior knowledge of the reward level), and van
  Hasselt et al. (gradient-norm spread across games) all support "scale matters
  to a learner with fixed step size and starting estimates".

## Numbers

```text
Figure: clip range [−1, 1]; positive rewards to +1, negative to −1, 0 unchanged
Owner:  Mnih et al. 2015, Methods, "Training details"
Scope:  training only, 49 Atari 2600 games; evaluation used unmodified scores

Figure: γ = 0.99
Owner:  Mnih et al. 2015, Methods, "Algorithm"; van Hasselt et al. 2016, Section 4, p. 8
Scope:  DQN; Double DQN with and without Pop-Art

Figure: up to +1600 for one ghost in Ms. Pac-Man; Pong rewards within [−1, +1]
Owner:  van Hasselt et al. 2016, Section 1, p. 1
Scope:  Atari reward magnitudes, as the authors state them

Figure: 32 of 57 games at least as good; median difference +0.4%, mean +34%
Owner:  van Hasselt et al. 2016, Section 4, p. 8
Scope:  Double DQN with Pop-Art versus clipped Double DQN, human-normalized scores, 57 Atari games

Figure: 95% of games' median gradient norms span less than two orders of magnitude
        (about 1 to 20) with Pop-Art; almost four with clipped Double DQN; more than six
        unclipped without Pop-Art
Owner:  van Hasselt et al. 2016, Section 4, p. 7
Scope:  median ℓ2 gradient norm over training, per game, across 57 games

Figure: v_c = c/(1 − γ)
Owner:  researcher's working from Sutton and Barto eq. (3.8); not printed in the book
Scope:  continuing task, constant c added to every reward

Figure: NormalizeReward defaults gamma = 0.99, epsilon = 1e-8; no clip
Owner:  Gymnasium 1.4.0 (PyPI upload 2026-10-05)
Scope:  divides each reward by sqrt(running variance of the discounted reward sum + epsilon)

Figure: VecNormalize defaults norm_reward = True, clip_reward = 10.0, gamma = 0.99, epsilon = 1e-08
Owner:  Stable-Baselines3 2.9.2 (PyPI upload 2026-10-26)
Scope:  divides each reward by sqrt(running variance of the discounted return + epsilon), then clips to ±10

Figure: PPO reward clip "usually [−5, 5] or [−10, 10]"
Owner:  Engstrom et al. 2020, Section 3, item 5 (describing OpenAI Baselines PPO2)
Scope:  MuJoCo-style continuous-control configurations

Figure: initial estimate +5 against true values drawn from N(0, 1)
Owner:  Sutton and Barto, Section 2.6, p. 34
Scope:  10-armed testbed; the optimism is relative to the reward distribution
```

## Limits

- No textbook in hand states the positive-scaling result as a theorem. Sutton
  and Barto Ch. 3 does not state it. Ng et al.'s footnote 3 is the cleanest
  published statement; the page's own derivation is the evidence.
- Sutton and Barto print no answers to Exercises 3.15 and 3.16. The shift results
  rest on the lesson's derivation; the book supplies only the question.
- No source analyses whether reward normalization by a running statistic can
  change the optimal policy. The page must reason it out from the code facts
  recorded above.
- The courier grid's reward values, discount and policies have no outside
  source. Its value-iteration and Q-learning output is the evidence.
- A caution for building the courier's extreme shift case, from Sutton and
  Barto eq. (3.11) and Ng et al. Section 2.1: with γ = 1 and a positive per-step
  reward, a policy that never delivers has an unbounded return and is not
  proper, so value iteration will not converge. The "never deliver" case needs
  γ < 1.
- The baselines issue quotes came through a page-fetch tool as excerpts; the
  page itself was not opened in a browser. Reopen before quoting it.
- GitHub source files at the release tags returned 403 through this session's
  proxy, which means gated. The tags were confirmed to exist with git
  ls-remote, and the code was read in the released wheels and on the versioned
  documentation sites, which are the URLs of record above.
- Nature's full text is paywalled. Methods was read in DeepMind's distributed
  copy of the typeset article.
- Ng et al.'s proceedings page range was not confirmed; cite the paper as ICML
  1999 without page numbers.

## Source assets

```text
Sutton and Barto (source 1)
Asset: None found. Exercises 3.15 and 3.16 are text; Example 3.5's gridworld
       figure (p. 60) illustrates a different point.

Ng, Harada and Russell (source 2)
Asset: None found. The cited passages are text and an equation.

Mnih et al. (source 3)
Asset: None found for clipping. Figure 2's caption notes scaled Q-values but the
       figure shows learning curves, not the clipping.

van Hasselt et al. (source 4)
Asset: Figure 2, proceedings p. 8 (Figure 1 in arXiv v2): sorted bar chart
       of the difference in normalized score between Double DQN with and
       without Pop-Art, one bar per game, 57 Atari games, on a nonlinear axis
       running from −1600% to +1600%.
Shows: removing clipping moves scores up on some games and down on others, so
       clipping changed behaviour in both directions.
Crop:  keep the full bar set, the axis label and the game names; the caption
       must be kept or restated. Useful only if the page widens its DQN
       mention, which the commission limits to a sentence.

Engstrom et al. (source 5)
Asset: Figure 1, p. 4: histograms of final reward with each of four
       optimizations on or off, Humanoid-v2 and Walker2d-v2.
Shows: reward scaling shifts PPO's outcome distribution.
Crop:  keep the reward-scaling panels with their on/off legend and the
       environment labels. Needs PPO context the course has not taught, so
       probably not for this page.

Huang et al. (source 6): None found.
Gymnasium 1.4.0 (source 7): None found.
Stable-Baselines3 2.9.2 (source 8): None found.
Baselines issue #538 (source 9): None found.
Haarnoja et al. (source 10): Figure 3(b), p. 7, learning curves across reward
       scales. Not for this page: it needs entropy-regularized RL.
```

## Discarded

```text
https://arxiv.org/pdf/1602.07714v2: read in full for the clipping passages; its Section 1 wording differs from the NIPS proceedings version, which is the version quoted.
https://www.nature.com/articles/nature14236 (free HTML view): carries no Methods text; kept as URL of record, text read elsewhere as noted.
https://openreview.net/pdf?id=r1etN1rtPB: 403 behind browser verification; the arXiv v1 PDF, marked as the ICLR 2020 paper, was read instead.
https://gymnasium.farama.org/api/wrappers/reward_wrappers/: unversioned docs page; replaced by the v1.4.0 page so the version is fixed.
https://stable-baselines3.readthedocs.io/en/master/guide/vec_envs.html: tracks master, not a release; replaced by the v2.9.2 page.
https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/stateful_reward.py: 403 through the session proxy (gated); versioned docs source page used instead.
https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/vec_normalize.py: 403 through the session proxy (gated); versioned docs source page used instead.
```
