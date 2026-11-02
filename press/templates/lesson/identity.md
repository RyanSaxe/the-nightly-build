# lesson

A lesson teaches one main idea to a reader who is working through a course. A reader who finishes it
can explain the idea, use it on a new case, and say how it extends earlier lessons.

## Teach one idea

Write the main idea as one sentence of at most 30 words in `draft-handoff.md` before you start
drafting. Correct the sentence if your work changes the explanation. If the idea won't fit in 30
words, the topic holds more than one idea. Teach the first one and save the rest for a later lesson,
even if they are usually taught together.

Use that sentence to decide what goes on the page. For each section, ask whether a reader could
still explain the main idea without it. If so, cut the section, even if what it says is true and
interesting. A later lesson can pick it up. A contradiction in the evidence counts as material, and
belongs on the page, only if it changes what the lesson says.

Aim for about 2,000 words of prose. Prose means every sentence a person reads, including the two
cards, captions, table cells, and problems. It leaves out equations, code, printed output, text
inside drawings, and the sources list. The editor counts these words on the rendered page and
reports the count under The experience in the editorial review.

When a lesson runs past about 2,500 words, cut a whole idea or result. Don't shorten the explanation
of what stays, because a reader can't follow a half-explained step.

## Build on earlier lessons

Assume the reader has read the earlier lessons in the course, and spend the lesson on what's new.
Use an earlier idea by name. The first time it appears in this lesson, link the lesson that taught
it. If a sentence is hard to follow without a reminder, add a few words saying what the idea means.
Don't explain the idea again, and don't describe what an earlier lesson did.

- Too little: "Lesson 1 put cell 13 at exactly −2.01."
- Too much: a paragraph that describes the grid again, along with its rewards and how its values are
  solved.
- About right: "An agent that starts in cell 13 earns −2.01 on average, which is that cell's value,"
  with "value" linked.

Link the lesson that introduced a running example, and describe only what this lesson changes about
it. Refer to earlier lessons by title or by idea, since pages don't show lesson numbers. Define each
new term in plain words the first time the body uses it.

## Start from a small case

After the opening card, start the body with a small case, and don't repeat the card's problem
statement. Use specific numbers or a drawing, and state the general rule after the case. Someone who
has just watched one update happen with numbers can read the general equation as a description of
what they saw. Work through the case in order, even though Why this matters has already stated the
idea.

Explain one thing at a time, and return to the same example each time. The reader then has to learn
only the new idea.

Let each section answer a question the last one raised, and ask that question on the page in plain
words. A result with no question in front of it reads as a report.

- Before: "Temporal-difference learning updates an estimate after each move, using the next cell's
  estimate in place of the rest of the return."
- After: "So why wait for the end of the episode? An agent could update after one move, if something
  could stand in for the rest of the return."

Check each paragraph before you keep it. The reader needs every piece the paragraph uses, from this
lesson or an earlier one. If a piece is missing, teach it if it's new, remind the reader if it's
old, or cut the paragraph.

## Write clearly

Write the way a good teacher talks through a problem: one step per sentence, plain verbs, and the
purpose of a step before the step itself. Say "we" for what the writer and reader do together, such
as choosing a case, running the code, or looking at a figure. Say "you" when the reader is the one
acting. Whatever the agent does, the agent is the subject.

This template allows three things that `spec/slop.md` otherwise rules out: addressing the reader,
openers such as "consider" and "let's", and sentences about the lesson itself. It also allows an
analogy that a literal description follows. Lessons may share one order of parts, so apply the
Formula rule in `spec/slop.md` only to phrasing, deks, and headings.

The rules below use sentences from old drafts of this course. Don't reuse the rewrites in a lesson.

**Say who does what.** Put the actor first and the action next. A passive is fine when it ends on a
new term, as in "This decision is made by a sigmoid layer called the forget gate layer."

- Before: "Neither needs the episode history kept."
- After: "Neither method has to store past episodes."

**Keep each sentence to one or two clauses.** Split a sentence that carries several ideas into
several sentences.

- Before: "Using an existing estimate inside the target is bootstrapping, the move dynamic
  programming made in lesson 1, except there the model supplied the average over next cells and here
  a single sampled step stands in for it."
- After: "Using an existing estimate inside a target is called bootstrapping. Dynamic programming
  also bootstraps, but it averages over every next cell. TD uses one sampled next cell."

**Use few numbers.** A lesson explains why something happens, and a run is there to show it. Most
paragraphs need one number or none. Give the number that shows the comparison, and cut the rest.

