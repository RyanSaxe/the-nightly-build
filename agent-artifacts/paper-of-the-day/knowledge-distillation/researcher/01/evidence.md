# Evidence record — knowledge-distillation

The evidence strongly supports the reconstruction: the 2015 mechanism (a
temperature-scaled softmax exposing relative probabilities of wrong classes,
trained against a weighted sum of soft and hard cross-entropies) and its
headline results are read firsthand from the paper and are internally exact. It
also strongly supports the counter-reading: Stanton et al. 2021, read in full,
show that on modern architectures a student trained to copy the teacher usually
fails to match the teacher's predictive distribution, and pin the cause on
optimization, not capacity or data. Where the record is thin is any single
tidy number for "how often distillation fails," because fidelity is measured
several ways (top-1 agreement, predictive KL) across several settings; the
honest statement is a range and a contrast (near-perfect on a toy task,
mid-80s% agreement on CIFAR-100), not one figure. The successes are real and
well-sourced (DistilBERT, Born-Again, Beyer), and Müller et al. give the clean
mechanistic confirmation that the relational logit information is exactly what
distillation lives on. All eight sources are primary (each authoring team owns
its own results); there is no independent secondary reporting cited, which is
appropriate for a paper-reconstruction that argues from the papers themselves.

## Sources

### [S1] Hinton, Vinyals & Dean 2015 — "Distilling the Knowledge in a Neural Network"
- URL: https://arxiv.org/abs/1503.02531 (PDF: https://arxiv.org/pdf/1503.02531). Resolves.
- Kind: PRIMARY. The paper owns the distillation method and all its reported
  experiments. Venue: NIPS 2014 Deep Learning Workshop; arXiv v1, 9 Mar 2015.
- Establishes firsthand:
  - Abstract (verbatim, for the paper card): "A very simple way to improve the
    performance of almost any machine learning algorithm is to train many
    different models on the same data and then to average their predictions. …
    Caruana and his collaborators [1] have shown that it is possible to compress
    the knowledge in an ensemble into a single model which is much easier to
    deploy and we develop this approach further using a different compression
    technique. We achieve some surprising results on MNIST and we show that we
    can significantly improve the acoustic model of a heavily used commercial
    system by distilling the knowledge in an ensemble of models into a single
    model. We also introduce a new type of ensemble composed of one or more full
    models and many specialist models which learn to distinguish fine-grained
    classes that the full models confuse. Unlike a mixture of experts, these
    specialist models can be trained rapidly and in parallel." (Abstract, p.1)
  - The reframing of "knowledge": rather than the learned parameter values,
    "a more abstract view … is that it is a learned mapping from input vectors
    to output vectors." (p.1–2)
  - Dark knowledge, verbatim: "The relative probabilities of incorrect answers
    tell us a lot about how the cumbersome model tends to generalize. An image
    of a BMW, for example, may only have a very small chance of being mistaken
    for a garbage truck, but that mistake is still many times more probable than
    mistaking it for a carrot." (p.2)
  - The MNIST ratio example, verbatim: "one version of a 2 may be given a
    probability of 10^-6 of being a 3 and 10^-9 of being a 7 whereas for another
    version it may be the other way around. This is valuable information that
    defines a rich similarity structure over the data." (p.2)
  - Soft targets carry more per case: "When the soft targets have high entropy,
    they provide much more information per training case than hard targets and
    much less variance in the gradient between training cases, so the small
    model can often be trained on much less data … and using a much higher
    learning rate." (p.2)
  - Temperature softmax, Eq. (1): q_i = exp(z_i / T) / sum_j exp(z_j / T),
    "where T is a temperature that is normally set to 1. Using a higher value
    for T produces a softer probability distribution over classes." (§2, p.2–3)
  - Two-objective training: a weighted average of (a) cross-entropy with the
    soft targets, computed at the same high T in the student's softmax, and (b)
    cross-entropy with the true labels at T=1; "best results were generally
    obtained by using a condiderably [sic] lower weight on the second objective
    function." (§2, p.3)
  - Gradient scaling: "Since the magnitudes of the gradients produced by the
    soft targets scale as 1/T^2 it is important to multiply them by T^2 when
    using both hard and soft targets." (§2, p.3)
  - Matching logits is a special case: gradient dC/dz_i = (1/T)(q_i − p_i); in
    the high-T limit with per-case zero-meaned logits it reduces to
    dC/dz_i ≈ (1/(N T^2))(z_i − v_i), i.e. "distillation is equivalent to
    minimizing 1/2 (z_i − v_i)^2." (§2.1, Eqs. 2–4, p.3)
  - "At lower temperatures, distillation pays much less attention to matching
    logits that are much more negative than the average"; when the student "is
    much too small to capture all of the knowledge … intermediate temperatures
    work best." (§2.1, p.3)
