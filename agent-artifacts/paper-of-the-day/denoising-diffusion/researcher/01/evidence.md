# Evidence: paper-of-the-day/denoising-diffusion (01)

The evidence fully supports the reconstruction the commission asks for. The focal
paper (Ho, Jain, Abbeel 2020) is read past the abstract into the Section 2-3
derivations and the experiments. Every equation the reconstruction leans on is
captured verbatim with its printed number: the forward process (Eq. 2), the
closed-form marginal q(x_t|x_0) with the alpha-bar reparameterization (Eq. 4), the
reverse parameterization (Eq. 1), the tractable forward posterior (Eq. 6-7), the
reduction of the KL term to mean-matching (Eq. 8), the epsilon reparameterization of
the mean (Eq. 11), the weighted noise-prediction term (Eq. 12), and the simplified
objective L_simple (Eq. 14) with the weighting explicitly dropped. Algorithm 1
(training) and Algorithm 2 (sampling) are captured line by line. All reported metrics
are verified against the paper's own Table 1 (CIFAR-10), Table 2 (ablation), and the
Figure 3/4 captions (LSUN); CelebA-HQ is qualitative only. Where the evidence is thin
is exactly where the commission wants a verdict: the paper reports strong FID/IS but
**worse** log-likelihood than its own variational-bound variant and concedes its
codelengths "are not competitive with other types of likelihood-based generative
models," and it never treats the 1000-step sampling cost as a limitation. Those two
gaps are precisely what the after-record (DDIM, Improved DDPM, score-SDE) closes, and
they are the spine of the honest verdict. The lineage (Sohl-Dickstein 2015, NCSN 2019)
and the after-record (DDIM, classifier / classifier-free guidance, latent diffusion,
score-SDE, Improved DDPM) are each read firsthand from their own abstracts/claims.

Note on equation and figure numbering: transcribed from the arXiv v2 / ar5iv HTML,
which matches the published NeurIPS 2020 numbering. Some cells were cross-checked
across two independent fetches; where a number appears below it agreed on both reads.

## Sources

```text
URL:         https://arxiv.org/abs/2006.11239
             (proceedings: https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)
Kind:        primary. The focal paper; owns every DDPM claim, equation, algorithm, and metric.
Establishes: The whole reconstruction — forward/reverse processes, the variational bound,
             the epsilon-prediction objective L_simple, the training/sampling algorithms,
             and the CIFAR-10 / LSUN / CelebA-HQ results.
Paraphrase:  A latent-variable generative model defines a fixed forward Markov chain that
             adds Gaussian noise over T steps until data becomes ~N(0,I), and learns a
             reverse Markov chain to denoise. The variational bound reduces, under a fixed
             forward posterior and an epsilon (added-noise) parameterization of the reverse
             mean, to a simple weighted denoising regression; dropping the weight gives a
             plain MSE on predicted noise, which trains stably and yields the best samples.
Locators:    Title/authors/abstract (p.1); Sec. 2 Background (Eq. 1-5); Sec. 3.1-3.2 and
             3.3 (Eq. 6-14, Alg. 1-2); Sec. 4 Experiments (Table 1-2, Fig. 1-4).
Venue:       NeurIPS 2020. Authors: Jonathan Ho, Ajay Jain, Pieter Abbeel (all UC Berkeley).
             arXiv subjects cs.LG, stat.ML; submitted 2020-06-19 (v1), revised 2020-12-16 (v2).
Quote (abstract, verbatim, for the card):
             "We present high quality image synthesis results using diffusion probabilistic
             models, a class of latent variable models inspired by considerations from
             nonequilibrium thermodynamics. Our best results are obtained by training on a
             weighted variational bound designed according to a novel connection between
             diffusion probabilistic models and denoising score matching with Langevin
             dynamics, and our models naturally admit a progressive lossy decompression
             scheme that can be interpreted as a generalization of autoregressive decoding.
             On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and
             a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality
             similar to ProgressiveGAN."
```

