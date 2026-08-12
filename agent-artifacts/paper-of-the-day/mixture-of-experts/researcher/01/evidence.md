# Evidence: paper-of-the-day/mixture-of-experts (01)

The record supports the commissioned reconstruction firsthand. The 2017 paper's
own text gives the softmax gate, the noisy top-k gate, both auxiliary losses
(importance in the body, load in Appendix A), the shrinking-batch problem and its
parallelism fix, and the headline numbers with their scope, plus the exact figures
and tables the writer needs as source assets. The follow-on record is established
from each owning paper: Switch (top-1), GShard (top-2), expert-choice routing, the
loss-free bias controller, and DeepSeekMoE/V3. It confirms rather than undermines
the commissioned angle: sparse top-k routing survived, and the specific balancing
machinery (the two 2017 losses, and later the loss-based approach itself) was
largely replaced. It is thin in three places, each recorded below: the DeepSeek-V3
technical detail is read only to the abstract's claims; the 2017 parameter counts
appear at two scopes (Table 1 excludes embeddings, the appendix totals include
them) that must not be conflated; and the ">1000x capacity" line is the abstract's
ceiling framing, not one controlled measurement, so the writer must anchor it to
the compute-matched comparison rather than repeat it bare.

## Sources

```text
URL:         https://arxiv.org/abs/1701.06538
Kind:        primary. It is the paper under reconstruction; Shazeer et al. own
             every claim about the MoE layer, the gating, the losses, and the
             experiments.
Establishes: Title "Outrageously Large Neural Networks: The Sparsely-Gated
             Mixture-of-Experts Layer." Authors: Noam Shazeer, Azalia Mirhoseini,
             Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean.
             arXiv:1701.06538 [cs.LG], submitted 23 Jan 2017; accepted ICLR 2017.
             The mechanism, the two losses, the shrinking-batch fix, and the LM
             and translation results.
Paraphrase:  A trainable gating network picks a sparse combination of up to
             thousands of feed-forward expert sub-networks per example, applied
             convolutionally between stacked LSTM layers. The abstract claims
             greater than 1000x model capacity at minor computational cost, with
             MoE layers up to 137 billion parameters, beating state of the art on
             language modeling and translation at lower compute.
Locators:    Abstract; Sections 2, 3, 4, 5; Appendix A (load loss); Appendix C
             (model detail). Equations and tables located per line below.
Quote:       Abstract, verbatim: "The capacity of a neural network to absorb
             information is limited by its number of parameters. Conditional
             computation, where parts of the network are active on a per-example
             basis, has been proposed in theory as a way of dramatically
             increasing model capacity without a proportional increase in
             computation. In practice, however, there are significant algorithmic
             and performance challenges. In this work, we address these challenges
             and finally realize the promise of conditional computation, achieving
             greater than 1000x improvements in model capacity with only minor
             losses in computational efficiency on modern GPU clusters. We
             introduce a Sparsely-Gated Mixture-of-Experts layer (MoE), consisting
             of up to thousands of feed-forward sub-networks. A trainable gating
             network determines a sparse combination of these experts to use for
             each example. We apply the MoE to the tasks of language modeling and
             machine translation, where model capacity is critical for absorbing
             the vast quantities of knowledge available in the training corpora.
             We present model architectures in which a MoE with up to 137 billion
             parameters is applied convolutionally between stacked LSTM layers. On
             large language modeling and machine translation benchmarks, these
             models achieve significantly better results than state-of-the-art at
             lower computational cost."
```

The full-text HTML used to read the equations, appendices, figures, and tables of
the above paper is the ar5iv rendering; recorded so the writer can reopen the
exact passages. The canonical source page is the arXiv entry above.

