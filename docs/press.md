# Your press — ownership, forks, and updates

## The layout rule

- **`press/` is yours.** All configuration — series, voice, title, themes,
  templates — lives here. It does not exist on the upstream repo, so upstream
  can never ship a change that collides with it.
- **Everything else is the engine** — upstream-owned machinery you have no
  reason to touch (but see below: it's your fork, you *can*).
- **`examples/`** is a complete working press configuration kept as
  documentation. The engine never reads it; copy from it into `press/`.

The upstream repo is engine-only: it runs no press, publishes no library.
Even the maintainer dogfoods by forking it like any other user.

```
press/
  site.yaml          masthead title, theme, appearance, email delivery
  editorial.md       your voice — composed into every edition's instructions
  series/<id>/       series.yaml + prompt.md + sources/ per series
  series/_tags/      reusable prompt fragments shared across series
  themes/            custom design-token files
  templates/         your own edition templates (see docs/customization.md)
```

## The fork lifecycle

1. **Fork** with GitHub's "Copy the main branch only" box checked.
2. **Set up**: say "set me up" to your agent, or run `./setup.sh` by hand. It
   scaffolds your empty `press/`, creates the empty `library` branch, seeds
   its trigger workflows, and enables Pages + auto-merge. Enable workflows
   once in your fork's Actions tab.
3. **Publish forever**: the night shift adds editions to `library` via
   one-file PRs; `main` only changes when you change configuration or pull an
   engine update.

## Updating the engine — plain git, no tricks

```
git remote add upstream https://github.com/RyanSaxe/the-nightly-build.git   # once
git fetch upstream
git merge upstream/main
./setup.sh    # re-syncs the trigger workflows onto library
```

An ordinary fork merge. It is clean by construction for anyone who only
writes inside `press/`: your commits and upstream's commits touch disjoint
paths — upstream has no `press/` at all — so there is nothing to conflict.

**Editing the engine is allowed — it's your fork.** If you patch engine
files, future merges may conflict exactly where you deviated, and resolving
them is yours, same as any fork on GitHub. Conflicts are proportional to
deviation; staying inside `press/` keeps them at zero.

Two follow-ups after an engine update:

- `./setup.sh` re-syncs the two trigger workflows the `library` branch
  carries — the only engine-adjacent files outside `main`.
- Optionally dispatch the publish workflow (Actions → nightly-build-publish →
  Run workflow) to re-render your whole back catalog with the new assets
  immediately instead of waiting for tonight's build. Nothing on `library`
  ever merges with upstream — forks copy `main` only, and your library is
  yours alone.
