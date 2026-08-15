# Evidence: paper-of-the-day/variational-autoencoder (researcher/01)

The focal paper was read in full (all 14 pages of the current arXiv version,
including every appendix) by downloading the PDF and extracting its text
directly, so every equation number, figure caption, and experimental claim
below was checked against the paper's own typeset text, not a summary. The
ELBO decomposition, the SGVB estimator, the reparameterization identity, and
the two named figure candidates are all locatable and quotable with page-level
precision. The after-record is solid on two of three planned sources: Bowman
et al. 2016 and Burda et al. 2016 were read in full from their own arXiv PDFs,
including the exact sentences that bear on posterior collapse and on the IWAE
bound. Higgins et al. 2017 (beta-VAE) is the one gap: its only home is an
OpenReview forum page, and every automated route to it (direct fetch, a
browser-header curl, the OpenReview REST API, a Wayback Machine lookup) hit
the same bot-verification wall in this session. Its title, author list, venue,
and abstract's first sentence are independently corroborated across DBLP,
Semantic Scholar, and a search-engine-indexed excerpt of the paper's own
abstract, and the beta-weighted-KL mechanism is stated identically across all
of them, but I have not read the primary's own page directly. That gap is
flagged everywhere it matters below. One correction to the commission's own
premise: the paper contains no "reparameterization schematic" figure. I read
every figure in it (Figures 1 through 5) and only two are diagrams; the
reparameterization trick is presented as prose and equations only. The
writer's two figure candidates should be understood as one real asset (the 2D
manifold, Figure 4) and one that does not exist in this source.

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
             shown derivation, at this exact step.)

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
             ACCESS LIMITATION: every automated route into this page failed
             in this session — a direct fetch, a browser-header curl, the
             OpenReview REST API (api.openreview.net/notes), and a Wayback
             Machine lookup all returned an OpenReview bot-verification
             challenge page instead of content. I did not read the primary's
             own text. What follows is corroborated across three independent
             secondary indexes (DBLP, Semantic Scholar, and a search-engine
             excerpt that quotes the paper's own abstract), which agree with
             each other and are consistent with the mechanism as it is
             described by every later paper that cites beta-VAE, but this is
             not a substitute for reading the source.
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
Locators:    Unresolved — I could not open the paper to give a section or
             equation locator for the beta-weighted objective itself. The
             orchestrator or writer should either retry access (a human
             browser will very likely clear OpenReview's challenge where
             automated fetches cannot) or treat this source as usable only
             for the general, well-corroborated claim above, without a
             specific equation citation.
Quote:       See Paraphrase (the one sentence independently confirmed
             verbatim).
```

## Contradictions

Two sources directly complicate claims the focal paper makes about itself,
rather than merely adding context.

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
