# Evidence: feature/muon-fine-tuning-crossover (researcher 01)

The paper (arXiv:2611.03633v1, CMU, submitted 2 November 2026) supports the commissioned finding inside its own range. For OLMo-style dense models from 30M to 600M parameters, Muon reaches lower pretraining loss in every cell it reports. Past a crossover budget, though, the AdamW-pretrained model has the better learning-forgetting frontier, and the crossover token-to-parameter ratio (TPR) falls with model size on all four fine-tuning sets. The scouted figures are exact: on StackMathQA the crossover is 320 TPR at 30M and 10 TPR at 600M (Section 3.2; Table 2). The fall depends heavily on the fine-tuning set. From 30M to 600M the crossover falls 8x on Alpaca, 16x on GSM8K (and the 600M value is censored at the smallest budget), 32x on StackMathQA and 64x on MusicPile. The paper prints crossovers only on a doubling grid of budgets, with no seeds or error bars for any language-model run. Converted to tokens, every crossover lies between 2.4B and 19.2B tokens, and the pooled log-log slope of crossover TPR against size is -0.97. That is close to what a fixed token count would give, a reading the paper does not offer. Every Muon-pretrained production model with published counts (Moonlight, Kimi Linear, Trinity Nano/Mini/Large, Kimi K2, GLM-4.5, GLM-5) sits at 475 to 10,000 TPR on active parameters and 15 to 1,667 TPR on total parameters. At 2B to 1T parameters they are 4 to 1,700 times larger than the largest model tested. The paper never mentions these models' ratios and does not test anything near them. The mechanism has real limits. The theorem covers one step of exact-orthogonalization Muon against full-batch gradient descent, not AdamW. It is proved only for data budget γ ≥ 16, and the paper's own one-step AdamW surrogate never crosses over (R reaches 0.93 at γ = 64). The theory explains the reversal with budget, not the fall with model size. The strongest outside evidence against extrapolating is Moonlight's own production-scale ablation. At 1.2T tokens, the Muon-pretrained, Muon-fine-tuned model beats the AdamW-pretrained, AdamW-fine-tuned twin on all four post-SFT benchmarks. That is a single run measured on benchmarks, not forgetting, and taken before cooldown. I found no author response, replication or substantive public critique since 2 November.

## Sources

### The paper

```text
URL:         https://arxiv.org/abs/2611.03633 (HTML: https://arxiv.org/html/2611.03633v1 ; PDF: https://arxiv.org/pdf/2611.03633v1)
Kind:        primary. The authors own the experiments, the definitions (fine-tuning gap, crossover TPR, margin-to-spread ratio) and the theorem.
Establishes: firsthand: all crossover values, tuning protocol, pretraining-loss ordering, MSR measurements, Theorem 4.2 and its proof.
Paraphrase:  Catherine Li and Jingchu Gai (equal contribution), Andrej Risteski, Jacob Mitchell Springer and Aditi Raghunathan
             (equal advising), all Carnegie Mellon University. "Pretraining Data Scale Reverses the Muon–AdamW Fine-Tuning Gap",
             v1, Mon 2 Nov 2026 18:56:43 UTC, 49 pages, single version. The arXiv listing shows v1 only. Jingchu Gai's homepage
             lists it as "Preprint". No code or data release is mentioned anywhere in the PDF.
Locators:    see the itemized record below. Page numbers are PDF pages, which match the printed numbers.
```

**Scale and setup** (Section 1 p1; Section 3.1 p3; Appendix A.3 p16; C.1 p19)
- About 600 pretraining runs and 29,000 fine-tuning runs ("nearly 600 pretraining runs and 29,000 fine-tuning runs in total", Section 1).
- OLMo-style decoder-only transformers at 30M, 60M, 100M, 300M and 600M parameters, trained on DCLM with the OLMo 2 tokenizer. The paper does not say whether parameter counts include embeddings. The sibling paper by two of the same authors (Springer et al. 2025, App. C.1) states non-embedding counts for its "OLMo-30M".
- Budgets by size (C.1): 5–1,280 TPR at 30M, 5–2,560 at 60M, 5–640 at 100M, 5–160 at 300M, 5–40 at 600M. "150M to 154B tokens" is 30M × 5 and 60M × 2,560 (153.6B).
- TPR = D/N; "The compute-optimal budget of Hoffmann et al. (2022) corresponds to TPR = 20; our budgets range from 5 to 2,560 TPR" (A.3).
- Fine-tuning sets: GSM8K, StackMathQA, Alpaca, MusicPile. Each fine-tune is 20M tokens, sequence length 1,024, global batch 65,536 tokens (about 305 steps), cosine schedule with 20 warmup steps, weight decay 0.1, betas (0.9, 0.95), clipping 1.0 (C.2 p21).
- Learning is measured as validation loss on the fine-tuning set, and forgetting as loss on a held-out DCLM shard of about 4.19M tokens. Both are mean next-token cross-entropy in nats (C.5 p21).
- The frontier is the lower-left arc of the convex hull of (forgetting, fine-tuning loss) points. The fine-tuning gap G_FT is a signed mean over 100 arc-length samples on the AdamW frontier of the distance to the nearest Muon-frontier point. It is negative when Muon dominates. The crossover TPR is "the smallest budget at which G_FT > 0" (C.5 p21). A reported crossover is therefore a grid point. The true crossing lies between the previous budget (half the value) and the reported one.

**Hyperparameter tuning protocol** (Section 3.1 p3; C.1–C.2 pp19–21; Table 1 p20; Figure 8 p20; D.3 p25)
- Pretraining for both optimizers: sequence length 4,096, global batch 2^20 tokens, WSD schedule, weight decay 0.1, gradient clipping 1.0. AdamW betas are (0.9, 0.98). Muon updates the hidden weight matrices, and AdamW updates embeddings, output layer and norms (C.1). The paper does not report warmup or decay lengths, Muon momentum, Newton–Schulz settings or whether Muon's update is RMS-matched.
- Lowest-pretraining-loss setting, used in the main text. "For each model size, budget and optimizer, we sweep the peak learning rate" and keep the run with the lowest held-out DCLM loss. Only the peak learning rate is swept. Weight decay, batch size and schedule shape are fixed and shared. For Muon the Muon learning rate is swept and the AdamW-side learning rate is fixed to the tuned AdamW value of the same cell (C.1.1). The authors check this choice at 60M, 20–160 TPR, with 3–4 AdamW-side rates from 0.5x to 2.8x the tuned value. Best loss "varies by at most 0.021 nats", and the tuned value is within 0.016 nats of the best, against the "0.03–0.20 nats by which Muon beats AdamW at these budgets" (C.1.2, Figure 8).
- Table 1 tuned peak learning rates (AdamW / Muon), by TPR 5, 10, 20, 40, 80, 160, 320, 640, 1,280, 2,560:
  - 30M AdamW 0.08, 0.04, 0.04, 0.014, 0.02, 0.014, 0.02, 0.014, 0.01, –; Muon 0.01, 0.01, 0.01, 0.014, 0.02, 0.01, 0.014, 0.01, 0.014, –
  - 60M AdamW 0.056, 0.04, 0.02, 0.02, 0.01, 0.014, 0.01, 0.01, 0.007, 0.01; Muon 0.014, 0.01, 0.014, 0.01, 0.014, 0.01, 0.014, 0.007, 0.005, 0.005
  - 100M AdamW 0.04, 0.02, 0.01, 0.01, 0.01, 0.007, 0.007, 0.007; Muon 0.014, 0.014, 0.014, 0.014, 0.01, 0.014, 0.01, 0.005
  - 300M AdamW 0.001, 0.0025, 0.0035, 0.0025, 0.0025, 0.0025; Muon 0.02, 0.014, 0.02, 0.014, 0.014, 0.02
  - 600M AdamW 0.0025 at all four budgets (5–40); Muon 0.014 at all four
  - Several AdamW optima at 300M and 600M (0.001 to 0.0035) sit far below the 0.005 floor of the best-frontier grid in C.1.3, and the 600M rate is identical across all four budgets. Whether these edges were bracketed cannot be checked from the paper. This is my observation, not the authors'.