- Kind test: primary — authoring party, owns the method and data.

### [S2] Stanton, Izmailov, Kirichenko, Alemi & Wilson 2021 — "Does Knowledge Distillation Really Work?"
- URL: https://arxiv.org/abs/2106.05945 (PDF: https://arxiv.org/pdf/2106.05945). Resolves. NeurIPS 2021; v2, 6 Dec 2021.
- Kind: PRIMARY. Owns its fidelity measurements and diagnosis.
- Establishes firsthand:
  - Abstract (verbatim): "Knowledge distillation is a popular technique for
    training a small student network to emulate a larger teacher model, such as
    an ensemble of networks. We show that while knowledge distillation can
    improve student generalization, it does not typically work as it is commonly
    understood: there often remains a surprisingly large discrepancy between the
    predictive distributions of the teacher and the student, even in cases when
    the student has the capacity to perfectly match the teacher. We identify
    difficulties in optimization as a key reason for why the student is unable to
    match the teacher. We also show how the details of the dataset used for
    distillation play a role in how closely the student matches the teacher —
    and that more closely matching the teacher paradoxically does not always
    lead to better student generalization." (Abstract, p.1)
  - The two-word answer, verbatim: "Does knowledge distillation really work? In
    short: Yes, in the sense that it often improves student generalization …
    No, in that knowledge distillation often fails to live up to its name,
    transferring very limited knowledge from teacher to student." (§1, p.1)
  - Definitions: "fidelity, the ability of a student to match a teacher's
    predictions, and generalization, the performance of a student in predicting
    unseen, in-distribution data." (§1, p.1). Metrics: Average Top-1 Agreement
    (Eq. 2) and Average Predictive KL (Eq. 3). (§3.2, p.3)
  - Same loss family as Hinton, α=0 in the main text (pure distillation) to
    avoid label confounding; and the high-temperature limit
    ∇_{z_s} L_KD ≈ z_t − z_s "approximately equivalent to ∇ ||z_t − z_s||^2 / 2,
    assigning equal significance to every class logit." (§3.1, Eq. 1, p.3)
  - Easy case works: LeNet-5 teacher (trained on 200 MNIST examples, 84–86%
    test acc) self-distilled with the full 60k MNIST + up to 700k EMNIST reaches
    "over 99% top-1 test agreement." (§4.1, Fig. 2, p.4)
  - Hard case plateaus: ResNet-56 on CIFAR-100 self-distilled with GAN-augmented
    data — fidelity "nowhere near 99%," test agreement "below 80%" even at 50k
    synthetic images. (§4.1, Fig. 1, and §6.1, p.4, p.8)
  - Augmentation ceiling: best fidelity policy MixUp(τ=4) "only achieves a
    modest 86% test agreement"; "Baseline (τ = 4) policy is quite competitive,
    achieving 84.5% test agreement." Best augmentation policies for
    generalization (MixUp, GAN) are NOT the best for fidelity. (§5.1, Fig. 3, p.7)
  - Data recycling: best teacher-student agreement "only around 85%." (§5.2, p.7)
  - Self-distillation exceeds teacher only by failing: "This result is only
    possible by virtue of failing at the distillation procedure: if the student
    matched the teacher perfectly then the student could not outperform the
    teacher." (§4.2, p.4)
  - Optimization is the root cause: ResNet-20 self-distillation train agreement
    "83.3% agreement when training for 5k epochs compared to 78.95% when
    training for 300 epochs" — a ~2% gain for 16x compute, extrapolating to
    "tens of thousands of epochs" for ~100%. (§6.2, Fig. 6a, p.9). Combined
    augmentations drop train agreement "to just 60% in self-distillation."
    (§6.1, p.8)
  - Initialization basin: with θ_s = λθ_t + (1−λ)θ_r, students init far from the
    teacher (λ ≤ 0.25) fall into "a distinct, sub-optimal basin"; at λ = 0.375
    "the final train loss drops to the optimal value and the agreement
    drastically increases." But initializing at the teacher's *initial* weights
    does not help: Table 1 test agreement 77.174 (random) vs 77.098 (teacher
    init) — "functionally the students are identical." (§6.2, Table 1, p.9–10)
  - Discussion findings (verbatim bullets): "Good student accuracy does not
    imply good distillation fidelity"; "Student fidelity is correlated with
    calibration when distilling ensembles"; "Optimization is challenging in
    knowledge distillation: even in cases when the student has sufficient
    capacity to match the teacher on the distillation data, it is unable to do
    so"; "There is a trade-off between optimization complexity and distillation
    data quality." (§7, p.10)
