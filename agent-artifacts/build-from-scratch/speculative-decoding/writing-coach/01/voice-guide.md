# Voice guide — Build From Scratch: speculative decoding (01)

Register: a first-principles argument in plain declarative sentences, aimed at
a reader who already builds transformers for a living. State the assumed
background once, then never re-teach it; the only new material is the
draft-then-verify loop and the accept/reject step, so spend the sentences
there. Structure does the persuading, not adjectives. The relationship with
the reader is a colleague reading over your shoulder while you build
something, not a student being led.

Moves that change sentences in this article:

- **Make each nb-code block carry an argument.** Before a listing, say in one
  sentence what property it is about to establish (`p_draft` and `p_target`
  must be checkable per-token distributions, not "here is the sampler").
  After it, name what the run now lets you claim, not what the lines did.
  When code and an equation express the same fact, pick one carrier and let
  the other gloss it in a phrase, so the reader is never told twice.
- **Report run output as data, not as narration.** Quote the printed numbers
  and the exact call that produced them. A frequency that lands at 0.31
  against a target of 0.33 is reported the same plain way as an exact match —
  no relief, no apology, no rounding it into a nicer number.
- **Earn the accept/reject rule before you name it.** State the two failure
  modes in prose first — accepting too often drifts from the target
  distribution, rejecting too often wastes the draft's cheap tokens — so
  `min(1, p_target(x)/p_draft(x))` lands as the ratio that balances them, not
  as notation dropped from above. Give the residual `(p_target − p_draft)_+`
  the same treatment: say in prose what is left to sample from before the
  formula names it. State the equivalence as a claim, cite the paper's own
  lemma for it, and let the empirical frequency match be what closes the gap
  between claim and belief. No line-by-line algebra derivation.
- **Order sections by dependency, not by system layout.** Move from
  single-token sampling to K-token draft-and-verify to the real-system
  comparison only where each step needs the previous one's result. A section
  that would still make sense if moved elsewhere is in the wrong place.