```text
URL:         https://ar5iv.labs.arxiv.org/html/1701.06538
Kind:        primary (same paper, HTML rendering of the arXiv source).
Establishes: The gating math, both loss definitions, the shrinking-batch fix, and
             the table/figure numbers, read into body and appendices.
Paraphrase:  Softmax gate (Eq. 2): G_sigma(x) = Softmax(x . W_g). Noisy top-k gate
             (Eqs. 3-5): G(x) = Softmax(KeepTopK(H(x), k));
             H(x)_i = (x . W_g)_i + StandardNormal() . Softplus((x . W_noise)_i);
             KeepTopK keeps the k largest entries and sets the rest to -infinity so
             their softmax weight is zero. Importance loss (Sec. 4):
             Importance(X) = sum over the batch of G(x), and
             L_importance(X) = w_importance . CV(Importance(X))^2, where CV is the
             coefficient of variation. Load loss (Appendix A): a smooth estimator
             P(x,i) = Phi( ((x . W_g)_i - kth_excluding(H(x), k, i)) /
             Softplus((x . W_noise)_i) ), the probability expert i is chosen given
             a fresh noise draw; Load(X)_i = sum over the batch of P(x,i);
             L_load(X) = w_load . CV(Load(X))^2. Shrinking batch (Sec. 3.1): with k
             of n experts chosen, each expert sees about kb/n of a batch of b;
             mixing data and model parallelism across d devices raises this to
             about kbd/n, and applying the MoE convolutionally over LSTM timesteps
             further enlarges the per-expert batch.
Locators:    Sec. 2.1 (Eqs. 2-5); Sec. 3.1 (batch shrinking); Sec. 4 (Eqs. 6-7,
             importance); Appendix A (Eqs. 9-11, load); Sec. 5 and Appendix C
             (results).
Quote:       Eq. 4, verbatim: "H(x)_i = (x . W_g)_i + StandardNormal() .
             Softplus((x . W_noise)_i)". Sec. 5.1, verbatim: "Even the fastest of
             these models beats the best published result (when controlling for
             the number of training epochs), despite requiring only 6% of the
             computation." Why two losses: importance equalizes the summed gate
             weight per expert but leaves the number of examples per expert free,
             so a separate load term is needed; the paper motivates the load loss
             precisely because importance alone does not balance example counts.
```

```text
URL:         https://arxiv.org/abs/2101.03961
Kind:        primary. Fedus, Zoph, Shazeer own the Switch Transformer design and
             its claim that top-1 routing suffices.
Establishes: Title "Switch Transformers: Scaling to Trillion Parameter Models with
             Simple and Efficient Sparsity." Authors: William Fedus, Barret Zoph,
             Noam Shazeer. arXiv:2101.03961, submitted 11 Jan 2021; published JMLR
             (2022). Routes each token to a single expert (k=1); a single
             differentiable load-balancing loss; expert capacity with a capacity
             factor and token dropping; trillion-parameter scale.
Paraphrase:  Switch routes each token to one expert, contradicting the 2017
             conjecture that k>1 was needed for usable router gradients, and
             reports this both preserves quality and performs better while cutting
             routing and communication cost. Its load loss is
             loss = alpha . N . sum_i f_i . P_i, where f_i is the fraction of
             tokens dispatched to expert i, P_i the fraction of router probability
             mass on expert i, N the number of experts, and alpha = 1e-2. Expert
             capacity = (tokens per batch / number of experts) . capacity factor;
             tokens beyond capacity are dropped (typically under 1%). Switch-C
             reaches 1.571 trillion parameters with 2048 experts and gives a 4x
             pre-training speedup over T5-XXL; Switch-Base reaches T5-Base quality
             about 7x sooner in step time.
Locators:    Sec. 2.1 (single-expert routing, and the reference to Shazeer et al.
             2017's k>1 conjecture); Sec. 2.2 (Eqs. 3-6, capacity and load loss,
             alpha value); Sec. 5.6 and Table 9 (Switch-C scale, 4x over T5-XXL).
Quote:       Sec. 2.1, verbatim: "we instead use a simplified strategy where we
             route to only a single expert." On the prior conjecture, Sec. 2.1
             attributes to Shazeer et al. (2017) the claim that "routing to k>1
             experts was necessary in order to have non-trivial gradients to the
             routing functions," which Switch reports it overturns.
```