- Best-frontier setting (C.1.3 p20). For each cell and optimizer, the loss-optimal base model and the base models "at the next five larger learning rates" of the grid {0.005, 0.007, 0.01, 0.014, 0.02, 0.028, 0.04, 0.056, 0.08, 0.12, 0.16} are each fine-tuned, and the runs are pooled into one frontier.
- Fine-tuning sweep (C.2). AdamW learning rate from 1e-4 to 1e-2. Muon learning rate from 6e-4 to 2e-2, with its AdamW-side rate set to 0.25x the Muon rate. The range runs "from runs that barely move the base model to runs that reach the lowest fine-tuning loss at the cost of more than a nat of forgetting."
- Asymmetry in fine-tuning optimizer. AdamW-pretrained models are fine-tuned only with AdamW. Muon-pretrained models are fine-tuned with both AdamW and Muon (Section 3.1; C.2). The paper motivates this in D.3: on AdamW-pretrained models AdamW fine-tuning dominates Muon fine-tuning at every budget, while for Muon-pretrained models "the two frontiers ... lie close together with no consistent winner" (60M, GSM8K, Figure 15 p25). The protocol gives Muon-pretrained models two fine-tuning optimizers and AdamW-pretrained models their better one.
- Robustness checks the paper reports. Replay (10–30% DCLM) and EWC (λ in {1e3, 4e3, 1e4, 4e4}) on 60M models move the crossover from 80 to 320 TPR on Alpaca and StackMathQA, "but AdamW's frontier is better at large budgets on every dataset under both (Figure 18), with one exception: under EWC on StackMathQA the gap turns negative again at the largest budget, 2,560 TPR" (D.4 p25).

**Main result and crossovers** (Section 3.2 p4; Figures 1–3; Table 2 p32; Figure 14 p25)
- 60M, StackMathQA, lowest-loss setting: "At small pretraining data budgets (2.4B tokens), Muon Pareto-dominates AdamW (Figure 1) ... beyond 2.4B tokens, AdamW achieves lower fine-tuning loss with less forgetting than Muon" (Section 3.2). 2.4B tokens is 40 TPR at 60M. The crossover grid point is 80 TPR (4.8B tokens).
- "On StackMathQA, the crossover is 320 TPR for 30M models but only 10 TPR for 600M models (Figure 2). The specific crossover TPR depends on the fine-tuning dataset, but the broader trend persists" (Section 3.2).
- Table 2 (right block, "the fine-tuning crossover of Figure 2") gives every crossover in the lowest-loss setting. I decoded the marker coordinates of Figure 2's SVG and they reproduce Table 2 exactly. Figure 14 (best-frontier setting) has no table. Its values below are decoded from SVG marker coordinates against the log-4 axis ticks (5, 20, 80, 320), using the method that reproduced Table 2. See Numbers.
- The authors' size account: "We hypothesize that ... this scaling trend is driven by two factors: Muon's shrinking pretraining loss advantage and increased degradation relative to AdamW (Figure 3b,c)" (Section 3.2). This is stated as a hypothesis.
- Figure 9 (p22): "the loss-optimal Muon model reaches a lower pretraining loss than its AdamW counterpart at every budget and model size". Figure 9 plots 600M only at 5, 10 and 20 TPR. Table 2's caption also calls 20 TPR "the largest 600M budget" for the perturbation study, while C.1 and Table 1 list 600M budgets up to 40 TPR. The perturbation and MSR studies use 36 cells (72 checkpoints), consistent with 600M stopping at 20 TPR there. The fine-tuning studies include 600M at 40 TPR (Figure 3b,c are "at 40 TPR" across all five sizes).

**Mechanism** (Section 4 pp4–9; Appendix B pp16–19; E pp29–33; F pp34–49)
- Margin-to-spread ratio, Definition 4.1 (p6). For fact i, the pairwise margins are m_ij = s_ii − s_ij over wrong candidates j. h_i is their mean and κ_i² their variance. ρ_i = h_i/κ_i, and the model-level ρ = h̄/κ̄ with means taken over facts before the ratio. "κ_i is also the standard deviation of the incorrect logits", so the MSR is the average margin in units of the wrong logits' spread.
- Why it predicts robustness (Corollary B.5 p18). With uncorrelated logit noise of standard deviation σ, the expected fraction of wrong answers that stay below the right one is at least ρ_i²/(ρ_i² + 1 + 2σ²/κ_i²). The proof is Cantelli's inequality. The paper notes that a union bound over all N−1 competitors "is informative only when ρ_i² is much larger than N".
- Setting (Section 4.1). A linear associative memory. N key-value pairs with u_i, v_i ~ N(0, I_d), weight matrix W ∈ R^{d×d}, logits s_ij = v_jᵀ W u_i, softmax cross-entropy. The "data budget" γ = N/d > 1 is facts per dimension and "plays the role of token-parameter ratio". Muon is exact orthogonalization, W ← W − η polar(∇L), against full-batch GD. It is not AdamW and has no momentum.
- Theorem 4.2 (informal, p7): one GD step and one Muon step from zero init with uniform query weights. For sufficiently large γ, GD has the larger MSR, a fixed-percentage increase in γ raises R = ρ_GD/ρ_Muon with high probability, and R approaches 3π/8 ≈ 1.18 from below at rate 1/γ. All claims hold with probability tending to one as d → ∞.
- Proof, in steps (Section 4.2 sketch; F.1–F.5):
  1. One step gives W_GD = G and W_Muon = polar(G), where G = Σ_k (v_k − v̄)u_kᵀ. Scale does not affect ρ (Lemma F.1). W_Muon is orthogonal almost surely (Lemma F.2).
  2. Mean margin h̄(W) = ⟨W, G⟩/(N−1). For GD this gives ‖G‖_F²/(N−1). For Muon it gives ‖G‖_*/(N−1), the nuclear norm or sum of singular values.
  3. GD's spread: (κ̄_GD)² = d³(γ + 2)(1 + o_p(1)) (Lemma F.15). The N d² part is crosstalk from all other stored facts. The 2d³ part comes from the query and candidate facts.
  4. Muon's spread: (κ̄_Muon)² = d(1 + O(γ^{-3/2}) + o_p(1)) (Lemma F.31). Orthogonality preserves key norms, so the wrong-logit spread does not grow with the number of stored facts.
  5. ρ_GD = sqrt(d/γ)(1 − 1/γ + O(γ^{-2})) (Lemma F.16). ρ_Muon = sqrt(d/γ)[(8/(3π))(1 − 1/(10γ)) + O(γ^{-3/2})] (Lemma F.32, requires γ ≥ 16). The 8/(3π) comes from the Marchenko–Pastur singular-value integral (Lemma F.4(iv)). Therefore R = (3π/8)(1 − 9/(10γ)) + O(γ^{-3/2}) + o_p(1) (Eq. 8).
  - The paper's decomposition (E.1.1 p29): "The limiting ratio 3π/8 is therefore carried by the margin. Its approach to that limit comes from both factors: Muon's margin contributes the +1/(10γ) correction, while the −1/γ part of the 9/(10γ) term comes from GD's variance, the factor γ + 2."
