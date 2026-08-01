# Evidence record — paper-of-the-day/grokking (researcher, 01)

This record supports a clean phenomenon-vs-mechanism argument. The focal paper
(Power et al. 2022, arXiv:2201.02177) is read in full via its ar5iv HTML
rendering and its abstract page; it firmly establishes the grokking curve, the
modular-arithmetic task family (p=97, 12 binary operations), the weight-decay
and dataset-fraction dependence, and — importantly — that the authors
themselves offer no mechanism and flag this as future work (Section 4,
Appendix A.5). Nanda et al. 2023 (arXiv:2301.05217) is read in full via its
HTML rendering; it firmly establishes the Fourier/rotation algorithm, the
three-phase account, and the "progress measures" framework, on a narrower task
(one-layer transformer, modular addition only, p=113 — not p=97, and not the
41 other operations Power tested). Three further primary sources are read and
verified, each changing the interpretation of the 2022 result in a different
direction: Liu et al.'s two 2022 papers (effective theory / Goldilocks zone;
Omnigrok / LU mechanism) locate the cause in weight-norm geometry rather than
optimization steps per se, and generalize it off algorithmic data entirely;
Varma et al. 2023 relocates the cause in circuit efficiency and predicts two
new behaviors (ungrokking, semi-grokking); Prieto et al. 2025 relocates the
mechanism again, in floating-point Softmax Collapse, and argues weight decay's
real job is numerical, not the norm-shrinking job Omnigrok assigns it. This
gives the writer four non-redundant, mutually disagreeing causal accounts to
weigh against the original phenomenon, which is exactly the shape the
commission's angle needs.

**Thin spot, flagged for the writer/editor:** the focal paper's exact
publication venue could not be pinned down with confidence. See
Contradictions §1 below — do not print "ICLR 2022 Workshop" without
resolving this; the only primary trace found says ICLR 2021.

---

## Paper card (for the `abstract` section — paste verbatim)

**Title:** Grokking: Generalization Beyond Overfitting on Small Algorithmic
Datasets

**Authors:** Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin
(OpenAI); Vedant Misra (Google)

**Venue:** Workshop paper — exact conference/year unresolved, see
Contradictions §1. arXiv posting carries no Comments/Journal-ref field (I
checked the abstract page directly). Safest precise phrasing until resolved:
"presented as a workshop paper; posted to arXiv January 2022" — do not assert
a specific workshop/year without flagging the uncertainty, or resolve it
editorially before press.

**Year:** 2022 (arXiv v1 submitted 6 Jan 2022)

**Canonical link:** https://arxiv.org/abs/2201.02177

**Abstract (verbatim):**

> In this paper we propose to study generalization of neural networks on
> small algorithmically generated datasets. In this setting, questions about
> data efficiency, memorization, generalization, and speed of learning can be
> studied in great detail. In some situations we show that neural networks
> learn through a process of 'grokking' a pattern in the data, improving
> generalization performance from random chance level to perfect
> generalization, and that this improvement in generalization can happen well
> past the point of overfitting. We also study generalization as a function
> of dataset size and find that smaller datasets require increasing amounts
> of optimization for generalization. We argue that these datasets provide a
> fertile ground for studying a poorly understood aspect of deep learning:
> generalization of overparametrized neural networks beyond memorization of
> the finite training dataset.

---

## Sources

### 1. Power, Burda, Edwards, Babuschkin, Misra — "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets" (arXiv:2201.02177) — FOCAL PAPER

- **URL:** https://arxiv.org/abs/2201.02177 (abstract/metadata) and
  https://ar5iv.labs.arxiv.org/html/2201.02177 (full text, read in full — the
  arxiv.org/html/2201.02177 route 404s; ar5iv is the working mirror).
- **Classification:** Primary. The paper making every claim below is the
  paper that owns them.