```text
URL:         https://arxiv.org/abs/2006.16668
Kind:        primary. Lepikhin et al. own the GShard top-2 design and the 600B
             translation result.
Establishes: Title "GShard: Scaling Giant Models with Conditional Computation and
             Automatic Sharding." Authors: Dmitry Lepikhin, HyoukJoong Lee,
             Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun,
             Noam Shazeer, Zhifeng Chen. arXiv:2006.16668, June 2020. Group-level
             top-2 gating, an auxiliary load loss, randomized second-expert
             dispatch, and enforced expert capacity.
Paraphrase:  Each token is dispatched to at most two experts. A local group splits
             the batch and enforces per-expert capacity; the second expert is taken
             with probability proportional to its gate weight. The auxiliary loss
             is l_aux = (1/E) sum_e (c_e / S) . m_e, where c_e/S is the fraction of
             tokens routed to expert e and m_e the mean gate value for e, used as a
             differentiable stand-in for the non-differentiable count. Scaled a
             multilingual translation Transformer past 600 billion parameters with
             2048 experts per MoE layer, translating 100 languages into English,
             for an average +13.5 BLEU over bilingual baselines, trained on 2048
             TPU v3 cores in 4 days (22 TPU v3 core-years).
Locators:    Sec. 2.2 (top-2 gating, random second expert, capacity, Algorithm 1
             line 19 for l_aux); Sec. 4.3 and Figure 6 (600B, 100 languages, BLEU);
             Figure 1 caption (training cost).
Quote:       Auxiliary loss, verbatim: "l_aux = (1/E) sum_{e=1}^{E} (c_e / S) .
             m_e". On routing width, Sec. 2.2: each token is "dispatched to at most
             two experts."
```

```text
URL:         https://arxiv.org/abs/2202.09368
Kind:        primary. Zhou et al. own the expert-choice routing method and its
             load-balance-by-construction claim.
Establishes: Title "Mixture-of-Experts with Expert Choice Routing." Authors: Yanqi
             Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao,
             Andrew Dai, Zhifeng Chen, Quoc Le, James Laudon. NeurIPS 2022. Experts
             select their top-k tokens instead of tokens selecting top-k experts,
             giving each expert a fixed bucket and a variable number of experts per
             token, and removing the need for an auxiliary load-balancing loss.
Paraphrase:  Token-choice top-k routing can leave experts under- or over-loaded;
             expert-choice inverts the direction so every expert fills a fixed
             bucket, making load uniform by construction and dropping the auxiliary
             balancing loss. Reports better than 2x faster training convergence at
             equal compute versus Switch top-1 and GShard top-2, and beats dense T5
             on 7 of 11 GLUE/SuperGLUE tasks at lower activation cost.
Locators:    Abstract; method section on the top-k token selection per expert.
Quote:       Abstract, verbatim: "Instead of letting tokens select the top-k
             experts, we have experts selecting the top-k tokens. As a result, each
             token can be routed to a variable number of experts and each expert
             can have a fixed bucket size." And: "improves training convergence
             time by more than 2x."
```

```text
URL:         https://arxiv.org/abs/2408.15664
Kind:        primary. Wang et al. own the Loss-Free Balancing method and the claim
             that the auxiliary loss itself degrades the model.
Establishes: Title "Auxiliary-Loss-Free Load Balancing Strategy for
             Mixture-of-Experts." Authors: Lean Wang, Huazuo Gao, Chenggang Zhao,
             Xu Sun, Damai Dai (DeepSeek). Submitted 28 Aug 2024. A per-expert bias
             added to routing scores before top-K, updated by recent load, replaces
             the auxiliary loss and its interference gradients.
Paraphrase:  An auxiliary balancing loss large enough to balance load injects
             interference gradients that hurt the primary objective. Loss-Free
             Balancing adds an expert-wise bias to each expert's routing score
             before the top-K decision and nudges that bias up or down by the
             expert's recent load, holding load balanced without any balancing-loss
             gradient. Validated on MoE models up to 3B parameters trained on up to
             200B tokens, reporting both better perplexity and better load balance
             than auxiliary-loss control.
Locators:    Abstract; method section (bias applied before top-K, dynamic update
             rule); experiments (up to 3B params, 200B tokens).
Quote:       Abstract, verbatim: "a large auxiliary loss will introduce
             non-negligible interference gradients into training and thus impair
             the model performance." And: "before the top-K routing decision,
             Loss-Free Balancing will first apply an expert-wise bias to the
             routing scores of each expert."
```

```text
URL:         https://arxiv.org/abs/2401.06066
Kind:        primary. Dai et al. own the DeepSeekMoE architecture and its
             specialization results.
Establishes: Title "DeepSeekMoE: Towards Ultimate Expert Specialization in
             Mixture-of-Experts Language Models." First author Damai Dai (DeepSeek).
             Submitted 11 Jan 2024. Two structural changes to top-k MoE:
             fine-grained expert segmentation and shared-expert isolation; it still
             uses expert-level and device-level auxiliary balancing losses.
Paraphrase:  Segments N experts into mN finer experts and activates mK of them for
             more flexible combinations, and reserves Ks always-active shared
             experts for common knowledge so routed experts specialize. Reports 2B
             matching GShard 2.9B with 1.5x fewer expert parameters, 16B matching
             LLaMA2 7B at about 40% of the compute, and 145B matching DeepSeek 67B
             at roughly 28.5% of its compute.
Locators:    Abstract (the two strategies); architecture section (segmentation and
             shared experts, auxiliary losses retained); results (2B, 16B, 145B).
Quote:       Abstract, verbatim: "(1) finely segmenting the experts into mN ones
             and activating mK from them, allowing for a more flexible combination
             of activated experts; (2) isolating Ks experts as shared ones, aiming
             at capturing common knowledge and mitigating redundancy in routed
             experts."
```

