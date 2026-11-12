# Commission: daily-brief/2026-11-12

Series: daily-brief (rolling, strict). Template: brief. Slug: 2026-11-12, the
UTC date `nb duty` selected. Bands: exactly 6 items, 300 to 700 words, at least
6 sources, one citation per item at minimum.

## Assignment

Six items in the series order: one Word of the Day, three news items, two
technology items. The researcher selects the items under the rules below and
records why each was chosen; the orchestrator confirms or replaces the choices
before drafting.

## Selection rules for this edition

- Word of the Day: a word with a documented origin story, preferably a coinage
  with a known coiner or a datable first use. Not a word used in the last eight
  briefs: psephology, sphexish, ecdysiast, mumpsimus, ultracrepidarian,
  eucatastrophe, agathokakological, phatic. Prefer a different field from those
  (several recent words came from literature and scholarship; politics was used
  for psephology). Run `nb history` on the candidate to confirm it was never
  used in any series.
- News: three items, chosen for consequence, not volume. United States first.
  Events of 10 to 12 November 2026, or a change in that window on a running
  story. The Hegseth impeachment resolution was the lead on 9 and 11 November
  and was referred to committee on 11 November; it takes no item unless a new
  development occurs. Check `nb history --series daily-brief` for the last four
  briefs and do not repeat a story without a new development.
- Technology: two items from the last few days: a release, a capability, a
  research result or another change worth following. The audience builds ML
  systems, so a technical item is welcome, but do not overlap the feature or the
  reinforcement learning lesson running in the same edition (see Neighbours).

## Sourcing

One strong source per item, the underlying record (court order, agency release,
roll call, paper, release notes) where it can be opened; a reputable report
where it cannot. A second source only where the first is disputed or cannot
settle the claim. Attribute unverified claims to their source.

## Display text

The headline reports the most consequential news item, with subject, verb and
the news in the first words, in the present tense. The dek adds a fact the
headline left out and does not restate it. Recent deks: "Thomas Massie was the
only Republican to vote against...", "An unsigned order holds that...",
"Once Thomas Massie raises...". Do not lead with a person's name again, and do
not build the dek as "X, which Y reports, ..." with an attributing relative
clause like 11 November's.

## Neighbours in this edition

- feature: topic to be recorded in the feature commission; do not choose a
  technology item on the same subject.
- reinforcement-learning/the-deadly-triad: a lesson on divergence of off-policy
  TD with function approximation. No overlap expected.

## Production

Roles: writing-coach (model capable, effort low), researcher (capable, high),
writer (capable, medium), editor (inherit, high, required). This run uses the
orchestrator's model for every role through subagents; record any deviation in
this file.

## Decisions during production

- Word of the Day may not be "grawlix" or "spoiler": the voice guide's
  word-history exemplars cover those words, so the writer would inherit their
  facts. (Answer to the writing coach's query.)
- Selection confirmed (orchestrator, after researcher/01): word "scofflaw";
  news: USDA SNAP categorical-eligibility proposed rule (lead, headline),
  Mississippi Senate race called for Scott Colom, DOJ indictment of three
  Iran-backed operatives; technology: Google Gemini Decisions API, Meta FAIR
  e-means in Faiss. The Nvidia board story stays out: as of drafting no
  outcome is announced and the reports rest on unnamed sources. e-means
  (posted 6 November) is accepted as recent; it does not overlap the feature
  (Glasswing vulnerability ledger) or the RL lesson.
- Mississippi: use AP's percentages; do not print a vote margin.
- Indictment: do not state custody status.