```text
URL:         https://arxiv.org/abs/1503.03585
Kind:        primary. Owns the diffusion-generative-model idea DDPM builds on.
Establishes: The forward/reverse diffusion framework itself — DDPM is a training recipe on
             top of this, not a new class of model. Changes the interpretation of DDPM's
             novelty: the architecture and framing are 2015; DDPM's contribution is the
             parameterization and objective that made it produce competitive images.
Paraphrase:  Slowly destroy structure in data with an iterative forward diffusion process,
             then learn a reverse diffusion process that restores structure, yielding a
             flexible and tractable deep generative model.
Locators:    Title, abstract. Sohl-Dickstein, Weiss, Maheswaranathan, Ganguli. ICML 2015.
Quote:       "The essential idea, inspired by non-equilibrium statistical physics, is to
             systematically and slowly destroy structure in a data distribution through an
             iterative forward diffusion process. We then learn a reverse diffusion process
             that restores structure in data, yielding a highly flexible and tractable
             generative model of the data."
```

```text
URL:         https://arxiv.org/abs/1907.05600
Kind:        primary. Owns the score-matching + annealed-Langevin approach DDPM connects to.
Establishes: The parallel score-based lineage. DDPM's abstract claims a "novel connection
             between diffusion probabilistic models and denoising score matching with
             Langevin dynamics"; NCSN is the other half of that connection. Its CIFAR-10
             IS 8.87 is the score-based number DDPM's 9.46 improves on (and appears as the
             NCSN baseline row in DDPM Table 1, FID 25.32).
Paraphrase:  Estimate the gradient of the log data density (the score) at multiple Gaussian
             noise levels via score matching, then sample with annealed Langevin dynamics,
             lowering noise toward the data manifold. No adversarial training.
Locators:    Title, abstract. Song & Ermon. NeurIPS 2019 (oral). Abstract reports CIFAR-10
             Inception score 8.87.
```

```text
URL:         https://arxiv.org/abs/2010.02502
Kind:        primary (after-record). Owns the DDIM sampler.
Establishes: Directly answers DDPM's unstated sampling-cost problem. Same training objective,
             a non-Markovian deterministic reverse process, 10x-50x fewer steps. Reframes
             DDPM's 1000-step sampler as one point on a speed/quality curve, not a fixed cost.
Paraphrase:  DDPMs need a long Markov chain to sample; DDIM defines non-Markovian processes
             with the SAME training objective, enabling far fewer sampling steps and
             deterministic (implicit) sampling without retraining.
Locators:    Title, abstract. Song, Meng, Ermon. ICLR 2021.
Quote:       "we present denoising diffusion implicit models (DDIMs) ... with the same
             training procedure as DDPMs ... 10x to 50x faster in terms of wall-clock time
             compared to DDPMs".
```

```text
URL:         https://arxiv.org/abs/2011.13456
Kind:        primary (after-record). Owns the SDE unification.
Establishes: Places DDPM inside a continuous framework: DDPM and NCSN are two discretizations
             of the same forward SDE, with a reverse-time SDE and an equivalent
             probability-flow ODE that gives exact likelihoods. Recontextualizes DDPM's
             discrete-time derivation as a special case and reports a much stronger CIFAR-10
             FID 2.20 / IS 9.89 / 2.99 bits-dim, showing the family's headroom.
Paraphrase:  Both score-based and diffusion models are discretizations of a stochastic
             differential equation; a corresponding reverse-time SDE and a probability-flow
             ODE recover data from noise, the ODE enabling exact likelihood computation.
Locators:    Title, abstract. Song, Sohl-Dickstein, Kingma, Kumar, Ermon, Poole. ICLR 2021
             (oral/outstanding). Abstract-region metrics: CIFAR-10 FID 2.20, IS 9.89,
             2.99 bits/dim.
```

