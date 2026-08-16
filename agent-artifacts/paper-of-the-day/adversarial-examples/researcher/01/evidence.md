# Evidence: paper-of-the-day/adversarial-examples (01)

This record supports a full reconstruction of Goodfellow, Shlens, and Szegedy,
"Explaining and Harnessing Adversarial Examples" (ICLR 2015, arXiv:1412.6572),
verified against the paper's own PDF: the linear explanation and its
dimension-growth expression, the fast gradient sign method, the Figure 1
panda-to-gibbon panel with all three labels and confidences, and the adversarial
training objective with its results. It also supports weighing the linear claim
against the decade that followed: Szegedy et al. 2013 (the phenomenon and its
original framing), Madry et al. 2018 (PGD adversarial training as the durable
baseline), Athalye et al. 2018 and Carlini and Wagner 2017 (weak evaluations and
broken defenses), Ilyas et al. 2019 (non-robust features), Tsipras et al. 2019
(the robustness-accuracy tension), and the current state via RobustBench and the
present leaderboard leader. The evidence is strong on everything the paper prints
and everything the follow-on abstracts and headline tables state. It is thinner
in two places, both recorded below: the focal paper's equations carry no printed
numbers, so cite by section, and the RobustBench live leaderboard is a moving
artifact, so the single current-best figure is anchored to a dated paper (Wang
et al. 2023) rather than to a leaderboard read that will drift. One load-bearing
notational point about the linear-explanation perturbation is flagged in Numbers
so the writer reproduces the growth term correctly.

## Sources

```text
URL:         https://arxiv.org/abs/1412.6572
Kind:        primary — the focal paper; owns the linear explanation, FGSM,
             Figure 1, and the adversarial training objective. It is secondary
             where it characterizes Szegedy et al. 2013's explanation.
Establishes: The central claim that the primary cause of adversarial
             vulnerability is the linear nature of models in high dimensions,
             not nonlinearity or overfitting; the FGSM attack; adversarial
             training as a regularizer; the cross-model generalization argument.
Paraphrase:  A per-feature perturbation too small to exceed sensor precision
             (max-norm bounded by epsilon) can still move a linear unit's
             pre-activation by an amount that scales with input dimension,
             because the worst-case perturbation aligns with the sign of the
             weights. Neural nets built from piecewise-linear units (ReLU,
             maxout, LSTM) inherit this, so a single linearized step, FGSM,
             reliably fools them. Training on FGSM examples mixed with clean
             ones regularizes and partly hardens the model. Because independently
             trained models learn similar weights, the same perturbation
             transfers between them, which linearity explains and nonlinearity
             does not.
Locators:    Abstract; Sec. 1 Introduction; Sec. 3 "The Linear Explanation of
             Adversarial Examples"; Sec. 4 "Linear Perturbation of Non-Linear
             Models" (FGSM, Figure 1); Sec. 6 (adversarial training objective and
             MNIST results); Sec. 8 "Why Do Adversarial Examples Generalize?"
             (verified against the arXiv PDF, v3, 20 Mar 2015).
Quote:       Sec. 3: "Consider the dot product between a weight vector w and an
             adversarial example x-tilde: w^T x-tilde = w^T x + w^T eta. The
             adversarial perturbation causes the activation to grow by w^T eta.
             We can maximize this increase subject to the max norm constraint on
             eta by assigning eta = sign(w). If w has n dimensions and the
             average magnitude of an element of the weight vector is m, then the
             activation will grow by epsilon*m*n."
             Sec. 4: "We can linearize the cost function around the current value
             of theta, obtaining an optimal max-norm constrained pertubation of
             eta = epsilon sign(grad_x J(theta, x, y)). We refer to this as the
             'fast gradient sign method' of generating adversarial examples."
```

