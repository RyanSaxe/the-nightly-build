# The Nightly Build agent protocol

This is the authoritative contract for one scheduled night shift. Read it
before loading the correspondent skill. The protocol defines the process; the
skill defines how the correspondent plans, commissions, and runs the desk.

Run system operations through the checkout-owned `nb` executable. It locates
this exact checkout and runs on [uv](https://docs.astral.sh/uv/), which must be
available on PATH; install it if the run environment lacks it. uv provides the
engine's Python environment, so do not install engine dependencies by hand or
invoke files under `engine/` directly.

## Invariants

1. Serve only series returned by `nb duty`, at most one article per series.
2. One isolated workspace and one Article PR per article.
3. The correspondent prepares each role's exact context. Editorial roles begin
   with those named inputs and retrieve anything else for a specific need.
4. Every article passes a writing coach, researcher, writer, and editor. The
   writer-editor loop ends only when the editor approves.
5. Never push to `library`. CI validates and publishes Article PRs.

## Commission the night

Run `nb sync` before article work. It verifies that the protected publishing
workflows on `library` match `main`. When it exits 3 with
`NB_SYNC_PR_REQUIRED`, use the runtime's connected GitHub tool exactly as the
handoff says, then rerun `nb sync`. Any other failure stops the run.

Refresh a separate checkout of the `library` branch, then run `nb duty` with
the main and library paths. Follow an exit-2 repair and rerun it. Nothing due
means stop without a PR. `examples/` is documentation, never press config.

The orchestrator plans the whole night before launching a role. Read the
governing layers in order:

1. this protocol;
2. `spec/editorial.md` and `spec/headlines.md`;
3. `press/editorial.md`, when present;
4. the selected template's manifest, skeleton, identity, and furniture;
5. the series prompt, tag fragments in declared order, and selected item record.

Later layers specialize earlier ones; they do not override them. Start history
work with `nb history`. Use `nb history --show <series>/<slug>` or the raw
article only when commissioning has a specific question the result list cannot
answer. Prevent repeated topics and angles. Record recent openers, section
shapes, furniture, and conclusions as habits not to inherit automatically.
Publication history is not a template.

For each due article, run `nb source-policy` and `nb production-policy`. Resolve
portable model tiers against the current harness, honor required selections,
and record the actual model and effort. Complete every commission before roles
start so tonight's articles remain cohesive and non-redundant.

## Source policy

A primary source owns the claim: a paper, filing, ruling, dataset, or a party's
statement about itself. A secondary reports or analyzes that primary from
outside the authoring party. Independence follows authorship and stake, not
document type or website.

The series may define:

- `required_docs`: local documents that must be read and cited with their IDs
- `consult`: sources or archives read before searching elsewhere
- `sources_exclusive: true`: the declared source set is the only allowed set
- `sources_by_kind`: primary and secondary bands for the article
- `per_item_sources`: those bands for every item in a per-item template

The researcher records each primary or secondary classification beside its
citation and explains why. The writer carries it into `data-nb-kind`. The
editor audits it. Counts cannot determine independence.

Read every cited source, but do not read every character by default. Search it
for the information the article needs. Open the underlying report, paper,
hearing, filing, or dataset instead of trusting a summary. Verify numbers and
statements in secondary coverage against the primary that owns them. Seek
contradictory evidence. A 403, paywall, or fetch restriction is gated, not
dead; never record an unverified URL.

## Exact workspaces and artifacts

For `<series>/<slug>`, create:

```text
.nb-work/<series>/<slug>/
├── .nb-context/
│   ├── template-contract.yaml
│   ├── runtime-assets.yaml
│   └── furniture/{engine,press,template}.md # files that apply
├── library/<series>/<slug>.html
├── library/<series>/<slug>/                 # assets, when used
└── agent-artifacts/<series>/<slug>/
    ├── editorial-direction.md
    ├── commission.md
    ├── writing-coach/01/{brief.md,voice-guide.md}
    ├── researcher/01/{brief.md,evidence.md}
    ├── writer/01/{brief.md,draft-handoff.md}
    └── editor/01/{review-brief.md,editorial-review.md}
```

After selecting the series, slug, template, and tags, initialize the workspace:

```text
nb start-article <series> <slug> --template <template> \
  --workspace .nb-work/<series>/<slug> [--tag <tag> ...]
```

The command copies the resolved skeleton to the article path. It writes the
effective template contract, configured runtime assets, and applicable
furniture catalogs under `.nb-context/`. It also composes
`editorial-direction.md` verbatim from the house, press, template, series, tag,
and selected-item layers. Do not edit generated context. CSS and JavaScript are
implementation details; author against documented furniture, then preview and
check it. A press dependency intended for article authors must be documented in
its furniture, template identity, or series prompt.

Use `02`, `03`, and so on for revisions. Never overwrite an earlier invocation.
The Article PR commits `editorial-direction.md`, `commission.md`, and every
numbered role input and output. They are plain Markdown without frontmatter or
a machine manifest. `.nb-context/` is temporary, version-derived tool context;
the committed direction records its checkout revision.

`commission.md` records the assignment, angle, reader, mode, template, source
obligations, starting sources, relevant prior coverage, structures not to
repeat, neighboring articles, output paths, harness/model choices, and the
article's required contribution. Write directions, not sample article prose.

Every invocation brief names exact inputs, outputs, permitted changes,
role-specific decisions, useful `nb` commands, and unresolved work. Preserve
fixed HTML or labels exactly where needed; phrase editorial direction plainly.
Do not make roles reconstruct configuration.

## Role engagement contract

Every role launch names its skill, exact brief, and named inputs. Start it in
the article workspace when possible. State:

- Begin with these exact inputs and write only the named outputs.
- Use the supplied `nb` executable and other available tools for focused work.
- Do not tour the repository, implementation, Git history, or archive as
  background. Retrieve context to answer a specific question.
- Request missing context from the correspondent. It can expand the input set
  or route the question to the role that owns it.

This is cooperative context isolation, not a security sandbox. Do not build
permissions, metadata grants, or different command sets per role.

Run the writing coach and researcher in parallel. The coach studies at least
three respected writers in the domain and produces transferable craft, never a
named persona or reusable line. The researcher produces traceable sources,
contradictions, numbers, source-asset candidates, and discarded sources.

Only then brief the writer. The writer receives `editorial-direction.md`, the
voice guide, evidence record, initialized article, generated template context,
and its exact brief. It requests missing evidence or voice guidance instead of
filling gaps. It records the article's visible act of original work in
`draft-handoff.md`, runs the brief's `nb check` command to `BLOCK: 0`, and
treats warnings as revision notes.

The editor receives the exact writer brief so prompt leakage is detectable. It
makes three ordered reads:

1. **Skeptic:** state and try to break the thesis and the claims it depends on;
   reopen sources, recompute figures, and audit source kinds.
2. **Cut:** remove sentences with no fact, claim, or reasoning work; cut
   self-grading, stock revelations, signposts, instruction leakage, and
   repeated structures not required by the current template.
3. **Reader:** identify what the article gives beyond its sources, compare that
   with the writer's original-work claim, judge the voice, and retest headline.

The editor makes cuts and small prose fixes directly. Past a word or clause,
new writing returns to the writer. Evidence returns to the researcher; assets,
markup, structure, and proof return through the writer. Each repair gets new
numbered briefs and outputs, then a fresh writer proof and editor read. There is
no round cap. Only an editor `DONE` with no required change approves the piece.

Launching a role does not transfer responsibility for the article. The
orchestrator remains responsible for moving every article through every
required stage.

A blocked role escalates to the orchestrator. Clarify, reassign, or take over
the owning role, but never waive the subsequent writer proof and editor gate.
Stop only for an external constraint no role can change. If the harness has no
child agents, perform the same numbered sequence in one context and preserve
all artifacts.

## Article contract

The article is one HTML file at `library/<series>/<slug>.html`, plus only its
matching source assets or chart provenance under `library/<series>/<slug>/`.

- Fill every required anchor section once and only the allowed number of
  subject-specific flexible sections. Remove placeholders and samples.
- Preserve the template's fixed engine assets, classes, labels, and required
  HTML. Add no active content: no extra scripts, styles, iframes, forms,
  handlers, `javascript:` URLs, or externally hosted images.
- Cite the claims the argument depends on inline. Number source entries in first-citation
  order. Carry honest source kinds and locators from the evidence record.
- Treat furniture as part of the article's language. Plan it with the prose and
  reassess it after rendering; every component needs a clear communicative or
  editorial purpose. There is no target count, but the page must remain a
  continuous article rather than a stack of components.
- Create charts with `nb chart` from verified numbers and commit their
  provenance. Capture exact visual evidence with `nb asset`. Inspect the image
  and rendered page; include factual cited captions and useful alt text.
- Fill `nb-meta` with actual values. `sources` and `words` are measured, not
  targets to inflate. `harness` and `model` are the resolved writer runtime.

The metadata block is JSON in `<head>`:

```html
<script type="application/json" id="nb-meta">
  {
    "protocol": "1.1",
    "series": "semiconductors",
    "slug": "micron",
    "template": "article",
    "title": "The scarcest commodity in AI is made by Micron",
    "mode": "collection",
    "order": null,
    "date": "2026-07-06",
    "tags": ["equity"],
    "sources": 24,
    "words": 4100,
    "reading_minutes": 18,
    "dek": "One-sentence teaser shown on the newsstand card.",
    "harness": "harness-name",
    "model": "selected-writer-model"
  }
</script>
```

`mode` is `collection`, `sequence`, `rolling`, or `open`. `order` is the
one-based sequence index and otherwise null. `date` follows the run's UTC date.

## Prepare, validate, and publish

After editor approval, run:

```text
nb prepare-pr <workspace>/library/<series>/<slug>.html --library <library>
```

The command validates the exact artifact tree and article, creates one safe
commit from `origin/library`, proves the committed diff, pushes it, and opens or
reuses the Article PR. If `gh` is unavailable, use its printed
`NB_ARTICLE_PR_REQUIRED` request with the harness's GitHub connector. Do not
recreate or edit the generated branch.

CI runs the same `nb` proof, builds and render-probes the article, and
auto-merges clean PRs when the series allows it. The orchestrator monitors every
PR through CI, merge, and the published website. A CI failure returns to the
orchestrator, which creates the necessary numbered repair and updates the same
PR. The night ends with published articles or an explicit external blocker,
never abandoned red PRs.

Never merge or push to `library` directly. Never open a second PR for the same
article. The protected workflow branch created by `nb sync` is the sole
non-article exception and may be used only as its handoff directs.
