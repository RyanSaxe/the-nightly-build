# Editorial review: tech-news/2026-08-11 (editor/01)

## Skeptic

The brief's thesis, carried by the title and dek: one AI result on the day was
checked by people and a proof assistant (Claude's Riemann-zeta bound), while the
other headline AI numbers, OpenAI's cyber benchmark and Meta's open-weight
comparisons, are the labs' own self-reports. Each item then adds the fine print
its announcement dropped. That thesis is stated in provenance terms, a claim
about the numbers rather than a grade of the desk's selection, so the dek holds.

I opened all nine citation targets as printed. Every one resolves to the source's
own page. OpenAI's announcement (#s3) returns HTTP 403 to an outside fetch; the
item does not pretend otherwise, it cites the gated page only as the thing it
could not open and sources the figures to the secondary that quotes OpenAI, so
the gating is the item's own subject and the link is still the correct canonical
address. Every `data-nb-kind` matches the primary/secondary test: one owning
primary and at least one independent secondary per item. Crypto Briefing (#s2) is
lower-prestige but independent of Anthropic, so it passes the independence test
the brief set as the routing trigger; it is a quality preference, not a sourcing
failure.

Item 1 (Riemann). The bound figures 41.6 to 67.2 percent match Anthropic's page
and Crypto Briefing. The token, session, and subagent counts, the four named
checkers, the Lean proof, and the "we don't expect the techniques to prove the
hypothesis" limitation all check out against Anthropic's writeup. Two claims did
not hold as printed and I fixed both. First, the draft credited "its authors and
one outside report" with calling the result the single largest improvement "the
problem has seen." Anthropic's page makes no magnitude claim at all, and the only
source for the superlative is Crypto Briefing, which scopes it to "this
particular bound in the history of the problem," not the whole problem. I
reattributed it to the outside report alone and restored the bound-scoped
wording. Second, the "would need the fraction to reach 100 percent" clause was
cited to Anthropic (#s1), which does not state it; Crypto Briefing does. I split
the citation so the limitation carries #s1 and the 100-percent requirement
carries #s2.

Item 2 (OpenAI cyber). CVE-2026-15903, the two chained V8 bugs that corrupt
memory and bypass the heap sandbox, and the completion-rate figures (95 vs 57.3
vs 1.5 percent) all match The Decoder, which also reports Google fixed the flaws
after coordinated disclosure. The headline's "zero-days" is supported: the bugs
were previously unknown, are now CVE-assigned and patched, and The Decoder uses
the term. The headline is hedged with "OpenAI says," and the body states plainly
that the benchmark is OpenAI's own and reaches the reader only through OpenAI's
account. TechCrunch (#s5) is a genuine independent US account that confirms the
launch and partners and carries none of the vulnerability detail, exactly as the
item says. No change.

Item 3 (photonic chip). Title, authors, and submission date match the arXiv
preprint; the measured figures (4-photon 16-qubit GHZ state, witnessed 10-qubit
entanglement above 11 sigma, Grover at 0.987, brightness 0.154 Hz) match the
evidence record's firsthand read of the full text. The company transliteration
was correctly left out. One display-text break: the headline read "built a
16-qubit entangled state and ran Grover on it." Grover ran on a single-photon
cluster state, not the 16-qubit state, which both the abstract and the body
confirm, so "on it" was a false coupling; and the article's own body and stat
strip reserve "entangled" for the witnessed 10-qubit claim while calling the
16-qubit result a GHZ state. I rewrote the headline to "built a 16-qubit GHZ
state and ran Grover's search," which matches the body and removes the false
implication.

Item 4 (Muse Glimmer). Parameter count, Apache 2.0, 131,072-token context, the
32GB build at 0.2 percent degradation, the SWE-Bench Pro row (51.2 / 50.2 /
36.9) and the GDPVal-AA v2 row (953 / 811 / 1141) all match the model card read
firsthand. SiliconAngle corroborates the half-the-benchmarks framing. The item
carries the self-report caveat and shows one named win and one named loss rather
than a sweep. No change.

## Cut

I ran the slop pass over every sentence, both edges, and the two furniture
components. No sentence failed the test. The items do not all end the same way:
item 1 stops on a scope limitation, item 2 on the independent secondary's silence,
item 3 on a throughput caveat, item 4 on a losing benchmark figure, so the brief
does not read as stamped despite each item carrying its caveat. The four headings
use four different verbs and none takes the colon-subtitle mold or a paired-
adjective triad. The dek is a single declarative with an appositive; it is not
one of the banned dek molds (no semicolon reversal, no suspended question, no
comma-and triad) and it does not restate the headline. Against the recent-pattern
notes, no item is stamped to the "ships X without the Y" withholding frame or to
a single mechanism-versus-caveat second sentence. No em-dashes, no prompt leakage,
no borrowed phrasing from the voice-guide exemplars, no self-reference. The stat
strip on item 3 carries three heterogeneous figures each cited in nearby prose,
which is its documented use. I made no cuts; the piece was already compressed to
the template's wire-service register.

## Reader

What the reader gets beyond the sources: a single frame that sorts the day's four
big numbers by how far you can trust them, one machine-and-human-checked math
result set against three figures that are the producing labs' own, with the exact
caveat each announcement dropped attached to it. That is a synthesis the evidence
record supplies the parts for but does not itself make, and it matches the
handoff's original-work sentence. The prose sits closer to the voice-guide
exemplars than to a median summary: it states provenance before the number where
that is the story (who checked the Riemann proof, whose benchmark the 95 percent
is), and it lets items stop on the caveat rather than manufacturing closers. The
title, read as the largest claim, commits to what the piece proves: an unreleased
Claude raised a proven bound to 67.2 percent.

## Edits

- Item 1: rewrote "Its authors and one outside report call that the single
  largest improvement the problem has seen" to "One outside report calls it the
  single largest improvement to that bound in the history of the problem" —
  removed the unsupported attribution to Anthropic and restored the source's
  bound-scoped claim (#s2).
- Item 1: split the final citation so "does not expect ... to prove the
  hypothesis itself" carries #s1 (Anthropic) and "would need the fraction to
  reach 100 percent" carries #s2 (Crypto Briefing), which is the source that
  states the 100-percent requirement.
- Item 3: rewrote the heading from "built a 16-qubit entangled state and ran
  Grover on it" to "built a 16-qubit GHZ state and ran Grover's search" —
  Grover ran on a single-photon cluster state, not the 16-qubit state, and the
  article's body and stat strip call the 16-qubit result a GHZ state.

## Required work

- writer (optional, non-blocking): item 1's independent secondary is Crypto
  Briefing. It passes the independence test, so it does not block. If the
  researcher surfaces a stronger US-newsroom secondary that carries the bound
  figures and the superlative, swap it into #s2; the item's scoped "single
  largest improvement to that bound" claim must stay sourced to whatever replaces
  it.
- orchestrator: re-stamp to refresh nb-meta (word count moved by a few words
  from my edits; reading time and all else unchanged).

## Decision

approve — every figure and label verifies against its owning primary, all
citations resolve, and the three breaks I found (one over-attribution, one
miscitation, one false Grover coupling) were prose and citation fixes within the
draft's own evidence, now applied.
