# Evidence: paper-of-the-day/generative-adversarial-networks (researcher/01)

The evidence fully supports the commission's angle. The GAN paper (arXiv:1406.2661) itself
states, verbatim and in exact equation form, the value function, Proposition 1 (the optimal
discriminator D*_G(x) = p_data/(p_data+p_g)), Theorem 1 (global optimum at p_g = p_data,
value -log4, reducing to 2·JSD(p_data||p_g) - 2·log2), the non-saturating heuristic and its
stated reason (saturation of log(1-D(G(z))) early in training), the Parzen-window evaluation
with its own stated caveat, and — notably — the paper's own Section 6 names mode collapse
by the phrase "the Helvetica scenario" as a disadvantage the authors already anticipated.
This last point sharpens the commission's angle: the paper did not merely fail to foresee
mode collapse: it named the risk and moved on without a fix. WGAN's (1701.07875) diagnosis
of vanishing gradients is corroborated and made rigorous by its own cited precursor,
Arjovsky & Bottou's "Towards Principled Methods" (1701.04862), which supplies the actual
theorem (2.4) and disjoint-support lemma that WGAN's prose summarizes; researching both
closes a gap the brief did not anticipate. Lucic et al. (1711.10337) is unambiguous in its
abstract-level conclusion and supplies a comparable FID table. Diffusion-beats-GANs
(2105.05233) supplies exact, table-sourced FID comparisons. The evidence is thin only on: (a)
the original paper's disadvantages section is two sentences, not a developed treatment, so
the "instability" side of the argument leans on Salimans et al. 2016 and Goodfellow's own
2016 tutorial rather than the founding paper; (b) diffusion models' publication venue is not
stated on the arXiv abstract page, so the record does not claim a conference beyond "arXiv
preprint, submitted May 11 2021"; (c) CIFAR-10 in the founding paper was used only for
sample visualization, not for the Parzen-window number, and the paper gives no epoch/example
counts, so any claim about training scale must stay unstated rather than invented.

## Sources

### 1. Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville, Bengio,
"Generative Adversarial Nets," arXiv:1406.2661 (NIPS 2014)
URL: https://arxiv.org/abs/1406.2661 (full text read via https://ar5iv.labs.arxiv.org/html/1406.2661, arXiv's own HTML mirror of the same submission)
**Primary.** The paper owns every claim made about what it proves, states, and ran. All eight
authors are listed on the arXiv abstract page in this order: Ian J. Goodfellow, Jean
Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville,
Yoshua Bengio. Affiliation (paper header, all authors unless noted): Département
d'informatique et de recherche opérationnelle, Université de Montréal. Footnotes state: Jean
Pouget-Abadie was visiting Université de Montréal from École Polytechnique; Sherjil Ozair was
visiting from Indian Institute of Technology Delhi; Yoshua Bengio is a CIFAR Senior Fellow.
Submitted 10 June 2014 (v1).

What it establishes firsthand, with locators:
- **Value function (Eq. 1, Section 3, "Adversarial nets"):** "min_G max_D V(D,G) =
  E_{x~p_data(x)}[log D(x)] + E_{z~p_z(z)}[log(1-D(G(z)))]".
- **Proposition 1 (Section 4.1, "Global Optimality of p_g = p_data"):** "For G fixed, the
  optimal discriminator D is D*_G(x) = p_data(x)/(p_data(x)+p_g(x))."
- **Theorem 1 (Section 4.1):** "The global minimum of the virtual training criterion C(G) is
  achieved if and only if p_g = p_data. At that point, C(G) achieves the value -log4." Eq. 6
  gives the value as C(G) = -log(4) + 2·JSD(p_data‖p_g), i.e., the criterion reduces to twice
  the Jensen-Shannon divergence between p_data and p_g, minus log4.
- **Non-saturating heuristic (Section 3):** "In practice, equation [1] may not provide
  sufficient gradient for G to learn well." The paper explains that early in training, when G
  is poor, D rejects samples with high confidence, so log(1-D(G(z))) saturates. Its fix:
  "Rather than training G to minimize log(1-D(G(z))) we can train G to maximize log D(G(z))."
  This "provides much stronger gradients early in learning."
