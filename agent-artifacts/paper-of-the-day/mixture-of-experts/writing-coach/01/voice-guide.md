# Voice guide: paper-of-the-day/mixture-of-experts (01)

## How this piece should sound

This piece rebuilds one gating mechanism from a paper the field mostly knows by
reputation, so the register should hold the discipline Raschka shows when he
stops narration to ask his own question and then answers it with the actual
reasoning: "Why does specifically √d_k?" is a model for how to handle the noise
term inside noisy top-k gating, or the coefficient-of-variation form of the
importance loss. Pose the question in the piece's own terms, then answer it with
the paper's algebra, not with a description of what the algebra is for.

When the paper gives more than one justification for a mechanism, as it does for
running two separate auxiliary losses rather than one, give each justification
its own sentence the way Raschka gives normalization two distinct, numbered
reasons rather than one blended one. Importance balances what the softmax
assigns across experts; load balances how many examples actually reach each
expert even when the soft importance looks even. Naming what each loss is for,
separately, does more for the reader than a single sentence that gestures at
"balancing."

Olah's step-by-step walk through the LSTM gates is a model for the gating
mechanism itself: state what a value in the gate means before moving to the next
step, the way "a 1 represents completely keep this while a 0 represents
completely get rid of this" is settled before the next gate is introduced.
Noisy top-k gating has an equivalent moment: what happens to an expert's weight
when it falls outside the top k, and what the noise term changes about which
experts make that cut, deserve the same plain treatment before the piece moves
on to the load loss that exists because of it.

Before introducing what came after 2017, name the specific thing that broke, in
short declaratives, the way Weng states what breaks in the vanilla Transformer
before Transformer-XL has a name: the model can only attend within one segment,
and no information crosses a segment boundary. The paper's own batch-shrinking
problem and its communication cost are failures of this same kind, concrete and
statable before the mechanism built to address them is named. Naming the failure
first gives Switch Transformer's top-1 simplification, or GShard's sharding,
somewhere to land.

Where a later paper's ablation gives an actual number against the original
design, use that number rather than a comparative word, the way Weng attaches
"sequence length up to 16,384" directly to the claim it supports instead of
leaving the two apart. A reported expert count next to its perplexity, or
Switch Transformer's finding on top-1 against top-2 routing, belongs in the
sentence making the claim.

The verdict this piece owes at the end can hold the same discipline Olah holds
when he asks "Which of these variants is best? Do the differences matter?" and
answers only with what the cited comparisons found, letting one finding sit next
to a different one without forcing them to agree. What Switch Transformer,
GShard, expert-choice routing, and auxiliary-loss-free balancing changed about
the 2017 gating may not resolve into one line, and the piece can say so plainly
rather than settling for a tidier verdict than the record supports.

Bring the paper's own figures into the argument at the point where they carry
weight rather than after the point has already been made in prose: the MoE
layer schematic belongs where the gating math needs a picture of what is being
computed, and the perplexity-against-capacity figure earns its place where the
sentence reading it does the analysis, not as an illustration set beside a
paragraph that has already finished the point on its own.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this
> essay, you understand each word based on your understanding of previous
> words. You don't throw everything away and start thinking from scratch again.
> Your thoughts have persistence."

This is the essay's first sentence, and it makes a claim about memory in
ordinary human terms before RNNs are mentioned at all. There is no jargon and no
forward reference to a term the reader has not met yet. Olah is visible in how
much weight he lets a small, checkable observation carry before naming the
subject it motivates.

> "The first step in our LSTM is to decide what information we're going to
> throw away from the cell state. This decision is made by a sigmoid layer
> called the "forget gate layer." It looks at h_{t-1} and x_t, and outputs a
> number between 0 and 1 for each number in the cell state C_{t-1}. A 1
> represents "completely keep this" while a 0 represents "completely get rid of
> this.""

