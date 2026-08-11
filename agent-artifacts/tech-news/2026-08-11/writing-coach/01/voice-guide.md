# Voice guide: tech-news/2026-08-11

## How this piece should sound

This is a brief: four to six items, each a judgment about what moved, for a
reader who already saw the headline and came for the number and the caveat it
dropped. That reader has a graduate machine-learning background, so the
model card's own vocabulary is available without a gloss: parameter count,
weight release, harness, proof checker, in-plane field, RCE. Spend no words
establishing what that reader already holds; spend them on what the primary
record shows once you go past the announcement.

Willison's SWE-bench item opens by placing the result before any number
appears: it says whose run this is and why that matters, before it says what
the run found. An item here can do the same when the primary record's
provenance is itself part of the story, an independent leaderboard rerun, an
advisory versus a vendor's own disclosure, a proof a third party checked
rather than the lab that claimed it. State what kind of document is speaking
before you report what it says, when the reader needs that to weigh the
number.

Willison's line on GPT-5.3-Codex does something an item here can use: it
names an absence in the record as a fact, then offers the plain candidate
explanation as a hedge rather than a finding, "maybe because it's not yet
available." A benchmark leaderboard missing the vendor's best model, a
security advisory silent on a detail the researcher's writeup supplies, a
model card that doesn't report the number the press release leads with. Name
the gap and hedge the reason in the same plain register, without dressing the
hedge up as an inference the record doesn't support.

Hutson's habit of routing a methodological judgment through a named source
rather than his own assertion is worth this brief's items where the caveat
is contested rather than arithmetic: the security researcher who thinks the
disclosed severity is overstated, the mathematician skeptical a proof checker
settles what a headline claims it settles. Put the judgment in the mouth of
the person who holds it and is named for it, the way Jiaxuan You's two
clauses carry both what ARC is good for and what it can't reach, rather than
folding the same judgment into the writer's own voice.

Lambert's one-sentence dismissals of a benchmark's known weakness, SWE-Bench's
skew toward one repository, Terminal-Bench's crowdsourced noise, belong to
this brief's job description directly: it is exactly the fine print the
headline dropped, so it can sit in an item's body sentence rather than
needing its own paragraph. Keep it that compressed when the piece has already
spent its space on the primary finding.

Where an item does earn a last line, the record should have supplied it
already, the way Hutson's close rests on Ivanova's own words rather than a
sentence added to sound conclusive. Don't build that closing move into every
item; a brief whose items all end the same way reads as stamped no matter how
sharp any one of them is on its own, and several of tonight's items may
simply stop once the caveat is stated.

## Simon Willison, "SWE-bench February 2026 leaderboard update"

Source: https://simonwillison.net/2026/Feb/19/swe-bench/

> "SWE-bench is one of the benchmarks that the labs love to list in their
> model releases. The official leaderboard is infrequently updated but they
> just did a full run of it against the current generation of models, which
> is notable because it's always good to see benchmark results like this
> that weren't self-reported by the labs."

This item reports who ran the test before it reports a score. By the time a
number arrives, the reader already knows how much weight to give it. The
ordering is doing the sentence's whole argument.

> "OpenAI's GPT-5.2 is their highest performing model at position 6, but
> it's worth noting that their best coding model, GPT-5.3-Codex, is not
> represented - maybe because it's not yet available in the OpenAI API."

The absence is reported as plainly as the presence would have been. "Maybe
because" keeps the explanation a guess instead of dressing it up as
something the leaderboard confirmed. Two clauses, one fact and one hedge,
clearly marked apart.

> "This benchmark uses the same system prompt for every model, which is
> important for a fair comparison but does mean that the quality of the
> different harnesses or optimized prompts is not being measured here."

One sentence does the whole methodological job: what the constant controlled
for, and what it therefore left uncontrolled. The second half is the
sentence's entire reason for existing, and it earns its place by naming
something specific the number in front of it cannot tell you.

## Matthew Hutson, "The Turing Test is defunct. We need a new IQ test for AI"

Source: https://spectrum.ieee.org/agi-benchmark

> "While benchmarking any intellectual ability is tough, doing so for AGI
> presents special challenges. That's in part because people strongly
> disagree on its definition: Some define AGI by its performance on
> benchmarks, others by its internal workings, its economic impact, or
> vibes. So the first step toward measuring the intelligence of AI is
> agreeing on the general concept."

The piece states the disagreement before it takes a side in it, and lists
the competing definitions concretely enough that a reader can place any claim
they've already seen against one of them. "Vibes" sitting in that list, next
to internal workings and economic impact, is the one plainly informal word
in the paragraph, and it's accurate rather than decorative.

> "AI experts acknowledge ARC's value, and also its flaws. Jiaxuan You, a
> computer scientist at the University of Illinois at Urbana-Champaign, says
> ARC is 'a very good theoretical benchmark' that can shed light on how
> algorithms function, but 'it's not taking into account the real-world
> complexity of AI applications, such as social reasoning tasks.'"

Both the credit and the limitation come from the same named person in the
same breath, so neither reads as the writer's own opinion smuggled into a
source's mouth. Naming the institution alongside the name is what lets the
reader judge the credential rather than take it on faith.

> "We may never agree on what AGI or 'humanlike' AI means, or what suffices
> to prove it. [...] Ivanova, the psychologist at Georgia Tech, was on a
> panel recently, and the moderator asked about AGI timelines. 'We had one
> person saying that it might never happen,' Ivanova told me, 'and one
> person saying that it already happened.' So the term 'AGI' may be
> convenient shorthand to express an aim—or a fear—but its practical use may
> be limited. In most cases, it should come with an asterisk, and a
> benchmark."

The close adds one more data point, an expert disagreement witnessed
firsthand, and lets the final clause follow from everything the piece
already built. The last five words land because "a benchmark" is the piece's
own subject, not a moral tacked on to close it.

## Nathan Lambert, "Open models in perpetual catch-up"

Source: https://www.interconnects.ai/p/open-models-in-perpetual-catch-up

> "The benchmark mixes a ton of factors into 1 score that judges model
> 'quality.' This compresses far too many error bars, stories, and
> weaknesses into one metric. These metrics will always be used to inform
> policy and help more people understand the high-level trends of AI, but
> they do a poor job of capturing the frontier of AI progress."

The criticism names exactly what an aggregate score loses (error bars,
individual weak spots) and what it's still good for (informing policy, a
high-level read on trends). Both halves come with a reason attached, not
just a verdict.

> "Well known issues like SWE-Bench being almost 3/4 Django or Terminal
> Bench 2 being crowdsourced and a bit noisy will never be captured here."

A methodological complaint compressed into a single subordinate clause per
benchmark, named specifically enough (the repository, the crowdsourcing)
that a reader who knows the benchmark can check it. No paragraph is spent
building up to it.

> "All together, I'd bet that the current Artificial Analysis Intelligence
> Index is a bit unrepresentative of the true frontier, rather than open
> models being closer to the closed models than ever before (yes, I know,
> it's not like I am offering any obvious ways to improve it)."

The verdict is framed as a bet, and the parenthetical concedes the limit of
the writer's own position in the same sentence that states it: no obvious
fix for the index exists yet, and the writer says so directly instead of
leaving the reader to notice the gap.
