# Voice guide: finding optimal policies

## How this piece should sound

The voice is lesson 1's, unchanged. The body is a patient colleague working a problem on paper. It states what a thing is, computes it on the gridworld with real numbers, and says what the result shows. It speaks to no one and never refers to itself. The reader is fluent in probability, linear algebra and optimization, so max, argmax, sums and fixed points need no gloss as mathematics. What needs a sentence is each RL word on first use: action value, greedy, improvement, optimal. Use the exact terms and keep one word for each idea.

This lesson compares and improves, so three habits matter more than they did in lesson 1.

**Say the max in words, then write it.** Before `max` or argmax appears, say what is being done at one cell: price each of the four moves using the values already computed, and take the largest. Put the four numbers at cell 13 in the sentence, say which move wins and by how much, and only then write `q_π(s,a)` and the argmax. Olah's rule-down-to-a-number passage and Karpathy's read-the-formula-aloud passage are the models. The reader should be able to reproduce the choice with a calculator before the notation arrives.

**Present "better at every cell" as a column of arithmetic.** Where the lesson says the new policy beats the old one, show the old value, the new value and the difference, cell by cell, in a table or a printed grid the reader can compare. State the inequality after the numbers, in one plain sentence. Do not write that the improvement is "clear" or "guaranteed" before the reader has seen a number. For the improvement theorem, take Gundersen's pace: one line of the telescoping at a time, with a plain sentence between lines saying what changed.

**Spend the one correction on a real misconception.** A careful reader will arrive here believing that improving a policy needs a full policy evaluation first, or that the greedy step can wait for exact values. The lesson's own run answers it: one greedy step against `q_π` already raises every cell. Quote the belief in the words a reader would hold it, then correct it with the printed numbers. That is the lesson's only "is not X, it is Y," and it stays only if the piece states the misconception first. Everywhere else, state what is true without the contrast.

Keep the sentence-level discipline of lesson 1. A joke or a plain personal remark is welcome when it comes from the subject, and it goes if the nouns can be swapped for another subject's. Lesson 2 runs code and has a word budget, so leave out any aside that does not help the reader compute, check or understand the next quantity. Tie policy iteration and value iteration together once, at the end, with the numbers each run printed.

The bookends are one particular teacher addressing the reader directly, plain and not loud. The opener picks up the question lesson 1 left open, that nobody said the hand-drawn policy was any good, and names what the reader will be able to do by the end, using this lesson's own nouns and its real case. The takeaway resolves that opener with the numbers the lesson produced and says what comes next, which is learning from samples. Neither summarizes the body or claims importance in general terms. Do not reuse lesson 1's takeaway move or its title and dek shapes.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That's the difference between a model taking a week to train and taking 200,000 years."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
Copy the opener's habit: name the subject, give one figure, then restate it on a scale the reader can feel. For the Why this matters card, use a figure this lesson's real case supports.

> "If we change a at a speed of 1, c also changes at a speed of 1. In turn, c changing at a speed of 1 causes e to change at a speed of 2. So e changes at a rate of 1*2 with respect to a."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
Copy the order: the instance with numbers first, one step per sentence, the product last. Here that is the four action values at cell 13, then the max. The "we" is writer and reader working together, which is as close to addressing the reader as the body gets.

> "When I first understood what backpropagation was, my reaction was: "Oh, that's just the chain rule! How did it take us so long to figure out?" I'm not the only one who's had that reaction."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
Copy the move of stating the reader's likely reaction as one's own before explaining it. A bookend can do this in two plain sentences.

> "Derivatives are cheaper than you think. That's the main lesson to take away from this post. In fact, they're unintuitively cheap, and us silly humans have had to repeatedly rediscover this fact."

Checked: https://colah.github.io/posts/2015-08-Backprop/ (raw HTML via curl), retrieved 2026-10-31
Copy the takeaway shape: the finding in the first sentence, a reason after it, one human aside. The self-reference is allowed only in a bookend card.

## Gregory Gundersen, "The Reparameterization Trick"

Source: https://gregorygundersen.com/blog/2018/04/29/reparameterization/

> "I found these unsatisfactory. What does a "random node" mean and what does it mean for backprop to "flow" or not flow through such a node?"

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
Copy the move of asking what a vague phrase would have to mean. Here the phrases are "the best action" and "a better policy." Ask what each must mean, and the answer is a comparison of values at every state.

> "The first term of the last equation is not guaranteed to be an expectation. Monte Carlo methods require that we can sample from pθ(z), but not that we can take its gradient. This is not a problem if we have an analytic solution to ∇θpθ(z), but this is not true in general."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
Copy the way it points at one term, says what fails, says what the method needs, and says when the failure would not matter. No adjectives, and each claim checks against the line above. This is the register for the step in the improvement proof where the inequality enters.

> "The issue is not that we cannot backprop through a "random node" in any technical sense. Rather, backproping would not compute an estimate of the derivative."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
The model for the lesson's single allowed correction. The wrong reading was set up earlier, and the correction follows it.

> "I always find it useful to close the loop and talk about implementation."

Checked: https://gregorygundersen.com/blog/2018/04/29/reparameterization/ (raw HTML via curl), retrieved 2026-10-31
One first-person sentence of method that introduces the code, kept to one line.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for Image Captioning. Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
Take only the habit of opening on a particular event with particular numbers. The enthusiasm comes from what happened.

> "At the core, RNNs have a deceptively simple API: They accept an input vector x and give you an output vector y. However, crucially this output vector's contents are influenced not only by the input you just fed in, but also on the entire history of inputs you've fed in in the past."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
Copy the definition by what goes in and what comes out. For lesson 2: the greedy step takes a value function and returns a policy, and the evaluation step takes a policy and returns a value function. State each interface before saying how it works inside.

> "There are two terms inside of the tanh: one is based on the previous hidden state and one is based on the current input. In numpy np.dot is matrix multiplication. The two intermediates interact with addition, and then get squashed by the tanh into the new state vector. If you're more comfortable with math notation, we can also write the hidden state update as"

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/ (raw HTML via curl), retrieved 2026-10-31
Copy the order: read the code or formula in words piece by piece, then offer the notation. Do this for the optimality backup and for the value-iteration line of code. Leave out the sentence that precedes it in the source, which starts with "Notice."