Olah states what each possible gate value means in the same breath that
introduces the gate, so the reader never holds an undefined symbol for more than
a sentence. The two readings of the value are given in the plainest available
words. The mechanism is explained by what it does to the number, not by a
picture standing in for it.

> "Which of these variants is best? Do the differences matter? Greff, et al.
> (2015) do a nice comparison of popular variants, finding that they're all
> about the same. Jozefowicz, et al. (2015) tested more than ten thousand RNN
> architectures, finding some that worked better than LSTMs on certain tasks."

Olah asks the evaluative question directly, then answers it with two named
studies whose findings do not agree with each other. The judgment stops exactly
where the cited evidence stops: "finding that they're all about the same" is not
pushed into a stronger claim than the study made.

## Lilian Weng, "The Transformer Family"

Source: https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/

> "Self-attention is a type of attention mechanism where the model makes
> prediction for one part of a data sample using other parts of the observation
> about the same sample. Conceptually, it feels quite similar to non-local
> means. Also note that self-attention is permutation-invariant; in other
> words, it is an operation on sets."

Weng states a structural fact about self-attention as a single sentence and lets
it stand without elaboration: "an operation on sets." The claim is precise
enough to check, and nothing is added to make it sound bigger than it is.

> "The vanilla Transformer has a fixed and limited attention span. The model
> can only attend to other elements in the same segments during each update
> step and no information can flow across separated fixed-length segments."

Before naming Transformer-XL, Weng states exactly what breaks in the design that
came before it, in two short declaratives. The reader knows the specific failure
the next section's mechanism is built to fix before that mechanism has a name.

> "The compute and memory cost of the vanilla Transformer grows quadratically
> with sequence length and thus it is hard to be applied on very long
> sequences. Sparse Transformer (Child et al., 2019) introduced factorized
> self-attention, through sparse matrix factorization, making it possible to
> train dense attention networks with hundreds of layers on sequence length up
> to 16,384, which would be infeasible on modern hardware otherwise."

The sentence carries the actual number the paper reports, sequence length up to
16,384, rather than a comparative word like "much longer." The claim about why
the design matters, infeasible otherwise, is attached directly to that number
instead of left to stand on its own afterward.

## Sebastian Raschka, "Understanding and Coding Self-Attention, Multi-Head Attention, Causal-Attention, and Cross-Attention in LLMs"

Source: https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention

> "Note that there are many variants of self-attention. A particular focus has
> been on making self-attention more efficient. However, most papers still
> implement the original scaled-dot product attention mechanism introduced in
> the Attention Is All You Need paper since self-attention is rarely a
> computational bottleneck for most companies training large-scale
> transformers."

Raschka names that many variants exist, then gives the actual practical reason
the field mostly does not need them: self-attention is "rarely a computational
bottleneck." The judgment weighs a design against what practitioners actually
did with it, not against a hypothetical better version.

> "Why does specifically √d_k? The dot product between q and k is a sum of d_k
> independent terms, each with variance about 1. That means the variance of the
> raw score grows linearly with d_k. By dividing by √d_k, we cancel that growth
> and bring the variance back to about 1."

Raschka poses the design question in his own voice and then answers it with the
actual statistical reasoning behind the scaling factor: a sum of independent
terms, the variance of that sum, and what dividing by its square root does to
it. The math is not decoration set beside the claim; it is the answer to the
question just asked.

> "Normalizing attention weights in neural networks, such as in transformer
> models, is advantageous over unnormalized weights for two main reasons.
> First, normalized attention weights that sum to 1 resemble a probability
> distribution. This makes it easier to interpret the model's attention to
> various parts of the input in terms of proportions. Second, by constraining
> the attention weights to sum to 1, this normalization helps control the scale
> of the weights and gradients to improve the training dynamics."

Raschka gives two distinct, numbered reasons for a design choice instead of
folding them into one vague justification. Each reason names a separate
mechanism, a probability interpretation and a training-stability effect, so a
reader could check either one independently of the other.
