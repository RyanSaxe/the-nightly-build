# Editorial review: tech-news/2026-08-04 (editor/02)

Focused confirmation round. I verified only the two editor/01-required deltas and
checked that the settled parts of the piece did not regress. Both repairs hold.

## Skeptic

Delta 1 — Item 1 (Astra) headline and nb-meta title. The overclaim is gone. The
old line asserted accomplished settlement as narration ("OpenAI settles ten
previously open problems..."); the new line reports the true state: "OpenAI
released proofs it says settle ten previously open problems in mathematics and
computer science." It commits to what the sources establish — released,
machine-checkable Lean files, the settlement claim attributed to OpenAI ("it
says settle"), not independently confirmed — and matches the body's "no one
outside OpenAI has confirmed them yet." It is a real headline: subject, verb,
the news in the first words, no colon subtitle, no Betteridge question, and it
borrows no endorsement the sources lack. h1 (line 39) and the nb-meta `title`
(line 21) are byte-identical. The nb-meta `dek` (line 29) and the rendered
`nb-dekline` (line 40) remain byte-identical and were left untouched, as the
handoff states.

Delta 2 — Item 3 (vagus) clinical-use repointing. The miscitation I routed is
fixed. The fascicle-to-organ clinical significance now reads "the use the
Feinstein team says the atlas is meant to inform" and cites the primary (s5)
only. I reopened s5 (the Feinstein/Northwell release via BioSpace): it frames
the atlas as yielding "critical insights into how the vagus nerve communicates
with various organs" and enabling more precise therapy design, so the intended
use is honestly attributed to the authoring team rather than presented as a
proven fascicle-to-organ result. The "GEN underlined on July 28"
named-verification clause is deleted. GEN (s6) is now cited once, in the opening
paragraph (line 164), only for the atlas and its headline figures; I reopened
s6 and confirmed it independently reports the 200,000+ fibers, 60 nerves, and 30
donors. Both hrefs resolve to the sources themselves, the kinds are honest (s5
primary, s6 independent secondary), and the item keeps its one-primary +
one-independent-secondary composition.

No regression elsewhere. The Astra results-to-Lean-file table (all ten filenames)
is unchanged. The Cisco item still keeps CVE-2026-20316 (exploited, CVSS 5.3)
strictly distinct from the CVSS-10 CVE-2026-20079 (PoC-to-root, no observed
exploitation); untouched. Items 2 and 4 are otherwise as verified in editor/01.

## Cut

No new cuts. My editor/01 direct cut survives intact: the Item 2 signpost "The
report's own conclusion bounds the result." is gone and the orphaned pronoun
repair reads "quoted in the report" (line 141). No new leakage, self-grading, or
banned mold entered with either change. One non-blocking observation: because the
reframed headline now contains the verb "released," the dek's opening "It released
the proofs..." lightly echoes it before adding its own cargo (the Lean 4 form, the
line-by-line checker, the Astra credit). The dek's identifying detail is still
additive and the dek was correctly left untouched this round, so this is a note,
not required work.

## Reader

Unchanged from editor/01: the piece still gives more than its sources — the ten
scattered Astra claims resolved into one table of named, openable Lean files, and
four items ordered on a real seam of what can and cannot yet be independently
checked. With the headline repair, the largest claim now matches the body it
sits above instead of retracting itself three sentences later, and the vagus
close no longer dresses attribution as third-party verification. The prose sits
closer to the voice-guide exemplars than to a median summary.

## Edits

- None. Both required repairs were applied correctly by the writer; no changed
  line needed a correctness touch, so no `nb stamp` was run this round.

## Required work

- None. Both editor/01 required items are resolved and verified against their
  owning primaries; the proof stands (words 875, sources 9, PUBLISHABLE).

## Decision

approve — the Astra headline and nb-meta title now report the released,
machine-checkable, OpenAI-attributed result rather than settled fact (h1 ==
title, dek == dekline, byte-identical), the vagus clinical use is repointed to
the primary (s5) with GEN (s6) cited only for what it corroborates, and the
earlier cut, the Astra table, and the Cisco CVE distinction are untouched.
