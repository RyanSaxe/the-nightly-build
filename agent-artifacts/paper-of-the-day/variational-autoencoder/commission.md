# Commission: paper-of-the-day/variational-autoencoder

## The paper and why it earns the slot

Diederik P. Kingma and Max Welling, "Auto-Encoding Variational Bayes,"
arXiv:1312.6114 (ICLR 2014). The central claim to rebuild: the reparameterization
trick turns an intractable latent-variable objective into one a neural network
can optimize by ordinary backpropagation, by writing the evidence lower bound
(ELBO) as reconstruction minus the KL divergence from the approximate posterior
to the prior and sampling the latent through `z = mu + sigma (*) epsilon`. The
paper gives the article real material to examine: the derivation, the estimator's
variance argument, and a public record after publication that lets the piece weigh
the claim against what happened next. It stays inside the machine-learning center.

## Rebuild the argument with the paper's own artifacts

Reconstruct the idea in the piece's own order and examples, not the paper's.
Define each concept where the argument first spends it: the latent-variable model
and its intractable marginal likelihood, the variational posterior, the ELBO, and
why the naive score-function gradient is high variance where the reparameterized
one is not. Set the math the reconstruction leans on rather than paraphrasing it:
the ELBO and the reparameterized estimator are the equations the piece turns on,
so put them in `nb-math`, with the ELBO as the single annotated equation. Anchor
the turns of the argument in the citations themselves, with honest
`data-nb-locator` and `data-nb-note`, quoting the paper's exact sentence where it
earns display space. A reconstruction that only describes what the paper derives
is underusing its strongest material.

## Weigh it as a reviewer, against the after-record

What was measured, on what, and what would count as the claim failing to
generalize: the paper evaluates marginal likelihood on small image datasets
(MNIST, Frey faces), so name the limits of that evaluation plainly. Place the
paper among the work it builds on and the work that tests it, using other sources
only where they change the interpretation: posterior collapse as a real,
still-discussed failure mode (for example Bowman et al. 2016 on continuous-space
sentence VAEs), the tighter bound of importance-weighted autoencoders (Burda et
al. 2016), the disentanglement pressure of beta-VAE (Higgins et al. 2017), and
the forward link that the ELBO is the same objective the denoising-diffusion
training loss reappears from. State a verdict on the claims before the Sources.

## Source assets

The paper's own figures may carry the argument better than prose: the learned
low-dimensional data manifold and the reparameterization schematic are candidates.
Use a source asset only where the article's argument spends what the figure shows,
captured from the paper as a cited primary, with a factual caption. A minimal
reparameterized sampler in `nb-code` is welcome if it makes the trick concrete,
but the equation and the figure are the priority.

## Sources to begin from (researcher confirms and reads the primary)

- Kingma and Welling, arXiv:1312.6114 (the focal paper; read the derivation,
  the estimator, and Section on experiments and figures).
- Rezende, Mohamed, Wierstra, "Stochastic Backpropagation..." (the contemporaneous
  independent derivation) for context on the claim's standing.
- Bowman et al. 2016 (posterior collapse), Burda et al. 2016 (IWAE), Higgins et
  al. 2017 (beta-VAE) for the after-record. Each only where it changes the read.

## Habits to break (from the recent paper-of-the-day record)

The vision-transformer piece (2026-08-13) built headings as numeric findings
("ViT-B/16 gains 6.24 points between 1.3 million and 303 million images") and
closed with an `nb-note-strong` box. Do not copy the numeric-finding heading
formula wholesale or the closing `nb-note-strong` verdict box. Recent pieces in
this series have concentrated on transformers and reinforcement learning; a
generative latent-variable model is distinct, so keep it so. Vary heading
construction; the verdict is required by the template but earn it in prose rather
than defaulting to the standing verdict box.

Reader: the paper's declared audience (mathematics and CS, ML-engineering
career). Word band 1800-3400, 2 to 8 flex sections, at least 8 sources. No
overlap with the other six articles this edition.

Models and effort actually used (Agent runtime; effort not separately settable,
so intended effort recorded, model tier plus prompt emphasis carry it):
writing-coach — capable (sonnet), low; researcher — capable (sonnet), high;
writer — capable (sonnet), medium; editor — inherited (opus), high, required.
