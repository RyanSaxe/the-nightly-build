# Voice guide: expert-tools/beartype (01)

## How this piece should sound

This is a demonstration essay for people who already write Python and read type
hints without help, so it can move at their pace and skip the case for typing
itself. Hold the register Brandur Leach holds when he explains MVCC: calm, in
the first person where a first person genuinely helps, each sentence resting on
the one before it, the term of art defined in the sentence that first needs it.
The declared reader has machine-learning engineering and a mathematics
background behind them, so beartype's sampling mechanism can be explained
exactly rather than gestured at, the way Leach walks a reader through how a
snapshot decides which tuples it can see.

beartype's distinctive claim is near-constant-time checking by sampling a
container's contents rather than walking the whole structure. That is the kind
of value Hillel Wayne argues by mechanism when he writes that an hour of
modeling catches what days of tests miss: the benefit stated first, then earned
one plain sentence at a time. Where the piece makes beartype's case, the case
can rest on how the decorator actually does its work; then the adjectives about
speed and safety will not have to do the persuading.

The code example carries the argument, so it can be shown the way Wayne shows
his demo: the concrete figure doing the work, a found bug turned at once into
something useful. If the example catches a type violation at a call boundary
that a static checker cannot catch at runtime, the reader should be able to see
exactly which value crossed the boundary and why the hint rejected it. Should
the piece measure overhead, a number can carry the appreciation the way Leach
lets two bits per transaction carry his, without a separate sentence grading how
impressive it is.

Where beartype is genuinely good, the piece can say so plainly. Simon Willison,
writing about a tool he built and likes, still names what it does poorly before
he praises it and ties the praise to a concrete count of lines. That candor
about the limitation is what lets the praise land, and it keeps a demonstration
from reading as a sales page. Where the worked example is small or partial, it
can say that in the same voice.

The cost-benefit read is the spine, and it is most credible where it talks the
reader out of the tool. Wayne gives a rough threshold below which specification
does not pay and names it in weeks. The commission asks for exactness about what
beartype's sampling cannot promise, about the hints or constructs it does not
cover, and about where it sits against mypy, pyright, typeguard, and pydantic's
validation. Those boundaries can be stated as flatly as Wayne states his own,
held as findings the piece reaches rather than softened into a reflexive caveat.

## Hillel Wayne, "The Business Case for Formal Methods"

Source: https://www.hillelwayne.com/post/business-case-formal-methods/

> "It'll save you money. FM finds complex bugs in complex systems. The more complex the system is, the more likely a bug will slip past your testing, QA, and monitoring. Since it works at a higher level of design, an hour of modeling will catch issues that days of writing tests will miss."

The benefit comes first and is then earned in mechanism, one flat sentence at a
time: it works at a higher level, so an hour there beats days of writing tests.
Wayne is visible in his ease with "It'll save you money" as a bare topic
sentence, refusing to dress the argument up before he has made it.

> "It took the model checker two seconds to find the error. In less than six minutes I designed the system and found an expensive bug. I even have a set of steps to reproduce the bug, so I can write regression tests on the code itself."

Wayne reports the demonstration in concrete figures, two seconds and six
minutes, and lets the numbers carry the point rather than an adjective. The last
sentence extends the value instead of celebrating it, noting that the checker
also hands him reproduction steps. You can see the practitioner in how fast he
turns a found bug into a regression test.

> "Writing specifications are best when you're working on a complex system. If you can keep the whole system "in your head", or if it does not involve a lot of intricate logic, specifications may not provide you much benefit. As a rough rule of thumb, I don't think specifying things that would take less than a week to implement is worth the effort."

This is the honest limit, stated without hedging: below a certain complexity the
tool is not worth the effort, and he gives a rough threshold in weeks. Wayne is
visible in his willingness to talk a reader out of the tool where it does not
pay, which is part of why the rest of the piece is believable.

## Brandur Leach, "How Postgres Makes Transactions Atomic"

Source: https://brandur.org/postgres-atomicity

> "Postgres's implementation in particular is known to provide powerful transaction semantics with little overhead. And while I've used it for years, it's never been something that I've understood. Postgres works reliably enough that I've been able to treat it as a black box – wonderfully useful, but with inner workings that are a mystery."

Leach admits he ran Postgres for years as a black box, useful but not
understood, and that admission is what sets up the article. The writing is calm
and first-person without being about him. He is visible in the plain honesty of
"it's never been something that I've understood," which a reader trusts more
than a claim of mastery.

> "Under MVCC, statements execute inside of a transaction, and instead of overwriting data directly, they create new versions of it. The original data is still available to other clients that might need it, and any new data stays hidden until the transaction commits. Clients are no longer in direct contention, and data stays safely persisted because they're not overwriting each other's changes."

A mechanism explained in order, each sentence built on the last: statements make
new versions instead of overwriting, the old data stays available, the new data
stays hidden until commit, so clients stop colliding. Leach defines the term of
art in the sentence that needs it and never reaches past what he has already
built. The care in the sequencing is where the teacher shows.

> "In an example of the kind of frugality rarely seen in modern programming, the status of a transaction can be recorded in only two bits, so we can store four transactions per byte, or 32,768 in a standard 8k page."

Leach gives exact figures, two bits per transaction, four per byte, 32,768 per
8k page, and lets one quiet aside about frugality carry his admiration. The
appreciation is earned by the numbers rather than asserted over them. He is
visible in the restraint of noticing something impressive and still just
reporting it.

## Simon Willison, "Large Language Models can run tools in your terminal with LLM 0.26"

Source: https://simonwillison.net/2025/May/27/llm-tools/

> "LLMs are notoriously bad at mathematics. This is deeply surprising to many people: supposedly the most sophisticated computer systems we've ever built can't multiply two large numbers together? We can fix that with tools."

Willison states the problem in one flat sentence, poses the surprise as a
genuine question, and answers it in four words. There is no throat-clearing
before the point. He is visible in the readiness to name plainly the specific,
embarrassing weakness the tool exists to address.

> "A better search tool would have more detailed instructions and would return relevant snippets of the results, not just the headline and first paragraph for each result. This is pretty great for just four lines of Python though!"

Writing about his own tool, Willison says what it does poorly before he praises
it, then ties the praise to a concrete count, four lines of Python. The candor
about the limitation is what makes the appreciation credible. He is visible in
the refusal to oversell software he built and clearly likes.

> "It's such a simple trick: you tell the model that there are tools it can use, and have it output special syntax (JSON or XML or tool_name(arguments), it doesn't matter which) requesting a tool action, then stop."

The whole mechanism in one plain sentence: tell the model what tools exist, have
it emit a request, then stop. Willison strips a much-hyped capability to its
moving parts and adds that the exact syntax does not matter. He is visible in
treating the thing as a simple trick and describing it as one.
