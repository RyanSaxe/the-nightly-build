# Voice guide — tech-news/2026-07-31

Register: a wire-service brief for a reader who already saw the headline and
has a CS/ML background. Calm, factual, unhedged. The relationship is expert
to expert: state the finding and the number, not the tour of how you found it.

Moves that change sentences in this item set:

- **Put the verified number ahead of the vendor's word for it.** State what an
  independent source measured or confirmed in the sentence that carries the
  news; the company's own framing, if it appears at all, comes second and is
  attributed, never adopted as narration. This is how you keep "capability
  claim" and "independent check" from blurring into one voice.
- **Attach the caveat to the number it qualifies, in the same sentence or the
  next one, and stop.** A caveat is a fact (which benchmark, which condition,
  what it cost), not a paragraph of hedging. Adding it should shorten the
  item's confidence, not its length.
- **Name the exact model, version, or figure and reuse that exact name.**
  "The new model" or "the system" is a tell that the writer is padding around
  a number they haven't pinned down.
- **Open each item differently.** One item can open on the actor and verb,
  another on the number, another on the document. If two items in the set
  start with the same grammatical shape ("X announced," "X released"), rewrite
  one.
- **Let a flat declarative carry the skepticism.** Skepticism is a second,
  contradicting number placed next to the first, not an adjective. Never
  characterize a result as impressive, notable, or concerning; show the figure
  that makes it so.
- **End on the last fact that matters, not a reflection.** No sentence that
  steps back to tell the reader what to make of the item.

Recently used, do not reuse: hype adjectives; "why it matters" as a labeled or
implied scaffold; a closing line that hands the point back to the reader;
hedged-contrast deks ("X is not Y; it is Z" and its cousins); manufactured
punchlines ("that's the whole point," "the catch is"); roundup scaffolding
("in other news," a template shape stamped across items); and repeating the
same item-opening grammar twice in one brief.

## Simon Willison, on OpenAI's GPT-5.6 launch
Source: https://simonwillison.net/2026/Jul/9/gpt-5-6/
Craft:
- cadence: short declarative sentences with the number built into the
  sentence itself, not appended after a colon
- argument: states the vendor's own benchmark number, then immediately places
  a second, contradicting number from a different benchmark beside it, no
  connecting commentary needed
- evidence: exact percentages and a computed ratio ("roughly one-quarter the
  estimated cost") rather than a qualitative comparison
- stance: skeptical without a single evaluative adjective; the contradiction
  between two cited numbers does the arguing
- notice: catches which specific benchmark reverses the vendor's headline
  claim (SWE-bench Pro flips what Agents' Last Exam showed), rather than
  reciting the full scorecard
- diction: exact model names kept exact across sentences (Sol, Fable 5), never
  swapped for "the new model" or "its rival"
- reader: assumes fluency with named benchmarks, no definitional aside
- the move the axes miss: he never resolves the two competing numbers into a
  verdict. The tension between them is left standing as the finding, which is
  more honest than picking a winner the evidence doesn't yet support
Calibration: "On Agents' Last Exam, GPT-5.6 Sol sets a new high of 53.6,
eclipsing Claude Fable 5 (adaptive reasoning) by 13.1 points. Even at medium
reasoning, it beats Fable 5 by 11.4 points at roughly one-quarter the
estimated cost."

## Jack Clark, "Import AI 453: Breaking AI agents; MirrorCode"
Source: https://jack-clark.net/2026/04/13/import-ai-453-breaking-ai-agents-mirrorcode-and-ten-views-on-gradual-disempowerment/
Craft:
- cadence: opens on the flat capability claim, then compresses to one worked
  example instead of surveying the whole benchmark
- argument: anchors an abstract claim ("AI can reverse engineer complex
  software") in a single named case with a concrete scale, so the reader
  checks the claim against a fact rather than a category
- evidence: converts the abstract into a comparison the reader can hold
  (thousands of lines of Go, a named toolkit, an estimated human-hours range)
- stance: matter-of-fact about an extraordinary result; the plainness of the
  diction is what keeps it from reading as hype
- notice: picks the single most legible example from a large benchmark rather
  than listing scores
- diction: precise nouns (bioinformatics toolkit, 40+ commands) stand in for
  "complex software"
- reader: research-literate; no gloss on what the evaluating organizations are
- the move the axes miss: he flags his own estimate as an estimate inside the
  same sentence as the number ("We guess this... would take a human engineer
  2-17 weeks"), so the uncertainty travels with the figure instead of getting
  smoothed into false precision
Calibration: "Claude Opus 4.6 successfully reimplemented gotree - a
bioinformatics toolkit with ~16,000 lines of Go and 40+ commands. We guess
this same task would take a human engineer without AI assistance 2-17 weeks."

## Lucas Ropek, "Google's new Gemini Pro model has record benchmark scores, again" (TechCrunch)
Source: https://techcrunch.com/2026/02/19/googles-new-gemini-pro-model-has-record-benchmark-scores-again/
Craft:
- cadence: first sentence is actor, verb, day, done; the second sentence adds
  the one status detail (preview versus general availability) that changes
  what the news means
- argument: the news fact leads; the company's characterization of its own
  capability arrives only after, and only as an attributed quote
- evidence: every superlative is sourced to a name ("the company said,"
  "according to Brendan Foody, CEO of Mercor") rather than stated as narration
- stance: neutral scribe voice; when skepticism appears at all it comes from a
  second attributed source, not the writer's adjective
- notice: keeps "generally released" and "available as a preview" distinct,
  a status caveat easy to blur into one word
- diction: the exact version number (3.1) and the exact day anchor the
  sentence in time instead of "recently"
- reader: general tech audience, but the lede-first mechanics transfer
  directly to a brief item
- the move the axes miss: the piece's own weak point instructs by contrast.
  It repeats the vendor's benchmark framing on the strength of one quoted
  executive rather than its own independent check, which is exactly the gap
  this brief's per-item primary-plus-independent-secondary rule exists to
  close
Calibration: "On Thursday, Google released the newest version of Gemini Pro,
its powerful LLM. The model, 3.1, is currently available as a preview and
will be generally released soon, the company said."