- Author-stated limits of the proof:
  - "The GD estimates hold for every γ > 1; the Muon estimates, and hence the theorem, require γ ≥ 16" (F, p34).
  - "The leading term crosses one at γ ≈ 5.95, below the range γ ≥ 16 in which Lemma F.32 is proved, so the location of the crossing is established empirically rather than by Theorem 4.2" (p49).
  - Remark F.35: the hypotheses of the pointwise-monotonicity lemma F.34 are "not proved here".
  - Remark on data distribution (p7): "Other data distributions can change both the gradient spectrum and the competing-score variances, so the optimizer ordering may differ."
- Numerical checks:
  - One step at d = 512 (E.1.1, Figure 19 p30): R rises "from 0.53 at γ = 1/4 to 1.16 at γ = 64 and crossing 1 near γ = 5". The AdamW surrogate (first AdamW step = sign(G)) "has the same shape but reaches only 0.93 at γ = 64, so over the data budgets we ran the one-step reversal is a statement about GD, not about AdamW."
  - Many steps, 10⁴ full-batch steps with Zipf queries (E.1.2, Figure 21 p31): R ranges "from about 0.4 to about 1.2". The crossing R = 1 moves to larger budgets as d grows: γ* ≈ 4.0, 4.4, 5.4 and 9.9 at d = 64, 128, 256 and 512. The σ50 robustness ordering flips at γ ≈ 0.5, 1.3 and 11 at d = 128, 256 and 512, and "at d = 64 GD is already the more robust at the smallest data budget we ran." "The two turnovers need not coincide, and they do not."
- Language-model connection (Section 4.3 p8; Figure 5). The MSR is computed per token position against the whole vocabulary and reported as the median over correctly predicted positions. It is shown for 30M, 60M and 100M only. "Muon has a larger MSR at small data budgets, while AdamW has a larger MSR at sufficiently large budgets ... the ratio of AdamW's MSR to Muon's crosses one." Caveat in the text: "The MSR and fine-tuning crossovers do not necessarily appear at exactly the same budget, since the learning–forgetting tradeoff also depends on pretraining loss."
- MSR against weight-perturbation robustness (B.2.2 p19; E.3.2 p33). The Spearman correlation between ρ and δ* over 72 checkpoints is +0.83 at ΔL = 0.05 and 0.1 nats and +0.84 at 0.2. Within optimizer it is +0.87 to +0.89 (AdamW) and +0.92 to +0.93 (Muon).
- Weight perturbation (E.2.2 p31). Over 36 cells, δ* is "larger for AdamW in every cell and at every threshold, by a median factor of 1.4". Muon's loss increase exceeds AdamW's "in every cell at every δ from 0.005 to 0.2".
- Figure-label inconsistency: the axis labels in Figures 4, 5, 7, 20, 21 and 23 read "MNR" and "MNR ratio", while the text everywhere says MSR. A capture of those figures will show "MNR".

**Author caveats** (Section 6 p10; Section 5 p9)
- "We do not necessarily expect this for every fine-tuning distribution, since fine-tuning on data close to the pretraining data is simply continued pretraining."
- "the crossover budget decreases with model size, which suggests that the problem persists as we scale." This is the authors' only statement about scale beyond 600M. It is a suggestion, and they make no statement about MoE or production models.
- Related work concedes that Muon's pretraining speedup "shrinks as model size and data grow, and Muon is overtaken by other matrix-based optimizers at large data-to-model ratios (Wen et al., 2026b;a)". It also says Ruan et al. (2026) find Muon better after fine-tuning "for small data regimes ... consistent with our findings."
- The paper names Kimi K2 and GLM-4.5 as frontier models pretrained with Muon (Section 5) but never computes or discusses their TPRs.
- Acknowledgements thank Kaiyue Wen, an author of arXiv:2509.02046 and a co-author of Springer et al. 2025, for discussions.

### Production models pretrained with Muon

```text
URL:         https://arxiv.org/abs/2502.16982
Kind:        primary. Moonshot AI's technical report on its own model Moonlight and its own AdamW twin.
Establishes: firsthand: Moonlight's parameter and token counts, and a same-architecture Muon vs AdamW pretrain-and-SFT ablation.
Paraphrase:  Liu, Su et al., "Muon is Scalable for LLM Training". Moonlight is "a 3B/16B-parameter Mixture-of-Expert (MoE)
             model trained with 5.7T tokens using Muon" (abstract). "2.24B activated and 15.29B total parameters (3B activated
             and 16B total when including embedding)" (Section 3.3, p7). The stages are 0–33B, 33B–5.2T and 5.2T–5.7T tokens
             (p7–8). Table 6 (p10) fine-tunes the 1.2T-token checkpoints of Moonlight and Moonlight-A ("follows the same
             training settings as Moonlight, except that it uses the AdamW optimizer", p8) for two epochs on tulu-3-sft-mixture.
             Scores for MMLU (0-shot CoT) / HumanEval / MBPP / GSM8K (5-shot):
               Muon-pretrain + Muon-SFT    55.7 / 57.3 / 55.6 / 68.0
               AdamW-pretrain + Muon-SFT   55.3 / 53.7 / 55.5 / 62.1
               Muon-pretrain + AdamW-SFT   50.2 / 52.4 / 55.2 / 64.9
               AdamW-pretrain + AdamW-SFT  52.0 / 53.1 / 55.2 / 64.6
             The 1.2T checkpoints are taken where "the learning rate is not decayed to minimal and the model has not gone
             through the cooldown stage yet" (p8). Section 4 (p11) names the "Pretraining-Finetuning Mismatch" (an AdamW model
             fine-tuned with Muon or vice versa does worse) as an open problem.
Locators:    abstract p1; Section 3.3 p7; Table 4 p8; Section 3.5 and Table 6 p10; Table 7 p10; Section 4 p11.
```

```text
URL:         https://arxiv.org/abs/2507.20534
Kind:        primary. Moonshot AI (Kimi Team) on its own model.
Establishes: firsthand: Kimi K2's counts and its optimizer (MuonClip = Muon + weight decay + RMS matching + QK-Clip).
Paraphrase:  "1.04 trillion-parameter Mixture-of-Experts (MoE) transformer model with 32 billion activated parameters"
             (Section 2.3, p6). Table 2 gives Total 1.04T and Activated 32.6B. Pretrained "using the MuonClip optimizer ...
             processing a total of 15.5T tokens. The first 10T tokens were trained with a constant learning rate ... followed by
             5.5T tokens with a cosine decay". Then "an annealing phase followed by a long-context activation stage" of 400B
             tokens at 4k and 60B at 32k (Section 2.5, p9). Whether the 460B is inside the 15.5T is not stated. Post-training
             uses Muon: "we ... recommend its use for fine-tuning with K2. This follows from the conclusion of our previous work
             that a Muon-pre-trained checkpoint produces the best performance with Muon fine-tuning" (Section 3.1, p9).
Locators:    abstract; Section 2.3 and Table 2 p6; Section 2.5 p9; Section 3.1 p9.
```

