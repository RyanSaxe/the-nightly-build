# Voice guide: paper-of-the-day/direct-preference-optimization (01)

## How this piece should sound

This is a reconstruction of the DPO paper for an ML engineer who already holds
transformers and the RLHF/InstructGPT pipeline. Write to that reader: calm,
precise, and unhurried, with the derivation as the spine and no hype anywhere
near it. The register stays explanatory throughout. Assume the reader can
follow a gradient and a KL term, and define only what is specific to this paper
(the implicit reward, the reparameterization, the Bradley-Terry substitution) at
the moment the argument first spends it.

The math is the strongest material, so set it and narrate the steps that turn.
When the KL-constrained objective resolves to its closed-form optimal policy, or
the reward is rewritten as a function of the policy and the reference policy, or
the partition function cancels out of the Bradley-Terry model, the article can do
what Gundersen does at the point his derivation breaks: name the exact condition
that makes the step work, at the specific line, rather than gesturing at a
difficulty. The reader should be able to see why each move is licensed.

A derivation earns a short distillation once it is done, and the distillation may
be worth more than the steps that produced it. Olah compresses the whole
forward-versus-reverse contrast into two parallel sentences a reader can hold in
mind. The meaning of the DPO gradient, that it up-weights preferred and
down-weights dispreferred responses in proportion to how wrongly the implicit
reward orders them, is the kind of result that may call for that kind of
compression once the algebra behind it is on the page.

Several of the quantities here are ones the reader cannot scale unaided: a KL
budget, a win rate, the position of a curve on the reward-versus-KL frontier.
Olah turns "ten million times faster" into a week against 200,000 years, and Weng
refuses to leave "slow" as an adjective when a measured 20-hours-against-a-minute
comparison is available. Where the sentiment-control frontier or the
summarization and dialogue win rates enter, the figure may call for a stated
comparison the reader already holds rather than the bare number.

The piece also weighs DPO against the record that followed: on-policy PPO and
RLHF, IPO, KTO, and the analyses of probability mass moving off-distribution.
Weng gives each competing method a single sentence naming its own specific
weakness. That economy is available here. Each later result can be the one
concrete thing it established about DPO, held to the same evidentiary bar as the
reconstruction, without turning into a survey of preference-optimization methods.

The template asks you to rebuild in the order that teaches best rather than the
paper's order. Gundersen, reading Kingma, says plainly that the famous result was
buried as a mid-paper example. Where the DPO paper's own sequence hides the
derivation the reader most needs, saying so and reordering is available to you.
And where the later record shows DPO diverging from on-policy RLHF, that verdict
can be stated as precisely as the derivation was, located at the condition that
produces it, not softened into a hedge.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That's the difference between a model taking a week to train and taking 200,000 years."

The passage states the abstract number, ten million times faster, and then
converts it into a quantity the reader can feel, a week against 200,000 years, so
the magnitude is never left for the reader to scale on their own. Olah is visible
in the habit of following an abstract figure with a concrete one right after it,
before moving on.

> "Forward-mode differentiation tracks how one input affects every node. Reverse-mode differentiation tracks how every node affects one output."

Two sentences built the same way carry the entire distinction between the two
algorithms, and each half of the parallel names something the reader can check
against the graph. After pages of constructing the computational graph, Olah lets
a pair of plain sentences do the work a diagram had been doing, which is where his
economy shows.

> "For this graph, that's only a factor of two speed up, but imagine a function with a million inputs and one output. Forward-mode differentiation would require us to go through the graph a million times to get the derivatives. Reverse-mode differentiation can get them all in one fell swoop! A speed up of a factor of a million is pretty nice!"

He tests the result on a concrete case, a million inputs and one output, and
reports what each method would cost on it. The exclamation marks and "pretty nice"
are informal, but they land on a real quantitative payoff instead of decorating an
empty one, and Olah is visible in letting the worked number carry the enthusiasm
rather than asserting that the result matters.

## Lilian Weng, "What are Diffusion Models?"

Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

> "So far, I've written about three types of generative models, GAN, VAE, and Flow-based models. They have shown great success in generating high-quality samples, but each has some limitations of its own. GAN models are known for potentially unstable training and less diversity in generation due to their adversarial training nature. VAE relies on a surrogate loss. Flow models have to use specialized architectures to construct reversible transform."

Each competing method gets exactly one sentence naming its own specific weakness:
GAN's unstable training, VAE's surrogate loss, the reversibility constraint on
flow models. The compression is disciplined, since she trusts the reader to know
the methods and supplies only the single fact that motivates moving past each.
Weng's voice is in that economy, one idea per sentence and no throat-clearing
ahead of the list.

> "It is very slow to generate a sample from DDPM by following the Markov chain of the reverse diffusion process, as $T$ can be up to one or a few thousand steps. One data point from Song et al. (2020): 'For example, it takes around 20 hours to sample 50k images of size 32 × 32 from a DDPM, but less than a minute to do so from a GAN on an Nvidia 2080 Ti GPU.'"

Having said the sampling is slow, she declines to leave "slow" as an adjective and
instead borrows a measured comparison from the cited paper: 20 hours for a DDPM
against under a minute for a GAN. The number is attributed and specific, so the
claim is checkable. What shows is her instinct to reach for a source's own figure
the moment a qualitative word would otherwise stand alone.

> "Tractability and flexibility are two conflicting objectives in generative modeling. Tractable models can be analytically evaluated and cheaply fit data (e.g. via a Gaussian or Laplace), but they cannot easily describe the structure in rich datasets. Flexible models can fit arbitrary structures in data, but evaluating, training, or sampling from these models is usually expensive."

She sets up the tension a method has to resolve before naming any method's
advantage: tractable models are cheap but rigid, flexible ones expressive but
expensive. Building both poles first gives the eventual payoff something to sit
on. Weng's patience is visible in the refusal to state an advantage until the
reader is holding both sides of the tradeoff.

## Gregory Gundersen, "The Reparameterization Trick"

Source: https://gregorygundersen.com/blog/2018/04/29/reparameterization/

> "But why do we need this trick in the first place? When first learning about variational autoencoders (VAEs), I tried to find an answer online but found the explanations too informal."

He opens with the question the whole post answers and admits why he is writing it,
that the explanations he could find were too informal. Naming his own
dissatisfaction gives the derivation a reason to exist and sets an honest standard
the rest of the piece then has to meet. Gundersen is visible in the first-person
account of trying to understand something and finding the available answers
wanting.

> "The first term of the last equation is not guaranteed to be an expectation. Monte Carlo methods require that we can sample from $p_\theta(z)$, but not that we can take its gradient."

The sentence identifies exactly where a naive derivation breaks: the first term is
not guaranteed to be an expectation, so Monte Carlo sampling has nothing to
estimate. He states the precise condition that fails instead of waving at a
difficulty. What shows is his care to locate the problem at a specific line of the
math before proposing any fix.

> "When I first read Kingma's paper, I wondered why it focused on the stochastic gradient variational Bayes (SGVB) estimator and associated algorithm, while the now-famous variational autoencoder was just given as an example halfway through the paper."

He questions the paper's own choice of emphasis, wondering why the famous result
was presented as a mid-paper example while a more general estimator held the
focus. The move treats the source as something to reorganize for the reader rather
than to follow in order. Gundersen is visible in reading the paper critically,
noticing its framing and saying that the framing surprised him.