```text
URL:         https://arxiv.org/abs/1312.6199
Kind:        primary — Szegedy, Zaremba, Sutskever, Bruna, Erhan, Goodfellow,
             Fergus, "Intriguing properties of neural networks." Owns the
             discovery of adversarial examples and its original explanation.
Establishes: Firsthand that adversarial examples exist, are found by a
             box-constrained L-BFGS optimization, are imperceptible, and transfer
             across models trained on disjoint subsets. Firsthand its own
             explanation: the mapping is "fairly discontinuous," and the examples
             sit in "low-probability pockets" in the manifold. This is the record
             against which the focal paper's "early attempts focused on
             nonlinearity and overfitting" framing must be checked.
Paraphrase:  The authors minimize the norm of a perturbation r subject to the
             perturbed input being classified as a chosen target label and
             staying in the valid pixel box. They report that the same
             perturbation fools networks of different depth trained on different
             data subsets. Their offered explanation is that learned input-output
             maps are discontinuous and that adversarial inputs occupy rare,
             hard-to-sample pockets, and that the smoothness assumption behind
             kernel methods does not hold.
Locators:    Abstract; Sec. 4 "Blind Spots in Neural Networks" (pockets,
             smoothness); Sec. 4.1 (L-BFGS objective: minimize ||r||_2 subject to
             f(x+r)=l and x+r in [0,1]^m); Sec. 4.2 (cross-model, cross-subset
             transfer).
Quote:       Sec. 4: "adversarial examples represent low-probability
             (high-dimensional) 'pockets' in the manifold, which are hard to
             efficiently find by simply randomly sampling"; and "The smoothness
             assumption that underlies many kernel methods does not hold."
```

```text
URL:         https://arxiv.org/abs/1706.06083
Kind:        primary — Madry, Makelov, Schmidt, Tsipras, Vladu, "Towards Deep
             Learning Models Resistant to Adversarial Attacks" (ICLR 2018). Owns
             the robust-optimization framing and the PGD adversarial-training
             baseline.
Establishes: Firsthand the min-max (saddle-point) view of robust training and
             projected gradient descent as a strong, multi-step "universal
             first-order adversary," with the durable robust-accuracy numbers
             that FGSM training could not reach.
Paraphrase:  Robust training is cast as minimizing the expected worst-case loss
             inside an epsilon L-infinity ball, with PGD (many gradient steps
             with projection, unlike FGSM's single step) solving the inner
             maximization. A network trained against PGD becomes robust to a wide
             range of attacks, which single-step FGSM training does not achieve.
Locators:    Abstract; Sec. 2.1, Eq. (2.1) (the saddle-point objective); Sec. 3.2
             (PGD as universal first-order adversary); Sec. 4 / Tables 1-2
             (MNIST and CIFAR-10 robust accuracies).
Quote:       Abstract: "Our best MNIST model achieves an accuracy of more than
             89% against the strongest adversaries in our test suite"; the CIFAR-10
             model "achieves an accuracy of 46% against the same adversary."
             Eq. (2.1): min_theta rho(theta), where rho(theta) =
             E_{(x,y)~D}[ max_{delta in S} L(theta, x+delta, y) ].
```

```text
URL:         https://arxiv.org/abs/1802.00420
Kind:        primary — Athalye, Carlini, Wagner, "Obfuscated Gradients Give a
             False Sense of Security" (ICML 2018, best paper). Owns the
             obfuscated-gradients diagnosis and the attacks that break it.
Establishes: Firsthand that most defenses accepted at ICLR 2018 gave only the
             appearance of robustness by masking gradients, and fell to adapted
             attacks. This is the record that later work confirming FGSM/attacks
             are cheap also shows most defenses were illusory.
Paraphrase:  The authors name obfuscated gradients as a common failure in which a
             defense breaks gradient-based attacks without being robust. They
             identify three kinds (shattered, stochastic, and exploding/vanishing
             gradients) and build attacks for each, including a backward-pass
             differentiable approximation. In a case study of nine non-certified
             white-box defenses, seven relied on the effect; they circumvent six
             fully and one partially in each paper's own threat model.
Locators:    Abstract (7-of-9 and 6-complete-1-partial counts); Sec. 3 (the three
             gradient types, verified: shattered, stochastic, vanishing/exploding);
             Sec. 4.1 (BPDA, verified); body case study of nine ICLR 2018 defenses.
Quote:       Abstract: "we find obfuscated gradients are a common occurrence, with
             7 of 9 defenses relying on obfuscated gradients. Our new attacks
             successfully circumvent 6 completely, and 1 partially, in the
             original threat model each paper considers."
```

