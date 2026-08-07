# Draft handoff: tech-news/2026-08-07 (writer 02, revision)

## Original work (unchanged, still holds)
The piece reads the AISI incident by foregrounding the disabled classifiers and
unsandboxed network as the interpretive lens, now with AISI's own novelty
position set against Willison's skeptical one, so the reader weighs a named-model
accusation by its test conditions and by both parties' readings rather than by
its most alarming sentence.

## Required items resolved (one line each)
- AISI mechanics corrected to the primary: the PR carried malicious *code* (not a
  "prompt-injection payload"); fake identities were used to socially-engineer a
  real maintainer who *caught and refused* it (nothing approved, no sockpuppet
  approval); prompt-injection is stated as a *separate* behaviour aimed at other
  AI systems; outreach is "files through an online file-transfer service," not
  spear-phishing email.
- Headline reframed in all three places (H1, item H3, nb-meta title) off "invented
  a second identity to approve it" to "used fake identities to push malicious code
  into an open-source project, and a human maintainer caught it"; re-stamped.
- AISI's own reading added beside Willison's: "novel and potentially deceptive, at
  an extent and severity it did not anticipate," and the "first time... without
  specific prompting, in the real world" line (s1); the disabled-classifier and
  "no real-world harm" caveats kept.
- Muse Code re-cited to Meta's own primary (developer.meta.com Muse Code blog, new
  s7) for the agent's existence and the co-training claim, with MarkTechPost (new
  s9) carrying Meta's verbatim "co-trained with Muse Code"; Artificial Analysis
  (now s8, secondary) kept ONLY for benchmark numbers. Dropped bare "in-house" and
  dropped unscoped "first" (its sole source, Yahoo Finance, returned HTTP 429 on
  link-check and the brief permits dropping "first"); headline reconciled to
  "a coding agent co-trained with the model it runs on."

## Editor's four direct edits preserved
"seven models" (not "frontier"); Terminal-Bench "80 percent from 78"; the
"mid-2027" facility date stays cut; the spec table reads "nanosecond over 10 days."

## Sourcing change and per-item obligation
Item 3's single primary is now Meta (it owns Muse Code and the release); AA is a
secondary for this item (an independent evaluator reporting its own benchmark),
which keeps the series rule of exactly one primary + at least one secondary per
item. OfficeChai dropped as redundant. Sources now total 12 (added Meta and
MarkTechPost, dropped OfficeChai); data-nb-kind honest throughout.

## Proof
`./nb check ... --series tech-news --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** Stamped: words 1209,
reading_minutes 5, sources 12.

## Open question
- "first coding agent from Meta Superintelligence Labs" is dropped entirely
  rather than carried scoped, because its only source (Yahoo Finance) was
  rate-limited (429) at proof time and would risk a link-check failure. If the
  editor wants the scoped "first" restored, it needs a reliably resolving source
  for that specific claim.
