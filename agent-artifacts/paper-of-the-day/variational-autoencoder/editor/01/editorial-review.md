# Editorial review: paper-of-the-day/variational-autoencoder (editor/01)

## Skeptic

Thesis: Kingma and Welling's contribution reduces to one substitution.
Sampling fixed noise and building the latent code from it by arithmetic,
rather than sampling the code directly, moves the randomness outside the part
of the computation the encoder parameters shape, so an ordinary backward pass
can train encoder and decoder together. The piece then weighs that claim as a
reviewer: the marginal-likelihood evidence is thin, the "regularizes without
cost" reading is a property of the specific weak decoder, and the bound is the
loosest member of a family later work tightened. The reparameterization
substitution is what survives.

Claims it stands on, and how each held:

1. **The ELBO decomposition and its consequence.** Recomputed both equations
   against the evidence locators. Eq. (1), `log p(x) = KL(q‖p(z|x)) + L`, is
   the exact identity; since KL is non-negative, `L` is a lower bound, and for
   fixed theta the two right-hand terms sum to a quantity independent of phi,
   so raising `L` in phi can only shrink the KL to the true posterior. The
   article's sentence that maximizing the bound and closing the gap to the
   true posterior are the same optimization is therefore earned, not asserted.
   Eq. (3), `L = -KL(q‖p(z)) + E_q[log p(x|z)]`, is a valid rewrite of Eq. (2)
   via `log p(x,z) = log p(x|z) + log p(z)`. The annotated legend labels each
   term correctly. Held.

2. **Why the phi-gradient is intractable and what the substitution changes.**
   This is the throughline's load-bearing step, so I pushed hardest here. The
   score-function identity the piece prints,
   `∇_φ E_{q_φ}[f] = E_{q_φ}[f·∇_φ log q_φ]`, is correct (it uses
   `∇q = q·∇log q` and assumes `f` independent of phi). The reparameterization
   argument is correct, not merely plausible: the change of variables
   `z = g_φ(ε, x)`, `ε ~ p(ε)` turns the expectation over the phi-shaped
   `q_φ(z|x)` into an expectation over a fixed `p(ε)` phi has no say over, so a
   plain Monte Carlo average estimates it and the gradient reaches phi through
   the deterministic `g_φ` like any other layer. The Gaussian instance
   `z = μ + σ⊙ε` is the worked case, differentiable in mu and sigma with only
   epsilon random. Held. One wording repair below: the draft said the gradient
   had "no path through a discrete draw," which mis-signals for an expert
   reader, since the latents here are continuous and the trick works precisely
   because they are. Fixed to "no differentiable path through the random draw."

3. **The "no overfitting" reading as a decoder property.** The focal paper's
   Figure 2 caption is quoted verbatim and attributed correctly. Bowman et
   al.'s posterior-collapse quote and their explicit diagnosis that Kingma and
   Welling's "much weaker independent pixel decoder" forced latent use are both
   verbatim and correctly attributed to source 3. The reading that the same KL
   term is benign under a weak decoder and the cause of collapse under a strong
   one is exactly the contradiction the evidence records, correctly earned and
   correctly owned by Bowman rather than invented. Held.

4. **The bound is the loosest of a tightening family.** IWAE's `L_k` is
   transcribed faithfully (the piece harmonizes Burda's `h` to its own `z`,
   which is honest); k=1 recovers the ELBO by direct expansion, and Theorem 1
   gives the monotonic tightening. Held.