- **Establishes firsthand:**
  - The term and phenomenon "grokking": training accuracy reaches near-perfect
    quickly while validation accuracy stays at chance for a long stretch,
    then rises to near-perfect. Exact definition, Section 3.1: "We show that,
    long after severely overfitting, validation accuracy sometimes suddenly
    begins to increase from chance level toward perfect generalization. We
    call this phenomenon 'grokking'."
  - Task family: 12 binary operations on **modulus p = 97**, evaluated as
    next-token prediction (Appendix A.1.1, "Binary operations"): x+y mod p;
    x−y mod p; x/y mod p; a piecewise x/y-or-x−y variant; x²+y² mod p;
    x²+xy+y² mod p; x²+xy+y²+x mod p; x³+xy mod p; x³+xy²+y mod p; and three
    permutation-composition operations on S₅ (x·y; x·y·x⁻¹; x·y·x).
  - Architecture: "a standard decoder-only transformer" with 2 layers, width
    128, 4 attention heads, ~4·10⁵ non-embedding parameters.
  - Optimizer: AdamW, learning rate 10⁻³, weight decay 1, β₁=0.9, β₂=0.98,
    linear LR warmup over the first 10 updates, minibatch 512 (or half the
    dataset, whichever is smaller), optimization budget 10⁵ gradient updates
    (extended to 5·10⁵ and 10⁶ in some runs).
  - The headline curve: Figure 1 (left panel), caption (verbatim, partial):
    "Grokking: A dramatic example of generalization far after overfitting on
    an algorithmic dataset. We train on the binary operation of division mod
    97 with 50% of the data in the training set." Body text, Section 3.1:
    training accuracy is "close to perfect at <10³ optimization steps," but
    "it takes close to 10⁶ steps for validation accuracy to reach that
    level," with "very little evidence of any generalization until 10⁵
    steps."
  - Weight decay's effect, Section 3.3 (ablations, Figure 2 left): "Adding
    weight decay has a very large effect on data efficiency, more than
    halving the amount of samples needed compared to most other
    interventions." Also: "weight decay towards the initialization of the
    network is also effective, but not quite as effective as weight decay
    towards the origin."
  - Dataset-fraction dependence, Section 3.1.1 ("Learning time curves"),
    Figure 1 (center): near the minimal viable dataset size, "a decrease of
    1% of training data leads to an increase of 40-50% in median time to
    generalization." Converged accuracy stays at 100% regardless; only the
    optimization time to reach it grows as the dataset shrinks. Steps to 99%
    train accuracy stay roughly in the 10³–10⁴ range regardless of dataset
    size, while steps to validation generalization do not.
  - The paper offers no mechanism and says so. Section 4 (Discussion): "We
    plan to test whether various proposed measures of minima flatness
    correlate with generalization in our setting" — a stated open question,
    not a finding. Appendix A.5: "This is suggestive that grokking may only
    happen after the network's parameters are in flatter regions of the loss
    landscape. It would be valuable for future work to explore this
    hypothesis." No mechanistic account is offered anywhere in the paper.
- **`data-nb-locator` suggestions:** `2201.02177#sec3.1` (grokking curve,
  definition); `2201.02177#fig1` (main curve); `2201.02177#sec3.1.1`
  (dataset-size/time curves); `2201.02177#sec3.3` (weight decay ablation,
  Fig. 2); `2201.02177#appA.1.1` (operation list); `2201.02177#sec4` and
  `2201.02177#appA.5` (unexplained-mechanism admission).

### 2. openai/grok — official code release for Power et al. 2022

- **URL:** https://github.com/openai/grok
- **Classification:** Primary. Same authoring team, the artifact the paper's
  results were produced with.
- **Establishes firsthand:** the repository is the code release for
  "Grokking: Generalization Beyond Overfitting on Small Algorithmic
  Datasets" by Power, Burda, Edwards, Babuschkin, Misra; contains
  `./scripts/train.py` and an `pip install -e .` setup; MIT-licensed;
  archived (read-only) as of 29 May 2026. Useful only to confirm the code
  exists and matches the paper's stated authorship — do not cite it for any
  number not already in the paper text, since the README carries no
  additional experimental detail beyond install/run instructions.
- **`data-nb-locator`:** `github.com/openai/grok` (repository root, README).

### 3. Nanda, Chan, Lieberum, Smith, Steinhardt — "Progress measures for grokking via mechanistic interpretability" (arXiv:2301.05217, ICLR 2023, Oral)

- **URL:** https://arxiv.org/abs/2301.05217 (abstract/metadata) and
  https://arxiv.org/html/2301.05217 (full text, read in full). Venue
  confirmed independently at https://iclr.cc/virtual/2023/oral/12572, which
  lists it as an "In-Person Oral presentation / top 25% paper," ICLR 2023.
- **Classification:** Primary for every claim below (this paper owns them).
  Secondary with respect to Power et al.'s original claims — it reports on
  and mechanistically explains the 2022 phenomenon from outside that paper's
  authorship, on a narrower task setup.
