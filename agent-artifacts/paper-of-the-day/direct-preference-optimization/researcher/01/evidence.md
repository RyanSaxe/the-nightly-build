# Evidence record: paper-of-the-day/direct-preference-optimization (01)

The evidence strongly supports the reconstruction the commission asks for. The DPO
paper's own text gives every equation the derivation leans on in closed form: the
KL-constrained objective (Eq. 3), its optimal policy (Eq. 4), the reward
reparameterization (Eq. 5), the Bradley-Terry substitution that cancels the
partition function (Eq. 6), the final loss (Eq. 7), and the gradient with its
per-example weight. The appendix carries the full proofs, the reward-equivalence-class
argument behind the "secretly a reward model" title, and the Plackett-Luce
extension. The experimental claim — DPO matches or beats PPO-based RLHF on sentiment,
summarization, and dialogue — is documented with specific figures and win rates, and
the figures the claim turns on are identified below for capture. Where the evidence is
thinner is the paper's own generalization claim: its out-of-distribution result (Table 1)
rests on one small transfer test the authors themselves flag as preliminary, and the
after-the-fact record contradicts the optimistic reading of it. The later literature
(Azar/IPO, Xu et al., Tang et al., Pal et al./DPOP) does not overturn DPO's central
theorem — nobody disputes that DPO optimizes the same KL-constrained objective in
principle — but it establishes, with primary sources, that offline DPO diverges from
on-policy RLHF in practice, that its loss can drive down the likelihood of the very
responses it prefers, and that with the reward model's regularization folded away DPO can
overfit near-deterministic preferences. The strongest honest tension for the writer is
internal to the record: DPO's Table 1 shows DPO generalizing *better* than PPO
out-of-distribution, while Xu et al. later argue the opposite. Both are recorded in full
below.

A note on venues: I read every paper's full text through the arXiv HTML rendering
(ar5iv) and recorded the canonical arXiv abstract page as each source's address. Venue
labels for KTO and Xu et al. are confirmed in-text; for IPO, Smaug/DPOP, and Tang et al.
the arXiv page did not display the conference line and I have labeled them by their arXiv
identifier plus the venue I am confident of, flagged where uncertain.

## Sources

```text
URL:         https://arxiv.org/abs/2305.18290
Kind:        primary. It is the paper the article reconstructs; it owns the DPO
             derivation, the algorithm, and all reported experimental results.
Establishes: The full DPO derivation and every headline result. Authors (in order):
             Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon,
             Christopher D. Manning, Chelsea Finn. Venue: NeurIPS 2023. arXiv history:
             v1 29 May 2023, v2 13 Dec 2023, v3 29 Jul 2024.
Paraphrase:  The standard RLHF pipeline (fit a reward model to preferences, then
             optimize the policy against it with RL under a KL penalty) can be replaced
             by a single supervised classification loss on preference pairs, with no
             explicit reward model and no RL loop. A change of variables expresses the
             reward as a function of the policy and the reference policy; substituting
             it into the Bradley-Terry model cancels the partition function and leaves a
             loss over the policy alone. The method provably targets the same
             KL-constrained reward-maximization objective as RLHF.
Locators:    Abstract; §1 Introduction; §3 Preliminaries (Eqs. 1-3); §4 Deriving DPO
             (Eqs. 4-7 and the gradient); §5 Theoretical Analysis; §6 Experiments;
             Appendix A (proofs). Figures 1-3, Table 1, Appendix Table 3.
Quote:       Abstract, verbatim: "In this paper we introduce a new parameterization of
             the reward model in RLHF that enables extraction of the corresponding
             optimal policy in closed form, allowing us to solve the standard RLHF
             problem with only a simple classification loss. ... Notably, fine-tuning
             with DPO exceeds PPO-based RLHF in ability to control sentiment of
             generations, and matches or improves response quality in summarization and
             single-turn dialogue while being substantially simpler to implement and
             train."
```

Exact equations, transcribed from the paper (equation numbers as printed):

- Eq. (1) Bradley-Terry preference model:
  `p*(y1 ≻ y2 | x) = exp(r*(x,y1)) / ( exp(r*(x,y1)) + exp(r*(x,y2)) )`