- **Algorithm 1 (Section 3):** minibatch SGD: k discriminator-ascent steps per generator
  step; the paper used k=1 in its own experiments ("The number of steps to apply to the
  discriminator, k, is a hyperparameter. We used k=1, the least expensive option, in our
  experiments.").
- **Experiments (Section 5):** "We trained adversarial nets on a range of datasets including
  MNIST, the Toronto Face Database (TFD), and CIFAR-10." Quantitative evaluation (Table 1) is
  a Gaussian Parzen-window log-likelihood estimate, computed for MNIST and TFD only; CIFAR-10
  appears only as visual samples (Figure 2), not in the Parzen table. Table 1 values: DBN
  138±2 (MNIST) / 1909±66 (TFD); Stacked CAE 121±1.6 / 2110±50; Deep GSN 214±1.1 / 1890±29;
  Adversarial nets 225±2 / 2057±26. The paper's own caveat, same section: "This method of
  estimating the likelihood has somewhat high variance and does not perform well in high
  dimensional spaces but it is the best method available to our knowledge."
- **Section 6, "Advantages and disadvantages" (disadvantages, quoted exactly):** "there is no
  explicit representation of p_g(x), and... D must be synchronized well with G during
  training (in particular, G must not be trained too much without updating D, in order to
  avoid 'the Helvetica scenario' in which G collapses too many values of z to the same value
  of x to have enough diversity to model p_data)." This is the paper's own name for what the
  field later calls mode collapse — the founding paper names the risk itself.
- **Figures:** Figure 1 is the schematic (four panels a-d) of the discriminative distribution
  (blue, dashed), data distribution (black, dotted), and generator distribution (green,
  solid) converging until p_g = p_data and D(x) = 1/2 everywhere. Figure 2 is sample grids
  (MNIST, TFD, two CIFAR-10 variants) with nearest-training-example columns. Figure 3 shows
  digits from linear interpolation in z-space.
- **Section structure:** 1 Introduction; 2 Related work; 3 Adversarial nets; 4 Theoretical
  Results (4.1 Global Optimality of p_g=p_data; 4.2 Convergence of Algorithm 1); 5
  Experiments; 6 Advantages and disadvantages; 7 Conclusions and future work.

### 2. Arjovsky, Chintala, Bottou, "Wasserstein GAN," arXiv:1701.07875
URL: https://arxiv.org/abs/1701.07875 (full text via https://ar5iv.labs.arxiv.org/html/1701.07875)
**Primary** for its own diagnosis and proposed replacement objective; the paper owns the WGAN
claim. Authors and affiliations from the paper header: Martin Arjovsky (Courant Institute of
Mathematical Sciences), Soumith Chintala (Facebook AI Research), Léon Bottou (Courant
Institute of Mathematical Sciences; Facebook AI Research). Submitted 26 Jan 2017 (v1), latest
v3 6 Dec 2017.

What it establishes:
- **Diagnosis:** In "Example 1 (Learning parallel lines)" the paper proves that as θ_t→0 the
  sequence (ℙ_θt) converges to ℙ_0 under the Earth-Mover (EM) distance "but does not converge
  at all under either the JS, KL, reverse KL, or TV divergences." Elsewhere: the discriminator
  "learns very quickly to distinguish between fake and real, and as expected provides no
  reliable gradient information," and the paper describes the discriminator loss as one that
  "saturates and results in vanishing gradients" as it approaches optimality.
- **Replacement objective — Earth-Mover / Wasserstein-1 distance (Eq. 1):** W(ℙ_r,ℙ_g) =
  inf_{γ∈Π(ℙ_r,ℙ_g)} E_{(x,y)~γ}[‖x-y‖].
- **Kantorovich-Rubinstein dual form used for training (Eq. 2):** W(ℙ_r,ℙ_θ) =
  sup_{‖f‖_L≤1} E_{x~ℙ_r}[f(x)] - E_{x~ℙ_θ}[f(x)].
- **Empirical claim on mode collapse:** "In no experiment did we see evidence of mode
  collapse for the WGAN algorithm." Also: WGAN training "does not require maintaining a
  careful balance in training of the discriminator and the generator, and does not require a
  careful design of the network architecture either."
- **Figures 3 vs 4:** Figure 3 shows WGAN's estimated Wasserstein distance correlating with
  sample quality; Figure 4 contrasts this with the standard GAN, where the JS estimate
  "increase[s] or stay[s] constant" even as sample quality improves — i.e., the original
  discriminator's loss is not a usable training signal.

### 3. Arjovsky, Bottou, "Towards Principled Methods for Training Generative Adversarial
Networks," arXiv:1701.04862
URL: https://arxiv.org/abs/1701.04862 (full text via https://ar5iv.labs.arxiv.org/html/1701.04862)
**Primary** for the rigorous vanishing-gradient theorem WGAN's prose summarizes; this is the
theoretical precursor paper by two of the three WGAN authors, published two weeks before
WGAN. Authors/affiliations: Martin Arjovsky (Courant Institute of Mathematical Sciences),
Léon Bottou (Facebook AI Research). Submitted 17 Jan 2017.

What it establishes, with exact locators:
- **Lemma 1 / Theorem 2.2 (Section 2.1):** if p_data and p_g have supports on low-dimensional
  manifolds that do not perfectly align, "there exists an optimal discriminator D* that has
  accuracy 1 and ∇_x D* = 0 for almost any x" on both manifolds — i.e., a perfect
  discriminator with zero useful gradient is achievable essentially for free when supports
  are disjoint.
- **Theorem 2.4 / Corollary 2.1 (Section 2.2.1), the vanishing-gradient result:**
  lim_{‖D-D*‖→0} ∇_θ E_{z~p(z)}[log(1-D(g_θ(z)))] = 0, with the bound ‖∇_θ
  E_{z~p(z)}[log(1-D(g_θ(z)))]‖_2 < Mε/(1-ε), where ε bounds the discriminator's distance
  from optimal. This is the exact theorem behind the brief's required claim ("JS divergence
  gives no usable gradient when supports are disjoint / discriminator is near-optimal").

### 4. Lucic, Kurach, Michalski, Gelly, Bousquet, "Are GANs Created Equal? A Large-Scale
Study," arXiv:1711.10337
URL: https://arxiv.org/abs/1711.10337 (full text via https://ar5iv.labs.arxiv.org/html/1711.10337)
**Primary** for its own empirical finding. Authors, all Google Brain: Mario Lucic, Karol
Kurach, Marcin Michalski, Sylvain Gelly, Olivier Bousquet. Submitted 28 Nov 2017 (v1), latest
v4 29 Oct 2018.

What it establishes:
- **Metrics:** Fréchet Inception Distance, FID(x,g) = ‖μ_x-μ_g‖₂² +
  Tr(Σ_x+Σ_g-2(Σ_xΣ_g)^(1/2)), computed on Inception-Net embeddings of real vs. generated
  images. The paper also proposes precision/recall metrics computed on synthetic
  convex-polygon datasets built for the study, "precision measures the fraction of relevant
  retrieved instances among retrieved instances, while recall measures the fraction of
  retrieved instances among relevant instances."
- **Conclusion, exact wording (Abstract):** "we did not find evidence that any of the tested
  algorithms consistently outperforms the non-saturating GAN introduced in [9]" (reference
  [9] is Goodfellow et al. 2014). The paper frames this against a compute-and-tuning budget:
  "most models can reach similar scores with enough hyperparameter optimization and random
  restarts... improvements can arise from a higher computational budget and tuning more than
  fundamental algorithmic changes."