```text
URL:         https://arxiv.org/abs/1608.04644
Kind:        primary — Carlini, Wagner, "Towards Evaluating the Robustness of
             Neural Networks" (IEEE S&P 2017). Owns the C&W attacks and the
             breaking of defensive distillation.
Establishes: Firsthand that a defense reported to cut attack success from 95% to
             0.5% (defensive distillation) provides essentially no real
             robustness once the attack is adapted, and that strong optimization
             attacks find adversarial examples with 100% success.
Paraphrase:  The authors build three attacks tuned to the L0, L2, and L-infinity
             metrics and show they find adversarial examples with 100% success on
             both distilled and undistilled networks, so defensive distillation
             does not meaningfully raise robustness. The lesson generalizes: a
             defense must be measured against an attack adapted to it.
Locators:    Abstract; attack sections (three norms); defensive-distillation
             evaluation. The 95%-to-0.5% claim and the 100% success figure are in
             the abstract.
Quote:       Abstract: defensive distillation reduces "the success rate of
             current attacks' ability to find adversarial examples from 95% to
             0.5%," yet the three new attacks succeed "on both distilled and
             undistilled neural networks with 100% probability."
```

```text
URL:         https://arxiv.org/abs/1905.02175
Kind:        primary — Ilyas, Santurkar, Tsipras, Engstrom, Tran, Madry,
             "Adversarial Examples Are Not Bugs, They Are Features" (NeurIPS
             2019). Owns the non-robust-features reframing.
Establishes: Firsthand that adversarial examples can be attributed to
             non-robust features that are genuinely predictive of the label yet
             brittle and human-incomprehensible, reframing the cause from a model
             artifact to a property of the data. This directly reweights the
             focal paper's "flaw in training" framing while confirming its
             transfer argument.
Paraphrase:  The authors separate a dataset into robust and non-robust feature
             content. Training a standard model on a dataset stripped to
             non-robust features, relabeled so the labels track only those
             features, still generalizes to the real test set, which shows the
             features are real signal, not noise. Because independently trained
             models pick up the same non-robust features, adversarial
             perturbations transfer between them.
Locators:    Abstract; Sec. 3.1 (robustified dataset); Sec. 3.2 / Table 1
             (non-robust datasets and their test accuracy on the original set);
             Sec. 3.3 (transfer explanation).
Quote:       Abstract: "adversarial examples can be directly attributed to the
             presence of non-robust features: features derived from patterns in
             the data distribution that are highly predictive, yet brittle and
             incomprehensible to humans." Sec. 3.3: "different classifiers trained
             on independent samples from that distribution are likely to utilize
             similar non-robust features."
```

```text
URL:         https://arxiv.org/abs/1805.12152
Kind:        primary — Tsipras, Santurkar, Engstrom, Turner, Madry, "Robustness
             May Be at Odds with Accuracy" (ICLR 2019). Owns the
             robustness-accuracy tension result.
Establishes: Firsthand that standard accuracy and adversarial robustness can be
             provably in tension in a simple setting, and that robust models
             learn different, more human-aligned features. This contradicts the
             focal paper's hope that adversarial training is a pure regularizer
             that also improves clean accuracy.
Paraphrase:  In a simple, natural binary task the authors construct, any
             classifier with high standard accuracy must have low robust
             accuracy, so the two goals trade off rather than reinforce. The same
             pattern appears empirically in harder settings. A side effect is that
             robust models' loss gradients align better with human perception.
Locators:    Abstract; the theoretical construction (simple binary task, provable
             trade-off); the feature-alignment discussion.
Quote:       Abstract: "We demonstrate that this trade-off between the standard
             accuracy of a model and its robustness to adversarial perturbations
             provably exists in a fairly simple and natural setting."
```

```text
URL:         https://arxiv.org/abs/2010.09670
Kind:        primary — Croce, Andriushchenko, Sehwag, Debenedetti, Flammarion,
             Chiang, Mittal, Hein, "RobustBench: a standardized adversarial
             robustness benchmark" (NeurIPS 2021 Datasets and Benchmarks Track).
             Owns the standardized evaluation and thresholds.
Establishes: Firsthand that robustness evaluation is error-prone and overstates
             defenses, that a standardized AutoAttack-based benchmark fixes the
             comparison, and the fixed threat models the field now reports
             against. It is the citable methodology behind any "where robustness
             stands" number.
Paraphrase:  The benchmark evaluates a restricted class of models with
             AutoAttack, an ensemble of white- and black-box attacks, to curb the
             robustness overestimation that adaptive-attack studies keep exposing.
             It standardizes on fixed L-infinity and L2 thresholds and maintains a
             live leaderboard across CIFAR-10, CIFAR-100, and ImageNet.
Locators:    Abstract; the threat-model definitions (CIFAR-10 L-infinity
             eps = 8/255 and L2 eps = 0.5, evaluated with AutoAttack). The
             specific top-of-leaderboard number is not in the paper; see Wang et
             al. 2023 below and the note in Numbers.
Quote:       Abstract: "its evaluation is often error-prone leading to robustness
             overestimation ... We evaluate adversarial robustness with
             AutoAttack, an ensemble of white- and black-box attacks."
```