- Eq. (2) Reward-model loss (negative log-likelihood of a logistic/BT classifier):
  `L_R(r_φ, D) = -E_{(x,y_w,y_l)~D}[ log σ( r_φ(x,y_w) - r_φ(x,y_l) ) ]`
- Eq. (3) KL-constrained reward-maximization objective (the RLHF objective):
  `max_{π_θ}  E_{x~D, y~π_θ(y|x)}[ r_φ(x,y) ]  -  β · D_KL[ π_θ(y|x) || π_ref(y|x) ]`
- Eq. (4) Closed-form optimal policy of Eq. (3):
  `π_r(y|x) = (1/Z(x)) · π_ref(y|x) · exp( (1/β) r(x,y) )`,
  with partition function `Z(x) = Σ_y π_ref(y|x) exp( (1/β) r(x,y) )`.
  The paper's point: Z(x) sums over all possible completions y and so is intractable to
  compute, which is why Eq. (4) "is still hard to utilize in practice."
- Eq. (5) Reward reparameterization (solve Eq. 4 for r):
  `r(x,y) = β · log( π_r(y|x) / π_ref(y|x) ) + β · log Z(x)`
- Eq. (6) Bradley-Terry under the reparameterization — the intractable Z(x) cancels
  because it is identical for y1 and y2 at the same x:
  `p*(y1 ≻ y2 | x) = 1 / ( 1 + exp( β log(π*(y2|x)/π_ref(y2|x)) - β log(π*(y1|x)/π_ref(y1|x)) ) )`
  `             = σ( β log(π*(y1|x)/π_ref(y1|x)) - β log(π*(y2|x)/π_ref(y2|x)) )`
- Eq. (7) The DPO loss (a binary-cross-entropy objective over the policy only):
  `L_DPO(π_θ; π_ref) = -E_{(x,y_w,y_l)~D}[ log σ( β log(π_θ(y_w|x)/π_ref(y_w|x)) - β log(π_θ(y_l|x)/π_ref(y_l|x)) ) ]`
- Gradient of the DPO loss (with implicit reward `r̂_θ(x,y) = β log(π_θ(y|x)/π_ref(y|x))`):
  `∇_θ L_DPO(π_θ; π_ref) = -β · E_{(x,y_w,y_l)~D}[ σ( r̂_θ(x,y_l) - r̂_θ(x,y_w) ) · ( ∇_θ log π(y_w|x) - ∇_θ log π(y_l|x) ) ]`

Gradient interpretation, quoted verbatim from §4: the weight `σ(r̂_θ(x,y_l) - r̂_θ(x,y_w))`
is labeled "higher weight when reward estimate is wrong"; the two inner terms are labeled
"increase likelihood of y_w" and "decrease likelihood of y_l." The surrounding prose:
"the examples are weighed by how much higher the implicit reward model r̂_θ rates the
dispreferred completions, scaled by β, i.e, how incorrectly the implicit reward model
orders the completions, accounting for the strength of the KL constraint. Our experiments
suggest the importance of this weighting, as a naïve version of this method without the
weighting coefficient can cause the language model to degenerate (Appendix Table 3)."

Appendix derivation (Appendix A), transcribed structure:
- A.1 derives Eq. (4) by rewriting Eq. (3) as a minimization of
  `D_KL( π(y|x) || π*(y|x) ) - log Z(x)`, where `π*` is the Eq. (4) form; since KL is
  minimized at 0 and Z(x) does not depend on π, the optimum is π = π*. This is the proof
  that Eq. (4) is the exact optimal policy.
