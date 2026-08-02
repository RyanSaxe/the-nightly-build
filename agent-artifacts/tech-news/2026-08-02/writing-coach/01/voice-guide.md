# Voice guide: tech-news/2026-08-02 (01)

## Directive

Register: a colleague briefing a colleague who already read the headline.
Nobody here needs the field defined; they need the one fact and the one
mechanism that changes what they'd do next. Write to be forwarded, not
explained to.

Three moves change sentences in this item set:

1. **Open on the claim, close on the consequence chain.** The item heading
   states what happened, in the technology's own actor and verb. The item's
   last sentence chains mechanism to practice in one unhedged clause:
   this changed, therefore that is now possible or false. No adjective does
   the arguing; the chain does.
2. **Sequence the number before the interpretation.** State the reported
   figure or spec first, then the one comparison that makes it legible to
   someone who already tracks this field (a prior benchmark score, a known
   model's price, last quarter's number), then draw the conclusion. Don't
   assert significance and back it with a number after the fact; let the
   number carry the weight it earns.
3. **Flag inference, don't hedge it.** When an item's reasoning reaches past
   what the primary source states, name the source it's extending from in a
   short subordinate clause, not a hedge word. "If the advisory's timeline
   holds" tells the reader what kind of claim they're getting. "Reportedly"
   or "may" tells them nothing and reads as slop.

Never label the reasoning "why it matters." Fold it into the item's own
sentences. A labeled subhead on a five-item brief is scaffolding the house
standard already rules out, and it does the reader's inference for them
instead of earning it.

## Licenses

```text
form: the compressed causal chain
move: Import AI closes an item by chaining what changed to what someone can
      now do or no longer assume, one clause per link, present tense,
      no summarizing adjective at the end.
bar:  every link traces to a cited fact in the item, and the final clause
      names a concrete capability, decision, or risk a practitioner gains
      or loses — never a restated magnitude of importance ("this is
      significant," "this matters a lot").
```

```text
form: number-first sequencing
move: Simon Willison states the reported spec or score before he
      interprets it, then supplies exactly one comparison the reader
      already holds, then draws the single conclusion that comparison
      supports.
bar:  the comparison must reference a quantity the declared reader
      plausibly already knows (a named prior model, a standard benchmark,
      a public price) — never an invented scale or a vague "far more than
      before."
```

```text
form: the sourced inference flag
move: Zvi Mowshowitz keeps a claim that outruns its primary source
      honest by naming what it's inferred from ("if the reversed binary
      is representative," "per the filing's account") instead of
      softening it with a hedge adverb.
bar:  used at most once per item, only when the item's own reasoning
      truly extends past the cited primary source, and the clause must
      name the source type, not just lower the confidence.
```

## Recently used, do not reuse

- Do not re-lead on "a model found a cryptographic weakness" (HAWK/NIST
  post-quantum candidates, three straight editions) or on an AI-agent CVE,
  unless 08-02 brings a genuinely new such event. If either story
  continued, lead on what advanced, not the pattern itself.
