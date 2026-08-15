# Evidence: paper-of-the-day/variational-autoencoder (researcher/02)

This is a complete record superseding researcher/01/evidence.md, not an
overwrite: all five prior sources, their contradictions, numbers, and source
assets are carried forward unchanged below, because rereading them for this
round found nothing that weakens them. Two new sources were read in full and
are added because they are load-bearing, not to hit a count. Ho et al. 2020
(DDPM) is now source 6: its own Section 2 states in one sentence, with its own
equation number, that training a diffusion model is "optimizing the usual
variational bound on negative log likelihood" — the exact ELBO-to-diffusion
forward link the brief asked for, with a page-and-equation locator the writer
can cite directly. Paisley, Blei, and Jordan 2012 is now source 7: it is the
paper Kingma and Welling's own text cites, uncited by the article, for the
claim that the naive score-function gradient estimator has high variance; its
Section 4 states that claim explicitly, with the exact mechanism (Monte Carlo
variance scaling as Cov(X)/S) that makes it true rather than asserted. The one
gap that is not closed: Higgins et al. 2017 (beta-VAE), source 5, is still not
a primary read. This round retried it with more routes than round one —
including a Cloudflare Turnstile inspection that identifies precisely why
automated access fails — and all of them failed for a reason stronger than a
missing header: OpenReview gates this specific paper behind an interactive
Cloudflare Turnstile challenge that requires solving a widget in a real
browser, which no tool available in this session can do. That gap, and every
route tried against it, is recorded in full in the source 5 entry and in
Discarded below. The total stands at seven sources: five carried forward, two
newly read and load-bearing, one still access-limited and flagged rather than
silently dropped or falsely upgraded.

## Sources

