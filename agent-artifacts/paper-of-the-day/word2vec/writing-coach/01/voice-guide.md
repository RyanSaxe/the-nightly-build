# Voice guide: paper-of-the-day/word2vec (01)

## Directive

Register: the house baseline (calm, precise, first-principles) with the Olah/Weng
patience for teaching turned all the way up, because this piece has three
mechanisms to build before it can spend them. Reader relationship: a peer
walking another ML practitioner through NLP literature they haven't read —
never a professor addressing a student, never a hype explainer selling a
result.

Two moves change sentences in this article:

1. **Show the object before you name it.** Every mechanism — the softmax cost
   that makes negative sampling necessary, the PMI matrix that Levy & Goldberg
   found underneath skip-gram, the excluded-word rule inside 3CosAdd — gets a
   small instance the reader can trace by hand (a tiny vocabulary, an actual
   pair of vectors, an actual excluded word) before the term for it appears.
   The term is a label for something already visible on the page, not a
   password the reader has to take on faith. Motivate each fix by the specific
   cost it solves (as negative sampling is motivated by the cost of scoring
   an entire vocabulary at each step), not by announcing "here is a clever
   trick."
2. **Keep the verdict paragraph checkable, not just confident.** Before the
   sentence that commits, state what is fixed and what varies across the
   studies being weighed — the exclusion rule, the dataset, the metric — the
   way a reviewer would before writing a recommendation. Every qualifier in
   the verdict must be cashed out in the next clause: what exactly is true,
   what exactly isn't, on what evidence. A hedge with no boundary attached is
   the banned slop register wearing a lab coat.

## Licenses

```text
form: a single rhetorical question addressed to the reader, at a mechanism's
      pivot point
move: Alammar opens the negative-sampling problem by asking what happens when
      scoring every word in the vocabulary gets too expensive, then answers it
      in the next sentence with the walkthrough itself, so the fix lands as
      the answer to a felt problem rather than a named trick being defined
bar:  at most once in the article, only at a genuine turn (softmax cost to
      negative sampling, or additive analogy to the exclusion rule), and the
      very next sentence must answer it — never left as a hook or a section
      opener
```

```text
form: one sustained concrete spatial image for the embedding geometry
      (coordinates, distance, direction), carried across a paragraph or
      section instead of swapped for a fresh metaphor each time
move: Pavlus keeps a single spatial image running long enough that the
      reader can use it to check a claim — is "king − man + woman ≈ queen"
      really a statement about direction and distance — and then explicitly
      marks the point where the image stops holding
bar:  must be used to make one specific mechanism checkable (why cosine and
      not Euclidean distance, why excluding the query words matters
      geometrically), and the piece must name where the image breaks down;
      an image never tested against the mechanism is decoration
```

```text
form: a hedge that quantifies a boundary, not a hedge that softens a claim
move: Pavlus's "sort of" survives because the piece cashes it out sentence by
      sentence, saying exactly what an embedding direction does and does not
      encode instead of leaving the qualification as a mood
bar:  every hedge in the verdict section is followed immediately by the
      specific scope it draws (which dataset, which exclusion rule, which
      result); a hedge that just softens without a stated boundary is cut
```

## Recently used, do not reuse

