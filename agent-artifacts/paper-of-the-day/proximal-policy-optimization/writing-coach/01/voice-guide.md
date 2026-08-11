# Voice guide: Proximal Policy Optimization Algorithms

## How this piece should sound

This piece rebuilds a mechanism before it argues about one, so the math has to
earn the same patience Karpathy gives the hidden-state update: define the
problem the clipped objective solves in plain language first, the way TRPO's
constrained optimization gets expensive and a plain policy gradient can wreck
a policy with one bad step, and only then let r_t(theta) and L^CLIP arrive as
the equation for a mechanism the reader already has in words. The clip and the
min() belong in the piece; they belong after the sentence that needs them, not
before it. When a specific number will carry the point better than the general
claim, use one, the way Karpathy runs "hello" through a four-letter vocabulary
before he generalizes about context and prediction. A worked ratio at one
timestep, one epsilon, one advantage sign, will do more for a reader checking
whether they understood the clip than another paragraph of description.

The paper's own evidence deserves the same treatment Olah gives curve
detectors: state the claim as a question the evidence answers, and count what
actually supports it. The paper compares clipping against a KL-penalty variant
and against no clipping at all. That comparison is the paper's case for its
own mechanism, and it can be shown as evidence, argument by argument, rather
than summarized as "the paper found clipping worked." Where the reconstruction
is thinner than it looks, an honest aside earns its place, the way Olah
interrupts his own claim to name polysemantic neurons as the case that
doesn't fit. If the trust-region-violation measurement in Engstrom et al. is
a stronger case for one part of the argument than another, say which part.

The turn toward the reexamination is where Huszár's habits matter most. He
distinguishes being wrong about what happened from being wrong about why a
thing that did happen worked, and that is exactly the shape of this piece's
central turn: PPO's advantage over TRPO happened, and the paper's account of
why is what the ablations complicate, not the fact of the advantage itself.
Keep that distinction sentence by sentence rather than folding it into a
single verdict. And where the paper's account and the reexamination's account
each hold something, grant the part that holds before the sentence that
limits it, the way "fair enough" precedes the clause that narrows it. The
commission already asks for a steelman before a weighing; Huszár's "fair
enough" is what that sounds like at the sentence level, a specific concession
followed by a specific limit, not a hedge and not a reversal.

## Chris Olah, "Zoom In: An Introduction to Circuits"

Source: https://distill.pub/2020/circuits/zoom-in/

> "Many important transition points in the history of science have been
> moments when science "zoomed in." At these points, we develop a
> visualization or tool that allows us to see the world in a new level of
> detail, and a new field of science develops to study the world through this
> lens. For example, microscopes let us see cells, leading to cellular
> biology. Science zoomed in. Several techniques including x-ray
> crystallography let us see DNA, leading to the molecular revolution. Science
> zoomed in. Atomic theory. Subatomic particles. Neuroscience. Science zoomed
> in."

Before the essay names a single neuron, three paragraphs go to microscopes and
cell theory. The technical claim, that studying individual neurons is a valid
unit of analysis, only arrives once the reader already holds the pattern (new
tool, new level of detail, new field) it will be an instance of. The
repeated fragment "Science zoomed in" marks each example as the same pattern
recurring, not a new point being added.

> "But are these "curve detectors" really detecting curves? We will be
> dedicating an entire later article to exploring this in depth, but the
> summary is that we think the evidence is quite strong. We offer seven
> arguments, outlined below. It's worth noting that none of these arguments
> are curve specific: they're a useful, general toolkit for testing our
> understanding of other features as well."

The claim is stated as a question before it is stated as a fact, and the fact
only arrives after the writers commit to a number, seven, and admit that the
arguments aren't specific to this one case. Naming the count up front lets a
reader track whether the case is being built or just asserted.

> "This essay may be giving you an overly rosy picture: perhaps every neuron
> yields a nice, human-understandable concept if one seriously investigates
> it? Alas, this is not the case. Neural networks often contain "polysemantic
> neurons" that respond to multiple unrelated inputs."

