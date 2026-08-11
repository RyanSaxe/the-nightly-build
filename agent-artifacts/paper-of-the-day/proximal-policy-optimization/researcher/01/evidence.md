# Evidence: paper-of-the-day/proximal-policy-optimization (01)

The record fully supports the reconstruction the commission asks for. Every PPO
equation the article leans on (the ratio, the CPI surrogate, the clipped
objective and its epsilon, the KL-penalty variant, the combined actor-critic
loss, the truncated-GAE advantage, Algorithm 1) is verified against the PPO PDF
itself, along with the hyperparameters and the two ablation tables. The angle is
solid: Engstrom et al. own two firsthand, quantified findings that the article
turns on, namely that code-level optimizations, not the clipped objective,
carry most of PPO's measured margin over TRPO, and that PPO's clipping does not
hold the ratio trust region it was designed to enforce. Both are checked against
their tables and figure captions. What is thinner is the "how far does it
generalize" contradiction: the strongest documented pushback is not a paper that
refutes Engstrom but the internal tension that PPO's own controlled ablation
picks clipping at epsilon=0.2 as the best surrogate, that Andrychowicz et al.
independently recommend the PPO loss and find it best on the hardest tasks, and
that Engstrom's own footnote concedes PPO strictly contains its no-clip variant.
No source read disputes PPO's practical dominance. One caution the writer must
respect: Engstrom's trust-region finding is specifically about the ratio, PPO
does keep mean KL below TRPO's bound in the same experiment, so "PPO leaves its
trust region" is only true of the ratio, not the KL.

## Sources

```text
URL:         https://arxiv.org/abs/1707.06347
Kind:        primary. Schulman, Wolski, Dhariwal, Radford, Klimov (OpenAI) own
             the clipped-objective claim and every PPO equation and result.
Establishes: PPO's advertised mechanism and training loop, firsthand.
Paraphrase:  PPO alternates between sampling and several epochs of minibatch SGD
             on a surrogate whose clipped probability ratio forms a pessimistic
             (lower-bound) estimate of policy performance. The clipped surrogate
             is presented as the paper's primary objective; the KL-penalty
             variant is included as a baseline and reported as worse. In the
             paper's own controlled comparison of surrogates, clipping at
             epsilon=0.2 scores best.
Locators:    Abstract and Sec.1 (p.1); ratio and L^CPI Eq.6, L^CLIP Eq.7,
             epsilon=0.2 and Fig.1 (Sec.3, p.3); KL-penalty Eq.8 and adaptive
             beta rule (Sec.4, p.4); combined loss Eq.9, truncated GAE Eq.10-12,
             Algorithm 1 (Sec.5, p.5); surrogate ablation Table 1 (Sec.6.1, p.6);
             continuous-control curves Fig.3 (Sec.6.2, p.7); Atari wins Table 2
             (Sec.6.4, p.8); hyperparameters Tables 3-5 (App.A, p.10).
Quote:       "clipped probability ratios, which forms a pessimistic estimate
             (i.e., lower bound) of the performance of the policy" (p.1).
             Fig.1 caption: "Plots showing one term (i.e., a single timestep) of
             the surrogate function L^CLIP as a function of the probability ratio
             r, for positive advantages (left) and negative advantages (right).
             The red circle on each plot shows the starting point for the
             optimization, i.e., r = 1."

Equations verified verbatim from the PDF (plain-text transcription):
  Ratio:      r_t(theta) = pi_theta(a_t|s_t) / pi_theta_old(a_t|s_t), so
              r_t(theta_old) = 1.                                        (Eq.6 context)
  L^CPI:      L^CPI(theta) = Ehat_t[ r_t(theta) Ahat_t ].               (Eq.6)
  L^CLIP:     L^CLIP(theta) =
              Ehat_t[ min( r_t(theta) Ahat_t,
                           clip(r_t(theta), 1-eps, 1+eps) Ahat_t ) ].   (Eq.7)
              epsilon a hyperparameter, "say, eps = 0.2".
  KL penalty: L^KLPEN(theta) =
              Ehat_t[ r_t(theta) Ahat_t - beta*KL[pi_theta_old, pi_theta] ]. (Eq.8)
              Adaptive: d = Ehat_t[ KL[pi_theta_old, pi_theta] ];
              if d < d_targ/1.5, beta <- beta/2; if d > d_targ*1.5, beta <- beta*2.
  Combined:   L^{CLIP+VF+S}_t(theta) =
              Ehat_t[ L^CLIP_t(theta) - c1 L^VF_t(theta) + c2 S[pi_theta](s_t) ], (Eq.9)
              L^VF_t = (V_theta(s_t) - V^targ_t)^2, S = entropy bonus.
  Trunc GAE:  Ahat_t = delta_t + (gamma*lambda) delta_{t+1} + ...
                       + (gamma*lambda)^{T-t+1} delta_{T-1},            (Eq.11)
              delta_t = r_t + gamma V(s_{t+1}) - V(s_t).                (Eq.12)
  Algorithm 1 (Actor-Critic Style): for iteration=1,2,...:
     for actor=1..N: run pi_theta_old for T timesteps; compute Ahat_1..Ahat_T;
     optimize surrogate L wrt theta with K epochs and minibatch size M <= NT;
     theta_old <- theta.
```

