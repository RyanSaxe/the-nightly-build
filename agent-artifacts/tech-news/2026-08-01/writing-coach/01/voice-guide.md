# Voice guide — tech-news/2026-08-01

The reader already saw the release. Do not re-describe what shipped; report
what it changes and what the announcement left out. Assume they can parse a
parameter count or a benchmark name unglossed. Your sentence earns its place
only if it adds a number, a caveat, or a comparison the release itself omitted
or buried. If a sentence would still be true with the model's name swapped
in for a competitor's, cut it.

Open each item on the concrete fact, not the occasion. Skip the scene-setting
clause ("In a move that...", "As the AI race heats up..."). State what
happened and what it measures in the same breath: put the number inside the
sentence that makes the claim, not in a trailing dependent clause. A caveat
reads strongest as a flat declarative next to the claim it limits, not
softened into "it should be noted that" or "however, some caution is
warranted."

Headline on the fresh verb that names the actual shift, with the actor doing
it. No colon, ever — a right half that would only add "here's what it
means" is proof the left half didn't earn its length. Never a paired-adjective
triad standing in for a real claim.

The judgment sentence should name who it changes something for — a specific
kind of user, buyer, or competitor, not "the industry" or "watchers." State
the implication as a plain clause and stop. Do not qualify it into mush with
stacked hedges, and do not manufacture a punchline that announces its own
importance. When two items in the same file share a shape (same sentence
count, same news-then-verdict rhythm, same kind of opening clause), rewrite
one so the piece doesn't read as a template applied six times.

Recently used, do not reuse: colon-subtitle headlines; a "faster, cheaper,
smarter" (or any paired-adjective) triad standing in for the actual claim;
closing an item on a line that hands the point back to the reader instead of
stating what it changes; running every item through the same shape.

## Simon Willison, "Kimi K3, and what we can still learn from the pelican benchmark"
Source: https://simonwillison.net/2026/Jul/16/kimi-k3/
Craft:
- cadence: short declarative openers carry the news; a longer sentence is
  reserved for the one idea that needs its subordinate clauses to hold together.
- argument: uses one small, reproducible test case (a fixed prompt, a fixed
  cost) as the entire evidentiary base for a claim about what benchmarks can
  no longer tell you.
- evidence: exact token counts and exact dollar costs stand in for
  adjectives; no figure appears without the unit that makes it comparable.
- stance: skeptical of the very tool being used, in the same paragraph that
  uses it — the skepticism is not a disclaimer bolted onto the intro.
- notice: catches a hidden fact through the reported number itself (a token
  count too high for the visible prompt implies an undisclosed system
  prompt) rather than asserting it from outside knowledge.
- diction: plain verbs, no adjective doing the work a number could do.
- reader: assumes the reader already knows what the benchmark is and does not
  re-explain it; explains only how its meaning has drifted.
- the caveat is delivered as a flat imperative sentence, not a hedge: it
  reads as an instruction to the reader's future self, not a qualifier on
  the writer's claim.
Calibration: "So don't go using pelicans to compare models!"

## Nathan Lambert, "GLM-5.2 is the step change for open agents"
Source: https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open
Craft:
- cadence: builds the release's context (timing, naming pattern, who
  publishes on a weekend and why) before stating the technical claim, so the
  claim lands already positioned against precedent.
- argument: treats an anomaly in how a release was handled (an unscheduled
  Saturday drop) as itself evidence worth reporting, on par with a spec.
- evidence: places the new model against the two or three models it actually
  competes with by name, not against an abstract prior state of the art.
- stance: withholds the verdict until independent replication exists;
  reports lab claims as claims, not as settled fact, without saying so
  explicitly — the distinction is structural, not announced.
- notice: reads release mechanics (a weekend ship date, a tier-gated rollout)
  as signal about how the lab itself rates the release.
- diction: blunt short sentences for judgment, longer ones only for
  chronology.
- reader: assumes fluency with the competitive field; no model is
  introduced with a definition, only with its place in the lineup.
- the move the axes miss: a caveat about the evidence itself ("benchmarks
  are half dead") is stated once, plainly, and then the piece keeps working
  with the benchmarks anyway — it doesn't stop the analysis, it recalibrates
  how much weight the analysis puts on any single number.
Calibration: "Benchmarks are half dead these days."

## The Batch (DeepLearning.AI), "Kimi K3 Reveals How A Giant Frontier AI Model Works"
Source: https://www.deeplearning.ai/the-batch/issue-363
Craft:
- cadence: one graf reports, one graf judges; each sentence in the judgment
  graf adds a distinct consequence rather than restating the last one in new
  words.
- argument: the claim is comparative and ranked ("finished just behind X and
  Y"), never freestanding praise.
- evidence: a benchmark gap is expressed as a point difference against a
  named competitor, and a cost gap as a ratio, so both numbers carry a
  built-in comparison.
- stance: no adjective of enthusiasm anywhere; the significance is carried
  entirely by what the numbers force a specific buyer to reconsider.
- notice: identifies which lever moved (price, policy control, or raw
  score) for each sentence, rather than treating "better" as one
  undifferentiated claim.
- diction: verbs that name a market action ("whittles away," "pressures"),
  not verbs that describe a spec ("features," "offers").
- reader: a developer deciding which model to call, addressed through their
  decision, never addressed directly.
- the move the axes miss: the judgment graf names a specific decision-maker
  (a developer picking a model) instead of an abstract "industry," which is
  what keeps the significance from floating free of anyone who has to act
  on it.
Calibration: "Kimi K3 whittles away at every reason why a developer choosing
a model might default to the top proprietary model."
