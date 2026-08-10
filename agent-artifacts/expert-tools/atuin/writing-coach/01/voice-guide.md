# Voice guide: expert-tools/atuin (01)

## How this piece should sound

This is a tool write-up for an engineer who lives in the terminal and reads
carefully. The register is Mitchell Hashimoto's: plain declarative sentences
that carry the reasoning themselves, argued from first principles, with the
structure doing the persuading rather than the phrasing. His "I've learned that
when I break down my large tasks" passage states a claim, hedges it honestly,
and never reaches for emphasis to make the point land. The reader has
command-line fluency, so the piece can show Atuin working without narrating an
installation; the worked command is there to prove the tool's value, not to
walk a beginner through setup.

When the piece shows an Atuin command, Julia Evans's strace post is the model
for the walk-through. She runs the tool, then says in short mechanical sentences
what it did, and just as plainly what it did not touch. Her line about the
kernel not being involved in the name check, so it never shows up in the output,
is the move worth taking from her: a demonstration earns trust when it names the
tool's limits at the same resolution as its results. If an Atuin command
deserves to be traced step by step, it can be traced the way she reconstructs a
mechanism from what actually happened on the screen.

Atuin replaces something the reader already has, so the piece will have to judge
whether it earns the swap. Dan Luu's architecture post shows how to weigh a tool
without rounding to a verdict. His Eventlet sentence keeps the benefit and the
cost in view at once, and his "None of these was a major mistake" passage holds
three things apart: a cost worth continuing to pay, a choice not worth migrating
away from, and a decision he would reconsider from scratch. Where Atuin's cost
is real, the piece can name it at that resolution instead of collapsing it into
praise or dismissal.

If Atuin carries a genuine risk or a rough edge, Simon Willison's llm-cmd post
puts the cost first, in plain words, in the same breath as the tool's value, and
the enthusiasm that follows reads as credible because of it. His line about
using Git for fifteen years and still not remembering one command grounds the
value in a specific, real friction rather than an abstract benefit. Where the
piece claims Atuin helps, it can point at the concrete moment in a working
session where it does, the way he points at a command he can never recall.

The frame under the whole judgment is Hashimoto's again: whether the tool works
for the person actually doing the work. His rule to "build only what you need as
you need it and adopt your software as quickly as possible" is that test stated
from first principles, and his willingness to call a demo bad while separating
the implementation from the product itself is the kind of plain, exact judgment
the piece can make about Atuin. A verdict here reads as earned when it commits
to a position and carries its reason inside the sentence.

## Julia Evans, "Understanding how killall works using strace"

Source: https://jvns.ca/blog/2013/12/22/fun-with-strace/

> "What strace does is capture every single system call that gets called when
> executing a program. System calls are the interface between userspace programs
> and the kernel, so looking at the output from strace is a fun way to
> understand how Linux works, and what's really involved in running a program."

She says what the tool does in one plain sentence, then why its output is worth
reading, before showing a single example. The voice is present and a little
delighted, but the sentence still carries real information about the userspace
and kernel boundary. You can hear a specific person who finds this genuinely
interesting and wants you to as well.

> "What's going on here is that it goes through every PID. To find the PIDs, it
> opens the /proc directory. There's a directory in /proc for each PID."

Three short sentences, each one mechanical step, with no connective padding
between them. She reconstructs how the tool works from what it did rather than
asserting it from the outside. The rhythm of short declaratives is most of what
makes the mechanism easy to follow on the first read.

> "The kernel isn't involved in seeing whether or not the process has the right
> name, so we don't see that in the strace output."

The honesty is the craft here. She points at the exact thing the tool cannot
show you and says why, which is what makes the reader trust the parts it does
show. Naming a limit precisely persuades more than a claim of completeness would.

## Simon Willison, "llm cmd undo last git commit—a new plugin for LLM"

Source: https://simonwillison.net/2024/Mar/26/llm-cmd/