```text
URL:         https://arxiv.org/abs/2508.06471
Kind:        primary. Zhipu AI / Tsinghua (GLM-4.5 Team) on its own model.
Establishes: firsthand: GLM-4.5 counts and use of Muon.
Paraphrase:  "355B total parameters and 32B activated parameters ... multi-stage training on 23T tokens" (abstract).
             Table 1 (p3) counts MTP layers "but not word embeddings and the output layer". GLM-4.5-Air is 106B total / 12B
             active, with no separate token count. Figure 3 (p4) breaks the budget into 15T general pretraining, 7T code and
             reasoning, then mid-training of 500B repo code, 500B synthetic reasoning and 100B long-context/agent data.
             "We employed the Muon optimizer for all parameters except word embedding, bias, and weights for RMSNorm"
             (Section 2.4, p5).
Locators:    abstract; Table 1 p3; Figure 3 p4; Section 2.4 p5.
```

```text
URL:         https://arxiv.org/abs/2602.15763
Kind:        primary. GLM-5 Team (Zhipu AI) on its own model.
Establishes: firsthand: GLM-5 counts and that pretraining follows the GLM-4.5 Muon setting.
Paraphrase:  "a 744B parameter model (40B active parameters)". The training budget for all stages totals "28.5 trillion
             tokens for the base model" (Section 2, p4). Appendix A (p36): "For training, we follow the setting of GLM-4.5,
             including the Muon optimizer". Section 2.1 adds a "Muon Split" variant.
Locators:    Section 2 and 2.1 p4; Appendix A p36.
```

```text
URL:         https://arxiv.org/abs/2602.17004
Kind:        primary. Arcee AI on its own models.
Establishes: firsthand: Trinity Nano, Mini and Large counts, and Muon pretraining.
Paraphrase:  Trinity Large is "400B total parameters and 13B activated per token". Trinity Nano is 6B total / 1B active and
             Trinity Mini is 26B / 3B. "Trinity Nano and Trinity Mini were pre-trained on 10 trillion tokens, and Trinity Large
             was pre-trained on 17 trillion tokens" (abstract, p1; Section on data, p9). "we use the Muon optimizer ... for
             hidden layers and the AdamW optimizer ... for the embedding and output layers" (Section 3.4.2, p12).
Locators:    abstract p1; data section p9; Section 3.4.2 p12.
```

```text
URL:         https://arxiv.org/abs/2510.26692
Kind:        primary. Moonshot AI (Kimi Team) on its own model.
Establishes: firsthand: Kimi Linear counts and MuonClip pretraining.
Paraphrase:  "3B activated parameters and 48B total parameters" (abstract). Ablation models use MuonClip on 1.4T tokens. "Our
             final released Kimi Linear checkpoint is pretrained using the same procedure, but with an expanded total of 5.7
             trillion tokens" (Section 5.4.1, p10).
Locators:    abstract p1; Section 5.4.1 p10.
```

```text
URL:         https://arxiv.org/abs/2602.02276
Kind:        primary. Moonshot AI on Kimi K2.5.
Establishes: firsthand: K2.5 continues training of the K2 base (1.04T / 32B) with MuonClip on about 15T mixed vision-text tokens.
Paraphrase:  K2.5 builds on Kimi K2 "pre-trained on 15 trillion high-quality text tokens" with MuonClip. It adds
             "approximately 15T tokens across three stages", the main joint stage being "15T vision-text tokens at 4K sequence
             length" (pp7–8).
Locators:    Section 2 / pre-training, pp7–8.
Use:         I left it out of the overlay. The extra tokens are multimodal continued training of the same weights, so a
             single TPR would mix two regimes. It is recorded so the editor knows it was checked.
```

### Prior and adjacent work

```text
URL:         https://arxiv.org/abs/2503.19206
Kind:        primary for its own findings. It is not independent of 2611.03633: Springer and Raghunathan are authors of both,
             and Kaiyue Wen is a co-author here.
Establishes: firsthand: "catastrophic overtraining". Extended pretraining makes models harder to fine-tune, which the authors
             attribute to "progressive sensitivity".
Paraphrase:  "the instruction-tuned OLMo-1B model pre-trained on 3T tokens leads to over 2% worse performance on multiple
             standard LLM benchmarks than its 2.3T token counterpart" (abstract). Controlled experiments use OLMo 15M/30M/90M
             (non-embedding) on 4B–128B C4 tokens, all with AdamW and no Muon (App. C.1). Larger learning rates bring the
             inflection point earlier (Section 3). Gaussian weight perturbation is the robustness probe that 2611.03633 reuses
             (2611.03633 B.1.1).
Locators:    abstract p1; Section 3.2–3.3; App. C.1.
Bearing:     This is the parent finding. It shows overtraining hurts adaptability under AdamW alone, so 2611.03633 is a claim
             about the relative rate at which the two optimizers degrade, not that Muon models alone become fragile.
```

```text
URL:         https://arxiv.org/abs/2509.02046
Kind:        primary for its own benchmark. Wen, Hall, Ma, Liang (Stanford). v3, 25 Oct 2026.
Establishes: firsthand: under equal tuning, Muon's pretraining-loss speedup over AdamW shrinks with scale.
Paraphrase:  Ten optimizers, 0.1B–1.2B parameters, 1–8x the Chinchilla ratio. "the speedup of matrix-based optimizers is
             inversely proportional to model scale, decreasing from 1.4x over AdamW for 0.1B parameter models to merely 1.1x for
             1.2B parameter models" (abstract). "while Muon is consistently the best optimizer in smaller Chinchilla ratio
             regimes, it is outperformed by Kron and Soap when the data-to-model ratio increases to 8x or larger" (p3).
             "optimal hyperparameters for one optimizer may be suboptimal for another, making blind hyperparameter transfer
             unfair", for example Lion's optimal weight decay of about 0.6 against AdamW's 0.1 (abstract; p3). It also warns
             that "comparing intermediate checkpoints before reaching the target training budgets can be misleading" (abstract).
Locators:    abstract p1; Section 1 contributions p3; Figure 1 bottom-left p2.
Bearing:     This bears on the tuning objection. 2611.03633 sweeps only the peak learning rate and fixes weight decay at 0.1
             for both optimizers. It also bears on Moonlight's pre-cooldown 1.2T comparison.
```

```text
URL:         https://arxiv.org/abs/2606.16899
Kind:        primary. Wen, Dang, Lyu, Ma, Liang, v2 25 Oct 2026. Cited by 2611.03633 as Wen et al. 2026a.
Establishes: firsthand: Muon's shrinking gain is tied to constant decoupled weight decay. A norm-fixing wrapper (Hyperball)
             restores it.
Paraphrase:  "gains over AdamW are observed to shrink as model size and data scale grow when using standard constant
             decoupled weight decay." Muon Hyperball reaches a "20–30% token equivalent speedup over weight decay baselines"
             on Qwen3-style models up to 1.2B (abstract).
Locators:    abstract p1.
Bearing:     2611.03633 uses exactly the constant decoupled weight decay (0.1) this work says penalizes Muon at large data
             scale. It measures pretraining loss only, so it says nothing directly about fine-tuning.
```

