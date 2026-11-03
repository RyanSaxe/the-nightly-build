# Editorial direction
These are the exact standing directions for this article. Later sections specialize earlier ones; the orchestrator's commission adds article-specific decisions without rewriting them.

Checkout revision: `dcfff437632af2f98cb49baddc4f82442a892855`

## 1. House editorial standard

Source: `spec/editorial.md`

# Editorial standard

Every article meets this standard, whatever its template and whatever the press.

The first section is about writing, and it applies to everything. The second is
about what this paper does, and an owner may move any of it in
`press/editorial.md` except correctness. Register, formality, and how hard to
press a judgment are an owner's to set in `press/editorial.md` and in the
article's voice guide. Nothing here sets them.

`spec/slop.md` lists the prose failures, and they apply at every register. An
owner may allow one of them in a template or a press, and has to say which one
and where.

Nothing here covers trivia. There is no paper-wide position on the Oxford comma.
Be consistent within a piece.

## The principles of great writing

**It is clear.** Clear writing is easy to understand, and that has little to do
with how hard the words are. Use the exact word. An approximate one leaves a
reader guessing which of several things you meant, and a precise one settles it.
The subject can be difficult without the sentence being difficult. Use one word
for each idea and keep using it. Reach for a synonym and whoever reads it looks
for a second idea.

**It teaches.** Someone who finishes the piece can reason about the subject and
not only recall it. Order it so each part can be used where it appears. Define a
technical term where it first appears and assume the rest. Carry an abstract
claim down to an instance before moving on. Order the piece so each section uses
what you set up earlier.

**It stands on its own.** Someone arriving from a link has read nothing else.
Introduce every term and event inside the article. A lesson in a running course
is the exception, because it may rely on the earlier lessons it links.

**It does original work.** Do something with the sources that the sources did
not do. Say in one sentence what that was. If you cannot write that sentence,
the article is not finished.

## The paper's principles

Correctness is the one nothing loosens. An owner who wants a different bar on
the others says so in `press/editorial.md`.

**It is correct.** Cite what could be doubted and the claims without which the
piece does not work. Common ground needs no citation. Open the source and find
the passage before citing it, and record the section, page or paragraph, so a
reader lands on the words and not on a homepage. Cite the document that made a
claim ahead of any article about it, and where a figure is disputed cite the
document that owns it. If you cannot source a claim, cut it or state the
uncertainty plainly. Never fabricate, pad or decorate a citation.

**It says what the reporting supports.** Say it without hedging. Withholding a
conclusion you can show is its own distortion. Where the reporting does not
reach one, say that, and separate what is established from what is judged. Show
the reasoning from the evidence to the conclusion. Never write that someone
hinted, implied or signalled, which attributes your guess to them.

**It is fair to a view it disagrees with.** State a view in the words of someone
who holds it before taking it apart. Beating a weak version of the opposition
tests nothing.

**It is written for more than one person.** Use the profile in
`press/editorial.md` to decide what to cover and what background to assume, then
write each piece for the audience around that profile. Where the profile is a
new parent, write articles any parent could be handed. Narrow a series to one
person only where `press/editorial.md` or the series prompt says to.

## Numbers

Give the figure and not the magnitude. Give the range a source gives and no more
precision than that. Where nobody could scale a figure alone, put it beside one
they already hold. Say plainly what nobody knows.

## Punctuation

Use the plainest mark that works. Where two marks would both work, use the
plainer one, and where you are unsure use the period.

- **Period.** Two thoughts are two sentences. In most drafts, a period belongs
  where the em-dash, the semicolon or the colon is.
- **Comma.** Joins inside one thought, and sets off a short aside. Two
  independent clauses joined by a comma alone are two sentences.
- **Colon.** Introduces a list, a definition, or the payoff. The clause in front
  of it stands on its own.
- **Semicolon.** Rare. Two independent clauses close enough that a period would
  be too much between them. Do not chain them and do not patch a comma splice
  with one.
- **Em-dash.** A real interruption or a sharp aside. When you delete one, a
  period is usually what belongs there. `spec/banned-terms.yaml` sets the count.
- **Parentheses.** A true aside. Take them out and the sentence still says what
  it said. If you need what is inside them, fold it back in.

An owner may extend this section and may not loosen it.

## Form

Each template's identity specifies its own form: paragraph length, how the dek
reads, how the piece closes. End on the conclusion you built. Skip the generic
moral.

