# Evidence: reinforcement-learning/potential-based-shaping (researcher 01)

Ng, Harada and Russell (1999) state the theorem and prove both directions, and the record has
locators for the statement, both proofs, the terminal-state convention and the bicycle example.
Their proof does not telescope a trajectory. It substitutes Q* − Φ into the Bellman optimality
equation. The telescoped return the commission builds on (shaped return = original return −
Φ(s₀) + γᴺΦ(s_N)) is printed as Eq. 3 of Grześ (2017), which also gives the terminal-potential
counterexample and the rule Φ = 0 wherever a trajectory stops. Ng's paper covers two cases: an
undiscounted task with a single absorbing state, where Φ(s₀) = 0 holds without loss of generality,
and a discounted task with no terminal state at all. A discounted task that terminates, which is
the race, falls outside both, and Grześ shows the guarantee then needs Φ = 0 at the terminal
state. Wiewiora (2003) proves the
initialization equivalence for tabular Q-learning only. He asserts it for Sarsa and other TD
methods without proof and says nothing about terminal states. The thinnest point is the time limit.
Grześ and Müller and Kudenko both say a state where an episode is cut after a fixed number of steps
must have potential 0, but both treat the cut as a termination. No source I found handles a cut
that the learner bootstraps through, which is how the course treats truncation. The
derivation that bootstrapping keeps the guarantee with Φ(s_T) unchanged is mine, and the writer
has to show it on the page. Ng's "zero net shaping around a cycle" holds exactly only at γ = 1. At
the race's γ = 0.99 the cycle's net shaping is negative for a positive potential. Gymnasium 1.4.0
and stable-baselines3 2.9.2 are current on PyPI as of 2026-11-20.

## Sources

