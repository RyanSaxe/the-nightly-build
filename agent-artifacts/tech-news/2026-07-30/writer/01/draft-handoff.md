# Draft handoff — tech-news/2026-07-30 (writer invocation 01)

Production: single-context, no isolation.

## Original-work sentence
From a July 29–30 news cycle dominated by funding rounds, chip awards, and a
policy fight over pacing AI, this brief selects five results in which a machine
or a beam of light did work once reserved for human experts, and pins each to
its own ceiling — no deployed cryptosystem broken, a reduced-round AES attack
only, a record off-nuclear flare rather than a threat — so the capability and its
limit are read together rather than one at a time.

## Files changed
- Article: `.nb-work/tech-news/2026-07-30/library/tech-news/2026-07-30.html`
  (authored from the initialized brief skeleton; five items, ten sources).
- No assets or charts (none load-bearing per the evidence record).

## Proof
`./nb check … --series tech-news --repo . --library ../library` → BLOCK: 0,
WARN: 0, verdict PUBLISHABLE. First pass returned two warnings (a 53-word
sentence in item 1; a word-count mismatch); both were fixed by splitting the
sentence and setting nb-meta words to the counted 719 (reading_minutes 3, byline
matched). No warnings intentionally left.

## Source geometry
Every item carries exactly one primary (headline link) and one independent
secondary (cited inline), numbered in first-citation order s1–s10, five primary
and five secondary, `data-nb-kind` set honestly. Items 4 and 5 have primaries
(University of Michigan; Science Advances) that return HTTP 403 to automated
fetchers; these are gated, not dead — domains resolve and every cited claim was
verified through the independent secondary and search retrieval, per the evidence
record.

## Editorial choices worth the editor's eye
- Title commits to the single most consequential development (item 1) rather than
  performing breadth; the dek adds the two-year-review detail and the
  no-production-impact caveat.
- The AES result is stated as reduced-round only, with the >400-octillion-message
  limit, so "200 to 800 times faster" is not overread as a break of AES.
- Item 2 is framed as a multi-institution robotics result; Nvidia is one of many
  named collaborators and is deliberately not foregrounded, per the commission's
  Nvidia-fatigue note.
- The electron-lighthouse semiconductor material is not named because no source
  states it.

## Remaining questions
None. Evidence and voice guidance were sufficient.
