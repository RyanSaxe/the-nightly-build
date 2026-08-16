# Commission: paper-of-the-day/adversarial-examples

## The paper
Goodfellow, Shlens, and Szegedy, "Explaining and Harnessing Adversarial
Examples," ICLR 2015 (arXiv:1412.6572). Its central claim is an explanation: the
tiny, imperceptible perturbations that flip a confident classifier come mainly
from the linear behavior of neural networks in high dimensions, not from
overfitting or excess nonlinearity, which was the original suspicion in Szegedy
et al. 2013. From that linear view the paper derives a fast attack, the fast
gradient sign method, and proposes adversarial training as a regularizer.

The paper qualifies for this desk because its central claim is a mechanism that
can be reconstructed and then weighed against a decade of what followed: the
explanation was influential, partly right, and later reframed. That gives the
article something to examine, not a famous result to announce.

## What the reconstruction must rebuild, from the paper's own artifacts
- The linear explanation. Set the math the argument turns on: for a weight
  vector and a perturbation bounded in max-norm by epsilon, the change in the
  activation grows with the input dimension, so a per-pixel change too small to
  see moves the pre-activation by a large amount. This is the paper's key step;
  set it, do not paraphrase it.
- The fast gradient sign method: the perturbation is epsilon times the sign of
  the gradient of the loss with respect to the input. Set the equation and say
  why the sign, given the max-norm constraint, is the fastest increase.
- Figure 1, the panda that becomes a gibbon under a 0.007 perturbation, brought
  in as a source asset with a caption stating exactly what it settles
  (imperceptible perturbation, high-confidence wrong label). This is the figure
  the claim turns on; the article should spend what it shows.
- Adversarial training as the paper frames it, the loss that mixes clean and
  FGSM-perturbed examples, if the piece has room to land it.

## What the article must weigh (the public record)
Rebuild the claim, then judge it against what happened next. The linear
explanation captured real things: perturbations are cheap, gradient-aligned, and
transfer between models, and FGSM plus adversarial training became the field's
starting point. It did not survive as the whole story. Later work reframed the
cause as the data's non-robust-but-predictive features rather than a model
artifact to regularize away (Ilyas et al. 2019), documented a robustness-
accuracy tension (Tsipras et al. 2019), showed most defenses gave a false sense
of security under proper attack (Athalye et al. 2018; Carlini and Wagner 2017),
and left projected-gradient adversarial training (Madry et al. 2018) as the
durable, still-costly baseline. The verdict the article earns: where the linear
view was right, and where "linearity explains adversarial examples" turned out
to be incomplete.

## Boundaries
- Reconstruct with the paper's artifacts and set the math; a reconstruction that
  only describes the figures underuses the material.
- The declared reader has an ML background: use the field's terms exactly, and
  spend the space on the argument, not on defining gradient descent.
- Weigh, do not both-sides. Commit to the synthesis the record supports, and
  hold it to a higher bar precisely because "adversarial examples are famous" is
  the crowd's read.

## Sources
Template floor is 8. Expect the paper itself, Szegedy et al. 2013 (Intriguing
properties, arXiv:1312.6199), Madry et al. 2018 (arXiv:1706.06083), Athalye et
al. 2018 (Obfuscated Gradients, arXiv:1802.00420), Carlini and Wagner 2017
(arXiv:1608.04644), Ilyas et al. 2019 (arXiv:1905.02175), Tsipras et al. 2019
(arXiv:1805.12152), and one current survey or benchmark of the robustness state
(for example RobustBench). Read the passages; cite what is read.

## Habits to break (recent paper desk)
The desk's recent headline and dek mold is "the paper's own proof or measurement
leaves out its claim" (batch normalization never measured internal covariate
shift; GANs train a loss their optimality proof leaves out; word2vec's demo
predates word2vec). This paper's story is different, a proposed explanation
partly right and later reframed, so do not force it into that mold. The GAN piece
(theorem versus Algorithm 1) is recent; do not mirror its structure. Reconstruct
with nb-math and nb-figure where earned and close on the piece's own weighing,
not a stamped "what the paper is right about" heading.

## Neighbors this run
Tech News is also in production and is AI-central for 2026-08-16. That desk
covers the day's developments; this piece reconstructs a 2015 paper. If Tech
News surfaces an adversarial-robustness news item, the boundary still holds: news
there, reconstruction here. No cross-reference is needed.

## Production record
- Harness: `claude-code-routine`. Writer model recorded in nb-meta: `claude-opus`.
- Effort by role: writing-coach low, researcher high, writer medium, editor high
  (required). Roles run as in-process children on the routine's session model;
  where a stage's configured effort cannot be set explicitly, the closest
  available setting on that model is used. No `required` directive was traded
  down.
- Source policy: `{"templates": {"paper": {"min_sources": 8}}}`.