Read the published library for what a series has covered and what not to repeat.
Do not read it for the form. An older piece was written to the format of its
time, and if you copy that structure forward you bring back a section somebody
retired.

### Literal strings

Use inline `<code>` only where somebody must preserve a string's exact spelling:
something they could type, paste, execute or match character for character.
Ordinary terms, product names and model names do not take it, and neither does a
literal you have already established. Where several tokens need comparison, give
them a table or a code listing.

## Charts

Use a chart where a trend or a comparison is the point. Charts are PNGs rendered
from the committed `chart-N.py` script beside the article (`spec/charts.md`).
Label the axes, note a non-linear scale, and cite the data source in the
caption.

## One exception

If following a rule in this file would give you a sentence you would not say
aloud, break the rule. Correctness, teaching and sourcing stay.

## 2. Slop standard

Source: `spec/slop.md`

# Slop

Slop is writing that reads as machine-written. Whoever recognizes it stops
trusting the reporting, which costs the paper more than a dull sentence does.
The editor cuts it on every article, against this file.

Cutting slop does not mean making the prose dry. A joke, a fragment or a short
quotable line is not slop. Do not cut them to stay safe.

## The test

Replace every subject-specific noun in the sentence with a placeholder, then
read what is left.

If the sentence was reporting something, what is left makes no sense, because
the nouns carried it. If it still makes sense, the writer filled in a familiar
pattern and the subject was interchangeable. Cut the second kind.

"The tension here is real, and it is structural" reduces to "the X here is real,
and it is Y", which anyone could write about anything. "The board met twice in
March and adjourned without a vote" reduces to nothing at all.

Run the test on any sentence that sounds like the best line in its paragraph. A
joke that depends on the nouns passes, which is why applying the test does not
flatten a piece.

## Where it sits

Slop is most common at the edges: the first and last sentence of a paragraph, of
a section, and of the article. A writer with nothing left to add writes a
sentence there anyway. Test every edge even when the middles read clean, and
test the article's last sentence most carefully, since it is the position with
the least left to say.

An opening sentence has no earlier sentence to introduce its nouns. The
dangling-referent rule: a definite noun phrase whose referent appears only in
the briefing reads as complete to everyone who wrote the brief, and as a
dangling reference to whoever arrived from a link.

Delete. Do not repair. Rewriting gives you a slop sentence that sounds better,
because the fault is that the writer had nothing to say there. Write a
replacement only when something real was waiting to be said.

## Figures of speech

A figure of speech is allowed when it makes something understood, and never when
it makes something sound important. Rare either way. An agent reaches for these
to add weight. That is the case to cut.

- **Abstractions acting.** "Writing goes unclear", "the argument rests on", "the
  trend demands". Nothing there can do anything. Say who acted, or use the verb
  that states what the thing is. A document is the exception: a filing says what
  is printed in it.
- **Metaphor.** "The pond of prose", "a headwind for the sector". Keep one where
  the comparison explains something a plain sentence cannot. Cut one that
  decorates.
- **Antithesis.** "X is not Y, it is Z", "not just X but Y", "X rather than Y".
  Check every draft for it. It stays only where the misconception it corrects is
  real and stated in the piece.
- **Built to be quoted.** "That's the whole point", "here's the kicker", "the
  catch is". Write one of these and you are grading your own argument. The next
  sentence should continue it.
- **The inflated copula.** "Serves as", "stands as", "represents". Also the
  trailing clause that supplies an opinion in the grammar of a finding:
  "highlighting", "underscoring", "cementing". Write "is", or write the finding.
- **Tricolon.** Three items where the material has one or five. You picked three
  for the rhythm.
- **Anaphora.** Consecutive sentences opening the same way. Repeat once to carry
  an argument. Three times and you are writing to a cadence.
- **The rhetorical question.** "So what does this mean for the industry?" Ask
  one only where the answer that follows is the piece's own work.

Analogy is permitted without qualification. An analogy exists to make something
understood, and whoever reads it either follows it or does not.

## What else it looks like

These failures recur. They are not a complete list, and a sentence matching none
of them still goes if it fails the test above.

- **Empty conclusions.** A sentence that sounds like a finding and states
  nothing the article established: an idea for a subject, a linking verb, and an
  assessment. "That limit is itself part of the design" and "the difficulty here
  should not be understated" state nothing anyone could check.
