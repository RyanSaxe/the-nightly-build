# Voice guide — paper-of-the-day/grokking

Calm and precise. State what the 2022 paper showed in your own sentence before
you touch a source; the reader should never wait for a citation to learn what
happened. Talk to no one: the piece explains grokking, it does not narrate
itself explaining grokking.

**Reconstruct in your order, not the paper's.** Open on the phenomenon in
plain terms — a network that fits the training table perfectly while sitting
at chance on the rest, for a long time, before it doesn't — and only then
supply "grokking," "progress measures," and the modular-addition setup, each
defined in the sentence that first needs it. A definition placed before the
argument needs it reads as throat-clearing; the same definition placed at the
point of first use reads as teaching. Sequence the piece by what a reader must
know next, never by the order the original sections run in.

**Keep the focal paper load-bearing.** Power et al. gets the measurements: the
p-value(s) tested, the dataset fraction, the optimizer and weight decay
setting, the number of steps to each accuracy threshold. Nanda et al. and the
fragility line enter only at the sentence where they change what a claim
means — the moment "grokking happens" becomes "grokking happens because the
network is computing modular addition by rotation, and the delay is three
identifiable phases," or the moment "grokking is a property of this task"
becomes "grokking is a property of this task under this weight decay and this
numerical regime." Mark that entry as a turn in the argument, not a new
paragraph in a lineup of related work. A source that doesn't move the claim
doesn't get a slot; cut it rather than pad the citation count with it.

**Land the verdict on what was measured, not on vibes.** A reviewer's verdict
names the exact quantity, its range, and the point past which the paper is
silent — "tested at p up to N, on this architecture, with this decay; it does
not show whether the same delay holds at a p in the hundreds of thousands" —
not "the results are promising but more work is needed." State plainly what
the after-record settled and what it left open; don't split the difference
between the two the same way twice.

**Teach the equation by using it.** Walk the p = 113 case with actual numbers
before or beside the symbolic form — pick two residues, add them, take the
modulus, show what the network has to get right on the number it never saw in
training — so the formula lands as a compressed version of something the
reader just did, not a new object to decode. The same rule for the Fourier
formulation: state what a rotation in embedding space buys the network before
writing the frequency terms.

**Sentence-level defaults, held all the way through:** short sentences that
carry one claim each; verbs doing the work instead of nominalizations; the
concrete number over the vague magnitude, with a comparison the reader already
holds. No manufactured punchline sentences that announce their own stakes. No
"X is not Y, it is Z" unless the misconception it corrects is one a real
reader would actually hold — earn every one you use, and use very few. No
self-reference to the piece, the newsroom, or "the reader." One em-dash per
stretch of prose at most, reserved for a genuine interruption, never a
connective. Vary section shapes; a run of similarly shaped sections is a sign
the piece is listing rather than arguing.

