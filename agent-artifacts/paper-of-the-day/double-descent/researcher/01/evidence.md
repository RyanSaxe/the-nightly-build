# Evidence record: paper-of-the-day/double-descent (01)

The evidence strongly supports the article's core reconstruction. Both primaries were
read in full from their arXiv PDFs. Belkin et al. (2019) own the "double descent" risk
curve: a schematic (Fig. 1) and empirical curves for random Fourier features, fully
connected nets, random forests, and boosting, with the interpolation threshold placed at
model capacity = sample size and a min-norm/smoothness mechanism posited for the second
descent. Nakkiran et al. (2019) own the deep-network extension: model-wise, epoch-wise,
and sample-wise double descent, unified by "effective model complexity" (EMC), with the
peak located where EMC ≈ n and the effect strongest under label noise. The after-record
is genuine and cuts against the "ubiquity" framing on two fronts, both read as their own
primaries: Curth, Jeffares & van der Schaar (NeurIPS 2023) argue the *classical-ML*
double descent in Belkin is largely an artifact of plotting one parameter-count x-axis
that silently switches complexity mechanisms at the threshold; Nakkiran, Venkat, Kakade &
Ma (ICLR 2021) prove and show empirically that optimally-tuned L2 regularization removes
or mitigates the peak.

Eight distinct sources are recorded, clearing the paper template's 8-source floor with
interpretation-changing material rather than padding. The record is thin in two places the
writer should respect. (1) Exact figure numbers differ between the freely-readable arXiv
version (used for `nb asset`) and the canonical PNAS version; this is documented below and
matters for locators. (2) Four supporting primaries (Zhang et al. 2017; Hastie et al.
2019/2022; Mei & Montanari 2019; Spigler et al. 2018) were read at abstract + owned-claim
level only, not in full; cite them only for the claim recorded here.

The single most important limitation of the whole record: double descent as "a curve in
the number of parameters" is **contingent, not a law**. Its appearance and the location
of the peak depend on the choice of complexity axis (Curth), on regularization (Nakkiran
et al. 2020), and on label noise / model misspecification (Nakkiran et al. 2019, by their
own account). The steelman-both-sides requirement is live: the effect is real and
reproducible, but its strongest original claim — ubiquity across model families as an
extension of the classical U-curve — is exactly what the after-record contests.

---

## Sources

```text
URL:         https://arxiv.org/abs/1812.11118  (PDF: https://arxiv.org/pdf/1812.11118)
             Canonical published version: https://doi.org/10.1073/pnas.1903070116
Kind:        primary — the paper owns the "double descent" curve, its experiments, and
             its posited mechanism. It is the focal paper.
Establishes: The double descent risk curve (Fig. 1); empirical double descent for random
             Fourier features on MNIST (Fig. 2), fully connected nets (arXiv Fig. 4),
             random forests (arXiv Fig. 5), and L2-boosting (arXiv Fig. 12); the
             interpolation threshold at capacity = n (and n·K for K-class nets); the
             min-norm / function-smoothness (Occam) mechanism for the second descent;
             Theorem 1 (noiseless approximation bound favoring small-norm interpolants).
Paraphrase:  Classical bias-variance predicts a U-shaped test-risk curve with a "sweet
             spot" and overfitting beyond it. Belkin et al. show that once capacity passes
             the interpolation threshold (where the model can exactly fit the training
             data), test risk peaks and then descends *again*, often below the classical
             sweet spot. Among the infinitely many interpolating solutions available past
             the threshold, the learning procedure implicitly picks the smoothest
             (smallest-norm) one; larger classes contain lower-norm interpolants, so risk
             keeps falling. They present this across RFF, ReLU random features, fully
             connected nets, random forests, and boosting.
Locators:    Abstract (PDF p1); U-curve corollary quote (PDF p2); Fig. 1 + threshold
             definition (PDF p3); RFF setup and N=n threshold (PDF p4); Fig. 2 (PDF p5);
             mechanism / norm argument (PDF p6); neural nets and n·K rule (PDF p7);
             Fig. 4 (PDF p8); Fig. 5 (PDF p9); trees/ensembles (PDF p9-10); "Historical
             absence" and "Inductive bias" (PDF p10-11); Theorem 1 (PDF p14).
Quote:       "the double descent risk curve ... incorporates the U-shaped risk curve (i.e.,
             the 'classical' regime) together with the observed behavior from using high
             capacity function classes (i.e., the 'modern' interpolating regime), separated
             by the interpolation threshold. The predictors to the right of the
             interpolation threshold have zero training risk." (Fig. 1 caption, PDF p3)
             Textbook view they overturn: "a model with zero training error is overfit to
             the training data and will typically generalize poorly" (Hastie-Tibshirani-
             Friedman, quoted PDF p2).
Note:        TITLE DISCREPANCY. The arXiv PDF is titled "Reconciling modern machine
             learning practice and the bias-variance trade-off" (authors listed as
             Belkin[a], Hsu[b], Ma[a], Mandal[a]; a = The Ohio State University, Columbus,
             OH; b = Columbia University, New York, NY; dated Sept 12, 2019, v2). The
             canonical PNAS title (verified via Crossref) is "Reconciling modern
             machine-learning practice and the classical bias-variance trade-off," PNAS
             vol. 116, no. 32, pp. 15849-15854, published 2019-08-06. Use the PNAS title
             for the abstract card; the abstract text is identical in both. The PNAS DOI
             returns HTTP 403 to automated fetches (publisher bot-gating) but resolves in
             a browser; the arXiv version is fully open and is what `nb asset` should pull.
```