```text
URL:         https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf
             (bibliographic record: https://mlanthology.org/icml/1999/ng1999icml-policy/)
Kind:        primary. Ng, Harada and Russell are the authors of the theorem and its proofs.
             Affiliation as printed: Computer Science Division, University of California, Berkeley.
             Published in Proc. ICML 1999, pp. 278–287 (mlanthology). The PDF is the authors'
             copy on Russell's Berkeley page. It prints no page numbers. Proceedings pages below
             assume PDF page 1 = p. 278 through PDF page 10 = p. 287.
Establishes: firsthand: Theorem 1 (sufficiency and necessity), the sufficiency proof,
             Corollary 2, Remarks 1–2, the necessity proof (Appendix A), the terminal/absorbing
             convention, the grid-world experiments. Merely repeats: the bicycle and soccer-robot
             failures (the bicycle is Randløv and Alstrøm's; the soccer robot is a personal
             communication from David Andre and Astro Teller).
Paraphrase:  - Setup (§2.1, pp. 279–280): MDP M = (S, A, T, γ, R), γ ∈ (0, 1]. For γ = 1, S
               contains one distinguished absorbing state s₀ ("the MDP 'stops' after a transition
               into s₀, with no further rewards thereafter") and all policies are proper.
               "Discounted MDPs have no corresponding absorbing state and are always
               infinite-horizon; note therefore that for them, we can write S − {s₀} = S" (p. 280).
             - Shaping (§2.2, p. 280): learn on M' = (S, A, T, γ, R') with R' = R + F, F bounded.
               Footnote 3: for additive memoryless shaping this is the most general form; a
               non-additive form only adds the freedom to rescale rewards by a positive factor.
             - Bicycle (§1, p. 279): Randløv and Alstrøm gave "positive rewards whenever the agent
               made progress towards the goal. The agent learned to ride in tiny circles near the
               start state because no penalty was incurred for riding away from the goal." Soccer
               robot rewarded for touching the ball learned to stay by it and "vibrate".
             - Cycle intuition (§3, p. 281), explicitly "First focusing on the undiscounted case
               (γ = 1)": a cycle s₁ → … → sₙ → s₁ with positive net shaping can "distract" the
               agent; with F(s, a, s') = Φ(s') − Φ(s) the cycle's sum is 0.
             - Theorem 1 (p. 281): F is potential-based if there is Φ : S → ℝ with
               F(s, a, s') = γΦ(s') − Φ(s) for all s ∈ S − {s₀}, a ∈ A, s' ∈ S (Eq. 2).
               Sufficiency: if F is potential-based, every optimal policy in M' is optimal in M
               and vice versa. Necessity: if F is not potential-based, there exist (proper)
               transition functions T and a reward function R : S × A → ℝ such that no optimal
               policy in M' is optimal in M. For infinite S, Φ must be bounded (p. 281).
             - Scope of necessity (p. 282): it applies when "we have no knowledge of T and R".
               "If we do have intimate knowledge of T, R, then the necessity condition does not
               say much, and it is possible that we might be able to use other shaping functions."
             - Sufficiency proof, key step (pp. 282): for γ = 1, replace Φ by Φ − Φ(s₀) (F is
               unchanged by a constant shift when γ = 1), so assume Φ(s₀) = 0. Subtract Φ(s) from
               both sides of the Bellman optimality equation for Q*_M and rearrange to
               Q*_M(s,a) − Φ(s) = E[R + γΦ(s') − Φ(s) + γ max_a' (Q*_M(s',a') − Φ(s'))]. Define
               Q̂(s,a) = Q*_M(s,a) − Φ(s); Q̂ satisfies M''s Bellman optimality equation, so
               Q*_M' = Q*_M − Φ. Φ(s) does not depend on a, so argmax_a is unchanged. For γ = 1,
               Q̂(s₀, a) = 0 − 0 = 0 uses Φ(s₀) = 0. Reverse direction: same proof with −F.
             - Corollary 2 (p. 282): Q*_M' = Q*_M − Φ and V*_M' = V*_M − Φ, under Φ(s₀) = 0 if γ = 1.
             - Remark 1 (p. 282): the identities "actually hold for arbitrary policies π",
               V^π_M' = V^π_M − Φ, "Although we have not proved it here". Consequence: near-optimal
               policies in M' are near-optimal in M by the same ε.
             - Remark 2 (p. 282): if R itself is γΦ(s') − Φ(s), every policy is optimal.
             - §3 end / §4 (p. 283): choosing Φ = V*_M makes V*_M' ≡ 0; useful Φ need not be close
               to V*_M.
             - Experiments (§4, pp. 283–285): undiscounted grids (10x10, 50x50, 5x5 with five
               flags), −1 per step, 80% intended move / 20% random. Φ₀(s) = −manhattan(s, goal)/0.8
               and 0.5Φ₀; Sarsa, 0.10-greedy, learning rate 0.02; averages over 40 runs (footnote 4,
               p. 284). Both potentials speed learning; on 50x50 the shaped curves "can barely be
               seen". Because these grids are undiscounted, the F used there is Φ(s') − Φ(s).
             - §5 (p. 285): an expert may propose an "undiscounted" Φ(s') − Φ(s) even when γ ≠ 1;
               "Even though our theorem may no longer guarantee optimality in this case, such a
               shaping function may ... still be worth trying". Potential-based F also preserves
               the best policy within a restricted policy class.
             - Necessity proof (Appendix A, pp. 286–287), a sketch for |A| = 2. Lemma 3: if F
               depends on the action for some (s, s'), send both actions to s' with rewards 0 and
               Δ/2; the two MDPs pick different actions. Otherwise F = F(s, s'); fix ŝ₀ (the
               absorbing state if γ = 1), shift so F(ŝ₀, ŝ₀) = 0, set Φ(s) = −F(s, ŝ₀), find
               s₁, s₂ with γΦ(s₂) − Φ(s₁) ≠ F(s₁, s₂), and build the three-state MDP of Fig. 3:
               from s₁, a → ŝ₀ with reward Δ/2, a' → s₂ → ŝ₀, Δ = F(s₁,s₂) + γF(s₂,ŝ₀) − F(s₁,ŝ₀).
               M picks a iff Δ > 0; M' picks a' iff Δ > 0. The proof assumes s₁, s₂, ŝ₀ distinct
               ("the other cases are either impossible or handled similarly") and states for γ < 1
               that "constant offsets of the reward do not affect the optimal policy".
Locators:    §1 p. 279 (bicycle); §2.1 pp. 279–280 (absorbing state); §2.2 p. 280; §3 p. 281
             (cycle intuition, Theorem 1, Eq. 2); p. 282 (necessity scope, sufficiency proof,
             Corollary 2, Remarks 1–2); §4 pp. 283–285 (experiments, Figs. 1–2); §5 p. 285;
             Appendix A pp. 286–287 (Lemma 3, necessity proof, Fig. 3).
Quote:       Eq. 2 as printed: "F(s, a, s') = γΦ(s') − Φ(s)" (p. 281). The γ is in the theorem and
             absent from the γ = 1 intuition paragraph on the same page.
```

