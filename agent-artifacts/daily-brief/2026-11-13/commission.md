# Commission: daily-brief/2026-11-13

Series: daily-brief (rolling, strict). Template: brief. Slug: 2026-11-13, the
UTC date `nb duty` selected (Friday). Bands: exactly 6 items, 300 to 700 words
(hard limit), at least 6 sources, one citation per item at minimum.

## Assignment

Six items in the series order: one Word of the Day, three news items, two
technology items. The researcher selects the items under the rules below and
records why each was chosen; the orchestrator confirms or replaces the choices
before drafting.

## Selection rules for this edition

- Word of the Day: a word with a documented origin story, preferably a coinage
  with a known coiner or a datable first use. Not a word used in the last nine
  briefs: scofflaw, phatic, agathokakological, eucatastrophe,
  ultracrepidarian, mumpsimus, ecdysiast, sphexish, psephology. Not "grawlix"
  or "spoiler" (the voice guide's exemplars may cover them). Prefer a field
  none of those came from: science, medicine, technology, commerce, sport or
  everyday objects. Run `nb history <word>` on the candidate to confirm it was
  never used in any series.
- News: three items, chosen for consequence, not volume. United States first.
  Events of 11 to 13 November 2026, or a change in that window on a running
  story. Check `nb history --series daily-brief` for the last four briefs and
  do not repeat a story without a new development. 12 November covered the
  USDA SNAP categorical-eligibility proposal, the Mississippi Senate race
  called for Scott Colom, and the DOJ indictment tied to RAF Fairford; 11
  November covered the Hegseth impeachment referral.
- Technology: two items from the last few days: a release, a capability, a
  research result or another change worth following. The audience builds ML
  systems, so a technical item is welcome. Not the subject of tonight's feature
  (recorded under Neighbours once chosen) and not observation normalization in
  RL (tonight's lesson).

## Sourcing

One strong source per item, the underlying record (court order, agency release,
roll call, paper, release notes) where it can be opened; a reputable report
where it cannot. A second source only where the first is disputed or cannot
settle the claim. Attribute unverified claims to their source.

## Display text

The headline reports the most consequential news item, with subject, verb and
the news in the first words, in the present tense. The dek adds a fact the
headline left out and does not restate it.

Recent headlines: "USDA estimates its SNAP proposal would end benefits for 6.3
million people in FY 2029", "House votes 211-204 to send the resolution
impeaching Hegseth to committee", "Supreme Court clears the way for Big Bend
border-wall construction". Three of the last three put a figure or a vote count
in the headline; tonight's should carry a figure only if the figure is the
news. Recent deks: "Limiting automatic eligibility to households on TANF
assistance would cut...", "Thomas Massie was the only Republican...", "An
unsigned order holds that...". Do not open the dek with a gerund phrase or a
person's name, and do not build it as "X, which Y reports, ...".

The headline and the lead item's heading must differ in wording; recent briefs
have let them nearly match.

## Neighbours in this edition

- feature/cloudflare-quepaxa: Cloudflare's choice of the QuePaxa consensus
  algorithm (blog post of 11 November). The technology items must not cover
  QuePaxa, Meerkat or Cloudflare's consensus work.
- reinforcement-learning/observation-scale: a lesson on observation scale and
  normalization in reinforcement learning. No overlap expected.

## Production

Roles: writing-coach (policy: capable, low), researcher (capable, high), writer
(capable, medium), editor (inherit, high, required). This run uses subagents on
the orchestrator's model for every role, with per-agent effort set to the
policy value where the Agent tool allows it. Record any deviation below.

## Decisions during production
- Word of the Day may not be "snarge" or "bootleg": the voice guide's
  word-history exemplars cover them. (Writing coach query, decided by the
  orchestrator.)
- Selection confirmed (orchestrator, after researcher/01): word
  "zenzizenzizenzic"; news: Jensen Huang resigns as Nvidia CEO (lead,
  headline), House passes the Major Richard Star Act 392-18 after a discharge
  vote, American Cancer Society's new PSA screening guideline; technology:
  DeepMind AlphaGenome 2, Runway Praxis-1 open weights. "Worse Together" stays
  out (paper predates the window). Praxis-1 over Gemini 4 Hydrogen to avoid a
  fourth consecutive Google-only technology pair.
- Word: do not say Recorde coined it. Say what the evidence supports: the
  OED's only citation is Recorde's 1557 Whetstone of Witte, where he notes
  others already called squares "zenzikes".
- Nvidia: no reason for the resignation is in the filings; attribute any
  reported reason to the outlet or omit it. The 8-K owns the facts.
- Star Act: use the Clerk's roll calls; give CBO-derived cost or beneficiary
  figures only if attributed to the outlet that reports them, or omit them.
- PSA: set the ACS guideline beside the still-current 2018 USPSTF grade C
  recommendation; benchmarks for both technology items are self-reported and
  say so.
