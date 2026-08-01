# Evidence record — build-from-scratch/speculative-decoding (01)

The two founding papers were read in full (PDF, primary text, not a summarizer's
paraphrase) and their accept/reject math, residual-distribution formula, and
correctness proofs are transcribed verbatim below with section/theorem
locators; I re-derived the proof independently (see "Clean statement for the
writer") and it matches both papers' own derivations term for term. The one
substantive risk for the writer's code is notational: Leviathan et al. write
**p = target, q = draft**; Chen et al. write **q = target, p = draft** — the
letters are swapped between the two papers. Both papers' formulas are
mathematically identical once you fix a convention; the evidence below flags
every place this matters. Six follow-on sources (Medusa, EAGLE, self-speculative
"Draft & Verify," Lookahead decoding, and two production writeups — PyTorch's
"GPT, Fast!" and vLLM's speculative-decoding blog) were read for one verified
measured number each, chosen because each either changes what "the draft
model" can be (Medusa/EAGLE/self-speculative/lookahead need no separate small
model, or need one with different properties) or complicates the "always
faster" reading of the core algorithm (workload- and load-dependence). The
evidence is thin on affiliations for the four follow-on arXiv papers (not
stated on the abstract pages I read) and on independent replication of Medusa/
EAGLE/lookahead's own math — those papers were read only for their abstract's
measured number and framing claim, per the brief's scope, not for a from-
scratch proof check the way the two founding papers were.

## Sources

### 1. Leviathan, Kalman, Matias — "Fast Inference from Transformers via Speculative Decoding"

- **URL**: https://arxiv.org/abs/2211.17192 (read via full PDF at
  https://arxiv.org/pdf/2211.17192, arXiv version v2, 18 May 2023; ICML 2023,
  PMLR 202)