```text
URL:         https://arxiv.org/abs/2105.05233
Kind:        primary (after-record). Owns classifier guidance; secondary as commentary on DDPM.
Establishes: The claim that closes DDPM's LSUN hedge ("similar to ProgressiveGAN"). Two years
             later, diffusion models beat the strongest GANs on ImageNet via classifier
             guidance plus architecture search — the empirical vindication of the diffusion bet.
Paraphrase:  Better architectures plus "classifier guidance" (mixing the diffusion score with
             a classifier's gradient at test time) let diffusion models exceed GAN sample
             quality while covering the distribution better.
Locators:    Title, abstract. Dhariwal & Nichol. NeurIPS 2021. Reported FID: ImageNet 128
             2.97, 256 4.59, 512 7.72; matches BigGAN-deep "with as few as 25 forward passes".
```

```text
URL:         https://arxiv.org/abs/2207.12598
Kind:        primary (after-record). Owns classifier-free guidance.
Establishes: The conditioning technique the production wave (Stable Diffusion, Imagen, DALL-E 2)
             actually uses. Shows DDPM's plain unconditional objective extends to controllable
             generation without a separate classifier — a direct line from L_simple to text-to-image.
Paraphrase:  Jointly train one conditional and one unconditional diffusion model (drop the
             condition at random), then combine their score estimates at sampling time to
             trade sample quality against diversity, with no separate classifier.
Locators:    Title, abstract. Ho & Salimans. NeurIPS 2021 workshop; arXiv 2022-07.
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary (after-record). Owns latent diffusion / underpins Stable Diffusion.
Establishes: How DDPM's per-pixel, per-step cost was made economical enough for public
             text-to-image. Moving the same denoising process into a pretrained autoencoder's
             latent space plus cross-attention conditioning is the practical descendant of DDPM.
Paraphrase:  Run the diffusion process in the latent space of a pretrained autoencoder rather
             than in pixels, cutting compute while keeping quality, and add cross-attention
             layers for general conditioning (e.g. text).
Locators:    Title, abstract. Rombach, Blattmann, Lorenz, Esser, Ommer. CVPR 2022.
```

```text
URL:         https://arxiv.org/abs/2102.09672
Kind:        primary (after-record) and the serious later assessment. Secondary as critique of DDPM.
Establishes: The most direct rebuttal to DDPM's own weak spot. It shows DDPM's log-likelihood
             was NOT competitive and fixes it by learning the reverse-process variances
             (which DDPM fixed to a constant) via a hybrid objective plus a cosine schedule,
             and gets an order-of-magnitude fewer sampling steps at negligible quality cost.
             Names both DDPM limitations the verdict rests on: likelihood and sampling cost.
Paraphrase:  A few modifications — learning the reverse variances, a cosine noise schedule,
             a hybrid loss — give DDPMs competitive log-likelihoods and ~10x cheaper sampling
             with negligible sample-quality loss; quality and likelihood scale smoothly with
             compute.
Locators:    Title, abstract. Nichol & Dhariwal. ICML 2021.
Quote:       "learning variances of the reverse diffusion process allows sampling with an
             order of magnitude fewer forward passes with a negligible difference in sample
             quality".
```

## Equations captured (verbatim, for the reconstruction)

All from Ho, Jain, Abbeel 2020, Sec. 2-3. Printed equation numbers in brackets.

- **Forward process [Eq. 2]:**
  `q(x_{1:T}|x_0) := prod_{t=1}^T q(x_t|x_{t-1})`,
  `q(x_t|x_{t-1}) := N(x_t; sqrt(1-beta_t) x_{t-1}, beta_t I)`.

- **Closed-form marginal [Eq. 4]**, with `alpha_t := 1-beta_t` and `alpha_bar_t := prod_{s=1}^t alpha_s`:
  `q(x_t|x_0) = N(x_t; sqrt(alpha_bar_t) x_0, (1-alpha_bar_t) I)`.
  Reparameterization: `x_t = sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) * eps`, `eps ~ N(0,I)`.

- **Reverse process [Eq. 1]:**
  `p_theta(x_{0:T}) := p(x_T) prod_{t=1}^T p_theta(x_{t-1}|x_t)`,
  `p_theta(x_{t-1}|x_t) := N(x_{t-1}; mu_theta(x_t,t), Sigma_theta(x_t,t))`. (Sigma is fixed, not learned.)