- A.2 defines the reward-equivalence class: two reward functions are equivalent iff they
  differ by a function of x alone, `r'(x,y) = r(x,y) + f(x)`; the paper shows two
  equivalent rewards induce the same Bradley-Terry (and Plackett-Luce) preference
  distribution and the same optimal policy under Eq. (3), and that the map
  `f(r; π_ref, β)(x,y) = r(x,y) - β log Σ_y π_ref(y|x) exp((1/β) r(x,y)) = β log(π_r(y|x)/π_ref(y|x))`
  is a bijection onto the class. This is the formal content of the title claim ("your
  language model is secretly a reward model"): the policy log-ratio *is* a reward in the
  equivalence class, so no separate reward network is needed.
- A.3 extends the same argument to the Plackett-Luce model for rankings of K responses,
  giving the general DPO loss over permutations τ.

```text
URL:         https://arxiv.org/abs/2310.12036
Kind:        primary for its own theorem. It owns the ΨPO/IPO analysis and the claim
             about DPO's overfitting; it is secondary as a *characterization of DPO*
             (it reports on someone else's method), but the failure-mode result is its
             own contribution and firsthand.
Establishes: A theoretical account of when DPO overfits. Title: "A General Theoretical
             Paradigm to Understand Learning from Human Preferences." Authors: Mohammad
             Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele
             Calandriello, Michal Valko, Rémi Munos. Venue: AISTATS 2024 (not shown on
             the arXiv page; arXiv 2310.12036, submitted 18 Oct 2023).
Paraphrase:  DPO makes two approximations RLHF-with-a-reward-model does not: it assumes
             pairwise preferences can be substituted by pointwise Bradley-Terry rewards,
             and it fits the policy directly on an empirical (often near-deterministic)
             preference dataset. When the empirical preference between two completions is
             deterministic or close to it (one always preferred), the BT/logistic
             transform sends the target log-ratio toward infinity, so the KL
             regularization stops binding and the optimal empirical policy is driven
             toward a deterministic policy regardless of β. IPO (Identity-PO, Ψ set to
             the identity) is an offline loss defined directly on pairwise preferences
             that regularizes the policy log-ratio toward a bounded margin, so the KL
             term keeps binding and the policy does not collapse.
Locators:    Abstract; the ΨPO section defining the general objective; the sub-section
             on DPO as a special case and its overfitting; the IPO section.
Quote:       (Closely paraphrased from the paper's argument, not a verbatim quote — the
             fetched rendering did not preserve exact sentence boundaries.) IPO is
             empirically shown to avoid DPO's collapse on illustrative bandit-style
             examples where preferences are deterministic.
```

```text
URL:         https://arxiv.org/abs/2402.01306
Kind:        primary for KTO's method and its head-to-head numbers against DPO.
Establishes: A DPO alternative that needs only unpaired binary labels. Title: "KTO:
             Model Alignment as Prospect Theoretic Optimization." Authors: Kawin
             Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, Douwe Kiela.
             Venue: ICML 2024 (confirmed in-text).
Paraphrase:  KTO is a "human-aware loss" (HALO) grounded in Kahneman-Tversky prospect
             theory. It maximizes a utility of generations rather than the log-likelihood
             of preferences, and needs only a binary desirable/undesirable signal per
             example, not paired (chosen, rejected) comparisons. Across scales from 1B to
             30B parameters KTO matches or exceeds DPO, and it tolerates data imbalance
             that paired methods cannot. KTO frames DPO itself as one HALO among several,
             so the choice of alignment loss is an inductive-bias choice.
Locators:    Abstract; the HALO/utility section; the experiments across 1B-30B.
Quote:       "matches or exceeds the performance of preference-based methods"; KTO
             "directly maximizes the utility of generations instead of maximizing the
             log-likelihood of preferences, as current methods do."
```

```text
URL:         https://arxiv.org/abs/2404.10719
Kind:        primary for its own comparison study; firsthand experiments pitting tuned
             PPO against DPO.
Establishes: That properly-tuned on-policy PPO can beat DPO, and a theoretical account
             of why DPO can go wrong. Title: "Is DPO Superior to PPO for LLM Alignment?
             A Comprehensive Study." Authors: Shusheng Xu, Wei Fu, Jiaxuan Gao, Wenjie
             Ye, Weilin Liu, Zhiyu Mei, Guangju Wang, Chao Yu, Yi Wu. Venue: ICML 2024
             (confirmed in-text).
Paraphrase:  DPO can find policies that exploit responses lying outside the
             preference-data distribution. Theoretically, the set of policies DPO can
             reach is a superset of those PPO can reach, and the extra ones include
             out-of-distribution exploitative solutions; DPO is therefore more exposed
             to the distribution shift between the preference data and the model's own
             outputs. Empirically, with careful tuning PPO surpasses DPO across the
             benchmarks tested, including a hard code-competition benchmark
             (CodeContests) where PPO reaches state-of-the-art.
Locators:    Abstract; the theory section on DPO's reachable policies; the empirical
             sections on dialogue and code.
Quote:       "PPO is able to surpass other alignment methods in all cases and achieve
             state-of-the-art results in challenging code competitions." The paper states
             DPO "may have fundamental limitations."
```

```text
URL:         https://arxiv.org/abs/2402.13228
Kind:        primary for the likelihood-decrease failure mode and the DPOP fix.
Establishes: That standard DPO can lower the likelihood of the preferred response.
             Title: "Smaug: Fixing Failure Modes of Preference Optimisation with
             DPO-Positive." Authors: Arka Pal, Deep Karkhanis, Samuel Dooley, Manley
             Roberts, Siddartha Naidu, Colin White. Venue: arXiv 2402.13228 (submitted
             20 Feb 2024; conference line not shown).
Paraphrase:  The DPO loss depends only on the *relative* log-ratio between chosen and
             rejected, so it can be reduced by pushing down the log-probability of the
             chosen completion as long as the rejected one falls faster. This drives the
             absolute likelihood of the preferred response down, and it is worst when the
             two completions in a pair have small edit distance (common in real
             datasets). DPOP (DPO-Positive) adds a term that penalizes the chosen
             log-probability for dropping below its reference value. DPOP outperforms DPO
             across datasets and was used to train Smaug-72B, reported as the first
             open-source model above 80% average on the HuggingFace Open LLM Leaderboard.
Locators:    Abstract; the failure-mode analysis; the DPOP definition; results.
Quote:       "the standard DPO loss can lead to a reduction of the model's likelihood of
             the preferred examples, as long as the relative probability between the
             preferred and dispreferred classes increases"; the effect is acute "in
             datasets in which the edit distance between pairs of completions is low."
```

```text
URL:         https://arxiv.org/abs/2405.08448
Kind:        primary for its own online-vs-offline comparison.
Establishes: That online/on-policy alignment outperforms offline DPO at matched budgets.
             Title: "Understanding the performance gap between online and offline
             alignment algorithms." Authors: Yunhao Tang, Daniel Zhaohan Guo, Zeyu Zheng,
             Daniele Calandriello, Yuan Cao, Eugene Tarassov, Rémi Munos, Bernardo Ávila
             Pires, Michal Valko, Yong Cheng, Will Dabney (Google DeepMind). Venue: arXiv
             2405.08448 (submitted 14 May 2024; ICML 2024).
Paraphrase:  Online alignment methods (sampling from the current policy during training)
             hold a clear and persistent advantage over offline ones such as standard
             DPO. Offline-trained policies become good at pairwise classification but
             worse at generation; online-trained policies are the reverse. The gap
             survives both contrastive and non-contrastive losses and is not closed by
             scaling the policy network, which points at on-policy sampling itself as the
             active ingredient rather than the loss form.
Locators:    Abstract; the opening comparison experiments; the ablations over loss type
             and scale.
Quote:       "the performance discrepancy persists for both contrastive and
             non-contrastive loss functions" and "appears not to be addressed by simply
             scaling up policy networks."
```

## Contradictions

- **DPO's own OOD claim vs. Xu et al.** The DPO paper's Table 1 (§6.3) reports DPO
  *generalizing better* than PPO on out-of-distribution CNN/DailyMail articles (DPO
  0.36/0.31 vs PPO 0.26/0.23 at temperatures 0 and 0.25). The paper hedges it: "our
  initial results suggest that DPO policies can generalize similarly to PPO-based models,
  but more comprehensive study is needed." Xu et al. (2404.10719) later argue the
  opposite direction — that DPO is *more* exposed to distribution shift and can exploit
  out-of-distribution responses, and that tuned PPO beats DPO. These are not a clean
  refutation of each other: DPO's Table 1 is one small transfer of a single trained pair
  of policies, evaluated by GPT-4 against ground-truth summaries; Xu et al. run a broader,
  harder benchmark suite with heavy PPO tuning. The writer should present DPO's OOD result
  as the preliminary result its authors called it, and Xu et al. as the fuller later test
  that reads the shift the other way.

- **"Matches PPO" (DPO paper) vs. the online/offline gap (Tang et al., Xu et al.).** The
  DPO paper's claim is that DPO optimizes the *same objective* as RLHF and empirically
  matches or beats PPO on its three tasks. Tang et al. and Xu et al. do not dispute the
  objective-level equivalence; they establish that in practice on-policy sampling gives
  online RLHF an edge offline DPO does not close. The distinction to preserve: DPO's
  theorem is about the optimum of the objective; the later work is about what each
  algorithm actually reaches with finite data and no on-policy sampling.

- **The KL regularization: binding vs. not (Azar/IPO).** The DPO paper presents β as
  controlling how far the policy drifts from π_ref. Azar et al. show that on
  near-deterministic empirical preferences the effective regularization can vanish and the
  policy collapses toward determinism regardless of β. This complicates, without negating,
  DPO's KL story: the constraint is exact for the true preference distribution but can be
  hollowed out by the finite, hard-labeled dataset DPO trains on.

- **DPO's gradient claim vs. the likelihood-decrease finding (Pal et al.).** The DPO
  paper says the update "increases the likelihood of the preferred completions y_w and
  decreases the likelihood of dispreferred completions y_l." Pal et al. show the first
  half can fail: the loss only needs the *relative* margin to grow, so the chosen
  completion's absolute likelihood can fall. The paper's own description is of intent, not
  a guarantee about absolute log-probabilities, and it does not report chosen-response
  log-probabilities over training; the later work supplies the gap.

## Numbers

```text
Figure: DPO summarization win rate ≈ 61% at sampling temperature 0.0
Owner:  DPO paper (Rafailov et al., 2305.18290), §6.2 and Figure 2 (right)
Scope:  Reddit TL;DR test split; GPT-J SFT policy; win rate vs human-written reference
        summaries; GPT-4 as evaluator; averaged over test prompts.
```
```text
Figure: PPO summarization win rate 57% at its optimal sampling temperature (0.0)
Owner:  DPO paper, §6.2 and Figure 2 (right)
Scope:  Same TL;DR test setup and evaluator as the DPO 61% figure; same GPT-J SFT base.
```
```text
Figure: DPO (temp 0.25) preferred 58% of the time over PPO (temp 0) in human evaluation
Owner:  DPO paper, §6.2 (reported), human study in §6.4
Scope:  Head-to-head human preference judgments on TL;DR summarization samples.
```
```text
Figure: Out-of-distribution GPT-4 win rate vs ground-truth summaries (CNN/DailyMail)
        DPO 0.36 (temp 0), 0.31 (temp 0.25); PPO 0.26 (temp 0), 0.23 (temp 0.25)
Owner:  DPO paper, §6.3, Table 1
Scope:  Policies trained on Reddit TL;DR, evaluated zero-transfer on CNN/DailyMail news
        articles; GPT-4 win rate against ground-truth summaries.
```
```text
Figure: Sentiment control — DPO attains the highest expected reward at every KL value
Owner:  DPO paper, §6.1, Figure 2 (left)
Scope:  IMDb movie-review prefixes; GPT-2-large SFT; preference pairs generated from a
        pre-trained sentiment classifier so the ground-truth reward is known and the
        reward-vs-KL frontier is exactly computable. Baselines include PPO and PPO-GT
        (PPO with access to the ground-truth reward).
```
```text
Figure: Anthropic-HH dialogue — DPO is the only method whose win rate exceeds the
        dataset's chosen responses
Owner:  DPO paper, §6.2, Figure 3 (left)
Scope:  Anthropic Helpful-Harmless dataset (170k dialogues), one-step human-assistant
        subset of the test split; Pythia-2.8B; GPT-4 evaluator; baseline is the
        preferred response in the test set; compared against Best-of-128 and a 2-shot
        Pythia-2.8B prompt.
```
```text
Figure: Naïve loss without the per-example weight causes the model to degenerate
Owner:  DPO paper, Appendix Table 3
Scope:  Ablation removing the σ(r̂_θ(x,y_l) - r̂_θ(x,y_w)) weighting coefficient from the
        DPO gradient; establishes the weighting is load-bearing.
```
```text
Figure: DPOP-trained Smaug-72B > 80% average on the HuggingFace Open LLM Leaderboard
Owner:  Pal et al. (2402.13228)
Scope:  Reported as the first open-source model above 80% average on that leaderboard;
        supports DPOP over DPO, not a direct DPO win rate.
```

## Source assets

```text
Asset: Figure 1 (page 1) — schematic contrasting the RLHF pipeline (reward model + RL)
       with DPO (direct preference classification into the policy).
Shows: The whole thesis in one image: RLHF's two stages (fit reward model, then RL under
       KL) versus DPO's single classification objective on preference pairs. It settles
       what DPO removes from the pipeline.
Crop:  Keep both halves side by side and their loss labels ("reward model" / "maximum
       likelihood"); the contrast is the content. Omit nothing that distinguishes the two
       pipelines.
```
```text
Asset: Figure 2, Left (§6.1) — reward-vs-KL frontier for IMDb sentiment control.
Shows: DPO's curve sits above every other method (including PPO and PPO-GT) at every KL
       value, i.e. more reward for the same drift from the reference. This is the figure
       the "exceeds PPO in sentiment control" claim turns on, and it is clean because the
       reward is a known ground-truth classifier.
Crop:  Retain both axes (x = KL divergence to π_ref, y = expected reward) and the full set
       of labeled method curves, so DPO's dominance over PPO/PPO-GT is visible. Do not
       crop out the PPO-GT curve — its presence is what makes the frontier claim strong.
```
```text
Asset: Figure 2, Right (§6.2) — TL;DR summarization win rate vs sampling temperature.
Shows: DPO peaks near 61% and stays high across temperatures; PPO peaks near 57% at
       temperature 0 and collapses toward the base model at higher temperatures. Settles
       both the "matches/beats PPO" and the "more temperature-robust" claims.
Crop:  Keep the temperature x-axis, the win-rate y-axis, and the DPO, PPO, and Best-of-N
       curves; the comparison is the point.
```
```text
Asset: Figure 3, Left (§6.2) — Anthropic-HH one-step dialogue win rates by method.
Shows: DPO is the only method above the dataset's chosen-response baseline; supports the
       dialogue claim.
Crop:  Retain the baseline reference line (the "chosen" level) and all method bars/points
       so DPO's position above the line is legible.
```
```text
Asset: Table 1 (§6.3) — out-of-distribution CNN/DailyMail win rates, DPO vs PPO.
Shows: A four-number table: DPO 0.36/0.31 vs PPO 0.26/0.23 at temperatures 0 and 0.25.
       This is the paper's OOD generalization evidence, and the exact table a writer needs
       to set against Xu et al.'s later contrary reading.
Crop:  It is a small table; reproduce it as furniture (a table), not an image crop.
```
```text
Asset: Appendix Table 3 — degeneration of the naïve, unweighted objective.
Shows: The per-example weighting in the DPO gradient is necessary, not cosmetic; without
       it the model degenerates.
Crop:  Reproduce the relevant rows as a small table if used.
```
Follow-up papers (IPO, KTO, Xu et al., Pal et al., Tang et al.): no single figure carries
their claim better than a sentence and a number; the argument in each is textual or a
table of win rates. `None found` for a decisive standalone visual asset from these.

## Discarded

```text
URL: https://ar5iv.org/abs/2305.18290 — redirect only; not the source's own page. Used
     https://ar5iv.labs.arxiv.org/html/2305.18290 as the reading transport and recorded
     the canonical https://arxiv.org/abs/2305.18290 as the source address.
```
No source was read far enough to reject on the merits. Candidate later works beyond the
six recorded (e.g. Rafailov et al.'s "From r to Q*", further RLHF-vs-DPO surveys) were not
opened, to keep the record a reconstruction-and-assessment rather than a survey of
preference-optimization methods, per the commission's boundary. If the editor wants the
token-level MDP reinterpretation of DPO, that is the paper to add next.