```text
URL:         https://arxiv.org/abs/2005.12729
Kind:        primary. Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph,
             Madry (MIT / Two Sigma) own the code-level-optimization ablation
             and the trust-region-violation measurement. ICLR 2020 (OpenReview
             id r1etN1rtPB); arXiv abs page read and recorded.
Establishes: firsthand, that code-level optimizations carry most of PPO's reward
             margin over TRPO and that PPO's clipping does not enforce a ratio
             trust region.
Paraphrase:  The standard PPO implementation adds nine optimizations absent from
             (or only barely described in) the paper: value-function clipping,
             reward scaling, orthogonal initialization with layer scaling, Adam
             learning-rate annealing, reward clipping, observation normalization,
             observation clipping, tanh activations, and global gradient
             clipping. In a full 2x2x... ablation of the first four and a
             step-vs-optimization ablation across Walker2d/Hopper/Humanoid,
             adding the optimizations raises reward more than switching the core
             step (PPO vs TRPO) does. PPO-NoClip, keeping the optimizations but
             dropping clipping, beats PPO-Minimal (clipping without
             optimizations) on all three tasks. Measured over training, PPO's
             maximum probability ratio consistently exceeds 1+epsilon (violates
             the ratio trust region) while its mean KL stays below TRPO's 0.07
             bound.
Locators:    Nine optimizations listed Sec.3 (p.3); value-clipping and reward-
             scaling formulas Sec.3 items 1-2 (p.3); ablation histograms Fig.1
             and algorithm table Table 1 (p.4); PPO objective Eq.2, ratio Eq.3,
             piecewise gradient of L_PPO (Sec.4, p.5); trust-region figure Fig.2
             (p.6); step-vs-optimization ablation Table 2 with AAI/ACLI
             (Sec.5, p.7); PPO-NoClip Table 3 (p.8).
Quote:       Abstract: code-level optimizations are "responsible for most of
             PPO's gain in cumulative reward over TRPO" and "fundamentally change
             how RL methods function." p.2: "the PPO code-optimizations are more
             important in terms of final reward achieved than the choice of
             general training algorithm (TRPO vs. PPO). This result is in stark
             contrast to the previous view that the central PPO clipping method
             drives the gains." p.7: "the clipping mechanism is not necessary to
             achieve high performance -- we find that PPO-NoClip performs
             uniformly better than PPO-M." Fig.2 caption: "the PPO variants'
             maximum ratios consistently violate the ratio 'trust region'";
             "both PPO and PPO-M constrain the KL well (compared to the TRPO
             bound of 0.07)."
```