- **Establishes firsthand:**
  - Narrower task than Power et al.: "the model takes inputs a,b∈{0,…,P−1}
    for some prime P and predicts their sum c mod P" (Section 3) — modular
    **addition only**, not the 12-operation family Power tested. **P = 113**,
    not 97. One-layer ReLU transformer (not two-layer): embedding dim d=128,
    4 attention heads (head dim 32), MLP width 512, no LayerNorm, untied
    embed/unembed. Training data: 30% of all 12,769 (a,b) pairs (~3,850
    pairs). AdamW, lr 10⁻³, weight decay λ=1, full-batch, 40,000 epochs.
  - The algorithm claim, Section 3.1: the network maps each input token to
    sin/cos at several frequencies wₖ=2kπ/P via the embedding matrix, applies
    the angle-addition trigonometric identities cos(wₖ(a+b)) =
    cos(wₖa)cos(wₖb) − sin(wₖa)sin(wₖb) (and the sine analogue), then the
    unembedding matrix sums cos(wₖ(a+b−c)) terms across k so that "the cosine
    waves ... constructively interfere at c*=a+b mod p (giving c* a large
    logit), and destructively interfere everywhere else." Figure 1 shows this
    as literal rotation: "the model projects each point onto a corresponding
    rotation using its embedding matrix ... composes the rotations to get a
    representation of a+b mod P." Five key frequencies are identified:
    k∈{14,35,41,42,52} (Figure 3, Section 4.1).
  - Quantitative confirmation the algorithm is really what's implemented,
    Section 4.2–4.4: MLP-neuron projections explain 93–98% of variance for
    the cos/sin(wₖ(a+b)) terms; summing the identified frequency terms
    explains 95% of logit variance; of 512 neurons, 433 (84.6%) have >85% of
    their variance explained by a single frequency (Section 4.3, Figure 5);
    ablating to only the 10 key Fourier directions drops loss 50% (to
    1.19·10⁻⁷) and dropping the non-key frequencies drops loss 70% (to
    7.24·10⁻⁸) (Section 4.4, Figure 6).
  - The three-phase account, Section 5.2 (Figure 7), defined by four
    "progress measures" tracked over training: restricted loss (loss after
    zeroing all Fourier logit components except the constant term and the
    key-frequency terms), excluded loss (loss after zeroing only the
    key-frequency components, measured on training data), a Gini coefficient
    of per-frequency weight norms, and total weight ℓ₂-norm (Section 5.1).
    - **Memorization** (epoch 0–1.4k): "The model memorizes the data, and the
      frequencies wₖ used by the final model are unused." Train and excluded
      loss fall; test and restricted loss stay high; Gini stays flat.
    - **Circuit formation** (epoch 1.4k–9.4k): "The model's behavior on the
      train set transitions smoothly from the memorizing solution to the
      Fourier multiplication algorithm." Excluded loss rises, weight norm
      falls, restricted loss starts falling, while test and train loss stay
      flat — explicitly, "the circuit is formed well before grokking
      occurs."
    - **Cleanup** (epoch 9.4k–14k): "Weight decay encourages the network to
      shed the memorized solution in favor of focusing on the Fourier
      multiplication circuit." Excluded loss plateaus, restricted loss keeps
      falling, test loss suddenly drops, weight norm sharply drops.
  - "Progress measures" itself is defined by reference to prior work
    (Section 2, citing Barak et al. 2022 — see Source 7 below): metrics "that
    improve smoothly and that precede emergent behavior."
  - Result framing, restated in the abstract (already quoted verbatim in the
    paper card note above): "grokking, rather than being a sudden shift,
    arises from the gradual amplification of structured mechanisms encoded
    in the weights, followed by the later removal of memorizing components."
- **`data-nb-locator` suggestions:** `2301.05217#sec3` (task/architecture);
  `2301.05217#sec3.1` and `#fig1` (Fourier/rotation algorithm);
  `2301.05217#sec5.1` (progress-measure definitions); `2301.05217#sec5.2` and
  `#fig7` (three phases); `2301.05217#sec4.3` and `#sec4.4` (neuron/ablation
  numbers).

### 4. Liu, Kitouni, Nolte, Michaud, Tegmark, Williams — "Towards Understanding Grokking: An Effective Theory of Representation Learning" (arXiv:2205.10343, NeurIPS 2022)

- **URL:** https://arxiv.org/abs/2205.10343
- **Classification:** Primary for its own claims. Interpretation-changing
  follow-on with respect to Power et al.: it relocates the cause of grokking
  from "steps of optimization" to a geometric property of the parameter
  space, and it precedes and motivates Omnigrok (Source 5).
- **Establishes firsthand (abstract, verified verbatim):** "We find that
  generalization originates from structured representations whose training
  dynamics and dependence on training set size can be predicted by our
  effective theory in a toy setting. We observe empirically the presence of
  four learning phases: comprehension, grokking, memorization, and
  confusion. We find representation learning to occur only in a 'Goldilocks
  zone' (including comprehension and grokking) between memorization and
  confusion." It further claims "on transformers the grokking phase stays
  closer to the memorization phase ... leading to delayed generalization."
  This is the first appearance of the "Goldilocks zone" / weight-norm framing
  that Omnigrok later generalizes off algorithmic data.
- **Changes the interpretation how:** Power et al. frame grokking as a
  function of optimization steps and dataset fraction. This paper reframes it
  as a function of where a network's weight norm sits relative to a bounded
  "Goldilocks" region — steps and dataset size become proxies for that
  underlying geometric variable, not the cause itself.
