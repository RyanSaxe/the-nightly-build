# evidence.md — paper-of-the-day/instructgpt (researcher/01)

The evidence supports the commissioned reconstruction. The three equations the
writer must set — the reward-model ranking loss, the PPO objective with the
β-KL penalty (and the PPO-ptx pretraining-mix term), and the DPO
reparameterization — are recoverable verbatim from the owning papers and are
mutually consistent: DPO's closed-form optimum is exactly the maximizer of
InstructGPT's KL-regularized objective, which is why the same preference data
admits a classification loss with no explicit reward model. The headline claim
(a 1.3B InstructGPT preferred to the 175B GPT-3) is verified against the paper's
abstract and results, but its evaluation conditions matter and are easy to
misstate: the metric is human *preference* on OpenAI's own API prompt
distribution, judged by ~40 contracted labelers, against a *plain* (un-prompted)
GPT-3 baseline; few-shot prompting the baseline narrows the gap sharply. The
after-record genuinely qualifies durability: Gao et al. show the optimized
reward is a proxy whose *gold* value peaks and then falls with KL budget, and
DPO shows the RL loop InstructGPT introduced is not required to reach the same
optimum. The record is thin in one place by nature: DPO's empirical evidence is
on sentiment/summarization/single-turn dialogue, not full instruction-following
at InstructGPT scale, so "the field moved on" is directionally supported but not
a head-to-head at the same task. All equations below were read in the arXiv
HTML (ar5iv mirror) and cross-checked against the abstract pages; URLs recorded
are the documents' own arXiv pages.

## Sources

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — the focal paper; OpenAI authors own every InstructGPT claim, method, and figure.
Establishes: the three-stage RLHF pipeline (SFT → RM → PPO); the RM ranking loss (Eq. 1);
             the PPO / PPO-ptx objective (Eq. 2); the headline preference result and its
             evaluation conditions; the alignment-tax finding; the self-stated limitations.
Paraphrase:  GPT-3 is fine-tuned in three stages. Stage 1 (SFT) trains on ~13k labeler
             demonstrations. Stage 2 trains a 6B reward model r_θ on human rankings of
             K=4–9 sampled completions per prompt, using a pairwise logistic (Bradley-Terry)
             loss over all C(K,2) comparisons, treated as one batch element per prompt.
             Stage 3 optimizes the policy with PPO to maximize r_θ minus a per-token β-KL
             penalty to the frozen SFT policy; the "-ptx" variant adds a γ-weighted
             pretraining log-likelihood term to limit regression on public NLP tasks.
             In human evaluation on the API prompt distribution, the 1.3B InstructGPT
             (PPO-ptx) is preferred to the 175B GPT-3.
Locators:    Method §3, Eq. 1 (RM loss) and Eq. 2 (RL objective); Results §4.1; Fig. 1, Fig. 2,
             Fig. 3; Fig. 29 (public-NLP regressions); Discussion / Limitations §5.2.
Quote:       Abstract: "In human evaluations on our prompt distribution, outputs from the 1.3B
             parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite
             having 100x fewer parameters."
             §5.2: "This procedure aligns the behavior of GPT-3 to the stated preferences of a
             specific group of people (mostly our labelers and researchers), rather than any
             broader notion of 'human values'."
             §5.2: "Our models are neither fully aligned nor fully safe; they still generate
             toxic or biased outputs, make up facts, and generate sexual and violent content
             without explicit prompting."
             §5.2: "Perhaps the greatest limitation of our models is that, in most cases, they
             follow the user's instruction, even if that could lead to harm in the real world."
```

```text
URL:         https://openai.com/index/instruction-following/
Kind:        primary (authoring party's press release) — but redundant with the paper it announces.
Establishes: the public-facing version of the headline claim and the plain-language method.
Paraphrase:  OpenAI's release states labelers prefer the 1.3B InstructGPT's outputs over the
             175B GPT-3's despite >100x fewer parameters, and describes the SFT-then-RLHF method.
             It adds InstructGPT makes up facts less often and is somewhat less toxic.
Locators:    Blog body, opening result statement and "Methods" summary.
Quote:       "our labelers prefer outputs from our 1.3B InstructGPT model over outputs from a
             175B GPT-3 model, despite having more than 100x fewer parameters."
Note:        Direct WebFetch of this page returned HTTP 403 / DNS failure on the CDN mirror; per
             source policy this is gated, not dead, and the page is the correct address to cite.
             The claim itself is verified against the paper's abstract, which owns it — do not
             lean on the blog as the owner of any number. A canonical archived copy also exists
             at https://cdn.production.openai.com/research/instruction-following (not fetchable
             here). Writer/editor should resolve the live openai.com URL at publication.
