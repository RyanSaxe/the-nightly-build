# Scheduled shift operations

This reference owns the scheduled run from checkout verification through
publication. Read it at the start of every scheduled shift.

## Start from trusted state

Run system operations through this checkout's `nb` executable. It selects the
current engine and its `uv` environment; do not install engine dependencies by
hand or invoke files under `engine/` directly. If `uv` is unavailable, install
it or report the runtime as blocked before article work begins.

Run `nb sync` first. It verifies that the protected workflows on `library`
match `main`. When it exits 3 with `NB_SYNC_PR_REQUIRED`, carry the printed
request to the runtime's connected GitHub tool, wait for its validation and
merge, then rerun `nb sync`. Any other failure stops the shift.

Refresh a separate checkout of `library`, then run `nb duty` with the current
main and library paths. Follow an exit-2 repair and rerun it. A missing press is
an error; `examples/` is documentation, never live configuration. If nothing is
due, finish without opening a PR.

## Initialize each due article

After the edition is planned, resolve the selected series with
`nb source-policy` and `nb production-policy`. Honor required model selections
and record the actual model and effort used for each role.

Initialize the chosen series, slug, template, and tags with:

```text
nb start-article <series> <slug> --template <template> \
  --workspace .nb-work/<series>/<slug> [--tag <tag> ...]
```

The command owns the initial article, generated editorial direction, effective
template contract, runtime assets, and applicable furniture catalogs. Do not
edit generated context or recreate it in a brief. Keep later role invocations
numbered `02`, `03`, and onward without overwriting earlier work.

## Prepare and monitor the Article PR

After editor approval and a fresh writer proof, run:

```text
nb prepare-pr <workspace>/library/<series>/<slug>.html --library <library>
```

The command creates the branch and commit from current `origin/library`, proves
the submitted diff, pushes it, and opens or describes the one Article PR. If it
prints `NB_ARTICLE_PR_REQUIRED`, use the connected GitHub tool exactly as the
handoff directs. Never recreate or edit its generated branch manually.

Monitor every Article PR through CI, merge, and the published website. Route a
failure back through the desk, update the existing PR, and prove it again. The
shift ends only with published articles or a clearly recorded external blocker;
it never leaves an abandoned red PR.

Never merge or push to `library` directly. The protected workflow branch
created by `nb sync` is the sole non-article exception and may be used only as
that command directs.