```text
URL:         https://arxiv.org/abs/1912.02292  (PDF: https://arxiv.org/pdf/1912.02292)
Kind:        primary — owns the deep-network double descent results and the EMC framework.
             This is the second focal paper (deep-network extension).
Establishes: Model-wise, epoch-wise, and sample-wise double descent in modern deep nets
             (ResNets, CNNs, Transformers); the Effective Model Complexity (EMC)
             definition (Def. 1); the Generalized Double Descent hypothesis (Hyp. 1); that
             the peak sits at the critical regime EMC ≈ n; that "more data can hurt";
             that the effect is strongest under label noise but appears without it; and
             that early stopping usually suppresses it.
Paraphrase:  Belkin's parameter-count curve is a special case. Define EMC as the largest
             training-set size on which a training procedure reaches ~0 training error.
             Double descent occurs as a function of EMC, so it shows up along model size,
             along training epochs (epoch-wise), and along dataset size (sample-wise).
             Near EMC ≈ n the interpolating solution is unique and noise-sensitive, so
             test error peaks; past it, many interpolants exist and SGD finds one that
             absorbs noise while generalizing. Because the peak sits where EMC matches n,
             adding data can shift the peak onto a fixed model and *raise* its error.
Locators:    Abstract (PDF p1); Fig. 1 (PDF p1); Fig. 2 model×epoch grid (PDF p2); Fig. 3
             sample-wise Transformer (PDF p3); EMC Definition 1 and Hypothesis 1 (PDF p3);
             ε = 0.1 heuristic (PDF p3); model-wise section + Fig. 4 (PDF p5); noise-
             sensitivity intuition (PDF p5-6); epoch-wise + Fig. 9 (PDF p7); sample-wise +
             Fig. 11 (PDF p8); Remarks on Label Noise (PDF p8, and Discussion PDF p9);
             experimental setup / architectures (PDF p4, Appendix B PDF p13-15).
Quote:       "Under-parameterized regime. If EMC(T) is sufficiently smaller than n, any
             perturbation of T that increases its effective complexity will decrease the
             test error. Over-parameterized regime. If EMC(T) is sufficiently larger than
             n, any perturbation ... will decrease the test error. Critically parameterized
             regime. If EMC(T) ≈ n, then a perturbation ... might decrease or increase the
             test error." (Hypothesis 1, PDF p3)
             On label noise: "we observe double descent most strongly in settings with
             label noise. However, we believe this effect is not fundamentally about label
             noise, but rather about model mis-specification." (PDF p8)
Note:        Authors: Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang (Harvard);
             Boaz Barak (Harvard); Ilya Sutskever (OpenAI). Kaplun/Bansal marked equal
             contribution; Nakkiran's work partly done interning at OpenAI. arXiv v1
             4 Dec 2019; published at ICLR 2020. They explicitly credit Belkin for naming
             double descent and Christopher Olah for suggesting the model-size × epoch
             visualization (Fig. 2).
```