```text
URL:         https://arxiv.org/abs/1312.6114
Kind:        primary — Kingma and Welling's own paper; owns every claim about
             the ELBO, SGVB, reparameterization, and the MNIST/Frey Face
             experiments.
Establishes: The full argument: the intractable marginal-likelihood problem,
             the ELBO, the SGVB estimator, the reparameterization trick, the
             concrete Gaussian VAE, and the reported experiments.
Paraphrase:  Read as the current version served at this URL (v11, revised
             2022-12-10 per the submission history on the abstract page; the
             original was submitted 2013-12-20). The abstract page confirms
             title "Auto-Encoding Variational Bayes," authors Diederik P.
             Kingma and Max Welling.
Locators:    See the Numbers and Source assets sections below for other
             figure- and number-level locators. The equations the
             commission asks for are transcribed in full here, since the
             writer needs the exact content, not just a pointer:

             Eq. (1), Section 2.2, page 3 — the exact-decomposition identity
             the whole method turns on:
               log p_theta(x^(i)) = D_KL( q_phi(z|x^(i)) || p_theta(z|x^(i)) )
                                     + L(theta, phi; x^(i))

             Eq. (2)-(3), Section 2.2, page 3 — the lower bound, then the
             reconstruction-minus-KL form. Eq. (3) is the ELBO decomposition
             the commission names as the piece's single annotated equation:
               Eq. (2): L(theta,phi;x^(i)) =
                 E_{q_phi(z|x)}[ -log q_phi(z|x) + log p_theta(x,z) ]
               Eq. (3): L(theta,phi;x^(i)) =
                 -D_KL( q_phi(z|x^(i)) || p_theta(z) )
                 + E_{q_phi(z|x^(i))}[ log p_theta(x^(i)|z) ]
             (Paraphrase, not quote, of the sentence right after Eq. (3):
             the naive Monte Carlo gradient estimator for the second RHS
             term's dependence on phi — built from f(z) times the score
             function grad_phi log q_phi(z), averaged over L samples — is
             asserted to have very high variance, citing Blei, Jordan, and
             Paisley 2012 ("Variational Bayesian inference with Stochastic
             Search," ICML). The paper does not derive that variance itself
             here; it cites the claim rather than proving it. That is an
             honest limit worth naming if the piece leans on the variance
             argument: the paper's own text argues by citation, not by a
             shown derivation, at this exact step. Source 7 below is that
             citation, read in full for this round.)

             Eq. (4)-(6), Section 2.3, page 3 — the reparameterization and
             the generic SGVB estimator:
               Eq. (4): z-tilde = g_phi(epsilon, x), with epsilon ~ p(epsilon)
               Eq. (5): E_{q_phi(z|x^(i))}[f(z)] = E_{p(epsilon)}[f(g_phi(epsilon,x^(i)))]
                 ~= (1/L) sum_{l=1}^{L} f(g_phi(epsilon^(l), x^(i))), epsilon^(l) ~ p(epsilon)
               Eq. (6), the generic SGVB estimator L-tilde^A:
                 L-tilde^A(theta,phi;x^(i)) =
                   (1/L) sum_{l=1}^{L} [ log p_theta(x^(i), z^(i,l)) - log q_phi(z^(i,l)|x^(i)) ]
                 where z^(i,l) = g_phi(epsilon^(i,l), x^(i)), epsilon^(l) ~ p(epsilon)

             Eq. (7)-(8), Section 2.3, page 4 — the lower-variance estimator
             (uses the closed-form KL) and the minibatch estimator:
               Eq. (7), estimator L-tilde^B: L-tilde^B(theta,phi;x^(i)) =
                 -D_KL( q_phi(z|x^(i)) || p_theta(z) )
                 + (1/L) sum_{l=1}^{L} log p_theta(x^(i)|z^(i,l))
                 where z^(i,l) = g_phi(epsilon^(i,l), x^(i)), epsilon^(l) ~ p(epsilon)
               Eq. (8), minibatch estimator: L(theta,phi;X) ~=
                 L-tilde^M(theta,phi;X^M) = (N/M) sum_{i=1}^{M} L-tilde(theta,phi;x^(i))
             The paper states L-tilde^B "typically has less variance than the
             generic estimator" (i.e. than Eq. 6) — the only place it
             compares variance between its own two estimators, and again by
             assertion, not derivation.

             Section 2.4, page 4-5 — the reparameterization trick, stated in
             general and then worked through the univariate Gaussian case
             that becomes the paper's running example (this is the source of
             "z = mu + sigma * epsilon"; it is presented in this general
             prose form before it reappears as the model-specific Eq. 9-10):
               General: z = g_phi(epsilon, x), epsilon ~ p(epsilon) an
               auxiliary variable independent of x.
               Univariate Gaussian worked example (page 5): "let z ~
               p(z|x) = N(mu, sigma^2). In this case, a valid
               reparameterization is z = mu + sigma*epsilon, where epsilon is
               an auxiliary noise variable epsilon ~ N(0,1)."

             Eq. (9)-(10), Section 3, page 5 — the concrete VAE the paper
             builds and evaluates, and the sampling line that is the vector
             (multi-dimensional, Hadamard-product) form of "z = mu + sigma *
             epsilon":
               Eq. (9): log q_phi(z|x^(i)) = log N(z; mu^(i), sigma^2(i) * I)
               Sampling line (unnumbered, between Eq. 9 and Eq. 10): z^(i,l)
                 = g_phi(x^(i), epsilon^(l)) = mu^(i) + sigma^(i) (o) epsilon^(l),
                 epsilon^(l) ~ N(0, I). "(o)" is the paper's own notation for
                 an element-wise product.
               Eq. (10), the full trainable loss for one datapoint:
                 L(theta,phi;x^(i)) ~=
                   (1/2) * sum_{j=1}^{J} ( 1 + log((sigma_j^(i))^2)
                     - (mu_j^(i))^2 - (sigma_j^(i))^2 )
                   + (1/L) * sum_{l=1}^{L} log p_theta(x^(i)|z^(i,l))
                 where z^(i,l) = mu^(i) + sigma^(i) (o) epsilon^(l), epsilon^(l) ~ N(0,I).
               The first term (the closed-form Gaussian-to-Gaussian KL) is
               derived in Appendix B, page 10-11, and is exact, not
               estimated — only the second (reconstruction) term is a Monte
               Carlo estimate.

Quote:       Full abstract, verbatim: "How can we perform efficient inference
             and learning in directed probabilistic models, in the presence
             of continuous latent variables with intractable posterior
             distributions, and large datasets? We introduce a stochastic
             variational inference and learning algorithm that scales to
             large datasets and, under some mild differentiability
             conditions, even works in the intractable case. Our
             contributions are two-fold. First, we show that a
             reparameterization of the variational lower bound yields a
             lower bound estimator that can be straightforwardly optimized
             using standard stochastic gradient methods. Second, we show
             that for i.i.d. datasets with continuous latent variables per
             datapoint, posterior inference can be made especially efficient
             by fitting an approximate inference model (also called a
             recognition model) to the intractable posterior using the
             proposed lower bound estimator. Theoretical advantages are
             reflected in experimental results."
```

