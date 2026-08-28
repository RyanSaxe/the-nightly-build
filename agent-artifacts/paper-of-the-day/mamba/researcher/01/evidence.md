# Evidence: paper-of-the-day/mamba (01)

The evidence supports the commissioned angle in its precise form and sharpens
where the claim stops. The focal paper (arXiv:2312.00752) states the math the
reconstruction needs at exact locators: the continuous SSM (Eq. 1), the
ZOH-discretized recurrence (Eq. 2, Eq. 4), the convolutional form it gives up
(Eq. 3), the selection mechanism that makes B, C, and Δ input-dependent
(Algorithm 2, §3.2), and the hardware-aware scan that restores speed once
selection kills the convolution (§3.3). The empirical claims each trace to a
named figure or table: selective copying (Fig. 4), induction-head extrapolation
to million-length sequences (Fig. 5), language-modeling scaling against
Transformer++ (Fig. 6), zero-shot downstream accuracy (Table 1), and the scan and
throughput benchmarks (Fig. 12). The public record since publication confirms the
architecture (Mamba-2 / state-space duality, and the NVIDIA 8B study) and
qualifies it exactly where the commission expected: pure selective SSMs trail
attention on tasks needing bulk verbatim copying, associative recall, and state
tracking, and the field's answer has been to reintroduce a small fraction of
attention (Jamba, the NVIDIA hybrid). The record does not undermine the angle. It
lets the writer weigh the claim rather than announce it.

Two limitations to flag. First, the paper's math and every figure/table label and
number below were read from the arXiv HTML v2 rendering; the downstream asset step
should confirm the exact figure images against the paper PDF when capturing them
with `nb asset`, and confirm the printed accuracy values in Fig. 4 and Table 1 at
pixel level. Second, one predecessor and one recall study (S4; Zoology) establish
context the writer should attribute carefully: Zoology's tested models predate
Mamba's selection mechanism, so it frames the recall gap without measuring Mamba
itself.

## Sources

```text
URL:         https://arxiv.org/abs/2312.00752
Kind:        primary — the focal paper; Gu and Dao own every claim, figure, and equation the reconstruction sets.
Establishes: The central claim and all of its supporting math and experiments. Title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces," Albert Gu and Tri Dao. arXiv:2312.00752, cs.LG. v1 submitted 1 Dec 2023; v2 (the version read) 31 May 2024. Not yet a venue paper at v2; widely cited as the Mamba paper. The abstract card should quote the abstract verbatim (recorded under Quote).
Paraphrase:  Foundation models rest on attention, whose cost is quadratic in sequence length. Prior sub-quadratic models (linear attention, gated convolutions, recurrent models, structured SSMs) had not matched attention on language. The paper diagnoses the weakness as an inability to do content-based reasoning, and fixes it by making the SSM's parameters functions of the input, so the model can selectively propagate or forget along the sequence depending on the current token. That change forecloses the efficient convolution, so they design a hardware-aware parallel scan that runs in recurrent mode. The selective SSM goes into a simplified architecture with no attention and no MLP block (Mamba). Claims: 5x higher inference throughput than Transformers, linear scaling in length, and a 3B model that beats same-size Transformers and matches Transformers twice its size.
Locators:    Abstract; §2 (SSMs, discretization, convolution); §3.1 (motivation from selective copying / induction); §3.2 + Algorithm 2 (the S6 selection mechanism); §3.3 (efficient implementation, hardware-aware scan); §3.4 (Mamba block); §3.5 (interpretation, gating connection); §4.1–4.2, §4.5 (experiments).
Quote:       Abstract, verbatim: "Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5x higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation."
```

The exact math to set, from §2 and §3.2 (equations transcribed from the arXiv HTML v2):