- **`data-nb-locator`:** `2205.10343#abstract` (four-phase / Goldilocks-zone
  claim — I did not verify section-level detail beyond the abstract; flag to
  writer if a body quote is needed, request a follow-up read).

### 5. Liu, Michaud, Tegmark — "Omnigrok: Grokking Beyond Algorithmic Data" (arXiv:2210.01117, ICLR 2023)

- **URL:** https://arxiv.org/abs/2210.01117 (abstract/metadata) and
  https://ar5iv.labs.arxiv.org/html/2210.01117 (full text, read in full).
- **Classification:** Primary for its own claims. Interpretation-changing
  follow-on: it names a general mechanism (loss-landscape geometry) that
  subsumes Power et al.'s specific weight-decay and dataset-size findings as
  special cases, and empirically breaks the "algorithmic data only" framing
  of the original paper.
- **Establishes firsthand:**
  - The "LU mechanism," Section 2 (Figure 1b): "the (reduced) training loss
    and test loss are L-shaped and U-shaped against weight norm,
    respectively." A model whose weight norm sits outside a bounded "spherical
    shell in the weight space (the 'Goldilocks' zone)" (Section 2, Figure 1a)
    first minimizes training loss into an overfit solution, then regularization
    slowly shrinks the weight norm back toward the Goldilocks zone —
    generalization appears only once the norm crosses in.
  - Predicted scaling: generalization time scales as t ∝ γ⁻¹ in weight-decay
    magnitude γ (Section 2) — this directly reframes Power et al.'s empirical
    "weight decay more than halves the samples needed" finding as a special
    case of a general norm-shrinkage law.
  - Dataset-size claim, Section 4: "Larger datasets lead to de-grokking" —
    consistent in direction with Power et al.'s dataset-fraction finding, but
    now explained by a broadening Goldilocks zone rather than left as a bare
    correlation.
  - Off-algorithmic-data claim, directly answering whether grokking is
    unique to Power et al.'s task family (Abstract): "we demonstrate grokking
    for a wide range of machine learning tasks ... including image
    classification, sentiment analysis and molecule property prediction,"
    though these signals are "usually less dramatic than for algorithmic
    datasets." Concrete setups: MNIST reduced to 1,000 samples with
    initialization scale α>1; IMDb sentiment (LSTM), 1k and 50k samples,
    α=6 (Figure 4); QM9 molecule property prediction (GCNN), 200 training
    samples, α=3 (Figure 5). It also replicates a transformer-on-modular-
    addition setup at **p=113, train fraction 0.3** (Appendix B) — the same
    p=113 choice Nanda uses, not Power's p=97.
- **Changes the interpretation how:** directly undercuts any reading of
  grokking as an algorithmic-data curiosity. It also reframes Power et al.'s
  weight-decay result as one instance of a norm-shrinkage law rather than an
  independent empirical finding.
- **`data-nb-locator` suggestions:** `2210.01117#sec2` and `#fig1` (LU
  mechanism, Goldilocks zone); `2210.01117#sec4` (dataset-size,
  off-algorithmic tasks); `2210.01117#appB` (p=113 transformer replication).

### 6. Varma, Shah, Kenton, Kramár, Kumar — "Explaining grokking through circuit efficiency" (arXiv:2309.02390)

- **URL:** https://arxiv.org/abs/2309.02390
- **Classification:** Primary for its own claims. Interpretation-changing
  follow-on: proposes a third, distinct causal account (efficiency of
  competing circuits) and derives two behaviors — ungrokking and
  semi-grokking — that neither Power et al. nor Nanda et al. predict or
  observe.
- **Establishes firsthand (abstract, verified verbatim):** "We propose that
  grokking occurs when the task admits a generalising solution and a
  memorising solution, where the generalising solution is slower to learn
  but more efficient, producing larger logits with the same parameter norm.
  We hypothesise that memorising circuits become more inefficient with
  larger training datasets while generalising circuits do not, suggesting
  there is a critical dataset size at which memorisation and generalisation
  are equally efficient." It reports confirming "four novel predictions,"
  and demonstrating two new behaviors: "ungrokking, in which a network
  regresses from perfect to low test accuracy, and semi-grokking, in which a
  network shows delayed generalisation to partial rather than perfect test
  accuracy."
- **Changes the interpretation how:** relocates the cause from Nanda et al.'s
  Fourier-circuit-specific story and from Omnigrok's weight-norm story to a
  general efficiency competition between any generalizing and memorizing
  circuit pair — and it makes falsifiable predictions (ungrokking,
  semi-grokking) that go beyond restating the original phenomenon, which is
  exactly the kind of follow-on that earns a slot per the source-obligations
  rule.
