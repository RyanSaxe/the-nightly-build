# Feature catalog

The Nightly Build is a configurable publishing system. This catalog maps what
the released engine supports and where each capability is controlled.

## Shape the paper

| Capability                | What it supports                                                                                     | Configure or learn more                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Paper identity            | Masthead, footer, public description, and paper-wide editorial direction                             | `press/site.yaml`, `press/editorial.md`, and [Appearance and voice](../guides/customize/appearance-and-voice.md) |
| Default paper             | Three scaffolded series and a default voice. Edit the opening paragraph in each prompt.              | `nb setup`. See [Create your paper](../getting-started/create-your-paper.md)                                     |
| Recurring series          | Separate beats, genres, prompts, quality rules, and schedules within one paper                       | `press/series/<id>/` and [Series reference](series.md)                                                           |
| Series modes              | Curated collections, ordered sequences, date-based rolling coverage, and open-ended beats            | `mode` in `series.yaml`. See [the four modes](series.md#the-four-modes)                                          |
| Sections                  | One level of named grouping for the home page, Sections page, and article kickers                    | `section` in `series.yaml`. See [cadence, pausing, and sections](series.md#cadence-pausing-and-sections)         |
| Commissions and queues    | Required topics for collection and sequence series, plus a priority commission queue for open series | `items` and optional item prompts or tags in `series.yaml`                                                       |
| Shared prompt fragments   | Reusable editorial instructions selected by item tags                                                | `tags` in `series.yaml` and Markdown fragments under `press/series/_tags/`                                       |
| Multiple article packages | One enforced template for a series or several choices selected article by article                    | `template` or `templates` in `series.yaml`. See [Template reference](./templates.md)                             |

## Control timing and publication

| Capability              | What it supports                                                                                                        | Configure or learn more                                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Mixed cadences          | Daily, weekdays, weekends, selected UTC weekdays, and manual-only series under one scheduled run                        | `cadence` in `series.yaml`. See [cadence, pausing, and sections](series.md#cadence-pausing-and-sections) |
| Pause and resume        | Stop new scheduled articles while leaving the archive published                                                         | `paused` in `series.yaml`                                                                                |
| Deterministic duty list | Computes what is due from current press configuration and published state                                               | `nb duty` and [Schedule](../guides/operate/schedule.md)                                                  |
| Manual publication      | Commission an article from a topic, question, URL, documents, event, or detailed brief without waiting for cadence      | [Publish an article now](../guides/publish/publish-now.md)                                               |
| Hold before publish     | Open an asked-for article's PR as a draft that CI validates. Nothing merges until you mark it ready.                    | `nb prepare-pr --hold`. See [Your first article](../getting-started/first-article.md)                    |
| Reviewed revisions      | Change one published article and/or its matching figures or other local assets through the normal proof and render gate | [Revise an article](../guides/publish/revise-an-article.md)                                              |
| Retraction              | Remove one article, its assets, and its production record through a narrow, owner-reviewed PR                           | [Manage your paper](../guides/operate/manage-your-paper.md)                                              |
| Automatic publication   | Auto-merges every clean new-article PR and exact workflow sync. Revisions and owner curation wait for human review.     | [Publishing and security](../concepts/publishing-and-security.md)                                        |

## Govern editorial quality

| Capability                    | What it supports                                                                                                            | Configure or learn more                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Paper and series voice        | Paper-wide reader and register plus series-specific territory, structure, and editorial moves                               | `press/editorial.md` and each `prompt.md`. See [Appearance and voice](../guides/customize/appearance-and-voice.md) |
| Four editorial roles          | Writing coach, researcher, writer, and editor with isolated briefs and recorded outputs for new articles                    | [Architecture](../concepts/architecture.md)                                                                        |
| Deterministic proof           | Checks PR shape, metadata, structure, prose, citations, source policy, rubrics, and rendered behavior                       | The checkout-owned `nb check` command and [Publishing and security](../concepts/publishing-and-security.md)        |
| Strict mode                   | Promotes proof warnings to blocking failures for selected series, except advisory warnings marked non-promotable            | `strict` in `series.yaml`                                                                                          |
| Geometry guidance             | Sets recommended ranges for words, repeated items, and flexible sections                                                    | `bands` in `series.yaml`. See [quality and sources](series.md#quality-and-sources)                                 |
| Source floors                 | Requires a minimum number of cited sources, with template-aware defaults                                                    | `min_sources` in `series.yaml`                                                                                     |
| Source composition            | Requires primary and secondary source ranges for an article or for every repeated item                                      | `sources_by_kind` and `per_item_sources`. See [source composition](series.md#source-composition)                   |
| Required and bounded research | Requires configured documents, asks agents to consult background documents, or confines research to an exclusive source set | `required_docs`, `consult`, and `sources_exclusive` in `series.yaml`                                               |
| Enforced review rubrics       | Pins criteria, validates score rows and citations, and permits subject-specific additions                                   | `rubric` in `series.yaml`. See [Rubrics](series.md#rubrics)                                                        |
| Banned prose patterns         | Applies the engine's maintained vocabulary and prose checks, with press-owned additions                                     | `press/banned-terms.yaml` and [Appearance and voice](../guides/customize/appearance-and-voice.md)                  |

## Choose models and execution

| Capability                       | What it supports                                                                                                        | Configure or learn more                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Portable cost profiles           | `inherit`, `economy`, `balanced`, and `quality` profiles mapped to models available in the current harness              | `profile` in `press/production.yaml`. See [Production policy](production.md)    |
| Portable model tiers             | `efficient`, `capable`, `premium`, or the runtime's inherited model                                                     | `model` for a production stage                                                  |
| Exact model selection            | Provider-specific model IDs when portability is less important than pinning a model                                     | Set the stage `model` to the exact provider model ID                            |
| Per-role reasoning effort        | Provider-supported effort value for writing coach, researcher, writer, or editor                                        | `effort` for a production stage                                                 |
| Required or best-effort routing  | Require a model or effort directive. Record unavoidable deviations without stopping production.                         | `required` paper-wide or per stage                                              |
| Per-series production overrides  | Give one demanding or inexpensive series a different profile, model, effort, or requirement                             | `production` in that `series.yaml`                                              |
| Isolated or sequential execution | Run article roles in isolated child contexts where supported. Otherwise, run them sequentially with the same artifacts. | Selected by runtime capability. See [Architecture](../concepts/architecture.md) |

The production policy controls article roles, not the scheduled orchestrator.
Choose the orchestrator's model in the scheduler or automation where it runs.
The engine does not estimate model cost. Use the provider's usage reporting.

## Design articles and the site

| Capability               | What it supports                                                                                  | Configure or learn more                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Theme and color mode     | Shipped or press-owned CSS with automatic, light, and dark appearance                             | `theme` and `appearance` in `site.yaml`. See [Appearance and voice](../guides/customize/appearance-and-voice.md)                             |
| Front-page density       | Compact story cells or comfortable cells with deks                                                | `front` in `site.yaml`. See [Site reference](site.md)                                                                                        |
| Reusable furniture       | Timelines, comparison grids, evidence cards, pull quotes, rubrics, and custom semantic components | Shipped `templates/FURNITURE.md` or `press/furniture/`. See [Furniture reference](furniture.md)                                              |
| Custom templates         | Press-owned article skeletons with enforceable sections, citation geometry, chrome, and furniture | `press/templates/<id>/` with finished packages to copy in `examples/templates/`. See [Customize templates](../guides/customize/templates.md) |
| Figures and charts       | Store local images and data-backed charts with an article. Revisions can replace them.            | The article's matching asset directory and [Architecture](../concepts/architecture.md)                                                       |
| Trusted external assets  | Owner-selected HTTPS scripts and styles with exact Subresource Integrity pins                     | `assets` in `site.yaml`. See [Site reference](site.md)                                                                                       |
| Accessible static output | Semantic, script-free article content with responsive layouts and browser-render checks           | [Template reference](./templates.md) and [Publishing and security](../concepts/publishing-and-security.md)                                   |

## Operate and deliver

| Capability                         | What it supports                                                                                                                                       | Configure or learn more                                                  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Guided setup                       | Creates the press, publication branch, and workflows. Configures GitHub settings when the account permits it and reports settings that need the owner. | `./nb setup` and [Set up](../getting-started/setup.md)                   |
| Separate setup and schedule agents | Set up and request articles with one agent, then use ChatGPT Work or Claude Code Routines for scheduled publication                                    | [Integrations](../integrations/README.md)                                |
| Engine updates                     | Sync upstream engine changes without mixing `press/` or `library` state, then repair protected workflow copies                                         | `nb sync` and [Update the engine](../guides/operate/update-engine.md)    |
| Static GitHub Pages paper          | Publishes the complete site without an application backend or database                                                                                 | [Delivery](delivery.md)                                                  |
| Full-text search and catalog API   | Generates `search-index.json` and machine-readable paper state in `catalog.json`                                                                       | [Delivery](delivery.md#catalogjson-the-api)                              |
| Atom feeds                         | Publishes a paper-wide feed and one feed per series with full recent article content                                                                   | [Delivery](delivery.md#feeds-zero-setup)                                 |
| Shared directory                   | Makes a public fork discoverable from the Nightly Build directory, with an explicit opt-out                                                            | `directory` in `site.yaml`. See [Delivery](delivery.md#the-directory)    |
| Article history search             | Gives production agents narrowly requested prior coverage without loading the whole archive                                                            | The `nb history` command and [Architecture](../concepts/architecture.md) |
| Pinned series voice guide          | States once how a settled section should sound, so the writing coach never runs for it                                                                 | `voice_guide` in [Series](series.md#pinning-a-voice-guide)               |

For a complete working press, browse `examples/`. It demonstrates all four
modes, daily and day-list cadences, source policies, production policy, themes,
furniture, and series prompts without acting as configuration for your own
paper. Not every capability in this catalog has an example. The reference pages
above are the complete contract.