```text
URL:         https://www.jair.org/index.php/jair/article/view/10338  (DOI 10.1613/jair.1190)
Kind:        primary. Wiewiora proves the equivalence. Research Note, Journal of Artificial
             Intelligence Research 19 (2003) 205–208; submitted 12/02, published 9/03.
             Affiliation as printed: Department of Computer Science and Engineering, University of
             California, San Diego.
Establishes: firsthand: the two theorems and their conditions; the remark on learning speed.
Paraphrase:  - Uses F(s, s') = γΦ(s') − Φ(s), no action argument (§1, p. 205).
             - Two learners (§2, p. 206): L starts from Q₀(s,a) and receives shaping rewards; L'
               starts from Q₀(s,a) + Φ(s) and receives none. Both run the standard Q-learning
               update with the same α on the same sequence of experiences ⟨s, a, r, s'⟩.
             - Theorem 1 (p. 206; induction proof pp. 206–207): given the same experiences, the
               total change ΔQ(s,a) always equals ΔQ'(s,a). The TD errors are equal term by term.
             - Theorem 2 (p. 207): with an "advantage-based" policy, one whose action
               probabilities in a state depend only on differences of that state's Q-values, L and
               L' have the same distribution over their next action. Greedy, ε-greedy and
               Boltzmann soft-max are advantage-based.
             - Scope: "We prove this result only for the Q-learning algorithm, but the results
               extend to Sarsa and other TD algorithms as well" (p. 206); eligibility traces
               asserted too (§4, p. 208). No proof for those.
             - Learning speed (§3, p. 208): in goal-directed tasks, Q-values initialized below
               optimal can need exploration time exponential in the state-action space before the
               goal is found; optimistic initialization in deterministic environments needs
               polynomial time (citing Koenig and Simmons 1996). "Because potential-based shaping
               is equivalent to Q-value initialization, care must be taken in choosing a potential
               function that does not lead to poor learning performance."
             - Conclusion (§4, p. 208): for discrete states, initialize Q with Φ instead of
               shaping; for continuous state spaces, shaping "may still offer some benefit", and
               a careful analysis is left to future work.
             - Silent on terminal states, function approximation and potentials that change.
Locators:    §1 p. 205; §2 pp. 206–207 (update rules, Theorem 1, advantage-based policy,
             Theorem 2); §3 and §4 p. 208.
Quote:       "we prove that a reinforcement learner with initial Q-values based on the shaping
             algorithm's potential function make the same updates throughout learning as a
             learner receiving potential-based shaping rewards" (abstract, p. 205).
```

```text
URL:         https://www.ifaamas.org/Proceedings/aamas2017/pdfs/p565.pdf
Kind:        primary. Grześ derives the finite-horizon shaped return and the terminal-potential
             condition himself. Marek Grześ, School of Computing, University of Kent. Proc. AAMAS
             2017, pp. 565–573 (printed page numbers on each page).
Establishes: firsthand: Eq. 3, the two-terminal counterexample, the Φ(s_N) = 0 rule including
             time-limit stops, the linear-programming view. Repeats: Ng's theorem; Eck et al.'s
             finite-horizon planning result (not opened).
Paraphrase:  - §3 (p. 566): episodic implementations set V(s_N) = 0 at a terminal state because
               no actions are taken there. Ng et al. "indicated that with γ = 1 the shaping
               rewards have to be zero in all goal states, the issue of the potential function of
               the goal states was not considered."
             - §4.1 (p. 567), Fig. 1: from s_i (Φ = 0), action a₁ enters terminal g₁ (r = 0,
               Φ = 1000) and a₂ enters terminal g₂ (r = 100, Φ = 10). Shaped rewards are γ·1000
               and 100 + γ·10, so shaping flips the choice to g₁ when γ > 10/99.
             - Eq. 3 (p. 567), for a trajectory s₀, a₀, …, s_N that stops at s_N:
               U_Φ(s̄) = Σ_{i=0}^{N−1} γⁱ(R(sᵢ) + γΦ(s_{i+1}) − Φ(sᵢ)) = U(s̄) + γᴺΦ(s_N) − Φ(s₀).
               Φ(s₀) does not depend on any action; γᴺΦ(s_N) does, so it can change the policy.
               "multiple terminal states arise naturally in tasks where the trajectories are
               stopped after a fixed number of steps, because whenever a trajectory is terminated,
               the state at which the termination happens is a terminal state in the sense of Eq.
               3." Holds discounted and undiscounted.
             - §4.1 (p. 568): remedy is Φ(s_N) = 0 for whatever state a trajectory stops in; the
               same state keeps its potential where it is not the last state of a trajectory.
               Intuition: Φ(s_N) = 0 "neutralises" potential accumulated on the way in. Eck et al.
               [8, Thm 4] found invariance only as the horizon goes to infinity when Φ(s_N) ≠ 0.
             - §5 (pp. 570–571): in the discounted, infinite-horizon dual LP, total shaping is
               −Σ Φ(s₀)μ(s₀), a constant, so the policy is unchanged. In the undiscounted
               stochastic-shortest-path LP, the shaping term is Σ over goal states of Φ(g) times
               the flow into g. That term leaves the policy unchanged only if every goal state
               has the same potential C; the paper concludes goal-state shaping must be zero.
             - Conclusion (§6, pp. 571–572): terminal potential must be zero, "This applies also
               to states at which Q-learning or UCT trajectories are terminated."
             - Does not discuss bootstrapping through a time-limit cut.
Locators:    §3 p. 566; §4.1 pp. 567–568 (Fig. 1, Eq. 3, remedy); §4.2 pp. 568–569 (multi-agent
             version); §5 pp. 570–571; §6 pp. 571–572.
Quote:       "the potential function has to be set to zero for a state, s_N, at which a particular
             learning trajectory stops" (p. 568).
```