- **`data-nb-locator`:** `2309.02390#abstract` (I read the abstract in full
  and verified it verbatim; I did not verify body-section locators for the
  four specific predictions — flag to writer/editor if a body quote with
  section number is needed for a display note, request a follow-up read).

### 7. Prieto, Barsbey, Mediano, Birdal — "Grokking at the Edge of Numerical Stability" (arXiv:2501.04697)

- **URL:** https://arxiv.org/abs/2501.04697 (abstract/metadata) and
  https://arxiv.org/html/2501.04697 (full text, read in full).
- **Classification:** Primary for its own claims. Interpretation-changing
  follow-on and the piece's best "grokking is fragile" evidence: it directly
  disputes what weight decay is doing, contradicting Omnigrok's account (see
  Contradictions §2).
- **Establishes firsthand:**
  - Abstract (verbatim): "In this work we argue that without regularization,
    grokking tasks push models to the edge of numerical stability,
    introducing floating point errors in the Softmax that we refer to as
    Softmax Collapse (SC). We show that SC prevents grokking and that
    mitigating SC leads to grokking without regularization."
  - Definitions: **Softmax Collapse** (Definition 3, Section 3.1) — a
    floating-point absorption error where, when one logit is much larger than
    the rest, ∑e^zₖ ≐ e^z_y and the cross-entropy loss numerically floors at
    0 without further learning. **Naïve Loss Minimization** (Definition 5,
    Section 4.2) — a direction that reduces loss purely by scaling all logits
    by a constant c>1, f(θ+d_NLM(θ);x)=c·f(θ;x), without changing any
    prediction.
  - Weight decay reframed, Section 5.2: "We argue that the main roles of
    weight decay are preventing floating point errors and preventing NLM" —
    not primarily the norm-shrinkage/Goldilocks-zone role Omnigrok assigns
    it.
  - Modular-arithmetic replication, at **p=113** (matching Nanda/Omnigrok,
    not Power's p=97): Figure 2/Section 3.2, an MLP trained on modular
    addition mod 113 with 40%, 60%, 70% training splits shows generalization
    halting once Softmax Collapse begins, earlier in float32 than float64.
    Figure 4/Section 3.3: with 40% of all pairs mod 113, their StableMax
    activation achieves grokking *without* any weight decay, where standard
    cross-entropy fails to generalize at all.
- **Changes the interpretation how:** if weight decay's real job is
  preventing a floating-point failure mode rather than shrinking weight norm
  into a Goldilocks zone, then Power et al.'s central ablation finding
  (weight decay "more than halving the amount of samples needed") is real
  but was misattributed by the two years of intervening literature that
  explained it geometrically. This is the sharpest interpretation-changing
  claim in the record.
- **`data-nb-locator` suggestions:** `2501.04697#sec3.1` (Softmax Collapse
  definition); `2501.04697#sec4.2` (NLM definition); `2501.04697#sec5.2`
  (weight-decay reattribution); `2501.04697#sec3.2` and `#fig2` (p=113
  replication); `2501.04697#sec3.3` and `#fig4` (StableMax without
  regularization).

### 8. Barak, Edelman, Goel, Kakade, Malach, Zhang — "Hidden Progress in Deep Learning: SGD Learns Parities Near the Computational Limit" (arXiv:2207.08799)

- **URL:** https://arxiv.org/abs/2207.08799
- **Classification:** Primary for its own claims (sparse-parity learning, not
  grokking on modular arithmetic). Secondary/contextual for the grokking
  story: this is the paper Nanda et al. cite (Section 2) as the origin of the
  "progress measures" concept the whole mechanistic account depends on, and
  it independently documents an unexplained discontinuous generalization
  curve on a different task, which is useful corroboration that the
  phenomenon is not an artifact of Power et al.'s specific setup.
- **Establishes firsthand (abstract, verified verbatim):** studies "learning
  a k-sparse parity of n bits, a canonical discrete search problem which is
  statistically easy but computationally hard," and finds "a variety of
  neural networks successfully learn sparse parities, with discontinuous
  phase transitions in the training curves," at "approximately n^O(k)
  iterations." Crucially: "these observations are not explained by a
  Langevin-like mechanism, whereby SGD 'stumbles in the dark' ... Instead,
  ... SGD gradually amplifies the sparse solution via a Fourier gap in the
  population gradient, making continual progress that is invisible to loss
  and error metrics" — i.e., a smooth "hidden" progress measure exists
  beneath a visibly discontinuous accuracy curve, the same shape of claim
  Nanda et al. later make about grokking specifically.
- **Use with care:** do not cite this as evidence about modular arithmetic or
  transformers — it studies parity learning, a different task and (in the
  cited abstract) does not specify architecture. Cite it only for the
  "progress measures" lineage and the general point that discontinuous
  accuracy curves can hide smooth underlying progress, which is Nanda et
  al.'s own framing move applied to a different setting first.
- **`data-nb-locator`:** `2207.08799#abstract` (I verified only the abstract
  verbatim; did not read body sections — if the writer wants a body quote
  or figure number, flag for a follow-up read).

### 9. MATH-AI workshop (ICLR 2021 edition) — accepted-papers page

- **URL:** https://mathai-iclr.github.io/papers/
- **Classification:** Primary for the one fact it's cited for: whether
  Power et al.'s paper appears on this workshop's own accepted-papers list,
  and what that page calls itself. Not a source for any grokking claim.
- **Establishes firsthand:** the page self-identifies as "MATH-AI - ICLR 2021
  Workshop on the Role of Mathematical Reasoning in General Artificial
  Intelligence" and lists "Grokking: Generalization Beyond Overfitting on
  Small Algorithmic Datasets" as paper #20 among its accepted papers. I could
  not extract the underlying PDF text (binary/compressed) to independently
  confirm the paper content matches, only the listing itself.
  Cross-referenced against https://mathai2022.github.io/ (the *second*
  MATH-AI workshop, held at NeurIPS 2022, 3 Dec 2022), whose own page states
  the prior edition was "1st MATH-AI Workshop at ICLR'21" — confirming there
  was no ICLR 2022 MATH-AI workshop for Power et al. to have appeared in
  under that workshop's own numbering.