- **Table 2, best FID achieved per model/dataset (verified numbers):** NS-GAN (the original
  paper's non-saturating loss) 6.8±0.5 (MNIST), 26.5±1.6 (Fashion-MNIST), 58.5±1.9 (CIFAR-10),
  55.0±3.3 (CelebA); WGAN-GP 20.3±5.0 / 24.5±2.1 / 55.8±0.9 / 30.0±1.0; BEGAN 13.1±1.0 /
  22.9±0.9 / 71.4±1.6 / 38.9±0.9 on the same four datasets in the same order. No model
  dominates across all four datasets, which is the empirical basis of the abstract's
  conclusion.

### 5. Salimans, Goodfellow, Zaremba, Cheung, Radford, Chen, "Improved Techniques for
Training GANs," arXiv:1606.03498
URL: https://arxiv.org/abs/1606.03498 (full text via https://ar5iv.labs.arxiv.org/html/1606.03498)
**Primary** for its own diagnosis of mode collapse and training instability; co-authored by
Goodfellow, one of the GAN paper's own authors, documenting a failure mode of his own
architecture from the inside. Authors: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki
Cheung, Alec Radford, Xi Chen; affiliation OpenAI. Submitted 10 June 2016.

What it establishes (Section 3, "Minibatch Discrimination" and its intro):
- "One of the main failure modes for GAN is for the generator to collapse to a parameter
  setting where it always emits the same point." And: "Because the discriminator processes
  each example independently, there is no coordination between its gradients, and thus no
  mechanism to tell the outputs of the generator to become more dissimilar to each other.
  Instead, all outputs race toward a single point that the discriminator currently believes
  is highly realistic."
- On instability generally (Section 3 intro): "Finding Nash equilibria is a very difficult
  problem... a modification to θ^(D) that reduces J^(D) can increase J^(G), and a
  modification to θ^(G) that reduces J^(G) can increase J^(D). Gradient descent thus fails to
  converge for many games."

### 6. Goodfellow, "NIPS 2016 Tutorial: Generative Adversarial Networks," arXiv:1701.00160
URL: https://arxiv.org/abs/1701.00160 (WebFetch on the abstract page returned a transient
HTTP 503; the URL itself is live — confirmed via direct curl, HTTP 200 — and full text was
read via https://ar5iv.labs.arxiv.org/html/1701.00160, arXiv's own HTML mirror)
**Primary.** Self-authored retrospective by the GAN paper's lead author on his own
architecture's known failure modes; affiliation OpenAI. Dated 2016 (NIPS 2016 tutorial;
arXiv submission 1701.00160).

