# Editorial direction
These are the exact standing directions for this article. Later sections specialize earlier ones; the orchestrator's commission adds article-specific decisions without rewriting them.

Checkout revision: `95c2d74961ce9cbad64272443ceb717e735b2d02`

## 1. House editorial standard

Source: `spec/editorial.md`

# Editorial standard

This is the editorial standard every article meets, whatever its template.

The standard is prescriptive on purpose. Its job is to make the default
professional: research-grade writing. It has two parts.

- **Standards a paper cannot loosen.** Sourced claims, teach don't summarize,
  earned analysis, and the prose failures `spec/slop.md` rules out. A template
  or a press may allow one of those prose failures where its own work needs it.
  `spec/slop.md` bans self-reference, for instance, and the lesson template
  allows its two bookend cards to address the reader. Say which failure is
  allowed and where. Nothing loosens sourced claims, teaching, or earned
  analysis.
- **Defaults a paper may override.** Everything that is taste rather than
  quality: register, formality, the assumed reader and that reader's background,
  how far to press a judgment, and any other choice of that kind. These belong
  to `press/editorial.md` and the series prompts. This standard sets the quality
  of those choices, never the choices themselves.

This file bans failures of writing. How a paper sounds is its own to set in
`press/editorial.md`.

The standard does not legislate trivia: no paper-wide rule on the Oxford comma.
Be consistent within a piece.

## Teach, don't summarize

The reader finishes knowing how to think about the topic. Each section builds on
what the last one taught. A section that spends nothing an earlier one taught is
in the wrong place. Cut any sentence that adds nothing new. Define each term of
art the declared reader does not hold in the sentence where it first appears.
Assume the rest. Ground abstract claims in a worked example.

The declared reader centers the paper: the profile chooses what to cover and
when, and what background to assume. Write each piece for the natural audience
around that center. A paper declaring a new parent gets articles any parent
could be handed. A declared practitioner gets pieces worth forwarding to a
colleague. Narrowing a series to the reader personally takes an explicit ask in
`press/editorial.md` or the series prompt.

## Report and analyze

Report what is true and analyze what it means. Hold the analysis to the same bar
as the reporting. Analysis must be earned: grounded in the cited evidence, its
reasoning shown. Keep three things distinct: reported fact, estimate, and
synthesis. Never write that someone hinted, implied, or signalled. That is the
writer's guess presented as attribution. Synthesis with a point of view is
welcome. Cut unsupported opinion. How hard to press a view is the paper's call,
and a press that wants opinion may have a column or an opinion series. A verdict
is welcome once it is earned, and it meets the same bar as any analysis: cited,
reasoned, shown.

## Citations

- Every claim the argument rests on carries an inline citation linking to a
  source entry.
- Prefer primary sources: the document that owns the claim, whatever form the
  document takes. Secondary reporting is acceptable for context. Contested
  figures need a primary source.
- Never fabricate, pad, or decorate citations. If you cannot source a claim, cut
  it or state the uncertainty plainly.
- Cite only what you have read. Open the source, find the passage that supports
  the specific claim, and cite that. Its URL must resolve.
- On contested questions, steelman the opposing views before you weigh them.

## Numbers

Give the figure, not the magnitude, and a sourced range rather than a precision
the source does not support. Anchor a figure the reader cannot scale on their
own to a comparison they already hold. Say plainly what is unknown.

## Clarity

An article is understood on the first read or it has failed. Abstraction is the
usual reason it fails: an abstract noun the article has not built up asks the
reader to carry something unstated, and a weak argument is easy to hide inside
one. Prefer the concrete. Reach for an abstraction only when the abstraction
itself is the subject, and build it up like any other term.

Name a thing one way and keep that name. Once a term is set, reuse it exactly. A
synonym reached for variety reads as a new thing.

Default to short, single-purpose sentences, and vary their length. A long
sentence under control is good writing, and a page of same-length declaratives
is monotonous. If a sentence can be misread, rewrite it rather than trust the
next one to rescue it. Shorten by cutting, never by packing ideas denser. If a
paragraph holds more ideas than it has sentences, it is no longer explaining
them.

## Prose

The house register is a serious paper, not a feed. It is a default, and a press
may move it. `spec/slop.md` is the standard for prose that reads as
machine-written. It binds every article at every register.

Register and formality belong to `press/editorial.md`, which a paper writes for
itself, and to the article's voice guide, which sets how one piece should sound.
A paper that wants to be funny, loose, or direct with its reader says so there,
and every article inherits it. No form is forbidden for being expressive. What
gets cut is writing that fails `spec/slop.md`, at whatever register the paper
has chosen.

If a rule in this Prose section would produce a sentence you would not say
aloud, break that rule. Sourcing, teaching, and earned analysis are not subject
to this.