```text
URL:         http://incompleteideas.net/book/the-book-2nd.html  (PDF: http://incompleteideas.net/book/RLbook2020.pdf)
Kind:        secondary on the shaping theorem and Wiewiora's result, which it reports from
             outside. Primary for its own textbook advice. Sutton and Barto, Reinforcement
             Learning: An Introduction, 2nd ed. (MIT Press, 2018), authors' online PDF. HTTPS on
             this host failed certificate verification from here, so the http address is recorded.
Establishes: firsthand: the authors' advice to put prior knowledge in initial values, Eq. 17.11.
             Repeats: Ng et al.'s aim and Wiewiora's equivalence.
Paraphrase:  - §3.2 p. 54: the reward signal "is not the place to impart to the agent prior
               knowledge about how to achieve what we want it to do"; a chess agent rewarded for
               taking pieces might take them and lose. Footnote 5: "Better places for imparting
               this kind of prior knowledge are the initial policy or initial value function."
             - §14.3 p. 360: Skinner's shaping, reinforcing successive approximations of a desired
               behavior (the bowling pigeon), called powerful for computational RL too.
             - Ch. 14 Bibliographical and Historical Remarks, 14.3, p. 372: lists Randløv and
               Alstrøm (1998) among shaping examples; "Ng (2003) and Ng, Harada, and Russell
               (1999) used the term shaping in a sense somewhat different from Skinner's, focusing
               on the problem of how to alter the reward signal without altering the set of
               optimal policies."
             - §17.4 p. 470: rewarding subgoals "may lead the agent to behave differently from
               what is intended; the agent may end up not achieving the overall goal." Better to
               leave the reward alone and add an initial guess v₀ to the value approximation,
               Eq. 17.11: v̂(s, w) = wᵀx(s) + v₀(s), "though it is not guaranteed to always
               accelerate learning." Then Skinner-style shaping that changes the reward as
               learning proceeds.
             - Ch. 17 Bibliographical and Historical Remarks, 17.4, p. 479: "Skinner's shaping
               should not be confused with the 'potential-based shaping' technique introduced by
               Ng, Harada, and Russell (1999). Their technique has been shown by Wiewiora (2003) to
               be equivalent to the simpler idea of providing an initial approximation to the
               value function, as in (17.11)."
             - The book does not state the theorem, its necessity, or any terminal or time-limit
               condition.
Locators:    pp. 54 (§3.2 and footnote 5), 360 (§14.3), 372 (remarks 14.3), 470 (§17.4, Eq.
             17.11), 479 (remarks 17.4). Page numbers are the printed ones in RLbook2020.pdf.
```

```text
URL:         https://mlanthology.org/icml/1998/randlv1998icml-learning/
             (PDF read at https://gwern.net/doc/reinforcement-learning/model-free/1998-randlov.pdf;
             no publisher copy is online, so the record page is the stable address and the
             mirror is where the text can be read)
Kind:        primary for the bicycle incident. Randløv (CATS, Niels Bohr Institute, University of
             Copenhagen) and Alstrøm ran the experiment. Proc. ICML 1998, pp. 463–471.
Establishes: firsthand: what the bicycle agent did and the authors' two explanations.
Paraphrase:  §4 (p. 468, PDF p. 6): in their first experiments they rewarded driving towards the
             goal without punishing driving away, and the agent "drove in circles with a radius
             of 20–50 meters around the starting point." They give two causes: the reward paid
             for it, and "circles with a certain radius are physically very stable when driving
             a bicycle". Their working reward (p. 467) punishes driving away and rewards driving
             towards the goal, as a function of the heading angle to the goal. It is not
             potential-based.
Locators:    §4, p. 467 (final reward), p. 468 (circles).
Quote:       "Consequently the agent drove in circles with a radius of 20–50 meters around the
             starting point." (p. 468)
```