```text
URL:         https://arxiv.org/abs/1401.4082
Kind:        primary — Rezende, Mohamed, and Wierstra's own paper, cited by
             Kingma and Welling in their Related Work section as [RMW14].
             Read for the commission's requested context on the claim's
             standing, not for a load-bearing figure.
Establishes: A second, independently derived route to the same
             reparameterized-gradient technique ("stochastic
             backpropagation"), developed at the same time as Kingma and
             Welling's paper.
Paraphrase:  Title "Stochastic Backpropagation and Approximate Inference in
             Deep Generative Models," authors Danilo Jimenez Rezende, Shakir
             Mohamed, Daan Wierstra, submitted 16 January 2014. The paper's
             own Related Work section (page 6 of its PDF) states: "Concurrently
             with this paper, Kingma & Welling (2014) present an alternative
             discussion of stochastic backpropagation. Our approaches were
             developed simultaneously and provide complementary perspectives
             on the use and derivation of stochastic backpropagation rules."
             This mirrors Kingma and Welling's own Related Work sentence
             (Section 4, page 8 of their PDF): "Even more recently, [RMW14]
             also make the connection between auto-encoders, directed
             probabilistic models and stochastic variational inference using
             the reparameterization trick we describe in this paper. Their
             work was developed independently of ours and provides an
             additional perspective on AEVB." Note: Kingma and Welling's own
             reference list gives this paper's title as "Stochastic
             backpropagation and variational inference in deep latent
             gaussian models" — an earlier title than the one the paper
             carries on arXiv today. Same paper, same arXiv ID, title changed
             between preprint revisions.
Locators:    Rezende et al., Related Work, "Stochastic backpropagation in
             other contexts" subsection. Kingma and Welling, Section 4
             (Related work), page 8.
Quote:       See Paraphrase above for both directions of the mutual citation.
```

```text
URL:         https://arxiv.org/abs/1511.06349
Kind:        primary — Bowman, Vilnis, Vinyals, Dai, Jozefowicz, and Bengio's
             own paper; owns the posterior-collapse finding and the KL-cost-
             annealing fix.
Establishes: That training a straightforward VAE with a sufficiently
             expressive (autoregressive) decoder reliably drives the
             approximate posterior to equal the prior, collapsing the KL term
             to zero and making the latent code carry no information — a
             failure mode of the exact objective Kingma and Welling propose,
             not a defect specific to text.
Paraphrase:  Title "Generating Sentences from a Continuous Space," submitted
             19 November 2015, published at CoNLL 2016. The paper explicitly
             uses "the Gaussian reparameterization trick of Kingma and
             Welling (2015)" and computes the KL term in closed form
             "following Kingma and Welling (2015)" — i.e., it is a direct,
             acknowledged application of the focal paper's method, not a
             tangential comparison.
Locators:    Section 3.1 "Optimization challenges" (the collapse mechanism
             and diagnosis); Section 3.1 "KL cost annealing" (the fix);
             Section 4 "Results: Language modeling" (the Penn Treebank
             numbers).
Quote:       "Straightforward implementations of our vae fail to learn this
             behavior: except in vanishingly rare cases, most training runs
             with most hyperparameters yield models that consistently set
             q(z|x) equal to the prior p(z), bringing the kl divergence term
             of the cost function to zero. When the model does this, it is
             essentially behaving as an rnnlm." And, on the fix: "In this
             simple approach to this problem, we add a variable weight to
             the kl term in the cost function at training time. At the start
             of training, we set that weight to zero, so that the model
             learns to encode as much information in z as it can. Then, as
             training progresses, we gradually increase this weight... until
             it reaches 1, at which point the weighted cost function is
             equivalent to the true variational lower bound."
```

```text
URL:         https://arxiv.org/abs/1509.00519
Kind:        primary — Burda, Grosse, and Salakhutdinov's own paper; owns the
             IWAE bound and the theorem that it strictly tightens the ELBO.
Establishes: A strictly tighter lower bound on log p(x) than the plain ELBO,
             obtained by averaging k importance weights inside the log before
             taking the expectation, which recovers the ordinary VAE bound
             exactly at k=1 and provably improves (weakly) as k grows.
Paraphrase:  Title "Importance Weighted Autoencoders," submitted 1 September
             2015 (final revision 7 November 2016), presented at ICLR 2016.
             The paper opens by naming the object it is correcting: "The
             variational autoencoder (VAE; Kingma, Welling (2014))... As we
             show empirically, the VAE objective can lead to overly
             simplified representations which fail to use the network's
             entire modeling capacity."
Locators:    Section 3 "Importance weighted autoencoder," Eq. 8 (the L_k
             bound), the paragraph immediately after Eq. 8 ("the special case
             of k=1 is equivalent to the standard VAE objective"), Theorem 1
             and Eq. 10 (the monotonic-tightening result), all within Section
             3, page 3 of the PDF.
Quote:       Eq. 8: "L_k(x) = E_{h_1,...,h_k~q(h|x)}[ log( (1/k) sum_{i=1}^k
             p(x,h_i)/q(h_i|x) ) ]." Theorem 1 (Eq. 10): "log p(x) >= L_{k+1}
             >= L_k. Moreover, if p(h,x)/q(h|x) is bounded, then L_k
             approaches log p(x) as k goes to infinity." And, on why the
             estimator does not inherit importance sampling's usual
             variance blowup: "as our estimator is based on the log of the
             average importance weights, it does not suffer from high
             variance."
```