- Kind test: primary — authoring party, owns the experiments and diagnosis.

### [S3] Sanh, Debut, Chaumond & Wolf 2019 — "DistilBERT"
- URL: https://arxiv.org/abs/1910.01108. Resolves.
- Kind: PRIMARY. Owns the DistilBERT model and its benchmark numbers.
- Establishes firsthand: "it is possible to reduce the size of a BERT model by
  40%, while retaining 97% of its language understanding capabilities and being
  60% faster." Distillation is applied during *pre-training*; a triple loss
  (language modeling + distillation + cosine-distance). (Abstract)
- Role: the canonical deployment success — compression that keeps generalization.

### [S4] Furlanello, Lipton, Tschannen, Itti & Anandkumar 2018 — "Born-Again Neural Networks"
- URL: https://arxiv.org/abs/1805.04770. Resolves. ICML 2018.
- Kind: PRIMARY. Owns the BAN result.
- Establishes firsthand: "rather than compressing models, we train students
  parameterized identically to their teachers. Surprisingly, these Born-Again
  Networks (BANs), outperform their teachers significantly, both on computer
  vision and language modeling tasks." Reported DenseNet validation error
  CIFAR-10 3.5%, CIFAR-100 15.5%. (Abstract)
- Role: a same-capacity student beats the teacher — which, per Stanton §4.2, is
  possible precisely because the student does NOT match the teacher. Ties the
  "success" and "low fidelity" readings together.

### [S5] Müller, Kornblith & Hinton 2019 — "When Does Label Smoothing Help?"
- URL: https://arxiv.org/abs/1906.02629. Resolves. NeurIPS 2019.
- Kind: PRIMARY. Owns the label-smoothing/distillation finding.
- Establishes firsthand: "if a teacher network is trained with label smoothing,
  knowledge distillation into a student network is much less effective." Cause:
  label smoothing tightens same-class clusters, causing "loss of information in
  the logits about resemblances between instances of different classes, which is
  necessary for distillation, but does not hurt generalization or calibration."
  (Abstract)
- Role: mechanistic confirmation that the relational logit structure — Hinton's
  dark knowledge — is exactly what distillation depends on; erase it and a
  more-accurate teacher becomes a worse teacher.