- Before: "The frozen arrows average −0.86, and 94% of runs end below the hand-drawn arrows. The
  mean sits below the median run's −0.17 because the lowest tenth of runs average −5.62, on arrows
  that often loop: they hold 86% of the episodes that hit the cap."
- After: "The learned arrows score −0.86 on average, well below the hand-drawn arrows' 1.36. Almost
  every run ends worse than it started."

**Write complete sentences.** Don't split one thought across several short lines, and don't close a
paragraph on a line written to sound quotable. A short sentence is fine when it states a complete
point.

- Before: "High variance and a settling bias, read off one cell."
- After: "Cell 13 shows both kinds of error. Monte Carlo's estimate varies widely, and TD's estimate
  starts too low."

**Describe the actual thing.** Keep a figurative phrase only if it's the field's standard term, such
as "deadly triad", or if a literal description follows it. Don't invent a label for a measurement.

- Before: "The exact solve returns once, as a referee."
- After: "We use the exact solve only to measure each estimate's error."
- Before: "The 14-cell mean rises from −0.86 to 1.45."
- After: "The arrows' average value rises from −0.86 to 1.45."

**Start each paragraph with its main point.** In a paragraph about a worked case, the main point is
what happens in the case. Don't announce how many points are coming.

- Before: "Three properties fix where Monte Carlo is useful."
- After: "Monte Carlo can't update a cell until the episode ends. Its first-visit average is
  unbiased but noisy."

**Use one word for each thing.** Readers assume that a new word means a new thing.

- Before: "the walker", "the learner", and "the agent", all for the same thing.
- After: "the agent" every time.

**Give parallel items the same structure.** Apply this rule to steps, figure captions, and table
rows. Readers assume that a difference in structure means something.

- Before: "Monte Carlo waits for the end of the episode. An update happens under TD after each
  move."
- After: "Monte Carlo updates after each episode. TD updates after each move."

**Name the thing instead of writing "this" or "that" alone.**

- Before: "That matters when the quantity being estimated drifts."
- After: "A constant step matters when the quantity being estimated drifts."

## Why this matters and The takeaway

Every lesson opens with Why this matters and closes with The takeaway. `furniture.md` documents
both. Write them after the body.

Why this matters runs about 100 to 150 words. First, it names the problem this lesson solves.
Second, it states the new idea in terms from earlier lessons, then gives the idea's name. Third, it
says what the reader will be able to do, in words particular to this lesson. Don't use a stock
opening for that third part, because lessons that share a phrase read as a formula. Include a
real-world case only if it shows the idea at work, and keep it to a sentence or two. If you say that
later work depends on the idea, name the later methods.

The takeaway runs about 100 words. It states the idea and what the lesson found, plainly enough that
the reader could repeat it to someone else. It introduces nothing new.

Why this matters carries the Background band, which lists the earlier lessons this one relies on and
then other reading. The takeaway carries the Go deeper band, which lists reading outside this site.
Each row is a link and one line on what the reader will get from it, in terms the course has taught.

## Reader check

Every lesson gets a reader check after the editor's first review, even if that review approves. The
orchestrator runs the check. A lesson settles only on an editorial review that follows the last
check and has no required change.

First, the orchestrator builds the lesson with `nb preview`, uses Playwright to save the page's
visible text and images of the page with collapsed sections closed, and starts a new agent. The
agent receives those files, the text of the earlier lessons the lesson links (`nb history --show`),
and the reader's background from `press/editorial.md`. It doesn't receive the commission, brief,
evidence record, or voice guide. It opens only the files it was given and runs nothing.

Second, the agent treats those earlier lessons as everything it knows about the subject, even if it
knows more. It restates the main idea in its own words. Then it lists each place where it got lost,
starting with the worst, and quotes the passage. A place counts when a sentence uses a term or step
that neither the lesson nor those earlier lessons explain, when a step doesn't follow from the one
before it, or when the agent can't say why a sentence is there. Last, it names any section it could
skip and still explain the main idea, and any passage that reports a result without saying what the
result means.

Third, the orchestrator copies the report into the editor's next `review-brief.md`. The editor
compares the restatement with the main-idea sentence, and a mismatch means the page has to change.
For each place, the editor first asks whether the passage can be cut. The editor adds explanation
only where the main idea needs it, and records the action on each place in the editorial review.

If the editor's response changes the lesson's central explanation or rewrites a whole section, the
orchestrator runs the check again on the new page with a new agent, because no reader has seen that
text.
