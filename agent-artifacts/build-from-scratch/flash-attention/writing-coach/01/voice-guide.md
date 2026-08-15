# Voice guide: build-from-scratch/flash-attention

## How this piece should sound

This piece has one argument to carry: the online-softmax recurrence, proven
equivalent to the naive softmax by code that runs and an experiment that shows
where the naive version breaks. The register that carries an argument like that
is Hashimoto's in "Everyone Should Know SIMD" — state the claim plainly, then
earn it against the actual listing. The piece can open the same way: say what a
running max and a running denominator buy you (the score matrix never has to
exist in memory) before building up to why, rather than saving it as a reveal.

The naive/streaming split is the whole piece, so the trace of what `m`, `l`,
and `o` do at each block should read like Hashimoto's walk through `@bitCast`
and `@ctz`: one sentence per step, the variable that changed and the value it
took, not a paraphrase of what the update accomplishes. When a new block raises
the running max and the accumulator has to be rescaled, that rescaling earns the
same treatment his bit-mask trick gets — shown against real numbers from the
code, not summarized as "the accumulator is corrected."

Olah's LSTM piece earns the right to say a reader doesn't need something yet.
The recurrence has several moving parts that depend on each other — the running
max, the running normalizer, the rescale it forces on the next block — and nothing
requires introducing all of them before the reader needs the first one. Get the
reader comfortable with what `m` and `l` hold before the update rule that
changes them, the way Olah gets the reader comfortable with the notation before
the walk through the gates.

Weng's habit of anchoring a claim to a specific outside number, sourced and
named, is the move for the honest comparison the commission calls for. The
piece has to say plainly that the NumPy prototype cannot show the wall-clock
speedup the real kernel delivers. That admission lands harder next to a real
figure — hours to minutes, or however the FlashAttention paper states its
speedup — than as a bare disclaimer. The same habit applies to the piece's own
measurements: when the naive score matrix's memory is set against the streaming
buffers as N grows, give the actual numbers the code produced rather than
describing the shape of the curve.

Vocabulary from the papers — IO-aware, fused kernel, HBM, SRAM tiling — belongs
in the piece, but each term needs the concrete thing it names attached to the
sentence it first appears in, the way Weng's "tractable" gets a parenthetical
example before the sentence moves past it. A term introduced without its
referent reads as inherited from the source rather than understood.

End on what the experiment showed: the assert that holds across sizes, the
overflow the running max avoids, the honest limit of what a NumPy prototype can
demonstrate about a GPU kernel. Olah's close names the specific gap his essay
closes, in the vocabulary the essay just built, rather than reaching for a
verdict past what it earned.

## Mitchell Hashimoto, "Everyone Should Know SIMD"

Source: <https://mitchellh.com/writing/everyone-should-know-simd>

> "I think that's wrong. SIMD can be simple to understand, and common "process
> N values at a time" SIMD code to speed up a naive for loop almost always
> follows the same general shape. Once you learn the basics, writing SIMD is
> just about as easy as a for loop. And when it's not, it's usually a good sign
> to skip it for now."

He states the disagreement flatly in four words, then spends the rest of the
paragraph earning it with a specific, checkable claim about how the code looks.
The writer is visible in "I think that's wrong" — a position taken, not hedged
into a survey of views.

> "@bitCast turns the vector of booleans into an integer with one bit per lane.
> A 1 bit means the value was greater than 0xF and a 0 means it wasn't. We
> invert the mask so failed comparisons are 1, and then @ctz counts the number
> of zero bits before the first failure. That count is the index of the first
> failing lane."

Each sentence advances exactly one step of the trace, using the real function
names and values from the listing above it rather than describing what the code
does in general terms. A reader can check every sentence against the code
sitting next to it.

> "Every developer should be able to recognize the opportunity and, most
> importantly, should not be scared of SIMD. If you see a hot loop scanning,
> comparing, counting, or transforming a large amount of contiguous data, you
> should be able to imagine processing it a vector-width chunk at a time."

The close restates the opening claim using the vocabulary the piece just built
— "hot loop," "vector-width chunk" — instead of reaching for a bigger idea the
piece never argued for.

## Chris Olah, "Understanding LSTM Networks"

Source: <https://colah.github.io/posts/2015-08-Understanding-LSTMs/>

> "Humans don't start their thinking from scratch every second. As you read
> this essay, you understand each word based on your understanding of previous
> words. You don't throw everything away and start thinking from scratch
> again. Your thoughts have persistence."

The essay opens on a fact about the reader's own experience of reading the
sentence, before it names the network the essay is about. The abstract idea —
persistence of state across a sequence — arrives only after the reader already
has a concrete version of it.

> "Don't worry about the details of what's going on. We'll walk through the
> LSTM diagram step by step later. For now, let's just try to get comfortable
> with the notation we'll be using."

He tells the reader directly what not to hold onto yet, sequencing the
difficulty instead of front-loading all of it. The permission to not understand
something on first sight is stated in plain words, not implied by silence.

> "Written down as a set of equations, LSTMs look pretty intimidating.
> Hopefully, walking through them step by step in this essay has made them a
> bit more approachable."

The close names the specific gap the essay exists to close — equations versus
approachability — instead of reaching past what the essay demonstrated.

## Lilian Weng, "What are Diffusion Models?"

Source: <https://lilianweng.github.io/posts/2021-07-11-diffusion-models/>

> "Langevin dynamics is a concept from physics, developed for statistically
> modeling molecular systems. Combined with stochastic gradient descent,
> stochastic gradient Langevin dynamics (Welling & Teh 2011) can produce
> samples from a probability density p(x) using only the gradients … in a
> Markov chain of updates."

She names the field a technique is borrowed from and what it was originally for
in the same sentence that introduces it, with the citation sitting inside the
explanation rather than parked in a separate clause. The borrowing is stated,
not assumed.

> "Tractability and flexibility are two conflicting objectives in generative
> modeling. Tractable models can be analytically evaluated and cheaply fit data
> (e.g. via a Gaussian or Laplace), but they cannot easily describe the
> structure in rich datasets. Flexible models can fit arbitrary structures in
> data, but evaluating, training, or sampling from these models is usually
> expensive."

Two sentences share one shape to build a contrast, and each abstract adjective
— tractable, flexible — gets a concrete example attached before the paragraph
moves on. The trade-off the whole section explains is visible before either
model family is named.

> "It is very slow to generate a sample from DDPM by following the Markov
> chain of the reverse diffusion process, as T can be up to one or a few
> thousand steps. One data point from Song et al. (2020): 'For example, it
> takes around 20 hours to sample 50k images of size 32 × 32 from a DDPM, but
> less than a minute to do so from a GAN on an Nvidia 2080 Ti GPU.'"

A claim about slowness gets a specific outside number attached to it, with the
hardware and the comparison model named, rather than resting on the word
"slow." A reader could go check the figure against its source.