What it establishes:
- **Section 5.1.1, "Mode collapse":** "Mode collapse, also known as the Helvetica scenario,
  is a problem that occurs when the generator learns to map several different input z values
  to the same output point." This directly ties the term back to the 2014 paper's own coinage
  (see Source 1) and confirms it is the same failure mode later literature calls mode
  collapse.
- **Section 5.1, "Non-convergence":** "GANs require finding the equilibrium to a game with
  two players... Even if each player successfully moves downhill on that player's update, the
  same update might move the other player uphill... Simultaneous gradient descent converges
  for some games but not all of them," and no convergence guarantee exists once both players
  are deep networks operating in parameter space rather than in the space of the functions
  they can represent.

### 7. Dhariwal, Nichol, "Diffusion Models Beat GANs on Image Synthesis," arXiv:2105.05233
URL: https://arxiv.org/abs/2105.05233 (full text via https://ar5iv.labs.arxiv.org/html/2105.05233)
**Primary** for its own results; the paper owns the FID numbers and the comparison claim.
Authors: Prafulla Dhariwal, Alex Nichol; affiliation OpenAI (per author emails
prafulla@openai.com, alex@openai.com). Submitted 11 May 2021 (v1), latest v4 1 June 2021. No
conference venue is stated on the arXiv abstract page itself — do not assert one beyond
"arXiv preprint" without a further, separately verified source.

What it establishes (Abstract and Table 5):
- Claim: "We show that diffusion models can achieve image sample quality superior to the
  current state-of-the-art generative models."
- FID, ADM-G (their guided diffusion model) vs. BigGAN-deep, same ImageNet resolutions (Table
  5): 128×128 — ADM-G 2.97 vs. BigGAN-deep 6.02; 256×256 — ADM-G 4.59 vs. BigGAN-deep 6.95;
  512×512 — ADM-G 7.72 vs. BigGAN-deep 8.43. Classifier guidance combined with upsampling
  further improves FID to 3.94 (256×256) and 3.85 (512×512) — these are different, better
  numbers than the plain ADM-G row above; keep the two readings distinct if both are cited.
  Sampling-cost claim: "we match BigGAN-deep even with as few as 25 forward passes per
  sample, all while maintaining better coverage of the distribution."

### 8. Lilian Weng, "From GAN to WGAN," Lil'Log, lilianweng.github.io
URL: https://lilianweng.github.io/posts/2017-08-20-gan/
**Secondary.** An independent ML researcher's explainer, written from outside the authoring
parties of any of the papers above; cited for context only, and every figure/claim it repeats
is separately verified against the owning primary above. Published 20 Aug 2017 (updated 30
Sep 2018 and 18 Apr 2019).
What it repeats (not new evidence, but confirms the vanishing-gradient story is legible to an
independent reader working from the same primaries): "When the discriminator is perfect, we
are guaranteed with D(x) = 1, ∀x ∈ p_r and D(x) = 0, ∀x ∈ p_g. Therefore the loss function L
falls to zero and we end up with no gradient to update the loss during learning iterations."
And on mode collapse: "During the training, the generator may collapse to a setting where it
always produces same outputs. This is a common failure case for GANs, commonly referred to as
Mode Collapse." The post cites both the original GAN paper and WGAN by name, consistent with
the primaries above.

