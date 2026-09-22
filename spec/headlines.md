# Headlines, deks, and section headings

This is the standard for the three lines a reader meets first. The prose rules
of `spec/editorial.md` and `spec/slop.md` apply here word for word.

Hold all three to one test: write a line you can defend from what the piece
establishes. Every tell below is a way of avoiding that.

## The headline

Subject, verb, and the surprise in the first words. Put the concrete news ahead
of every qualifier, because a scanning reader may not get past it.

- **State the finding, and say who did it.** "Steve Ballmer was an underrated
  CEO" (Dan Luu) and "Ghostty Is Now Non-Profit" (Mitchell Hashimoto) are claims
  each writer defends. Prefer a specific record to a scope: "A decade of major
  cache incidents at Twitter" (Luu again) tells you exactly what is in it.
- **Use a fresh verb, in the present tense for events.** The classic headline
  pair: "Students applaud later start times" reports the event from the side
  that felt it. "Officials approve schedule change" reports the same event as
  paperwork.
- **Put a number in only where the number is the surprise.** "Building a World
  Map with only 500 bytes" (Simon Willison).
- **Ask a question only where the piece answers it.** "Why is DNS still hard to
  learn?" (Julia Evans) is honest because the post contains the answer.
  Betteridge's law covers the other kind: a headline ending in a question mark,
  so that nobody has to stand behind a claim.
- **The colon subtitle is a machine tell.** "X: How Y Changed Z" and "Company:
  The Adjective Noun and the Adjective Noun" are templates that fit any topic.
  Keep a colon only where you need both halves, as in "git branches: intuition &
  reality" (Evans). Where the right half is decoration, cut the colon and write
  the claim.
- **A triad of paired adjectives ("Faster Models, Firmer Rules, Tighter Supply")
  only sounds comprehensive.** Pick the one development that matters most and
  say what happened to it. Put the other two in the dek or the body.
- **Anchor wit in the story's own nouns, with a plain dek beside it.** The
  Economist headlined a meat-producer merger "A steak in the market" and could
  afford to, because the dek under it stated the argument plainly. Write the dek
  anyway.

All of that at once. A writer who found two chip CEOs reading the same market
data and reaching opposite conclusions could headline it "The Chip Curtain:
Slowdown or Surrender?" and hedge twice, once with the borrowed metaphor and
once with the question. You found something better, so say it: "Two CEOs read
the same chip data and reach opposite conclusions."

## The dek

Put in the dek what the headline left out, and never restate the headline.
Commit the headline to the surprise, then give the dek the who, the what, and
the one detail that makes the piece unmistakable for any other. "The very modern
corporate tale of what happens when a top executive at a $6 billion public
company can't stop tweeting" works because of the dollar figure and the verb.
"The fascinating tale of a San Francisco-based executive" identifies nothing.
One lean sentence, a stance and not a topic, and no detail that pulls attention
from the thesis.

The negative-parallelism reflex is banned in body prose (`spec/slop.md`) and the
dek gets no exemption. Three dek molds are built from it: the semicolon reversal
("X did A; Y refuses B"), the suspended question ("...and the real question is
whether"), and the comma triad, three clauses joined by commas and closed with
"and" ("The trial cut the rate from 14 in 100 to 2, the general-population
evidence is thinner, and the benefit depends on sustained feeding"). Cut them on
sight. Even a good mold looks stamped once it recurs, so check the recent
library's deks before settling on one.

## Section headings

Each heading is a step of the argument, in the piece's own nouns. Somebody
skimming only the headings should be able to reconstruct the argument and its
order. A heading that would fit any article on any subject is scaffolding, and
the scaffolding slots ("Background", "Implications", "The Road Ahead", "Key
Takeaways") are the machine tell. Keep the `data-nb-section` label short,
concrete, and the same as its heading. A fixed template heading ("Sources") is
furniture and exempt. Everything you write is held to this standard.

Headings repeat the same way deks do. Join two clauses with a comma and "and" in
several of them ("The scale, and what it is compounding against") and the piece
looks stamped however sharp each line is. Build them differently from each
other, and check the recent library's headings as you checked its deks.
