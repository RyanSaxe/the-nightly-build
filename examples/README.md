# examples/: how the default paper grows

A full paper configuration, kept as living documentation. The engine never reads
this folder. `nb setup` scaffolds three series, and this press starts from those
three and extends them, so the difference between it and a fresh `press/` is the
set of edits an owner makes. Copy pieces into your `press/` and edit:

```sh
cp -r examples/series/kernels press/series/my-course
cp -r examples/templates/lesson press/templates/lesson
```

- `news-brief/`: the scaffolded brief with its territory rewritten to AI and the
  items labeled by lane.
- `feature/`: the scaffolded daily read with two example packages added to its
  `templates:` list, so the orchestrator can choose `opinion` or `unbiased` when
  the material calls for one.
- `dispatches/`: the scaffold as shipped. Every article in it started as a
  request.
- `kernels/`: a sequence course on the example `lesson` package, with a pinned
  voice guide, `nb-code` listings, and the `hardware` and `benchmarks` tags.
- `docket/`: an open section on a day-list cadence, carried by this paper's own
  `rs-docket` furniture.

`templates/` holds the three example packages: `lesson`, `opinion`, and
`unbiased`. They are not in the shipped registry. A press copies the ones it
uses into `press/templates/`, which is where they land when this whole folder is
copied to `press/`.

`production.yaml` makes the balanced cost profile visible. Presses that omit it
receive the same cost-aware default. Set `profile: inherit` to keep the harness
model for every role.

Together the series exercise the rolling, open, and sequence modes, a manual
cadence, the three shipped templates and the three example packages, a
`templates:` list, press furniture, tag fragments, a pinned voice guide, and
word-band and source-floor calibration. The
[furniture guide](../docs/guides/customize/furniture.md) explains how templates,
themes, and furniture fit together. The shipped palette in `themes/newsroom.css`
is kept unchanged on purpose.

The upstream repo is engine-only and runs no site of its own. The maintainer
dogfoods by forking this repo like any other user.
