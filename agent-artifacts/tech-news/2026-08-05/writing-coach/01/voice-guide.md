# Voice guide: tech-news/2026-08-05

Register: a colleague briefing a colleague who already read the headline
elsewhere. No throat-clearing, no vendor's adjectives repeated as your own.
The reader relationship is peer, not student: name the eval, the n, and the
hardware or dataset it ran on, then move. Do not re-explain what a benchmark
is; explain what this run of it shows.

The moves below change specific sentences in this brief:

- When a number carries a published margin of error, an interval, or a
  confidence range, put it next to the headline figure, not in a trailing
  caveat clause. A clean point estimate that hides a wide interval is the
  vendor's framing, not yours.
- When a benchmark score is a delta from a prior run (this model vs. the last
  one, this chip vs. its predecessor), convert the delta into a ratio or
  multiple stated in the source's own units before moving on. A raw score
  jump means less to this reader than what it is a multiple of.
- When you are inferring a reason for a result rather than reporting a
  measured one, mark the sentence as inference with a plain verb (suspect,
  likely, appears to) and keep it grammatically identical to the sentences
  around it. Do not wall it off with a hedge clause or a qualifier stack.
- State the vendor's claim in its own terms first, once, then give the
  independent result immediately after with no transition sentence between
  them. The juxtaposition does the arguing; a sentence like "however, testing
  shows" is doing work the juxtaposition already did.

## Licenses

```text
form: interval-anchored figure
move: pairing a headline benchmark number with the uncertainty band the
      source itself published, placed at first mention rather than deferred
bar:  the interval must come from the primary source's own reporting; an
      invented or estimated margin is not licensed
```

```text
form: magnitude conversion
move: restating a score delta as a multiple or ratio in the benchmark's own
      unit (time, tokens, requests) so the reader holds a comparison instead
      of two raw numbers
bar:  the multiple must be derivable from the source's published numbers with
      no invented denominator; if the units don't support a clean ratio, cut
      the device and give the two numbers plain
```

```text
form: marked inference
move: a single plain hedge verb (suspect, likely, appears to) flagging a
      sentence as the writer's read of the data rather than a reported
      measurement, kept in the same declarative register as the rest of the
      item
bar:  one hedge verb per inference, never stacked with a second qualifier;
      reserved for reading unstated causes out of published data, never for
      speculating about a vendor's motive or intent
```

## Recently used, do not reuse

No triad-of-adjectives headline. No colon subtitle. No scaffolding subhead
("Background," "Implications," "What's Next"). No closing line that hands
the point back to the reader.

## Simon Willison, "Claude Sonnet 4.5 is probably the best coding model in the world (at least for now)"
Source: https://simonwillison.net/2025/Sep/29/claude-sonnet-4-5/
Craft:
- cadence: dense technical exposition ("Added `parent_response_id` column")
  sits next to plain commentary; the shift in pace marks the shift from spec
  to opinion.
- argument: states the vendor's superlative in the vendor's own words, then
  reports his own tested result immediately after it, with no editorial
  bridge between the two.
- evidence: grounds claims in something he ran himself: "All 466 tests
  passed in 167.69 seconds." A number he produced outranks a number he was
  handed.
- stance: commits to a verdict ("probably the best") while dating its own
  shelf life ("at least for now," a rival's release already rumored). The
  qualifier is a fact about the market, not a hedge about his confidence.
- notice: catches the gap between a benchmark's presentation and its
  substance, e.g. flagging that a demo is "whimsical" evidence of capability
  rather than proof of superiority.
- diction: plain and concrete on specs (price per million tokens, seconds,
  pass counts); looser and evaluative once the numbers are on the table.
- reader: peer-to-peer, assumes the reader could reproduce the test.
- the move the axes miss: he treats "I ran this myself" and "the vendor
  says" as different categories of sentence and never lets the second stand
  in for the first, even when they agree.

## Timothy B. Lee, "Why it's getting harder to measure AI performance"
Source: https://www.understandingai.org/p/why-its-getting-harder-to-measure
Craft:
- cadence: short declarative sentences break up longer analytical runs at
  exactly the point a claim needs to land cleanly ("METR's benchmark is
  close to saturating.").
- argument: builds in stages, from the benchmark's apparent success to the
  specific place it degrades to what that degradation implies, rather than
  stating the conclusion up front.
- evidence: names the methodology before the number, e.g. that task
  difficulty was set by hiring programmers and timing their actual
  completions, not estimated.
- stance: skeptical of the clean story without dismissing the underlying
  work; he credits METR's rigor and still reports where its own numbers stop
  being usable.
- notice: goes straight to the confidence interval sitting under a headline
  score and treats a 5-to-66-hour range as the real finding, not an asterisk
  on the point estimate.
- diction: technical terms (bracket, saturating) placed in context that
  defines them by use rather than by definition sentence.
- reader: addressed as a co-investigator ("so we know X, but it's hard to
  say how much"), not lectured.
- the move the axes miss: he converts an opaque score gap into a stated
  multiple ("5,400 times 'harder'") so the reader holds one comparison
  instead of two raw numbers, and only does it when the units support a real
  ratio.

## Chester Lam, "Analyzing Nvidia GB10's GPU"
Source: https://chipsandcheese.com/p/analyzing-nvidia-gb10s-gpu
Craft:
- cadence: complex clauses stating measurement conditions alternate with
  short, flat assertions of a spec number.
- argument: builds a picture of the chip from independently run
  microbenchmarks, cross-checking one test's result against another's before
  drawing a conclusion.
- evidence: names the exact test and its limits before trusting its output,
  distinguishing what a Vulkan-based benchmark shows from what a narrower
  OpenCL kernel can and cannot show.
- stance: withholds judgment until the measurement supports it; a claim
  about which chip "wins" waits for the qualifying clause that says by how
  much and under what load.
- notice: catches where a measurement goes silent, e.g. a cache invisible in
  a latency plot because it's smaller than the level below it, and reports
  the absence as a finding.
- diction: exact units always (KB, MHz, GB/s), never a rounded-off
  adjective in their place.
- reader: assumed to know what L1 latency implies without being told why it
  matters, but still walked through what a specific term (shared memory)
  means the first time the piece needs it.
- the move the axes miss: he marks his own inferences with a plain verb
  ("I suspect," "likely") inside otherwise flat declarative sentences,
  keeping the guess grammatically indistinguishable from the fact around it
  except for that one word, so the hedge costs no rhythm.

## Self-test

The house standard already demands sourced claims, a number with a
comparison, and separation of reported fact from vendor claim. Left there, a
writer would still default to printing the clean headline number and
tucking any uncertainty into a subordinate clause at the end, because that
reads more confident and a brief has no room for a caveat paragraph. What
this guide adds beyond the default: put the uncertainty where the number is,
not after it, and convert a delta into a ratio in the source's own units
before treating it as news. That is a placement and unit-conversion
discipline the default doesn't specify, and it is the difference between an
item that reports a benchmark and one that reprints a vendor's chart.
