# Evidence record: paper-of-the-day/generative-adversarial-networks (01)

The evidence supports the commissioned angle in full: elegant theory, messy
practice, and a principled after-record diagnosis, not a debunking. The focal
paper (Goodfellow et al. 2014) is read firsthand for its four load-bearing
artifacts: the minimax value function (Eq. 1), the optimal discriminator
D*_G(x) = p_data/(p_data+p_g) (Prop. 1), the global-optimum theorem reducing the
criterion to a Jensen-Shannon divergence with minimum −log 4 at p_g = p_data
(Thm. 1, Eqs. 5-6), and Algorithm 1's alternating minibatch SGD. Crucially, the
paper *itself* records the theory-practice gap the commission wants: it names the
saturation of log(1−D(G(z))) early in training and substitutes the non-saturating
heuristic (maximize log D(G(z))) in Section 3, and its convergence proof (Prop. 2)
is explicit that it assumes optimization in function space with the discriminator
trained to its optimum in the inner loop, assumptions parameter-space alternating
SGD does not meet. The after-record adjudicates the gap: Arjovsky & Bottou (2017)
prove that when p_data and p_g sit on non-aligned low-dimensional manifolds the JS
divergence is constant at log 2 and the generator gradient vanishes (Thms. 2.1-2.4),
and that the very non-saturating heuristic the original paper adopts optimizes
KL(p_g‖p_data) − 2·JSD with infinite-variance gradients (Thms. 2.5-2.6); Wasserstein
GAN (2017) proposes the Earth-Mover distance as the principled fix, continuous and
differentiable where JS is not (Example 1, Thm. 1).

Where the record is thin, and where it complicates the angle: the "JS vanishing
gradient" story is not the last word. Fedus et al. (2018), with Goodfellow himself
a co-author, gives empirical counterexamples where GANs learn distributions the
divergence-minimization view predicts they cannot, arguing that framing is "overly
restrictive." Mescheder et al. (2018) shows WGAN and WGAN-GP with a finite number
of critic steps do not always converge, and Gulrajani et al. (2017) shows WGAN's own
weight-clipping fix "can lead to undesired behavior." So the honest shape is: the
diagnosis located a real failure of the JS objective, the WGAN fix was itself
quickly patched, and the divergence-minimization lens the diagnosis assumes has been
contested by later theory. The focal paper's weakest claim is its *evaluation* (Parzen
window log-likelihood, which the paper itself flags as poor and high-variance in high
dimensions), not its theory. Equation and theorem numbers below are read from the
ar5iv HTML rendering; the writer should confirm the exact printed numbers against
the arXiv source captured with `nb asset`, since camera-ready numbering can differ.

## Sources