- Continuous SSM (Eq. 1): h'(t) = A h(t) + B x(t);  y(t) = C h(t).
- Discretized recurrence (Eq. 2): h_t = A-bar h_{t-1} + B-bar x_t;  y_t = C h_t.
- ZOH discretization (Eq. 4): A-bar = exp(Δ A);  B-bar = (Δ A)^{-1} (exp(Δ A) − I) · Δ B. (Δ is the step size; discretization is the rule that turns the continuous (A, B) into discrete (A-bar, B-bar).)
- Convolutional form for the time-invariant case (Eq. 3): K-bar = (C B-bar, C A-bar B-bar, ..., C A-bar^k B-bar, ...);  y = x * K-bar. This is the global convolution S4 uses and Mamba gives up.
- Selection (Algorithm 2, §3.2): the parameters become input-dependent. B ← s_B(x) = Linear_N(x); C ← s_C(x) = Linear_N(x); Δ ← τ_Δ(Parameter + s_Δ(x)) with s_Δ(x) = Broadcast_D(Linear_1(x)) and τ_Δ = softplus. Shapes go from (D, N) time-invariant to (B, L, D, N) time-varying, which is exactly what breaks the convolution. A stays a learned per-channel parameter and becomes selective only through Δ (see §3.5.2).

```text
URL:         https://arxiv.org/abs/2405.21060
Kind:        primary — the Mamba-2 / state-space-duality paper; same authors (Dao and Gu). It owns the SSD framework and the Mamba-2 layer.
Establishes: That structured SSMs and a form of attention are two views of the same object (state space duality, SSD), through decompositions of structured semiseparable matrices, and that this yields Mamba-2, a refined selective-SSM layer 2–8x faster than Mamba-1 while staying competitive with Transformers. Title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality." Tri Dao, Albert Gu. arXiv:2405.21060, submitted 31 May 2024, ICML 2024. CONFIRMS and generalizes Mamba: it does not contradict the claim; it places Mamba on a firmer theoretical footing and speeds it up.
Paraphrase:  SSMs like Mamba match or beat Transformers at small-to-medium scale. The two families are closely related: SSD connects them through semiseparable-matrix decompositions, letting the authors design Mamba-2 whose core layer refines Mamba's selective SSM to be 2–8x faster while remaining competitive on language modeling.
Locators:    Abstract; SSD framework in the body (semiseparable matrices); Mamba-2 layer design.
Quote:       "Our state space duality (SSD) framework allows us to design a new architecture (Mamba-2) whose core layer is a[] refinement of Mamba's selective SSM that is 2-8X faster, while continuing to be competitive with Transformers on language modeling."
```

```text
URL:         https://arxiv.org/abs/2403.19887
Kind:        primary — the Jamba paper; AI21 owns the architecture and the ablations it reports.
Establishes: That a production model interleaves attention with Mamba (ratio 1 attention layer to 7 Mamba layers per 8-layer block, MoE on alternate layers), and that pure Mamba's specific failure is in-context learning / format following, which even a single attention layer in eight repairs. QUALIFIES the "replace attention" reading: the field's frontier long-context model keeps a slice of attention on purpose. Title: "Jamba: A Hybrid Transformer-Mamba Language Model," Lieber et al. (AI21 Labs). arXiv:2403.19887, submitted 28 Mar 2024, rev. 3 Jul 2024. Context length up to 256K tokens, fits on one 80GB GPU.
Paraphrase:  Jamba interleaves Transformer and Mamba layers with MoE to get the benefits of both. In an ablation, the pure Mamba model often fails to follow the answer format (e.g. producing something other than "Positive"/"Negative" on IMDB), which the authors attribute to weak in-context learning from the absence of attention; the hybrid does ICL successfully even with only 1 of 8 layers attention.
Locators:    Abstract; architecture/config section (block definition l=8, a:m=1:7); ablation on ICL / format following.
Quote:       "The pure Mamba model often does not follow the correct format... While the Attention model adheres to this format, the pure Mamba model often produces other answers." And: "the hybrid Attention-Mamba model does perform successful ICL, even when only 1 out of 8 layers is an Attention one."
```