```text
URL:         https://arxiv.org/abs/2412.19437
Kind:        primary (production technical report). DeepSeek-AI owns DeepSeek-V3 and
             its stated balancing strategy at scale.
Establishes: Title "DeepSeek-V3 Technical Report." Author: DeepSeek-AI (200+ named
             contributors). Submitted 27 Dec 2024. A 671B-total-parameter MoE with
             37B activated per token that uses an auxiliary-loss-free balancing
             strategy at production scale.
Paraphrase:  A frontier open-weight MoE of 671B total parameters, 37B active per
             token, whose abstract states it pioneers an auxiliary-loss-free load
             balancing strategy. It is the production evidence that the loss-based
             balancing of 2017 was displaced at frontier scale by the bias
             controller.
Locators:    Abstract (parameter counts; auxiliary-loss-free strategy). Deeper
             configuration (expert counts, sequence-wise complementary loss, no
             token dropping) not read beyond the abstract; see Contradictions/thin.
Quote:       Abstract, verbatim: "671B total parameters with 37B activated for each
             token" and it "pioneers an auxiliary-loss-free strategy for load
             balancing."
```

```text
URL:         https://arxiv.org/abs/1308.3432
Kind:        primary. Bengio, Leonard, Courville own the conditional-computation
             gradient-estimator survey the 2017 paper builds on.
Establishes: Title "Estimating or Propagating Gradients Through Stochastic Neurons
             for Conditional Computation." Authors: Yoshua Bengio, Nicholas
             Leonard, Aaron Courville. Submitted 15 Aug 2013. Estimators for
             gradients through stochastic/hard-threshold gating units, including the
             straight-through estimator, motivated by conditional computation.
Paraphrase:  Frames conditional computation as sparse stochastic gating units that
             switch off large parts of a network, and studies four ways to get
             gradients through such non-differentiable gates (REINFORCE-based
             unbiased estimator, a decomposition, injected noise, and the
             straight-through estimator). This is the difficulty the 2017 paper's
             noisy top-k gate works around with a smooth load estimator rather than
             a straight-through gradient.
Locators:    Abstract and the enumeration of the four estimators.
Quote:       Abstract, verbatim: sparse stochastic units "form a distributed
             representation of gaters that can turn off in combinatorially many
             ways large chunks of the computation."
```

```text
URL:         https://direct.mit.edu/neco/article/3/1/79/5560/Adaptive-Mixtures-of-Local-Experts
Kind:        primary. Jacobs, Jordan, Nowlan, Hinton own the original mixture-of-
             experts formulation the 2017 paper revives; Hinton is an author of
             both.
Establishes: Title "Adaptive Mixtures of Local Experts." Authors: Robert A. Jacobs,
             Michael I. Jordan, Steven J. Nowlan, Geoffrey E. Hinton. Neural
             Computation 3(1):79-87, 1991. The origin of expert networks plus a
             gating network trained so experts specialize on subsets of cases.
Paraphrase:  Introduces a system of separate expert networks and a gating network
             that learns which expert handles which cases, so experts specialize
             rather than interfere. The 2017 layer is this idea scaled with sparse
             top-k gating.
Locators:    Neural Computation vol. 3, issue 1, pp. 79-87 (1991).
Quote:       None retrieved. The MIT Press page returns HTTP 403 to automated
             fetch; it is gated, not dead, and is the article's own canonical page.
             Bibliographic detail confirmed via the publisher listing.
```

## Contradictions

- The 2017 paper conjectured k>1 experts were needed for non-trivial router
  gradients. Switch Transformer routes to k=1 and reports it preserves quality and
  performs better (Switch Sec. 2.1). This is a direct overturning of a stated
  premise of the original design.