```text
URL:         https://arxiv.org/abs/1406.2661
Kind:        primary — the focal paper; it owns the minimax framework, the optimal
             discriminator, the JS reduction, and Algorithm 1. Authoring party with
             full stake in the claims.
Establishes: The GAN framework and its complete theoretical result, plus the
             paper's own acknowledgment of the training-practice gap.
Paraphrase:  Two networks play a minimax game: D estimates the probability a sample
             is real; G maps noise z~p_z to samples and is trained to fool D. For G
             fixed, the optimal discriminator is D*_G(x) = p_data(x)/(p_data(x)+p_g(x))
             (Prop. 1). Substituting D* into the value function gives a virtual
             criterion C(G) whose global minimum is −log 4, attained iff p_g = p_data,
             at which point the criterion equals −log 4 + 2·JSD(p_data‖p_g) (Thm. 1).
             The convergence guarantee (Prop. 2) holds "if G and D have enough
             capacity" and the discriminator "is allowed to reach its optimum given
             G" — i.e. in function space with an optimal inner loop, not the
             parameter-space alternating SGD actually run. Section 3 records that
             early in training log(1−D(G(z))) saturates and substitutes the
             non-saturating heuristic (train G to maximize log D(G(z))).
Locators:    Value function Eq. (1), Section 3 "Adversarial nets". Non-saturating
             heuristic: Section 3, paragraph after Eq. (1). Prop. 1 / optimal D:
             Section 4.1, Eq. (2). Integral form of V(G,D): Eq. (3). C(G)=max_D V:
             Eq. (4). KL form: Eq. (5). JSD form −log4+2·JSD: Eq. (6), Thm. 1,
             Section 4.1. Convergence: Prop. 2, Section 4.2. Algorithm 1: Section 3.
             Fig. 1: Section 3. Fig. 2 samples + Table 1: Section 5 "Experiments".
Quote:       Eq. (1): "min_G max_D V(D,G) = E_{x~p_data(x)}[log D(x)] +
             E_{z~p_z(z)}[log(1 − D(G(z)))]".
             Non-saturating heuristic: "In practice, equation 1 may not provide
             sufficient gradient for G to learn well. Early in learning, when G is
             poor, D can reject samples with high confidence because they are clearly
             different from the training data. In this case, log(1 − D(G(z)))
             saturates. Rather than training G to minimize log(1 − D(G(z))) we can
             train G to maximize log D(G(z))."
             Prop. 1: "For G fixed, the optimal discriminator D is
             D*_G(x) = p_data(x) / (p_data(x) + p_g(x))."
             Thm. 1: "The global minimum of the virtual training criterion C(G) is
             achieved if and only if p_g = p_data. At that point, C(G) achieves the
             value − log 4."

Note on title: The arXiv record titles this "Generative Adversarial Networks"; the
NeurIPS/NIPS 2014 proceedings title is "Generative Adversarial Nets." Authors, in
order: Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David
Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio. The paper card should
carry the venue title and this author order.
```

```text
URL:         https://arxiv.org/abs/1701.04862
Kind:        primary — Arjovsky & Bottou own the diagnosis; they derive and prove the
             instability results firsthand.
Establishes: Why the JS-based objective fails in the early-training regime, and why
             the non-saturating heuristic the original paper adopts is itself
             pathological. This is the after-record's analytical core; WGAN is its
             constructive companion.
Paraphrase:  A neural-net generator maps a lower-dimensional z into a high-dimensional
             space, so p_g is supported on a set of measure zero (Lemma 1); p_data is
             believed to lie on a low-dimensional manifold too. When two such supports
             are disjoint, or are manifolds that do not "perfectly align," a perfect
             discriminator exists with zero gradient on the supports (Thms. 2.1, 2.2),
             the JS divergence equals log 2 and both KL divergences are +∞ (Thm. 2.3).
             Consequently, as D approaches optimal, the generator gradient through the
             original minimax loss is bounded by M·ε/(1−ε) and goes to zero (Thm. 2.4,
             Cor. 2.1) — the vanishing-gradient failure. The non-saturating −log D
             alternative does not vanish but is unstable: its expected gradient equals
             ∇_θ[KL(p_g‖p_data) − 2·JSD(p_g‖p_data)], an objective that pushes the KL
             the wrong way and *subtracts* the JS (Thm. 2.5), and each coordinate of
             the update is a centered Cauchy with infinite mean and variance (Thm. 2.6).
Locators:    Manifold/measure-zero: Lemma 1, Section 2. Perfect discriminator:
             Thms. 2.1-2.2, Section 2.1. JSD = log 2: Thm. 2.3, Section 2.1. Vanishing
             gradient: Thm. 2.4 + Cor. 2.1, Section 2.2.1. Non-saturating cost
             identity: Thm. 2.5, Section 2.2.2. Infinite-variance/Cauchy gradient:
             Thm. 2.6, Section 2.2.2. (Page numbers from the ar5iv rendering are
             approximate; section locations are reliable.)
Quote:       Thm. 2.4 bound: "‖∇_θ E_z[log(1 − D(g_θ(z)))]‖_2 < M ε/(1 − ε)".
             Cor. 2.1: "lim_{‖D−D*‖→0} ∇_θ E_z[log(1 − D(g_θ(z)))] = 0".
             Thm. 2.5: "E_z[−∇_θ log D*(g_θ(z))|_{θ=θ0}] =
             ∇_θ[KL(P_{g_θ}‖P_r) − 2 JSD(P_{g_θ}‖P_r)]|_{θ=θ0}".
```

