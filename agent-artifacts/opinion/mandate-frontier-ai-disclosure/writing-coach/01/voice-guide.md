# Voice guide: opinion/mandate-frontier-ai-disclosure

## Directive

House register holds: calm, precise, argued from first principles, to a
reader who already knows what a compute threshold and a systemic-risk
evaluation are. One discipline sits on top of it for this piece.

Build the case for a disclosure floor so it survives full charity toward the
labs it binds. Do not argue from distrust: not "labs will cut corners
without a mandate," not "self-reported safety frameworks can't be trusted."
Argue from what a floor does even when every named developer is acting in
good faith — it fixes an information asymmetry regulators, competitors, and
downstream users all face regardless of anyone's intentions, and it survives
contact with a lab's best account of its own conduct. A sentence that only
works if the reader suspects a lab is lying is doing the wrong kind of work.
Rebuild it on the coordination or asymmetry problem underneath, or cut it.

The counter-section is where this pays off. The strongest opposing case
(entrenchment, a moving-target technology, extraterritorial flight) is not
answered by doubting its sincerity. It is answered by showing the floor
holds even when the objection is granted in full. Concede fast and
specifically, then hold the line on a different ground than the one just
given away.

Three moves earn this discipline on the sentence level; each is licensed
below with a bar an editor can hold a single sentence to.

## Licenses

form: the concrete-incident open
move: Rozenshtein does not open his export-control piece on the legal
question. He opens on a timestamp: a specific Friday, a specific hour, a
letter from the Commerce Department, a named model pulled globally within
hours. The abstraction — what authority the government actually has over
model weights — arrives only after one dated, sourced action has given it
something to be about.
bar: The opening fact must be a specific, cited, dated action or filing,
not a compressed preview of the piece's thesis dressed as a scene. Test it
by deleting the date and the proper noun: if the paragraph argues exactly
the same afterward, the incident isn't doing anything and the piece should
open on the claim directly instead.

form: the compressed concession
move: Arguing that procedural design, not just substantive coverage,
decides whether an AI statute bites, Arnold and Musser meet the objection
that regulators already have what they need with one flat sentence: the
skeptics have a point. Nothing hedges it and nothing rebuts it in the same
breath. The next sentence draws where the point stops reaching — resource
shortfalls don't explain why procedurally armed regulators still miss.
bar: The grant is exactly one sentence, contains no hedge word ("largely,"
"to some extent," "admittedly, but"), and does not smuggle in its own
rebuttal. The following sentence must state what the concession leaves
untouched in terms the conceded position's own holders would sign, not a
softened restatement of the thesis wearing the concession as cover.

form: the opponent's own word carries the steelman
move: Rozenshtein's steelman of the government's case does not paraphrase
David Sacks. It quotes him describing the jailbreak as enabling "the
operability of a cyber weapon" and lets that phrase, not a summary of it,
carry the government's strongest claim into the piece.
bar: The load-bearing claim in a steelman sentence must be the source's own
phrase, cited, not the writer's gloss on what they probably meant. If no
named holder on the opposing side has said the strong version in their own
words, the section is not ready — find the source who said it, or write the
milder claim they actually made and argue against that instead.

## Recently used, do not reuse

Checked against the last four opinion pieces in the library
(`mail-in-voting-order`, `end-the-emergency-tariffs`,
`saudi-nuclear-enrichment`, `france-under-15-social-media-ban`):