### [S6] Buciluǎ, Caruana & Niculescu-Mizil 2006 — "Model Compression"
- URL: https://www.cs.cornell.edu/~caruana/compression.kdd06.pdf. Resolves (HTTP 200). KDD '06.
- Kind: PRIMARY. Owns the original ensemble-compression result.
- Establishes firsthand: the strategy Hinton [S1] credits as pioneering — the
  knowledge of a large ensemble can be transferred into one small model that is
  much cheaper to deploy (Hinton's ref [1]); they used a large unlabeled
  transfer set labeled by the ensemble.
- Role: the origin. Distillation generalizes their probability/logit-target idea
  via temperature.

### [S7] Ba & Caruana 2014 — "Do Deep Nets Really Need to be Deep?"
- URL: https://arxiv.org/abs/1312.6184. Resolves. NIPS 2014.
- Kind: PRIMARY. Owns the shallow-mimic result.
- Establishes firsthand: "shallow feed-forward networks can learn the complex
  functions previously learned by deep nets and achieve accuracies previously
  only achievable with deep models," by training the student to match the
  teacher — Hinton [S1] notes they "circumvent this problem by using the logits
  … rather than the probabilities … and they minimize the squared difference
  between the logits." (Abstract; and S1 §, p.2)
- Role: the immediate precursor whose logit-matching Hinton shows is the
  high-temperature special case of distillation.

### [S8] Beyer, Zhai, Royer, Markeeva, Anil & Kolesnikov 2022 — "Knowledge distillation: A good teacher is patient and consistent"
- URL: https://arxiv.org/abs/2106.05237 (PDF: https://arxiv.org/pdf/2106.05237). Resolves. CVPR 2022.
- Kind: PRIMARY. Owns its recipe and ImageNet result.
- Establishes firsthand: "distillation works the best when we train patiently
  for a large number of epochs and provide consistent image views to teacher
  and student models." They treat distillation as *function matching*, use an
  "aggressive variant of mixup," train up to ~9600 epochs (Fig. 1 x-axis: 30,
  90, 300, 1200, 4800, 9600), and "obtain a state-of-the-art ResNet-50 model
  for ImageNet, which achieves 82.8% top-1 accuracy." (Abstract, §, Fig. 1)
- Role: the constructive answer to Stanton — if the bottleneck is optimization,
  pay for it (patience + consistency) and fidelity/accuracy both improve. A
  direct contradiction-in-emphasis to the pessimistic reading.

## Contradictions
- **Stanton (S2) vs Beyer (S8).** Same year, opposite headline. Stanton: on
  modern nets the student usually fails to match the teacher and the cause is a
  very hard optimization problem. Beyer: solve that optimization problem with
  patience (thousands of epochs) and consistency (same views) and distillation
  is "a powerful tool," 82.8% ResNet-50. These are not really opposed — Stanton
  names optimization as the obstacle; Beyer pays the price to overcome it. The
  article should present them as diagnosis and prescription, not as a
  disagreement about facts. Note Stanton explicitly discusses Beyer as
  concurrent work (§2).
- **Born-Again (S4) vs the fidelity frame (S2).** A same-capacity student beats
  its teacher — apparently the strongest success. Stanton §4.2 reframes it: the
  student can only beat the teacher because it did NOT match it. So Born-Again is
  evidence FOR low fidelity, not against it. Do not present BAN as a fidelity
  success.
- **Hinton's "much less data" (S1) vs Stanton's "more data lowers train
  agreement" (S2).** Hinton says soft targets let you train on much less data;
  Stanton says enlarging the distillation set beyond the teacher's training data
  makes the optimization harder and lowers train agreement. Both are consistent:
  the tension is fidelity (matching the distribution) vs generalization
  (accuracy on unseen data), which is the article's spine.
- **Müller (S5) caveat.** More-accurate teacher (label-smoothed) → worse student.
  Confirms distillation depends on the exact relational structure Hinton
  identified, and warns that "better teacher" is not monotone for distillation.

## Numbers
All verified against the owning primary.

MNIST (S1, §3, p.4):
- Large net (2×1200 ReLU, dropout + weight constraints, images jittered ≤2px):
  67 test errors.
- Small net (2×800 ReLU, no regularization): 146 test errors.
- Same small net, regularized only by matching soft targets at T=20: 74 errors.
- Omit all 3s from transfer set: distilled net makes 206 test errors, 133 of
  them on the 1010 test threes. With the 3-bias raised by 3.5: 109 errors, 14 on
  3s → "98.6% of the test 3s correct despite never having seen a 3 during
  training."
- Transfer set = only 7s and 8s: 47.3% test errors → 13.2% after adjusting the
  7/8 biases by 7.6.

Speech, Table 1 (S1, §4, p.5):
- Baseline single model: 58.9% frame accuracy, 10.9% WER.
- 10× ensemble: 61.1% frame accuracy, 10.7% WER.
- Distilled single model (T ∈ {1,2,5,10}, hard-target weight 0.5): 60.8% frame
  accuracy, 10.7% WER. "More than 80% of the improvement in frame classification
  accuracy achieved by using an ensemble of 10 models is transferred to the
  distilled model." Architecture: 8×2560 ReLU, 14k softmax outputs, ~85M params,
  ~2000 h / ~700M frames.

Soft targets as regularizer, Table 5 (S1, §6, p.7–8):
- Baseline, 100% of data: 63.4% train / 58.9% test frame accuracy.
- Baseline, 3% of data (~20M): 67.3% train / 44.5% test (severe overfitting).
- Soft targets, 3% of data: 65.4% train / 57.0% test — "recover almost all the
  information in the full training set (about 2% shy)," no early stopping.

Fidelity (S2) — CANDIDATE CHART SERIES (test top-1 agreement, student↔teacher):
- LeNet-5 → LeNet-5, MNIST (self-distillation, enough data): >99% (Fig. 2, p.4).
- ResNet-56 ensemble → ResNet-56, CIFAR-100, MixUp(τ=4): 86.0% (Fig. 3, p.7).
- ResNet-56 ensemble → ResNet-56, CIFAR-100, Baseline crops+flips (τ=4): 84.5%
  (Fig. 3, p.7).
- ResNet-56 self-distillation, CIFAR-100, GAN-augmented: below 80% (Fig. 1, p.4).
- Data recycling best: ~85% (§5.2, p.7).
Optimization series (S2, train agreement, ResNet-20 self-distillation, §6.2):
- 300 epochs (SGD): 78.95%; 5k epochs (SGD): 83.3%. Adam: worse. Combined
  augmentations: ~60%.
- Table 1 test agreement: random init 77.174 (0.352) vs teacher init 77.098
  (0.238) — indistinguishable.

Follow-ons:
- DistilBERT (S3): 40% smaller, 60% faster, 97% of GLUE.
- Born-Again (S4): DenseNet CIFAR-100 15.5% val error (abstract headline);
  identical-capacity student beats teacher.
- Beyer (S8): up to ~9600 epochs; ResNet-50 ImageNet 82.8% top-1.

## Source assets
- **S1, Table 1 (speech).** Three rows (baseline / 10×ensemble / distilled) — a
  clean three-column table in prose is better than a screenshot; the numbers are
  short. Recommend a rebuilt `nb-table`, not an asset capture.
- **S2, Figure 1 / Figure 2 (fidelity vs dataset size).** The visual contrast
  (LeNet reaching ~99%, ResNet plateauing) is the paper's headline image but is
  a multi-panel plot with GAN-augmentation x-axes that need explanation. Better
  rebuilt as a focused `nb chart` bar of test top-1 agreement across the three
  cleanest settings (LeNet/MNIST 99, ResNet MixUp τ=4 86, ResNet baseline τ=4
  84.5), which isolates the article's claim. Recommend chart over asset.
- No other asset is worth a capture; the equations belong in KaTeX furniture,
  not images.

## Discarded
- ACM DL landing for Buciluǎ 2006 (https://dl.acm.org/doi/10.1145/1150402.1150464):
  returns HTTP 403 to automated fetch (gated, not dead). Use the author's
  cs.cornell.edu PDF, which resolves 200 and carries the same paper.
- Hinton's specialist-models / JFT sections (S1 §5) and mixtures-of-experts
  (§7): real but tangential to the temperature/soft-target claim this article
  reconstructs; leave out to keep the piece continuous.
- Popular secondary explainers of distillation (blog posts, survey papers):
  not needed — a paper reconstruction argues from the primaries, and none change
  the interpretation the way S2, S5, and S8 do.