```text
URL:         https://arxiv.org/abs/2310.18988  (PDF: https://arxiv.org/pdf/2310.18988)
Kind:        primary — the authors own this critique and its re-analysis/experiments. It
             is a secondary commentary *on* Belkin, but a primary source for its own claim.
Establishes: That the double descent observed by Belkin in trees, gradient boosting, and
             linear (RFF) regression is explained by an implicit switch between two
             distinct complexity axes at the interpolation threshold, not by an inherent
             property of interpolation; that the second descent's location is therefore
             not intrinsically tied to p = n; and that an effective-parameter measure folds
             the curves back into classical convex (U/L) shapes.
Paraphrase:  Reproducing Belkin's non-deep experiments, Curth et al. show each x-axis
             secretly concatenates two mechanisms. For trees, capacity is first grown by
             leaves (P_leaf, capped at ~n) and then, past the cap, by ensembling more full-
             depth trees (P_ens) — i.e. the model silently becomes a random forest exactly
             at the peak. Holding one axis fixed, error is convex in the other (U/L-shaped);
             double descent appears only at the hand-off, and the peak can be moved or
             removed by choosing when to switch. The same holds for boosting (P_boost then
             P_ens). For linear regression with RFF the min-norm solution used past p = n
             performs an implicit unsupervised dimensionality reduction, again a second
             mechanism. A generalized effective-parameter count is not increasing in the
             interpolation regime, so the apparent second ascent-then-descent disappears.
Locators:    Abstract (PDF p1); Fig. 1 unfolding schematic (PDF p2); Contributions (PDF
             p2); trees re-analysis + Fig. 2 (PDF p3); "shifting/removing the peak" Fig. 3
             (PDF p3-4); boosting + Fig. 4 (PDF p4); linear-regression deep dive (PDF p4-5).
Quote:       "the second descent appears exactly (and only) when and where the transition
             between these underlying axes occurs, and ... its location is thus not
             inherently tied to the interpolation threshold p = n." (Abstract, PDF p1)
Note:        Authors: Alicia Curth, Alan Jeffares (equal contribution), Mihaela van der
             Schaar (University of Cambridge). NeurIPS 2023. IMPORTANT SCOPE: this critique
             targets Belkin's *classical / non-deep* evidence; it does not refute Nakkiran
             et al.'s deep-network (ResNet/CNN/Transformer) double descent. A fair
             treatment must not let it read as a refutation of deep double descent.
             Curth cites Belkin's trees experiment as "[BHMM19]'s Fig. 4" and the RFF/
             linear experiment as "Fig. 2" — PNAS numbering (see figure-numbering note in
             Source assets).
```

```text
URL:         https://arxiv.org/abs/2003.01897  (PDF: https://arxiv.org/pdf/2003.01897)
Kind:        primary — owns its theorems and experiments on regularization vs. double
             descent. (Secondary commentary on the phenomenon; primary for its own result.)
Establishes: That optimally-tuned L2 (ridge) regularization can make test risk monotonic
             in both sample size and model size for isotropic linear regression (proved),
             and empirically mitigates double descent for random-feature classifiers and
             CNNs; plus a counterexample showing optimal ridge is not always sample-
             monotonic.
Paraphrase:  Double descent is largely a phenomenon of unregularized or under-regularized
             models. For well-specified linear regression with isotropic covariates,
             optimally-tuned ridge regression is provably sample-wise monotone (Theorem 1)
             and, for a random-projection model, model-wise monotone (Theorem 3) — "more
             data never hurts" and "bigger is never worse" once λ is tuned. Empirically,
             adding optimal weight decay flattens the double-descent peak for 5-layer CNNs
             on CIFAR-100. The optimal λ varies with model size, so no single value works
             everywhere; and for non-Gaussian, heteroscedastic data optimal ridge can still
             be non-monotonic.
Locators:    Abstract (PDF p1); Fig. 1 ridge monotonicity (PDF p2); contributions +
             Theorems 1 and 3 (PDF p3); counterexample caveat (PDF p4); experiments Sec. 5,
             random features Fig. 3, CNN Fig. 4 (PDF p13-14).
Quote:       "we prove that for certain linear regression models with isotropic data
             distribution, optimally-tuned L2 regularization achieves monotonic test
             performance as we grow either the sample size or the model size. We also
             demonstrate empirically that optimally-tuned L2 regularization can mitigate
             double descent for more general models, including neural networks." (Abstract)
             "the double descent phenomenon is largely observed for unregularized or
             under-regularized models in practice." (PDF p2)
Note:        Authors: Preetum Nakkiran, Prayaag Venkat (Harvard); Sham Kakade (Microsoft
             Research & University of Washington); Tengyu Ma (Stanford). arXiv v2 29 Apr
             2021; published at ICLR 2021. Shares lead author with the Deep Double Descent
             paper, so it is a self-qualification, not an outside attack — worth noting.
```

