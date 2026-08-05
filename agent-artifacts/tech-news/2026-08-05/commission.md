# Commission: tech-news/2026-08-05

## Authorized work
Scheduled duty for UTC 2026-08-05 returned `tech-news` (rolling, `brief`
template) for the unpublished date 2026-08-05. Publish exactly one brief for that
date. This is the only tech-news article this run.

## What this brief is
The day's technology front page for 2026-08-05: 4-6 selected items, each stating
the development with its actors named and saying why it matters technically. This
is a *rolling news* piece: selection happens in research against live reporting.
The researcher assembles candidates from primary records (papers, model cards,
release notes, benchmarks, official announcements) and reputable independent
reporting; the writer selects and orders the final 4-6.

## Selection standard (from the series prompt)
- Select the day's most consequential developments *in technology*. AI is
  central but significance decides the mix. Product promotion, incremental
  releases, and online attention do not qualify on their own.
- Science and health belong when a result changes technical knowledge or
  practice enough to deserve attention here. Treat the research itself as the
  development.

## Sourcing
`brief` template: 4-6 items; per item exactly 1 primary + at least 1 independent
secondary; `min_sources: 5` overall. Verify every benchmark number, parameter
count, price, and date against the primary that owns it (a model card or paper,
not a blog aggregator). A vendor's own claim is a primary for *what was
announced*, secondary for *whether it is true*; where a capability claim is the
news, note independent verification or its absence. Confirm every URL resolves to
the source's own page. Beware aggregator/newsletter summaries that inflate or
garble figures: trace each claim to its owner.

## Template and policy
- Template: `brief` (fixed).
- Production policy (balanced): editor required at high effort, model inherit.
  Researcher/writer models = capable; writing-coach = capable, low effort.

## Boundaries — do not repeat, and non-overlap with this edition
- Recent tech-news slugs are dated 2026-07-26 … 2026-08-04 (consecutive). Do not
  re-file an already-covered release/result as new. Use
  `nb history --structure tech-news/2026-08-04` and a prior day or two to see
  recent leads and break those shapes.
- **Non-overlap with current-events (same run):** a story whose news is its
  *public or policy consequence* belongs to current-events. Keep this brief to
  developments *in the field* (models, chips, systems, scientific results).
- **Non-overlap with the opinion desk (same run):** the opinion piece argues AI
  *governance* (EU AI Act GPAI obligations, US policy). Report a field
  development, not a governance argument. If an AI-regulation milestone is
  genuinely a field-shaping event, a one-line factual note is the ceiling; the
  argument is not ours.
- **Non-overlap with paper-of-the-day (same run):** that piece reconstructs the
  2020 DDPM diffusion paper. Do not file a diffusion-history retrospective here;
  only current (this-week) diffusion news qualifies, if any.
- Headlines/deks: pick the one development that matters most and say what
  happened to it; avoid the triad-of-adjectives headline, colon subtitles, and
  the banned dek molds. Numbers earn the headline only when the figure is the
  story.

## Neighbors this edition
Full edition: current-events, tech-news (this), expert-tools/visidata,
investing/free-cash-flow, opinion/mandate-frontier-ai-disclosure,
paper-of-the-day/denoising-diffusion, word-of-the-day/ultracrepidarian. Keep this
brief's items disjoint from current-events.