```text
URL:         https://arxiv.org/abs/2502.01307
Kind:        primary for its own claims. Müller and Kudenko, L3S Research Center, Hannover.
             arXiv v1, 3 Feb 2025; arXiv comment: "accepted as extended abstract at AAMAS 2025".
             On terminal potentials it repeats Grześ (its ref. [5]) and extends the rule to
             truncation.
Establishes: firsthand: the truncation rule as they state it; that badly offset potentials
             trapped some of their runs. Repeats: Grześ's terminal rule.
Paraphrase:  - §3 Background (p. 2): in episodic MDPs terminal Q-values are 0, so "the potential
               function must also be equal to zero in all terminal states to be able to guarantee
               policy invariance [5]. Notably, this includes the state preceding the truncation of
               a training episode after a fixed number of steps."
             - §2 (p. 2): a constant shift of all rewards "can change the optimal policy when
               moving into terminal states of episodic MDPs" (their criticism of Sun et al.).
             - §6.2.1 (p. 6): with a large negative offset, every terminal state, truncation
               included, gets a large positive shaping reward, and "some runs get stuck oscillating
               into the non-goal state the agent has truncated an episode in before."
             - Paper's subject is learning speed: how Φ's offset relative to the initial Q-values
               decides whether shaping helps.
Locators:    §2 and §3, p. 2; §6.2.1, p. 6.
```

```text
URL:         https://arxiv.org/abs/2208.09570
Kind:        primary for its generalized necessity theorem. Jenner, van Hoof and Gleave, arXiv
             preprint, v2 of 2 Dec 2022 (comment: "Fixed mistake in proof that affected several
             results"). No journal reference shown. Optional; use only for the scope of necessity.
Establishes: firsthand: Theorem 3 and its comparison with Ng.
Paraphrase:  §4.4 (PDF p. 5): a conservative (potential) shaping term always preserves optimal
             policies; the converse holds whenever the transition graph has "distinguishing
             actions" (from s, different actions can lead to s' and to s''). They say Ng's
             necessity "requires G to be complete (i.e. T = S × A × S)", meaning Ng assumes nothing
             is known about which transitions exist.
Locators:    §4.4, Theorem 3 and the two paragraphs after it, PDF p. 5.
```

```text
URL:         https://www.ifaamas.org/Proceedings/aamas2012/papers/2C_3.pdf
Kind:        primary. Devlin and Kudenko, Department of Computer Science, University of York.
             "Dynamic Potential-Based Reward Shaping", Proc. AAMAS 2012, pp. 433–440 (page numbers
             from the published version deposited at https://eprints.whiterose.ac.uk/id/eprint/75121/).
             Pointer only; the commission makes dynamic potentials mention-only.
Establishes: firsthand: invariance with a time-varying potential, and loss of the initialization
             equivalence.
Paraphrase:  §3.1 (p. 435): F(s, t, s', t') = γΦ(s', t') − Φ(s, t) keeps the optimal policy (and
             Nash equilibria); their proof telescopes the shaped return to U(s̄) − Φ(s₀, t₀).
             §3.2 (p. 436): with a dynamic potential, shaping "is not equivalent to Q-table
             initialisation", because a Q-table initialized with Φ(s, t₀) cannot follow later
             changes in Φ.
Locators:    §3.1 p. 435; §3.2 p. 436.
```

```text
URL:         https://pypi.org/project/gymnasium/1.4.0/  and  https://pypi.org/project/stable-baselines3/2.9.2/
Kind:        primary. PyPI is the release channel the packages' maintainers publish to.
Establishes: current versions as of 2026-11-20 (PyPI JSON API, read today).
Paraphrase:  gymnasium latest 1.4.0, uploaded 2026-10-05, requires Python ≥ 3.10.
             stable-baselines3 latest 2.9.2, uploaded 2026-10-26, requires Python ≥ 3.10 and
             gymnasium ≥ 0.29.1, < 2.0; numpy ≥ 1.20, < 3.0; torch ≥ 2.8, < 3.0. So 1.4.0 is
             inside its range. sb3-contrib latest 2.9.2 (2026-10-26). torch latest 2.15.0
             (2026-10-28, Python ≥ 3.11). numpy latest 2.5.5 (2026-11-15, Python ≥ 3.12).
Locators:    project pages above; https://pypi.org/pypi/<name>/json.
```

