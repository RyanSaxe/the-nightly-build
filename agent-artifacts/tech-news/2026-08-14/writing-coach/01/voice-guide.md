# Voice guide

## How this piece should sound

This is a brief item: a development stated, and the reason it changes what a
machine-learning engineer knows or can do, in the span the wire-service form
allows. The reader already has the headline. What earns their minute is the
detail the headline left out, delivered without a runway.

State the finding and its significance in the same breath, the way Clark's
Gen-1 item does: one sentence on what the system does, one plain sentence on
why that generalizes ("This is a powerful, general capability"). Don't build
toward the significance across several sentences the way an explainer can —
the item doesn't have the room, and a brief that delays its point past the
opening lines has already lost the reader who came from the headline.

When the piece has a number worth stating, anchor it the way Lee and Trott
anchor GPT-3's theory-of-mind score against a three-year-old and a seven-
year-old, or its training compute against months of work on dozens of chips.
A bare percentage or exponent asks the reader to supply their own sense of
scale; give them one instead, drawn from something in the field they already
have a feel for.

Where a result is genuinely striking, say what it doesn't yet do in the same
motion, the way Timmer's piece states the 48-logical-qubit result and then,
immediately, that this isn't full error correction. The caveat isn't a
hedge tacked on to look careful — it's the fact that keeps the claim honest,
and it belongs next to the result, not filed away in a later paragraph.

Use the field's vocabulary at full precision and don't translate it down.
Toolformer, RLUR, Name Mover Heads, feed-forward layer — the declared reader
holds a machine-learning engineering background, and a term defined once,
plainly, in the sentence that introduces it does more for them than a
softened paraphrase. Clark and Lee both trust their readers with the actual
name of the thing.

Close an item on the state of the work, not on a line that turns back to the
reader. Timmer's piece ends on what has moved from belief to demonstrated
technology — a fact, not a moral. An item in this brief should be able to do
the same: stop where the finding stops.

## Jack Clark, "Import AI 318: RL and addiction; Toolformer; and theology and AI"

Source: https://jack-clark.net/2023/02/20/

> "AI media startup Runway has built Gen-1, a model for editing videos. Gen-1 lets people “realistically and consistently synthesize new videos by applying the composition and style of an image or text prompt to the structure of your source video.”"

This opens the item with what the system is and what it does, in two short
sentences, and lets the direct quotation from the source carry the technical
claim rather than restating it in Clark's own looser words. The writer is
visible in the choice of which four words of the source description to quote
and which to compress into "a model for editing videos."

> "Language models should be thought of less as 'cut and paste machines' and more like 'alien intelligences which can be taught to interface with our world through the context window'. This paper highlights how given a few examples we can train language models to further interface with our world through the use of our tools, and also shows how LMs display some reassuringly generic 'tool use' capability."

This is Clark stating what a result means for how to think about language
models generally, not just what the paper did. The framing is his own
synthesis, offered plainly and without qualification, and it comes only
after two paragraphs of describing exactly what Toolformer is and how it was
trained — the interpretation is earned by the description that precedes it.

> "Benchmarks like ManiSkill2 help drive progress forward, especially in robotics where it's incredibly expensive to train systems in the real world. Kudos to the authors for implementing some soft body physics tasks, as well."

The assessment is small and specific rather than sweeping: it names the
actual mechanism (expensive real-world training) that makes a benchmark
matter, and the second sentence singles out one concrete piece of the work
worth crediting instead of praising the paper in general terms.

## John Timmer, "Quantum computer performs error-resistant operations with logical qubits"

Source: https://arstechnica.com/science/2023/12/quantum-computer-performs-error-resistant-operations-with-logical-qubits/

> "There's widespread agreement that most useful quantum computing will have to wait for the development of error-corrected qubits. Error correction involves distributing a bit of quantum information—termed a logical qubit—among a small collection of hardware qubits. The disagreements mostly focus on how best to implement it and how long it will take."

The opening states the field's consensus and the field's live disagreement
in three sentences, before the story's own news appears at all. Timmer is
visible in the restraint of the second sentence: he defines "logical qubit"
in a clause rather than a separate sentence, and moves on.

> "This isn't full error correction. “What is happening in the paper is that the errors are corrected only after the calculation is done,” Boger said. “So, what we have not demonstrated yet is mid-circuit correction, where during the calculation, we measure… an indication of whether there's an error, correct it, and move forward.”"

Placed right after the paragraph reporting the 48-logical-qubit result, this
sentence states the limit before a reader can mistake the finding for more
than it is. Timmer's own voice is the four-word opening line; everything
that explains the limit is then handed to a named source in his own words.

> "But the value of all of that potential progress is predicated on the belief that we'd ultimately be able to perform a complex series of manipulations on logical qubits and correct any errors in real time. The first half of that has now moved out of the realm of belief and into the list of technologies that have been demonstrated."

The piece's closing line states exactly what changed status — from belief to
demonstrated fact — without reaching for a larger claim about where the
field is headed. The judgment is precise about its own scope: "the first
half," not the whole promise of error-corrected quantum computing.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "We love this example because it illustrates just how difficult it will be to fully understand LLMs. The five-member Redwood team published a 25-page paper explaining how they identified and validated these attention heads. Yet even after they did all that work, we are still far from having a comprehensive explanation for why GPT-2 decided to predict Mary as the next word."

Right after describing an impressive piece of interpretability work, the
writers state plainly how far short of a full explanation it still falls.
The admission of the field's own limits is not softened or buried — it's the
point of the paragraph, stated in the same register as everything around it.

> "OpenAI estimates that it took more than 300 billion trillion floating point calculations to train GPT-3—that's months of work for dozens of high-end computer chips."

A number too large to hold in the head is immediately converted into
something a reader can: a span of time and a scale of hardware. Nothing in
the sentence tells the reader the number is big; the comparison does that
work by itself.

> "GPT-1 and GPT-2 flunked this test. But the first version of GPT-3, released in 2020, got it right almost 40 percent of the time—a level of performance Kosinski compares to a three-year-old. The latest version of GPT-3, released last November, improved this to around 90 percent—on par with a seven-year-old. GPT-4 answered about 95 percent of theory-of-mind questions correctly."

Four data points across four sentences trace a progression, each one given
its own comparison rather than left as a bare percentage. The writers let
the sequence of numbers make the case for how fast the capability moved,
without a sentence telling the reader that it moved fast.