The writers interrupt their own argument to flag where it breaks down, before
a skeptical reader would ask. "Overly rosy picture" names the specific shape
of the distortion their own essay risks, which does more work than a general
disclaimer would.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "A glaring limitation of Vanilla Neural Networks (and also Convolutional
> Networks) is that their API is too constrained: they accept a fixed-sized
> vector as input (e.g. an image) and produce a fixed-sized vector as output
> (e.g. probabilities of different classes). Not only that: These models
> perform this mapping using a fixed amount of computational steps (e.g. the
> number of layers in the model). The core reason that recurrent nets are more
> exciting is that they allow us to operate over sequences of vectors:
> Sequences in the input, the output, or in the most general case both."

Before defining what an RNN does, the passage defines what an ordinary network
can't do. "Sequences" earns its emphasis only after the fixed-size limitation
has been named twice, once for input and output and once for computation, so
the new term arrives already carrying the problem it solves.

> "The two intermediates interact with addition, and then get squashed by the
> tanh into the new state vector. If you're more comfortable with math
> notation, we can also write the hidden state update as \( h_t = \tanh (
> W_{hh} h_{t-1} + W_{xh} x_t ) \), where tanh is applied elementwise."

The equation restates a mechanism already given in plain English, addition
then squashing, rather than introducing it. Framing the notation as an option
for readers who prefer it signals that the equation is a second encoding of
something the reader already has, not new information arriving cold.

> "As a working example, suppose we only had a vocabulary of four possible
> letters "helo", and wanted to train an RNN on the training sequence
> "hello". This training sequence is in fact a source of 4 separate training
> examples: 1. The probability of "e" should be likely given the context of
> "h", 2. "l" should be likely in the context of "he", 3. "l" should also be
> likely given the context of "hel", and finally 4. "o" should be likely given
> the context of "hell"."

A four-letter vocabulary and a five-letter word carry the entire claim about
how one training sequence becomes several training examples. The general
point, that context of varying length predicts the next character, is worked
through the smallest case that can show it before it is ever stated as a
rule.

## Ferenc Huszár, "Deep Learning is Powerful Because It Makes Hard Things Easy - Reflections 10 Years On"

Source: https://www.inference.vc/deep-learning-is-powerful-because-it-makes-hard-things-easy-reflections-10-years-on/

> "Ouch. Now this one has aged like my great-uncle-in-law's wine (He didn't
> have barrels so he cleaned up an old wheelie bin to serve as fermentation
> vat). Of course today, 40% of people credit the transformer architecture for
> everything that's going on, 60% credit scaling laws which are essentially
> existence proofs of stupendously expensive low hanging fruit."

The writer states that his old prediction was wrong before he explains why,
rather than softening the miss with qualifiers. The invented percentages are
a joke, not a citation, and the joke doesn't excuse him from the wrong call
it's attached to.

> "In hindsight: There is a lot of stuff in deep learning that we don't
> understand nearly enough. Yet they work. Some simple things have
> surprisingly huge impact, and mathematical rigour doesn't always help. The
> bitter lesson is bitter for a reason (maybe it was the wheelie bin).
> Sometimes things work for reasons completely unrelated to why we thought
> they would work. Sometimes people are right for the wrong reason. I was
> certainly wrong, and for the wrong reason, multiple times."

The passage separates two failures that most retrospectives blur together:
being wrong about what happened, and being wrong about why the thing that did
happen worked. Naming both, and pinning the second one specifically on
himself, is more exact than a general "I was wrong."

> "Fair enough. There are different aspects of intelligence and LLMs only
> capture some aspects. But this is not reason enough to call them a dead end
> unless the goal is to create something indistinguishable from a human. A
> non-embodied, language-based intelligence has an infinitely deep rabbit-hole
> of knowledge and intelligence to conquer: an inability to catch a mouse or
> climb a tree won't prevent language-based intelligence to have profound
> impact."

"Fair enough" grants the opposing argument's premise before the sentence that
limits its conclusion arrives. The concession is specific, LLMs capture some
aspects of intelligence and not others, rather than a rhetorical nod, which is
what lets the disagreement that follows respond to that claim instead of
brushing past it.