- The "X, not Y" / "the [term] and the [term] are not the same [term]"
  antithesis heading appears twice ("The block covers 23 states, not the
  country"; "The harm question and the instrument question are not the same
  question"). It is becoming a house tic on top of already being a bounded
  form in body prose. Do not open this piece's argument on a heading shaped
  that way.
- A heading reading "The case for [doing the thing]," placed as the last
  argument section before Sources, appears twice ("The Case for Signing
  Anyway"; "The case for drawing a bright line"). This piece's counter
  section already carries that job; do not also title a section "the case
  for" anything.
- Two of the four lean on Title-Case noun-phrase headings throughout
  ("The 150-Day Clock Section 122 Set for Itself," "The Power the Statute
  Never Delegated"). Use full-sentence, lowercase-led headings for this
  piece instead, to vary the recent shape per `spec/headlines.md`.
- All four open their first section on a jurisdictional or definitional
  distinction before any evidence. That is sound craft, not a habit to
  break by itself — but do not phrase that opening distinction as another
  "X question versus Y question" pair; that specific frame is the same tic
  as the first bullet.

## Alan Z. Rozenshtein, "A Kill Switch for Frontier AI"
Source: https://www.lawfaremedia.org/article/a-kill-switch-for-frontier-ai
Craft:
- cadence: Short declaratives carry the legal findings; longer conditional
  sentences carry the analysis of what those findings imply. The two never
  blur into one register.
- argument: Builds outward from a single dispute (one export-control letter)
  to a general claim (Congress needs a real framework) without ever
  pretending the single dispute proves the general claim by itself — the
  generalization is stated as a separate, weaker-warranted move.
- evidence: Primary documents first — the letter's own language, the
  regulation's own text — with named officials' public statements used only
  to establish stance, never to establish fact.
- stance: Committed to a structural verdict (this needs legislation) while
  staying genuinely undecided on the underlying factual dispute (was the
  jailbreak really that dangerous). The piece never needs to resolve the
  second question to win the first.
- notice: Catches that the government's own favored precedent (chip export
  controls) doesn't actually map onto model weights the way officials imply,
  and spends a paragraph on exactly where the analogy breaks.
- diction: Legal terms of art (deemed-export rule, supply-chain risk) are
  used once they're defined, then reused verbatim — no variation for
  elegance.
- reader: Assumes the reader can hold a legal argument and a technical one
  in the same paragraph without either being re-explained.
- the move the axes miss: the piece refuses to adjudicate which side of the
  factual dispute (government vs. Anthropic) is more credible, and wins its
  argument anyway, because the argument was never about who's right in this
  one incident. That separation — a structural verdict earned without a
  verdict on the parties' credibility — is the whole piece's discipline.

## Zachary Arnold and Micah Musser, "The Next Frontier in AI Regulation Is Procedure"
Source: https://www.lawfaremedia.org/article/the-next-frontier-in-ai-regulation-is-procedure
Craft:
- cadence: Each historical example gets almost exactly the same sentence
  count before the piece moves to the next one — a deliberate evenness that
  makes the case read as a pattern, not a cherry-picked anecdote.
- argument: Inductive, not analogical. Three procedural reforms from three
  different decades function as data points toward one general claim about
  how enforcement gaps form, not as three separate mini-arguments loosely
  gestured at the present.
- evidence: Statutory and regulatory history (workers' compensation,
  citizen-suit provisions, FTC enforcement) cited to the actual reform, not
  to secondary accounts of it.
- stance: Argues a mechanism, not a side. The piece isn't for or against AI
  regulation; it's for a specific claim about what makes regulation work,
  which is compatible with several different substantive positions.
- notice: Spots that "existing law already covers this" and "we need
  enforcement resources" are two different claims usually bundled together,
  and splits them before answering either.
- diction: Plain procedural vocabulary (standing, relief, forum) introduced
  once and never swapped for a synonym across the piece.
- reader: Assumes policy fluency but not legal training — procedural terms
  get one clean definition in context, then get used like any other word.
- the move the axes miss: the concession ("the skeptics have a point") is
  positioned as the pivot the whole piece turns on, not a courtesy paid
  before the real argument starts. Everything before it sets up the
  objection at full strength; everything after it depends on the boundary
  drawn in the very next sentence. Cut the concession and the piece has no
  argument left, which is the test of a real one.

## Noah Smith, "How I Would Regulate AI"
Source: https://www.noahpinion.blog/p/how-i-would-regulate-ai
Craft:
- cadence: Conversational stretches ("Well, OK, I don't think we're going to
  be facing off with Skynet") sit right next to flatly technical ones
  ("you don't really know what a model can do before it's trained") without
  a transition sentence bridging them — the shift itself signals a change
  from mood to mechanism.
- argument: Rejects the available menu (heavy pre-training mandates vs. no
  regulation) by relocating the argument to a third axis — where in the
  pipeline a rule can attach to something observable — rather than arguing
  for a point on the existing spectrum.
- evidence: Reasons from the technology's own development process (you
  can't know capabilities before training completes) as evidence against a
  specific policy design, not from a survey of other countries' rules.
- stance: States a considered uncertainty as part of the claim, not as a
  disclaimer bracketing it: "I don't think anything can eliminate those
  risks" is inside the argument, not before or after it.
- notice: Catches that "AI is a powerful new technology" and "this specific
  bill regulates it well" are conceded and disputed independently, so
  agreeing with the first buys the piece no ground on the second.
- diction: Reaches for engineering vocabulary (training run, inference,
  compute) over policy vocabulary wherever both are available, matching the
  register to how the reader already thinks about the technology.
- reader: Writes to someone who will check the mechanism, not just the
  conclusion — every claim about what a model can or can't do before
  deployment gets a sentence of "why," not just an assertion.
- the move the axes miss: the uncertainty ("I don't think anything can
  eliminate those risks") is immediately followed by a concrete, falsifiable
  proposal, not a summary of concern. The hedge buys credibility and then
  spends it on a specific mechanism in the very next sentence, rather than
  drifting into vaguer territory the way an unspent hedge usually does.

## Self-test

A writer following only the house default would build the case for a
federal disclosure floor on labs' incentive to cut corners without one —
the standard regulatory-capture-of-trust story. That piece would still pass
every rule in `spec/editorial.md`. It would not be this piece. This piece
should sound like an argument that never needs the reader to doubt a
frontier lab's word to work: concede every lab currently signing the EU
Code of Practice is acting in good faith, and show the disclosure floor is
still the right call because good faith doesn't solve an asymmetry that
only structured, comparable, third-party-checkable disclosure solves. That
is the one thing beyond the default: a case for regulation that would not
get weaker if every regulated party turned out to be telling the truth.