Display text checked descriptor by descriptor. Title "Auto-Encoding
Variational Bayes," authors, venue ICLR 2014, and arXiv:1312.6114 in the paper
card are correct. The abstract blockquote is verbatim against the evidence.
Every number in the experiments section (500/200 hidden units, minibatch 100,
one sample, 100 units and 3 latent dimensions for the marginal-likelihood run,
Bowman's 99-vs-2 costs) matches the evidence with correct locators. Every
named person's role is right. The headline is a claim the piece defends; the
dek makes a claim about the world (what the paper did) rather than grading the
article, and adds the mechanism the headline omits.

Citations: I opened all five hrefs as printed. Sources 1-4 resolve to the
correct arXiv papers; source 5 resolves to the DBLP record for beta-VAE. None
is a broken or redirected link. Every `data-nb-kind` is honest: sources 1-4
are the authors' own papers (primary); source 5 is labeled secondary because
it is a bibliographic index and the researcher could not read the primary, and
its citation note says exactly that. Nothing hides a missing independent
source behind a wrong label.

No broken central claim and no fabrication. One editorial gap belongs to the
sources floor and is routed below, not to any factual break.

## Cut

Sentence-by-sentence against `spec/slop.md`, then the edges alone, then the
delete test. Six sentences failed and were cut or repaired:

- **A self-referential signpost.** "The identity does more than name a bound"
  announced a turn the next sentence already makes. Cut; the reasoning that
  follows stands without it.
- **A doubled "the paper's real move" framing.** The orientation stacked "the
  paper's actual departure" against "the paper's real move comes next," a
  hype escalation that also signposted where the piece was headed. Merged into
  one sentence that keeps every fact (train a second network, rewrite the
  objective, one substitution in sampling) and drops the signpost.
- **Self-grading.** "It is worth naming plainly rather than passing over" is
  the article congratulating itself for naming the variance gap instead of
  naming it. Cut. The substantive point (the paper argues the high-variance
  claim by citation, not derivation) stays.
- **A "where we go next" signpost.** "It does not change what the paper does
  next, which is abandon this estimator and build a different one" bridges to a
  section whose own heading already makes the bridge. Cut.
- **An unearned punchline.** "It was the thing the objective needed" restated
  the prior sentence's synthesis as a quotable closer. Cut; the reported fact
  (two independent, simultaneous derivations) carries the point.
- **A doubled negative-parallelism plus self-reference in the beta-VAE
  paragraph.** The draft said the terms were treated "not as fixed, but as a
  dial," then "not a single fixed trade after all. It is one setting of a
  knob," stating the same idea twice in "not X, but Y" form, and pointed at
  "the decomposition this piece annotated earlier." Rewritten to state the
  one-parameter-family point once, positively, without the self-reference and
  without altering the sourced claim (beta > 1 trades reconstruction for a more
  factorized code).

One comma splice repaired: "Call the second network q_phi(z|x), the paper's
own name for it is a recognition model" joined two independent clauses with a
comma. Recast the second as a relative clause.

The three `W-SENTENCE-DENSITY` warnings the writer left standing are the
genuinely-unavoidable category, not maskable slop. Two flag raw TeX inside the
ELBO and SGVB equations, where the heuristic counts subscripts and braces as
punctuation weight; the equations are transcribed verbatim from the paper and
must stay. The third flags the Bowman quotation, whose internal `q(z|x)`,
`p(z)`, and colon push the score over threshold; it is reproduced exactly and
cannot be repunctuated without ceasing to be a verbatim quote. The published
denoising-diffusion piece carries the same equation-driven warnings. I concur
with leaving all three.

Furniture and formula check against the recent record. The vision-transformer
piece's numeric-finding heading formula and its closing `nb-note-strong`
verdict box are both avoided: the headings are argument steps in the piece's
own nouns, varied in construction, and the verdict lives in prose in the final
section, as the brief and voice guide require. The one annotated equation
respects the at-most-one rule. The `nb-code` contrast and the manifold figure
each carry evidence rather than decorate. No borrowed phrasing from the voice
guide's exemplars and no prompt leakage from the briefs or commission survived
into the draft.

## Reader

Read straight through as the paper's declared reader, I come away with the
causal chain the sources supply only as separate facts: why the phi-gradient is
intractable, what the reparameterization substitution changes about it, and why
that same substitution reframes the paper's own "no overfitting" caption as a
statement about its weak decoder once Bowman's collapse result is set beside it.
The evidence record holds those as discrete entries; the article builds them
into one argument, which matches the original-work sentence in the draft
handoff. The prose sits closer to the voice-guide exemplars than to a median
summary: concepts are earned before they are used (Olah's order), citations
land in the clause that defines the method (Weng's habit), and the evaluation
states what was measured and what it does not license (Hashimoto's scoping).
The headline reads true as the largest claim.

## Edits

- Orientation: merged "The paper's real move comes next..." into one sentence,
  removing the doubled "actual departure / real move" signpost while keeping
  every fact.
- Posterior-network: repaired the comma splice in "Call the second network
  q_phi(z|x)..." to a relative clause.
- Posterior-network: cut the signpost sentence "The identity does more than
  name a bound."
- Gradient-problem: changed "no path through a discrete draw" to "no
  differentiable path through the random draw," removing a term that
  mis-signals discreteness for a continuous-latent method.
- Gradient-problem: cut the self-grading clause "and it is worth naming plainly
  rather than passing over" and the signpost sentence "It does not change what
  the paper does next, which is abandon this estimator and build a different
  one."
- Reparameterization: cut the punchline "It was the thing the objective
  needed."
- Verdict / beta-VAE paragraph: rewrote to remove the self-reference "the
  decomposition this piece annotated earlier," the doubled dial/knob
  "not X, but Y" pair, keeping the sourced disentanglement claim intact.

## Required work

- **researcher** — Sources floor. The article stands at five sources against
  the series floor of eight and the commission's explicit "at least 8." I rule
  that the five do not carry it, because real, readable, load-bearing sources
  exist and would strengthen the piece rather than pad it. A targeted round-02
  should read: (1) a denoising-diffusion primary (for example Ho et al. 2020 or
  Sohl-Dickstein et al. 2015) to support the ELBO-to-diffusion forward link the
  commission named in its after-record but the draft omits entirely; (2) the
  beta-VAE primary via a human-browser retry at OpenReview, to upgrade source 5
  from an unread DBLP secondary to a primary with an equation-level locator;
  (3) at least one further genuinely relevant source, the strongest candidate
  being Blei, Jordan, and Paisley 2012, which the piece already leans on by name
  for the high-variance claim and does not yet cite as a source of its own.
  Doersch's VAE tutorial is an acceptable fourth candidate for the exposition.
  Do not add a source that is not read and load-bearing; the count is not the
  goal, the missing after-record link and the uncited variance result are.
- **writer** — Integrate whatever round-02 returns: weave the diffusion
  forward-link into the verdict where the commission asked for it, attach the
  variance citation at the score-function step, and upgrade the beta-VAE
  citation (kind, locator, and note) if the primary is recovered. This is
  reporting-dependent, so it follows the researcher round. No redraft is
  needed; the argument, math, and structure hold.

## Decision

revise — the math, citations, sourcing labels, and prose are sound after this
round's edits, but the piece publishes below the owner's sources floor when
real, load-bearing sources (the missing diffusion forward-link, the uncited
variance result, the recoverable beta-VAE primary) would both meet the floor
and strengthen it, so the sources round is owed before approval.