```text
URL:         https://arxiv.org/abs/1701.07875
Kind:        primary — Arjovsky, Chintala & Bottou own the Wasserstein GAN proposal
             and its distance-theory results.
Establishes: The constructive fix: a distance that stays continuous and differentiable
             where JS does not, and a training algorithm (the "critic") that follows it.
Paraphrase:  The Earth-Mover (Wasserstein-1) distance is the infimum over couplings of
             expected transport cost (Eq. 1). Example 1 (two parallel lines) makes the
             gap concrete: for P_0 on {0}×[0,1] and P_θ on {θ}×[0,1], W(P_0,P_θ)=|θ|
             (smooth in θ), while JS jumps to log 2 for every θ≠0 and KL is +∞ — so JS
             and KL give no usable gradient as θ→0, exactly the barely-overlapping
             regime of Arjovsky & Bottou. W is continuous everywhere and differentiable
             a.e. under a local-Lipschitz condition (Thm. 1), and its topology is
             weaker than JS/KL/TV, so it converges in strictly more cases (Thm. 2).
             Kantorovich-Rubinstein duality turns W into a supremum over 1-Lipschitz
             functions (Eq. 2), approximated by a "critic" network f_w; the Lipschitz
             constraint is enforced by clipping critic weights to [−c, c]. Algorithm 1
             runs n_critic critic steps per generator step with RMSProp.
Locators:    W definition: Eq. (1), Section 2. Example 1 + the JS/KL/W comparison:
             Section 2 (Fig. 1 caption). Continuity/differentiability: Thm. 1,
             Section 2. Weaker-topology: Thm. 2, Section 2. Duality: Eq. (2),
             Section 3. Algorithm 1 (weight clip c=0.01, n_critic=5, α=0.00005,
             m=64, RMSProp): Section 3.
Quote:       Example 1 values: "W(P_0,P_θ)=|θ|; JS(P_0,P_θ)= log 2 if θ≠0, 0 if θ=0;
             KL(P_θ‖P_0)=+∞ if θ≠0, 0 if θ=0." Fig. 1 caption: "The EM plot is
             continuous and provides a usable gradient everywhere. The JS plot is not
             continuous and does not provide a usable gradient."
```

```text
URL:         https://arxiv.org/abs/1710.08446
Kind:        primary — Fedus, Rosca, Lakshminarayanan, Dai, Mohamed, Goodfellow own
             the empirical counterexamples. This is the strongest complication of the
             commission's angle, and Goodfellow (the focal author) is a co-author.
Establishes: That the divergence-minimization lens the WGAN diagnosis rests on is not
             the full story: GANs learn distributions where that lens predicts failure.
Paraphrase:  GANs "do not minimize a single training criterion"; they seek a Nash
             equilibrium in a two-player game. The paper argues that treating a
             divergence as "the primary guide for the learning process," with every
             step required to decrease it, is "overly restrictive." Empirically, the
             discriminator supplies useful signal precisely in cases where the
             divergence gradients would be useless, and GANs learn distributions the
             divergence-minimization view predicts they would fail on. Gradient
             penalties motivated by the divergence view help even where that view does
             not predict they should. GAN training is better read as approaching Nash
             equilibria along trajectories that need not decrease any fixed divergence.
Locators:    Central claims: abstract and Introduction. Empirical counterexamples: main
             body (submitted Oct 2017, rev. Feb 2018; presented at ICLR 2018).
Quote:       "We show that this view is overly restrictive. During GAN training, the
             discriminator provides learning signal in situations where the gradients
             of the divergences between distributions would not be useful. ... we
             demonstrate that GANs are able to learn distributions in situations where
             the divergence minimization point of view predicts they would fail."
```