```text
URL:         https://arxiv.org/abs/2605.10468
Kind:        primary. Xingyu Qu (MBZUAI), Peigeng Huang (Nanjing University), Samuel Horvath (MBZUAI). ICML 2026 per the PDF
             header.
Establishes: firsthand: an optimizer mismatch between pretraining and fine-tuning hurts, and LoRA reduces it.
Paraphrase:  Two 561M NanoChat models pretrained on about 11B FineWeb-Edu tokens (about 20 TPR, "following the Chinchilla
             scaling law"), one with Muon and one with Adam, are fine-tuned on WikiText-2. Table 1 (p3) gives relative
             perplexity normalized to each model's own pretrained baseline. Muon-pretrained: Full-Muon 0.716, Full-Adam 0.739.
             Adam-pretrained: Full-Adam 0.710, Full-Muon 0.719. "using the matched optimizer ... consistently outperforms the
             mismatched one."
Locators:    abstract; Section 3 and Table 1 p3.
Bearing:     The study does not compare Muon-pretrained against Adam-pretrained models across budgets, and its columns are
             normalized differently. It supports the fairness of 2611.03633 fine-tuning AdamW models with AdamW. It disagrees
             with 2611.03633's D.3 finding of "no consistent winner" between the two fine-tuning optimizers on Muon-pretrained
             models.
```

```text
URL:         https://arxiv.org/abs/2606.09658
Kind:        primary. Ruan, Zhang, Wang, Zhang. Cited by 2611.03633 as consistent at small budgets.
Establishes: firsthand: Muon-pretrained GPT-2 models reach lower instruction-tuning perplexity than Adam-pretrained ones.
Paraphrase:  nanoGPT GPT-2 (124M) and GPT-2 Medium (354M) on a FineWeb10B subset, with "token-to-parameter ratio is at least
             2x the Chinchilla ratio" (p6). Each optimizer's learning rate is swept and weight decay is fixed at 0 (App. A.3).
             Both models are fine-tuned with the same Adam. Table 3 (p28) instruction-tuning perplexity, Adam vs Muon:
             GPT-2 Alpaca 16.25 vs 15.12, Dolly 8.99 vs 8.61, WizardLM 51.91 vs 45.75. GPT-Medium (single seed) 12.53 vs 12.23,
             7.85 vs 7.62, 27.28 vs 26.68.
Locators:    Section 4 setup p6; Figure 4; App. A.3 p25; Table 3 p28.
Bearing:     It measures learning only, not forgetting, and does not give exact token counts. At 354M and at least 40 TPR it
             overlaps budgets where 2611.03633's 300M crossovers (10–40 TPR) say AdamW should win the trade-off. The two do
             not conflict directly, because Ruan never measures the forgetting axis.
```

```text
URL:         https://arxiv.org/abs/2605.06654
Kind:        primary. Yuxing Liu, Jianyu Wang, Tong Zhang. Cited by 2611.03633.
Establishes: firsthand: fine-tuning with the pretraining optimizer forgets less. In a Muon-to-Muon versus AdamW-to-AdamW
             pipeline, Muon's edge disappears on math.
Paraphrase:  A GPT-2-small-sized model (about 123M) is pretrained on 8B OpenWebText tokens (about 65 TPR), with AdamW and Muon
             both at learning rate 3e-3 (App., p17). When each optimizer is used for both stages, "Muon achieves a significantly
             better learning-forgetting tradeoff when finetuned on Alpaca than AdamW. On math and code tasks, however, Muon is
             generally comparable to AdamW: slightly better in Magicoder, and slightly worse in MetaMathQA" (Section 4.1, p9).
Locators:    abstract; Section 4.1 and Figure 6 p9; appendix p17.
Bearing:     This is an independent learning-forgetting measurement near 2611.03633's 100M cell. 2611.03633's 100M crossovers
             are 80 TPR (Alpaca) and 40 TPR (StackMathQA). At about 65 TPR it predicts Muon still ahead on instruction data and
             AdamW ahead on math, which matches the direction Liu et al. report. Pretraining learning rates were not tuned
             separately per optimizer.
```

### Public response

```text
URL:         https://github.com/Hiroki11x/Papers/issues/613
Kind:        secondary. A personal paper-notes issue by GitHub user Hiroki11x, opened 3 Nov 2026. The site returned 403 to curl,
             and I read it through a fetch summary. The exact wording is unverified.
Establishes: only that one reader logged the paper with skepticism.
Paraphrase:  It summarizes the paper (30M–600M, 320 to 10 TPR on StackMathQA) and adds a note in Japanese that, as summarized
             to me, asks whether both optimizers were carefully tuned and what the mechanism is, and suggests that favoring
             confident predictions could worsen calibration. It has no comments.
Locators:    issue body.
```

```text
URL:         https://gaijingchu.github.io/
Kind:        primary for publication status. Co-first author Jingchu Gai's own homepage.
Establishes: Gai's homepage lists the paper as "Preprint" (CMU PhD student advised by Risteski and Raghunathan).
Locators:    "LLM optimization & scaling laws" list.
```

Searches since 2 November (arXiv listings, web, Hacker News Algolia, OpenReview API, alphaXiv page) found no author thread, rebuttal, comment or replication. Only daily-digest mentions turned up, and I did not open them.

## Contradictions