- Cut the three dek/heading molds this library has stamped: the semicolon
  reversal ("X did A; Y refuses B"), the suspended question ("...and the
  real question is whether"), and the comma triad closed with "and."
- Cut the two-clause-joined-by-comma-and-"and" heading shape generally
  ("The scale, and what it is compounding against") even outside the dek —
  it reads stamped by the second use.

## Jack Clark, "Import AI 455: Automating AI Research"
Source: https://jack-clark.net/2026/05/04/import-ai-455-automating-ai-research/
Craft:
- cadence: Each item runs a short setup, a chronological run of hard
  numbers (Claude 2's 2% on SWE-Bench to Claude Mythos Preview's 93.9%;
  METR time horizons from 30 seconds in 2022 to ~12 hours in 2026), then
  one or two sentences of consequence. The numbers do the pacing; commentary
  is kept short around them.
- argument: Never asserts importance directly. Establishes a benchmark as a
  proxy for a real activity (coding, research labor), then shows the proxy
  moving, then states what kind of work now falls inside a model's
  competence.
- evidence: Leans on named, checkable benchmarks (SWE-Bench, METR,
  PostTrainBench) with dated data points, not on aggregated "reports show."
- stance: Confident but bounded — states a human baseline explicitly
  ("instruct-tuned versions... developed by talented human AI researchers")
  before saying how close the machine got, so the claim of progress carries
  its own ceiling.
- notice: Chooses the boring-sounding proxy (fine-tuning uplift, issue
  resolution rate) over the dramatic anecdote, on the theory that the proxy
  is what a practitioner can actually act on.
- diction: Concrete measurement over adjective. "~93.9%, effectively
  saturating the benchmark" instead of "remarkable progress."
- reader: Assumes the reader already knows what SWE-Bench and METR
  measure in outline; spends its words on the new data point and what it
  now implies, not on redefining the benchmark.
- the move the axes miss: the closing sentence is always a chain, not a
  verdict — "AI systems have gotten good enough to automate a major
  component of AI R&D, speeding up all the humans that work on it" links
  capability directly to a changed workflow, never to a bare "this matters."

## Simon Willison, "Kimi K3, and what we can still learn from the pelican benchmark"
Source: https://simonwillison.net/2026/Jul/16/kimi-k3/
Craft:
- cadence: Opens with the announcement stated flatly, moves immediately
  into self-reported figures with a qualifier that keeps them honest
  ("mostly beating... while losing out to"), then alternates a long
  explanatory sentence with a short declarative to reset pace ("So don't go
  using pelicans to compare models!").
- argument: Builds significance by accumulation and comparison rather than
  claim. Says what a benchmark isn't good for before saying what it is
  good for, so the eventual claim survives its own qualification.
- evidence: Runs its own test and reports the exact cost and token count
  ("95 input tokens and 16,658 output tokens... for a total cost of 25
  cents"), preferring a number he generated himself to one he's quoting.
- stance: Comfortable being unimpressed. Willing to say a widely-cited
  benchmark is mediocre while still explaining precisely what it's useful
  for.
- notice: Notices the gap between a lab's self-reported benchmark and what
  a reader can actually verify, and treats that gap as the story.
- diction: Numbers as anchors — price per million tokens, parameter counts,
  token counts — stated plainly, with the interpretation arriving only
  after the figure is on the page.
- reader: Writes for someone who will go run the same test; the piece
  hands over exactly enough method to reproduce the number, not a
  black-boxed conclusion.
- the move the axes miss: sequencing. The number always lands before the
  interpretation, never after, so the reader can disagree with the
  conclusion without having to first dig out the fact it rests on.

## Zvi Mowshowitz, "AI #177 Part 1: Tip of the Iceberg"
Source: https://thezvi.substack.com/p/ai-177-part-1-tip-of-the-iceberg
Craft:
- cadence: Item opens on a declarative headline treating the event as
  settled fact, then works through the sourcing (a reverse-engineered
  binary, a legal filing) before advancing any interpretation.
- argument: Keeps two ledgers visible in the same paragraph — what the
  source says happened, and what he thinks it means — and marks the
  boundary explicitly rather than letting them blur.
- evidence: Cites the specific technical origin of a claim (a reversed
  binary, a kill-switch's current deployment status) rather than a
  secondhand summary of it.
- stance: Names his own confidence in a short aside — "this looks really
  bad if the claims are true, although [X] is still overstating it" —
  crediting the source while discounting the spin around it in the same
  breath.
- notice: Tracks a story to its unresolved edge and says so instead of
  manufacturing a close; ends items mid-consequence when the consequence is
  in fact still unfolding.
- diction: Plain verbs carrying legal and technical weight without
  decoration — "uploaded," "disabled it with a remote kill-switch" — no
  synonym reached for variety.
- reader: Assumes the reader already followed the prior week's version of
  the story and wants only what's new and what it changes about the
  standing account.
- the move the axes miss: the confidence flag is load-bearing, not
  decorative — it's the sentence that keeps a strong claim from becoming an
  unsupported one, placed right where the claim would otherwise outrun its
  source.