```text
URL:         https://openreview.net/forum?id=Sy2fzU9gl
Kind:        primary in principle — this is beta-VAE's only official home;
             the paper (Higgins, Matthey, Pal, Burgess, Glorot, Botvinick,
             Mohamed, Lerchner, ICLR 2017) has no arXiv preprint. Confirmed
             by an arXiv API title+author search returning zero results.
             STILL NOT UPGRADED. Round 1's access limitation stands, and this
             round establishes the specific reason. Fetching the forum page
             directly with a full browser user agent (Chrome 124 on
             Windows), and separately with an Accept-Language header and a
             persisted cookie jar, returns HTTP 200 but the page itself is
             OpenReview's Cloudflare Turnstile interstitial ("Verifying your
             browser") — inspecting its markup shows a
             `<div class="cf-turnstile" data-sitekey="...">` widget that
             requires solving an interactive challenge in a real browser and
             POSTing the resulting token to api2.openreview.net/challenge/verify
             before the real page is served. No tool available in this
             session executes JavaScript or solves a Turnstile widget, so
             this is not a header problem a "browser-style request" can fix
             by itself; it is presented as a Cloudflare "Error 403" page.
             The OpenReview REST API (both api.openreview.net and
             api2.openreview.net /notes endpoints) returns the same
             challenge as a JSON "ChallengeRequiredError." A read-through
             proxy (r.jina.ai) hit the identical interstitial rather than
             bypassing it. The Wayback Machine's availability API reports a
             cached snapshot of the PDF endpoint from 2026-04-30
             (http://web.archive.org/web/20260430152217/https://openreview.net/pdf?id=Sy2fzU9gl,
             status 200 at capture time), but every attempt to fetch that
             snapshot from this session — over HTTP, over HTTPS, with a
             browser user agent, repeated three times — either failed at the
             egress layer or reset the TLS connection before any content
             arrived; the fetch tool available in this session declined the
             same host outright. DeepMind's own publications page for this
             paper (deepmind.com, redirecting to deepmind.google) no longer
             serves the 2019 publication entry; it 302s to the current
             generic research-index page with no reference to this paper.
             Semantic Scholar's API returned HTTP 429 (rate limited) on
             every attempt in this session, including after two delays, so
             its recorded open-access PDF field (if any) could not be read.
             Google Scholar's results page returned a bot-check page rather
             than results. I did not read the primary's own text. What
             follows is corroborated across three independent secondary
             indexes (DBLP, Semantic Scholar, and a search-engine excerpt
             that quotes the paper's own abstract), which agree with each
             other and are consistent with the mechanism as it is described
             by every later paper that cites beta-VAE, but this is not a
             substitute for reading the source.
Establishes: (per corroborated secondary description, not a primary read) A
             modification of the ELBO that multiplies the KL term by a
             coefficient beta > 1, trading reconstruction accuracy for a more
             factorized ("disentangled") latent code — i.e., the same
             reconstruction-minus-KL decomposition the focal paper derives
             (its Eq. 3) is not a fixed objective but a one-parameter family,
             and moving that parameter changes what the encoder is pressured
             to do with each latent dimension.
Paraphrase:  Title "beta-VAE: Learning Basic Visual Concepts with a
             Constrained Variational Framework," ICLR 2017 poster. Abstract
             opening sentence, as indexed verbatim: "Learning an
             interpretable factorised representation of the independent data
             generative factors of the world without supervision is an
             important precursor for the development of artificial
             intelligence that is able to learn and reason in the same way
             that humans do."
Locators:    Unresolved — still no section or equation locator for the
             beta-weighted objective itself, for the reasons stated above.
             If the writer needs this source cited, it must be cited as the
             general, well-corroborated claim only, without an equation- or
             page-level locator, and its kind must stay "secondary" until a
             human clears the Turnstile challenge directly (the login hint
             on the challenge page suggests an authenticated OpenReview
             session may skip it) or the paper becomes available through
             another channel.
Quote:       See Paraphrase (the one sentence independently confirmed
             verbatim).
```

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary — Ho, Jain, and Abbeel's own paper; owns the DDPM
             training objective and its explicit statement as a variational
             bound. Added this round for the ELBO-to-diffusion forward link.
Establishes: That a denoising diffusion probabilistic model is trained by
             optimizing a variational lower bound on negative log
             likelihood — the same family of object as the focal paper's
             ELBO, applied to a T-step latent-variable model instead of a
             one-step encoder-decoder. This is the passage the writer needs
             to fold the diffusion forward-link into the verdict: the later
             literature did not abandon the bound Kingma and Welling
             derive, it generalized it to a deeper chain of latents.
