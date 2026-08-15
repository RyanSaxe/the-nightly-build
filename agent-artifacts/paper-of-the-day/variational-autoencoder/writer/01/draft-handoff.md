# Draft handoff: paper-of-the-day/variational-autoencoder (writer/01)

## Original work

The article builds the chain of reasoning the evidence only supplies as
separate facts: it shows step by step why the ELBO's gradient with respect to
phi is intractable, demonstrates in an original `nb-code` contrast exactly
what the reparameterization substitution changes about that gradient, and
then uses that same substitution to argue that the paper's "no overfitting"
claim in Figure 2 is a property of its specific weak decoder rather than of
the lower bound itself, turning the evidence's separately recorded
contradiction (Bowman et al. vs. the focal paper) into the piece's
throughline verdict.

## Proof result

`./nb check --series paper-of-the-day
.nb-work/paper-of-the-day/variational-autoencoder/library/paper-of-the-day/variational-autoencoder.html
--library /home/user/library-checkout`, links included, after `nb stamp`:

```
BLOCK: 0
WARN:  4
verdict: PUBLISHABLE
```

(2818 words, 5 sources, 12 min read, per the final `nb stamp`.)

Warnings left standing, and why:

- **W-SENTENCE-DENSITY x2, on the annotated ELBO equation and the generic
  SGVB-estimator equation.** Both flagged "sentences" are the raw TeX inside
  an `nb-math-eq`/`nb-math-in` node, not prose; the density heuristic counts
  their internal commas, braces, and subscripts as punctuation weight. The
  published `denoising-diffusion.html` carries five equivalent warnings from
  its own equations for the same reason, so this is a known, accepted
  category rather than a prose failure.
- **W-SENTENCE-DENSITY x1, on the Bowman et al. verbatim quote**
  ("Straightforward implementations of our vae fail to learn this
  behavior..."). The quote's own parenthetical notation, `q(z|x)` and `p(z)`,
  plus one internal colon push its punctuation score over the threshold. It
  is reproduced exactly as published; shortening or repunctuating it would
  mean not quoting the source verbatim, which the citation standard requires.
- **W-SOURCES-MIN: 5 sources against the series floor of 8.**
  researcher/01's evidence record confirms exactly five usable sources:
  Kingma & Welling; Rezende, Mohamed & Wierstra; Bowman et al. 2016; Burda et
  al. 2016; and beta-VAE, cited to its DBLP index entry because every
  automated route into the primary's OpenReview page (direct fetch, a
  browser-header curl, the OpenReview API, Wayback, and my own WebFetch retry
  this round) returned the same bot-verification wall. I did not pad the
  count with a source I have not read. Closing this warning legitimately
  needs a researcher round that finds further sources actually worth citing,
  not a citation-count exercise.

## Open question

Would a human-browser retry at OpenReview (`https://openreview.net/forum?id=Sy2fzU9gl`)
be worth a dedicated attempt, to upgrade beta-VAE from a DBLP-sourced
secondary citation to a primary read with its own equation-level locator? A
same-attempt research round could also look for two or three more
legitimately relevant sources (e.g., a closed-form derivation of the
naive estimator's variance, or a source on the VAE's role as diffusion's
training-objective ancestor) to close W-SOURCES-MIN honestly, if the paper
wants that warning cleared rather than left as a documented, evidence-bound
shortfall.