- The 2017 paper balances load with two coefficient-of-variation losses (importance
  and load). GShard and Switch collapse balancing into a single differentiable
  load loss (GShard l_aux; Switch loss = alpha.N.sum f_i.P_i). The two-loss design
  did not survive even in work that kept a balancing loss.
- Expert-choice routing (Zhou et al.) and Loss-Free Balancing (Wang et al.) both
  discard the auxiliary balancing loss entirely, by inverting routing and by a bias
  controller respectively. Wang et al. argue the balancing loss actively harms the
  model through interference gradients. This qualifies the 2017 claim that an
  auxiliary balancing loss is the way to make the layer trainable: the balancing
  goal held, the loss-based means did not.
- The 2017 shrinking-batch fix is mixed data-and-model parallelism plus convolution
  over timesteps to enlarge the per-expert batch (Sec. 3.1). GShard and Switch
  instead cap each expert with a fixed capacity and drop overflow tokens. Same
  throughput problem, different solution; the writer should not present the 2017
  fix as the one the field adopted.
- Expert-choice routing's guarantee that experts fill fixed buckets requires seeing
  a batch/sequence of tokens together, which sits awkwardly with autoregressive
  decoding. The record does not source a decoder-side limitation from the paper
  read to abstract and method summary only; flagged as unverified rather than
  asserted.

## Numbers

```text
Figure: greater than 1000x
Owner:  Shazeer et al. 2017, abstract
Scope:  Model capacity (parameter count) relative to a dense network of comparable
        per-example compute; the abstract's framing, not a single controlled row.
        Anchor it to the compute-matched comparison below, not repeated bare.
```

```text
Figure: 137 billion parameters (largest MoE layer built)
Owner:  Shazeer et al. 2017, Sec. 5.2 / Appendix table (MoE-131072-h)
Scope:  131,072 hierarchical experts, 137.7B total params, 9.7M ops/timestep,
        28.9-29.2 test perplexity, trained on the 100-billion-word Google News
        corpus. Companion MoE-65536-h: 68.9B params, 9.2M ops/timestep.
```

```text
Figure: 4.3-4.4 billion parameters (1B-word benchmark models)
Owner:  Shazeer et al. 2017, Table 1
Scope:  Parameters excluding embedding/softmax, for the flat/hierarchical MoEs (up
        to 4096 experts, each about 1M params) on the 1 Billion Word LM benchmark.
        The appendix quotes total counts including embeddings near 5-6B for the
        same models; do not conflate the two scopes.
```

```text
Figure: 28.0 test perplexity (best MoE, 1B-word benchmark)
Owner:  Shazeer et al. 2017, Table 1
Scope:  High-compute MoE, 142.7M ops/timestep, 47 hours on 32 K40 GPUs; the run at
        10 training epochs. Best previously published: 34.7 (10 epochs) at 151M
        params and 151M ops/timestep; 30.6 at 100 epochs.
```

```text
Figure: 6% of the computation
Owner:  Shazeer et al. 2017, Sec. 5.1
Scope:  The fastest MoE (8.9M ops/timestep, 34.1 perplexity) beats the best
        published 10-epoch result while using about 6% of that baseline's
        computation (151M ops/timestep). This is the concrete compute-matched claim
        behind the capacity headline.
```

```text
Figure: BLEU 40.56, +1.34 over baseline (WMT'14 En->Fr)
Owner:  Shazeer et al. 2017, Table 2
Scope:  MoE with 2048 experts, 8.7B params, 85M ops/timestep, longer training, on
        newstest2014; GNMT baseline 39.22 (perplexity 2.63 MoE vs 2.79 baseline).
        Shorter-training MoE: BLEU 40.35, perplexity 2.69.
```

```text
Figure: BLEU 26.03 vs 24.91 (WMT'14 En->De)
Owner:  Shazeer et al. 2017, Table 3
Scope:  MoE 2048 experts on newstest2014, perplexity 4.64; GNMT baseline BLEU
        24.91, perplexity 5.25.
```

```text
Figure: 8 of 12 language pairs improved (multilingual translation)
Owner:  Shazeer et al. 2017, Sec. 5.3
Scope:  A single multilingual MoE, 8.7B params, 102M ops/timestep, outperformed the
        monolingual GNMT baselines on 8 of 12 pairs.
```

```text
Figure: 1.571 trillion parameters, 4x speedup over T5-XXL
Owner:  Fedus et al. 2021, Sec. 5.6 / Table 9
Scope:  Switch-C, 2048 experts, top-1 routing; pre-training speedup over a tuned
        T5-XXL baseline. Switch-Base reaches T5-Base quality about 7x sooner in
        step time.
```

