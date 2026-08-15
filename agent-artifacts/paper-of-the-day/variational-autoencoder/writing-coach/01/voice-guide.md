# Voice guide: paper-of-the-day/variational-autoencoder

## How this piece should sound

This is a paper reconstruction of Kingma and Welling's "Auto-Encoding
Variational Bayes," and the reader is the press's declared one: a
mathematics-and-CS background, a career in ML engineering. That reader does
not need linear algebra or what a neural network is explained to them. They
do need the intractable marginal likelihood, the ELBO, and the
reparameterization trick built up in an order that earns each term before
using it, the way Olah earns "entropy" before he writes the word (see the
Bob passage and the fundamental-limit passage below). When the piece reaches
the ELBO's two halves, reconstruction and the KL term against the prior,
it can hold the plain sentence and the equation together rather than
choosing one, the way Olah holds "it's like a distance between two
distributions" next to the KL divergence he has just defined. The equation
in `nb-math` carries the rigor; a sentence like that carries the intuition,
and the piece has room for both since the equation is not asked to do
double duty as its own explanation.

Weng names a method's origin in the same clause that defines it, the way
the NCE passage below does. That habit is worth carrying into how this
piece introduces Rezende, Mohamed, and Wierstra's independent derivation,
and Bowman's, Burda's, and Higgins's after-record: the definition and the
citation land in the same breath rather than the citation trailing on as an
afterthought. Weng's BYOL passage is the model for weighing the paper as a
reviewer. What MNIST and Frey faces do and do not establish, what posterior
collapse means for the claim, and how IWAE's tighter bound reframes it are
exactly the kind of complication to name plainly, in the paper's own terms,
rather than gesturing at "limitations" in general. The commission already
gives this piece its complications by name; the job is to state them with
that same directness instead of softening them into a hedge.

Hashimoto's plainness sets the floor for the sentences around the math. A
claim gets made and then held to exactly what it covers, the way "SIMD can
be simple to understand... and when it's not, it's usually a good sign to
skip it for now" scopes its own confidence rather than posturing before
walking it back. That habit fits the paper's own evaluation directly: Kingma
and Welling report marginal likelihood on small image datasets, and the
figure the paper claims and the figure a modern reader should trust it for
are not automatically the same number, the way Hashimoto's theoretical 4x
and his measured real-world 5x are two different, both honestly reported,
numbers. State what was measured and on what, then say what that does and
doesn't license. His "let's back up and explain it step by step" move fits
a derivation that has run long enough to earn an explicit map of its own
steps. This piece can use it once, for whichever derivation runs longest,
probably the reparameterization estimator's variance argument, not for
every equation in the piece.

Two decisions belong to the brief rather than to any exemplar. First, the
verdict the paper template requires goes in prose the argument has already
built, not in a boxed callout; the recent record's `nb-note-strong` habit is
one this piece is explicitly breaking. Second, because the declared reader
already has the degrees and the career, jargon introduced once can be used
at full density afterward. The piece owes the reader the concrete build-up
Olah and Weng model, not a second explanation once the term is set.

## Chris Olah, "Visual Information Theory"

Source: https://colah.github.io/posts/2015-09-Visual-Information/

> "Let me tell you about my imaginary friend, Bob. Bob really likes animals. He constantly talks about animals. In fact, he only ever says four words: "dog", "cat", "fish" and "bird"."

Olah invents a character with a fixed, tiny vocabulary before he writes a
single equation about codes or entropy. Everything that follows, from
codeword length to the trade-off between short and long codes, has a
concrete case to point back to. The playfulness doubles as the worked
example the rest of the section leans on.

> "There is simply a fundamental limit. Communicating what word was said, what event from this distribution occurred, requires us to communicate at least 1.75 bits on average. No matter how clever our code, it's impossible to get the average message length to be less. We call this fundamental limit the entropy of the distribution – we'll discuss it in much more detail shortly."

The number and the fact come first; the name "entropy" arrives in the
sentence after the reader already knows what it refers to. This is the
concrete-before-abstract order held all the way through: define the thing,
then hand it its label, never the reverse.

> "The really neat thing about KL divergence is that it's like a distance between two distributions. It measures how different they are! (If you take that idea seriously, you end up with information geometry.)"

This sits right after the formal definition, not instead of it. Olah gives
the intuition its own sentence rather than folding it into the equation's
caption, and the exclamation point is doing real work: it marks a moment the
writer finds genuinely useful, not a flourish.

## Lilian Weng, "Contrastive Representation Learning"

Source: https://lilianweng.github.io/posts/2021-05-31-contrastive/

> "The goal of contrastive representation learning is to learn such an embedding space in which similar sample pairs stay close to each other while dissimilar ones are far apart. Contrastive learning can be applied to both supervised and unsupervised settings. When working with unsupervised data, contrastive learning is one of the most powerful approaches in self-supervised learning."

The opening states what the method is for before it states what it is. A
reader who stops after this paragraph already knows what problem every
later equation is solving, which is what keeps the dozens of method
definitions that follow readable in sequence rather than exhausting.

> "Noise Contrastive Estimation, short for NCE, is a method for estimating parameters of a statistical model, proposed by Gutmann & Hyvarinen in 2010. The idea is to run logistic regression to tell apart the target data from noise."

The citation lands inside the same sentence that gives the term its name
and its abbreviation. The second sentence then compresses the mechanism
into one plain clause before any notation appears. Precision and
readability are not traded off against each other here.

> "It is quite interesting and surprising that without negative samples, BYOL still works well. Later I ran into this post by Abe Fetterman & Josh Albrecht, they highlighted two surprising findings while they were trying to reproduce BYOL:"

Weng flags her own surprise plainly, then names exactly whose follow-up work
resolved it, rather than smoothing the anomaly into the main narrative. The
reader gets to see a real complication in the record and who ran it down,
which is the same move a reviewer makes when weighing a claim against what
happened after it published.

## Mitchell Hashimoto, "Everyone Should Know SIMD"

Source: https://mitchellh.com/writing/everyone-should-know-simd

> "I think that's wrong. SIMD can be simple to understand, and common "process N values at a time" SIMD code to speed up a naive for loop almost always follows the same general shape. Once you learn the basics, writing SIMD is just about as easy as a for loop. And when it's not, it's usually a good sign to skip it for now."

He states a contrary claim in five words and then spends the rest of the
paragraph earning it. The closing sentence works as a scope condition: it
tells the reader exactly where the claim stops applying. The confidence and
the limit each get their own sentence.

> "In real-world end-to-end throughput from terminal program to finalized terminal state on an AVX2 Intel desktop, this was more like a 5x speedup. You always lose some of the ideal speedup due to the other stuff around the SIMD code, but... that's still 5x!"

The theoretical number (up to 16x, stated a paragraph earlier) and the
measured number sit side by side instead of the measured one quietly
replacing the theoretical one. Hashimoto names the gap and moves on; he
doesn't apologize for the real number being smaller.

> "Okay, now I understand that those 12 lines are going to look really alien to someone not familiar with the concepts. So now let's back up and explain it step by step, mapping it directly to the shape previously mentioned."

He names the moment a block of code has outrun what he's explained so far
and announces the fix in one sentence: back up, go step by step. The
reader is told exactly what kind of explanation is coming next, which is
why the five numbered steps that follow read as inevitable rather than as
padding.