```

```text
URL:         https://arxiv.org/abs/2210.10760
Kind:        primary — Gao, Schulman, Hilton own the over-optimization scaling laws firsthand.
Establishes: the functional form of the proxy-vs-gold reward gap as a function of KL, and that
             the gold reward peaks then declines as the policy over-optimizes the proxy.
Paraphrase:  In a synthetic setup a large 6B "gold" reward model stands in for human labels; a
             smaller proxy RM (3M–3B params) is trained on the gold RM's labels and then
             optimized against, by best-of-n (BoN) sampling or by RL/PPO. Gold reward first
             rises, peaks, then falls as optimization pushes the policy further (measured in KL
             from the initial policy). The gold-score curve fits a closed functional form whose
             coefficients vary smoothly (roughly log-linearly) with proxy-RM size and RM-data
             size. Policy size held at 1.2B while RM size is varied.
Locators:    Abstract; §"Functional forms" (Eqs. for R_bon and R_RL); Fig. 1 (BoN and RL panels).
Quote:       (functional forms recorded verbatim in Numbers, below.)
Note:        Submitted 2022-10-19; published ICML 2023 per the field record, though the arXiv
             abstract page does not state the venue — writer should confirm the venue string
             before printing it.
```

```text
URL:         https://arxiv.org/abs/2305.18290
Kind:        primary — Rafailov et al. own the DPO derivation and algorithm.
Establishes: that InstructGPT's KL-regularized RLHF objective has a closed-form optimal policy,
             which reparameterizes into a reward expressed through the policy itself, collapsing
             the two-stage RM+PPO pipeline into a single classification loss over preference pairs.
Paraphrase:  Under a Bradley-Terry preference model (Eq. 1), the standard RLHF objective (Eq. 3;
             identical in form to InstructGPT Eq. 2 without the ptx term) has the analytic optimum
             π_r(y|x) ∝ π_ref(y|x) exp(r(x,y)/β) (Eq. 4). Inverting this gives reward as a function
             of the optimal policy and reference (Eq. 5); substituting into the Bradley-Terry
             likelihood makes the partition function Z(x) cancel, leaving the DPO loss (Eq. 7), a
             logistic loss on the difference of β-scaled log-ratios for chosen vs rejected
             completions. No reward model and no sampling from the policy are needed. Empirically
             DPO matches or beats PPO-based RLHF on sentiment control, summarization, and
             single-turn dialogue.
Locators:    §4 preliminaries (Eq. 1 BT; Eq. 3 objective); §4 "Deriving the DPO objective"
             (Eq. 4 optimum, Eq. 5 reparameterization, Eq. 7 loss); §4 "What does the DPO update
             do?" (gradient and implicit reward r̂_θ).
Quote:       Title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model."
             (equations recorded verbatim in Numbers, below.)
Note:        Published NeurIPS 2023 per the field record; the arXiv page does not print the venue —
             confirm before citing venue/award.
```

```text
URL:         https://arxiv.org/abs/2310.10076
Kind:        primary (for its own claim) / secondary to InstructGPT — Saito, Wachi, Wataoka, Akimoto.
Establishes: that preference labeling carries a verbosity/length bias — judges can prefer longer
             answers of comparable quality — which bears on what a "win rate" measures.
Paraphrase:  Examining RLHF/RLAIF preference labeling, the authors find a verbosity bias where
             longer answers are preferred at similar quality; GPT-4 as a judge shows this more
             strongly than humans. They propose a metric to quantify it.
Locators:    Abstract; the bias definition and the GPT-4-vs-human comparison.
Quote:       "we see that in our problem setting, GPT-4 prefers longer answers more than humans."
Note:        Use only as a named, general caveat on preference win-rate as a metric. It does not
             measure InstructGPT specifically; it does not establish that InstructGPT's win rate
             is driven by length. It supports "the metric has a known confound," not more.