- **Performed carefulness.** The writer advertising their judgment where a
  qualification belongs. "The honest position is" and "what the evidence has
  established" rate the writer's own care. "The confidence on both sides runs
  ahead of the evidence" rates the people arguing and says nothing about the
  argument. A real qualification states something checkable: what went
  unmeasured, who disagrees, what would settle it. Keep those and cut the
  display.
- **Fluff.** Filler openings ("In today's fast-paced world"), empty connectives,
  throat-clearing ("As you might know"), and openers that lecture: Note,
  Consider, Imagine.
- **Puffery.** Ordinary facts described as significant, pivotal, transformative,
  a testament, a turning point, or part of a broader movement. State what
  happened and give the figures that show how big it was.
- **Reaching for the generic.** The median phrasing where a specific one exists:
  the drug's name, not "a treatment". 40 nanometers, not "tiny". Say what you
  mean and commit where the evidence lets you.
- **Vague attribution.** "Experts argue", "observers note", "many believe". Say
  who, or cut the claim.
- **Self-reference.** The piece never narrates itself or its newsroom ("this
  dossier", "what follows") and never gestures at a hypothetical reader. Citing
  or linking another article the paper published is reporting, not
  self-reference.
- **Formula.** A closer, section opener, dek or heading built to the same
  pattern as the last article's. A house catchphrase is the same failure. One
  article cannot show this, so the editor compares against the recent record.

Punctuation tells belong to the punctuation section of `spec/editorial.md`, and
the counted lexical tells to `spec/banned-terms.yaml`, which a press extends in
`press/banned-terms.yaml` and the proof counts against the merged list. Both
apply here too. When a count runs over, rewrite the sentence. Substituting a
synonym keeps the same vagueness, and repunctuating an em-dash keeps the fluff.
Delete first, then rewrite what remains.

An owner may allow one of these failures in a template or a press.
`spec/editorial.md` sets the terms. The example lesson template has that
allowance for its two bookend cards, so the editor leaves them addressing the
reader and judges them like any other sentence. A sentence written in an allowed
form still has to say something.

## Who this binds

Every role, and every file a role writes. The editor cuts slop out of a draft,
and whoever writes the next article reads the commission, the brief, the
evidence record, the voice guide and the editorial review, and picks up the
register they are written in. Hold your own artifact to this standard before you
hand it on.

## 3. Headline standard

Source: `spec/headlines.md`

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

## 4. Press editorial direction

Source: `press/editorial.md`

# Reader and presentation

Assume a widely read audience with degrees in computer science and mathematics and
experience building machine learning systems in production. Introduce only the
subject-specific context needed to follow the work.

Write concisely and clearly. This audience learns by seeing, so show an idea
wherever it can be shown and use prose for what a visual cannot say. Keep the page
readable and the article free of filler.

Prefer a drawing of the mechanism to a basic bar or line chart: how the parts
connect, where a quantity comes from, what changes from one step to the next. Reach
for whichever of these fits, along with anything else in the furniture catalogs:

- Inline SVG inside `figure.nb-figure`, for a diagram drawn for the article. Set
  colors and fonts with theme variables in `style` attributes (`var(--ink)`,
  `var(--ink-soft)`, `var(--panel)`, `var(--chart-1)` through `var(--chart-6)`,
  `var(--sans)`) so the diagram follows the light and dark themes. Give the `svg`
  an `aria-label` saying what it shows and `style="display: block; width: 100%;
  max-width: 34rem; margin: 0 auto; height: auto"`, and use a `viewBox` about 400 units
  wide so its text stays readable on a phone and in proportion on a desktop. Draw
  panels meant to be compared as separate `svg` elements inside
  `<div style="display: flex; flex-wrap: wrap; gap: 1rem">`, each with
  `style="flex: 1 1 18rem; min-width: 0; height: auto"`, so they stack on a phone.
  A diagram that can't shrink can scroll sideways inside a
  `<div style="overflow-x: auto">`, with its caption outside that `div`.
- Plotly figures from `nb chart`, for anything computed: heatmaps, small multiples,
  surfaces, annotated plots.
- Figures captured from a source with `nb asset`, where the original shows the idea
  best.
- Annotated equations, with color-coded terms in an `nb-math` legend and every
  symbol defined, wherever the math is the point.

Look at every visual in the rendered article before handing it on, at phone and desktop
width and in both the light and dark themes. Build the page with `nb preview` and capture it
with Playwright, which `scripts/install-figure-capture.sh` sets up. Overlapping
labels and arrows that stop short of their target are the common faults, and the proof
catches neither.

## 5. Template identity

Source: `press/templates/lesson/identity.md`

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
inside drawings, the reading bands, and the sources list. The editor counts these words on the
rendered page and reports the count under The experience in the editorial review.

When a lesson runs past about 2,200 words, cut a whole idea or result. Don't shorten the explanation
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

Let each section answer a question the last one raised, so the reader knows why the next step comes.
Put a question on the page only a few times in a lesson, and don't end sections on one. Elsewhere, a
plain sentence can say what's still unsolved.

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

If the editor's response to the first report changes the lesson's central explanation or rewrites a
whole section, the orchestrator runs the check once more on the new page with a new agent, because
no reader has seen that text. Never run more than two checks, because a careful reader always finds
something. The editor answers the second report by cutting or correcting text. It can rerun the
lesson's code but doesn't start new experiments, and it cuts any explanation the existing runs can't
support.

## 6. Series direction

Source: `press/series/reinforcement-learning/prompt.md`

# Reinforcement Learning

The course runs daily and assumes no knowledge of reinforcement learning. It ends with designing
environments and training agents in them, first for control and games and then for language models.
The last topic is reinforcement learning with verifiable rewards (RLVR). Someone who finishes can read
the RLVR literature critically, write an environment and a verifier for a language model, and train the
model in that environment. A package such as `verifiers` is a good place to practice, but teach what
would still be true if the package changed.

Don't simplify the math or the code. Teach each reinforcement learning idea when the course first needs
it. For reinforcement learning, a lesson can rely only on what earlier lessons taught. For everything
else, it can rely on the background in `press/editorial.md`. Explain any reinforcement learning term
the course hasn't taught, and never present one as already known.

## The first three lessons

The first three lessons were written under older instructions. They are
`environments-and-the-rl-problem`, `finding-optimal-policies`, and `learning-values-from-samples`. Read
them to learn what the course has taught and to reuse their environment and code. Don't copy their
length, structure, voice, or the way they refer to each other. Where they disagree with these
instructions about how to write, follow these instructions.

## Curriculum

Work through the stages below in order, with one exception. You can alternate between stages 1 and 2,
because stage 1's topics from the Gymnasium contract onward don't depend on stage 2.

Read the published lessons to see how far the course has come, and teach what it needs next. A topic that holds more than one idea becomes several lessons. You can
split, merge, or reorder topics within a stage. If a lesson needs a foundation the course hasn't taught,
teach the foundation first. New research that changes practice can get a lesson once the course has taught its prerequisites.

The stages set the order of dependencies, and they don't assign topics to lesson numbers. The one target
on timing is that the reader trains an off-the-shelf agent on a custom environment within the first few
weeks. Use the agent's library without explaining its algorithm until a later lesson teaches that
algorithm.

Don't give a "Mention only" topic its own lesson. If it helps the main idea, give it a sentence and a
pointer.

Tools and recipes change quickly, especially in stage 8. When you write a lesson, check that each one still
exists and works the way the lesson says. These names date from November 2026.

### 1. Environments and the RL problem

- The agent-environment loop, Markov decision processes, and the Bellman equations
- Value iteration and policy iteration
- The Gymnasium contract, including termination and truncation
- A first custom environment, checked with the environment checker, random actions, a
  hand-written policy, play by hand, and a look at the scale of observations and rewards
- Training an off-the-shelf agent on it, with a separate evaluation environment, several
  seeds, and random and scripted baselines

Mention only: CleanRL as reading material, PufferLib as a source of practical advice, and
JAX environments.

### 2. Learning from samples

- Monte Carlo and temporal-difference prediction
- Action values from samples and generalized policy iteration
- Why greedy learning stalls, and epsilon-greedy exploration
- SARSA and Q-learning
- On-policy and off-policy learning, with importance sampling
- N-step returns
- Function approximation with semi-gradient updates
- The deadly triad, with its statement and one example of divergence

Mention only: Expected SARSA, backward-view eligibility traces, Gradient-TD, and
Emphatic-TD.

### 3. Designing environments

- Observation contents, scale, and normalization
- The Markov property, with history, frame stacking, and time awareness
- Action spaces, including removal, discretization, factoring, and action frequency
- Action masking in Q-learning and in an off-the-shelf agent
- Reward specification, reward scale, and specification gaming
- Potential-based shaping and the limits of its guarantee
- Held-out levels, procedural generation, domain randomization, and checks for memorized
  behavior
- A small project that changes one design choice at a time and measures each change
  across seeds

Mention only: sim-to-real as an example under domain randomization, and Procgen's way of generating
levels, without installing its package.

### 4. Deep value methods

- DQN with replay and target networks, on small environments
- Double Q-learning and multi-step targets
- What Rainbow's ablation found about its parts
- Small test environments that expose bugs in value learning, and a tabular cross-check
- Reporting results with individual runs, interval estimates, and enough seeds for the
  claim being made

Mention only: dueling networks, distributional RL, noisy nets, and Atari as a benchmark.

### 5. Policy gradients

- Policies for discrete and continuous actions
- The policy gradient theorem and REINFORCE
- Baselines and actor-critic
- Generalized advantage estimation through the λ-return
- The vector environment contract and autoreset
- The importance-sampled surrogate objective and limiting policy change by KL
- PPO built against a reference run, and the implementation details that decide whether
  it works
- Small test environments that expose bugs in policy learning, and diagnostics such as
  entropy, KL, and explained variance
- Hyperparameter search with separate tuning and evaluation seeds
- Soft actor-critic and maximum entropy RL

Mention only: natural gradients, the Fisher matrix, TRPO, monotonic improvement theory,
DDPG, TD3, and offline RL.

### 6. Harder environments

- Bandits, UCB, and regret, as the exploration problem in its simplest form
- Optimism in MDPs through count bonuses and random network distillation, with the limits
  of bonuses
- Partial observability with recurrent policies
- Masking in policy gradients and why the gradient stays valid
- Fast environments, with speed measured on the laptop CPU the course uses
- Curricula through level prioritization
- One complete project on a new environment, trained with an implementation already known
  to work

Mention only: ICM, Go-Explore, HER, PAIRED and unsupervised environment design, and speed
claims measured on GPUs.

### 7. Games

- Normal-form games, mixed strategies, best response, minimax, Nash equilibrium in the
  zero-sum case, and exploitability
- Turn-based games, negamax, and a multi-agent environment contract with turn order,
  per-agent observations, masks, and a way to simulate from any state
- Self-play, non-stationarity, cycling, and how to measure progress against fixed baselines
- Decision-time planning and UCT
- Policy-value networks and PUCT
- AlphaZero's self-play loop, built small on a board an exact solver can check
- Models learned from samples, model error, and MuZero built small
- External regret, regret matching, and why no-regret self-play reaches equilibrium
- Extensive form, information sets, and why a state has no value of its own under hidden
  information
- Counterfactual regret minimization on small poker, checked against a reference
- Sampling with Monte Carlo CFR
- Superhuman poker as a case study in abstraction and subgame solving
- Regularized self-play with policy gradients, and the 2026 results built on it, such as Ataraxos
- Populations through double oracle and PSRO, with leagues as a case study
- General-sum and cooperative games, as the place where zero-sum guarantees stop
- Self-play in a custom game

Mention only: AlphaGo's pipeline as history, Markov games and minimax-Q, Gumbel search,
EfficientZero, Sampled and Stochastic MuZero, NFSP, Deep CFR, DREAM, ESCHER, ReBeL, Student
of Games, Obscuro, CTDE, MAPPO, Hanabi, Cicero, correlated equilibrium, and PPAD.

### 8. Language models

- The model as a policy, with tokens as actions and one reward spread across a sequence
- Fine-tuning as behavior cloning and as a warm-up for RL
- Reward models from human preferences, RLHF, and why its KL penalty exists
- Overoptimization of a proxy
- Reward sources across exact checks, solvers, tests, judges, and learned models
- A first environment and verifier, validated with a known solution and a no-op, with a
  baseline evaluation before any training
- GRPO derived from PPO by removing the critic and taking the baseline from the same prompt
- A small run and what to watch during it
- How much a result depends on the base model, and controls such as random rewards and
  held-out shift
- Rollout reuse, the trainer and inference split, and what PPO's importance ratio and clip do when rollouts are reused
- What GRPO's variants change about length, normalization, and clipping
- The DeepSeek-R1 recipe as a dated example, and current recipes built on specialists and
  distillation
- The verifier as a proxy with an error rate
- Multi-turn and tool-using environments
- Rendering prompts so that the trained tokens match the sampled tokens
- Reward hacking, measured against a true-task metric
- Detection, monitorability, and keeping the reasoning trace out of the reward
- Whether hacking spreads into wider misalignment, and what mitigates it
- Asynchronous training, staleness, and what a run costs
- One complete project that trains a model in a custom environment and audits its results
  for hacks

Mention only: DPO, rejection sampling, active querying, distributional methods,
language-model self-play, evaluation awareness, and the catalog of training frameworks.

## Each lesson

The commission names the topic, the one idea, and the case to start from. It leaves the experiments,
the causes to test, and the page's structure to the writer. Ask the researcher only for what the
page will use, because a lesson on a classic method cites little.

Draw a concept when a drawing shows a structure, a path, or a pattern that a sentence can't show
easily, and put the drawing next to the words that explain it. Show what the agent learned as well
as whether it improved. A learning curve only shows improvement, so go further with value functions
as heatmaps, policies drawn on the grid, trajectories, search trees, or whatever fits the idea. When
a lesson walks through a process, the same diagram can return at each step with the current part
marked, so its notation needs teaching only once. Draw charts of the lesson's own runs as inline SVG
instead of with `nb chart`, because they then follow the light and dark themes and need no outside
source.

When the main idea can be derived, derive it in full, and use a run to check the derivation. A side
result doesn't get a derivation. Put each equation next to the words or figure it belongs to.

Cite what the lesson takes from someone else. A derivation or a run printed on the page is its own
evidence, so a section made of them can go without a citation, and `W-CITE-DENSITY` needs no action
there. Link the paper that introduced an idea when one clearly did. Don't add a sentence only to
hold a citation. In the Go deeper band, say which part of each paper to read and why, in one line.

Keep one small custom environment through the control lessons, and change it only when an idea needs
it, so results stay comparable. A lesson can start the agent from any policy, so pick the one that
shows the idea most plainly. Link the lesson that introduced its rules. A lesson on continuous
actions can add a second small environment, because a grid can't exercise continuous actions.

The writer writes and runs the lesson's code, and its printed output counts as evidence alongside
`evidence.md`. The editor can change the code, rerun it, and update the page to match, and a number
that a rerun prints counts as evidence. Check a chart of the lesson's own runs against the printed
output.

Write the code as Python files with inline script metadata, so that `uv run file.py` works with no
other setup apart from copying any linked file. Run every listing exactly as printed before the
lesson publishes. A published lesson can include only images and chart files, so print in full every
file its listings need to run. A script that only draws a figure can stay off the page. A later
lesson may import a file printed in an earlier lesson if it links that lesson. Put a long experiment
script and its output inside a `details` element. Scale each experiment to finish within a few
minutes on a laptop CPU. When an idea truly needs a GPU, give the recipe and say on the page that it
wasn't run.

Write an experiment script as clearly as the lesson's main code, have it print only the numbers the
page uses, and label every column it prints. Every number from a run appears in that output, or
rounds a number that does. If a script passes about 100 lines, the lesson is reporting too much, so
cut a result instead of compressing the code.

Outside a project lesson, report at most two experimental results, the ones that teach the main
idea. A lesson explains how a method works and why, from its construction and its math, and it
doesn't have to explain everything a run does. When nobody knows why a run behaves as it does, or
showing why would take more than a short section, say so in a sentence or two and move on. Check
each result before you report it:

- Rerun the experiment with seeds you haven't used. If new seeds change the conclusion, rewrite or
  cut it. Round a noisy number to the precision it repeats at, and give its spread when the spread
  changes what the lesson concludes.
- If a result comes from one cell or one seed, check other cells or seeds before you generalize from
  it.
- When the lesson says something causes an experimental result, remove that cause in the code and
  rerun. If the result survives, rewrite or cut the explanation.
- Then find the case the explanation fits worst, such as a cell where its mechanism can't act, and
  run that case. If the explanation doesn't cover it, fix the explanation before you write it up.

Checks of seeds and cells can stay off the page. Use throwaway code, list each check and what it
found in `draft-handoff.md` so the editor can rerun it, and give the conclusion without its numbers.

A claim about a cause has to stay checkable. Put its removal test on the page as a flag or a few
lines in a listing, with its number in the printed output, or cut the claim. A removal test belongs
to the result it explains, so it doesn't count as another result.

End the body with an `nb-note` of two or three problems that can be answered from the lesson and the
course so far. At least one problem asks about a case the lesson didn't work through. One problem
can bring back an earlier idea, with a link to the lesson that taught it. Put each answer and its
working inside a `details` element.