- **Variational bound decomposition [Eq. 5]:**
  `L = L_T + sum_{t>1} L_{t-1} - log p_theta(x_0|x_1)`, where
  `L_T = KL(q(x_T|x_0) || p(x_T))`, `L_{t-1} = KL(q(x_{t-1}|x_t,x_0) || p_theta(x_{t-1}|x_t))`.

- **Tractable forward posterior [Eq. 6-7]:**
  `q(x_{t-1}|x_t,x_0) = N(x_{t-1}; mu_tilde_t(x_t,x_0), beta_tilde_t I)`, with
  `mu_tilde_t(x_t,x_0) = (sqrt(alpha_bar_{t-1}) beta_t)/(1-alpha_bar_t) * x_0 + (sqrt(alpha_t)(1-alpha_bar_{t-1}))/(1-alpha_bar_t) * x_t`
  and `beta_tilde_t = (1-alpha_bar_{t-1})/(1-alpha_bar_t) * beta_t`.

- **KL term as mean-matching [Eq. 8]:**
  `L_{t-1} = E_q[ (1/(2 sigma_t^2)) || mu_tilde_t(x_t,x_0) - mu_theta(x_t,t) ||^2 ] + C`.

- **Epsilon reparameterization of the reverse mean [Eq. 11]:**
  `mu_theta(x_t,t) = (1/sqrt(alpha_t)) ( x_t - (beta_t/sqrt(1-alpha_bar_t)) eps_theta(x_t,t) )`.

- **Resulting weighted noise-prediction term [Eq. 12]:**
  `L_{t-1} = E_{x_0,eps}[ (beta_t^2)/(2 sigma_t^2 alpha_t (1-alpha_bar_t)) || eps - eps_theta(sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) eps, t) ||^2 ]`.

- **Simplified objective [Eq. 14] — the decisive move (weighting dropped):**
  `L_simple(theta) := E_{t,x_0,eps}[ || eps - eps_theta(sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) eps, t) ||^2 ]`.
  The paper drops the `beta_t^2/(2 sigma_t^2 alpha_t (1-alpha_bar_t))` coefficient from Eq. 12;
  because that coefficient is largest at small t, dropping it down-weights the easy small-t
  denoising tasks and up-weights harder large-t tasks, which the paper reports improves sample quality.

**Algorithm 1 (Training):**
```
1: repeat
2:   x_0 ~ q(x_0)
3:   t ~ Uniform({1,...,T})
4:   eps ~ N(0, I)
5:   Take gradient descent step on
       grad_theta || eps - eps_theta( sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) eps, t ) ||^2
6: until converged
```

**Algorithm 2 (Sampling):**
```
1: x_T ~ N(0, I)
2: for t = T,...,1 do
3:   z ~ N(0, I) if t > 1, else z = 0
4:   x_{t-1} = (1/sqrt(alpha_t)) ( x_t - ((1-alpha_t)/sqrt(1-alpha_bar_t)) eps_theta(x_t,t) ) + sigma_t z
5: end for
6: return x_0
```
Setup (Sec. 4): `T = 1000`; forward variances linear from `beta_1 = 1e-4` to `beta_T = 0.02`.
Sampling variance choice (verbatim): "The first choice is optimal for x_0 ~ N(0,I), and the
second is optimal for x_0 deterministically set to one point." (i.e. sigma_t^2 = beta_t or
sigma_t^2 = beta_tilde_t; experiments give comparable results.)

## Contradictions

Where DDPM's own claims are qualified, by later work or by the paper itself:

- **Log-likelihood is not the win.** The abstract leads with sample quality (FID 3.17), but
  Table 1 shows the L_simple model has a WORSE (higher) NLL bound, `<= 3.75` bits/dim, than the
  paper's own variational-bound variant at `<= 3.70`. The paper concedes (verbatim): "Still,
  while our lossless codelengths are better than the large estimates reported for energy based
  models and score matching using annealed importance sampling, they are not competitive with
  other types of likelihood-based generative models." So the objective that maximizes image
  quality is not the one that maximizes likelihood. Nichol & Dhariwal 2021 (arXiv:2102.09672)
  confirm this and close the gap by learning the variances DDPM held fixed.