```text
URL:         https://arxiv.org/abs/1801.04406
Kind:        primary — Mescheder, Geiger & Nowozin own the convergence analysis.
Establishes: That WGAN's fix is not a clean resolution: WGAN and WGAN-GP with finite
             critic steps do not always converge; the manifold/absolute-continuity
             issue is the real driver, and simple gradient penalties (not Wasserstein)
             restore local convergence.
Paraphrase:  Local convergence of GAN training had been shown for absolutely
             continuous distributions; this paper proves that absolute continuity is
             *necessary*, giving a prototypical counterexample where unregularized GAN
             training does not converge for non-absolutely-continuous distributions
             (the realistic manifold case). Instance noise and zero-centered gradient
             penalties converge; Wasserstein-GAN and WGAN-GP "with a finite number of
             discriminator updates per generator update do not always converge to the
             equilibrium point." Simplified gradient penalties give provable local
             convergence even when data and model lie on lower-dimensional manifolds.
Locators:    Abstract; counterexample and convergence theorems in the body. ICML 2018.
Quote:       "we show that Wasserstein-GANs and WGAN-GP with a finite number of
             discriminator updates per generator update do not always converge to the
             equilibrium point."
```

```text
URL:         https://arxiv.org/abs/1704.00028
Kind:        primary — Gulrajani, Ahmed, Arjovsky, Dumoulin & Courville (Arjovsky again)
             own the critique of weight clipping and the gradient-penalty replacement.
Establishes: That WGAN's own Lipschitz-enforcement mechanism was flawed and needed a
             follow-on fix within months — evidence the "principled fix" was itself
             provisional.
Paraphrase:  WGAN improves stability but "sometimes can still generate only low-quality
             samples or fail to converge." The authors trace this to weight clipping,
             which "can lead to undesired behavior" (pathological weight distributions,
             wasted critic capacity, exploding/vanishing gradients), and replace it with
             a penalty on the norm of the critic's gradient with respect to its input
             (WGAN-GP), enabling stable training across architectures including
             101-layer ResNets with little tuning.
Locators:    Abstract; weight-clipping analysis and gradient penalty in the body.
             NIPS 2017.
Quote:       "We find that these problems are often due to the use of weight clipping
             in WGAN to enforce a Lipschitz constraint on the critic, which can lead
             to undesired behavior."
```

```text
URL:         https://arxiv.org/abs/1606.03498
Kind:        primary — Salimans, Goodfellow, Zaremba, Cheung, Radford & Chen own the
             mode-collapse characterization and the minibatch-discrimination remedy.
Establishes: The practical failure the theorem does not predict — mode collapse — from
             a credible source authored in part by Goodfellow himself, plus the
             Inception score metric later work uses.
Paraphrase:  A characteristic GAN failure is collapse: the generator maps many z to a
             single point the discriminator currently rates highly, and once this
             happens the discriminator's gradient points in similar directions for many
             points, so training cannot recover the correct entropy. Minibatch
             discrimination lets D look at a batch jointly to penalize this. The paper
             introduces the Inception score, exp(E_x KL(p(y|x)‖p(y))), as an automatic
             image-quality metric.
Locators:    Mode collapse + minibatch discrimination: Section 3.2. Inception score:
             Section 4. Visual Turing test numbers: Section 6.
Quote:       "When collapse to a single mode is imminent, the gradient of the
             discriminator may point in similar directions for many similar points."
```

```text
URL:         https://arxiv.org/abs/1511.06434
Kind:        primary — Radford, Metz & Chintala own the DCGAN architecture and results.
Establishes: That GANs became reliably trainable for image generation within ~18
             months of the 2014 paper — the "GANs worked and reshaped generative
             modeling" premise the commission requires, so the piece is not a debunking.
Paraphrase:  A class of CNN GANs (DCGANs) with specific architectural constraints
             trains stably and learns a hierarchy of representations from object parts
             to scenes in both generator and discriminator; the learned features
             transfer as general image representations. This is the practical
             breakthrough that made GANs usable and launched the image-generation line.
Locators:    Abstract; architecture guidelines and representation experiments in the
             body. ICLR 2016.
Quote:       "we show convincing evidence that our deep convolutional adversarial pair
             learns a hierarchy of representations from object parts to scenes in both
             the generator and the discriminator."
```