1. **Moonlight at production scale, against the extrapolation.** Moonlight and Moonlight-A share an architecture of 2.24B active / 15.29B total. At 1.2T tokens (536 TPR active, 78 TPR total), the Muon-pretrained, Muon-fine-tuned model beats the AdamW-pretrained, AdamW-fine-tuned model on all four reported post-SFT benchmarks (Table 6, arXiv 2502.16982 p10). Under 2611.03633's own protocol (AdamW model with AdamW, Muon model with its better optimizer), Muon wins this comparison. If the paper's trend held at 2.24B, AdamW should be far past its crossover. Limits on the counterexample: one run per arm, a single SFT learning rate, benchmarks rather than held-out pretraining loss (so forgetting is not measured directly), and checkpoints taken before cooldown, which 2509.02046 warns can mislead. When both arms use AdamW SFT, the AdamW-pretrained model is ahead on MMLU (52.0 vs 50.2) and HumanEval (53.1 vs 52.4), level on MBPP and behind on GSM8K (64.6 vs 64.9). That split is mixed, despite Muon's better base model (Table 4).
2. **Fine-tuning optimizer for Muon-pretrained models.** 2611.03633 (D.3, Figure 15, 60M GSM8K) finds "no consistent winner" between AdamW and Muon fine-tuning of Muon-pretrained models. Moonlight (Table 6), Kimi K2 (Section 3.1) and Qu et al. (Table 1) report that Muon fine-tuning is better for Muon-pretrained models. Production Muon models are post-trained with Muon. 2611.03633 pools both fine-tuning optimizers for Muon models, so this disagreement should not bias its frontier against Muon. It does mean the paper's fine-tuning regime differs from how Kimi models are actually post-trained.
3. **Muon's shrinking pretraining edge may be a weight-decay artifact.** 2611.03633 attributes part of the size trend to "Muon's shrinking pretraining loss advantage" (Section 3.2). Wen et al. 2026a (2606.16899) attribute that shrinkage, at least in part, to constant decoupled weight decay, which 2611.03633 uses (0.1, untuned). Wen et al. 2025 (2509.02046) show that optimizers' optimal weight decays differ. Nobody has tested whether tuned or Hyperball weight decay moves the fine-tuning crossover.
4. **Theory against experiment on the size trend.** In the linear memory, the many-step crossing γ* rises with model dimension (4.0, 4.4, 5.4, 9.9 at d = 64 to 512; E.1.2). In language models, the crossover TPR falls with model size. The theory addresses the budget trend only. The size trend rests on an empirical hypothesis (Figure 3b,c). γ is facts per dimension, not tokens per parameter, so the two axes are not directly comparable. The direction still differs, and the paper does not discuss it.
5. **Theory compares against GD, not AdamW.** By the paper's own E.1.1, the one-step AdamW surrogate never overtakes Muon over the budgets run (R = 0.93 at γ = 64). The bridge to AdamW is empirical, the language-model MSR curves in Figure 5, measured only at 30M–100M.
6. **Ruan et al. 2606.09658 against the robustness story.** Ruan et al. find Muon features "more robust" (lower corrupted-text perplexity) and transferring better at at least 2x Chinchilla, at 124M–354M. The disagreement is partial. Ruan measures input-corruption robustness and fine-tuning perplexity, never forgetting, and 2611.03633's claim concerns the learning-forgetting frontier.
7. **Commission against paper on "every budget".** The commission says Muon "reaches lower pretraining loss at every budget". The paper says so too (Figure 9; Section 4), but Figure 9 shows 600M only through 20 TPR. The 600M, 40 TPR cell appears only in Figure 3b, where Muon is also lower (2.957 vs 2.974 nats, digitized). The claim holds on the evidence shown.
8. **Within-paper budget inconsistency.** C.1 and Table 1 give 600M budgets of 5–40 TPR. Table 2's caption calls 20 TPR "the largest 600M budget" for the perturbation study. This is consistent if the perturbation and MSR studies (36 cells) dropped 600M at 40 TPR, but the paper does not say so.

## Numbers

### Crossover TPR (fine-tuning), lowest-pretraining-loss setting

Owner: arXiv 2611.03633 Table 2 (right block), p32, equal to Figure 2, p3. Scope: the smallest grid budget at which G_FT > 0. The grid doubles from 5 TPR, so each value is an upper end with the true crossing above half of it. One base model per optimizer per cell. No seeds or error bars.

```text
Size    Alpaca  GSM8K  MusicPile  StackMathQA
30M      160     80      640         320
60M       80     80       80          80
100M      80     40       80          40
300M      40     10       40          20
600M      20      5       10          10
```

- At 600M, GSM8K's 5 is the smallest budget run (Table 1, C.1). AdamW is already ahead at the first budget, so this crossover is censored at 5 or below.
- 30M to 600M fall: Alpaca 8x, GSM8K 16x (censored), MusicPile 64x, StackMathQA 32x.
- Log-log least-squares slope of crossover TPR against parameters (my computation): Alpaca −0.64, GSM8K −1.02, MusicPile −1.17, StackMathQA −1.07. Pooled over all 20 points: −0.97.

### Crossover TPR, best-frontier setting

