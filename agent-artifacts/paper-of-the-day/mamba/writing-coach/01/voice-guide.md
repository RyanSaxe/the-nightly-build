# Voice guide: paper-of-the-day/mamba

## How this piece should sound

This is a reconstruction of the Mamba paper for a machine-learning engineer who
already knows why attention is expensive at long sequence length and wants to
understand the selective-state-space alternative from the mechanism up. The
register is calm and first-principles. The SSM recurrence, its discretization,
the selection that makes the step size and B and C input-dependent, and the
parallel scan are set as equations, and the prose exists to earn them. Assume the
reader can follow the algebra; the sentences are not there to narrate it symbol
by symbol.

When an equation is on the page, the sentence after it can say what it means or
what it now makes possible, the way Gundersen restates his integral as "the
gradient of the expectation is equal to the expectation of the gradient" and then
turns to the case that breaks it. For Mamba that is the difference between writing
the discretized recurrence and saying why a time-invariant A, B, and C let S4
fold the recurrence into one convolution, and why making those matrices depend on
the input removes that shortcut. The equation and the sentence after it can carry
the same idea in turn, so a reader who skips one still has the other.

The reconstruction turns on a claim about scale, and it reads best when the payoff
is shown at the size where it matters rather than asserted. Olah works a two-node
example, gets a factor of two, and only then scales it to a million-input function
to state the real advantage. A worked step of the selective scan on a short
sequence can do the same job, with the linear-time and memory argument stated
where the sequence is long, so the number the reader keeps comes from the
derivation and not from the abstract.

The verdict is the center of this piece, and the standard is that each judgment
carries its reason. Weng's summary of diffusion models gives the cost of
tractability and the cost of flexibility before it says the method has both, and
names the long Markov chain as the reason sampling is slow. Where Mamba replaces
attention and where the later record says it does not, the piece can name the
mechanism behind each: the selective scan for the throughput and length claims,
the fixed-size recurrent state for the recall and copying failures that Mamba-2
and the hybrid models responded to. A concession that a pure SSM loses
exact-recall tasks belongs stated plainly, beside what attention still buys, and
not softened.

Placing Mamba among its neighbors can follow Weng's move of giving each
alternative one honest clause: what S4's time-invariance cost it, what attention's
quadratic cost buys, what the hybrids give up by keeping some attention. A clause
that names the actual tradeoff does the work; a hedge that keeps every option open
does not.

Where a loose explanation of selectivity is in circulation, that the model learns
to attend to the tokens that matter, the piece can refuse it and set the precise
version instead, the way Gundersen quotes the informal answers to his question and
then does the formal work they skipped. Taking the paper's own names apart can
serve the same end: saying why "selective" points to input-dependent parameters,
and why the "selective scan" is the algorithm that keeps that selection fast, the
way Gundersen decodes the letters of SGVB from the method they name.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That’s the difference between a model taking a week to train and taking 200,000 years."

The speed factor is an abstract number, so he spends the next sentence converting
it into two durations a reader can hold side by side, a week against 200,000
years. The figure is exact rather than "much faster," and the comparison is what
makes it land. Olah is visible in choosing to cash out the claim instead of moving
on from it.

> "This is where “forward-mode differentiation” and “reverse-mode differentiation” come in. They’re algorithms for efficiently computing the sum by factoring the paths. Instead of summing over all of the paths explicitly, they compute the same sum more efficiently by merging paths back together at every node. In fact, both algorithms touch each edge exactly once!"

This paragraph comes right after the equation that factors a sum of nine
path-products into a product of two sums. He does not restate the algebra; he says
in plain words what the factoring buys, that each algorithm touches every edge
once. The math sits above, and the prose tells the reader what changed because of
it.

> "For this graph, that’s only a factor of two speed up, but imagine a function with a million inputs and one output. Forward-mode differentiation would require us to go through the graph a million times to get the derivatives. Reverse-mode differentiation can get them all in one fell swoop! A speed up of a factor of a million is pretty nice!"

He has just worked a tiny example where reverse-mode saves a factor of two, and he
does not let the small number stand as the result. He scales it to a
million-input function and states the real payoff there. The verdict on the method
comes out of the worked case rather than ahead of it, and the plain exclamations
are how Olah sounds when a result pleases him.

## Gregory Gundersen, "The Reparameterization Trick"

Source: https://gregorygundersen.com/blog/2018/04/29/reparameterization/

> "But why do we need this trick in the first place? When first learning about variational autoencoders (VAEs), I tried to find an answer online but found the explanations too informal."

He names the exact question the piece exists to answer and admits that the
explanations he found did not answer it. Setting the informal versions aside as
too informal fixes the standard the rest of the post has to meet. Gundersen is
visible in refusing to pass along an explanation he could not make precise.

> "In words, the gradient of the expectation is equal to the expectation of the gradient. But what happens if our density p is also parameterized by θ?"

He has just written the equation, and here he restates it in one plain sentence so
the reader carries the meaning and not only the symbols. The next sentence turns
straight to the case that breaks the identity. The equation and the prose do the
same work one after the other, and neither is decoration.

> "But with a better understanding of the differentiability of this Monte Carlo estimator, we can understand the focus of the paper and the name of the estimator. Variational Bayes refers to approximating integrals using Bayesian inference. The method is stochastic because it approximates an expectation with many random samples. And a VAE using neural networks is an example of a model you could build with the SGVB estimator because the estimator is gradient-based."

He returns to something that had puzzled him about the paper, why it centers the
estimator rather than the now-famous VAE, and answers it by taking the estimator's
name apart word by word, each clause saying why that word is there. The
explanation is built out of the paper's own vocabulary. Gundersen is visible in
treating a naming choice as something worth understanding rather than skipping.

## Lilian Weng, "What are Diffusion Models?"

Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

> "So far, I’ve written about three types of generative models, GAN, VAE, and Flow-based models. They have shown great success in generating high-quality samples, but each has some limitations of its own. GAN models are known for potentially unstable training and less diversity in generation due to their adversarial training nature. VAE relies on a surrogate loss. Flow models have to use specialized architectures to construct reversible transform."

Before introducing diffusion models she places them against GAN, VAE, and flow
models, and gives each a single clause naming its actual limitation: unstable
training, a surrogate loss, specialized reversible architectures. The comparisons
are specific and unflattering where they should be. Weng is visible in setting up
a new method by being honest about what the existing ones cost.

> "Pros: Tractability and flexibility are two conflicting objectives in generative modeling. Tractable models can be analytically evaluated and cheaply fit data (e.g. via a Gaussian or Laplace), but they cannot easily describe the structure in rich datasets. Flexible models can fit arbitrary structures in data, but evaluating, training, or sampling from these models is usually expensive. Diffusion models are both analytically tractable and flexible"

The favorable verdict is built rather than announced. She first states the tension
every generative model faces between tractability and flexibility, gives the cost
of each side, and only then says diffusion models get both. The judgment holds
because the two sentences before it earned the terms it uses.

> "Cons: Diffusion models rely on a long Markov chain of diffusion steps to generate samples, so it can be quite expensive in terms of time and compute. New methods have been proposed to make the process much faster, but the sampling is still slower than GAN."

The limitation is stated with its cause attached, the long Markov chain being why
sampling is expensive, and she concedes plainly that even after the speedups it is
slower than a GAN. She does not soften the concession or bury it. This is what a
grounded negative verdict reads like: the mechanism is the reason, and the
comparison is left honest.