- **Sampling cost is unstated as a limitation.** DDPM fixes `T = 1000` and its only stated
  reason is to match prior work's neural-net-evaluation count ("We set T=1000 for all experiments
  so that the number of neural network evaluations needed during sampling matches previous work").
  It does not frame 1000 sequential forward passes per sample as a cost. DDIM (arXiv:2010.02502,
  10x-50x fewer steps, same objective) and Improved DDPM (order-of-magnitude fewer forward passes)
  both treat it as the central practical problem. This is the sharpest gap between the paper's
  framing and the after-record.

- **"Similar to ProgressiveGAN" was a floor, not a ceiling.** The LSUN claim is hedged to parity
  with a 2018 GAN. Dhariwal & Nichol 2021 (arXiv:2105.05233) later show diffusion models *beat*
  the strongest GANs on ImageNet with classifier guidance, so DDPM's own hedge understates where
  the method went. Note the direction of the contradiction favors DDPM's thesis, not against it.

- **Not a new model class.** The abstract frames the connection to score matching as "novel," but
  the forward/reverse diffusion generative framework is Sohl-Dickstein et al. 2015
  (arXiv:1503.03585) and the score/Langevin machinery is NCSN 2019 (arXiv:1907.05600). DDPM's
  contribution is the epsilon-parameterization and L_simple objective, not the model family — a
  reviewer's honest read that the reconstruction should state plainly.

## Numbers

```text
Figure: FID 3.17 (unconditional CIFAR-10, best)
Owner:  Ho et al. 2020, Table 1, row "Ours (L_simple)"
Scope:  Unconditional CIFAR-10 32x32; lower is better; state-of-the-art at publication among unconditional models.
```
```text
Figure: Inception score 9.46 +/- 0.11 (unconditional CIFAR-10, best)
Owner:  Ho et al. 2020, Table 1, row "Ours (L_simple)"
Scope:  Unconditional CIFAR-10 32x32; higher is better.
```
```text
Figure: NLL <= 3.75 bits/dim (test), 3.72 (train) for the L_simple model; <= 3.70 (test), 3.69 (train) for the L (fixed isotropic Sigma) model
Owner:  Ho et al. 2020, Table 1, columns NLL
Scope:  CIFAR-10; lower is better. The best-FID model is NOT the best-NLL model. This is the key internal tension.
```
```text
Figure: Table 1 baselines (CIFAR-10, FID / IS): NCSN 25.32 / 8.87; NCSNv2 31.75 / --; SNGAN 21.7 / 8.22; SNGAN-DDLS 15.42 / 9.09; StyleGAN2+ADA(v1) 3.26 / 9.74
Owner:  Ho et al. 2020, Table 1
Scope:  CIFAR-10. DDPM (3.17) is best FID among the unconditional entries; StyleGAN2+ADA is a conditional/augmented GAN comparator.
```
```text
Figure: Ablation — epsilon-prediction + L_simple gives FID 3.17 / IS 9.46 (best); mu-tilde prediction + true variational bound (fixed Sigma) gives FID 13.51 / IS 7.67; learning a diagonal Sigma was unstable (blank cells)
Owner:  Ho et al. 2020, Table 2
Scope:  Unconditional CIFAR-10 reverse-process parameterization and objective ablation. This table is the direct evidence that L_simple + epsilon is the decisive choice.
```
```text
Figure: LSUN Church FID 7.89
Owner:  Ho et al. 2020, Figure 3 caption ("LSUN Church samples. FID=7.89")
Scope:  256x256 LSUN Church.
```
```text
Figure: LSUN Bedroom FID 4.90
Owner:  Ho et al. 2020, Figure 4 caption ("LSUN Bedroom samples. FID=4.90")
Scope:  256x256 LSUN Bedroom. Note: LSUN FIDs live in figure captions, not a comparison table; no per-baseline LSUN table exists in the paper.
```
```text
Figure: CelebA-HQ 256x256 — no FID reported
Owner:  Ho et al. 2020, Figure 1 (qualitative samples only)
Scope:  Shown for visual quality; the reconstruction must not attribute a CelebA-HQ FID to the paper.
```
```text
Figure: (after-record, for the verdict) Score-SDE CIFAR-10 FID 2.20, IS 9.89, 2.99 bits/dim; Diffusion-Beats-GANs ImageNet FID 2.97 (128), 4.59 (256), 7.72 (512)
Owner:  Song et al. 2021 (arXiv:2011.13456) and Dhariwal & Nichol 2021 (arXiv:2105.05233) respectively
Scope:  Different datasets/settings than DDPM; use only to show the family's later headroom, never as DDPM's own numbers.
```