## Contradictions

- **Zero net shaping around a cycle is a γ = 1 fact.** Ng's cycle argument (§3, p. 281) is stated
  "First focusing on the undiscounted case (γ = 1)" with F = Φ(s') − Φ(s). Under Eq. 2 with γ < 1
  (algebra from Eq. 2, mine): the plain sum of F around a cycle s₁ → … → sₙ → s₁ is
  (γ − 1)·Σᵢ Φ(sᵢ), and the discounted sum over one lap starting at s₁ is −(1 − γⁿ)Φ(s₁). Neither
  is 0. Both are negative when Φ > 0. The commission asks the page to show the race loop's net
  shaping around one cycle. At γ = 0.99 the writer has to say which sum is shown and that it is
  negative, not zero. Ng's undiscounted form Φ(s') − Φ(s) at γ < 1 is the case §5 (p. 285) says
  the theorem no longer covers. On a two-state loop s₁ → s₂ → s₁ → … it pays d, −d, d, … with
  d = Φ(s₂) − Φ(s₁), so the endless loop collects d(1 − γ + γ² − …) = d/(1 + γ) (my algebra). That
  is positive whenever the loop's forward move raises the potential.
- **Derivation route.** The commission frames the idea as telescoping along a trajectory. Ng
  proves sufficiency by substituting into the Bellman optimality equation (p. 282). He states the
  every-policy identity V^π_M' = V^π_M − Φ (Remark 1) "Although we have not proved it here". The
  telescoped return is Grześ Eq. 3 (p. 567), for trajectories that stop. Devlin and Kudenko §3.1
  telescope infinite trajectories. Cite Ng for the theorem, and Grześ for the finite-horizon form.
- **What Ng did about terminal states.** Grześ (p. 566) says Ng "did not consider" goal-state
  potentials. That overstates it for Ng's undiscounted case, where the proof sets Φ(s₀) = 0 for
  the single absorbing state without loss of generality (p. 282). It is accurate for several
  terminal states, and for discounted tasks that terminate, which Ng excludes by definition
  (p. 280). Ng's Appendix A remark that "constant offsets of the reward do not affect the optimal
  policy when γ < 1" (p. 287) also relies on the discounted MDP never terminating. Müller and
  Kudenko (p. 2) note the failure of that statement in episodic tasks.
- **Constant terminal potential.** Grześ's LP (§5, p. 571) allows one constant C on all goal
  states at γ = 1, which matches Ng's shift argument. From Eq. 3 (my algebra), at γ < 1 a
  constant C ≠ 0 still changes the comparison, because the extra term γᴺC depends on when a
  policy terminates and is 0 for a policy that never terminates. On the race at 0.99 this term
  enters the comparison of looping against finishing directly.
- **Ng's terminal convention, discounted case (my derivation, not in any source).** Suppose a
  discounted task models termination as Ng's model does: an absorbing state that loops forever
  with R = 0 and keeps paying F = (γ − 1)Φ(s_abs) on each loop. Those payments sum to −γᴺΦ(s_abs)
  from arrival at step N, which cancels the leftover term, so Ng's theorem holds for any
  Φ(s_abs). An implementation that stops the episode on arrival pays none of them, so it needs
  Φ(s_abs) = 0.
- **Time limits: sources versus the course's truncation rule.** Grześ (pp. 567, 572) and Müller
  and Kudenko (p. 2) both require Φ = 0 at the state where a time limit cuts an episode. Both
  treat the cut as a termination, with no bootstrap. The course's termination-and-truncation
  lesson bootstraps at a time-limit cut. My derivation, which no source covers: with the target
  r + γΦ(s_T) − Φ(s_{T−1}) + γ max_a Q'(s_T, a) and Q' converging to Q* − Φ, the target is
  r + γV*(s_T) − Φ(s_{T−1}), so the guarantee holds with Φ(s_T) at its ordinary value. Zeroing Φ
  at the cut while bootstrapping shifts that target by −γΦ(s_T). In the episode's sum of shaped
  rewards, the leftover γ^T Φ(s_T) cancels against the −γ^T Φ(s_T) inside the bootstrapped
  V'(s_T) = V(s_T) − Φ(s_T). Their rule is right for a learner that treats the cut as terminal,
  which the course has already shown solves a different problem. The writer should show this on
  the page with a removal test, not cite it.