```text
URL:         https://arxiv.org/abs/2302.04638
Kind:        primary — Wang, Pang, Du, Lin, Liu, Yan, "Better Diffusion Models
             Further Improve Adversarial Training" (ICML 2023). Owns the
             current-best CIFAR-10 RobustBench L-infinity number cited here.
Establishes: Firsthand a concrete, dated anchor for where CIFAR-10 robustness
             stands: 70.69% robust accuracy at L-infinity eps = 8/255 under
             AutoAttack, using only diffusion-generated data, then top of
             RobustBench. Used here to pin the moving leaderboard to a checkable
             figure rather than a live read.
Paraphrase:  Replacing DDPM-generated training data with samples from a stronger
             diffusion model raises RobustBench CIFAR-10 robust accuracy to 70.69%
             at eps = 8/255 without any external dataset, improving the prior best
             by 4.58 points, with parallel gains on CIFAR-100 and the L2 setting.
Locators:    Abstract (the CIFAR-10 L-infinity 70.69% figure and the +4.58 delta).
Quote:       Abstract: "Under the l-infinity-norm threat model with eps=8/255, our
             models achieve 70.69% and 42.67% robust accuracy on CIFAR-10 and
             CIFAR-100, respectively, i.e. improving upon previous state-of-the-art
             models by +4.58% and +8.03%."
```

## Contradictions

- The focal paper's account of the prior explanation versus what Szegedy et al.
  2013 actually wrote. Goodfellow et al. open by saying "Early attempts at
  explaining this phenomenon focused on nonlinearity and overfitting" and cast
  their linear view against a "supposed highly non-linear nature" (Sec. 3). But
  Szegedy et al. 2013's own text does not rest on nonlinearity: it hypothesizes
  "low-probability ... 'pockets' in the manifold" and a "fairly discontinuous"
  mapping (Sec. 4). The focal paper is a secondary source for that framing, and
  its "nonlinearity" strawman is partly its own construction. The writer should
  state the original hypothesis in Szegedy's words, not only in Goodfellow's
  characterization of it.

- The pockets picture versus the linear picture. Szegedy 2013 casts adversarial
  examples as rare, precisely located pockets. Goodfellow et al. argue the
  opposite geometry: "adversarial examples occur in contiguous regions of the
  1-D subspace defined by the fast gradient sign method, not in fine pockets"
  (Sec. 8, Fig. 4). This is a direct, load-bearing disagreement, and the focal
  paper's abundance claim is what its transfer explanation rests on.

- Ilyas et al. 2019 reframes the cause and both confirms and undercuts the focal
  paper. It confirms transferability by the same mechanism Goodfellow invoked:
  independently trained models learn the same features, so perturbations carry
  across them. It undercuts the focal paper's framing that the vulnerability is a
  training "flaw" or "accidental steganography" to regularize away. Under Ilyas,
  the non-robust features are real predictive signal in the data, not a model
  artifact, so "regularize it out" is the wrong picture even though FGSM
  adversarial training does help.

- Tsipras et al. 2019 contradicts the focal paper's regularizer optimism.
  Goodfellow et al. report adversarial training lowering clean test error from
  0.94% to 0.84% (Sec. 6), reading robustness and accuracy as aligned. Tsipras
  et al. show a provable trade-off in a simple setting and the same pattern
  empirically in harder ones. On MNIST at small epsilon the tension is mild,
  which is why the focal paper saw a gain; at the scales the field now targets it
  is not.

- The focal paper's own results already qualify the harnessing claim, and later
  work confirms the qualification. Goodfellow et al. reduce FGSM adversarial
  error from 89.4% to 17.9% but note the model "when it does misclassify ... its
  predictions are unfortunately still highly confident," average confidence 81.4%
  (Sec. 6). Madry et al. 2018 later show single-step FGSM training is weak
  against multi-step PGD and make PGD training the durable baseline; Athalye et
  al. 2018 and Carlini and Wagner 2017 show most defenses that looked robust were
  not, once attacked properly. The cheapness and gradient-alignment the linear
  view predicted held up; the implied "and adversarial training largely fixes it"
  did not.

