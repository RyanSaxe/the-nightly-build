# Voice guide: tech-news/2026-08-12 (01)

## How this piece should sound

This is a brief, not a survey: six items at most, each a judgment about what
moved today, for a reader who has a machine-learning career and does not need
the field explained. The three passages below all show writers making that
same judgment call in public, on results and benchmarks, without either
inflating them or hedging them into mush.

Willison's SWE-bench item earns its place here because the whole item hangs
on one distinction: this run "weren't self-reported by the labs." When an
item's figure comes from an independent leaderboard or a third-party
evaluation rather than a lab's own release notes, say so in the sentence that
gives the number, not as a caveat bolted on afterward. And take his other
move too: when a comparison is missing an obvious entry (GPT-5.3-Codex, off
the SWE-bench table), naming the gap and the likely reason is worth a clause.
An item that only reports the top score and skips what the table conspicuously
lacks has left out half the finding.

Clark's caveats paragraph in Import AI 453 is the clearest model for the
skepticism this brief owes a lab's self-report: state plainly what a
benchmark does and doesn't show, in the same breath as reporting the result,
without inventing a misreading to knock down. His numbered cross-references
to earlier issues are also worth the item's structure: this brief tracks
threads across nights the same way, and where a story is a sequel, naming
exactly what today added is more useful to this reader than re-explaining the
thread.

Zvi's insistence on naming the comparison point, not just the win, is the
sharpest instinct to carry over: a lab claiming to beat a named competitor is
making a comparison claim, and the competitor and its number belong in the
sentence, stated plainly, the way "96% vs. 100%" does more work than "close
behind." Where a self-reported number and an independently measured one both
exist for the same claim tonight, that gap is itself the sentence worth
writing, not a footnote to it.

None of the three writers below work in anything like this brief's compressed
form; the compression is the template's job, not theirs. What carries over is
the discipline: a figure is not evidence until the reader knows whose figure
it is, and a comparison is not neutral until both numbers are on the page.

## Simon Willison, "SWE-bench February 2026 leaderboard update"

Source: https://simonwillison.net/2026/Feb/19/swe-bench/

> "SWE-bench is one of the benchmarks that the labs love to list in their model releases. The official leaderboard is infrequently updated but they just did a full run of it against the current generation of models, which is notable because it's always good to see benchmark results like this that weren't self-reported by the labs."

The second sentence does the real work: it doesn't just report a new leaderboard run, it says why this particular run is worth a reader's attention, and the reason is a provenance fact (self-reported versus not) rather than a score. The judgment is stated once, plainly, and the piece moves on rather than circling back to remind the reader of it.

> "OpenAI's GPT-5.2 is their highest performing model at position 6, but it's worth noting that their best coding model, GPT-5.3-Codex, is not represented - maybe because it's not yet available in the OpenAI API."

Willison reports a ranking and then immediately reports what the ranking is missing, with a stated (and hedged with "maybe") reason for the gap. He doesn't let a top-line number stand as the whole finding; the absence gets named as specifically as the presence does.

> "This benchmark uses the same system prompt for every model, which is important for a fair comparison but does mean that the quality of the different harnesses or optimized prompts is not being measured here."

This is a scope statement, not a disclaimer: it says exactly what the shared methodology buys (fairness across models) and exactly what it costs (harness quality goes unmeasured), in one sentence, using the benchmark's own mechanics rather than a generic hedge that could follow any result.

## Jack Clark, "Import AI 453: Breaking AI agents; MirrorCode; and ten views on gradual disempowerment"

Source: https://jack-clark.net/2026/04/13/import-ai-453-breaking-ai-agents-mirrorcode-and-ten-views-on-gradual-disempowerment/

> "Caveats: Now, this benchmark isn't quite like normal coding tests. It's better to think of it as a proofpoint for AI systems being able to generate systems which imitate the function of other systems when they get a lot of help: AI systems tested out here are asked to clone programs which produce a canonical output (and therefore can naturally generate a specification), there may be some cases of memorization on the basic programs, and this only covers a slice of the large universe of potential software projects."

Clark states three separate limitations of the same benchmark in one paragraph, each one specific to how the test is built (canonical output, possible memorization, narrow coverage) rather than a single generic "results may vary." The reader learns exactly what kind of overclaim to guard against, not just that one is possible.

> "The results: Today's AI models are extremely capable at some of these tasks: "Claude Opus 4.6 successfully reimplemented gotree — a bioinformatics toolkit with ~16,000 lines of Go and 40+ commands. We guess this same task would take a human engineer without AI assistance 2–17 weeks. We see continued gains from inference scaling on larger projects, suggesting they may be solvable given enough tokens.""

The load-bearing figures here (the line count, the week estimate) are the researchers' own words, quoted rather than paraphrased into Clark's voice, with the estimate's own hedge ("we guess") left intact. The attribution is doing double duty: it credits the source and it preserves how confident that source actually was.

> "Why this matters – most people keep underestimating AI progress: Ryan's timeline update follows a similar one from Ajeya Cotra, who in March (#448) substantially updated her own timeline estimates, based in part on time-horizon modeling, and also Eli Lifland and Daniel Kokotajlo of AI 2027 (#408) who in April said they had recently "updated our timelines earlier by ~1.5 years" mostly due to "faster time horizon growth" and "coding agents"."

Clark ties a new claim to two named prior claims by two named people, with issue numbers standing in for full citations, so a returning reader can trace the thread without Clark re-explaining it and a new reader still gets both names and both numbers.

## Zvi Mowshowitz, "Kimi K2.5"

Source: https://thezvi.substack.com/p/kimi-k25

> "As usual, benchmarks are highly useful, but easy to overinterpret. Kimi K2.5 gets to top some benchmarks: HLE-Full with tools (50%), [...] and InfoVQA (93%). It is not too far behind on AIME 2025 (96% vs. 100%), SWE-Bench (77% vs. 81%) and GPQA-Diamond (88% vs. 92%)."

Every claim of closeness is backed by both numbers side by side, not a qualitative word like "close" or "comparable." The reader can check "96% vs. 100%" against their own sense of what a four-point gap means; they cannot check "nearly matches."

> "I always note who is the comparison point. Remember those old car ads, where they'd say 'twice the mileage of a Civic and a smoother ride than the Taurus' and then if you were paying attention you'd think 'oh, so the Civic and Taurus are good cars.'"

Zvi names the move he's making (tracking the comparison target, not just the win) before he makes it, and the car-ad example shows exactly how a stated comparison can smuggle in an unstated concession. The technique generalizes past cars: any claim of the form "beats X" is also a claim about X, and both halves are worth a sentence.

> "The main practical advantage of open weights is that it can make the models cheaper and faster. If you try to run them locally, they are instead a lot more expensive and slow, if you count the cost of the hardware, and also much more fiddly."

A stated advantage is immediately followed by its stated cost, in the same register, with no signal that one is the "real" point and the other a hedge. Both sentences carry equal weight, which is what makes the second one land as analysis rather than throat-clearing.