## Punctuation

Reach for the plainest mark that does the job. When two marks would both work,
the plainer one is right, and when in doubt the period is the default.

- **Period.** The default. Two thoughts are two sentences. Most em-dashes,
  semicolons, and colons in a draft belong where a period would do.
- **Comma.** Joins within a single thought, and sets off a short aside. It is
  not a splice: two independent clauses joined by a comma alone are two
  sentences.
- **Colon.** Introduces what the clause before it promises, a list or a
  definition or the payoff. The clause before it stands on its own. It is not a
  general connector between two thoughts.
- **Semicolon.** Rare. Two independent clauses so tightly bound that a period
  would over-separate them. Do not chain them, do not use one to patch a comma
  splice, and do not use one to extend a run-on.
- **Em-dash.** A real interruption or a sharp aside, and never a general
  connective or a stand-in for a semicolon. When you delete one, the fix is
  usually the period the thought wanted rather than another mark in its place.
  `spec/banned-terms.yaml` sets the count.
- **Parentheses.** A true aside the sentence survives without. If the sentence
  needs what is inside them, it is not an aside, so fold it back in.

A press extends this section for its own paper. It does not loosen it.

## Form

Each template's identity sets its own form: paragraph length, how the dek reads,
how the piece closes. A press may shadow them. This file holds those choices to
a standard. Keep the writing easy to follow. End on the conclusion the argument
built. Skip the generic moral. Let the teaching and the citations equip the
reader to go further.

### Literal strings

Use inline `<code>` only when the reader must preserve a string's exact
spelling: something they could type, paste, execute, match, or distinguish
character-for-character. It is not technical emphasis. Ordinary terms, product
names, model names, and prose do not take it. Neither does every repeat of a
literal once the sentence has established it. When several tokens need
comparison, give them a table or a code listing instead of turning a paragraph
into labels.

An article's form comes only from its template and its own content. Reading the
published library informs content and context: what a series has covered, what
not to repeat. It never informs form. A structure in an older piece records what
the format was at the time. It does not say what the format should be now. A
template that has moved on leaves its old structure in the back-catalog, and
copying that structure forward is how a retired section reappears where it no
longer belongs.

## Charts

Use a chart when a trend or comparison is the point. Charts are PNGs rendered
from the committed `chart-N.py` script beside the article (spec/charts.md),
never hand-drawn images or script blocks. Keep them honest: label axes, note a
non-linear scale, and cite the data source in the caption.

## 2. Slop standard

Source: `spec/slop.md`

# Slop

Slop is writing that reads as machine-written. A reader who recognizes it stops
trusting the article's reporting, which is why it costs the paper more than a
dull sentence does. The editor cuts it on every article, against this file.

Cutting slop does not mean making the prose dry. A joke, a fragment, or a short
quotable line is not slop. Do not cut them to stay safe.

## The test

Replace every subject-specific noun in the sentence with a placeholder, then
read what is left.

If the sentence was reporting something, what is left makes no sense, because
the nouns carried it. If it still makes sense, the writer filled in a familiar
pattern and the subject was interchangeable. Cut the second kind.

"The tension here is real, and it is structural" reduces to "the X here is real,
and it is Y", which is a sentence anyone could write about anything. "The board
met twice in March and adjourned without a vote" reduces to nothing that says
anything.

Run the test on any sentence that sounds like the best line in its paragraph. A
joke survives it when the joke depends on the nouns, which is why this test does
not flatten a piece.

## Where it sits

Slop collects at edges: the first and last sentence of a paragraph, of a
section, and of the article. Those positions feel like they need a sentence, so
a writer with nothing left to add writes one. Test every edge even when the
middles read clean, and test the article's last sentence most carefully: it is
the position with the least left to say.

An opening sentence has no earlier sentence to introduce its nouns. The
dangling-referent rule: a definite noun phrase whose referent appears only in
the briefing reads as complete to everyone who wrote the brief, and as a
dangling reference to the reader who arrived from a link.

Delete. Do not repair. Rewriting produces a slop sentence that sounds better,
because the fault is that the writer had nothing to say there. Write a
replacement only when something real was waiting to be said.

## What it looks like

These failures recur. They are not a complete list, and a sentence matching none
of them still goes if it fails the test above.

- **Empty conclusions.** A sentence that sounds like a finding and states
  nothing the article established: an idea for a subject, a linking verb, and an
  assessment. "That limit is itself part of the design" and "the difficulty here
  should not be understated" name nothing a reader could check.