```text
URL:         https://arxiv.org/abs/2402.01032
Kind:        primary — the copying-limits paper; the authors own the theorem and the experiments. Secondary only insofar as it reports on Mamba from outside.
Establishes: The strongest on-topic criticism: models with a fixed-size state that does not grow with sequence length (which the authors call generalized state space models, GSSMs, and which includes Mamba) are fundamentally limited at copying from context, because a bounded state cannot store an arbitrarily long string. A two-layer Transformer can copy exponentially long strings; Mamba cannot. QUALIFIES the induction-head win: single-item associative retrieval is not bulk verbatim copying. Title: "Repeat After Me: Transformers are Better than State Space Models at Copying," Jelassi, Brandfonbrener, Kakade, Malach. arXiv:2402.01032, submitted 1 Feb 2024, rev. 3 Jun 2024 (ICML 2024).
Paraphrase:  GSSMs use a fixed-size latent state independent of sequence length and are efficient at inference, but they are limited versus Transformers on tasks that require copying from the input context. A two-layer Transformer can duplicate strings of exponential length; a bounded-state model provably cannot store an arbitrarily long input. Pretrained Transformers substantially outperform pretrained SSMs at retrieving and reproducing context.
Locators:    Abstract; theoretical section (two-layer Transformer copies exponential-length strings; GSSM bounded-memory bound); empirical section (synthetic copying generalization; pretrained-LM evaluation).
Quote:       "while GSSMs are promising in terms of inference-time efficiency, they are limited compared to transformer models on tasks that require copying from the input context."
```

```text
URL:         https://arxiv.org/abs/2406.07887
Kind:        primary — NVIDIA's controlled 8B-scale study; the authors own the trained models and measurements. Reports on Mamba from a third party (Gu and Dao are among many co-authors).
Establishes: At 8B parameters and 3.5T tokens, pure Mamba/Mamba-2 match or exceed Transformers on many standard tasks but fall short on tasks needing strong copying or in-context learning (5-shot MMLU, Phonebook) and long-context reasoning. A hybrid of 43% Mamba-2, 7% attention, and 50% MLP layers exceeds the 8B Transformer on all 12 standard tasks (+2.65 avg) and matches or beats it across 23 long-context tasks, with a projected ~8x inference speedup. CONFIRMS the efficiency and the standard-task parity; QUALIFIES with the recall/ICL gap and the hybrid remedy. Title: "An Empirical Study of Mamba-based Language Models," Waleffe et al. (NVIDIA). arXiv:2406.07887, submitted 12 Jun 2024.
Paraphrase:  Selective SSMs overcome the Transformer's quadratic cost and KV-cache memory. But direct comparison at scale shows pure SSMs lag on copying, in-context learning, and long-context reasoning. A hybrid with a small share of attention (7%) closes and reverses the gap on standard and long-context tasks while keeping most of the speed advantage.
Locators:    Abstract; task-category results (5-shot MMLU, Phonebook, long-context); hybrid composition (43% Mamba-2 / 7% attention / 50% MLP) and its 12-task and 23-task results.
Quote:       Pure SSMs lag on "tasks which require strong copying or in-context learning abilities (e.g., 5-shot MMLU, Phonebook) or long-context reasoning."
```

```text
URL:         https://arxiv.org/abs/2404.08819
Kind:        primary — the expressivity paper; the authors own the complexity-theoretic result and the state-tracking experiments.
Establishes: That despite the recurrent framing, SSMs (including Mamba/S6) sit in the complexity class TC0, the same ceiling as Transformers, so they provably cannot solve state-tracking problems like permutation composition, and by extension cannot reliably track chess moves, evaluate code, or track entities across a long narrative. QUALIFIES the "recurrent, RNN-like" selling point: a true RNN can do these, an SSM cannot. Title: "The Illusion of State in State-Space Models," Merrill, Petty, Sabharwal. arXiv:2404.08819, submitted 12 Apr 2024 (ICML 2024).
Paraphrase:  SSMs are marketed as addressing the Transformer's inability to do sequential state tracking, by analogy to RNNs. But their expressive power is limited very similarly to Transformers: they cannot express computation outside TC0, so they cannot solve permutation composition and related state-tracking tasks. Experiments show Mamba-style SSMs indeed struggle with state tracking. The "state" is in this sense an illusion.
Locators:    Abstract; the TC0 result and permutation-composition (S5) corollary; the Mamba state-tracking experiments.
Quote:       "the expressive power of SSMs is limited very similarly to transformers: SSMs cannot express computation outside the complexity class TC0. In particular, this means they cannot solve simple state-tracking problems like permutation composition."
```