```text
URL:         https://arxiv.org/abs/1811.02553
Kind:        primary. Ilyas, Engstrom, Santurkar, Tsipras, Janoos, Rudolph,
             Madry own the companion analysis. Same group, ICLR 2020.
Establishes: firsthand, that PPO/TRPO gradient estimates, value fits, and
             surrogate landscapes diverge from what the motivating theory
             predicts.
Paraphrase:  In the ~2,000 state-action-pair regime that standard
             implementations use, estimated gradients correlate poorly with the
             "true" gradient (approximated from ten million pairs), sometimes at
             zero or negative correlation, and correlation degrades as tasks get
             harder and training proceeds. The value network solves its
             supervised regression (low GAE-loss MRE) but the learned value is
             off by about 50% against the true value function; as a baseline it
             reduces gradient variance far less than the true value would, though
             far more than no baseline. Late in training, in the low-sample
             regime, increasing the surrogate objective can decrease true reward.
Locators:    Contributions list (p.1-2); gradient cosine-similarity Fig.1-2 and
             "poor estimates" claim (Sec.2.1, p.2-3); value MRE Fig.3 and
             "off by about 50%", baseline variance Fig.4 (Sec.2.2, p.4-5);
             surrogate-vs-true landscapes Fig.5-7 (Sec.2.3, p.6-7); gap
             conclusion (Sec.3 and Sec.5, p.7-8).
Quote:       Fig.3 caption: "the learned value function is off by about 50% with
             respect to the underlying true value function." Abstract: "the
             surrogate objective does not match the true reward landscape,
             learned value estimators fail to fit the true value function, and
             gradient estimates poorly correlate with the 'true' gradient."
```

```text
URL:         https://arxiv.org/abs/1502.05477
Kind:        primary. Schulman, Levine, Moritz, Jordan, Abbeel own the trust-
             region method PPO approximates. ICML 2015.
Establishes: what "trust region" means and the constrained update PPO replaces
             with a clip.
Paraphrase:  TRPO maximizes a surrogate (the importance-weighted advantage,
             identical to L^CPI) subject to a bound on the KL divergence between
             the new and old policies. This descends from a monotonic-improvement
             guarantee: the true return is lower-bounded by the surrogate minus a
             penalty proportional to the max KL. Because the theoretical penalty
             forces tiny steps, the practical algorithm uses a hard mean-KL
             constraint delta and solves it with conjugate-gradient / natural-
             gradient steps and a line search.
Locators:    eta, L_pi local approximation Eq.3 and first-order match Eq.4
             (p.2); monotonic-improvement bound Theorem 1 / Eq.8-9, Algorithm 1
             (p.3); KL-constrained update Eq.11 and mean-KL heuristic Eq.12
             (p.3); single-path / vine estimation (Sec.5, p.4).
Quote:       Eq.11 (transcribed): maximize_theta L_theta_old(theta) subject to
             Dbar_KL(theta_old, theta) <= delta.
```

```text
URL:         https://arxiv.org/abs/1506.02438
Kind:        primary. Schulman, Moritz, Levine, Jordan, Abbeel own GAE, the
             advantage estimator PPO uses. ICLR 2016.
Establishes: how PPO forms its advantages and the bias-variance knob lambda.
Paraphrase:  GAE(gamma, lambda) is the exponentially weighted sum of TD
             residuals. lambda trades bias for variance: lambda=0 gives the
             one-step TD residual, lambda=1 gives the empirical return minus the
             value baseline. PPO's Eq.11 is the truncated form of this estimator.
Locators:    TD residual delta^V_t and gamma-just estimators Eq.10-15 (Sec.3,
             p.4); GAE definition Eq.16 and special cases Eq.17-18 (p.5).
Quote:       Eq.16 (transcribed): Ahat^{GAE(gamma,lambda)}_t =
             sum_{l=0..inf} (gamma*lambda)^l delta^V_{t+l},
             delta^V_t = r_t + gamma V(s_{t+1}) - V(s_t).
```

