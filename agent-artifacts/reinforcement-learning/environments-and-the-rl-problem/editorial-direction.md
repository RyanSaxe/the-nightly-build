# Editorial direction
These are the exact standing directions for this article. Later sections specialize earlier ones; the orchestrator's commission adds article-specific decisions without rewriting them.

Checkout revision: `9b9fb0432e40f6348516ea92d88688f5b4ce5bbd`

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
Introduce every term and event inside the article.

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

Aim past the basic bar or line chart. Draw the mechanism itself: how the parts
connect, where a quantity comes from, what changes from one step to the next. Reach
for whichever of these fits, along with anything else in the furniture catalogs:

- Inline SVG inside `figure.nb-figure`, for a diagram drawn for the article. Set
  colors and fonts with theme variables in `style` attributes (`var(--ink)`,
  `var(--ink-soft)`, `var(--panel)`, `var(--chart-1)` through `var(--chart-6)`,
  `var(--sans)`) so the diagram follows the light and dark themes. Give the `svg`
  an `aria-label` saying what it shows and `style="width: 100%; min-width: 34rem;
  height: auto"`, with `style="overflow-x: auto"` on the figure, so its text stays
  readable on a phone.
- Plotly figures from `nb chart`, for anything computed: heatmaps, small multiples,
  surfaces, annotated plots.
- Figures captured from a source with `nb asset`, where the original shows the idea
  best.
- Annotated equations, with color-coded terms in an `nb-math` legend and every
  symbol defined, wherever the math is the point.

Look at every visual in the rendered article before handing it on. Overlapping
labels and arrows that stop short of their target are the common faults, and the
proof catches neither.

## 5. Template identity

Source: `press/templates/lesson/identity.md`

# lesson

A lesson teaches one subject to a reader who is new to it. The reader is smart
and reads widely. What they lack is this subject. Explain everything the field
takes for granted, however elementary it feels to an insider, and never pad or
talk down.

Every lesson has three parts in a fixed order: the Why this matters bookend, the
body, and The takeaway bookend. The bookends are documented in this template's
`furniture.md`. Write the body first. Write both bookends after the body is
done, so they describe the lesson that was actually written.

Each lesson is one piece of a running course. The library holds everything
already taught. A lesson may build on an earlier one by linking it in Background
instead of re-teaching it, and it should leave ground a later lesson can build
on.

Decide what the lesson teaches before drafting, and keep the list short: teach a
short list completely rather than a long one in passing. Each idea gets three
things: a plain statement of what it is, a worked example with real numbers or a
real case, and the reason it matters here. Finish one idea before starting the
next. When the material does not fit, cut an idea entirely. It can be its own
lesson later. Never keep an idea and shrink its explanation to make room.

Present ideas in the order the reader needs them: nothing appears before
everything it depends on has been taught. Check every paragraph against one test
before keeping it: does the reader have, from this lesson or from a Background
link, every piece this paragraph uses? If not, teach the missing piece first,
link where it was taught, or cut the paragraph.

The clarity rules in `spec/editorial.md` govern the prose. One rule is stricter
here: a technical term enters only when the lesson cannot proceed without it,
and it is defined in plain words in the same sentence or the one just before.

The two bookends are written together, after the body, and they are read
together. Why this matters gives the reader a real reason to read the lesson:
what this subject is, where it is at work in the world right now, and what they
will understand by the end. The takeaway is what they keep: what the lesson
found, said plainly enough to carry away and repeat. Both speak directly to the
reader, in the same plain voice as the body, at whatever length clarity needs.

These two cards are the one place a lesson refers to itself. They address the
reader, and they say what the lesson covers and what the reader will know by the
end. Nowhere else does: the body speaks to no one and never mentions the lesson.

Write the bookends with the care of a teacher who knows exactly what was just
taught and who is reading. Every sentence should belong to this lesson in
particular: its subject, its findings, its place in the course. Posing the
lesson's questions in the opener and answering them in the takeaway is one
honest way to hold the pair together, when it fits. What is required is only
that the takeaway resolves what the opener set up.

When both are drafted, read them back to back without the body between them.
They should read as a setup and its resolution. If either could be moved to a
different lesson, rewrite it around this lesson's particulars.