- The dek/headline reversal mold this desk has run for several straight
  nights — "Paper X's own result was really about Y" — and its two vehicles:
  the semicolon/comma reversal ("Rescoring the same GPT-3 outputs turns a
  leap into a slope") and the em-dash swap. Find the headline true to
  word2vec without either.
- The suspended-question dek and the comma-triad dek (`spec/headlines.md`);
  neither is native to this material and both are already overused stock.
- Section headings that join two clauses with a comma and "and" ("The scale,
  and what it is compounding against") — vary the shape.
- Generic scaffolding headings ("Background," "Implications," "Key
  Takeaways") — already banned by the house standard, worth naming here
  because a paper-desk piece reaches for them under deadline pressure.

## Chris Olah, "Deep Learning, NLP, and Representations"
Source: https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/
Craft:
- cadence: a short declarative claim, then one sentence that turns it — "But
  there isn't anything particularly impressive or exciting about that" pivots
  from settled theory to the actual subject without a transition word.
- argument: starts from a capacity the reader already grants (a network can
  memorize a lookup table) and only then asks what's interesting about what
  training actually finds, so each step earns the next rather than staging a
  reveal.
- evidence: a small trained task (predicting whether a short sentence is
  valid) and the nearest-neighbor lists it produces, reported plainly and
  left to make the point unassisted.
- stance: a fellow puzzler working through the strangeness of what training
  produces alongside the reader, not a professor certifying a result.
- notice: catches exactly where a finding could be over-read — "These
  properties more or less popped out of the optimization process" — naming
  the emergence without dressing it up as more than it is.
- diction: plain nouns for the machinery (words, sentences, distance); no
  term is reached for before the thing it names has appeared.
- reader: assumes technical patience and background, not the specific
  literature; rebuilds from first principles rather than citing prior art
  as a substitute for explanation.
- sequencing: the phenomenon always appears in a small experiment before its
  name does — the label is a summary of something already visible, never a
  password for something still abstract.

## Jay Alammar, "The Illustrated Word2vec"
Source: https://jalammar.github.io/illustrated-word2vec/
Craft:
- cadence: a short summary sentence followed by one longer explanatory one;
  each paragraph makes exactly one move before stopping.
- argument: layers one abstraction onto the last — numbers, then vectors,
  then vector similarity, then word vectors, then the training signal, then
  negative sampling — and never doubles back to redefine an earlier step.
- evidence: an invented worked example (a five-number "personality" vector,
  a constructed neighbor list) built specifically so the next abstraction is
  checkable by hand, not borrowed from the paper being explained.
- stance: direct address in the second person, walking the reader through a
  shared problem rather than lecturing from outside it.
- notice: introduces negative sampling exactly at the moment the naive
  training objective becomes expensive to compute, so the fix answers a
  problem the reader has just felt, not a trick being announced.
- diction: everyday phrasing for technical operations ("looking at which
  other words they tend to appear next to") stands in until the formal term
  is needed and has been earned.
- reader: assumes no prior NLP background; every technical word gets a plain
  restatement before its second use.
- problem-before-fix: the order is always cost, then remedy — the reader
  meets the expense of scoring the full vocabulary before meeting negative
  sampling as the answer to it.

## John Pavlus, "How 'Embeddings' Encode What Words Mean — Sort Of"
Source: https://www.quantamagazine.org/how-embeddings-encode-what-words-mean-sort-of-20240918/
Craft:
- cadence: an explanatory passage followed by a short sentence that
  unsettles the claim just made, keeping the piece from resting on its own
  momentum.
- argument: moves from mechanism (how an embedding is built) to the
  interpretation people attach to it, to the gap between the two, landing on
  a bounded claim about what the numbers are actually doing.
- evidence: names the king − man + woman ≈ queen example directly, credits
  it for the attention it earned, then explicitly separates that resonance
  from proof of understanding.
- stance: a patient explainer who respects the reader's intelligence and is
  willing to unsettle a popular claim without mocking whoever believed it.
- notice: catches the exact place enthusiasm outran the mechanism — an
  example "enhanced the aura" rather than demonstrated the claim — naming the
  overclaim with a precise verb instead of a verdict-word.
- diction: the same spatial nouns (coordinates, distance, direction) recur
  through the whole piece instead of being swapped for synonyms.
- reader: general-educated, so every term gets defined in place; the
  discipline of a scoped hedge transfers regardless of the reader's
  technical level.
- title-as-verdict: the hedge is stated in the very first words the reader
  sees, then earned sentence by sentence rather than held back for a closing
  paragraph.

## Zachary C. Lipton and Jacob Steinhardt, "Troubling Trends in Machine Learning Scholarship"
Source: https://arxiv.org/abs/1807.03341
Craft:
- cadence: a two-beat rhythm repeated per pattern — the aspirational
  statement of what good practice looks like, then the documented departure
  from it.
- argument: keeps the observed pattern (what papers actually do) and the
  speculative cause (why they do it) in separate sentences, and never lets
  the second borrow the first's certainty.
- evidence: each named failure (mathiness, conflating explanation with
  speculation) comes with a citable instance, not a mood or an adjective.
- stance: a concerned colleague addressing the field's practice, not a
  prosecutor scoring a particular paper.
- notice: flags exactly where a paper's language claims more certainty than
  its result supports, and stops there instead of extrapolating to intent.
- diction: neutral technical nouns for failure ("departures," "patterns")
  in place of charged adjectives that would do the judging for the reader.
- reader: practitioners who have read or will read the papers under
  discussion, so the critique can name specifics without re-deriving the
  field for them.
- causal-discipline: marks, in the prose itself, the sentence where the
  essay shifts from an established pattern to an uncertain cause, so the
  reader always knows which register — reported fact or speculation — they
  are reading in.