```text
URL:         https://arxiv.org/abs/2312.04927
Kind:        primary — the Zoology study; the authors own the 17 pretrained models and the MQAR analysis. Context source, not a test of Mamba itself.
Establishes: That the quality gap between attention-free efficient models and attention is largely a recall gap: across a suite of gated-convolution and attention models, 82% of the Pile perplexity gap is explained by associative recall, and attention is far more parameter-efficient at it (a 70M attention model beats a 1.4B gated-convolution model on associative recall). Frames the recall-vs-efficiency tradeoff Mamba sits inside. NOTE for the writer: the tested efficient models are gated-convolution SSM-family models that predate Mamba's selection mechanism, so this establishes the framing, not a measurement of Mamba. Title: "Zoology: Measuring and Improving Recall in Efficient Language Models," Arora et al. arXiv:2312.04927, submitted 8 Dec 2023 (one week after Mamba's v1).
Paraphrase:  Attention-free gating+convolution models still trail attention by up to 2.1 perplexity on the Pile; 82% of that gap is associative recall (retrieving in-context information). Attention is dramatically more parameter-efficient at recall. The authors formalize multi-query associative recall (MQAR) and show input-dependent sparse-attention hybrids close 97.4% of the gap while staying sub-quadratic.
Locators:    Abstract; the 82%/2.1-ppl decomposition; the 70M-vs-1.4B associative-recall comparison; MQAR; the hybrid result.
Quote:       "82% of the gap is explained by each model's ability to recall information that is previously mentioned in-context... a 70M parameter attention model outperforms a 1.4 billion parameter gated-convolution model on associative recall."
```

```text
URL:         https://arxiv.org/abs/2111.00396
Kind:        primary — the S4 paper; the predecessor Mamba departs from. Gu, Goel, Ré own it.
Establishes: What "time-invariant" means and why it matters. S4's A, B, C are fixed across the sequence (linear time-invariant), which is exactly the property that permits the global-convolution computation Mamba gives up when it makes the parameters input-dependent. S4's A uses the HiPPO normal-plus-low-rank structure for long-range memory. Title: "Efficiently Modeling Long Sequences with Structured State Spaces," Gu, Goel, Ré. arXiv:2111.00396, submitted 31 Oct 2021 (ICLR 2022, outstanding-paper honorable mention).
Paraphrase:  S4 is a structured SSM whose parameters are constant over time, computed efficiently as a convolution via a low-rank correction to A (Cauchy-kernel evaluation), with the HiPPO structure supplying principled long-range memory. It solves Path-X (length 16k) and leads the Long Range Arena.
Locators:    Abstract; the LTI/convolution property; the normal-plus-low-rank (HiPPO) parameterization of A.
Quote:       (paraphrase sufficient; the load-bearing fact is that S4's parameters are fixed across the sequence, enabling the convolution.)
```

## Contradictions

- Mamba's induction-head result (Fig. 5) shows perfect generalization on an
  associative-recall task to million-length sequences, while Jelassi et al.
  (2402.01032) and Waleffe et al. (2406.07887) report that Mamba fails at copying
  and recall from long context. These are not in conflict once the tasks are
  distinguished. Induction heads is a single associative lookup (retrieve the one
  token that followed a prior occurrence of the cue), which a bounded state can do.
  Verbatim copying and multi-key recall (Phonebook) require holding many items in
  the fixed-size state at once, which the bounded-state argument says it cannot.
  The writer should not present Fig. 5 as evidence Mamba matches attention on
  recall in general; it settles the narrow selective-retrieval ability, not bulk
  memory.

- The paper frames selective SSMs as recurrent and RNN-like, implying the
  state-tracking strengths of RNNs. Merrill et al. (2404.08819) contradict that
  implication directly: SSMs are TC0 and provably cannot do permutation-composition
  state tracking that a true RNN can. This qualifies the "recurrence buys you RNN
  expressivity" reading, not the efficiency or the language-modeling parity.

- The throughput multiple is stated two ways in the paper itself: the abstract
  says "5x higher throughput than Transformers"; §4.5 says "4-5x." Report the
  range, and anchor it to the stated condition (recurrent inference with no
  KV cache, allowing larger batch sizes), not as a single headline number.

- Zoology (2312.04927) reports gated-convolution models lag attention by up to
  2.1 Pile perplexity with 82% of the gap being recall; Mamba's Table 1 shows
  Mamba-2.8B beating Pythia-2.8B on Pile perplexity. No direct contradiction:
  Zoology tested pre-Mamba gated-convolution models, and Mamba's selection is in
  part a response to the recall problem Zoology names. The recall gap reopens at
  larger scale and on harder recall tasks per the NVIDIA study.