## Contradictions

- **WGAN's "no mode collapse" claim is an absence-of-evidence claim, not a proof.** WGAN
  (Source 2) states only "In no experiment did we see evidence of mode collapse for the WGAN
  algorithm" — that is a claim about the experiments the paper ran, not a theorem that WGAN
  cannot mode-collapse. Later practice (WGAN-GP and other variants) did report training
  failures; Lucic et al. (Source 4) show WGAN-GP's own FID is not uniformly the best across
  datasets (e.g., WGAN-GP is worse than NS-GAN on MNIST: 20.3±5.0 vs. 6.8±0.5), which
  complicates any simple "WGAN solved it" reading. Steelmanned: WGAN's own claim is narrow and
  honestly scoped (no evidence *in the experiments they ran*), and its Wasserstein-distance
  metric behaving monotonically with sample quality (Figure 3 vs. 4) is a real, verified
  result distinct from the mode-collapse claim.
- **Lucic et al.'s finding complicates, but does not erase, WGAN's theoretical contribution.**
  Lucic et al. (Source 4) found no variant "consistently outperforms" the non-saturating GAN
  on FID under a fair budget. That is a claim about final sample quality under tuning, not
  about training stability, gradient behavior, or ease of tuning — WGAN's diagnosis (Sources
  2, 3) concerns the latter. A defender of WGAN can hold both: the Earth-Mover reframing
  changed *what is optimized and how reliably it can be monitored*, while still producing
  final FID scores statistically comparable to a well-tuned original loss. The evidence
  supports treating these as answers to different questions rather than a flat rebuttal.
- **The original paper already named mode collapse ("the Helvetica scenario"), so the
  standard story that GAN researchers had to "discover" mode collapse after 2014 is not quite
  right.** Source 1's Section 6 names the risk explicitly in 2014. What later work (Sources 5,
  6) added was not the discovery of the failure mode but its empirical documentation at scale
  and partial mitigations (minibatch discrimination). This sharpens rather than undermines the
  commission's angle: the gap is not "the paper didn't foresee this," it is "the paper
  foresaw it, named it, and offered no fix beyond careful synchronization of D and G."

## Numbers

| Figure | Value | Unit / definition | Owning primary | Locator |
|---|---|---|---|---|
| Global optimum value of C(G) | -log 4 (≈ -1.386) | nats, value of the training criterion at p_g=p_data | Goodfellow et al. 1406.2661 | Section 4.1, Theorem 1 |
| C(G) in terms of JSD | C(G) = -log(4) + 2·JSD(p_data‖p_g) | nats | Goodfellow et al. 1406.2661 | Section 4.1, Eq. 6 |
| Parzen-window log-likelihood, MNIST | 225 ± 2 | mean log-likelihood, MNIST test set | Goodfellow et al. 1406.2661 | Table 1 |
| Parzen-window log-likelihood, TFD | 2057 ± 26 | mean log-likelihood, Toronto Face DB test set | Goodfellow et al. 1406.2661 | Table 1 |
| Parzen-window comparators, MNIST | DBN 138±2; Stacked CAE 121±1.6; Deep GSN 214±1.1 | same units | Goodfellow et al. 1406.2661 | Table 1 |
| Parzen-window comparators, TFD | DBN 1909±66; Stacked CAE 2110±50; Deep GSN 1890±29 | same units | Goodfellow et al. 1406.2661 | Table 1 |
| Discriminator steps per generator step (k) | 1 | hyperparameter, as run in the paper's own experiments | Goodfellow et al. 1406.2661 | Section 3 / Algorithm 1 |
| Best FID, NS-GAN (the original non-saturating loss) | MNIST 6.8±0.5; Fashion-MNIST 26.5±1.6; CIFAR-10 58.5±1.9; CelebA 55.0±3.3 | FID (lower is better), best over hyperparameter search | Lucic et al. 1711.10337 | Table 2 |
| Best FID, WGAN-GP | MNIST 20.3±5.0; Fashion-MNIST 24.5±2.1; CIFAR-10 55.8±0.9; CelebA 30.0±1.0 | FID | Lucic et al. 1711.10337 | Table 2 |
| Best FID, BEGAN | MNIST 13.1±1.0; Fashion-MNIST 22.9±0.9; CIFAR-10 71.4±1.6; CelebA 38.9±0.9 | FID | Lucic et al. 1711.10337 | Table 2 |
| Diffusion (ADM-G) FID vs. BigGAN-deep, ImageNet 128×128 | ADM-G 2.97 vs. BigGAN-deep 6.02 | FID | Dhariwal & Nichol 2105.05233 | Table 5 |
| Diffusion (ADM-G) FID vs. BigGAN-deep, ImageNet 256×256 | ADM-G 4.59 vs. BigGAN-deep 6.95 | FID | Dhariwal & Nichol 2105.05233 | Table 5 |
| Diffusion (ADM-G) FID vs. BigGAN-deep, ImageNet 512×512 | ADM-G 7.72 vs. BigGAN-deep 8.43 | FID | Dhariwal & Nichol 2105.05233 | Table 5 |
| Diffusion FID with classifier guidance + upsampling | 3.94 (256×256); 3.85 (512×512) | FID, best configuration in the paper, distinct from the ADM-G row above | Dhariwal & Nichol 2105.05233 | Abstract; Table 5 region |
| Forward passes for diffusion to match BigGAN-deep | 25 | number of sampling steps (DDIM) | Dhariwal & Nichol 2105.05233 | Abstract |
| Vanishing-gradient bound | ‖∇_θ E[log(1-D(g_θ(z)))]‖₂ < Mε/(1-ε) | ε = discriminator's distance from optimal; M a constant | Arjovsky & Bottou 1701.04862 | Section 2.2.1, Theorem 2.4 / Corollary 2.1 |