```text
URL:         https://arxiv.org/abs/1611.03530
Kind:        primary for its own finding (secondary as background here). Read at abstract +
             owned-claim level only, not in full.
Establishes: That state-of-the-art CNNs trained with SGD can perfectly fit random labels
             (and even random-noise inputs), and that depth-two nets have perfect finite-
             sample expressivity once parameters exceed data points — the capacity puzzle
             that motivates both focal papers.
Paraphrase:  Large nets can memorize arbitrary labelings, so their capacity vastly exceeds
             the training set; explicit regularization barely changes this. This is the
             empirical fact that makes the classical overfitting story inadequate and sets
             up why interpolating models needed a new account.
Locators:    Abstract.
Quote:       "state-of-the-art convolutional networks for image classification trained with
             stochastic gradient methods easily fit a random labeling of the training data.
             This phenomenon is qualitatively unaffected by explicit regularization, and
             occurs even if we replace the true images by completely unstructured random
             noise." (Abstract)
Note:        Authors: Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol
             Vinyals. ICLR 2017. Cited by both focal papers. Cite only for the random-label
             capacity claim unless the writer opens it further.
```

```text
URL:         https://arxiv.org/abs/1903.08560
Kind:        primary for its own theory (secondary as background here). Read at abstract +
             owned-claim level only, not in full.
Establishes: A precise, quantitative recovery of the double-descent risk curve for minimum-
             L2-norm ("ridgeless") interpolation in high-dimensional least squares, for
             both a linear feature model and a random one-layer-network (nonlinear) feature
             model — i.e. rigorous theory behind Belkin's empirical linear/RFF curves.
Paraphrase:  Studying ridgeless interpolation as dimension and sample size grow together,
             the paper reproduces double descent and the benefit of overparametrization in
             closed form, giving the theoretical backbone Belkin's linear experiments lack.
Locators:    Abstract.
Quote:       "We recover -- in a precise quantitative way -- several phenomena that have
             been observed in large-scale neural networks and kernel machines, including
             the 'double descent' behavior of the prediction risk, and the potential
             benefits of overparametrization." (Abstract)
Note:        Authors: Trevor Hastie, Andrea Montanari, Saharon Rosset, Ryan J. Tibshirani.
             arXiv 2019; later published in Annals of Statistics, 2022 (venue not re-
             verified against the journal record — treat the journal citation as approximate
             and cite the arXiv version). Cited by Nakkiran et al. for the misspecification
             point. Read only at abstract level.
```

```text
URL:         https://arxiv.org/abs/1908.05355
Kind:        primary for its own theory (secondary as background here). Read at abstract +
             owned-claim level only, not in full.
Establishes: The first analytically tractable model that captures the full double descent
             curve — precise asymptotics of the test error for ridge regression on N random
             features σ(w^T x) (a two-layer net with random first layer) in the limit
             N,n,d → ∞ with N/d, n/d fixed — and, notably, does so WITHOUT assuming any ad
             hoc misspecification structure.
Paraphrase:  Gives the closed-form theory behind Belkin's empirical RFF curve and shows the
             global test-error minimum sits well above the interpolation threshold, in the
             heavily overparameterized regime.
Locators:    Abstract.
Quote:       "the first analytically tractable model that captures all the features of the
             double descent phenomenon without assuming ad hoc misspecification structures."
             (Abstract)
Note:        Authors: Song Mei, Andrea Montanari. arXiv 2019 (later Communications on Pure
             and Applied Mathematics, 2022 — journal not re-verified; cite arXiv). Cited by
             Nakkiran et al. Its "no misspecification needed" result is in tension with
             Nakkiran's framing (see Contradictions). Read only at abstract level.
```

