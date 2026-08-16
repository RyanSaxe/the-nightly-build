# Voice guide: paper-of-the-day/adversarial-examples (01)

## How this piece should sound

This is a reconstruction of one paper for readers who already work in machine
learning, so it can move at the speed of an argument and skip the tutorial. Two
registers live inside it. Rebuilding the linear explanation and the fast
gradient sign method wants the patience of Olah and Weng: build each idea before
the sentence that spends it, and let the reader feel why a per-pixel change
bounded in max-norm can move a pre-activation by a large amount before the
inequality that says so arrives. Weighing the claim against the decade that
followed wants the first-principles calm of Huszár: grant the strongest version
of the explanation before saying where it stops.

Take the patience from Olah's opening passage. He tells the reader what the
section will deliver and why the restriction to low-dimensional networks buys
clarity, then earns it. The linear view has the same shape available: the
intuition the epsilon bound rests on can be stated before the algebra, so the
equation confirms something the reader already sees rather than introducing it
cold.

When the reconstruction sets its math, Weng's Earth Mover passage shows one way
to keep it legible. She puts a concrete reading of the quantity next to the
notation, so the metric is understood before it is written down. The same is
available here: the sign of the gradient, the max-norm constraint, and why that
sign gives the fastest available increase can each carry an intuition in the
prose while the equation stands as the record.

The figures are evidence, and Olah's visualization passage shows what reading
one looks like. He says what the picture is doing in plain verbs before he
states the outcome. Figure 1, the panda relabeled a confident gibbon under a
tiny perturbation, invites the same treatment: prose that says what the panel
settles in the article's own words rather than a restatement of the caption.

The verdict is the writer's to reach from the evidence, and Huszár's passages
show the temperament it asks for. He concedes what maximum likelihood gets right
in the ideal case before naming the practical regime where it fails, and when a
formal distinction could blur he fixes it with a plain characterization the
reader can hold. The weighing here has the same demands. Where it reaches a
distinction a reader could run together, a plain sentence can keep the two
apart; where a later result revises the original claim, conceding what the
explanation genuinely captured makes the revision more convincing than a
dismissal would. Olah's scoping passage is the companion move: he bounds a claim
to the setting that produced it the moment it might mislead, which is the
instinct a reconstruction needs when it says how far the linear view reaches.

The reader holds the field's vocabulary, so let the terms carry their exact
weight: perturbation, max-norm, the sign of the gradient, transfer between
models, the robustness of a classifier under attack. Spend the space on the
argument the paper makes and the record that tested it.

## Chris Olah, "Neural Networks, Manifolds, and Topology"

Source: https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/

> "While it is challenging to understand the behavior of deep neural networks in general, it turns out to be much easier to explore low-dimensional deep neural networks – networks that only have a few neurons in each layer. In fact, we can create visualizations to completely understand the behavior and training of such networks."

Olah names the hard general problem and then narrows to the case he can actually
show, and he says why the narrowing helps before he uses it. "In fact, we can
create visualizations to completely understand" commits to a payoff the rest of
the piece delivers. The person is visible in the confidence to promise complete
understanding and then set about earning it.

> "In the following visualization, we observe a hidden representation while a network trains, along with the classification line. As we watch, it struggles and flounders trying to learn a way to do this."

Olah describes a training animation in verbs a reader can watch for, "struggles
and flounders", so the figure is read rather than only pointed at. He tells you
what to look for before he tells you how it turns out. Where he shows: he trusts
a plain, almost physical account of what the network is doing over a technical
restatement of it.

> "It is worth explicitly noting here that these tasks are only somewhat challenging because we are using low-dimensional neural networks. If we were using wider networks, all this would be quite easy."

Olah stops to bound his own demonstration, conceding that the difficulty is an
artifact of the low-dimensional setting and would vanish with width. The claim
about difficulty is tied to the conditions that produced it. The person shows in
the willingness to deflate his example the instant it might mislead.

## Lilian Weng, "From GAN to WGAN"

Source: https://lilianweng.github.io/posts/2017-08-20-gan/

> "Generative adversarial network (GAN) has shown great results in many generative tasks to replicate the real-world rich content such as images, human language, and music. It is inspired by game theory: two models, a generator and a critic, are competing with each other while making each other stronger at the same time. However, it is rather challenging to train a GAN model, as people are facing issues like training instability or failure to converge."

Weng states what a GAN is and, in the same breath, the concrete trouble that
motivates the whole post: instability, failure to converge. The register is
plain and declarative, and the difficulty is reported as fact rather than
staged. Weng's habit is to lay out the plan of the piece early and keep the
sentences short enough to follow.

> "Wasserstein Distance is a measure of the distance between two probability distributions. It is also called Earth Mover's distance, short for EM distance, because informally it can be interpreted as the minimum energy cost of moving and transforming a pile of dirt in the shape of one probability distribution to the shape of the other distribution. The cost is quantified by: the amount of dirt moved x the moving distance."

Weng attaches a physical picture to the metric before the formula appears: piles
of dirt, and a cost that is the amount moved times the distance. The quantity
becomes something the reader can hold before it is written down, so the notation
that follows confirms an intuition instead of supplying one. Her move is a
concrete, almost tactile reading of an abstract measure.

> "Sadly, Wasserstein GAN is not perfect. Even the authors of the original WGAN paper mentioned that "Weight clipping is a clearly terrible way to enforce a Lipschitz constraint" (Oops!). WGAN still suffers from unstable training, slow convergence after weight clipping (when clipping window is too large), and vanishing gradients (when clipping window is too small)."

Weng weighs the method she has just built and does not cushion the finding,
quoting the original authors' own admission and then listing the specific ways
the method fails. The judgment rests on the record and on the authors' words,
not on her impression. Where she shows: the flatness of "not perfect" set
against the exact failure modes that follow it.

## Ferenc Huszár, "How (not) to Train your Generative Model: Scheduled Sampling, Likelihood, Adversary?"

Source: https://www.inference.vc/how-to-train-your-generative-models-why-generative-adversarial-networks-work-so-well-2/

> "The key organising principle should be this: the objective function we use for training a probabilistic model should match the way we ultimately want to use the model. Yet, in unsupervised learning this is often overlooked and I think we lack clarity around what the models are used for and how they should be trained and evaluated."

Huszár states a first principle in one plain sentence and then names the
field-wide gap it exposes, so the criticism that follows has a stated premise
under it. The argument is built rather than asserted. Huszár's manner is calm
and first-person, willing to say plainly what he thinks the field has skipped.

> "I argue that when the goal is to train a model that can generate natural-looking samples, maximum likelihood is not a desirable training objective. Maximum likelihood is consistent so it can learn any distribution if it is given infinite data and a perfect model class. However, under model misspecification and finite data (that is, in pretty much every practically interesting scenario), it has a tendency to produce models that overgeneralise."

Huszár grants what maximum likelihood gets right in the ideal case, infinite
data and a perfect model class, before naming the regime where it fails. The
concession is what makes the criticism land, because he has already agreed with
the strongest version of the thing he is about to fault. The person shows in the
precision of the qualifier, "under model misspecification and finite data".

> "In other words: $KL[P|Q]$ is liberal, $KL[Q|P]$ is conservative. In yet other words: $KL[P|Q]$ is an optimist, $KL[Q|P]$ is a pessimist."

Huszár compresses a formal distinction between two divergences into a pair of
plain words each, so the reader carries the difference without the algebra. The
characterization is earned by the derivation surrounding it, not dropped in as a
label. His move is to name the behavior a formula produces in words the reader
already holds.