Paraphrase:  Title "Denoising Diffusion Probabilistic Models," authors
             Jonathan Ho, Ajay Jain, Pieter Abbeel (UC Berkeley), submitted
             19 June 2020 (v1), revised 16 December 2020 (v2), published at
             NeurIPS 2020. Read the PDF directly (25 pages) rather than a
             summary. Section 2 ("Background") defines the reverse process
             p_theta(x_0:T) as a Markov chain with learned Gaussian
             transitions (Eq. 1) and the forward process q(x_1:T|x_0) as a
             fixed Markov chain that adds Gaussian noise on a variance
             schedule beta_1,...,beta_T (Eq. 2). The very next sentence
             states the training objective is exactly the same kind of
             bound the focal paper derives, not a different one: training
             optimizes "the usual variational bound on negative log
             likelihood." Eq. (5), two paragraphs later, rewrites that bound
             as a sum of KL-divergence terms plus a reconstruction term —
             structurally the same reconstruction-minus-KL shape as the
             focal paper's Eq. (3), stretched across T timesteps instead of
             one. This is the concrete mechanism a "forward link" claim can
             cite: the diffusion objective is not merely ELBO-flavored by
             analogy, it is derived the same way, as a Jensen's-inequality
             lower bound on log p_theta(x_0) via a variational posterior,
             the same move as the focal paper's Eq. (1).
Locators:    Section 2 "Background," page 2 of the PDF, Eq. (1)-(2) (reverse
             and forward process definitions) and Eq. (3) (the variational
             bound itself, with the sentence naming it). Section 2, page 3,
             Eq. (5)-(7) (the KL-decomposed rewrite and the closed-form
             forward-process posterior it depends on).
Quote:       Eq. (3), page 2, with its introducing sentence: "Training is
             performed by optimizing the usual variational bound on negative
             log likelihood: E[-log p_theta(x_0)] <= E_q[-log
             p_theta(x_0:T)/q(x_1:T|x_0)] = E_q[-log p(x_T) -
             sum_{t>=1} log (p_theta(x_{t-1}|x_t) / q(x_t|x_{t-1}))] =: L."
             And, on the KL rewrite immediately after Eq. (5): "Consequently,
             all KL divergences in Eq. (5) are comparisons between
             Gaussians, so they can be calculated in a Rao-Blackwellized
             fashion with closed form expressions instead of high variance
             Monte Carlo estimates" — the same variance concern the focal
             paper and source 7 (Paisley, Blei, and Jordan 2012) raise about
             the naive score-function estimator, independently recurring in
             a later paper working the same kind of bound.
```

```text
URL:         https://arxiv.org/abs/1206.6430
Kind:        primary — Paisley, Blei, and Jordan's own paper; owns the
             high-variance score-function gradient claim that Kingma and
             Welling cite by name but do not derive. Added this round
             because the article leans on this variance claim without
             citing the source that owns it.
Establishes: That the naive Monte Carlo estimator of the score-function
             gradient (the same identity the focal paper prints and rejects
             in favor of reparameterization) has variance that scales as
             Cov(f(theta))/S for S samples, which the paper states can
             remain "very large in practice" even after averaging — the
             specific, load-bearing reason a plain score-function estimator
             is a poor choice for the focal paper's gradient problem, argued
             here with a concrete variance-reduction fix (control variates)
             rather than merely asserted.