- **Publisher/venue**: Proceedings of the 40th International Conference on
  Machine Learning (ICML 2023), Honolulu, Hawaii. Authors affiliated with
  Google Research, Mountain View, CA, USA (stated on the paper's first page).
- **Classification**: Primary. This is the paper that names and defines
  speculative decoding, the acceptance rule, the residual distribution, and
  proves the exact-distribution theorem — it owns all of these claims.
- **What it establishes firsthand**: the algorithm (Algorithm 1,
  `SpeculativeDecodingStep`), the acceptance-probability rule, the residual/
  adjusted distribution on rejection, the correctness proof, the acceptance-
  rate formula α, the expected-generated-tokens formula, and the walltime-
  improvement theorem, plus empirical α and speedup measurements on T5-XXL,
  a 97M-parameter GPT-like model, and LaMDA 137B.
- **Notation** (Section 2.1, p.2): "Let $M_p$ be the target model... and
  $p(x_t|x_{<t})$ the distribution we get from the model... Let $M_q$ be a
  more efficient approximation model... $q(x_t|x_{<t})$." **p = target, q =
  draft.**
- **The acceptance rule and residual distribution, verbatim** (Section 2.3,
  p.3): "To sample $x \sim p(x)$, we instead sample $x \sim q(x)$, keeping it
  if $q(x) \le p(x)$, and in case $q(x) > p(x)$ we reject the sample with
  probability $1 - \frac{p(x)}{q(x)}$ and sample $x$ again from an adjusted
  distribution $p'(x) = \mathrm{norm}(\max(0, p(x) - q(x)))$ instead. It's
  easy to show (see Appendix A.1) that for any distributions $p(x)$ and
  $q(x)$, and $x$ sampled in this way, indeed $x \sim p(x)$." This is
  algebraically the accept-with-probability-min(1, p/q) rule: keeping when
  q(x) ≤ p(x) always accepts (probability 1, since p/q ≥ 1), and rejecting
  with probability 1 − p(x)/q(x) when q(x) > p(x) means accepting with
  probability p(x)/q(x) in that case — i.e., accept with probability
  min(1, p(x)/q(x)) uniformly.
- **Algorithm 1, `SpeculativeDecodingStep`, verbatim** (Section 2.3, p.3):
  Samples γ guesses $x_1,\dots,x_\gamma$ autoregressively from $M_q$: for
  $i=1$ to γ, $q_i(x) \leftarrow M_q(prefix+[x_1,\dots,x_{i-1}])$,
  $x_i \sim q_i(x)$. Then runs $M_p$ in parallel on all γ+1 prefixes:
  $p_1(x),\dots,p_{\gamma+1}(x) \leftarrow M_p(prefix),\dots,
  M_p(prefix+[x_1,\dots,x_\gamma])$. Draws $r_1,\dots,r_\gamma \sim U(0,1)$
  and sets $n \leftarrow \min(\{i-1 \mid 1\le i\le\gamma,\ r_i >
  p_i(x)/q_i(x)\} \cup \{\gamma\})$ — the first rejected index minus one, or
  γ if none rejected. Sets $p'(x) \leftarrow p_{n+1}(x)$, and if $n < \gamma$,
  $p'(x) \leftarrow \mathrm{norm}(\max(0, p_{n+1}(x) - q_{n+1}(x)))$. Returns
  one token $t \sim p'(x)$ plus the n accepted tokens: `prefix + [x_1,...,
  x_n, t]`.
- **The correctness proof, verbatim** (Appendix A.1, "Correctness of
  Speculative Sampling," p.11): "We will now show that for any distributions
  $p(x)$ and $q(x)$, the tokens sampled via speculative sampling from $p(x)$
  and $q(x)$ are distributed identically to those sampled from $p(x)$ alone.
  Let β be the acceptance probability (Definition 3.1). Note that as
  $p'(x) = \mathrm{norm}(\max(0,p(x)-q(x))) =
  \frac{p(x)-\min(q(x),p(x))}{\sum_{x'}(p(x')-\min(q(x'),p(x')))} =
  \frac{p(x)-\min(q(x),p(x))}{1-\beta}$, the normalizing constant for the
  adjusted distribution $p'(x)$ is $1-\beta$... Now:
  $P(x=x') = P(\text{guess accepted}, x=x') + P(\text{guess rejected}, x=x')$
  Where: $P(\text{guess accepted}, x=x') = q(x')\min(1,\frac{p(x')}{q(x')}) =
  \min(q(x'),p(x'))$ And: $P(\text{guess rejected}, x=x') = (1-\beta)p'(x') =
  p(x')-\min(q(x'),p(x'))$ Overall: $P(x=x') = \min(p(x'),q(x')) + p(x') -
  \min(p(x'),q(x')) = p(x')$. As desired. ∎" This is stated as prose/proof in
  Appendix A.1, not as a numbered "Theorem" — the paper's formal numbered
  results (Def. 3.1, Def. 3.2, Lemma 3.3, Cor. 3.4, Thm 3.5, Cor. 3.6, Def.
  3.7, Thm 3.8, Cor. 3.9, Def. 3.10, Thm 3.11) live in Section 3, and the
  exact-distribution result is proved separately in the appendix and simply
  asserted ("It's easy to show (see Appendix A.1)...") in Section 2.3.
- **Acceptance rate α (Section 3.1–3.2, pp.3–4)**: Definition 3.1: "The
  acceptance rate $\beta_{x_{<t}}$, given a prefix $x_{<t}$, is the
  probability of accepting $x_t \sim q(x_t|x_{<t})$ by speculative sampling."
  $\alpha := E(\beta)$. Definition 3.2 defines a divergence $D_{LK}(p,q) =
  \sum_x |p(x)-M(x)|$ with $M=(p+q)/2$. Lemma 3.3: $D_{LK}(p,q) = 1 -
  \sum_x \min(p(x),q(x))$. Theorem 3.5: "$\beta = 1 - D_{LK}(p,q)$," proved
  as $\beta = E_{x\sim q(x)}[1 \text{ if } q(x)\le p(x); p(x)/q(x) \text{ if }
  q(x)>p(x)] = E_{x\sim q(x)}\min(1,p(x)/q(x)) = \sum_x \min(p(x),q(x))$.
  Corollary 3.6: "$\alpha = 1 - E(D_{LK}(p,q)) = E(\min(p,q))$."
- **Expected generated tokens (Section 3.1, Eq. 1, p.3)**: assuming the βs
  are i.i.d., the number of tokens from one run of Algorithm 1 is a capped
  geometric variable (success prob. 1−α, cap γ+1): $E(\#\text{generated
  tokens}) = \frac{1-\alpha^{\gamma+1}}{1-\alpha}$ (Equation 1).
- **Walltime improvement (Section 3.3, p.4)**: Definition 3.7 defines cost
  coefficient c = (time for one $M_q$ run)/(time for one $M_p$ run).
  Theorem 3.8: "The expected improvement factor in total walltime by
  Algorithm 1 is $\frac{1-\alpha^{\gamma+1}}{(1-\alpha)(\gamma c+1)}$."
  Corollary 3.9: "If α > c, there exists γ for which we'll get an
  improvement, and the improvement factor will be at least
  $\frac{1+\alpha}{1+c}$." — i.e., speedup is not guaranteed; it requires the
  draft's acceptance rate to exceed its relative cost.
- **Rejection sampling comparison (Appendix A.2, p.11)**: shows plain
  (non-speculative) rejection sampling with $M=\max_x p(x)/q(x)$ has expected
  accept probability $\le \alpha$, i.e., speculative sampling's construction
  is provably at least as efficient as naive rejection sampling for the same
  p, q — a useful aside for explaining *why* the min(1,p/q) + residual
  construction was chosen over textbook rejection sampling.
- **Empirical results**: Abstract: "2X-3X acceleration compared to the
  standard T5X implementation, with identical outputs" on T5-XXL (11B).
  Table 2 (Section 4.1, p.6, batch size 1, single TPU-v4): e.g. EnDe
  translation, $M_q$=T5-small (77M), temp=0, γ=7 → α=0.75, speed 3.4X;
  temp=1, γ=7 → α=0.62, speed 2.6X. CNN/DM summarization, T5-small, temp=0,
  γ=5 → α=0.65, speed 3.1X; temp=1, γ=5 → α=0.53, speed 2.3X. Table 3
  (Section 4.2, p.7) gives measured α for many $M_p$/$M_q$ pairs, e.g.
  GPT-like 97M target with a 6M-parameter draft: α=0.88 (argmax) / 0.89
  (temp=1); LaMDA 137B target with LaMDA 8B draft: α=0.75 (argmax) / 0.74
  (temp=1); even a bigram $M_q$ against T5-XXL gets α≈0.20, yielding a 1.25X
  speedup with γ=3 and c≈0 (Section 3.6, p.5).

### 2. Chen, Borgeaud, Irving, Lespiau, Sifre, Jumper (DeepMind) — "Accelerating Large Language Model Decoding with Speculative Sampling"

- **URL**: https://arxiv.org/abs/2302.01318 (read via full PDF at
  https://arxiv.org/pdf/2302.01318, arXiv v1, 2 Feb 2023; DeepMind technical
  report, dated 2023-2-3 on the paper itself)
- **Publisher**: DeepMind ("All authors from DeepMind," stated on p.1).
- **Classification**: Primary. This is the paper that names "speculative
  sampling" (SpS) and states its own accept/reject rule, its own correctness
  theorem, and its own measured Chinchilla-70B benchmark — it owns all of
  these.
- **What it establishes firsthand**: an independently-derived version of the
  same accept/reject scheme (developed "concurrently and independently" of
  Leviathan et al., per its own Related Work, p.2), a formal Theorem 1
  correctness proof, and measured speedups on Chinchilla 70B (XSum,
  HumanEval) including per-K acceptance-rate and loop-time curves.
- **Notation — the swap to flag**: Algorithm 2's preamble (p.3): "Given
  auto-regressive target model $q(.|.)$, and auto-regressive draft model
  $p(.|.)$." **q = target, p = draft** — the opposite letter assignment from
  Leviathan et al. (who use p = target, q = draft). Any equation copied
  between the two papers must have its p/q relabeled, not copied literally.
- **The acceptance rule, verbatim** ("Modified Rejection Sampling," p.4):
  "Given a sequence of tokens $x_1,\dots,x_n$, and $K$ draft tokens
  $\tilde x_{n+1},\dots,\tilde x_{n+K}$ generated from $p(.|.)$, we accept
  $\tilde x_{n+1}$ with probability: $\min\left(1,
  \frac{q(\tilde x_{n+1}|x_1,\dots,x_n)}{p(\tilde x_{n+1}|x_1,\dots,x_n)}
  \right)$ Where $q(\tilde x_{n+1}|x_1,\dots,x_n)$ and
  $p(\tilde x_{n+1}|x_1,\dots,x_n)$ are the probability of $\tilde x_{n+1}$
  according to the target and draft models respectively." Same functional
  form as Leviathan's rule, with q playing the role of "target" here instead
  of p.
- **The residual distribution, verbatim** (p.4): "If $\tilde x_{n+1}$ is
  rejected, we resample $x_{n+1}$ from the following distribution:
  $x_{n+1} \sim (q(x|x_1,\dots,x_n) - p(x|x_1,\dots,x_n))_+$ Where $(.)_+$
  denotes: $(f(x))_+ = \frac{\max(0,f(x))}{\sum_x \max(0,f(x))}$." Identical
  construction to Leviathan's `norm(max(0, ...))`, again with target-minus-
  draft in target-first order (q − p here vs. p − q there, consistent with
  the swapped letters).
- **Algorithm 2 "Speculative Sampling (SpS) with Auto-Regressive Target and
  Draft Models," verbatim** (p.3): draws K draft tokens autoregressively
  from p; computes K+1 sets of target logits from q in parallel; for
  t=1..K, draws $r\sim U[0,1]$, and "if $r < \min(1,
  \frac{q(x|x_1,\dots,x_{n+t-1})}{p(x|x_1,\dots,x_{n+t-1})})$" accepts and
  continues, else resamples from $(q-p)_+$ and exits the loop; if all K
  tokens are accepted, samples one bonus token from q and continues.
  Structurally identical to Leviathan's Algorithm 1 (draft γ/K tokens →
  single batched verification pass → accept/reject left to right → resample
  or bonus-sample one token).
- **The correctness proof, verbatim** (Supplementary Materials, "Proofs,"
  p.10–11): "**Theorem 1** (Modified Rejection Sampling recovers the target
  distribution). *Given discrete distributions $q$, $p$ and a single draft
  sample $\tilde x \sim p$, let $X$ be the final resulting sample. For $X=x$
  to be true, we must either sample $\tilde x = x$ and then accept it, or
  resample it after $\tilde x$ (of any value) is rejected. Hence:*
  $\mathbb{P}(X=x) = \mathbb{P}(\tilde x=x)\mathbb{P}(\tilde x \text{
  accepted}|\tilde x=x) + \mathbb{P}(\tilde x \text{ rejected})
  \mathbb{P}(X=x|\tilde x \text{ rejected})$ For the first term: $p(x)
  \min(1,\frac{q(x)}{p(x)}) = \min(p(x),q(x))$. For the second: $\mathbb{P}
  (X=x|\tilde x \text{ rejected}) = (q(x)-p(x))_+$. And $\mathbb{P}(\tilde x
  \text{ rejected}) = 1-\sum_{x'}\min(p(x'),q(x')) = \sum_{x'}\max(0,
  q(x')-p(x'))$, which is exactly the denominator of $(q(x)-p(x))_+$, so
  $\mathbb{P}(\tilde x \text{ rejected})\mathbb{P}(X=x|\tilde x \text{
  rejected}) = \max(0,q(x)-p(x))$. Hence: $\mathbb{P}(X=x) = \min(p(x),q(x))
  + \max(0,q(x)-p(x)) = q(x)$ and we have recovered the desired target."
  This is the paper's one formally labeled "Theorem," unlike Leviathan et
  al.'s unlabeled Appendix A.1 proof — same result, opposite letters (q(x)
  is the recovered target distribution here because q is defined as target
  in this paper).
- **Empirical results** (Table 1, p.6; "Results," p.5): draft model is 4B
  parameters (8 layers, $d_{model}$=6144, 48 heads) vs. target Chinchilla 70B
  (80 layers, $d_{model}$=8192, 64 heads; Table 2/Hyperparams, p.10), both
  trained on 16 TPU v4s. Draft sampling speed "1.8ms/token compared to
  14.1ms/token for Chinchilla" (p.5). At batch size 1, K=4: XSum (nucleus,
  p=0.8) — ArS 14.1ms/token vs. SpS 7.52ms/token, "1.92×" speedup, ROUGE-2
  0.112→0.114 (parity). XSum (greedy) — 2.01× speedup, ROUGE-2 0.157→0.156.
  HumanEval 100-shot (nucleus, p=0.95, temp=0.8) — SpS 5.73ms/token, "2.46×"
  speedup, pass rate 45.1%→47.0% (Table 1). Abstract: "2–2.5× decoding
  speedup in a distributed setup." Figure 1 (p.7) shows acceptance rate
  falling from ~1.0 toward ~0.45–0.7 as K rises from 0 to 7, and total loop
  time rising roughly linearly with K — the paper's own evidence that
  "longer drafts" is not free and has a workload-specific optimum (XSum
  nucleus latency is minimized at K=3, stated explicitly on p.7).

### 3. Cai, Li, Geng, Peng, Lee, Chen, Dao — "Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"

- **URL**: https://arxiv.org/abs/2401.10774 (arXiv, first submitted 19 Jan
  2024; last revised 14 Jun 2024, v3)
- **Publisher**: arXiv preprint (accepted ICML 2024 per ACM DL record
  3692070.3692273). Affiliation not stated on the abstract page I read.
- **Classification**: Primary for its own measured speedup (Medusa's authors
  ran their own benchmark and report it in their own abstract). Read at
  abstract depth only, per brief scope — not verified against the full paper
  body/math the way the two founding papers were.
- **What changes the picture**: Medusa removes the separate draft *model*
  entirely. It "augments LLM inference by adding extra decoding heads to
  predict multiple subsequent tokens in parallel," verified with a
  tree-based attention mechanism, so drafting and target model share one set
  of weights instead of two models with an acceptance-rate/cost trade-off
  between them.
- **One measured number**: "Medusa-1 can achieve over 2.2x speedup without
  compromising generation quality, while Medusa-2 further improves the
  speedup to 2.3-3.6x" (abstract).

### 4. Li, Wei, Zhang, Zhang — "EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty"

- **URL**: https://arxiv.org/abs/2401.15077 (arXiv, submitted late Jan 2024)
- **Publisher**: arXiv preprint. Affiliation not stated on the abstract page
  I read.
- **Classification**: Primary for its own measured speedup. Read at abstract
  depth only.
- **What changes the picture**: EAGLE drafts at the *feature* level (the
  second-to-top-layer hidden state) rather than the token level, arguing
  (per its own abstract) that "autoregression at the feature... level is
  more straightforward than at the token level" but that feature-level
  autoregression has inherent uncertainty; EAGLE resolves this by
  conditioning the feature predictor on a token sequence advanced one step,
  while "maintaining the distribution of the generated text" (i.e., it still
  uses the acceptance-rule construction to stay exact, not a lossy
  approximation).
- **One measured number**: "For LLaMA2-Chat 70B, EAGLE achieved a latency
  speedup ratio of 2.7x-3.5x, doubled throughput" (abstract). Also: on
  MT-bench "EAGLE is 3x faster than vanilla decoding, 2x faster than
  Lookahead, and 1.6x faster than Medusa" — a head-to-head comparison against
  sources 6 and 3 below, from EAGLE's own paper (so primary for EAGLE's
  measurement of itself, secondary/contested for the Lookahead and Medusa
  comparison numbers, which those two papers did not themselves report in
  this configuration).

### 5. Zhang, Wang, Li, Shou, Chen, Chen, Mehrotra — "Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding"

- **URL**: https://arxiv.org/abs/2309.08168 (arXiv, accepted ACL 2024)
- **Publisher**: arXiv preprint / ACL 2024 (62nd Annual Meeting of the
  Association for Computational Linguistics). Affiliation not stated on the
  abstract page I read.
- **Classification**: Primary for its own measured speedup. Read at abstract
  depth only.
- **What changes the picture**: this is the "self-speculative" variant —
  "accelerating Large Language Models (LLMs) without the need for an
  auxiliary model," by "selectively skipping certain intermediate layers"
  of the *same* model to produce a cheap draft, then verifying with the full
  model in one forward pass. It reuses the identical accept/reject
  correctness argument (the paper's own framing: "This process ensures the
  final output remains identical to that produced by the unaltered LLM")
  but removes the need to train or host a second model at all.
- **One measured number**: "Benchmarks with LLaMA-2 and its variants
  demonstrated a speedup up to 1.99×" (abstract).

### 6. Fu, Bailis, Stoica, Zhang — "Break the Sequential Dependency of LLM Inference Using Lookahead Decoding"

- **URL**: https://arxiv.org/abs/2402.02057 (arXiv, submitted 3 Feb 2024;
  ICML 2024)
- **Publisher**: arXiv preprint / ICML 2024. Affiliation not stated on the
  abstract page I read.
- **Classification**: Primary for its own measured speedup. Read at abstract
  depth only.
- **What changes the picture**: Lookahead decoding needs no draft model and
  no data store at all — it is "an exact, parallel decoding algorithm that
  accelerates LLM decoding without needing auxiliary models," using Jacobi-
  iteration-style parallel n-gram extraction and verification directly
  against the one target model. It is a different mechanism for generating
  candidates than "small model drafts, big model checks," while still being
  exact (its abstract calls it "exact, parallel").
- **One measured number**: "Our implementation of Lookahead decoding can
  speed up autoregressive decoding by up to 1.8x on MT-bench and 4x with
  strong scaling on multiple GPUs in code completion tasks" (abstract) — the
  4x figure is explicitly workload- and hardware-scaling-specific (multi-GPU,
  code completion), not a general single-GPU number.

### 7. PyTorch team — "Accelerating Generative AI with PyTorch II: GPT, Fast!"

- **URL**: https://pytorch.org/blog/accelerating-generative-ai-2/ (PyTorch
  blog; confirmed resolving, read in full via fetch)
- **Publisher**: PyTorch (Meta/PyTorch Foundation engineering blog).
- **Classification**: Primary for its own measured numbers — this is an
  engineering team reporting the speedup it measured on its own from-scratch
  implementation (`gpt-fast`), not a third party repeating someone else's
  number.
- **What it establishes firsthand**: a production-style engineering
  demonstration that speculative decoding's realized speedup depends heavily
  on how well the draft and target models agree, using two draft/target
  pairs on the same codebase.
- **Numbers, verbatim**: "when running CodeLlama-34B + CodeLlama-7B, we're
  able to obtain a 2x boost in tokens/s for generating code," but "when
  using Llama-7B + TinyLlama-1B, we're only able to obtain about a 1.3x
  boost in tokens/s." Explicit caveat, verbatim: "Although speculative
  decoding guarantees that we have mathematically identical results compared
  to regular generation, it does have the property that the runtime
  performance varies depending on the generated text, as well as how aligned
  the draft and verifier model are." This directly supports (and is a
  concrete instance of) Leviathan's Corollary 3.9 condition (α must exceed
  cost c) and the general point that acceptance rate, not just draft-model
  cheapness, governs the payoff.

### 8. vLLM team — "How Speculative Decoding Boosts vLLM Performance by up to 2.8x"

- **URL**: https://blog.vllm.ai/2024/10/17/spec-decode.html (redirects to
  https://vllm.ai/blog/2024-10-17-spec-decode; confirmed resolving, read via
  fetch), published 17 Oct 2024, authored by the vLLM team.
- **Publisher**: vLLM project blog.
- **Classification**: Primary for vLLM's own benchmark of its own serving
  system — the party that ran the measurement.
- **What it establishes firsthand**: at low query rate (QPS=1), Llama-3-70B
  on 4×H100, draft-model-based speculative decoding gets "up to a 1.5x
  speedup in token generation" on ShareGPT, and n-gram/prompt-lookup
  decoding gets "up to 2.8x" on CNN/DailyMail summarization (Figures 5–6 in
  the source). Critically, at higher request rates the same post documents
  the effect reversing: "the overhead of speculative decoding can outweigh
  its benefits, leading to reduced performance" once the GPU is
  compute-saturated, with roughly a 1.4x slowdown on ShareGPT and 1.8x
  slowdown on CNN/DailyMail at higher QPS (Figure 7). This is the load-
  dependence the commission's "memory-bandwidth-bound decoding" framing
  needs: the free-lunch framing (accuracy is free) is true; the speed
  framing (speed is always better) is not — extra compute is spent on every
  draft attempt, so once compute rather than memory bandwidth is the
  bottleneck, speculative decoding can slow things down.

## Clean statement for the writer: acceptance rule, residual, and equivalence proof

Using **p = target distribution, q = draft distribution** (Leviathan et al.'s
convention — recommend the article adopt this one and note Chen et al.'s
swapped p/q once, since it is the more common downstream convention, e.g. in
Source 1's own later citations):

1. **Setup.** To sample from the target p, we first sample a candidate
   $x \sim q$ from the cheap draft model, drawing a fresh $r \sim U(0,1)$.
2. **Accept rule.** Accept x (keep it as the output) if
   $r \le \min\!\left(1, \dfrac{p(x)}{q(x)}\right)$. Because r is uniform on
   [0,1], this makes the probability of acceptance, given the draft x, exactly
   $\min(1, p(x)/q(x))$: always accept when $q(x)\le p(x)$ (the draft
   underweighted x relative to the target), accept with probability
   $p(x)/q(x) < 1$ when $q(x) > p(x)$ (the draft overweighted x).
3. **Residual on rejection.** If rejected, discard x and draw a fresh sample
   from the normalized positive residual $p'(x) = \dfrac{\max(0, p(x) -
   q(x))}{\sum_{x'} \max(0, p(x') - q(x'))} = \mathrm{norm}(\max(0, p(x) -
   q(x))_+)$ — i.e., only from the part of the target distribution the draft
   under-covered, renormalized to sum to 1.
4. **Equivalence proof** (matches Source 1 Appendix A.1 and Source 2 Theorem
   1 exactly once relabeled to this convention):
   - Marginal probability that x is produced *and accepted*, for any fixed
     x′: $q(x')\cdot\min\!\left(1,\frac{p(x')}{q(x')}\right) = \min(p(x'),
     q(x'))$. (When $q\le p$: $q\cdot 1 = q = \min(p,q)$. When $q>p$:
     $q\cdot p/q = p = \min(p,q)$. Either way it equals $\min(p(x'),q(x'))$.)
   - Total probability of rejection, summed over the draft's own
     distribution: $1 - \sum_{x'} \min(p(x'), q(x')) = \sum_{x'}\big(q(x') -
     \min(p(x'),q(x'))\big) = \sum_{x'} \max(0, q(x')-p(x'))$. Call this
     quantity $1-\beta$ where $\beta = \sum_{x'}\min(p(x'),q(x'))$ is the
     acceptance rate (Source 1 Theorem 3.5/Corollary 3.6).
   - Probability that x′ is produced *via the residual path*: (probability of
     rejection) × (probability the residual draw lands on x′) =
     $(1-\beta) \cdot \dfrac{\max(0, p(x')-q(x'))}{1-\beta} = \max(0,
     p(x')-q(x'))$ — the $(1-\beta)$ cancels exactly against the residual's
     own normalizing constant, which is why the residual is normalized by
     $\sum \max(0, p-q)$ and not by anything else.
   - Sum the two paths: $P(\text{output}=x') = \min(p(x'),q(x')) +
     \max(0, p(x')-q(x'))$. If $p(x')\ge q(x')$: this is $q(x') + (p(x')-
     q(x')) = p(x')$. If $p(x') < q(x')$: this is $p(x') + 0 = p(x')$. In
     both cases the sum is exactly $p(x')$ — the accept-path and residual-
     path probabilities are complementary pieces of p that partition
     perfectly regardless of how p and q compare at x′. **This is the whole
     equivalence proof**; it holds for *any* q with the same support
     considerations as p (Source 1, Section 3.6: "Speculative sampling...
     guarantee[s] an identical output distribution for any choice of
     approximation model $M_q$ without restriction").
5. **Extending to γ (or K) draft tokens.** Both papers apply the single-token
   rule token-by-token, left to right, against the batch of γ+1 (or K+1)
   target-model distributions computed in one parallel forward pass over the
   drafted prefix (Source 1 Algorithm 1; Source 2 Algorithm 2): accept
   greedily while r_i ≤ min(1, p_i/q_i) holds; at the first rejection, resample
   from that position's residual and stop; if every draft token is accepted,
   sample one bonus token from the target's own next-position distribution
   (since it was already computed for free in the same forward pass). Because
   each single-position step above is individually exact and the process is
   Markov given the accepted prefix, the joint sequence distribution equals
   what plain autoregressive sampling from p would have produced at every
   position — this composition argument is implicit in both papers'
   algorithm statements but not spelled out as a separate joint-distribution
   theorem in either; it is a straightforward induction on top of the
   single-token result above and worth stating explicitly as such in the
   article rather than attributing it to either source verbatim.
6. **Acceptance rate and expected speedup** (Source 1, Section 3.1–3.3): the
   position-level acceptance rate is $\beta = \sum_x \min(p(x),q(x)) = 1 -
   D_{LK}(p,q)$ (Theorem 3.5) where $D_{LK}$ is total-variation-style
   divergence between p and q (Definition 3.2/Lemma 3.3); $\alpha := E[\beta]$
   over the sequence (Corollary 3.6). Assuming i.i.d. β per position, the
   number of tokens produced per iteration is a geometric variable capped at
   γ+1: $E[\#\text{tokens}] = \frac{1-\alpha^{\gamma+1}}{1-\alpha}$ (Equation
   1). With cost ratio $c$ = (draft model time)/(target model time) per call,
   expected walltime speedup is $\frac{1-\alpha^{\gamma+1}}{(1-\alpha)(\gamma
   c+1)}$ (Theorem 3.8), positive only when $\alpha > c$ (Corollary 3.9).

## Contradictions / uncertainties

1. **Notation swap (real, not an error).** Leviathan et al. use p = target, q
   = draft; Chen et al. use q = target, p = draft (Sources 1 and 2, both
   quoted above). Both derivations are correct and isomorphic under
   relabeling; a reader or implementer copying an equation from one paper
   using the other paper's variable names would silently invert accept and
   residual. The article must pick one convention, state it once, and never
   let a quoted equation from the other paper stand un-relabeled next to code
   using the first convention.
2. **EAGLE's head-to-head numbers against Lookahead and Medusa (Source 4)**
   are EAGLE's own paper's report of the comparison ("3x faster than vanilla
   decoding, 2x faster than Lookahead, and 1.6x faster than Medusa" on
   MT-bench) — primary for EAGLE's own measurement, but not independently
   confirmed by Lookahead's or Medusa's own papers (Sources 6 and 3 report
   different benchmarks — MT-bench/multi-GPU code completion for Lookahead,
   generic "quality-preserving" framing for Medusa — not this same
   three-way comparison). Treat the three-way ranking as EAGLE's claim about
   itself relative to reimplementations of the others, not as independently
   corroborated.
3. **Every follow-on speedup number is workload- and hardware-specific, not
   general.** Explicitly flagged by the sources themselves: Chen et al.'s own
   Figure 1 shows acceptance rate and optimal K differing between XSum and
   HumanEval, with XSum's latency-optimal K=3 stated explicitly (Source 2);
   the PyTorch blog's CodeLlama-pair (2x) vs. TinyLlama-pair (1.3x) numbers
   differ by nearly 2x depending only on how well the two models agree
   (Source 7); the vLLM blog's numbers reverse from up to 2.8x speedup at low
   query rate to roughly 1.4–1.8x *slowdown* at high query rate on the same
   hardware and models, because speculative decoding trades memory-bandwidth
   idle time for extra compute, and that trade only pays when the GPU has
   compute headroom to spend (Source 8). None of these numbers should be
   quoted in the article without the workload/regime attached.
4. **Affiliations for Sources 3–6 (Medusa, EAGLE, Draft & Verify, Lookahead)
   were not stated on the arXiv abstract pages I read.** I did not open the
   full PDFs for these four (out of the brief's scope, which calls for the
   two founding papers to be verified in full and the follow-ons captured for
   "one concrete measured number each"), so I am not asserting institutional
   affiliation for their authors beyond the author name lists themselves.

## Numbers

| # | Value | Owning primary source | Locator | What it measures | Denominator/basis |
|---|---|---|---|---|---|
| 1 | 2X–3X | Leviathan et al. | Abstract; Table 2, §4.1 | Walltime speedup, T5-XXL (11B) vs. T5X baseline | batch size 1, single TPU-v4, EnDe translation & CNN/DM summarization |
| 2 | α=0.75, γ=7 → 3.4X speed | Leviathan et al. | Table 2, §4.1 | Best measured config, T5-small draft, EnDe, argmax | same setup as #1 |
| 3 | α≈0.20 → 1.25X speed | Leviathan et al. | §3.6, p.5 | Trivial bigram draft model vs. T5-XXL target, EnDe | c≈0 (negligible-cost draft) |
| 4 | α=0.88–0.89 | Leviathan et al. | Table 3, §4.2 | 6M-param draft vs. 97M-param GPT-like target, lm1b | argmax/temp=1 |
| 5 | α=0.74–0.75 | Leviathan et al. | Table 3, §4.2 | LaMDA 8B draft vs. LaMDA 137B target, dialog task | argmax/temp=1 |
| 6 | 2–2.5× | Chen et al. | Abstract | Chinchilla 70B decoding speedup, distributed setup | 16 TPU v4s |
| 7 | 1.92× (7.52ms/token vs. 14.1ms/token) | Chen et al. | Table 1 | XSum nucleus sampling (p=0.8), Chinchilla+4B draft | batch size 1, K=4 |
| 8 | 2.46× (5.73ms/token) | Chen et al. | Table 1 | HumanEval 100-shot (nucleus p=0.95, temp=0.8) | batch size 1, K=4 |
| 9 | 1.8ms/token vs. 14.1ms/token | Chen et al. | "Results," p.5 | Raw per-token sampling speed, draft (4B) vs. target (70B) | 16 TPU v4s |
| 10 | 2.2x+ (Medusa-1), 2.3–3.6x (Medusa-2) | Cai et al. (Medusa) | Abstract | Extra-decoding-heads speedup | not stated beyond abstract |
| 11 | 2.7x–3.5x, "doubled throughput" | Li et al. (EAGLE) | Abstract | LLaMA2-Chat 70B, feature-level drafting | not stated beyond abstract |
| 12 | up to 1.99× | Zhang et al. (Draft & Verify) | Abstract | LLaMA-2 and variants, layer-skipping self-draft | not stated beyond abstract |
| 13 | up to 1.8× (MT-bench), up to 4× (multi-GPU code completion) | Fu et al. (Lookahead) | Abstract | No-draft-model parallel n-gram decoding | 4× figure is multi-GPU-scaling-specific |
| 14 | 2x (CodeLlama-34B+7B) vs. 1.3x (Llama-7B+TinyLlama-1B) | PyTorch team | "GPT, Fast!" blog | Draft/target alignment sensitivity, tokens/s | own gpt-fast implementation |
| 15 | up to 1.5x (ShareGPT, draft model) / 2.8x (CNN-DM, n-gram) at QPS=1; ~1.4–1.8x *slowdown* at high QPS | vLLM team | vLLM blog, Figs. 5–7 | Load-dependent reversal of speedup | Llama-3-70B, 4×H100 |

## Source assets

- **Leviathan et al. Figure 1 (p.2)**: a worked trace of unconditional
  language-model generation, one line per algorithm iteration, coloring
  accepted draft tokens green and rejected/corrected tokens red/blue. A crop
  should keep at least 3–4 consecutive iteration lines and the color legend;
  it is the clearest existing illustration of what "accept, then resample
  the first rejection" looks like token-by-token, and could inspire (not be
  copied as) a similar visualization built from the article's own run.
- **Leviathan et al. Figure 5 (p.6)**: a trace/timeline diagram comparing
  wall-clock schedules for γ=7, γ=3, and plain baseline decoding, showing
  which calls are to $M_p$ vs. $M_q$ and where the encoder cost sits. Useful
  for explaining *why* fewer serial target-model calls yield speedup even
  though total arithmetic work rises; a crop must keep all three rows
  (γ=7, γ=3, baseline) for the comparison to make sense.
- **Chen et al. Figure 1 (p.7)**: three-panel plot (mean sampling time,
  acceptance rate, total loop time, each vs. K=0..7) for XSum and HumanEval.
  Directly shows the diminishing-returns shape behind "choosing γ/K" — total
  loop time rises roughly linearly with K while acceptance rate falls, so
  the speedup-optimal K is an interior point, not "as large as possible." A
  crop should keep all three panels together since the tradeoff is the
  point, not any single curve.
- **Leviathan et al. Table 1 (p.5)** and **Chen et al. Table 1 (p.6)**: both
  are small, already-tabular results (operations/speed vs. α,γ; and
  ROUGE-2/pass-rate vs. speedup) that could be adapted as a comparison table
  in the article rather than as an image — furniture, not visual asset,
  since the source data is already discrete numbers.
- Sources 3–8 (Medusa, EAGLE, Draft & Verify, Lookahead, PyTorch blog, vLLM
  blog): **not assessed** — only abstracts (and, for the two blogs, the full
  post text) were read; I did not review their figures/tables in the PDF
  bodies of the four arXiv follow-ons, so I am not recommending specific
  crops from papers I did not open beyond the abstract.

## Discarded

- `https://arxiv.org/html/2211.17192` and `https://arxiv.org/html/2302.01318`
  — both returned HTTP 404; arXiv did not generate an automatic HTML render
  for these submission dates (predates arXiv's HTML rollout). Discarded in
  favor of the full PDF, which was read directly and is quoted throughout
  above.
- `https://ar5iv.labs.arxiv.org/html/2211.17192` — fetched as a fallback HTML
  mirror; when asked to reproduce Algorithm 1 and the Appendix A.1 proof
  verbatim, the fetch tool's summarizing model declined on fair-use grounds
  and offered only a paraphrase. Discarded as a source of verbatim text in
  favor of the primary PDF (read directly via the Read tool, which returns
  the actual page images/text rather than a third-party summary), which is
  what all verbatim quotes above are drawn from.
- Several third-party "speculative decoding explained" tutorial/marketing
  blog posts surfaced in search results while locating Sources 7–8 (from
  Introl, Spheron, CoddyKit, DigitalOcean, and Jarvis Labs) were seen only as
  search snippets and never opened — excluded on sight because the
  commission bars repeating vendor marketing figures unverified, and each
  appeared to be restating other parties' benchmark numbers rather than
  reporting a measurement the author's own team ran. Not opened, so not
  claimed as "read and rejected," only noted here so the writer does not
  independently reach for them expecting they were vetted.