```text
URL:         https://arxiv.org/abs/2006.05990
Kind:        primary for its own large-scale study; secondary as commentary on
             PPO. Andrychowicz et al. (Google Research, Brain Team).
Establishes: independent evidence that both cuts of the debate hold: non-
             algorithmic choices matter enormously, and the PPO clipped loss is
             a strong default. Angle-breaking source.
Paraphrase:  Training >250,000 agents across five MuJoCo tasks (Hopper-v1,
             Walker2d-v1, HalfCheetah-v1, Ant-v1, Humanoid-v1) over >50
             configurable choices, the study's "most surprising finding" is that
             the policy initialization scheme (centering the initial action
             distribution near zero with small std, rarely mentioned in papers)
             strongly influences performance -- corroborating Engstrom's
             initialization result. It also finds the PPO policy loss best on 4
             of 5 environments and best on the two hardest tasks (Humanoid, Ant),
             and attributes the gain to trust-region behavior present in all the
             losses it tested, not to clipping specifically. Recommends the PPO
             loss with clipping threshold ~0.25.
Locators:    Setup and ">250,000 agents", five environments (Sec.2, p.2-3);
             "most surprising finding" on initialization (p.2); policy-loss
             comparison Fig.1, interpretation and recommendation (Sec.3.1, p.4);
             initial action-std Fig.2, init recommendation (Sec.3.2, p.5).
Quote:       p.4: "PPO performs better than the other losses on 4 out of 5
             environments"; "trust-region optimization ... which is present in
             all the other policy losses is crucial for good sample complexity."
             Recommendation: "Use the PPO policy loss. Start with the clipping
             threshold set to 0.25 but also try lower and higher values if
             possible."
```

```text
URL:         https://arxiv.org/abs/1709.06560
Kind:        secondary for this article. Henderson, Islam, Bachman, Pineau,
             Precup, Meger own their own reproducibility study, but here they
             frame the brittleness both Madry-lab papers build on. AAAI 2018.
Establishes: the background fact that deep-RL results are hard to reproduce and
             sensitive to codebase and seed, which is why attributing PPO's gain
             to a mechanism is hard in the first place.
Paraphrase:  Non-determinism in benchmarks plus variance intrinsic to the
             methods makes state-of-the-art deep-RL results hard to reproduce and
             hard to compare; the paper calls for significance metrics and
             tighter reporting. Both Engstrom papers cite it as motivation.
Locators:    Abstract; the paper is cited by Engstrom (Sec.1) and Closer Look
             (Sec.1) as the brittleness precedent.
Quote:       Abstract: "reproducing results for state-of-the-art deep RL methods
             is seldom straightforward."
```

```text
URL:         https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
Kind:        secondary. Huang, Dossa, Raffin, Kanervisto, Wang (CleanRL /
             Stable-Baselines3 maintainers), ICLR 2022 Blog Track. Reports on and
             aggregates the debate rather than owning a new controlled result.
Establishes: the practitioner/maintainer view that PPO is the field's standard
             on-policy baseline and that faithful reproduction requires the
             scattered implementation details -- context for "undisputed
             dominance" and for how the details travel across libraries.
Paraphrase:  Catalogs 37 implementation details needed to reproduce PPO with
             high fidelity across libraries (Stable-Baselines3, CleanRL,
             Tianshou, RLlib, SpinningUp), and affirms Engstrom's and
             Andrychowicz's findings rather than disputing them. Treats PPO as
             dominant enough to warrant book-length documentation.
Locators:    Blog body: reproduction difficulty; the 37-detail catalog;
             references to Engstrom et al. (2020) and Andrychowicz et al. (2021).
Quote:       Purpose stated as helping people "reproduce past results with high
             fidelity"; notes Engstrom et al. found PPO's clipped objective "to
             have similar performance to TRPO's objective when they controlled
             other implementation details to be the same."
```

## Contradictions

The angle survives, but the material that tests it is real and must be
steelmanned, not waved past.

1. **PPO's own ablation picks clipping.** The reexamination's headline is that
   clipping is not what carries the margin, yet the PPO paper's own controlled
   comparison of surrogates (Table 1) scores clipping at epsilon=0.2 highest
   (0.82 normalized), above every KL-penalty variant (0.62-0.74) and far above
   no-clipping/no-penalty (-0.39). Within the PPO paper's experiment, on its
   task set, clipping is the best surrogate. Engstrom does not deny this; it
   reframes what "best surrogate on that experiment" is worth once the
   surrounding code is held equal.

