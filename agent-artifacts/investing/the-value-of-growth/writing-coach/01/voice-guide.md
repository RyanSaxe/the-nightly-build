# Voice guide: investing/the-value-of-growth (01)

## How this piece should sound

This is a cumulative lesson that teaches one quantitative finance concept to a
reader who can handle the mathematics but does not yet hold the investing
vocabulary. Assume the arithmetic is easy for them and the words are new. That
gap sets the register: calm, unhurried, argued from first principles, with the
persuasion carried by the order of plain sentences rather than by emphasis. The
reader should be able to follow the concept on the first read and come away able
to explain it to someone else.

Teach the way Chris Olah does in the LSTM piece: reach for a concrete case the
reader already holds before the general statement, not after it. Olah motivates
an abstract problem with "I grew up in France... I speak fluent French" before
any mechanism appears, and the reader is oriented by the time the abstraction
arrives. Where this lesson introduces a new idea about securities, cash flows,
or the price a market puts on them, a worked case can come first and the
generalization second.

Olah also runs one example — a language model predicting the next word — through
every step of the mechanism, so the reader watches a single thing move rather
than reloading a new illustration each section. This lesson can carry one worked
case, one security or one cash-flow stream with real numbers, through the steps
of the concept, and let the numbers on the page do the explaining. A
math-fluent reader rewards actual figures over a gesture at magnitude, the way
Olah keeps his gate values concrete at "a number between 0 and 1" and Damodaran
names specific asset types instead of "assets in general."

Two of the exemplars teach by setting side by side two things a newcomer tends to
merge, then naming the difference on a concrete instance: Damodaran separates
value from price, Marks separates probabilities from outcomes. Where this lesson's
concept sits next to a neighbor the reader is likely to conflate, the passage can
put both on the page and show the gap with a specific case rather than a
definition alone.

Watch where the human voice is allowed to speak. Marks writes "Invest scared!"
and Damodaran addresses "your Picasso"; that direct, plainspoken turn is what
makes both of them sound like a person and not a textbook. In this template that
directness belongs to the two bookend cards, which may address the reader. The
body between them explains the concept to no one in particular and never refers
to the lesson itself. A turn that does land — Damodaran's "Do you want a value
for your business or a price for your business?" — earns its place only because
the sentences before it built the distinction, never because it was reached for
to sound quotable.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Consider trying to predict the last word in the text 'I grew up in France... I speak fluent French.' Recent information suggests that the next word is probably the name of a language, but if we want to narrow down which language, we need the context of France, from further back."

Olah introduces an abstract difficulty — needing information from far back in a
sequence — by handing the reader a sentence they can finish themselves. The
concrete case does the motivating before any formal statement of the problem
arrives, so the reader meets the abstraction already knowing why it matters. The
patience is Olah's: he trusts the small example to carry the idea and does not
rush past it.

> "The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged."

One plain analogy for a mechanism, stated and then immediately qualified with
what the analogy leaves out ("only some minor linear interactions"). The
comparison is doing explanatory work, not decoration, and Olah keeps it honest
by naming its limits in the same breath. The calm, exact voice is visible in how
little he claims.

> "Let's go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject."

Here he grounds one step of the abstract mechanism in the running example, so a
formal operation becomes something the reader can picture. Reusing the same case
across steps is what lets the reader follow a single thread instead of holding
several. Olah's habit of returning to one worked example is the teaching move on
display.

## Aswath Damodaran, "Thoughts on intrinsic value"

Source: https://aswathdamodaran.blogspot.com/2011/06/thoughts-on-intrinsic-value.html

> "Only assets that are expected to generate cash flows can have intrinsic values. Thus, a bond (coupons), a stock (dividends), a business (operating cash flows) or commercial real estate (net rental income) all have intrinsic values, though computing those values can be easier for some assets than others. At the other extreme, fine art and baseball cards do not have intrinsic value, since they generate no cash flows (though they may generate a more amorphous utility for their owners) and value, in a sense, is in entirely in the eye of the beholder."

Damodaran states a rule and then tests it across named cases — a bond, a stock,
a business, real estate, then art and baseball cards on the other side of the
line. The specific instances are what make an abstract definition checkable,
because the reader can run the rule against each one. The professor is visible in
the instinct to enumerate rather than assert.

> "So, how do people value assets where intrinsic value cannot be estimated? They look at what other people are paying for similar or comparable assets: i.e., they use relative valuation. Thus, an auction house sets a value for your Picasso, based on what other Picassos have sold for in the recent past, adjusted for differences (which is where the experts come in). The realtor sets the price for residential real estate, based on what other residences in the neighborhood have sold for, adjusted for differences again."

He introduces a term of art, "relative valuation," and immediately shows it
working in two ordinary settings the reader already understands, the auction
house and the realtor. The definition and the concrete demonstration arrive
together, so the term always has a concrete case attached to it. The
parenthetical asides ("which is where the experts come in") are the sound of
someone thinking aloud in front of a class.

> "In fact, I have a counter question, when I am asked the question of what the value of a business or stock is: Do you want a value for your business or a price for your business? The answers can be very different."

The whole passage exists to separate two words the reader has been using
interchangeably, and it does so by posing the choice directly rather than
defining the pair. It lands because the paragraphs before it built the
distinction, so the question resolves something already set up. Damodaran's
first-person, slightly contrarian voice is what carries it.

## Howard Marks, "The Most Important Thing"

Source: https://www.oaktreecapital.com/docs/default-source/memos/2003-07-01-the-most-important-thing.pdf

> "Hopefully, if I offered to sell you my car, you'd ask the price before saying yes or no. Deciding on an investment without carefully considering the fairness of its price is just as silly."

Marks reaches for the most ordinary transaction there is to make an abstract
discipline obvious. The everyday case carries the principle so plainly that the
formal version needs only one more sentence. His blunt, unpretentious voice is in
the choice of a used car over any finance example.

> "'Defensive investing' sounds very erudite, but I can simplify it: Invest scared! Worry about the possibility of loss. Worry that there's something you don't know. Worry that you can make high quality decisions but still be hit by bad luck or surprise events."

He takes a piece of jargon, admits it sounds impressive, and then restates it in
words a reader already owns. The short repeated "Worry that..." sentences turn an
abstract stance into a list of specific fears the reader can hold. The plainspoken
personality, willing to deflate his own field's vocabulary, is unmistakably
Marks — and note that this direct address to the reader is the kind of move a
lesson keeps for its bookends.

> "It's essential to remember that the fact that something's probable doesn't mean it'll happen, and the fact that something happened doesn't mean it wasn't improbable. So we educate our clients as to what they can fairly expect, and we count on them to bear in mind the difference between probabilities and outcomes."

Marks separates two ideas a newcomer collapses, a probability and what actually
occurred, by stating each direction of the confusion in turn. The symmetry of the
two clauses is doing the teaching: the reader sees the distinction from both
sides before it is named. The measured, first-principles reasoning is the voice
the house baseline points at.
