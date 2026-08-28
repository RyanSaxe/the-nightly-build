# Voice guide: investing/working-capital (01)

## How this piece should sound

This lesson teaches working capital as a mechanism: how receivables, inventory,
and payables absorb and release cash as a business operates and grows, and why
the change in working capital is the reason a profitable company can still run
short of cash. The reader arrives with the mathematics and with the earlier
lessons, the income statement, the balance sheet, and the profit-versus-cash
gap. What they lack is this particular machinery. Write for someone who can
follow arithmetic without hand-holding but has never been shown how a dollar of
sales growth becomes a dollar tied up in receivables. The register is calm and
exact, and the persuading is done by the worked example.

Build each account before the sentence that uses it, the way Olah introduces the
intermediary variables c and d only when the explanation is about to need them.
Accounts receivable, inventory, and accounts payable can each be defined by what
they represent in the operating business, the cash owed by customers, the cash
held in unsold inventory, the cash the company still owes its suppliers, before
any of them appears in a cash-flow line. Damodaran's habit of pinning a term to
its fundamentals before he uses it for anything is the model: a change in
receivables is only addable once receivables mean something concrete to the
reader.

When the change in working capital becomes a cash flow, it can be shown by
moving a real figure through the accounts one step at a time, as Olah walks a
single change from a through c to e. A company whose sales rise lets the reader
watch receivables and inventory grow alongside them, with the cash that growth
consumes appearing as the difference. The reader should come away able to
reproduce the number. The same walk run in reverse gives the
negative-working-capital case, where customers pay before suppliers are paid and
the business is financed by that gap; running the same steps lets the sign fall
out on its own.

The cash conversion cycle and its three measures, days sales outstanding, days
inventory outstanding, days payable outstanding, belong where the mechanism
needs a way to count time, after the reader has already seen cash leave and
return. Each can be introduced the way Weng introduces attention, by first
naming the quantity the reader is tracking, the number of days a dollar sits in
inventory before it sells, and then attaching the term to it. A label like DSO
is earned once the thing it counts has been built in front of the reader.

The lesson turns on a distinction the reader is likely to blur, profit against
cash, and Damodaran's separation of value from price is the pattern for holding
it: name the two plainly and never let a sentence use one where it means the
other. The cash conversion cycle can arrive as the answer to a limitation the
reader has felt, the way Weng names what a fixed-length summary forgets before
offering the fix. A single balance-sheet snapshot shows the cash tied up today
and not how long each dollar stays tied up, and measuring that duration is the
work the cycle does.

A figure the reader cannot scale on their own, the cash a fast-growing retailer
swallows over a year, can be anchored to something they already hold, as Olah
restates a speed-up as a week set against 200,000 years. The place where growth
multiplies the cash tied up is where such a comparison earns its keep.

Two of the lesson's cards, the opener and the takeaway, speak to the reader
directly; the body speaks to no one and never mentions itself. Hold the same
calm, exact voice across that shift, so the two cards read as the same teacher
who wrote the body, now turned to face the person in front of them.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That's the difference between a model taking a week to train and taking 200,000 years."

Olah gives the speed-up first as a bare multiple, then restates the same
multiple as two durations a reader already has a feel for, a week against
200,000 years. The general claim leads and the number that scales it follows, in
one short run of sentences. He clearly judged that "ten million times" would not
land until it was a week and a span no human lives to see.

> "What if we want to understand how nodes that aren't directly connected affect each other? Let's consider how e is affected by a. If we change a at a speed of 1, c also changes at a speed of 1. In turn, c changing at a speed of 1 causes e to change at a speed of 2. So e changes at a rate of 1*2 with respect to a."

He does not state the chain rule and then illustrate it. He moves one change
through the graph a single edge at a time, carrying the running number in the
prose, and the rule is what the reader is left holding at the end. Every sentence
advances the same worked example by one step, so nothing is asserted that the
sentence before it has not already made true.

> "For example, consider the expression e=(a+b)*(b+1). There are three operations: two additions and one multiplication. To help us talk about this, let's introduce two intermediary variables, c and d so that every function's output has a variable."

The variables c and d arrive with a stated reason, that every operation should
have a name to refer to, at the moment the explanation is about to need them.
Olah counts the operations in plain words, two additions and one multiplication,
before he reaches for any symbols. The reader is never left holding notation
whose purpose has not yet come up.

## Aswath Damodaran, "Thoughts on intrinsic value"

Source: https://aswathdamodaran.blogspot.com/2011/06/thoughts-on-intrinsic-value.html

> "It is the value that you would attach to an asset, based upon its fundamentals: cash flows, expected growth and risk. The essence of intrinsic value is that you can estimate it in a vacuum for a specific asset, without any information on how the market is pricing other assets (though it does certainly help to have that information)."

Damodaran defines the term by what it is built from, three named fundamentals,
before he puts it to any use. The parenthetical concedes a qualification without
letting it crowd the definition out. The precision is the visible trait: he is a
teacher who will not let a word be used until it has been pinned down.

> "In fact, I have a counter question, when I am asked the question of what the value of a business or stock is: Do you want a value for your business or a price for your business? The answers can be very different."

He splits two words most readers treat as the same thing, value and price, by
turning them into a choice the reader has to make out loud. The distinction is
carried by a plain question rather than a formal definition. This is the move of
someone who has watched the confusion happen and knows exactly which pair of
terms to pull apart.

> "Thus, a bond (coupons), a stock (dividends), a business (operating cash flows) or commercial real estate (net rental income) all have intrinsic values, though computing those values can be easier for some assets than others. At the other extreme, fine art and baseball cards do not have intrinsic value, since they generate no cash flows..."

The rule, that only cash-generating assets have intrinsic value, is made
concrete by a list in which each item names its own cash flow inside a
parenthesis, then a contrasting pair that names none. The abstract test is never
left abstract; every instance carries the specific cash flow that settles it. He
reaches for the everyday examples, fine art and baseball cards, that make the
boundary obvious.

## Lilian Weng, "Attention? Attention!"

Source: https://lilianweng.github.io/posts/2018-06-24-attention/

> "Similarly, we can explain the relationship between words in one sentence or close context. When we see "eating", we expect to encounter a food word very soon. The color term describes the food, but probably not so much with "eating" directly."

Before any equation, Weng grounds the idea in a sentence the reader can parse
without help: seeing "eating" makes a food word likely, while a color word is
tied to it less directly. The example is doing the defining work, and the
mechanism is presented as something the reader already does when reading. She
reaches for the reader's own experience before stating anything formally.

> "In a nutshell, attention in deep learning can be broadly interpreted as a vector of importance weights: in order to predict or infer one element, such as a pixel in an image or a word in a sentence, we estimate using the attention vector how strongly it is correlated with (or "attends to" as you may have read in many papers) other elements and take the sum of their values weighted by the attention vector as the approximation of the target."

With the intuition in place, the definition comes in one careful sentence that
names each part in turn, the weights, the correlation, the weighted sum. The
colon sets up the payoff the first clause promised. The ordering is deliberate:
the plain picture came first, and this is the exact version of the same idea.

> "A critical and apparent disadvantage of this fixed-length context vector design is incapability of remembering long sentences. Often it has forgotten the first part once it completes processing the whole input."

Weng introduces the next idea by first naming the concrete failure of the
current one, that a fixed-length summary forgets the start of a long sentence.
The problem is stated in operational terms the reader can picture before the
solution has a name. The concept that follows then arrives as the answer to a
difficulty the reader has already felt.