2. **Engstrom's own containment caveat.** Footnote 6 (p.8) concedes PPO-NoClip
   "can only express a subset [of] the training algorithms covered by PPO, as
   the latter leaves the clipping severity epsilon to be a free parameter." So
   "clipping is unnecessary" means "a tuned no-clip run matches PPO here," not
   "clipping can never help." The writer must not upgrade the finding to the
   stronger claim.

3. **Andrychowicz independently endorses the PPO loss.** A separate Google
   large-scale study recommends the PPO clipped loss and finds it best on the
   two hardest tasks. Its reading is subtler than either camp: the value comes
   from *trust-region behavior shared by all the losses it tried*, and clipping
   is a good, simple way to get that behavior. This both complicates "clipping
   is irrelevant" and corroborates "unglamorous choices dominate" (its own most
   surprising finding is the initialization scheme).

4. **The trust-region result is about the ratio, not the KL.** Engstrom Fig.2
   shows PPO's *maximum probability ratio* routinely exceeds 1+epsilon, but also
   that PPO's *mean KL* stays below TRPO's 0.07 bound. "PPO does not stay in its
   trust region" is accurate for the ratio the clip acts on and misleading for
   KL. All three algorithms fail to hold a ratio-based trust region; TRPO holds
   a mean-KL one nearly by construction.

5. **No source disputes PPO's dominance.** Andrychowicz calls PPO "probably the
   most commonly used on-policy RL algorithm at the moment"; the Huang blog
   documents PPO as the shared baseline across every major library. The "gap"
   the article describes is between advertised and operative mechanism, not
   between PPO and a better method.

What is *not* in the record: a paper that flatly claims the code-level findings
fail to generalize. The honest state is that later work refines and partially
redirects (Andrychowicz: shared trust-region behavior, not clipping per se; the
practitioner blog: the details are real and portable), rather than refuting.

## Numbers