```

## Contradictions

- **The headline's reference point shifts between abstract and figure.** The
  abstract claims 1.3B InstructGPT is preferred to *175B GPT-3*. The main
  win-rate plot (Fig. 1) measures every model's win rate against the *175B SFT*
  model, not against GPT-3. Both are real; do not conflate them. In Fig. 1 the
  1.3B PPO/PPO-ptx curve sits above the 175B GPT and GPT-prompted curves, which
  is the visual form of the headline; the abstract's "preferred to 175B GPT-3"
  is the against-GPT-3 statement. Set the reference explicitly wherever the
  number appears.

- **The gap depends heavily on how the GPT-3 baseline is prompted.** 175B
  InstructGPT is preferred to *plain* 175B GPT-3 85±3% of the time, but only
  71±4% over *few-shot-prompted* 175B GPT-3. The "small model beats big model"
  framing is starkest against the un-prompted baseline; a prompted GPT-3 closes
  much of the distance. The writer should state which baseline the headline
  number uses.

- **The alignment target is explicitly narrow, and the metric is
  distribution-bound.** The paper concedes it aligns to "a specific group of
  people (mostly our labelers and researchers), rather than any broader notion
  of 'human values'" (§5.2), and the evaluation runs on OpenAI's own API prompt
  distribution — skewed toward open-ended generation, brainstorming, and chat,
  not academic benchmarks. Training-labeler agreement is only 72.6±1.5%
  (held-out labelers 77.3±1.3%). This is a preference-on-a-distribution result,
  not a capability, correctness, or truthfulness result. Fig. 3 splits results
  by prompt source (submitted-to-GPT vs submitted-to-InstructGPT) and by labeler
  pool partly to test this dependence; the win persists across those splits, but
  the metric's scope stands.

- **Preference win-rate carries a length/style confound.** Saito et al. (2023,
  arXiv:2310.10076) document verbosity bias in preference labeling. InstructGPT
  outputs tend to be longer and more formatted than raw GPT-3 completions, so
  some of the win rate may reflect style the labelers reward rather than task
  quality. This is a caveat on the metric, not a measured attribution to
  InstructGPT.

- **Over-optimization: "more reward" is not "more aligned."** Gao et al. (2023)
  show the RM the PPO stage optimizes is a proxy whose *gold* value rises, peaks,
  then falls as KL from the initial policy grows. This makes the β-KL term and
  early stopping load-bearing rather than incidental: without the KL leash (or
  with too weak a β), the policy Goodharts the proxy and the true objective
  degrades. The result qualifies the pipeline's durability. Caveat on the
  after-record itself: Gao's setup is synthetic — a large gold RM substitutes
  for humans — so it bounds proxy-RM error, not human-preference error.

- **DPO shows the RL loop is optional, but its evidence is off-task from
  InstructGPT.** DPO reaches the same KL-regularized optimum with a
  classification loss and no reward model or sampling, evidence the field's
  practice moved off the exact SFT→RM→PPO pipeline. But DPO's experiments cover
  sentiment control, summarization, and single-turn dialogue — not
  full-distribution instruction-following at 175B scale — so it is not a
  head-to-head refutation of InstructGPT's pipeline at InstructGPT's task.
  Follow-on work also reports DPO has its own pathologies, notably length
  exploitation (Park et al. 2024, arXiv:2403.19159 — seen in search only, NOT
  independently opened; the writer must read it before citing). Present "the
  field moved on" as directional, not as a demonstrated superiority at the same
  benchmark.

## Numbers

The equations the reconstruction must set (transcribe faithfully; these are the
owning papers' exact forms):

```text
Figure: RM ranking loss (InstructGPT Eq. 1):
          loss(θ) = − (1 / C(K,2)) · E_{(x, y_w, y_l) ~ D} [ log σ( r_θ(x, y_w) − r_θ(x, y_l) ) ]
        where σ is the logistic sigmoid; r_θ(x,y) is the scalar reward for prompt x, completion y;
        y_w is the preferred and y_l the dispreferred completion; C(K,2) = K-choose-2; K ∈ [4,9]
        responses ranked per prompt; all C(K,2) pairs from a prompt form one batch element.
Owner:  arXiv:2203.02155, Eq. 1 (§3.5).
Scope:  reward model is 6B params; trained on human rankings; single scalar head on the SFT model.
```

```text
Figure: RL / PPO objective with β-KL and γ-ptx term (InstructGPT Eq. 2):
          objective(φ) = E_{(x,y) ~ D_{π_φ^RL}} [ r_θ(x,y) − β · log( π_φ^RL(y|x) / π^SFT(y|x) ) ]
                         + γ · E_{x ~ D_pretrain} [ log( π_φ^RL(x) ) ]
        π_φ^RL is the learned policy; π^SFT the frozen SFT policy; β the KL-penalty coefficient;
        γ the pretraining-mix coefficient. For plain "PPO" models γ = 0; "PPO-ptx" sets γ > 0.