- **Tension with the commission:** this is squarely at odds with the
  commission's assumption of "ICLR 2022 Workshop." See Contradictions §1.
- **`data-nb-locator`:** `mathai-iclr.github.io/papers` (accepted-papers
  listing, entry #20).

---

## Contradictions

1. **Venue of the focal paper is unresolved, and the one primary trace
   found contradicts the commission's assumption.** The commission and
   brief both instruct "ICLR 2022 Workshop... get it right." I read the
   arXiv abstract page directly: it carries no Comments field, no
   Journal-ref field, no venue metadata of any kind — only the cs.LG
   category and the 6 Jan 2022 submission date. The only primary trace of a
   workshop presentation I could find is the MATH-AI workshop's own
   accepted-papers page (Source 9), which lists the paper under "MATH-AI -
   ICLR 2021 Workshop" — and the *second* MATH-AI workshop's own page
   (mathai2022.github.io, NeurIPS 2022) confirms there was no ICLR 2022
   edition in that series. That leaves two bad options: either the paper
   genuinely was accepted to a 2021 workshop roughly a year before its
   arXiv posting (unusual but not impossible for a non-archival workshop,
   where authors are free to arXiv whenever), or the commission's "2022" is
   the correct year and I have not found the right venue page. I did not
   find an OpenReview forum for this paper (search turned up nothing, and
   direct OpenReview PDF fetches were blocked by a bot-check page, not a
   403 — see Discarded). **Recommend the writer/editor either verify
   independently before printing a specific venue/year, or use a
   deliberately non-committal phrasing** ("presented as a workshop paper";
   avoid naming the specific workshop and year in running text unless
   resolved).

2. **Two follow-on papers give incompatible accounts of what weight decay
   is doing, and both cite the same underlying fact (Power et al.'s
   ablation result) to support opposite mechanisms.** Omnigrok (Source 5)
   holds that weight decay works by shrinking the weight norm into a bounded
   "Goldilocks zone" — a geometric account, predicting generalization time
   scales as t ∝ γ⁻¹ in the decay magnitude. Prieto et al. (Source 7) holds
   that weight decay's main job is preventing a floating-point failure mode
   (Softmax Collapse) and a logit-scaling failure mode (Naïve Loss
   Minimization) — a numerical account that explicitly downplays norm
   geometry as the operative mechanism (Section 5.2: "the main roles of
   weight decay are preventing floating point errors and preventing NLM").
   Varma et al. (Source 6) offers a third account (circuit efficiency) that
   doesn't center weight decay at all. None of the three follow-ons cites or
   directly refutes the others' central mechanism in the passages I read;
   the field has not converged. State this as open disagreement, not as a
   sequence of supersession.

3. **The follow-on literature narrows the task before it explains it.**
   Power et al.'s central claim covers 12 operations at modulus p=97 on a
   2-layer transformer. Every mechanistic/explanatory follow-on I verified
   (Nanda, Omnigrok's Appendix B replication, Prieto et al.) instead studies
   modular **addition only** at **p=113** on a **1-layer** transformer (or,
   for Prieto et al., an MLP). No source in this record demonstrates the
   Fourier-rotation mechanism, the three-phase account, or the Softmax
   Collapse account on the *other 11 operations* Power et al. tested, or at
   p=97, or on the 2-layer architecture. The mechanistic story is verified
   on a narrower slice of the phenomenon than the phenomenon itself. This is
   worth stating plainly as a limit on how much of the 2022 paper the
   after-record actually explains.

4. **The paper's own admitted uncertainty is about flat minima, not about
   Fourier circuits, numerical stability, or circuit efficiency.** Power et
   al.'s own speculative hypothesis for future work (Appendix A.5) is that
   grokking "may only happen after the network's parameters are in flatter
   regions of the loss landscape" — a flat-minima account. None of the three
   follow-ons in this record (Nanda, Omnigrok, Prieto/Varma) frames its
   explanation in terms of loss-landscape flatness; Omnigrok explicitly
   frames it in terms of weight-norm geometry instead, which is related but
   not the same claim. Worth noting that the after-record didn't confirm the
   authors' own guess so much as replace it.

## Numbers

| Number | Owning source | Exact reading | Unit / denominator | Period / condition |
|---|---|---|---|---|
| Modulus | Power et al. (Source 1) | p = 97 | prime modulus | all 12 operations, main paper |
| Modulus | Nanda / Omnigrok appendix / Prieto (Sources 3, 5, 7) | p = 113 | prime modulus | modular-addition-only replications |
| Train fraction, headline curve | Power et al., Fig. 1 caption | 50% | fraction of all (x,y) pairs | division mod 97 |
| Train fraction, Nanda/Omnigrok | Nanda §3; Omnigrok App. B | 30% (≈3,850 of 12,769 pairs) | fraction of p² pairs | modular addition, p=113 |
| Steps to near-perfect train accuracy | Power et al. §3.1 | <10³ steps | optimizer steps | division mod 97, 50% train |
| Steps to validation generalization | Power et al. §3.1 | ~10⁶ steps | optimizer steps | same run |
| Steps before "very little evidence" of generalization | Power et al. §3.1 | 10⁵ steps | optimizer steps | same run |
| Effect of 1% less training data | Power et al. §3.1.1 | +40–50% | median steps to generalize | near minimal viable dataset size |
| Weight decay effect | Power et al. §3.3 | "more than halving" samples needed | fraction of dataset | vs. other interventions, ablation |
| Architecture (focal) | Power et al. | 2 layers, width 128, 4 heads, ~4·10⁵ non-embedding params | — | decoder-only transformer |
| Architecture (Nanda) | Nanda §3 | 1 layer, d=128, 4 heads (head dim 32), MLP width 512 | — | ReLU transformer, no LayerNorm |
| Training epochs (Nanda) | Nanda §3 | 40,000 | epochs, full-batch | modular addition p=113 |
| Phase boundaries (Nanda) | Nanda §5.2, Fig. 7 | memorization 0–1.4k; circuit formation 1.4k–9.4k; cleanup 9.4k–14k | epochs | modular addition p=113 |
| Key frequencies (Nanda) | Nanda §4.1, Fig. 3 | k ∈ {14, 35, 41, 42, 52} | frequency index | 5 of many possible |
| Neuron single-frequency fit (Nanda) | Nanda §4.3, Fig. 5 | 433 of 512 (84.6%) | neurons, >85% variance by one frequency | trained network |
| Ablation loss drop, non-key freqs removed (Nanda) | Nanda §4.4, Fig. 6 | loss falls 70%, to 7.24·10⁻⁸ | training loss | ablation study |
| Ablation loss drop, 10 Fourier dirs (Nanda) | Nanda §4.4, Fig. 6 | loss falls 50%, to 1.19·10⁻⁷ | training loss | ablation study |
| Generalization-time scaling law | Omnigrok §2 | t ∝ γ⁻¹ | optimization steps vs. weight-decay magnitude γ | predicted, general |
| Weight-decay magnitude, Nanda's mainline run | Nanda §3 | λ = 1 | AdamW weight decay | same run as above |
| Modular-addition splits tested, Prieto et al. | Prieto §3.2, Fig. 2 | 40%, 60%, 70% | fraction of pairs, p=113 | MLP, float32 vs float64 |

Full series worth transcribing for a chart (if the writer wants one, per the
commission's no-fabrication rule — I did not extract literal per-step
accuracy series, only the qualitative shape and the four cited thresholds
above; a real accuracy-vs-steps series would need a fresh read of Power et
al.'s released code/logs or a digitization of Figure 1, which I have not
done):
- Power et al. Figure 1 (left): train accuracy and validation accuracy vs.
  optimizer steps, log-x axis, division mod 97, 50% train split.
- Nanda et al. Figure 2: train and test accuracy vs. epoch, modular
  addition p=113, 30% train split — this is the curve the three-phase
  account (Figure 7) is laid over.

## Source assets

- **Power et al., Figure 1 (full figure, three panels).** Location:
  arxiv.org/abs/2201.02177, Figure 1 (left/center/right panels), Section 3.1.
  What a reader learns: the left panel is the canonical grokking curve
  itself (train vs. validation accuracy, division mod 97); the center panel
  shows how time-to-generalize scales with dataset size; useful as the
  single most load-bearing image in the piece since it *is* the paper's
  core claim. A crop must retain the log-scale x-axis and both curves (train
  and validation) with the axis labels legible — cropping to only the
  "before" or "after" half would misrepresent the delayed-generalization
  claim.
- **Nanda et al., Figure 1 (rotation diagram).** Location:
  arxiv.org/abs/2301.05217 (or arxiv.org/html/2301.05217), Figure 1, Section
  3.1. What a reader learns: the literal geometric picture of the claimed
  algorithm (embedding onto a circle, composing rotations, reading off the
  sum). A crop must keep the rotation arrows and the labeled angle so the
  "addition becomes rotation" claim is visually legible, not just the
  circle outline.
- **Nanda et al., Figure 7 (three-phase progress measures).** Location:
  arxiv.org/html/2301.05217, Figure 7, Section 5.2. What a reader learns:
  the four tracked metrics (train/test loss, restricted loss, excluded loss,
  Gini coefficient / weight norm) plotted together across the three named
  phases — this is the direct visual evidence for "grokking is not a sudden
  shift" argument. A crop must retain phase boundary markers/shading and all
  four metric lines with a legend; cropping to a single metric would lose
  the "several things move before the visible jump" argument.
- **Omnigrok, Figure 1 (L/U loss-vs-weight-norm panels).** Location:
  arxiv.org/abs/2210.01117 (ar5iv HTML), Figure 1, Section 2. What a reader
  learns: the L-shaped train loss and U-shaped test loss against weight
  norm, with the Goldilocks zone marked — the clean visual argument for the
  norm-geometry account. A crop must keep both the L and U curves on the
  same axes with the Goldilocks-zone band marked; showing only one curve
  loses the mismatch that is the entire mechanism.
- **Prieto et al., Figure 2 or Figure 4.** Location: arxiv.org/html/2501.04697,
  Section 3.2–3.3. What a reader learns: Figure 2 shows generalization
  halting once Softmax Collapse begins (float32 vs float64 comparison);
  Figure 4 shows StableMax achieving grokking without any weight decay. A
  crop must keep the float32/float64 or StableMax/cross-entropy comparison
  pairs together — either panel alone loses the contrast the argument
  depends on. I have not viewed the images themselves (text-only extraction
  via WebFetch); the writer/editor should visually inspect before using
  either as a chart source.

## Discarded

- **OpenReview PDFs for two candidate follow-ons** (`[Re] "Towards
  Understanding Grokking"`, id=Vz9VLcJqKS; "Progress Measures for Grokking
  on Real-world Tasks," id=0gswXyexqv) — both fetch attempts returned an
  OpenReview browser/bot-check page, not paper content. This is a gate, not
  necessarily a dead end, but I could not verify either paper's content
  within scope; do not cite either without a successful read.
- **Ootani, "Grokking Is Conditional and Fragile: A Fully-Tractable,
  Multi-Seed Study at 12K Parameters" (arXiv:2607.05104, July 2026)** — read
  in full via HTML fetch. Rejected as a citable source despite being
  on-topic (multi-seed fragility, floating-point-environment sensitivity,
  reproduces the Omnigrok inverted-U at small scale) because: single
  author, no listed institutional affiliation found, studies an idiosyncratic
  and unfamiliar "~11,856-parameter Llama-style transformer (Glimmer-1-Base)"
  rather than a standard architecture, and its central numerical-fragility
  claim is already covered by the verified, more established Prieto et al.
  2025 (Source 7). Flag to writer only as a "for further reading" pointer if
  wanted, not as a cited claim source, given I could not independently
  corroborate the model/setup described.
- **Wikipedia, "Grokking (machine learning)"** — read for orientation only.
  Tertiary source; used here only to confirm that no venue is stated in the
  article's own running text, not cited for any claim in this record.
- **Semantic Scholar paper pages** for both the focal paper and Nanda et
  al. — fetch attempts returned empty content (tool could not extract page
  body). Not used for any claim.
- **arxiv.org/html/2201.02177 (direct route)** — returns HTTP 404. This is
  the focal paper's non-ar5iv HTML route; the ar5iv.labs.arxiv.org mirror
  (used throughout Source 1) worked and was read in full instead, per the
  gated-not-dead instruction.
- **WebFetch on raw PDF bytes** (arxiv.org/pdf/2201.02177,
  arxiv.org/pdf/2301.05217) — both returned undecoded binary/PDF-stream
  content, unreadable by the fetch tool. Superseded by the HTML/ar5iv routes
  for both papers, which worked and were used for all substantive claims
  above.
