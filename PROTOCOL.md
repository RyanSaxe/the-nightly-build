# The Nightly Build agent protocol

This is the self-contained contract for one scheduled night shift. The
correspondent skill supplies the normal operating procedure; use this document
as the fallback when that skill cannot be loaded.

Run system operations through the checkout-owned `nb` executable. It locates
this exact checkout and lets uv provide its Python environment. Do not install
engine dependencies by hand or invoke files under `engine/` directly.

## Invariants

1. Serve only series returned by `nb duty`, at most one article per series.
2. One isolated workspace and one Article PR per article.
3. Only the orchestrator reads repository configuration, history, and the raw
   library. Editorial roles receive exact Markdown briefs and named inputs.
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
5. the series prompt, tag fragments in declared order, and item prompt.

Later layers specialize earlier ones; they do not override them. Use
`nb history` for bounded catalog searches, then read published work more deeply
only when commissioning needs it. Prevent repeated topics and angles. Record
recent structural habits—openers, section shapes, furniture, conclusions—as
things not to inherit automatically. Publication history is not a template.

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

- `required_docs`: local documents that must be read and cited with their IDs;
- `consult`: sources or archives read before searching elsewhere;
- `sources_exclusive: true`: the declared source set is the whole menu;
- `sources_by_kind`: primary and secondary bands for the article; and
- `per_item_sources`: those bands for every item in a per-item template.

The researcher records each classification and why. The writer carries it into
`data-nb-kind`. The editor audits it. Counts cannot determine independence.

Read every cited source. Open the underlying report, paper, hearing, filing, or
dataset instead of trusting a summary. Verify load-bearing numbers against the
primary that owns them. Seek contradictory evidence. A 403, paywall, or fetch
restriction is gated, not dead; never record an unverified URL.

## Exact workspaces and artifacts

For `<series>/<slug>`, create:

```text
.nb-work/<series>/<slug>/
├── library/<series>/<slug>.html
├── library/<series>/<slug>/                 # assets, when used
└── agent-artifacts/<series>/<slug>/
    ├── commission.md
    ├── writing-coach/01/{brief.md,voice-guide.md}
    ├── researcher/01/{brief.md,evidence.md}
    ├── writer/01/{brief.md,draft-handoff.md}
    └── editor/01/{review-brief.md,editorial-review.md}
```

Use `02`, `03`, and so on for revisions. Never overwrite an earlier invocation.
These files are plain Markdown without frontmatter or a machine manifest. The
Article PR commits them at these exact paths, so Git provides immutable bytes,
identity, and provenance.

`commission.md` records the assignment, angle, reader, mode, template, source
obligations, starting sources, relevant prior coverage, structures not to
repeat, neighboring articles, output paths, harness/model choices, and the
article's required contribution. Write directions, not sample article prose.

Every invocation brief names exact inputs, outputs, permitted changes,
role-specific decisions, useful `nb` commands, and unresolved work. Preserve
fixed HTML or labels exactly where needed; phrase editorial direction plainly.
Do not make roles reconstruct configuration.

## Role engagement contract

Every role launch names only its skill, exact brief, and the inputs that brief
allows. Start it in the article workspace when possible. State:

- These are your exact inputs and outputs.
- Do not inspect the repository, code, tests, Git history, raw library, other
  articles, or unlisted files.
- Use the supplied `nb` executable for system operations.
- Request missing context from the orchestrator instead of searching for it.

This is cooperative context isolation, not a security sandbox. Do not build
permissions, prompt compilers, metadata grants, or different command sets per
role.

Run the writing coach and researcher in parallel. The coach studies at least
three respected writers in the domain and produces transferable craft, never a
named persona or reusable line. The researcher produces traceable sources,
contradictions, numbers, source-asset candidates, and discarded sources.

Only then brief the writer. The writer drafts from the evidence record, follows
the voice guide, and uses the exact skeleton and constraints in its brief. It
requests missing evidence or voice guidance instead of filling gaps. It records
the article's visible act of original work in `draft-handoff.md`, runs the
brief's `nb check` command to `BLOCK: 0`, and treats warnings as revision notes.

The editor receives the exact writer brief so prompt leakage is detectable. It
makes three ordered reads:

1. **Skeptic:** state and try to break the thesis and load-bearing claims;
   reopen sources, recompute figures, and audit source kinds.
2. **Cut:** remove sentences with no fact, claim, or reasoning work; cut
   self-grading, signposts, instruction leakage, and repeated paper structures.
3. **Reader:** identify what the article gives beyond its sources, compare that
   with the writer's original-work claim, judge the voice, and retest headline.

The editor makes cuts and small prose fixes directly. Past a word or clause,
new writing returns to the writer. Evidence returns to the researcher; assets,
markup, structure, and proof return through the writer. Each repair gets new
numbered briefs and outputs, then a fresh writer proof and editor read. There is
no round cap. Only an editor `DONE` with no required change approves the piece.

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
- Cite load-bearing claims inline. Number source entries in first-citation
  order. Carry honest source kinds and locators from the evidence record.
- Use furniture only when it communicates information prose would obscure.
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
