# Voice guide — tech-news/2026-07-30 (invocation 01)

## Directive

Write each item cold on its news. The first clause of the prose names the thing
that changed and who changed it; everything the reader already saw in the
headline is spent, not repeated. Then give the one number or mechanism the
headline could not fit, and the one honest limit on it. Three moves, in that
order, and stop. An item that still reads as an item after you delete its last
sentence had a last sentence that graded the piece.

Register is a working engineer explaining a result to a sharp colleague: plain
declarative sentences, the specific noun (HAWK, a heat-pipe, orbital angular
momentum), never the soft one. Trust the verb. "Claude halved the key strength"
outperforms "researchers were able to achieve a reduction in." Prefer the period
to every other mark; you get one em-dash across the whole page, so save it.

Numbers are the evidence, so seat each one against something the reader already
holds. A cost of 2^64 dropping to 2^38 means nothing until you say it is the
difference between infeasible and a weekend of compute; 30,000 light-years means
nothing until it is "the farthest such flare ever seen from a galaxy's core." A
bare figure is a fact the reader has to convert themselves. Do the conversion.

State the caveat as a fact, not as a reassurance and not as a reversal. "No
deployed system is affected" is a fact; "but don't panic" grades the reader's
reaction, and "this is not a break, it is a warning" is the hedged-contrast
reflex the floor bans. When two labs or two methods disagree, say which one owns
the claim and move on.

Vary how items open. If one starts with the actor, the next can start with the
finding or the object acted on. Do not let every headline become "Company does
Adjective Thing." No colon subtitles. No triad of three parallel clauses in the
headline or the dek — that shape performs breadth instead of committing to the
one development that matters most.

Recently used, do not reuse: Nvidia-anchored openers and single-AI-lab framings
that dominated the recent run; headlines that perform comprehensiveness with a
paired-adjective or three-part triad; any closing line that hands the point back
to the reader; self-reference to the brief or the newsroom.

## Simon Willison, "Catching up on the weird world of LLMs"
Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/
Craft:
- cadence: short, plain sentences that each advance one fact; paragraphs end on
  the concrete example, not a summary.
- argument: builds from what is demonstrably true (a capability shown) toward
  the judgment, never ahead of it.
- evidence: names the exact model, the exact behavior, the exact date; links the
  primary artifact rather than describing it secondhand.
- stance: confident about what is shown, explicit about what is uncertain, and
  the two are kept visibly separate.
- notice: points at the surprising detail and lets it be surprising without
  announcing that it is.
- diction: technical terms used precisely and defined in the sentence they
  first appear, no jargon for texture.
- reader: assumes competence, never flatters or lectures.
- the move the axes miss: he reports capability and limitation in the same
  breath so neither reads as spin.
Calibration: "These things are genuinely weird. They can do things that feel
impossible, and they fail at things that feel trivial."

## Dan Luu, "A decade of major cache incidents at Twitter"
Source: https://danluu.com/cache-incidents/
Craft:
- cadence: dense but unhurried; long stretches of specifics broken by a flat,
  declarative judgment.
- argument: the pattern is earned from the individual cases, stated only after
  the cases are on the page.
- evidence: primary incident records and numbers; claims are traceable to a
  specific event, not to a general impression.
- stance: unshowy authority; the writer does not need the reader to be impressed.
- notice: the recurring failure mode is surfaced by accumulation, not assertion.
- diction: precise systems vocabulary, zero marketing register.
- reader: treated as an equal who will check the work.
- the move the axes miss: he lets the quantity of concrete detail do the
  persuading, so the conclusion feels inevitable rather than argued.
Calibration: "If you look at the incidents, a common theme is that a small,
seemingly innocuous change had a large, unexpected impact."

## Julia Evans, "Why is DNS still hard to learn?"
Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/
Craft:
- cadence: brisk, one idea per sentence, generous white space between ideas.
- argument: a question posed in the title and actually answered, point by point.
- evidence: worked, reproducible specifics (the exact `dig` output, the exact
  caching behavior) instead of abstractions.
- stance: curious and precise; admits what took her years to understand.
- notice: names the specific confusing thing rather than gesturing at difficulty.
- diction: concrete and unadorned; a term of art gets a one-line explanation.
- reader: a capable learner who was never told the missing piece.
- the move the axes miss: she isolates one mechanism at a time, so a hard topic
  arrives in pieces small enough to hold.
Calibration: "It took me an embarrassingly long time to realize that a domain
with no record will cache the fact that it has no record."

## Mitchell Hashimoto, "Ghostty Is Now Non-Profit"
Source: https://mitchellh.com/writing/ghostty-non-profit
Craft:
- cadence: calm, structural; each paragraph closes one question before the next
  opens.
- argument: reasons from a principle stated up front, then applies it to the
  specifics, so the decision reads as a consequence.
- evidence: the concrete terms of the arrangement (what transferred, what money
  moves where), not adjectives about intent.
- stance: measured and first-person without performing humility.
- notice: the load-bearing fact (irrevocability) is stated plainly, once.
- diction: plain, exact, no rhetorical heightening.
- reader: someone who wants the mechanism and the reasoning, not a pitch.
- the move the axes miss: he lets the plainness carry weight the emphasis would
  have cheapened.
Calibration: "No funds will be sent to me or used in any way that personally
benefits me."