## Numbers

```text
Figure: Selective copying accuracy — S4 layer, no gate: 18.3%
Owner:  Mamba paper, Fig. 4 (§4.1.1)
Scope:  Synthetic selective-copying task; accuracy over the copied tokens. Baseline showing a time-invariant SSM cannot do content-based selection.
```
```text
Figure: Selective copying accuracy — S6 (selective) layer, no gate: 97.0%; H3+S6: 99.7%; Mamba+S6: 99.8%
Owner:  Mamba paper, Fig. 4 (§4.1.1)
Scope:  Same task. Architecture gating alone (S4 layer) reaches only ~56–57% (H3+S4 57.0%, Mamba+S4 56.4%); the jump to ~97–99.8% comes from the S6 selection layer, not the surrounding block. This is the ablation that isolates selection as the cause.
```
```text
Figure: Induction-head length generalization — trained at length 2^8 = 256; solves the task up to 2^20 = 1,048,576
Owner:  Mamba paper, Fig. 5 (§4.1.2)
Scope:  Synthetic induction-heads (associative recall). Mamba extrapolates ~4000x beyond training length; the paper states no other tested method goes beyond ~2x. Attention baselines tested only to 2^14 = 16,384.
```
```text
Figure: Language-modeling scaling — models ~125M to ~1.3B params, Chinchilla protocol, trained on the Pile
Owner:  Mamba paper, Fig. 6 (§4.2.1)
Scope:  Perplexity vs compute. Mamba is the first attention-free model to match the Transformer++ recipe, and the gap to Transformer++ widens in Mamba's favor as sequence length grows. Beats H3, Hyena, RWKV, RetNet at equal size.
```
```text
Figure: Zero-shot downstream — Mamba-2.8B average accuracy 63.3% vs Pythia-2.8B 59.1%; Pile ppl 6.22 vs 6.73; LAMBADA acc 69.2% vs 64.7%
Owner:  Mamba paper, Table 1 (§4.2.2)
Scope:  Six zero-shot common-sense/QA tasks (LAMBADA, HellaSwag, PIQA, ARC-e, ARC-c, WinoGrande) plus Pile/LAMBADA perplexity. Baselines trained up to 300B tokens with various tokenizers. Paper's claim: Mamba matches baselines at roughly twice its size. (GPT-Neo/other rows read less cleanly from the HTML and are not relied on here; confirm any specific comparator at asset time.)
```
```text
Figure: Efficiency — selective scan faster than FlashAttention-2 beyond sequence length ~2K, and up to 20–40x faster than a standard scan implementation; ~40x faster than a standard scan overall (Fig. 12 left)
Owner:  Mamba paper, Fig. 12 (§4.5)
Scope:  Training-time scan microbenchmark on A100. The crossover point (~2K) is the load-bearing fact: below it attention is competitive, above it the scan wins.
```
```text
Figure: Inference throughput — 4–5x higher than a Transformer of similar size (abstract says 5x)
Owner:  Mamba paper, Fig. 12 right and §4.5
Scope:  Recurrent-mode generation; the advantage comes from having no KV cache, which allows much larger batch sizes. Report as a range with its condition.
```
```text
Figure: Mamba-2 core layer 2–8x faster than Mamba-1's selective SSM
Owner:  Mamba-2 paper (2405.21060), abstract
Scope:  Same-family speedup from the SSD-informed layer with a larger state dimension; competitive with Transformers on language modeling.
```
```text
Figure: NVIDIA hybrid — 43% Mamba-2 / 7% attention / 50% MLP; exceeds the 8B Transformer on all 12 standard tasks (+2.65 avg), ~8x projected inference speedup
Owner:  Waleffe et al. (2406.07887), abstract
Scope:  8B params, 3.5T tokens. The 7% attention figure is the load-bearing number: a small slice of attention is what closes the recall/ICL gap.
```
```text
Figure: Zoology recall gap — up to 2.1 Pile perplexity between gated-convolution and attention; 82% of it is associative recall; a 70M attention model beats a 1.4B gated-convolution model on recall
Owner:  Arora et al. (2312.04927), abstract
Scope:  Suite of 17 pretrained models (pre-Mamba efficient architectures). Context for the recall framing, not a Mamba measurement.
```