## Contradictions

- **Does later theory defend the original JS objective against the WGAN diagnosis?**
  Yes, partially, and this is the sharpest tension in the record. The WGAN
  after-record (Arjovsky & Bottou; Arjovsky, Chintala & Bottou) frames GAN training
  as divergence minimization and locates the failure in the JS divergence. Fedus et
  al. (2018) — with Goodfellow a co-author — directly disputes that frame, showing
  empirically that GANs learn distributions the divergence-minimization view predicts
  they cannot, and calling the "decrease a divergence at every step" view "overly
  restrictive." The two are not reconcilable as a single clean narrative: the writer
  should present the WGAN diagnosis as *a* principled account of instability, then
  note that the divergence lens it assumes was itself contested by the focal paper's
  own lead author within a year.

- **Is WGAN a clean fix?** No. Gulrajani et al. (2017) shows WGAN's weight clipping
  "can lead to undesired behavior" and replaces it (WGAN-GP) months later; Mescheder
  et al. (2018) shows both WGAN and WGAN-GP with finite critic steps do not always
  converge, and that the decisive stabilizer is a gradient penalty, not the Wasserstein
  distance per se. The "principled fix" was provisional and partially superseded.

- **What the original paper claims vs. what it proves.** No internal contradiction,
  but a precise gap the piece turns on: the paper's convergence result (Prop. 2)
  assumes function-space optimization with the inner discriminator at its optimum; the
  paper *itself* then abandons the analyzed minimax loss for the non-saturating
  heuristic in practice (Section 3). The theorem and the training loop are about
  different objects, and the paper says so. This is honest limitation-recording by the
  authors, not a flaw the after-record exposed.

- **Non-saturating loss framing.** The commission's shorthand is "JS gives vanishing
  gradient." That is exact only for the *original minimax* loss (Thm. 2.4). For the
  non-saturating loss the paper actually uses, Arjovsky & Bottou's result is different
  and arguably worse: not a vanishing gradient but an unstable, infinite-variance one
  optimizing KL − 2·JSD (Thms. 2.5-2.6). The writer must not collapse these two into
  one claim.

## Numbers

```text
Figure: −log 4  (≈ −1.386)
Owner:  Goodfellow et al. 2014, Thm. 1, Eq. (6)
Scope:  Value of the virtual training criterion C(G) at the global optimum p_g=p_data;
        equals −log 4 + 2·JSD(p_data‖p_g) with JSD=0 at the optimum. Dimensionless.
```

```text
Figure: D*(x) = 1/2 everywhere at the optimum
Owner:  Goodfellow et al. 2014, Prop. 1 / abstract
Scope:  Value of the optimal discriminator when p_g=p_data; follows from
        D*=p_data/(p_data+p_g) with p_g=p_data.
```

```text
Figure: JS(P_0,P_θ) = log 2 (≈ 0.693) for all θ≠0
Owner:  Arjovsky, Chintala & Bottou 2017, Example 1
Scope:  JS divergence between two parallel-line distributions offset by θ; constant in
        θ (zero gradient) while W(P_0,P_θ)=|θ| is smooth. Dimensionless.
```

```text
Figure: Generator gradient bound ‖∇_θ E[log(1−D(g_θ(z)))]‖_2 < M·ε/(1−ε) → 0
Owner:  Arjovsky & Bottou 2017, Thm. 2.4 / Cor. 2.1
Scope:  As discriminator error ε=‖D−D*‖→0; M a constant. Shows vanishing generator
        gradient in the barely-overlapping-support regime.
```