```text
URL:         https://arxiv.org/abs/1810.09665
Kind:        primary for its own finding (secondary as background here). Read at abstract +
             owned-claim level only, not in full.
Establishes: An independent, pre-Belkin observation of the interpolation-threshold cusp:
             in fully connected nets with hinge loss, a sharp "jamming" phase transition
             separates under- and over-parameterized regimes, and the generalization error
             shows three phases — decay, rise to a cusp at the transition, then slow decay.
Paraphrase:  Corroborates that the test-error peak at the interpolation threshold is not an
             artifact of one paper's setup; it was found from a statistical-physics angle,
             supporting Belkin's "not an aberration" and "historical absence" points.
Locators:    Abstract.
Quote:       "the generalization error displays three phases: (i) initial decay, (ii)
             increase until the transition point --- where it displays a cusp --- and (iii)
             slow decay toward a constant for the rest of the over-parametrized regime."
             (Abstract)
Note:        Authors: Stefano Spigler, Mario Geiger, Stéphane d'Ascoli, Levent Sagun, Giulio
             Biroli, Matthieu Wyart. Published in J. Phys. A: Math. Theor. (DOI
             10.1088/1751-8121/ab4c8b). Cited by both Belkin (ref [37], the "jamming"
             connection) and Nakkiran. Read only at abstract level.
```

---

## Contradictions

- **"Ubiquity" across model families vs. an x-axis artifact.** Belkin et al. present double
  descent as a general phenomenon spanning RFF, neural nets, random forests, and boosting
  (PDF p1, p7-10). Curth et al. (2023) reproduce the tree, boosting, and linear cases and
  argue the second descent there appears *only* at the point where the experiment switches
  its complexity mechanism (leaves → ensembles; boosting rounds → ensembles; least-squares
  → min-norm interpolation), and that with an effective-parameter axis the curves fold back
  to convex U/L shapes. Their claim: the peak's location is "not inherently tied to the
  interpolation threshold p = n" (2310.18988, Abstract). This directly qualifies Belkin's
  classical-ML evidence and the framing that double descent *extends* the U-curve.

- **Scope limit on that critique.** Curth et al. explicitly confine their re-analysis to
  non-deep methods and do not overturn Nakkiran et al.'s deep-network results. So the
  contradiction narrows Belkin's ubiquity claim without touching model-wise/epoch-wise
  double descent in ResNets, CNNs, and Transformers. Reported honestly, this is a partial
  contradiction, not a refutation of the phenomenon.

- **The peak depends on regularization.** Belkin frames the second descent as a property
  of increasing capacity under a small-norm inductive bias. Nakkiran, Venkat, Kakade & Ma
  (2021) show that optimally-tuned ridge regularization *removes* the peak (provably for
  isotropic linear regression; empirically for CNNs on CIFAR-100). Belkin himself notes in
  "Historical absence" that regularization "can both prevent interpolation and change the
  effective capacity ... attenuating or masking the interpolation peak" (1812.11118 PDF
  p10) — so the two are compatible, but the after-record makes the dependence sharp: double
  descent is mostly a story about under-regularized training.