- **Negative parallelism.** "X is not Y, it is Z" and its cousins ("not just X
  but Y", "X rather than Y"). This is a frequent tell, worth checking on every
  draft. It stays only where the misconception it corrects is real and named,
  and falls wherever the "not" clause is a strawman the sentence invented. An
  earned contrast is rare, so check each against a misconception the piece
  names.
- **Unearned punchlines.** Any sentence engineered to sound quotable while
  carrying little. Announcing stakes the argument has not built is one form
  ("that's the whole point", "here's the kicker", "the catch is"), and the "X is
  the whole Y" family is another ("that identity is the whole guarantee"). Such
  a sentence grades the argument instead of continuing it.
- **Fluff.** Filler openings ("In today's fast-paced world"), empty connectives,
  throat-clearing ("As you might know"), and openers that lecture: Note,
  Consider, Imagine.
- **Puffery.** Ordinary facts described as significant, pivotal, transformative,
  a testament, a turning point, or part of a broader movement. State what
  happened and give the figures that show how big it was.
- **Reaching for the generic.** The median phrasing where a specific one exists:
  the drug's name, not "a treatment". 40 nanometers, not "tiny". Say what you
  mean and commit where the evidence lets you.
- **Decorative analysis.** Trailing clauses that supply unattributed opinion in
  the grammar of a finding: "highlighting", "underscoring", "reflecting",
  "cementing". Also the elaborate copula, where "is" becomes "serves as",
  "stands as", "functions as", "represents".
- **Vague attribution.** "Experts argue", "observers note", "many believe". Name
  who, or cut the claim.
- **Self-reference.** The piece never narrates itself or its newsroom ("this
  dossier", "what follows") and never gestures at a hypothetical reader. Citing
  or linking another article the paper published is reporting, not
  self-reference.
- **Formula.** A closer, section opener, dek, or heading built to the same
  pattern as the last article's. A house catchphrase is the same failure. One
  article cannot show this, so the editor compares against the recent record.

Punctuation tells belong to the punctuation section of `spec/editorial.md`, and
the counted lexical tells to `spec/banned-terms.yaml`, which a press extends in
`press/banned-terms.yaml` and the proof counts against the merged list. Both
bind here too. When a count runs over, rewrite rather than substitute: a synonym
carries the same vagueness, and repunctuating an em-dash keeps the fluff the
dash was carrying. Delete first, then rewrite what remains.

A template or a press may allow one of these failures where its own work needs
it. The lesson template allows its two bookend cards to address the reader,
which the self-reference entry above otherwise rules out. `spec/editorial.md`
sets the terms. A sentence written in an allowed form still has to say
something.

## Who this binds

Every role, and every file a role writes. The editor is the one who cuts slop
out of a draft, but a commission, a brief, an evidence record, a voice guide, or
an editorial review written in slop reaches every article that reads it, because
the writer learns the register those files are written in. Hold your own
artifact to this standard before you hand it on.

## 3. Headline standard

Source: `spec/headlines.md`

# Headlines, deks, and section headings

This file defines the standard for the three lines a reader meets first. The
prose rules of `spec/editorial.md` and `spec/slop.md` apply here word for word.
One test governs all three: the line commits to something the piece establishes.
Every tell named below fails that test.

## The headline

Subject, verb, and the surprise in the first words. Put the concrete news in the
opening words, ahead of every qualifier, because a scanning reader may not reach
the rest.

- **State the finding, with its actors named.** "Steve Ballmer was an underrated
  CEO" (Dan Luu) and "Ghostty Is Now Non-Profit" (Mitchell Hashimoto) are claims
  their pieces defend. A specific record beats a scope: "A decade of major cache
  incidents at Twitter" (Luu again) promises exactly what it delivers.
- **Let a fresh verb carry it, in the present tense for events.** The classic
  headline pair: "Students applaud later start times" reports the event from the
  side that felt it. "Officials approve schedule change" reports the same event
  as paperwork.
- **Numbers earn their spot when they are the story.** "Building a World Map
  with only 500 bytes" (Simon Willison): the figure is the surprise, so it sits
  in the headline.
- **Ask a question only when the piece answers it.** "Why is DNS still hard to
  learn?" (Julia Evans) is honest because the post commits to an answer.
  Betteridge's law names the other kind: a headline ending in a question mark so
  the writer never has to stand behind a claim.
- **The colon subtitle is a machine tell.** "X: How Y Changed Z" and "Company:
  The Adjective Noun and the Adjective Noun" are templates any topic drops into.
  A colon survives only when both halves inform, as in "git branches: intuition
  & reality" (Evans). When the right half is atmosphere, cut the colon and write
  the claim.
- **A triad of paired adjectives ("Faster Models, Firmer Rules, Tighter Supply")
  only sounds comprehensive.** Pick the one development that matters most and
  say what happened to it. The other two get their own sentences in the dek or
  the body.
- **Anchor wit in the story's own nouns, with a plain dek beside it.** The
  Economist headlined a meat-producer merger "A steak in the market" and could
  afford to, because the dek under it stated the argument plainly. Wordplay only
  works on the story's own nouns, and no pun substitutes for the dek.

All of the above, at once: a piece that found two chip CEOs reading the same
market data and reaching opposite conclusions could headline itself "The Chip
Curtain: Slowdown or Surrender?" and hedge twice, once with the borrowed
metaphor and once with the question. It found something better. Say it: "Two
CEOs read the same chip data and reach opposite conclusions."

## The dek

The dek adds what the headline left out and never restates it. The headline
commits to the surprise. The dek supplies the who, the what, and the one detail
that makes the piece unmistakable for any other. "The very modern corporate tale
of what happens when a top executive at a $6 billion public company can't stop
tweeting" works because the dollar figure and the verb do the identifying. "The
fascinating tale of a San Francisco-based executive" decorates without
informing. One lean sentence, a stance and not a topic, and no detail that pulls
attention from the thesis.

`spec/slop.md` bans the negative-parallelism reflex in body prose, and the dek
gets no exemption. Three dek molds carry it: the semicolon reversal ("X did A; Y
refuses B"), the suspended question ("...and the real question is whether"), and
the comma triad, three clauses joined by commas and closed with "and" ("The
trial cut the rate from 14 in 100 to 2, the general-population evidence is
thinner, and the benefit depends on sustained feeding"). Cut them on sight. Even
a good mold looks stamped once it recurs, so check the recent library's deks
before settling on one.

## Section headings

Each heading is a step of the argument, written in the piece's own nouns. A
reader skimming only the headings should be able to reconstruct what the piece
argues and in what order. When a heading would fit any article on any subject,
it is scaffolding, and scaffolding slots ("Background", "Implications", "The
Road Ahead", "Key Takeaways") are the machine tell. The `data-nb-section` label
mirrors its heading, short and concrete. Fixed headings a template mandates
("Sources") are furniture and exempt. Every heading the writer names is held to
this standard.

Headings repeat the same way deks do. A paper whose headings keep joining two
clauses with a comma and "and" ("The scale, and what it is compounding against")
looks stamped however sharp each line is. Vary how they are built, and check the
recent library's headings as you checked its deks.

## 4. Press editorial direction

Source: `press/editorial.md`

# Style and Content Guide

This paper covers public policy, law, artificial intelligence,
technology, science, health, business, markets, and research. It has extra
appetite wherever a story runs through technology and none for a story that is
only trending. The orientation is innovation and research: the new result,
concept, or decision that changes what a field can do.

## Quality

This is a paper of analysis, not a record of events. A deep piece makes an
argument, with the reported facts as premises. Commit to the synthesis the
evidence supports. Assume the day's headlines and spend no space recapping
them. Hold synthesis to a higher bar when it agrees with the crowd. The popular
read is usually the shallow one.

## Voice

The baseline register is Mitchell Hashimoto's technical writing: calm and
precise, argued from first principles. Ideas arrive in plain sentences and
structure does the persuading. Where a piece teaches, take the patience of
Chris Olah and Lilian Weng and build each concept before the sentence that
needs it. Series prompts adapt this register to their subject.

## Page and flow

Favor visible structure. Break a substantial section when it contains distinct
steps or turns in the argument, and give each new section a heading that names
its work. Several long prose sections in a row should trigger another
structural pass. Keep one intact when continuous development genuinely makes
the argument clearer.

Use furniture proactively when evidence has a shape that prose would hide.
Comparisons, sequences, calculations, quantitative relationships, and close
readings of a source should take the form that explains them best, whether a
chart, equation, annotation, table, timeline, or another available component.
Furniture carries evidence or reasoning; it is neither decoration nor a quota.

## Reader

Assumed background: degrees in mathematics and computer science, a career in
machine-learning engineering, and generally well-read.

## 5. Template identity

Source: `templates/lesson/identity.md`

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

Source: `press/series/investing/prompt.md`

# Investing Course

Build a cumulative course in understanding investments and markets. It should
eventually support an independent judgment about an investment and its place in
a portfolio. Teach any financial, accounting, or market concept needed to reach
that point. Routine personal finance and personal investment advice are not.

The long-range destination is the ability to design and build an automated
financial-modeling system grounded in sound investing judgment. Do not make
automation the early subject. Establish the knowledge the system would encode
first; later lessons can turn it into models and software.

Use the published lessons as the curriculum. Choose the most important concept
they have not yet taught, and rely on earlier lessons instead of starting over.
If a later topic exposes a missing foundation, teach that first. Do not fix the
order in advance.

Once the topic is chosen, let the concept determine the lesson's form. Use a
company when it is the best way to make the idea real, while keeping what the
lesson teaches transferable to the next investment. Do not default to quarterly
earnings or a company walkthrough.