- Where the record confirms the focal paper. Perturbations are cheap and
  gradient-aligned (FGSM is one backprop step), they transfer between models, and
  FGSM plus adversarial training became the field's starting point. Athalye,
  Carlini and Wagner, Madry, and Ilyas all build on those three facts rather than
  dispute them. The linear explanation was right about the phenomenon's cheapness
  and transfer, and incomplete as a full account of the cause.

## Numbers

```text
Figure: activation growth = epsilon * m * n (max-norm-bounded perturbation of a
        linear unit; m = average magnitude of a weight element, n = input
        dimension)
Owner:  Goodfellow et al. 2015, Sec. 3
Scope:  Worst-case L-infinity perturbation, ||eta||_inf = epsilon. NOTE for the
        writer: the paper prints "eta = sign(w)" then states the growth is
        epsilon*m*n. The consistent reading is that the constraint-saturating
        perturbation is eta = epsilon * sign(w), each component +/- epsilon, so
        w^T eta = epsilon * sum_i |w_i| = epsilon * m * n. Reproduce it as
        epsilon * sign(w) with growth epsilon*m*n; the paper's "sign(w)" folds
        epsilon into the max-norm bound. The point: ||eta||_inf stays fixed at
        epsilon while the output change grows linearly in n.
```

```text
Figure: FGSM perturbation eta = epsilon * sign(grad_x J(theta, x, y))
Owner:  Goodfellow et al. 2015, Sec. 4 (equation is unnumbered; cite by section)
Scope:  One linearized step; sign gives the fastest cost increase under the
        L-infinity (max-norm) constraint because it puts every component at the
        constraint boundary in the ascending direction.
```

```text
Figure: Figure 1 (GoogLeNet / ImageNet): epsilon = 0.007; "panda" 57.7%
        confidence -> "gibbon" 99.3% confidence; middle (sign) panel labeled
        "nematode" 8.2% confidence
Owner:  Goodfellow et al. 2015, Figure 1, p. 3
Scope:  Single image, single model (GoogLeNet). epsilon = 0.007 is the magnitude
        of the smallest bit of an 8-bit image encoding after conversion to reals.
```

```text
Figure: FGSM error rates at generation time — MNIST epsilon=0.25: shallow softmax
        99.9% error at 79.3% avg confidence; maxout 89.4% error at 97.6%
        confidence. CIFAR-10 epsilon=0.1: convolutional maxout 87.15% error,
        96.6% avg probability on wrong label.
Owner:  Goodfellow et al. 2015, Sec. 4
Scope:  Test sets; MNIST pixels in [0,1]; CIFAR-10 preprocessed (std ~0.5).
```

```text
Figure: Adversarial training objective J-tilde(theta,x,y) =
        alpha * J(theta,x,y) + (1-alpha) * J(theta, x + epsilon*sign(grad_x
        J(theta,x,y))), with alpha = 0.5
Owner:  Goodfellow et al. 2015, Sec. 6 (equation unnumbered; cite by section)
Scope:  Maxout network with dropout on MNIST.
```

```text
Figure: Adversarial-training results (MNIST, maxout + dropout): clean test error
        0.94% -> 0.84%; larger 1600-unit model reaches 0.782% average (best on
        permutation-invariant MNIST at the time). FGSM adversarial error
        89.4% -> 17.9%; misclassified adversarial examples still 81.4% avg
        confidence.
Owner:  Goodfellow et al. 2015, Sec. 6
Scope:  MNIST test set; adversarial error measured against FGSM (single-step) at
        the model's training epsilon.
```

```text
Figure: Madry et al. 2018 robust accuracy — MNIST L-infinity epsilon=0.3: >89%
        (Table 1: 89.3% vs 100-step, 20-restart PGD). CIFAR-10 L-infinity
        epsilon=8/255: 46% in abstract (Table 2: 45.8% vs 20-step PGD).
Owner:  Madry et al. 2018, Abstract and Tables 1-2
Scope:  White-box PGD adversary; the durable baseline the focal paper's
        single-step FGSM training did not reach.
```

```text
Figure: Ilyas et al. 2019 (CIFAR-10) — standard model trained on non-robust
        feature datasets still generalizes to the real test set: D_rand 63.3%,
        D_det 43.7% test accuracy on the original CIFAR-10 test set. Robustified
        dataset yields ~48% robust accuracy via standard training.
Owner:  Ilyas et al. 2019, Sec. 3 / Table 1
Scope:  CIFAR-10; the 43.7-63.3% figures show the non-robust features are real
        predictive signal, well above chance (10%).
```