Owner:  arXiv:2203.02155, Eq. 2 (§3.5).
Scope:  the objective is maximized (PPO); the middle term is a per-token KL penalty to the SFT policy.
```

```text
Figure: DPO chain — the writer needs these to show why the same optimum is a closed form:
          Bradley-Terry (Eq. 1):  p*(y1 ≻ y2 | x) = exp(r*(x,y1)) / ( exp(r*(x,y1)) + exp(r*(x,y2)) )
          KL-regularized objective (Eq. 3):
              max_{π_θ}  E_{x~D, y~π_θ}[ r_φ(x,y) ] − β · D_KL[ π_θ(y|x) ‖ π_ref(y|x) ]
          Optimal policy in closed form (Eq. 4):
              π_r(y|x) = (1/Z(x)) · π_ref(y|x) · exp( (1/β) · r(x,y) ),   Z(x) = Σ_y π_ref(y|x) exp((1/β) r(x,y))
          Reward reparameterization (Eq. 5):
              r(x,y) = β · log( π_r(y|x) / π_ref(y|x) ) + β · log Z(x)
          DPO loss (Eq. 7):
              L_DPO(π_θ; π_ref) = − E_{(x,y_w,y_l)~D} [ log σ( β log( π_θ(y_w|x)/π_ref(y_w|x) )
                                                          − β log( π_θ(y_l|x)/π_ref(y_l|x) ) ) ]
          Implicit reward (§4):  r̂_θ(x,y) = β · log( π_θ(y|x) / π_ref(y|x) )
          Gradient (§4): ∇_θ L_DPO = − β · E_{(x,y_w,y_l)~D} [ σ( r̂_θ(x,y_l) − r̂_θ(x,y_w) ) ·
                                        ( ∇_θ log π_θ(y_w|x) − ∇_θ log π_θ(y_l|x) ) ]
Owner:  arXiv:2305.18290, Eqs. 1, 3, 4, 5, 7 and §4 gradient.
Scope:  the partition function Z(x) cancels between Eq. 5 substituted into Eq. 1, which is why the
        loss needs π_ref but no reward model and no sampling. Eq. 3 equals InstructGPT Eq. 2 with γ=0.
```

```text
Figure: Over-optimization functional forms (Gao et al.):
          Best-of-n:  R_bon(d) = d · ( α_bon − β_bon · d )
          RL/PPO:     R_RL(d)  = d · ( α_RL  − β_RL · log d )
        where d := sqrt( D_KL( π ‖ π_init ) ), the square-root of KL (in nats) from the initial policy;
        R is the GOLD reward-model score; α, β are fitted coefficients that scale smoothly with
        proxy-RM parameter count and RM-data size. Both curves rise then fall in d.
Owner:  arXiv:2210.10760, functional-forms section; coefficients differ by optimization method.
Scope:  proxy RM 3M–3B params; gold RM 6B; policy fixed at 1.2B; main RM-size runs use ~90k comparisons.
```

Headline / evaluation figures the argument depends on:

```text
Figure: 1.3B InstructGPT preferred over 175B GPT-3 (≈100x fewer params).
Owner:  arXiv:2203.02155, abstract + Fig. 1.
Scope:  human preference on OpenAI's API prompt distribution; InstructGPT = PPO-ptx; baseline = 175B GPT-3.
```

```text
Figure: 85 ± 3%.
Owner:  arXiv:2203.02155, §4.1. Scope: fraction of time 175B InstructGPT outputs preferred to PLAIN 175B GPT-3.
```

```text
Figure: 71 ± 4%.
Owner:  arXiv:2203.02155, §4.1. Scope: 175B InstructGPT preferred to FEW-SHOT-prompted 175B GPT-3.
```

```text
Figure: labeler inter-annotator agreement — 72.6 ± 1.5% (training labelers); 77.3 ± 1.3% (held-out).
Owner:  arXiv:2203.02155, §3/§4. Scope: agreement rate on preference comparisons; ~40 contractors (Upwork + Scale AI).
```

```text
Figure: K = 4 to 9 ranked responses per prompt; RM size = 6B; policy sizes shown = 1.3B, 6B, 175B.
Owner:  arXiv:2203.02155, §3.4–3.5. Scope: comparison-collection and model-size sweep.
```

## Source assets

```text
Asset: Figure 2 — the three-step method diagram (Step 1 SFT on labeler demonstrations; Step 2 RM
       training on ranked comparisons; Step 3 PPO against the RM). arXiv:2203.02155, §3.