```text
Figure: >600 billion parameters, +13.5 average BLEU
Owner:  Lepikhin et al. 2020, Sec. 4.3 / Figure 6
Scope:  MoE(2048E, 36L) multilingual model, 100 languages into English, versus
        bilingual baselines; trained on 2048 TPU v3 cores for 4 days (22 core-yrs).
```

```text
Figure: >2x faster training convergence
Owner:  Zhou et al. 2022, abstract
Scope:  Expert-choice routing versus Switch top-1 and GShard top-2 at equal
        compute; beats dense T5 on 7 of 11 GLUE/SuperGLUE tasks at lower
        activation cost.
```

```text
Figure: 671B total / 37B activated per token
Owner:  DeepSeek-AI 2024 (DeepSeek-V3), abstract
Scope:  Production MoE using an auxiliary-loss-free balancing strategy; per-token
        active parameters are 37B of 671B total.
```

```text
Figure: alpha = 1e-2 (Switch load-loss coefficient)
Owner:  Fedus et al. 2021, Sec. 2.2
Scope:  Weight on the single differentiable load-balancing loss loss = alpha . N .
        sum_i f_i . P_i; large enough to balance load, small enough not to
        dominate cross-entropy.
```

## Source assets

```text
Asset: Figure 1, Shazeer et al. 2017 - the MoE layer schematic embedded in the
       recurrent language model, with the gating network selecting two experts.
Shows: How a single input is routed through the gate to a sparse subset of experts
       and recombined; the one picture the reconstruction of the gate turns on.
Crop:  Must retain the gating network, the full expert row (with the unselected
       experts visibly inactive), and the weighted combination back into the
       sequence. Do not crop away the -infinity/zeroed experts, which are the point.
```

```text
Asset: Figure 2, Shazeer et al. 2017 - two plots on the 1 Billion Word benchmark:
       (left) test perplexity vs model capacity (number of parameters) at a fixed
       ~8M ops/timestep budget; (right) test perplexity vs computational budget
       (ops/timestep).
Shows: That added capacity lowers perplexity while per-example compute is held
       fixed - the empirical core of the "capacity is nearly free" claim.
Crop:  Must keep both axis labels and the units (parameters; ops/timestep) and the
       baseline point for comparison. Note the axis scaling in the caption if it is
       non-linear.
```

```text
Asset: Table 1, Shazeer et al. 2017 - 1 Billion Word LM results: MoE models vs best
       published, with perplexity, parameters, ops/timestep, and training
       time/hardware per row.
Shows: The 34.7 -> 28.0 perplexity move and the 6%-compute row in one place, at the
       correct parameter scope (excluding embeddings).
Crop:  Keep the baseline row and at least the fastest and best MoE rows together;
       keep the ops/timestep column, which carries the compute-matched argument.
```

```text
Asset: Table 2, Shazeer et al. 2017 - WMT'14 En->Fr translation: MoE (2048 experts)
       vs GNMT, BLEU and perplexity.
Shows: The +1.34 BLEU headline with its baseline in view, so the gain is read
       against GNMT rather than in isolation.
Crop:  Keep the GNMT baseline row beside the MoE rows; keep both BLEU and
       perplexity columns.
```

```text
Asset: Equations 2-5, Shazeer et al. 2017 (Sec. 2.1) - softmax gate and noisy
       top-k gate.
Shows: The exact gate the reconstruction must set rather than paraphrase; the
       StandardNormal noise and KeepTopK are the mechanism.
Crop:  Set as display math, not prose. This is the passage the series prompt asks be
       set rather than described.
```

```text
Asset: Switch Transformer (Fedus et al. 2021) load-loss equation (Sec. 2.2) and
       GShard (Lepikhin et al. 2020) l_aux (Algorithm 1) - the successor losses.
Shows: How the two-loss 2017 design was reduced to one differentiable balancing
       term; useful set beside Eqs. 6-7 of the original.
Crop:  Set as display math with each symbol (f_i, P_i, c_e/S, m_e) named.
None found beyond these for the remaining follow-on papers read only to abstract
and method summary.
```

## Discarded

```text
URL: https://ar5iv.org/abs/1701.06538 - 301 redirect to ar5iv.labs.arxiv.org; the
     working render is recorded above, and the canonical page is the arXiv abstract.
```