Neither bookend summarizes the body. The takeaway teaches nothing new and uses
no term the body did not set. Neither claims importance in general terms. Name
the particular thing at stake.

The Background band lists optional reading, from this library or beyond, each
row a link and one line on what it covers. The Go deeper band lists optional
reading for afterward, always beyond this paper, each row a link and one line on
what it offers. The lesson must work for a reader who opens none of them.

## 6. Series direction

Source: `press/series/reinforcement-learning/prompt.md`

# Reinforcement Learning

Build a daily course that starts from no reinforcement learning and ends with
designing environments and training agents in them, first for control and games
and then for language models. The destination is reinforcement learning with
verifiable rewards (RLVR): reading its literature critically, writing an
environment and a verifier for a language model, and training on them. A package
such as `verifiers` is a good place to practice, and the lessons teach what would
survive a change of package.

The course assumes fluency in probability, linear algebra, optimization, PyTorch,
and production deep learning, plus past study of bandits and regret minimization.
It teaches none of that. Where those ideas return, such as UCB in tree search or
regret in counterfactual regret minimization, build on them directly.

## Curriculum

Work through these stages in order. Read the published lessons to see how far the
course has come, teach what it needs next, and build on earlier lessons instead of
repeating them. Within a stage, split, merge, or reorder topics as the teaching
requires. Teach a missing foundation first when one appears, and give new research
a lesson once its prerequisites have been taught. A custom environment with an
off-the-shelf agent training on it should arrive by about lesson 5, with the
library treated as a black box that later lessons open. The course should finish
Designing environments by about lesson 25.

1. **Environments and the RL problem.** From bandits to states, Markov decision
   processes and the Bellman equations, the Gymnasium contract and a first custom
   environment, training an off-the-shelf agent on it, value iteration and policy
   iteration.
2. **Learning from samples.** Monte Carlo and temporal-difference prediction, SARSA
   and Q-learning, exploration from UCB to optimism in MDPs, n-step returns and
   TD(λ), function approximation and the deadly triad.
3. **Deep value methods.** DQN, Double DQN through Rainbow, debugging with probe
   environments, reporting results across seeds.
4. **Policy gradients.** The policy gradient theorem and REINFORCE, baselines and
   actor-critic, generalized advantage estimation, natural gradients and trust
   regions, PPO from scratch and the implementation details that decide whether it
   works, continuous actions and maximum entropy RL.
5. **Designing environments.** Observations and partial observability, action spaces
   and masking, reward design and potential-based shaping, hard exploration, fast
   vectorized environments, generalization and curricula, and one complete project
   on a new environment.
6. **Games.** Zero-sum Markov games and self-play, Monte Carlo tree search as bandits
   in a tree, AlphaGo through AlphaZero built small, planning with learned models,
   imperfect information and exploitability, counterfactual regret minimization
   through superhuman poker, populations and leagues, and self-play in a custom
   game.
7. **Language models.** The model as a policy and fine-tuning as behavior cloning,
   reward models from human preferences, RLHF and how its reward models break,
   verifiable rewards, GRPO, the reasoning-model recipe from DeepSeek-R1, environments
   and verifiers, multi-turn and tool-using environments, reward hacking, training
   infrastructure, and one complete project that trains a model in a custom
   environment.

## Each lesson

Give the math in full, including the derivations. Whenever a concept can be drawn,
draw it before explaining it. A learning curve shows that an agent improved, so go further
and show what it learned: value functions as heatmaps, policies drawn on the grid,
trajectories, search trees, whatever fits the idea.

Link the papers that introduced each idea, and use the Go deeper band to say which
part of each paper to read next and why.

Write the code as Python files with inline script metadata, so that
`uv run file.py` works with no other setup. Run every listing as printed before the
lesson publishes, and report only what the run produced. A later lesson may import a
file from an earlier one, and it links that lesson when it does. Keep one small custom
environment in use through the control lessons and grow it as the course needs, so
results stay comparable and the code accumulates into one project. Scale every run to
finish within a few minutes on a laptop CPU. When an idea truly needs a GPU, give the
recipe and say on the page that it was not run.

End the body with an `nb-note` of two or three problems answerable from the lesson
alone, with each answer and its working inside a `details` element.