- **The peak depends on label noise.** Nakkiran et al. observe all forms of double descent
  "most strongly in settings with label noise" (1912.02292 PDF p8), and Belkin's own
  cleanest empirical curves (RFF/MNIST) are on real-label data. This is not a flat
  contradiction — Nakkiran also shows peaks without label noise (ResNets/CNNs on CIFAR-100,
  Transformers on IWSLT'14) and attributes the effect to model misspecification — but it
  complicates any claim that the peak is a fixed feature of interpolation independent of the
  data's noise level. The honest reading: label noise amplifies and sharpens the peak; it
  is not strictly necessary.

- **Sample size: abstract vs. figure.** Nakkiran's abstract says "even quadrupling" the
  number of samples can hurt (4×); the underlying Fig. 3 / Sec. 7 example is 4k → 18k
  samples, a factor of 4.5. Use 4.5× when citing Fig. 3, "quadrupling"/4× when quoting the
  abstract; do not conflate them into a single invented figure.

- **What drives the peak: misspecification vs. nothing extra.** Nakkiran et al. argue the
  peak "is not fundamentally about label noise, but rather about model mis-specification"
  (1912.02292 PDF p8). Mei & Montanari (2019) cut against this by exhibiting the full double
  descent curve in random-features ridge regression "without assuming ad hoc
  misspecification structures" (1908.05355 Abstract) — i.e. the peak arises from the
  variance of the min-norm interpolant alone, no misspecification required. The two are
  reconcilable (label noise and misspecification both amplify the peak; neither is strictly
  necessary) but the writer should not present "it's about misspecification" as settled.

No further contradiction found after checking the theoretical after-record (Hastie et al.
2019 and Spigler et al. 2018 corroborate rather than contradict; d'Ascoli et al. 2020
extend it to "triple descent," noted in optreg PDF p5 but not read here).

---

## Numbers

```text
Figure: Interpolation threshold for RFF on MNIST at N = n = 10^4 features (n = 10^4
        training examples, 10 classes)
Owner:  Belkin et al. 2019 (1812.11118), Fig. 2 + text PDF p4-5
Scope:  MNIST subset, n = 10^4; N = number of random Fourier features; squared-loss ERM,
        min-L2-norm coefficients when N > n
```
```text
Figure: Interpolation threshold for a K-class fully connected net at n·K parameters
        (Fig. 4: MNIST, n = 4·10^3, d = 784, K = 10 → threshold at 40,000 params;
        param count = (d+1)·H + (H+1)·K for H hidden units)
Owner:  Belkin et al. 2019, Fig. 4 + text PDF p7-8
Scope:  MNIST subset n = 4,000; single hidden layer of H units; SGD, weight-reuse below
        threshold and random init above
```
```text
Figure: 1-D Random ReLU fit, coefficient-norm drop: N = 40 features → norm ≈ 695;
        N = 4000 features → norm ≈ 159 (fitting the same 10 points)
Owner:  Belkin et al. 2019, Fig. 3 (arXiv) + caption PDF p6
Scope:  10 data points, univariate; illustrates larger class → smaller-norm interpolant
```
```text
Figure: EMC threshold parameter ε = 0.1 (heuristic; "≈ 0 training error" cutoff)
Owner:  Nakkiran et al. 2019 (1912.02292), Def. 1 + text PDF p3
Scope:  Used throughout to locate EMC(T) = n
```
```text
Figure: CIFAR-10 label noise levels: 15% (Figs. 1, 2), 20% (Figs. 9, 12); Fig. 4 sweeps
        0-20%. Standard ResNet18 = width 64; widths scaled as [k,2k,4k,8k]
Owner:  Nakkiran et al. 2019, captions + Appendix B PDF p1-2, p5, p7, p13
Scope:  Model-wise curves; label noise fixed once, not resampled per epoch
```
```text
Figure: 5-layer CNN at width k = 64 has 1,558,026 parameters and >90% CIFAR-10 test
        accuracy with data augmentation
Owner:  Nakkiran et al. 2019, Appendix B.1 PDF p13
Scope:  Reference point for CNN model-size axis
```
```text
Figure: Sample-wise "more data hurts": 4× (abstract, "quadrupling") / 4.5× (Fig. 3, 4k→18k
        samples) more data raises Transformer test loss for a fixed model size
Owner:  Nakkiran et al. 2019, Abstract, Fig. 3, Sec. 7 PDF p1, p3, p8
Scope:  IWSLT'14 German→English, per-token perplexity; embedding dimension d_model as
        model-size axis
```
```text
Figure: Training regimes — Adam LR 1e-4 for 4K epochs (ResNets/CNNs) or SGD LR ∝ 1/√T for
        500K gradient steps; Transformers 80K gradient steps, 10% label smoothing.
        IWSLT'14 de-en = 160K sentences; WMT'14 en-fr subsampled to 200K
Owner:  Nakkiran et al. 2019, Sec. 4 + Fig. 8 PDF p4-5, p7
Scope:  Experimental setup underlying all deep curves
```
```text
Figure: Optimal-ridge monotonicity demo: d = 500, σ = 0.5, ||β*||_2 = 1; unregularized
        ridge non-monotonic in n, optimal-λ ridge monotonic
Owner:  Nakkiran, Venkat, Kakade & Ma 2021 (2003.01897), Fig. 1 + Theorem 1 PDF p2-3
Scope:  Well-specified isotropic Gaussian linear regression; λ_opt independent of n here
```
```text
Figure: Curth et al. reproduction uses MNIST with n_train = 10,000 (matching Belkin);
        second descent shown to coincide with the P_leaf→P_ens (trees) and P_boost→P_ens
        (boosting) axis switch, movable/removable by choosing the switch point
Owner:  Curth et al. 2023 (2310.18988), Figs. 2-4 + text PDF p3-4
Scope:  Non-deep methods only (trees, gradient boosting, RFF linear regression)
```

---

## Source assets

FIGURE-NUMBERING WARNING (read before capturing any Belkin figure). The freely-readable
arXiv PDF (arxiv.org/pdf/1812.11118), which `nb asset` should pull, numbers figures:
Fig. 1 schematic, Fig. 2 RFF/MNIST, Fig. 3 1-D ReLU, Fig. 4 fully connected net, Fig. 5
random forests. The canonical PNAS version renumbers (Curth cites the trees experiment as
PNAS "Fig. 4" and the RFF experiment as "Fig. 2"): PNAS keeps Fig. 1 and Fig. 2 identical
but the fully connected net becomes PNAS Fig. 3 and random forests PNAS Fig. 4, with the
1-D ReLU panel demoted to the SI. Fig. 1 and Fig. 2 are stable across both versions (these
are the two the commission names). For any other Belkin figure, cite the arXiv number in
`data-nb-locator` and pull from the arXiv PDF page listed below.

```text
Asset: Belkin Fig. 1 — the double descent schematic. arXiv PDF p3.
       URL: https://arxiv.org/pdf/1812.11118 (page 3). Stable in PNAS as Fig. 1.
Shows: (a) the classical U-shaped risk curve; (b) the double descent curve with the
       "classical" under-parameterized regime, the interpolation threshold peak, and the
       "modern" interpolating regime where test risk descends a second time. Training risk
       (dashed) hits zero at and past the threshold.
Crop:  Keep both panels together, or at minimum panel (b) with all three labels
       ("classical"/"modern" regimes and "interpolation threshold") and both curves. Do
       not crop out the training-risk line — the zero-training-risk region is the point.
```
```text
Asset: Belkin Fig. 2 — RFF double descent on MNIST. arXiv PDF p5.
       URL: https://arxiv.org/pdf/1812.11118 (page 5). Stable in PNAS as Fig. 2.
Shows: Test risk (log scale), coefficient L2 norm (log scale), and training risk vs. number
       of random Fourier features N, with the peak at N = n = 10^4 and a second descent
       below the classical sweet spot; the kernel min-norm solution h_{n,∞} beats every
       finite-N RFF predictor. The norm curve peaking at N = n is the mechanism evidence.
Crop:  Retain the x-axis (N in units of 10^3), the interpolation marker at N = 10^4, and at
       least the test-risk and coefficient-norm panels together so the norm-peak coincides
       visibly with the risk peak. The h_{n,∞} reference line should stay.
```
```text
Asset: Belkin Fig. 4 (arXiv) / Fig. 3 (PNAS) — fully connected net double descent on MNIST.
       arXiv PDF p8. URL: https://arxiv.org/pdf/1812.11118 (page 8).
Shows: Train/test risk vs. number of parameters for a single-hidden-layer net; the
       interpolation threshold (black dotted line) at n·K = 40,000 params, peak there, then
       second descent. This is the bridge from kernel/feature models to real nets.
Crop:  Keep the dotted threshold line and its position relative to the peak; keep both zero-
       one and squared-loss panels if space allows, else the zero-one panel.
```
```text
Asset: Nakkiran Fig. 1 — model-wise (left) and epoch-wise (right) double descent.
       arXiv PDF p1. URL: https://arxiv.org/pdf/1912.02292 (page 1).
Shows: Left: train/test error vs. ResNet18 width on CIFAR-10 with 15% label noise — the
       clean model-wise peak at the interpolation width. Right: test error vs. train
       epochs — the same shape in time. One figure establishes two of the three axes.
Crop:  Keep both panels; retain the width axis labels (up to width 64 = standard ResNet18)
       and the label-noise annotation.
```
```text
Asset: Nakkiran Fig. 2 — the Model Size × Epoch heatmap. arXiv PDF p2.
       URL: https://arxiv.org/pdf/1912.02292 (page 2).
Shows: Test error over the 2-D grid of model size and training epochs, with the high-error
       ridge running along the interpolation contour; horizontal slice = model-wise DD,
       vertical slice = epoch-wise DD. This is the figure that unifies the phenomenon under
       EMC (the visualization Olah suggested). Strongest single asset for the "EMC" section.
Crop:  Keep the full grid and the ridge; do not crop to a single slice — the point is that
       both slices are cross-sections of one surface.
```
```text
Asset: Nakkiran Fig. 4 — model-wise DD vs. label noise. arXiv PDF p5.
       URL: https://arxiv.org/pdf/1912.02292 (page 5).
Shows: (a) ResNet18 on CIFAR-100: a test-error peak even with NO label noise; (b) ResNet18
       on CIFAR-10: a "plateau" at the interpolation point with no noise that grows into a
       peak as label noise is added. This is the figure for the label-noise-dependence
       argument — it shows both that noise sharpens the peak and that the peak survives
       without noise.
Crop:  Keep both panels and all the noise-level curves; the no-noise vs. added-noise
       contrast is the evidence.
```
```text
Asset: Nakkiran Fig. 3 — sample-wise non-monotonicity (Transformers). arXiv PDF p3.
       URL: https://arxiv.org/pdf/1912.02292 (page 3).
Shows: Test loss vs. Transformer model size for 4k vs. 18k training samples on IWSLT'14;
       the 18k curve is lower overall but shifted right, so for a band of model sizes 18k
       (4.5×) samples give worse test loss than 4k. The concrete "more data hurts" case.
Crop:  Keep both sample-size curves and the overlapping model-size region where they cross.
```
```text
Asset: Curth Fig. 2 — decomposing double descent in trees. arXiv PDF p3.
       URL: https://arxiv.org/pdf/2310.18988 (page 3).
Shows: Left: reproduction of Belkin's tree double descent. Center: error vs. P_leaf at
       fixed P_ens — a plain U/L curve. Right: error vs. P_ens at fixed P_leaf — a plain L
       curve. The composite peak exists only at the hand-off between the two axes. The core
       asset for the "it may be an artifact of the x-axis" counter-argument.
Crop:  Keep all three panels side by side; the argument is the contrast between the composite
       (left) and the two single-axis curves (center, right).
```
```text
Asset: optreg Fig. 1 — optimal regularization removes the peak. arXiv PDF p2.
       URL: https://arxiv.org/pdf/2003.01897 (page 2).
Shows: Test risk vs. number of samples for isotropic ridge regression (d = 500):
       unregularized regression is non-monotonic (a sample-wise double-descent spike),
       optimally-regularized (λ = λ_opt) is monotone. Cleanest asset for the "regularization
       dependence" contradiction.
Crop:  Keep both the unregularized and optimal-λ curves on the same axes; the divergence is
       the point.
```

Optional supporting asset: optreg Fig. 4 (CNN on CIFAR-100, arXiv PDF p14) shows the same
regularization effect for a real network; use only if the article spends the CNN case.

---

## Discarded

```text
URL: https://ar5iv.labs.arxiv.org/abs/1812.11118 — used only to orient; superseded by
     reading the arXiv PDF directly. Its auto-generated figure summary was unreliable on
     exact figure numbers (it invented a "Fig. 3 = RFF" and mislabeled several appendix
     figures), so nothing from it is relied upon. Not a citable source.
```
```text
URL: https://www.pnas.org/doi/10.1073/pnas.1903070116 — the canonical published version,
     but it returns HTTP 403 to automated fetches (publisher bot-gating). Verified its
     bibliographic record via Crossref instead; recorded as the canonical citation for the
     abstract card. Content read from the open arXiv version, which is textually identical.
```
```text
d'Ascoli et al. 2020 ("triple descent," noted in optreg PDF p5) and Mei & Montanari 2019
     (random-features asymptotics) — not opened in full; mentioned only as after-record
     context. Do not cite beyond noting they exist unless opened.
```
