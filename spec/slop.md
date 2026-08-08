# Slop

Slop is the sentence that costs the reader attention and returns nothing. It is
the paper's most common failure and the hardest to see, because a slop sentence
reads as competent prose and often as the best line in the paragraph. This file
defines what qualifies and states the test that removes it. Every role reads it
in `editorial-direction.md`; the editor runs the test on every sentence of every
draft.

## What qualifies

A sentence earns its place by giving the reader something it did not already
hold: a name, a number, a source, a mechanism, a step the argument then uses, a
distinction the piece goes on to spend. Call that the sentence's referent. A
sentence with no referent is slop, whatever it sounds like.

Two shapes account for most of it. The first restates the preceding sentence at
a higher level of abstraction, so the reader crosses it and arrives where they
started. The second asserts an evaluation the article has not evidenced, most
often about the subject's importance, difficulty, or size.

Both are easiest to write at the places a draft feels thinnest: the opening of a
section, the sentence after a quotation, and the last line before a subhead. A
writer with nothing to add there writes something that sounds like an addition.

## The test

Ask one question of every sentence: what does this give a reader that the
sentence before it did not?

If the answer is a rephrasing, a summary of the article's own argument, or an
assessment of a claim already on the page, the sentence goes. If the answer
names something the reader can carry forward, it stays.

Three rules govern how the test is applied.

Cut rather than rewrite. A rewritten slop sentence is usually a better-sounding
slop sentence, because the fault is the missing referent and rewriting does not
supply one. Delete first. Write a replacement only when a real referent was
waiting to be stated.

A license never exempts a sentence. `press/editorial.md` and the article's voice
guide open expressive forms, and a form is permission to write a sentence a
certain way. It is not content, and it does not lower this bar. A licensed form
occupied by a sentence with no referent is slop that arrived with paperwork.

Sounding good is not a reason to keep a sentence. Neither is position. The
closing line of a section is held to the same test as any other, and a section
that has run out of things to say ends one sentence earlier.

## Failures that recur

These are the ones that show up most often, not the boundary of the standard. A
sentence that passes every entry below and still fails the test above is still
cut.

- **Fluff.** Filler openings ("In today's fast-paced world"), empty connectives,
  throat-clearing ("As you might know"), and openers that lecture: Note,
  Consider, Imagine. If a sentence carries no information, it goes.
- **The median AI read.** Smooth, hedged, reaching for the generic phrasing.
  Write the specific word: the drug's name, not "a treatment"; 40 nanometers,
  not "tiny". Commit where the evidence lets you. Anchor the prose to how the
  best writers on the subject write, not to the average of everything written
  about it.
- **Run-ons.** A sentence that piles clause on clause until the reader loses the
  thread gets broken. A semicolon chain is the same failure wearing punctuation,
  and often an em-dash swap: write the period, or write the list. Let the verbs
  carry the weight.
- **Unearned punchlines.** Cut the sentence that announces stakes the argument
  has not built ("that's the whole point", "here's the kicker", "the catch is").
  The "X is the whole Y" family belongs here too ("that identity is the whole
  guarantee", "where it is sent is the whole argument"): a sentence that
  announces its own stakes has stopped making the argument and started grading
  it. A closer or section opener reused as a formula across articles is the same
  failure. So is a house catchphrase. A punch sentence the argument has built
  and a license admits is craft, not a punchline.
- **Hedged contrast.** The "X is not Y; it is Z" mold and its softer cousins
  ("not X but Y", "rather than") stay only when the misconception they correct
  is real and named, and fall wherever the "not" clause is a strawman the
  sentence invented. One or two earned contrasts per piece is the ceiling.
- **Self-reference.** The piece never narrates itself or its newsroom ("this
  dossier", "what follows") and never gestures at a hypothetical reader ("a
  reader will notice", "where a reader's scrutiny belongs"). Report the subject;
  what deserves notice is shown by making it noticeable.
- **Banned terms.** `spec/banned-terms.yaml` lists the words and marks the
  corpus has ruled out and how many uses each may keep. A press extends or
  adjusts the list in `press/banned-terms.yaml`, and the proof counts every
  article against the merged list. When a count runs over, rewrite rather than
  substitute: a synonym carries the same vagueness, and repunctuating an em-dash
  keeps the fluff the dash was carrying. Delete first, then rewrite what
  remains. Keep an em-dash for a real aside or a sharp break, not as a reflex.