- **Wiewiora and terminal states (my derivation).** The note's proof uses the bootstrapped update
  everywhere. When an update enters a terminal state and does not bootstrap, the shaped learner's
  TD error is r + γΦ(s_term) − Φ(s) − Q(s,a), and the initialized learner's is r − Q'(s,a) with
  Q'(s,a) = Q(s,a) + Φ(s). They differ by γΦ(s_term). So the equivalence also needs
  Φ(terminal) = 0. Through a bootstrapped truncation, the TD errors stay equal with Φ(s_T)
  unchanged.
- **Sutton and Barto on Wiewiora.** S&B (p. 479) say Wiewiora showed equivalence to an initial
  value approximation "as in (17.11)", which is the linear function-approximation form.
  Wiewiora proved only tabular Q-learning (p. 206). His conclusion (p. 208) leaves continuous
  state spaces open and says shaping "may still offer some benefit" there. My algebra suggests
  S&B's claim does hold for semi-gradient TD on state values with the additive offset: the TD
  errors match with Φ = v₀ and both gradients are x(s). That rests on my algebra, not on
  Wiewiora's proof.
- **Bicycle.** Ng (p. 279) says "tiny circles near the start state", caused by the missing
  penalty. Randløv and Alstrøm (p. 468) report circles of 20–50 m radius around the start. They
  name a second cause: circles of a certain radius are physically stable on a bicycle. The prior
  lesson's Go deeper row cites Ng's account. If the page describes the circles, use the original's
  numbers.
- **Necessity on a known MDP.** The necessity direction is an existence claim over T and R
  (p. 281). Ng says it "does not say much" when T and R are known (p. 282), and the race's T and R
  are known. Jenner et al. (preprint, §4.4) extend necessity to a known transition graph with
  distinguishing actions. The race's graph has them: from every cell 0–6, back and forward reach
  different cells. Researcher check, not on any page: a throwaway value iteration of the
  2026-11-19 race, finish worth 10, at γ = 0.99. With the finish alone the optimal moves from
  unpaid cells 0–6 are → → → → → → →. Adding the prior lesson's pay-once checkpoint, which is not
  potential-based, changes them to → → ← ← ← ← →: cells 2–5 turn back to collect the checkpoint.
  A Q-learning agent started at cell 0 still finishes, which is what that lesson reported. The
  writer can rerun this check if the necessity sentence wants a concrete case on the course's own
  race.
- **Wiewiora's scope versus the commission.** The commission says "for a class of learners". The
  proof covers tabular Q-learning with the same α and the same experience sequence, and the
  identical-behavior result needs an advantage-based policy. Sarsa, other TD methods and
  eligibility traces are asserted without proof. Nothing covers PPO or other policy-gradient
  agents.

## Numbers

```text
Figure: Ng, Harada and Russell 1999, ICML proceedings pp. 278–287
Owner:  mlanthology record (and Wiewiora 2003's reference list, p. 208)
Scope:  PDF pages 1–10 mapped to pp. 278–287; the author PDF prints no page numbers
```
```text
Figure: Wiewiora 2003, JAIR vol. 19, pp. 205–208
Owner:  the article's own header, p. 205
Scope:  4-page research note
```
```text
Figure: Grześ 2017, AAMAS pp. 565–573
Owner:  printed page numbers in the IFAAMAS PDF
Scope:  9 pages
```
```text
Figure: shaping flips the terminal choice when γ > 10/99 (≈ 0.101)
Owner:  Grześ 2017, §4.1, p. 567
Scope:  Fig. 1 only: Φ(g₁) = 1000, r = 0; Φ(g₂) = 10, r = 100; Φ(s_i) = 0
```
```text
Figure: bicycle circles of radius 20–50 m around the start
Owner:  Randløv and Alstrøm 1998, §4, p. 468
Scope:  their first experiments, before the reward punished driving away
```
```text
Figure: Ng's grid experiments: 40 independent runs per curve; Sarsa, 0.10-greedy, learning rate 0.02; 80% intended move; Φ₀ = −manhattan(s, goal)/0.8 and 0.5Φ₀
Owner:  Ng, Harada and Russell 1999, §4 and footnote 4, p. 284
Scope:  undiscounted 10x10, 50x50 and 5x5-with-flags grids, −1 per step
```
```text
Figure: Sutton and Barto page locators: 54 (§3.2, fn. 5), 360 (§14.3), 372 (remarks 14.3), 470 (§17.4, Eq. 17.11), 479 (remarks 17.4)
Owner:  RLbook2020.pdf printed page numbers
Scope:  2nd edition
```
```text
Figure: gymnasium 1.4.0 (uploaded 2026-10-05); stable-baselines3 2.9.2 (2026-10-26); sb3-contrib 2.9.2 (2026-10-26); torch 2.15.0 (2026-10-28); numpy 2.5.5 (2026-11-15, Python ≥ 3.12)
Owner:  PyPI JSON API, read 2026-11-20
Scope:  latest release of each; SB3 2.9.2 accepts gymnasium ≥ 0.29.1, < 2.0
```
```text
Figure: race, γ = 0.99, optimal moves in unpaid cells 0–6: finish only → → → → → → →; with pay-once checkpoint → → ← ← ← ← →
Owner:  researcher's throwaway value iteration of the rules printed in reinforcement-learning/specification-gaming (race.py); not a source
Scope:  deterministic 8-cell race, finish 10, checkpoint 1 paid once
```