Shows: the whole SFT → RM → PPO pipeline in one image — the article's spine. It makes concrete
       where the RM loss (Step 2) and the KL-penalized objective (Step 3) each live.
Crop:  keep all three numbered panels and their captions (demonstration → ranking → PPO reward
       loop); do not crop to a single step, since the argument is the sequence. Caption verbatim:
       "A diagram illustrating the three steps of our method: (1) supervised fine-tuning (SFT),
       (2) reward model (RM) training, and (3) reinforcement learning via proximal policy
       optimization (PPO) on this reward model."
```

```text
Asset: Figure 1 — human-preference win rate by model size and variant (GPT, GPT-prompted, SFT,
       PPO, PPO-ptx at 1.3B / 6B / 175B), win rate measured against the 175B SFT model.
       arXiv:2203.02155.
Shows: the headline visually — the 1.3B PPO/PPO-ptx curve sits above the 175B GPT and
       GPT-prompted curves; PPO variants dominate SFT and raw GPT across all sizes.
Crop:  must retain the y-axis (win rate vs 175B SFT), the model-size x-axis, all five variant
       curves, and the 95% CI error bars. The reference model (175B SFT, not GPT-3) must remain
       legible in the caption so the number is not misread as "vs GPT-3." Caption: "Human
       evaluations of various models on our API prompt distribution, evaluated by how often
       outputs from each model were preferred to those from the 175B SFT model."
```

```text
Asset: Gao et al. Figure 1 — gold vs proxy reward as a function of sqrt(KL), for BoN (left) and
       RL (right), with a family of curves for different proxy-RM sizes. arXiv:2210.10760.
Shows: over-optimization directly — each gold curve rises, peaks, then declines while the proxy
       score keeps climbing; the peak arrives later/higher for larger RMs. This is the figure that
       carries the "the KL leash is load-bearing" argument.
Crop:  keep both panels (BoN and RL differ in functional form), the sqrt-KL x-axis with its unit
       (nats) and the note that it is a square-root scale, the reward-score y-axis, and enough of
       the curve family to show the size trend. Do not crop to one RM size — the scaling is the point.
```

```text
Asset: Figure 29 (appendix) — zero-shot performance on public NLP datasets (SQuAD, DROP,
       HellaSwag, WMT15 fr→en) showing the PPO regression and its recovery under PPO-ptx.
       arXiv:2203.02155. OPTIONAL — bring only if the article spends the alignment-tax paragraph.
Shows: the "alignment tax": plain PPO regresses on these benchmarks; PPO-ptx (the γ term)
       mitigates it and even surpasses GPT-3 on HellaSwag. Makes the γ term in Eq. 2 concrete.
Crop:  keep axis labels and the PPO-vs-PPO-ptx-vs-GPT-3 comparison per dataset; retain dataset names.
```

```text
Asset: DPO Figure 1 — reward/KL frontier on sentiment (DPO dominates PPO's achievable reward at a
       given KL). arXiv:2305.18290. OPTIONAL / probably OMIT.
Shows: DPO reaches equal-or-higher reward at lower KL than PPO on the sentiment task.
Crop:  n/a — recommend omitting. The commissioned DPO angle is the closed-form math (Eqs. 4–7),
       not the empirical frontier, and this figure is on sentiment, not instruction-following.
       Flagging its existence so the orchestrator can decide; default is to keep DPO purely mathematical.
```

## Discarded

```text
URL: https://cdn.production.openai.com/research/instruction-following — CDN mirror of the OpenAI
     blog; DNS/fetch failed here. Not the citable address (use openai.com/index/instruction-following/);
     content redundant with the paper abstract, which owns the claim.
URL: https://www.oxen.ai/blog/training-language-models-to-follow-instructions-instructgpt — secondary
     tutorial write-up; not opened for facts. Rejected: no claim it owns; paper is the source.
URL: https://www.freecodecamp.org/news/ai-paper-review-...-instructgpt/ — secondary explainer. Rejected.
URL: https://github.com/natashamessier/instruct_gpt_presentation — third-party slide deck. Rejected.
URL: https://exchange.scale.com/public/blogs/openais-instructgpt-2022-11-18 — vendor blog. Rejected;
     Scale AI was a labeling vendor, not an authoring party to the claims.
URL: https://arxiv.org/pdf/2403.19159 (Park et al., DPO length exploitation) — appeared in search as a
     lead for the DPO-pathology caveat; NOT opened. Left out of Sources; flagged in Contradictions so
     the writer opens it before citing.
```