## Source assets

- **Goodfellow et al. 1406.2661, Figure 1** (four-panel schematic of D, p_data, p_g
  converging over training stages a-d, ending at p_g=p_data, D(x)=1/2 everywhere): the
  clearest available visual of the paper's central theoretical claim — carries the minimax
  equilibrium argument better than a prose restatement, since the article already commits to
  building the D* and JSD result in its own words. A crop must retain all four panels (a-d)
  in order, since the argument is the progression, and the axis/curve labels (D, p_data,
  p_g), since the reader needs to know which curve is which.
- **Lucic et al. 1711.10337, Table 2** (best-FID-by-model-by-dataset): a small table (not a
  chart) could carry the "no consistent winner" finding more precisely than prose — the
  point is exactly that no row dominates every column. A table must keep all four dataset
  columns together, since the finding is about the *lack* of a consistent ranking across them,
  not any single number.
- **Dhariwal & Nichol 2105.05233, Table 5 (ADM-G vs. BigGAN-deep FID by resolution):** a small
  table or two-row chart could carry the "diffusion displaced GANs" context claim precisely,
  keeping both the FID values and the resolutions paired.
- **Goodfellow et al. 1406.2661, Figure 2 (sample grids) and Figure 3 (z-space
  interpolation):** available, but lower priority — they illustrate output quality, not the
  paper's argument, and the commission's angle is the theory-practice gap, not image fidelity.
  `None found` beyond what is listed above for a stronger visual candidate.

## Discarded

- `https://papers.nips.cc/paper_files/paper/2014/hash/5ca3e9b122f61f8f06494c97b1afccf3-Abstract.html`
  and the `proceedings.neurips.cc` equivalent — both returned HTTP 404. Discarded as a citable
  URL; the arXiv abstract page (Source 1) is used instead and is confirmed live.
- `https://arxiv.org/html/1406.2661` (arXiv's newer native HTML endpoint, tried before falling
  back to the ar5iv mirror) — returned HTTP 404 at fetch time. Discarded in favor of
  `ar5iv.labs.arxiv.org/html/1406.2661`, which mirrors the same arXiv submission and resolved.
- Direct WebFetch of the raw PDFs (`arxiv.org/pdf/...`) for all four core papers — the fetch
  tool returned only encoded PDF stream data, unusable for verification; poppler-utils was not
  installable in this environment (`apt-get install poppler-utils` failed with a 404 from the
  package mirror), so PDF-to-text rendering was not available either. Worked around by using
  the ar5iv HTML mirror instead, which reproduces the same submission's text and equations.