> "This is an alpha release. It's a very dangerous piece of software! Do not use
> this unless you are fluent in terminal and confident that you understand what
> it's doing for you and what could go wrong. I take no responsibility if you
> accidentally delete all of your files with this tool."

He puts the cost first, in plain and slightly alarmed words, before he has sold
you on anything. Stating the risk this directly is what makes the enthusiasm
that follows credible. The exclamation and the joke about deleting your files
are a person talking, not a boilerplate disclaimer.

> "The key feature that enables this plugin is the ability to populate the
> user's terminal with text that they can edit before they execute it."

One sentence isolates the single thing that makes the tool worth having,
stripped of everything around it. He has decided what the core actually is and
says only that. The reader comes away knowing where the value sits rather than
with a list of features.

> "This is my favourite example, because I've been using Git for 15+ years and I
> still can't ever remember the exact command for this."

He grounds the tool's value in a specific, slightly embarrassing friction he
still has after fifteen years. The concreteness does the persuading; a general
claim about convenience would not. The self-deprecation is where the person
becomes visible on the page.

## Dan Luu, "In defense of simple architectures"

Source: https://danluu.com/simple-architectures/

> "We previously tried Eventlet, an async framework that would, in theory, let
> us get more efficiency out of Python, but ran into so many bugs that we
> decided the CPU and latency cost of waiting for events wasn't worth the
> operational pain we had to take on to deal with Eventlet issues."

He reports a tool they tried, why it was appealing, and the exact reason they
dropped it, in one sentence that keeps the benefit and the cost side by side.
Nothing is oversold and nothing is hidden. The judgment is specific: operational
pain set against CPU and latency, not a vague sense that it did not work out.

> "None of these was a major mistake, and for some (e.g. Python) the downsides
> are minimal enough that it's cheaper for us to continue to pay the increased
> maintenance burden than to invest in migrating to something theoretically
> better, but if we were starting a similar codebase from scratch today we'd
> think hard about whether they were the right choice."

He calibrates instead of concluding. A choice that was not a major mistake, a
cost cheaper to keep paying than to fix, and a thing he would reconsider from
scratch are three different degrees of regret, and he keeps them apart. This is
what honest weighing looks like when the writer refuses to round to a verdict.

> "When we started out, we strongly preferred buying software over building it
> because a team of only a few engineers can't afford the time cost of building
> everything. That was the right choice at the time even though the "buy" option
> generally gives you tools that don't work."

He states that a decision was right while admitting what it cost, in the same
sentence, with a blunt aside about tools that don't work. The reasoning is
anchored to a concrete constraint, a team of only a few engineers. You watch him
weigh a trade-off rather than defend a position.

## Mitchell Hashimoto, "My Approach to Building Large Technical Projects"

Source: https://mitchellh.com/writing/building-large-technical-projects

> "I've learned that when I break down my large tasks in chunks that result in
> seeing tangible forward progress, I tend to finish my work and retain my
> excitement throughout the project. People are all motivated and driven in
> different ways, so this may not work for you, but as a broad generalization
> I've not found an engineer who doesn't get excited by a good demo."

Plain declarative sentences carry the whole idea, and the structure does the
persuading rather than any emphasis. He hedges honestly before he generalizes,
so the generalization is easy to accept. This is the calm, first-principles
register the paper takes as its baseline.

> "This is an area where I think experience actually hurts. I've seen senior
> engineers get bogged down building the perfect thing and by the time they get
> a demo, they realize it sucks. The implementation doesn't suck, but the
> product or feature itself actually sucks."

He is willing to use a blunt, plain word and repeat it, then draw an exact line:
the implementation is fine, the thing itself is not. The distinction is precise,
which is why the plainness reads as confidence rather than carelessness. The
judgment is his own and he owns it directly.

> "Even if you aspire to release some software for others, build only what you
> need as you need it and adopt your software as quickly as possible."

A single first-principles rule, stated without decoration. He reasons from the
person actually using the software, which is the test he applies to whether a
tool is worth keeping. The sentence commits to a position and carries its reason
inside it.