```text
Figure: Parzen-window log-likelihood — MNIST 225 ± 2 ; TFD 2057 ± 26
Owner:  Goodfellow et al. 2014, Table 1, Section 5
Scope:  Estimated test-set log-likelihood via Gaussian Parzen window (σ chosen on a
        validation set). The paper itself calls this estimator high-variance and a poor
        fit in high dimensions; treat as the paper's *weakest* quantitative evidence,
        not a headline number. Units: nats (log-likelihood). Confirm the exact figures
        against Table 1 in the captured source before printing.
```

```text
Figure: Visual Turing test — MNIST samples distinguished from real in 52.4% of trials
        (chance 50%); CIFAR-10 human error rate 21.3%
Owner:  Salimans et al. 2016, Section 6 (abstract for the 21.3%)
Scope:  Human evaluation of DCGAN-style samples with the paper's improved techniques;
        evidence GANs reached near-photo-realism, supporting the "GANs worked" premise.
        Not focal-paper numbers; use only as after-record context if the piece needs a
        realism datapoint.
```

## Source assets

```text
Asset: Figure 1 — the four-panel schematic (a)-(d), Section 3 "Adversarial nets".
Shows: The whole theorem in one picture. Two horizontal lines (lower = z domain,
       upper = x domain) with G mapping z→x; the black dotted curve is p_data, the
       green solid curve is p_g, the blue dashed curve is the discriminator D. Across
       (a)→(d) p_g slides onto p_data and D flattens to 1/2 everywhere — the visual of
       D*=p_data/(p_data+p_g) driven to the −log 4 optimum. This is the single best
       artifact for teaching Prop. 1 and Thm. 1 together.
Crop:  Keep all four labeled panels (a)-(d) and the color/line-style legend (data vs.
       p_g vs. D); the argument is the progression, so do not crop to a single panel.
       Retain the two-domain arrows (z→x mapping). The caption's fine print can be
       trimmed since the article's own caption will carry the reading.
```

```text
Asset: Algorithm 1 — "Minibatch stochastic gradient descent training of generative
       adversarial nets", Section 3.
Shows: The gap the piece turns on made concrete: an outer loop, k inner discriminator
       ascent steps on (1/m)Σ[log D(x_i) + log(1−D(G(z_i)))], then a single generator
       descent step on (1/m)Σ log(1−D(G(z_i))). The paper notes k=1 is used ("the least
       expensive option"), so the "inner loop trained to optimality" the theorem assumes
       is not what the algorithm does — the source of the theory-practice gap.
Crop:  Capture the full boxed pseudocode including the "for k steps" line, both gradient
       expressions, and the footnote/remark naming the k value. Do not crop out the
       generator-update line; the asymmetry between k discriminator steps and one
       generator step is the point.
```

```text
Asset: Figure 2 — sample grids (MNIST, TFD, CIFAR-10 fully-connected and convolutional),
       Section 5 "Experiments". Rightmost column = nearest training neighbor of the
       adjacent sample.
Shows: What the 2014 model could actually produce, and the memorization check: the
       rightmost yellow-boxed column is the nearest real training example, evidence the
       samples are not memorized. Useful to set reader expectations (blurry 2014 samples)
       against the DCGAN leap the after-record context describes.
Crop:  If space is tight, one or two dataset panels suffice, but each must retain its
       rightmost nearest-neighbor column and its border marker, or the memorization
       point is lost. Keep the per-panel dataset labels.
```

## Discarded

```text
URL: https://arxiv.org/pdf/1804.00140  — "GANs: What it can generate and what it cannot"
     survey surfaced in search; secondary, not needed to meet the count or change the
     interpretation; the primary after-record papers cover the same ground firsthand.
URL: https://arxiv.org/abs/1611.02163  — Metz et al. "Unrolled GANs" considered for the
     inner-loop-to-optimality point, but Algorithm 1 plus Prop. 2 in the focal paper and
     Mescheder et al. already carry that argument; adding it would pad, not change the
     reading.
```
