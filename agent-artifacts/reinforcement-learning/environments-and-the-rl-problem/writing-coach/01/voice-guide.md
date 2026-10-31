# Voice guide: environments and the RL problem

## How this piece should sound

The body is a patient colleague working a problem on paper. It states what a thing is, computes it on the gridworld with the real numbers, and says what the result shows. It speaks to no one and never refers to itself. The reader is fluent in probability, linear algebra and optimization, so nothing about expectations, matrices or sums needs explaining. What needs explaining is every word RL takes for granted: state, reward, return, policy, episode, terminal. Define each in the sentence where the lesson first needs it, in the words you would use across a table to a smart friend from another field.

Gundersen's passages show the move to copy for definitions and derivations. He quotes the explanations he found unsatisfactory, asks what the vague phrase would have to mean, and then writes the equations out line by line with a plain sentence between steps saying what changed. Karpathy's passage on the RNN step shows how to talk around a formula: say what each piece of it does in ordinary words, then give the notation. Olah's passages on derivatives show how to carry a general rule down to a number the reader can check by hand before the rule is stated. For this lesson that means computing a return or a one-step backup on the gridworld before, or right beside, the general equation. Use the subject's exact terms (transition, return, discount, Bellman expectation equation) and keep one word for each idea.

Where the material gives a reason a wrong turn is tempting, say who tempts it and why it fails. Olah's "Isn't This Trivial?" and Gundersen's "Sanity check" both name a real misconception and then correct it. Do that only where a real reader would arrive at the misconception, for example reading the Markov property as "the past does not matter."

The bookends speak to the reader, and the permission to do so is a license to be direct, not to be loud. Olah's introduction gives one concrete figure for what is at stake and one sentence on what the thing is, and his conclusion says what to take away in his own first person, with a reason. Karpathy's opening shows a person with a stake in the subject. Take from them that a bookend can sound like one particular teacher who knows what was just taught. The opener names what this lesson lets the reader do and where the idea is at work, using this lesson's own nouns. The takeaway resolves what the opener set up and names what comes next in the course. Neither one summarizes the body or announces importance in general terms.

A joke or a plain personal remark is welcome when it comes from the subject, as in Olah's "us silly humans" or Karpathy's "forget I said anything." Hold it to the standard in `spec/slop.md`: if the nouns can be swapped for a different subject and the line still stands, cut it.

The brief decides one more thing the exemplars cannot. Each of these writers has room to wander, and a 3600-word lesson that runs code does not. Leave out any aside that does not help the reader compute, check or understand the next quantity.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That's the difference between a model taking a week to train and taking 200,000 years."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
The opening names the subject, then gives one figure and the same figure as a week against 200,000 years, so the reader can scale it. The writer sounds like someone who wants the reader to see why the algorithm is worth the next ten minutes. This is the register a Why this matters card can hold, with the figure replaced by whatever this lesson's subject actually supports.

> "If we change a at a speed of 1, c also changes at a speed of 1. In turn, c changing at a speed of 1 causes e to change at a speed of 2. So e changes at a rate of 1*2 with respect to a."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
This is a rule carried down to numbers before it is stated in general. Each sentence takes one step along the graph, and the product at the end is the arithmetic the reader would do themselves. The "we" is the writer and reader working together, which is lighter than an address to the reader and is the closest the body should come to one.

> "When I first understood what backpropagation was, my reaction was: "Oh, that's just the chain rule! How did it take us so long to figure out?" I'm not the only one who's had that reaction."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
Here the writer states his own first reaction, which is the reaction a reader is about to have, and then explains why it was wrong. A person with a history with the subject is visible, in two plain sentences.

> "Derivatives are cheaper than you think. That's the main lesson to take away from this post. In fact, they're unintuitively cheap, and us silly humans have had to repeatedly rediscover this fact."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
A takeaway that states a finding in the first sentence and gives a reason after it. The self-reference ("this post") is allowed only in a bookend card, and the aside about silly humans shows the person.

## Gregory Gundersen, "The Reparameterization Trick"

Source: https://gregorygundersen.com/blog/2018/04/29/reparameterization/

> "I found these unsatisfactory. What does a "random node" mean and what does it mean for backprop to "flow" or not flow through such a node?"

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
After quoting three informal explanations, he asks what the key phrase would have to mean to be true. The questions are about the vocabulary itself, and the rest of the post answers them. A lesson that defines a word the field takes for granted can ask this of the word before defining it.

> "The first term of the last equation is not guaranteed to be an expectation. Monte Carlo methods require that we can sample from pθ(z), but not that we can take its gradient. This is not a problem if we have an analytic solution to ∇θpθ(z), but this is not true in general."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
This follows a multi-line derivation. He points at one term, says exactly what fails about it, says what the method needs, and says when the failure would not matter. There are no adjectives in it, and a reader can check each claim against the line above.

> "The issue is not that we cannot backprop through a "random node" in any technical sense. Rather, backproping would not compute an estimate of the derivative."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
The correction of a stated misconception, placed after the post has quoted that misconception. It is the case `spec/slop.md` allows for "is not X, it is Y": the wrong reading is real and was set up earlier.

> "I always find it useful to close the loop and talk about implementation."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
One first-person sentence of method that introduces the code section. It tells the reader why the next section exists, and it is kept to one line.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for Image Captioning. Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
The opener is a specific memory with a time scale and a detail (a few dozen minutes, arbitrary hyperparameters). The enthusiasm comes from what happened. This lesson's subject has no memory to borrow, so take only the habit of opening on a particular event with particular numbers.

> "At the core, RNNs have a deceptively simple API: They accept an input vector x and give you an output vector y. However, crucially this output vector's contents are influenced not only by the input you just fed in, but also on the entire history of inputs you've fed in in the past."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
He defines the object by what goes in and what comes out before saying anything about its insides. The reader gets the interface first. It is a good model for defining the environment as something that takes an action and returns a reward and a next state.

> "There are two terms inside of the tanh: one is based on the previous hidden state and one is based on the current input. In numpy np.dot is matrix multiplication. The two intermediates interact with addition, and then get squashed by the tanh into the new state vector. If you're more comfortable with math notation, we can also write the hidden state update as"

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
The passage reads the code in words, piece by piece, and then offers the notation as an alternative. It never explains matrix multiplication, which the reader already has. Leave out the sentence that precedes it in the source, which starts with "Notice", since the body should not tell the reader how to look.