## Limits

- No source addresses potential-based shaping when the learner bootstraps through a time-limit
  cut. The claim that bootstrapping keeps the guarantee with Φ(s_T) unchanged is my derivation
  (Contradictions). The page must derive or run it, not cite it.
- The telescoping derivation the commission centers on is not in Ng's paper. Grześ Eq. 3 prints
  it for stopped trajectories. For infinite discounted trajectories, the vanishing of γᴺΦ(s_N)
  needs bounded Φ, which Ng requires (p. 281) without writing the limit out.
- Wiewiora's equivalence is proven for tabular Q-learning only. Sarsa, other TD methods and
  traces are asserted. Nothing in the note covers function approximation, terminal states or
  SB3's agents.
- "A bad potential can slow learning" has only a qualitative source: Wiewiora p. 208, by way of
  Koenig and Simmons (1996), which I did not open. Müller and Kudenko show runs that got stuck.
  No source gives a number for the race. Any number on the page has to come from the writer's runs.
- Ng's necessity proof is a sketch: |A| = 2, distinct states assumed. Fine for one sentence.
- Proceedings page numbers for Ng are inferred from the 10-page author PDF and the 278–287 range.
  I did not check them against the printed volume. The Berkeley copy is a 2018 Ghostscript
  render of the paper.
- Sutton and Barto never state the theorem, its necessity, or any terminal or time-limit
  condition. Their passages support only the advice to use initial values and the textbook
  pointer to Wiewiora.
- Shaping in language-model RL (mention-only in the commission) was not in the brief and was not
  researched.

## Source assets

```text
Asset: Ng et al., Figure 3, p. 287 (PDF p. 10): three-state MDP s₁, s₂, ŝ₀ used in the necessity proof
Shows: how a shaping term that is not potential-based flips the choice at s₁ between going straight to ŝ₀ and going through s₂
Crop:  keep the whole diagram and its caption (the caption carries "All edges have probability 1" and the Δ/2 reward); omit the proof text around it
```
```text
Asset: Ng et al., Figure 1(a)/(b), p. 283, and Figure 2(a)/(b), p. 284: steps-to-goal against trial number
Shows: shaping with Φ₀ and 0.5Φ₀ cutting learning time on undiscounted grids; Fig. 2(a) is the flag grid
Crop:  the line-style key exists only in the caption ("Dot is no shaping ..."), so the caption must stay with the plot
```
```text
Asset: Grześ 2017, Figure 1, p. 567: s_i with two arrows to terminal states g₁ (Φ = 1000, r = 0) and g₂ (Φ = 10, r = 100)
Shows: the smallest case where a nonzero terminal potential changes the optimal choice
Crop:  keep every Φ and r label and the caption; the γ > 10/99 threshold is in the body text, so state it in the page's caption
```
```text
Asset: Wiewiora 2003: None found (no figures)
Asset: Sutton and Barto passages: None found
Asset: Randløv and Alstrøm 1998: None found for the circles (Figures 9–10 show later routes to the goal, not the circling)
Asset: Müller and Kudenko, Jenner et al., Devlin and Kudenko, PyPI: None found that the lesson needs
```

## Discarded

```text
https://ai.stanford.edu/~ang/papers/shaping-icml99.pdf: same paper on Ng's Stanford page; its text layer is unreadable (Type 3 fonts), so the Berkeley copy is the one to link
https://www.andrewng.org/publications/policy-invariance-under-reward-transformations-theory-and-application-to-reward-shaping/: redirected to a Google Scholar profile, not the paper
https://arxiv.org/pdf/1106.5267: arXiv mirror of Wiewiora's note; the JAIR page is the publisher's
https://eprints.whiterose.ac.uk/75121/2/p433_devlin.pdf: repository deposit of Devlin and Kudenko; used only for page numbers, the IFAAMAS copy is recorded
dblp search API: refused the request with a bot check; mlanthology supplied the page ranges instead
```