```text
Figure: epsilon = 0.2 (default clipping range 1-eps .. 1+eps)
Owner:  PPO (Schulman et al. 2017), Sec.3 Eq.7 and Table 1
Scope:  stated default; MuJoCo runs use 0.2, Atari uses 0.1*alpha (annealed)

Figure: PPO continuous-control surrogate ablation, avg normalized score (0=random,
        1=best), 7 MuJoCo tasks x 3 seeds, 1M steps, 21 runs averaged:
          No clipping or penalty   -0.39
          Clipping eps=0.1          0.76
          Clipping eps=0.2          0.82  (best)
          Clipping eps=0.3          0.70
          Adaptive KL d_targ=0.003  0.68
          Adaptive KL d_targ=0.01   0.74
          Adaptive KL d_targ=0.03   0.71
          Fixed KL beta=0.3         0.62
          Fixed KL beta=1           0.71
          Fixed KL beta=3           0.72
          Fixed KL beta=10          0.69
Owner:  PPO, Table 1 (p.6). beta initialized at 1.
Scope:  normalized within each environment then averaged over 21 runs

Figure: PPO Atari games "won" (metric averaged over 3 trials), 49 games:
          by avg reward over all training:   A2C 1, ACER 18, PPO 30, Tie 0
          by avg reward over last 100 eps:   A2C 1, ACER 28, PPO 19, Tie 1
Owner:  PPO, Table 2 (p.8)
Scope:  49 ALE games, 40M frames (10M timesteps)

Figure: PPO MuJoCo hyperparameters -- Horizon 2048, Adam 3e-4, epochs 10,
        minibatch 64, gamma 0.99, GAE lambda 0.95
Owner:  PPO, Table 3 (p.10)
Scope:  1M-timestep continuous-control benchmark

Figure: PPO Atari hyperparameters -- Horizon 128, Adam 2.5e-4*alpha, epochs 3,
        minibatch 32*8=256, gamma 0.99, lambda 0.95, actors 8,
        clip eps 0.1*alpha, VF coeff c1=1, entropy coeff c2=0.01
        (alpha linearly annealed 1 -> 0)
Owner:  PPO, Table 5 (p.10)
Scope:  ALE benchmark

Figure: Engstrom step-vs-optimization ablation, final reward with 95% CI
        [bootstrap, >=80 agents], MuJoCo:
                     Walker2d-v2          Hopper-v2            Humanoid-v2
          PPO       3292 [3157,3426]     2513 [2391,2632]     806 [785,827]
          PPO-M     2735 [2602,2866]     2142 [2008,2279]     674 [656,695]
          TRPO      2791 [2709,2873]     2043 [1948,2136]     586 [576,596]
          TRPO+     3050 [2976,3126]     2466 [2381,2549]    1030 [979,1083]
          AAI        242                   99                  224
          ACLI       557                  421                  444
Owner:  Engstrom et al. 2020, Table 2 (p.7)
Scope:  AAI = max{|PPO-TRPO+|,|PPO-M-TRPO|} (effect of switching step);
        ACLI = max{|PPO-PPO-M|,|TRPO+-TRPO|} (effect of adding optimizations).
        On all three tasks ACLI > AAI.

Figure: code-level optimizations give PPO and TRPO 17% and 21% reward gains on
        Hopper-v2 respectively
Owner:  Engstrom et al. 2020, Sec.5 (p.7)
Scope:  Hopper-v2, PPO vs PPO-M and TRPO+ vs TRPO

Figure: PPO-NoClip vs PPO vs PPO-M, final reward with 95% CI:
                     Walker2d-v2          Hopper-v2            Humanoid-v2
          PPO       3292 [3157,3426]     2513 [2391,2632]     806 [785,827]
          PPO(base) 3424                 2316                  --
          PPO-M     2735 [2602,2866]     2142 [2008,2279]     674 [656,695]
          PPO-NoClip 2867 [2701,3024]    2371 [2316,2424]     831 [798,869]
Owner:  Engstrom et al. 2020, Table 3 (p.8)
Scope:  PPO-NoClip > PPO-M on all three; on Humanoid PPO-NoClip (831) > PPO (806)

Figure: TRPO KL trust-region bound delta = 0.07 (Engstrom's TRPO setting);
        PPO/PPO-M mean KL stay below it while their max ratio exceeds 1+eps
Owner:  Engstrom et al. 2020, Fig.2 (p.6)
Scope:  Humanoid-v2 training run, KL measured every ~5 steps over state-action pairs

Figure: learned value function off by ~50% (returns MRE) vs true value, while its
        GAE-based supervised loss MRE is small
Owner:  Ilyas/Engstrom et al. 2018 (Closer Look), Fig.3 (p.4)
Scope:  Walker2d-v2 heldout state-action pairs

Figure: standard gradient-estimation sample regime ~2,000 state-action pairs;
        estimated gradient poorly correlated (sometimes ~0 or negative) with the
        "true" gradient computed from ~10^7 pairs
Owner:  Closer Look, Fig.1-2 (p.2-3)
Scope:  MuJoCo Humanoid; Walker2d/Hopper similar, slightly better

Figure: Andrychowicz study scale -- >50 choices, >250,000 agents, 5 MuJoCo tasks
Owner:  Andrychowicz et al. 2020, Abstract / Sec.2
Scope:  Hopper-v1, Walker2d-v1, HalfCheetah-v1, Ant-v1, Humanoid-v1
```

## Source assets