- **Cut the tells.** No sentence built to sound quotable ("that's the whole
  point," "the catch is"). No X-is-not-Y contrast unless a real misconception
  is named first. No address to the reader, no narrating the piece itself.
  Close on the number the build produced — accepted tokens per step at a
  measured agreement rate, or the wall-clock ratio — not a lesson about
  efficiency or where inference is headed.

Recently used, do not reuse: the byte-pair-encoding piece's "train a tiny X on
N bytes and reproduce Y" opener — find this piece's own way into the build.
No colon-subtitle headline. Vary section shapes from recent pieces; don't let
headings settle into a repeated comma-joined-clause cadence.

## Peter Norvig, "How to Write a Spelling Corrector"
Source: https://www.norvig.com/spell-correct.html
Craft:
- cadence: short declaratives punctuate longer explanatory runs; a payoff
  line lands deliberately short after a build-up ("And here it is.").
- argument: hook, promise, code, theory, implementation, empirical test,
  honest failure catalog, open problems — theory arrives only once the code
  needs it, never before.
- evidence: a held-out test set scored for accuracy and speed, stated
  plainly, including the shortfall against his own stated goal.
- stance: intelligent equal, not student — "why should they know about
  something so far outside their specialty" — explains the reason for a
  design choice, not just the choice.
- notice: failure cases get more space than successes; the future-work
  section is not an afterthought but a proportionate share of the piece.
- diction: concrete verbs (returns, generates, enumerates), metaphor used
  once and dropped, no hedging in the results sentence.
- reader: assumed to want the reasoning behind the formula, not just the
  formula — "cleaner to formally separate the two factors," argued from what
  the code must do next, not from elegance.
- the missed move: correctness is settled empirically, against a real corpus,
  not by a completed proof — the math derivation runs only as far as the next
  code decision needs it, then the piece hands the rest of the argument to a
  measured accuracy number.
Calibration: "So on the development set we get 75% correct... In conclusion,
I met my goals for brevity, development time, and runtime speed, but not for
accuracy."

## Sasha Rush (Harvard NLP), "The Annotated Transformer"
Source: https://nlp.seas.harvard.edu/2018/04/03/attention.html
Craft:
- cadence: conversational formality; declarative claim sentences alternate
  with a short line naming what the code is about to show.
- argument: paper claim, then formula, then the function that instantiates
  it immediately below — code is not illustration of the math, it is the
  proof that the math runs.
- evidence: real training logs quoted verbatim (loss, tokens/sec), BLEU
  scores, attention-weight visualizations — never a described result without
  the number that backs it.
- stance: collaborator sitting beside the reader — "my comments are
  blockquoted, the main text is all from the paper itself" — draws an
  explicit line between the source's authority and the annotator's voice.
- notice: what the code reveals that the paper's prose glosses over — a
  masked position, a shape mismatch, a detail the equation hides.
- diction: precise and unhurried; technical terms introduced once, then used
  exactly, no synonym swap for variety.
- reader: assumed to hold the paper already and want the gap between
  notation and execution closed, not the paper re-explained from zero.
- the missed move: the piece never explains a formula twice — once it is
  code, the prose stops restating it and instead narrates what the code now
  lets you compute, keeping math and code as two carriers of one fact rather
  than a redundant pair.
Calibration: "In this post I present an 'annotated' version of the paper in
the form of a line-by-line implementation. I have reordered and deleted some
sections from the original paper and added comments throughout."

## Andrej Karpathy, "Yes You Should Understand Backprop"
Source: https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b
Craft:
- cadence: short punchy statements bracket denser explanatory stretches; the
  rhythm resets after each code block instead of accumulating clauses.
- argument: each example (sigmoid saturation, dead ReLUs, an RNN, a DQN bug)
  runs the same shape — mechanism, then the exact place it silently breaks —
  so the repetition itself becomes the case for the thesis.
- evidence: a real bug from a public repository, the exact line number, the
  wrong loss function named and the fix given — abstraction cashed out as a
  specific, findable mistake.
- stance: writes to a reader who thinks the framework already handles this —
  earns the disagreement by showing where that belief fails, not by asserting
  it.
- notice: the failure that stays invisible until you compute the gradient by
  hand — the piece's whole case rests on what autodiff conceals from a user
  who never derives it.
- diction: words that carry risk — leaky, dead, trap, silently — doing the
  work adjectives of enthusiasm would otherwise do elsewhere.
- reader: assumed competent and slightly overconfident; the piece's job is to
  make the confidence conditional, not to build the reader up from zero.
- the missed move: a formula is only introduced at the exact moment a
  concrete failure needs it to be explained, so no equation ever appears
  before the reader has a reason to want it.
Calibration: "Why do we have to write the backward pass when frameworks in
the real world, such as TensorFlow, compute it for you automatically?"

## Jay Mody, "GPT in 60 Lines of NumPy"
Source: https://jaykmody.com/blog/gpt-from-scratch/
Craft:
- cadence: staccato short sentences carry the intuition ("We call this
  masking.") ahead of the notation that formalizes it.
- argument: build the smallest runnable version first, load real weights
  into it, run it, only then walk back through each piece — code-first,
  explanation second, so the explanation always has a working artifact behind
  it.
- evidence: an exact command line and its printed output, then a second run
  proving parity against the official implementation — working is a claim
  you demonstrate twice, once alone and once against the real system.
- stance: hands the reader a Dockerfile to check the claim independently
  rather than asking for trust; states plainly what the toy version omits on
  purpose.
- notice: the gap between what a minimal implementation must do and what a
  production system adds on top — the piece's back half is entirely that gap,
  itemized.
- diction: plain nouns for architecture pieces (mask, head, block), a
  metaphor introduced once ("see into the future") before the formal name
  ("causal mask") replaces it for the rest of the piece.
- reader: assumed to want the smallest thing that is still real, not a
  simplified toy detached from the actual weights.
- the missed move: the piece closes on the open engineering problems the
  minimal build exposed once compared to the real system, not on a summary of
  what was built — the ending is a list of unclosed gaps, not a conclusion.
Calibration: "We can test our implementation with... which gives the output:
the most powerful machines on the planet. It works!!!"