```text
Figure: Current CIFAR-10 robustness — RobustBench threat models: L-infinity
        epsilon=8/255 and L2 epsilon=0.5, evaluated with AutoAttack. Present
        leaderboard leader (Wang et al. 2023): 70.69% robust accuracy at
        L-infinity epsilon=8/255, diffusion-generated data only.
Owner:  Croce et al. 2020 (thresholds, AutoAttack); Wang et al. 2023 (the 70.69%
        figure)
Scope:  CIFAR-10. Anchor for scale: an undefended model sits near 0% robust
        accuracy under AutoAttack; Madry-style training reached ~46%; the current
        best is 70.69%, so a decade of work moved CIFAR-10 robust accuracy from
        near zero to about 71%, at large model and data cost, still far below
        clean accuracy. NOTE: 70.69% is a dated, checkable figure; the live
        leaderboard will move, so the writer should present it as "as of Wang et
        al. 2023 / then top of RobustBench," not as a permanent number.
```

## Source assets

```text
Asset: Figure 1, Goodfellow et al. 2015, p. 3 — the three-panel panda-to-gibbon
       demonstration on GoogLeNet.
Shows: An imperceptible, max-norm-bounded perturbation flips a confident correct
       classification to a confident wrong one. It settles the whole premise in
       one image: the change is invisible (epsilon = 0.007, one 8-bit level) and
       the model's confidence rises, from 57.7% on "panda" to 99.3% on "gibbon."
Crop:  A faithful crop must retain all three panels and their printed labels and
       confidences: left, the clean image x, "panda" 57.7%; middle, the sign
       image sign(grad_x J(theta,x,y)), "nematode" 8.2%; right, the adversarial
       image x + 0.007 * sign(...), "gibbon" 99.3%. Keep the "+ .007 x" and "="
       operators between panels and the per-panel expressions beneath them, since
       they carry the epsilon and the FGSM construction the caption depends on.
       Do not drop the middle panel: without it the reader cannot see that the
       perturbation is structured (sign of the gradient), not random noise.
```

```text
Asset: Figure 2, Goodfellow et al. 2015, p. 4 — logistic regression weights (a),
       the sign of the weights (b, the optimal perturbation), MNIST 3s and 7s
       (c), and their FGSM adversarial versions (d).
Shows: The exact case where FGSM is not an approximation but the truly worst-case
       max-norm perturbation. Panel (d) with epsilon=0.25 drives the logistic
       model from a 1.6% error rate on 3-vs-7 to 99%. Useful if the piece
       reconstructs the linear case concretely.
Crop:  If used, retain panels (b) and (d) at minimum, with the epsilon=0.25 and
       the 1.6%-to-99% error figures in the caption; (b) shows the perturbation
       is not human-recognizable as 3-vs-7 information.
```

```text
Asset: Figure 4, Goodfellow et al. 2015, Sec. 8 — the epsilon sweep along the
       FGSM direction.
Shows: Adversarial examples occupy contiguous regions of the 1-D FGSM subspace,
       not isolated pockets. This is the figure that carries the paper's
       disagreement with Szegedy 2013's pockets picture and grounds the
       transfer/abundance argument.
Crop:  Retain the axis showing classification as epsilon varies; the point is the
       wide contiguous misclassified band, so do not crop it to a single epsilon.
```

```text
Asset: Madry et al. 2018, Tables 1-2 (MNIST and CIFAR-10 accuracy vs attack
       strength).
Shows: The gap between single-step (FGSM) and multi-step (PGD) evaluation, and
       the robust-accuracy ceiling that adversarial training reaches. Supports
       the verdict that the focal paper's harnessing claim needed the stronger
       adversary to be tested honestly.
Crop:  A small extracted table, not the paper's image, is the honest form here
       (per house charts rule, a committed script if rendered). Numbers already
       recorded above.
```

## Discarded

```text
URL: https://robustbench.github.io/ — the live leaderboard page did not render
     its JavaScript table through the fetch tool, and a live read would drift
     anyway. Replaced by the citable RobustBench paper (arXiv:2010.09670) for
     methodology and thresholds, and by Wang et al. 2023 (arXiv:2302.04638) for a
     dated, checkable current-best number.
```

```text
URL: General web search results characterizing the leaderboard (e.g. secondary
     summaries quoting ~46% for older entries) — not opened as primaries; used
     only to locate the Wang et al. 2023 paper, then verified against that
     paper's own abstract. Not cited.
```