```text
Asset: PPO Figure 1 -- the two-panel plot of L^CLIP for one timestep vs the
       probability ratio r, positive advantage (left) and negative advantage
       (right), with a red circle at r=1 and dashed lines at 1-eps and 1+eps.
       Lives on p.3 of arXiv:1707.06347.
Shows: exactly how the clip works and why min() makes the objective a lower
       bound -- the update gets no credit for pushing r past 1+eps (A>0) or below
       1-eps (A<0), but full penalty in the harmful direction. This is the single
       figure that carries the reconstruction of the mechanism.
Crop:  keep both panels together (the asymmetry between A>0 and A<0 is the point),
       both axis labels (L^CLIP and r), the 1-eps / 1+eps markers, and the red
       r=1 starting circles. Do not crop to one panel.

Asset: PPO Figure 3 -- seven MuJoCo learning curves (HalfCheetah, Hopper,
       InvertedDoublePendulum, InvertedPendulum, Reacher, Swimmer, Walker2d) over
       1M timesteps comparing PPO(Clip) to A2C, A2C+Trust Region, CEM, Vanilla PG
       Adaptive, and TRPO. Lives on p.7.
Shows: PPO's original evidence that it matches or beats prior policy-gradient
       methods across continuous control -- the "practical dominance" the article
       must grant before weighing the reexamination.
Crop:  must retain the algorithm legend and the axes (return vs timesteps to 1M).
       A representative subset of panels is acceptable if the legend is kept, but
       do not drop the PPO and TRPO curves.

Asset: Engstrom Figure 1 -- 2x4 grid of 1-CDF(Reward) curves, Humanoid-v2 (top)
       and Walker2d-v2 (bottom), each column toggling one optimization
       (value clipping, reward normalization, Adam LR annealing, initialization)
       True vs False. Lives on p.4 of arXiv:2005.12729.
Shows: that individual code-level optimizations shift the whole reward
       distribution -- reward normalization, Adam annealing, and initialization
       each move it substantially. This is the "unglamorous tricks matter"
       evidence in one image.
Crop:  keep the True/False legend and the reward x-axis; retain at least the
       reward-normalization and initialization columns (largest effects). Keep
       both environment rows if space allows, to show the effect is not one-task.

Asset: Engstrom Figure 2 -- four panels for Humanoid-v2 (mean reward, maximum
       ratio, mean KL, mean KL on heldout), curves for TRPO, PPO, PPO-M, with the
       1+eps ratio constraint drawn as a dotted line. Lives on p.6.
Shows: the trust-region-violation finding -- PPO's and PPO-M's maximum ratios
       climb past 1+eps (the clip does not hold the ratio region), while their
       mean KL stays under TRPO's 0.07 bound. The figure is what keeps the
       article's claim precise (ratio violated, KL not).
Crop:  the maximum-ratio panel is essential and must keep the 1+eps dotted line
       and the TRPO/PPO/PPO-M legend; pair it with the mean-KL panel so the
       ratio-vs-KL distinction is visible. Do not show only the reward panel.

Asset: PPO Table 1 (surrogate ablation) and Engstrom Table 2 (AAI/ACLI) are
       tabular, not figures. Better rebuilt as the article's own furniture (a
       small table) than captured as images; the Numbers section above carries
       the exact values.

Asset: Closer Look Figure 3 (value MRE ~50%) and Figure 2 (gradient cosine
       similarity vs sample count) are available on p.4 and p.2-3 of
       arXiv:1811.02553 if the article spends the theory-practice-gap thread;
       optional, since the core angle rests on Engstrom's two results.
Shows:  the deeper "methods don't behave as theory predicts" evidence.
Crop:   Fig.3 must keep the returns-MRE panel and its y-axis; Fig.2 must keep the
        x=2K sample-regime marker and the true-gradient-similarity y-axis.
```

## Discarded

```text
https://ar5iv.labs.arxiv.org/html/1707.06347 : not a source, a rendering route.
  ar5iv could not convert this paper and fell back to a PDF view, so it returned
  navigation only. Read the arXiv PDF instead; recorded the abs page as the URL.
https://iclr.iro.umontreal.ca/.../ppo-implementation-details/ : a mirror of the
  37-details blog surfaced in search; rejected for the canonical
  iclr-blog-track.github.io page, which is the source's own home.
https://www.researchgate.net/publication/366139498 , https://docs.cleanrl.dev/... ,
  https://araffin.github.io/publication/ppo-iclr/ : secondary pointers to the same
  blog surfaced in search; not opened, nothing they add over the canonical page.
```