## Source assets

```text
Asset: Algorithm 1 (Training) box, Sec. 3.2. Six lines: sample x_0, t, eps; gradient step on ||eps - eps_theta(...)||^2.
Shows: The entire training loop is a noise-prediction regression — no adversary, no reconstruction decoder, no per-step targets. This is the paper's plainest evidence for why it trains stably.
Crop:  Retain all six lines and the objective inside the norm. Do not crop off the sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) eps input — that is the closed-form marginal doing the work.
```
```text
Asset: Algorithm 2 (Sampling) box, Sec. 3.2. Iterative x_{t-1} update with the sigma_t z noise term and the z=0 at t=1 condition.
Shows: Sampling is ancestral: T sequential denoising steps from pure noise. Pairing it with Alg. 1 makes the 1000-step cost visible, which sets up the DDIM/Improved-DDPM contradiction.
Crop:  Keep the full update line (both the eps_theta term and the + sigma_t z term) and the t>1 condition on z. Dropping the noise term would misrepresent it as deterministic (that is DDIM, not DDPM).
```
```text
Asset: Figure 2 — "The directed graphical model considered in this work." (the forward q / reverse p_theta Markov chain over x_0 ... x_T).
Shows: The two-process skeleton in one picture: fixed forward noising vs. learned reverse denoising. The cleanest single visual for teaching the setup before any math.
Crop:  Retain both the forward (q) and reverse (p_theta) arrow directions and the x_0 and x_T endpoints. A crop that keeps only one chain loses the point.
```
```text
Asset: Figure 3 (LSUN Church, FID=7.89) and Figure 4 (LSUN Bedroom, FID=4.90) sample grids.
Shows: The headline sample-quality claim at 256x256, with the FID printed in-caption so the visual and the number arrive together.
Crop:  Keep the FID value legible in/with the caption. These are the argument's quantitative-plus-visual evidence, not decoration.
```
```text
Asset: Figure 1 — CelebA-HQ 256x256 (left) and unconditional CIFAR-10 (right) samples.
Shows: The opening quality showcase across faces and CIFAR. Usable as the card/opening visual.
Crop:  Do not attach an FID to the CelebA-HQ panel; the paper reports none for it.
```
```text
Asset: Table 2 (ablation over parameterization and objective).
Shows: The single most load-bearing table for the reconstruction's thesis: epsilon + L_simple beats mu-tilde + true bound on FID. Better rendered as a small comparison table in-article than as an image.
Crop:  n/a (transcribe as furniture, not an image).
```

## Discarded

```text
URL: https://arxiv.org/html/2006.11239 and .../html/2006.11239v2 — arXiv native HTML returns 404 for this paper; used ar5iv.labs.arxiv.org HTML instead for full text and equations.
URL: A standalone LSUN comparison "Table 3" — searched for and not present; the paper reports LSUN FID only in Figure 3/4 captions, so no such table is cited.
URL: StyleGAN2+ADA / BigGAN primary papers — not read in full; they appear only as baseline names inside DDPM Table 1 and are cited transitively through it, not independently relied on.
```