Owner: 2611.03633 Figure 14, p25. Scope: decoded from SVG marker coordinates (https://arxiv.org/html/2611.03633v1/crossover-budget-high-lr.svg) against axis ticks 5/20/80/320. The paper prints no numbers. The same decoding reproduces Table 2 exactly from Figure 2's SVG.

```text
Size    Alpaca  GSM8K  MusicPile  StackMathQA
30M      320     80      640         320
60M       80     80       80          80
100M      80     40       80          80
300M      40     20       40          20
600M      20     10       10          10
```

Differences from the lowest-loss setting: Alpaca 30M (320 vs 160), GSM8K 300M (20 vs 10) and 600M (10 vs 5), StackMathQA 100M (80 vs 40). Pooled slope: −0.95.

### Crossovers in tokens

My computation, crossover TPR × parameters, from Table 2.

```text
Size    Alpaca   GSM8K   MusicPile  StackMathQA
30M     4.8B     2.4B    19.2B       9.6B
60M     4.8B     4.8B     4.8B       4.8B
100M    8.0B     4.0B     8.0B       4.0B
300M   12.0B     3.0B    12.0B       6.0B
600M   12.0B     3.0B     6.0B       6.0B
```

All 20 values lie within 2.4B–19.2B tokens. A slope of −1 in log TPR against log N is what a size-independent token threshold produces. The paper does not make this observation. The editor should weigh it before the piece calls the falling line a scaling effect separate from "crossover at a few billion tokens".

### Other paper figures

- **Grid of budgets per size** (C.1): 30M 5–1,280; 60M 5–2,560; 100M 5–640; 300M 5–160; 600M 5–40 TPR.
- **Fine-tuning gap G_FT, 60M, StackMathQA, lowest-loss** (Figure 3a p4). Digitized from fine-tuning-gap-size-loss-optimal.svg on a linear axis with ticks −0.1, 0, 0.1. Unit is the Euclidean distance in (nats, nats) loss space. By TPR: 20 −0.113; 40 −0.055; 80 +0.033; 160 +0.039; 320 +0.054; 640 +0.051; 1,280 +0.062; 2,560 +0.054.
- **Pretraining loss at 40 TPR, nats** (Figure 3b p4, digitized). It matches Figure 9 within 0.012 nats at the four sizes both show.

  ```text
  Size    AdamW   Muon    Muon edge
  30M     4.555   4.446   0.109
  60M     3.991   3.903   0.088
  100M    3.684   3.628   0.056
  300M    3.177   3.151   0.026
  600M    2.974   2.957   0.017
  ```

- **Degradation at 40 TPR**, the increase in held-out DCLM loss at a StackMathQA loss of 1.1x the best (Figure 3c p4; C.5). Digitized, linear axis with ticks 0 and 0.5, nats.

  ```text
  Size    AdamW   Muon
  30M     0.695   0.646
  60M     0.442   0.438
  100M    0.292   0.372
  300M    0.178   0.319
  600M    0.125   0.276
  ```

- **Full pretraining-loss series** (Figure 9 p22). Digitized from pretraining-loss-loss-optimal.svg. Axes verified linear by evenly spaced ticks (100M: 3.5/4.0/4.5; 300M: 3.2/3.4/3.6; 600M: 3.1/3.2/3.3). Held-out DCLM loss in nats, AdamW / Muon by TPR:
  - 30M: 5 6.024/5.330; 10 5.392/4.934; 20 4.909/4.562; 40 4.555/4.446; 80 4.423/4.383; 160 4.360/4.330; 320 4.322/4.300; 640 4.301/4.279; 1,280 4.280/4.269
  - 60M: 5 5.281/4.505; 10 4.578/4.180; 20 4.199/3.998; 40 3.997/3.903; 80 3.895/3.855; 160 3.837/3.803; 320 3.798/3.780; 640 3.769/3.755; 1,280 3.748/3.743; 2,560 3.728/3.723
  - 100M: 5 4.700/4.080; 10 4.090/3.845; 20 3.838/3.714; 40 3.696/3.628; 80 3.595/3.560; 160 3.540/3.522; 320 3.493/3.492; 640 3.463/3.466
  - 300M: 5 3.648/3.495; 10 3.405/3.334; 20 3.262/3.231; 40 3.177/3.151; 80 3.110/3.095; 160 3.058/3.046
  - 600M: 5 3.296/3.224; 10 3.141/3.109; 20 3.042/3.025
  - Caution: at 100M, 640 TPR the digitized Muon value (3.466) is 0.003 above AdamW (3.463). That is within digitizing precision, and the paper states Muon is lower at every budget. Do not report it as a reversal.
- **Language-model MSR ρ**, the median of h/κ over correctly predicted positions (Figure 5a p8, digitized, linear axis with ticks 5/6/7). AdamW / Muon:
  - 30M: 5 6.11/6.64; 10 6.52/6.45; 20 6.08/6.18; 40 5.80/5.86; 80 5.64/5.68; 160 5.46/5.40; 320 5.36/5.25; 640 5.28/5.16; 1,280 5.16/4.88
  - 60M: 5 6.47/6.90; 10 6.30/6.59; 20 6.22/6.50; 40 6.05/6.12; 80 6.35/5.72; 160 5.77/5.49; 320 5.50/5.14; 640 5.24/4.91; 1,280 5.00/4.82; 2,560 4.96/4.76
  - 100M: 5 6.42/6.98; 10 6.50/6.77; 20 6.33/6.54; 40 6.16/6.15; 80 5.99/5.85; 160 5.60/5.46; 320 5.41/5.06; 640 5.28/4.88
- **Ratio ρ_AdamW/ρ_Muon** (Figure 5b, digitized, ticks 1.0/1.1):
  - 30M: 0.92, 1.01, 0.98, 0.99, 0.99, 1.01, 1.02, 1.02, 1.06 (5 to 1,280 TPR)
  - 60M: 0.94, 0.96, 0.96, 0.99, 1.11, 1.05, 1.07, 1.07, 1.04, 1.04 (5 to 2,560)
  - 100M: 0.92, 0.96, 0.97, 1.00, 1.02, 1.03, 1.07, 1.08 (5 to 640)
  - The sustained crossing falls from about 160 TPR at 30M (the 10-TPR value of 1.01 is a single excursion) to 80 at 60M and about 40 at 100M. All three are digitized. Both MSRs fall with budget, and Muon's falls faster.
- **Linear memory**:
  - One-step R from 0.53 (γ = 1/4) to 1.16 (γ = 64), crossing 1 near γ = 5 (E.1.1).
  - Limit 3π/8 ≈ 1.178. Leading-term crossing at γ ≈ 5.95. Theorem valid for γ ≥ 16.
  - AdamW surrogate R = 0.93 at γ = 64.
  - Many-step γ* ≈ 4.0, 4.4, 5.4, 9.9 at d = 64, 128, 256, 512 (E.1.2).
  - Learning-rate ablation over a 16x range moves R by at most 1.3% (Table 3 p33; E.3.2).
- **Perturbation**: δ* is larger for AdamW in all 36 cells, by a median factor of 1.4 (E.2.2). Spearman ρ–δ* is +0.83 over 72 checkpoints (B.2.2).
- **Tuning-check magnitudes**: AdamW-side learning-rate sensitivity is at most 0.021 nats. The tuned value is within 0.016 nats of the best. Muon's margin is 0.03–0.20 nats at 60M, 20–160 TPR (C.1.2).

### Production models pretrained with Muon

Owners: each model's report, as listed in Sources. TPR is my computation, tokens / parameters. Scope: headline pretraining tokens, including mid-training where the report folds it into the headline figure.

```text
Model           Active     Total     Tokens   TPR active  TPR total  Param convention (report)
Moonlight       2.24B      15.29B    5.7T       2,545       373      excl. embeddings; 3B/16B incl. -> 1,900 / 356
Kimi Linear     3B         48B       5.7T       1,900       119      activated excl. embeddings (Table note)
Trinity Nano    1B         6B        10T       10,000     1,667      not stated
Trinity Mini    3B         26B       10T        3,333       385      not stated
Trinity Large   13B        400B      17T        1,308        43      not stated
Kimi K2         32.6B      1.04T     15.5T        475        15      Table 2 (abstract says 32B -> 484)
GLM-4.5         32B        355B      23T          719        65      incl. MTP, excl. embeddings and output layer
GLM-5           40B        744B      28.5T        712        38      not stated
```

- Kimi K2's 15.5T may or may not include the 400B + 60B annealing and long-context tokens (Section 2.5). Adding them gives 15.96T: 490 TPR active, 15.3 total.
- GLM-4.5's 23T is 15T + 7T pretraining plus 1.1T mid-training (Figure 3). Pretraining alone is 22T: 688 TPR active, 62 total.
- Size gap: the largest paper model is 600M. Production active sizes are 1B–40B (1.7x–67x). Totals are 6B–1.04T (10x–1,733x).

**Does the conclusion change between active and total parameters?**
- On active parameters, every model (475–10,000 TPR) is above every measured crossover at any size, including the largest, 640 at 30M on MusicPile.
- On total parameters, most models are still above every crossover measured at 300M–600M (5–40 TPR). The exception is Kimi K2 at 15 TPR, which is below the 600M Alpaca crossover (20) and below every 300M crossover except GSM8K (10). GLM-5 (38) and Trinity Large (43) sit near the 300M values.
- With the trend extrapolated (my log-log fits, which the paper does not make), the predicted crossover at 2.24B is 1.4–9.6 TPR across fine-tuning sets. At 32B it is 0.1–1.7, and at 1.04T it is 0.002–0.19. Every production model clears these on either convention.
- On the token reading (crossover of 2.4–19.2B tokens), production budgets of 5.7T–28.5T are 300x–12,000x past it.
- In short, the side of the line does not change except for Kimi K2 on total parameters without extrapolation. Every placement remains an extrapolation from dense 30M–600M models to MoE models.

### Moonlight 1.2T ablation

Owner: arXiv 2502.16982 Table 6, p10. Scope: 1.2T-token pre-cooldown checkpoints, 2 epochs of tulu-3-sft-mixture SFT, single runs. Scores for MMLU / HumanEval / MBPP / GSM8K:

```text
Pretrain  SFT     MMLU   HumanEval  MBPP   GSM8K
Muon      Muon    55.7   57.3       55.6   68.0
AdamW     Muon    55.3   53.7       55.5   62.1
Muon      AdamW   50.2   52.4       55.2   64.9
AdamW     AdamW   52.0   53.1       55.2   64.6
```

Base models at 1.2T (Table 4 p8), Moonlight-A vs Moonlight: MMLU 60.2 vs 60.4, HumanEval 29.3 vs 37.2, GSM8K 43.8 vs 45.0. TPR at 1.2T: 536 active, 78 total.

### Wen et al. 2509.02046 speedups

Owner: 2509.02046 abstract and Figure 1. Matrix-optimizer speedup over AdamW falls from 1.4x at 0.1B to 1.1x at 1.2B (at 8x Chinchilla). Muon is beaten by Kron and Soap at 8x Chinchilla or more (about 160 TPR, on their Chinchilla basis of about 20).

## Limits

- The paper has no error bars, seeds or repeated runs for any language-model pretraining or fine-tuning, so the crossover values carry no stated uncertainty. They are grid points on a doubling grid, accurate only to a factor of 2.
- The paper does not state whether its parameter counts include embeddings. That convention changes every TPR and the comparison with production models. The sibling paper uses non-embedding counts.
- The paper tests only dense models. Nothing in it, or in any source I found, says whether active or total parameters, or tokens, is the right denominator for an MoE model. The overlay therefore cannot be validated, and both columns above are offered as computations.
- Production models are not fine-tuned the way the paper fine-tunes: they use Muon SFT and RL, multi-phase data and annealing. No production lab reports a learning-forgetting frontier comparable to the paper's held-out-loss metric.
- The pretraining tuning protocol sweeps only the peak learning rate. Weight decay (0.1), batch size, schedule shape, Muon momentum and RMS scaling are fixed or unreported. Some AdamW optima at 300M–600M may sit at a grid edge. I could not establish whether that bracketing was checked.
- Theorem 4.2 compares one step of exact-orthogonalization Muon against full-batch GD from zero init. It does not cover AdamW, Newton–Schulz Muon, momentum or weight decay, and it is proved only for γ ≥ 16. The crossing location is empirical.
- The mechanism accounts for the reversal with budget. It does not account for the fall in crossover with model size, which the authors leave as a hypothesis (Figure 3b,c).
- I found no author response, replication or substantive public critique since 2 November. The only reaction located is one personal GitHub note, read through a fetch summary.
- The values for Figures 3, 5, 9 and 14 are digitized from the paper's vector SVGs, not printed numbers. The decoding method reproduces Table 2 exactly, but those values should be captioned as read from the figure.
- I did not open Mellum 2 (arXiv 2605.31268), which a search snippet describes as a Muon-trained model of about 12B total / 2.5B active trained on about 10.6T tokens. It is not in the overlay.

## Source assets

```text
Asset: Figure 2, "Crossover TPR decreases with model size" (arXiv 2611.03633, PDF p3; HTML element #S3.F2,
       https://arxiv.org/html/2611.03633v1#S3.F2). Four panels, one per fine-tuning set: crossover TPR (log scale, 5–320, with
       MusicPile's 640 point above the top tick) against model size 30M–600M.
Shows: the commissioned trend, and how strongly it depends on the fine-tuning set, in one image.
Crop:  keep all four panels and both axes with labels. Omitting a panel would select the most dramatic set. Keep the caption
       sentence "The exact crossover TPR varies depending on the fine-tuning dataset" or put it in our own caption.
```

```text
Asset: Figure 1, learning-forgetting frontiers for OLMo-60M on StackMathQA, 2.4B to 38.4B tokens (PDF p2; #S1.F1).
       Fine-tuning loss against forgetting (held-out DCLM loss), AdamW against Muon, one panel per budget.
Shows: what "better trade-off" means. At 2.4B Muon's frontier sits lower-left, and at larger budgets AdamW's does.
Crop:  keep all panels, the shared legend (AdamW / Muon) and both axis labels. The per-panel budget labels are in the panel
       headers and must be retained. Note in our caption that the axes are losses in nats and lower-left is better.
```

```text
Asset: Figure 3 (PDF p4; #S3.F3). (a) Fine-tuning gap against TPR, 60M StackMathQA. (b) Pretraining loss at 40 TPR by size.
       (c) Degradation at 40 TPR by size.
Shows: (a) the sign flip at the crossover. (b) and (c) the authors' two-factor account of the size trend: Muon's base-loss
       edge shrinking while its extra forgetting grows.
Crop:  (a) alone works as a single-panel crop if the zero line is kept. (b) and (c) must stay together with the AdamW/Muon
       legend.
```

```text
Asset: Figure 5 (PDF p8; #S4.F5). (a) MSR against TPR for 30M, 60M and 100M. (b) The ratio ρ_AdamW/ρ_Muon crossing 1.
Shows: the mechanism's quantity measured in real language models, flipping with budget.
Crop:  keep the legends. The axis labels read "MNR (ρ)" and "MNR ratio" while the text says MSR, so either explain this in the
       caption or redraw from the digitized series instead of capturing.
```

```text
Asset: Figure 4 (PDF p8; #S4.F4). The linear associative memory: (a, b) MSR and σ50 after 10⁴ steps at d = 256,
       (c, d) one-step normalized MSR and the ratio R against theory.
Shows: the toy model's budget trend and its agreement with Theorem 4.2.
Crop:  panel (d) (measured against theory curve for R) is the one that teaches the proof. Keep the "Measured / Theory" legend.
       The same "MNR" labeling issue applies.
```

```text
Asset: Table 2 (PDF p32). Crossover budgets for perturbation at four δ, beside the fine-tuning crossovers for all four sets
       and five sizes.
Shows: the only printed table of every crossover value. It is the data owner for any chart.
Crop:  better used as data for nb chart than captured. If captured, keep the caption defining "> 20", "≤ 5" and "†".
```

```text
Asset: Figure 15 (PDF p25). 60M GSM8K frontiers split by fine-tuning optimizer (solid AdamW, dashed Muon) for both pretraining
       optimizers.
Shows: that the reversal survives either fine-tuning optimizer for the Muon model. This is the paper's answer to the "you
       fine-tuned Muon wrong" objection.
Crop:  keep the four-entry legend. Without it the solid/dashed coding is unreadable.
```

```text
Asset: Moonlight Table 6 (arXiv 2502.16982, PDF p10). The 2x2 of pretraining optimizer against SFT optimizer at 1.2T tokens.
Shows: the production-scale counter-evidence.
Crop:  keep the "Pretraining Optimizer" and "SFT Optimizer" header rows and the shot counts. Better reproduced as a small table
       with the citation.
```

```text
Asset: Wen et al. 2509.02046 Figure 1, bottom-left panel, "Speedup vs Model Size (8x Chinchilla)" (PDF p2).
Shows: Muon's pretraining-loss speedup shrinking from about 1.4x to 1.1x between 130M and 1.2B.
Crop:  that panel only, with its legend. It is pretraining loss, not fine-tuning, and the caption must say so.
```

For the other production reports (Kimi K2, GLM-4.5, GLM-5, Trinity, Kimi Linear) I found none worth capturing. Their architecture tables are better restated as numbers.

## Discarded

```text
https://arxiv.org/abs/2609.24678: Muon used as the fine-tuning optimizer for LoRA continual learning, not as the pretraining
  optimizer. It does not bear on the commission.
Web-search summary claiming 2611.03633 is a "COLM 2026 Workshop oral": contradicted by the co-author's own homepage, which
  lists "Preprint". Not used.
https://jxzhangjhu.github.io/blog/2026/how-frontier-labs-train-llms/ (seen only as a search snippet giving GLM-5 counts):
  secondary and superseded by the GLM-5 report itself.
https://hn.algolia.com/api/v1/search?query=2611.03633: the only hit was an unrelated Sakana AI thread.
```