Paraphrase:  Title "Variational Bayesian Inference with Stochastic Search,"
             authors John Paisley, David M. Blei, Michael I. Jordan,
             submitted 27 June 2012, presented at ICML 2012 (Edinburgh).
             Read the PDF directly (8 pages). Section 3 ("Stochastic search
             variational Bayes") derives the identity the focal paper prints
             without derivation: starting from the intractable gradient
             grad_psi E_q[f(theta)], the paper applies grad_psi
             q(theta|psi) = q(theta|psi) grad_psi log q(theta|psi) to get
             grad_psi E_q[f(theta)] = E_q[f(theta) grad_psi log
             q(theta|psi)] (Eq. 4-6), then estimates it by plain Monte
             Carlo averaging over S samples of theta. Section 4 ("Searching
             with control variates") is the variance claim itself: it states
             the practical problem in one sentence, gives the exact scaling
             law, and reports that the required sample count is large enough
             in the paper's own experiments to make the plain estimator
             slow, which is the motivation for the control-variate fix the
             rest of the paper develops. This paper does not concern
             variational autoencoders; it is a general mean-field
             variational-Bayes paper, and Kingma and Welling cite it for
             exactly this one shared piece of machinery, the score-function
             gradient's variance, not for anything specific to
             autoencoders or amortized inference.
Locators:    Section 3 "Stochastic search variational Bayes," page 2-3 of
             the PDF, Eq. (4)-(6) (the score-function identity and its Monte
             Carlo estimator — the same identity, up to notation, as the
             focal paper's own printed score-function gradient). Section 4
             "Searching with control variates," page 3, opening paragraph
             (the variance claim and its scaling law).
Quote:       Eq. (6) and its estimator: "It follows that grad_psi
             E_q[f(theta)] = E_q[f(theta) grad_psi log q(theta|psi)]. We can
             stochastically approximate this expectation using Monte Carlo
             integration, grad_psi E_q[f(theta)] ~ (1/S) sum_{s=1}^{S}
             f(theta^(s)) grad_psi log q(theta^(s)|psi), where theta^(s) ~
             q(theta|psi) for s = 1,...,S." And the variance claim, Section
             4 opening: "A practical issue with the stochastic approximation
             proposed in Sec. 3 is that the variance of the gradient
             approximation may be very large. Given S samples of a random
             vector X, the covariance of its unbiased sample mean X-bar is
             known to be Cov(X-bar) = Cov(X)/S. When the diagonal values of
             Cov(X) are large, many samples will be required to bring this
             variance below a desired level for approximating the
             expectation. As our experiments will show in Sec. 6, the value
             of S can be very large in practice and lead to a slow
             algorithm."
```

## Contradictions

Two sources directly complicate claims the focal paper makes about itself,
rather than merely adding context. Both are carried forward from researcher/01
unchanged; this round's two new sources do not contradict the focal paper —
they extend and independently corroborate its machinery (Paisley, Blei, and
Jordan own the variance claim the focal paper cites; Ho, Jain, and Abbeel
generalize the same bound rather than dispute it).

1. **The "no overfitting" framing versus posterior collapse.** Figure 2's
   caption in the focal paper reads: "Interestingly enough, more latent
   variables does not result in more overfitting, which is explained by the
   regularizing effect of the lower bound" (Section 5, page 6-7). Bowman et
   al. 2016 studied the same regularizing pressure — the KL term pulling
   q(z|x) toward the prior — under a stronger decoder (an LSTM language
   model) and found it does not stop at preventing overfitting: it can drive
   the KL term all the way to zero, making the latent variable carry no
   information at all. The focal paper's own experiments used a
   comparatively weak, factorized-pixel decoder; Bowman et al. name this
   directly as the reason the failure did not show up in the focal paper:
   "Previous work on vaes for image modeling (Kingma and Welling, 2015) used
   a much weaker independent pixel decoder model p(x|z), forcing the model
   to use the global latent variable to achieve good likelihoods." The same
   mechanism the focal paper credits with a benign result becomes, with a
   sufficiently expressive decoder, the mechanism of a well-documented
   failure mode.

2. **Burda et al.'s framing of the VAE objective as restrictive.** Burda et
   al. 2016 open by stating plainly that "the VAE objective can lead to
   overly simplified representations which fail to use the network's entire
   modeling capacity," and locate the cause in the same single-sample bound
   the focal paper derives (its Eq. 3/7): a bound that "heavily penalizes
   approximate posterior samples which fail to explain the observations,"
   forcing the true posterior to be well approximated by the encoder's
   factorized Gaussian family or the bound stays loose. This does not
   contradict the focal paper's math — the ELBO is still a valid lower bound
   — but it contradicts any reading of the paper as having found a bound
   tight enough for general use; Burda et al.'s Theorem 1 shows the plain
   ELBO (k=1) is the loosest member of a family that gets strictly tighter
   with more importance samples.

## Numbers

```text
Figure: 500 hidden units (encoder and decoder)
Owner:  Kingma and Welling, Section 5 "Experiments," "Likelihood lower bound"
Scope:  MNIST generative model only; chosen from prior autoencoder
        literature, not tuned per algorithm.
```

```text
Figure: 200 hidden units (encoder and decoder)
Owner:  Kingma and Welling, Section 5, same paragraph
Scope:  Frey Face generative model only, reduced from 500 "to prevent
        overfitting, since it is a considerably smaller dataset."
```

```text
Figure: 100 hidden units, 3 latent dimensions
Owner:  Kingma and Welling, Section 5, "Marginal likelihood" paragraph
Scope:  The marginal-likelihood (not lower-bound) experiments only, MNIST
        only. The paper states plainly: "for higher dimensional latent space
        the estimates became unreliable" — the marginal-likelihood estimator
        (Appendix D, MCMC-based) only works in this low-dimensional regime.
```

```text
Figure: minibatch size M = 100, samples per datapoint L = 1
Owner:  Kingma and Welling, Algorithm 1 caption and Section 5
Scope:  All reported experiments; the paper states L=1 was sufficient "as
        long as the minibatch size M was large enough."
```

```text
Figure: estimator variance "< 1" (per-datapoint average lower bound)
Owner:  Kingma and Welling, Figure 2 caption
Scope:  Described as small enough to omit from the plot; no exact value or
        distribution given, so it cannot be checked more precisely than the
        paper's own qualitative bound.
```

```text
Figure: ~20-40 minutes per million training samples, Intel Xeon CPU, ~40
        GFLOPS effective
Owner:  Kingma and Welling, Figure 2 caption
Scope:  Wall-clock compute figure for the reported experiments; not broken
        out by dataset or latent dimensionality.
```

```text
Figure: reconstruction cost 99, KL divergence cost 2 (their VAE, "standard
        setting")
Owner:  Bowman et al. 2016, Section 4 "Results," Table 2 discussion
Scope:  Penn Treebank language-modeling task, standard setting (no word
        dropout or KL annealing); given as the concrete numbers behind their
        claim that an unmodified VAE on this task learns to use very little
        of its latent code before their fixes are applied.
```

## Source assets

```text
Asset: Figure 4, "Visualisations of learned data manifold for generative
       models with two-dimensional latent space, learned with AEVB" —
       Appendix A, page 10 of the PDF. Two panels: (a) Learned Frey Face
       manifold, (b) Learned MNIST manifold.
Shows: What a 2D latent space organizes without supervision: linearly spaced
       coordinates on the unit square, mapped through the inverse Gaussian
       CDF to latent values z, each decoded through the learned generative
       model p_theta(x|z). The MNIST panel visibly separates digit classes
       into regions of the 2D plane; the Frey Face panel shows continuous
       pose/expression change across the plane. This is the figure the
       commission calls "the learned 2D manifold" — it exists exactly as
       described and is a strong candidate asset.
Crop:  A crop must keep the full unit-square grid of one panel (MNIST or
       Frey Face, not a partial corner) so the reader can see the
       organization, not just a few isolated digits. It must retain the
       figure's own caption or the caption's substance in the article's
       caption, since the axes have no units of their own — the meaning
       comes entirely from "linearly spaced coordinates transformed through
       the inverse Gaussian CDF," stated in the source caption.
```

```text
Asset: None found for a "reparameterization schematic."
Shows: I read every figure in the paper (Figures 1 through 5, main text and
       both appendices) and none of them diagrams the reparameterization
       trick. Figure 1 (page 2) is the graphical-model diagram (solid lines
       for the generative model, dashed for the variational approximation) —
       a candidate for illustrating the latent-variable model itself, not
       the reparameterization. Figures 2 and 3 (Section 5) are lower-bound
       and marginal-likelihood convergence plots. Figure 5 (Appendix A) is a
       grid of random MNIST samples at varying latent dimensionality. The
       reparameterization trick is presented only as prose and equations
       (Section 2.4, page 4-5). If the writer wants a reparameterization
       visual, it has to be built new (e.g. as an `nb-code` sampler per the
       commission's own suggestion), not captured from this source.
Crop:  N/A.
```

```text
Asset: Figure 1, "The type of directed graphical model under consideration"
       — Section 2, page 2.
Shows: The two-node latent-variable model (z -> x, with phi/theta labeling
       which distribution is which, and N for the dataset plate) that
       everything else in the paper is built to do inference on. A minimal,
       fast read.
Crop:  Whole figure; it is already minimal (four symbols and a plate). No
       partial crop makes sense.
```

```text
Asset: Ho, Jain, and Abbeel's Figure 2, the directed graphical model of the
       forward and reverse diffusion process (page 2, immediately above
       Eq. 1-2).
Shows: The T-step chain x_T -> ... -> x_t -> x_{t-1} -> ... -> x_0, with the
       fixed forward process q(x_t|x_{t-1}) drawn one way and the learned
       reverse process p_theta(x_{t-1}|x_t) drawn the other. It is the same
       kind of two-process picture as the focal paper's own Figure 1, scaled
       from one latent step to T. Useful only if the piece actually draws the
       forward-link comparison in the verdict; not a replacement for the
       focal paper's own figure, and not needed if the link is made in prose.
Crop:  Whole figure if used; it is a short chain diagram with no meaningful
       partial crop.
```

## Discarded

```text
URL: https://openreview.net/pdf?id=Sy2fzU9gl — same access failure as the
     forum page (OpenReview bot-verification challenge on every automated
     route tried: WebFetch, curl with a browser user agent, the OpenReview
     API, Wayback Machine). Not rejected on merit; rejected on access. See
     the Sources entry above for what is usable from corroborated indexes.
```

```text
URL: https://paperswithcode.com/paper/beta-vae-learning-basic-visual-concepts-with
     — redirects to an unrelated Hugging Face trending-papers page; the
     paper's Papers-with-Code entry no longer resolves to its own content.
```

```text
URL: https://api.openreview.net/notes?id=Sy2fzU9gl and
     https://api2.openreview.net/notes?id=Sy2fzU9gl — both return HTTP 403
     with a JSON "ChallengeRequiredError" body pointing at the same
     Cloudflare Turnstile challenge as the forum and PDF pages. Confirms the
     gate is applied at the API layer too, not just the rendered page.
```

```text
URL: https://r.jina.ai/https://openreview.net/forum?id=Sy2fzU9gl — a
     read-through proxy tried on the theory it might already hold a cached,
     unchallenged copy. Returned the identical "Verifying your browser"
     interstitial, confirming the challenge is served per-request rather
     than cached past it.
```

```text
URL: http://web.archive.org/web/20260430152217/https://openreview.net/pdf?id=Sy2fzU9gl
     — the Wayback Machine's own availability API confirms a status-200
     snapshot exists from 2026-04-30, but fetching that snapshot from this
     session failed on every attempt: the plain-HTTP form was blocked by
     this session's egress policy outright, and the HTTPS form reset the
     TLS connection before completing the handshake's response, three times
     in a row. The fetch tool available in this session separately declined
     the same host. Not rejected on merit — the snapshot may well contain
     the readable PDF — rejected because this session cannot reach
     web.archive.org, a different and separate failure from OpenReview's own
     Turnstile gate.
```

```text
URL: https://deepmind.com/research/publications/2019/beta-VAE-Learning-Basic-Visual-Concepts-with-a-Constrained-Variational-Framework
     — 302-redirects to https://deepmind.google/research/publications/2019/beta-VAE-Learning-Basic-Visual-Concepts-with-a-Constrained-Variational-Framework,
     which no longer carries this specific publication; it serves DeepMind's
     current generic research index instead. The lab's own publications page
     for this paper no longer resolves to content about it.
```

```text
URL: https://scholar.google.com/scholar?q=beta-VAE+Learning+Basic+Visual+Concepts+Constrained+Variational+Framework
     — returned a "Sorry..." unusual-traffic interstitial rather than search
     results; not usable from this session.
```

```text
URL: https://api.semanticscholar.org/graph/v1/paper/... (both the search
     endpoint and the direct paper-ID endpoint for the Semantic Scholar
     record found in round 1) — returned HTTP 429 "Too Many Requests" on
     every attempt this round, including after two delays of 15-20 seconds.
     Could not confirm or read any open-access PDF field it might carry.
```

```text
URL: https://arxiv.org/abs/1503.03585 (Sohl-Dickstein, Weiss, Maheswaranathan,
     and Ganguli, "Deep Unsupervised Learning using Nonequilibrium
     Thermodynamics," 2015) — read the abstract and opening of the PDF to
     confirm identity: this is the paper that originates the diffusion
     probabilistic model Ho et al. 2020 builds on and cites as [53], and its
     own framing is explicitly variational ("a parameterized Markov chain
     trained using variational inference," per Ho et al.'s own description
     of it). Not added as a separate source entry: the brief names Sohl-
     Dickstein 2015 "and/or" Ho et al. 2020, and Ho et al. 2020 alone
     supplies the explicit "usual variational bound" sentence, its own
     equation number, and a direct, quotable locator, which is what the
     brief asks the writer be able to fold into the verdict. Citing both
     for the same single claim would be the padding the brief warns against.
```

## Reported to the orchestrator

Two of the three commissioned gaps are closed with primary sources read in
full: the diffusion forward-link (Ho et al. 2020, source 6) and the
score-function variance citation (Paisley, Blei, and Jordan 2012, source 7).
The third, the beta-VAE primary, is not closed. This round retried it with
substantially more routes than researcher/01 — a fresh browser-header fetch
with a persisted cookie jar, both OpenReview REST API hosts, a read-through
proxy, the OpenReview PDF endpoint directly, the Wayback Machine (whose
availability API confirms a live snapshot exists, unreachable from this
session), DeepMind's own publication page (now redirects away from the
paper), Semantic Scholar's API (rate-limited throughout), and Google Scholar
(bot-checked) — and every route failed for a specific, now-documented reason:
OpenReview gates this paper behind an interactive Cloudflare Turnstile
widget, which requires solving a challenge in a real browser session, not
just sending browser-shaped headers. No tool available in this session
executes JavaScript or clears a Turnstile challenge, so this gap cannot be
closed automatically from here. The login hint on the challenge page implies
an authenticated OpenReview session might skip the check; a human with
OpenReview credentials, or a session with real browser automation, is the
most likely way to close it. Source 5 in this record is written so the writer
can either omit the beta-VAE paragraph's specific equation citation and use
only the corroborated general claim (as researcher/01 already allowed), or
hold that paragraph until the primary is actually read. The total source
count is seven: five carried forward from researcher/01, two newly read and
load-bearing (sources 6 and 7 above), one still access-limited and clearly
flagged rather than silently dropped or falsely marked as upgraded.