**Recently used, do not reuse:** don't frame grokking as "another surprising
curve" — the recent run of Paper of the Day pieces (emergent abilities,
chain-of-thought, Chinchilla) already worked that vein, and this paper's
distinct hook is phenomenon-without-mechanism, not a strange plot. Don't open
with a rescoring-or-replotting move ("replot the same numbers and X becomes
Y") — that's the emergent-abilities piece's opener. Don't open with "a single
X breaks Y" — that's the Adam-optimizer piece's move. No colon-subtitle
headline. No scaffolding section headings ("Background," "Mechanism,"
"Implications," "Verdict") and no heading cadence that keeps joining two
clauses with a comma and "and."

## Nelson Elhage, Chris Olah, et al., "Toy Models of Superposition"
Source: https://transformer-circuits.pub/2022/toy_model/index.html
Craft:
- cadence: Short declaratives carry the claims; longer sentences appear only
  to walk a construction step by step, then the piece drops back to short.
- argument: Builds a controlled, provably-understood toy system first, states
  exactly what it proves there, and only afterward asks whether the same
  mechanism plausibly generalizes to real networks — the proof and the
  extrapolation are never allowed to blur into one sentence.
- evidence: Every mechanistic claim is tied to a specific constructed model
  where the behavior can be checked directly, not inferred from a trend.
- stance: States confidence and its limit in the same breath rather than
  qualifying after the fact; the hedge sits inside the claim, not appended to
  it.
- notice: Catches the gap between "we can prove this in the toy case" and
  "this is what's happening in the wild," and keeps that gap visible instead
  of letting the reader round it off.
- diction: Plain nouns for the mechanism (features, directions, interference)
  rather than borrowed metaphor; technical terms are introduced as tools, used
  immediately, then reused verbatim.
- reader: A peer who will check the math, not an audience to be impressed.
- the move the axes miss: it never lets a mechanism stand in for a phenomenon
  it hasn't demonstrated — a claim earned in the constructed model stays
  scoped to the constructed model until a separate sentence extends it, and
  that extension is flagged as a separate move.
Calibration: "We don't fully understand superposition yet."

## Lilian Weng, "What are Diffusion Models?"
Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
Craft:
- cadence: Long paragraphs that stay readable because each sentence adds one
  new fact and picks up the previous sentence's terms exactly.
- argument: Moves from a plain description of the mechanism in words to the
  formal statement, then to what the formal statement lets you compute — never
  formalism first.
- evidence: Each equation is followed immediately by a sentence translating it
  into what happens to the data physically, closing the gap between symbol and
  behavior before moving on.
- stance: Confident restatement of what each paper actually established, with
  the paper's own name attached to the specific contribution rather than a
  generic "researchers found."
- notice: Tracks exactly which problem in the prior formulation each new paper
  is responding to, so the sequence of papers reads as a chain of fixes, not a
  list of alternatives.
- diction: Ordinary verbs for what data does — "loses its distinguishable
  features," "concentrates in a low dimensional manifold" — instead of jargon
  standing alone.
- reader: Someone who wants to be able to derive the next line themselves, not
  someone being told the destination.
- the move the axes miss: each new source is introduced by naming the specific
  gap in the previous account it closes, which is what keeps four or five
  papers from reading like a bibliography.
Calibration: "They define a Markov chain of diffusion steps to slowly add
random noise to data and then learn to reverse the diffusion process to
construct desired data samples from the noise."

## Jay Alammar, "The Illustrated Transformer"
Source: https://jalammar.github.io/illustrated-transformer/
Craft:
- cadence: Short, sequential sentences that mirror the order of a calculation
  — first this, then this, then this — so the prose has the same shape as the
  worked example it's narrating.
- argument: Shows the system as a whole first, then opens it one part at a
  time, always returning to what the part is for before saying how it works.
- evidence: A single worked numeric example carries each mechanism; the
  general formula appears only after the specific case has already made the
  operation legible.
- stance: Comfortable naming its own abstractions as abstractions — a vector
  is called a convenient fiction for calculation, not oversold as a discovered
  truth.
- notice: Catches exactly where a reader would lose the thread (why three
  vectors, why divide by that constant) and answers it in the next sentence,
  before it can accumulate into confusion.
- diction: Concrete nouns for every intermediate object (score, weighted sum,
  matrix) named once and reused, never swapped for a synonym.
- reader: Someone building the mechanism by hand alongside the prose, not
  reading a summary of it.
- the move the axes miss: the general formula is always a compression of a
  specific case the reader has already computed, so the symbol arrives as
  shorthand rather than as new information.
Calibration: "The score is calculated by taking the dot product of the query
vector with the key vector of the respective word we're scoring."

## Ben Recht, "Reshelving generalization"
Source: https://www.argmin.net/p/reshelving-generalization
Craft:
- cadence: Blunt short sentences that state a position, then a slightly longer
  one that gives the specific reason, rarely more than that per paragraph.
- argument: Names exactly what a body of theory promised to predict, checks it
  against what actually happens, and states the mismatch as the verdict rather
  than working up to it through qualifiers.
- evidence: Grounds every judgment in a specific, checkable failure — a number
  a theory should have predicted and didn't — not in a general vibe that the
  field is troubled.
- stance: Willing to say a widely used framework doesn't do the job it's
  credited with, and says so once, plainly, instead of hedging it across three
  sentences.
- notice: Catches the difference between a term being popular and a term being
  useful, and treats that gap as the actual story.
- diction: Everyday words for technical failure ("the answer is always more")
  instead of the softened academic register that would blur the same claim.
- reader: A peer being told a direct opinion, expected to disagree openly if
  they do.
- the move the axes miss: the verdict names the specific quantity the theory
  failed to predict rather than rendering a general judgment on the theory's
  reputation, which is what keeps the criticism from reading as a hot take.
Calibration: "I put the scare quotes around 'useful' because, like so many
things in statistical theory, 'useful' often just means 'used a lot.'"