## Source assets

```text
Asset: Figure 5 (Induction Heads) — accuracy vs test sequence length, in the Mamba paper (§4.1.2). Lives in §4.1.
Shows: Mamba holds ~perfect accuracy from length 64 out to 2^20 = 1,048,576 while attention and other baselines collapse past roughly 2x their training length of 256. Settles the narrow claim: selection gives Mamba a length-robust selective-retrieval ability the time-invariant and attention baselines lack.
Crop:  Retain the full x-axis through 2^20 and the training-length marker at 2^8 = 256; retain the legend distinguishing Mamba from the baselines. Do not crop to only the region where all models succeed — the extrapolation past 256 is the point. Pair the caption with the copying/recall qualification so the reader does not over-read it as general recall.
```
```text
Asset: Figure 4 (Selective Copying) — the accuracy table over architecture x layer, Mamba paper §4.1.1.
Shows: The ablation that isolates the selection mechanism: swapping the inner layer from S4 to S6 moves accuracy from ~18–57% to ~97–99.8%, while changing only the surrounding architecture (adding a gate) does not. Settles that selection, not the block design, is the source of the content-based-reasoning ability.
Crop:  Keep all rows so the S4-vs-S6 contrast within each architecture is visible; keep the column headers (Architecture, Layer, Accuracy). A crop that drops the S4 rows destroys the ablation.
```
```text
Asset: Figure 6 (Scaling Laws) — perplexity-vs-compute curves, Mamba paper §4.2.1.
Shows: Mamba's curve tracking or beating Transformer++ and sitting below every other attention-free baseline (H3, Hyena, RWKV, RetNet). Settles the headline language-modeling parity claim at 125M–1.3B scale under the Chinchilla protocol.
Crop:  Retain the Transformer++ curve and the axis labels (params/compute vs perplexity) and the note that these are Pile-trained Chinchilla-protocol runs; retain enough of the legend to distinguish Transformer++ from the attention-free lines. If the figure has multiple sequence-length panels, keep the panel the article's argument cites and label the length.
```
```text
Asset: Figure 12 (Efficiency Benchmarks) — left: scan speed vs sequence length against FlashAttention-2 and a standard scan; right: inference throughput vs batch size, Mamba paper §4.5.
Shows: Left settles the "the scan makes selectivity practical" claim — the fused selective scan overtakes FlashAttention-2 beyond ~2K length and is 20–40x over a naive scan. Right settles the throughput claim — 4–5x over a similar-size Transformer, driven by no KV cache.
Crop:  Left panel must retain the crossover point (~2K) and both comparison curves (FlashAttention-2 and standard scan); do not crop out the sub-2K region where attention is competitive, since honesty about the crossover is the point. Right panel must retain the batch-size axis, since the throughput gain depends on it.
```
```text
Asset: Figure 3 (Architecture) — the Mamba block diagram, Mamba paper §3.4.
Shows: How the selective SSM sits inside a single homogeneous block that fuses the H3-style SSM path with a gated-MLP branch (SiLU/SwiGLU-style gating, expansion factor E=2), with no separate attention or MLP block. Useful if the reconstruction needs to show where the S6 layer lives in the network.
Crop:  Keep the two branches and the gate; label the SSM path. Optional — include only if the article reconstructs the block rather than just the layer.
```

No decorative or generated figures are proposed. Charts the article builds itself
(e.g. re-plotting the scaling or throughput series) are the writer's call under
spec/charts.md and are not source assets.

## Discarded

```text
URL: https://arxiv.org/abs/2312.00752 v1 — not discarded, but the v1/v2 distinction matters: v2 (31 May 2024) is the version read and cited. If a figure number must be exact, confirm against v2, since arXiv HTML rendering of v1 can differ.
URL: GPT-Neo-2.7B row of Table 1 — the automated read returned an implausible LAMBADA perplexity (62.2) for GPT-Neo, likely a column misalignment in the HTML-to-text conversion. Rejected as unreliable; do not cite GPT-Neo perplexity without a pixel-level re-read. The Mamba-vs-Pythia comparison is clean and sufficient for the parity claim.
```
