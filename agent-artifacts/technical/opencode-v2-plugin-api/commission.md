# Commission: technical/opencode-v2-plugin-api

## The assignment

OpenCode (the open-source terminal coding agent) went to version 2.0 (GA
2026-09-11), shipping a new, backward-incompatible plugin API under a new npm
scope (`@opencode/*`, e.g. `@opencode/plugin` and `@opencode/cli`, at 2.0.x). The
v1 packages (`@opencode-ai/plugin`, `@opencode-ai/sdk`) remain v1-only. Reporting
and a visible wave of community-plugin migration issues establish the change is
recent (within 90 days) and in active use, not a pitch.

Write a technical walkthrough of the v2 plugin API: what a plugin is, how the v2
shape differs from v1, and enough of its design and behavior that a reader could
write or migrate one. Open it with concrete code.

## The original work this piece owes

Go beyond "v2 has a new plugin API." The verified facts to build on (researcher
confirms the exact current shape against the v2 docs/source and a real plugin):

- v1's model: a plugin was a named export (a server/hooks export) from the
  `@opencode-ai/plugin` package.
- v2's model: a plugin is a **default export** that is one of two shapes — a
  promise/async API `{ id, setup }`, or an Effect API `{ id, effect }`. Confirm
  the exact field names, the function signatures, what `setup`/`effect` receive
  (context/hooks) and return, and how the CLI loads it.
- The migration reality: what breaks when a v1 plugin runs under v2, and the
  minimal diff to port one. A dual v1/v2 adapter pattern appears in the wild —
  confirm and show it only if real.

The walkthrough's original contribution: a reader finishes able to write a minimal
working v2 plugin and to port a v1 plugin, with the API surface explained from the
source rather than paraphrased from the announcement. The writer states the exact
one-sentence contribution in `draft-handoff.md`.

## Boundaries

- "Recent and in use": lead with the dated GA and ground adoption in concrete
  evidence (named community plugins migrating, dated issues/PRs, download or
  version facts) — not vendor adjectives.
- Code must be correct and runnable against the real v2 API. Every API name,
  package name, version string and file path is verified against the source or
  docs the researcher opened. If a detail cannot be confirmed, the writer states
  the uncertainty rather than inventing a signature.
- Prefer a minimal, illustrative plugin the reader could actually run. Label
  illustrative code as illustrative in the code header/caption.
- This is the edition's developer-tooling piece. Do not drift into the AI-model
  news (GPT-6.1 Sol) in the daily brief or the copyright feature.

## Furniture available and encouraged

`nb-code` (code listing with `data-language`, file/context header, cited caption)
is the backbone here — the behavior of the code is the evidence. A small
`nb-table` contrasting v1 vs v2 package names / export shapes may earn its place.
A conceptual `nb-figure` of how the CLI loads a default-export plugin and invokes
`setup`/`effect` is welcome if it shows the mechanism faster than prose. See
`.nb-context/furniture/engine.md`.

## Template, sources, production

- Template: `article` (longread; 2–6 flex sections; 800–6000 words; per-section
  citations; min 8 sources). (`technical` also allows `paper`; `article` is the
  right fit for a tooling walkthrough.)
- `nb-meta`: series `technical`, slug `opencode-v2-plugin-api`, mode `open`, date
  `2026-10-04`.
- Source policy: `article` min 8 sources (`nb source-policy --series technical`).
  Favor primaries: the v2 docs, the package on npm, the repository source, release
  notes, and real migration issues/PRs.
- Production (`nb production-policy --series technical`): editor required, high
  effort, model inherit. researcher capable/high, writer capable/medium,
  writing-coach capable/low. Recorded actual assignment: coach/researcher/writer on
  a capable model (sonnet-class), editor on the orchestrator's model (opus-class)
  at high effort. No `required` directive traded down.

## Neighbouring articles in this edition

- daily-brief/2026-10-04: Word of the Day + 3 news + 2 tech (GPT-6.1 Sol; SynthID
  Bio). The brief's tech items are deliberately NOT OpenCode; keep it that way.
- feature/thomson-reuters-ross-appeal: the Third Circuit AI-training fair-use
  ruling. No overlap.

## Orchestrator decision (after researcher/01) — corrected facts

The researcher verified the v2 API to code-exact precision against the published
`@opencode/plugin@2.0.22` .d.ts files, the loader source, and the docs (25 sources).
Adopt these corrections as decided:

- Published scope is `@opencode/plugin` / `@opencode/cli` / `@opencode/sdk` /
  `@opencode/client`, all at 2.0.22. `@opencode/cli` 2.0.0 was published to npm
  2026-09-11; `@opencode/plugin` 2.0.0 on 2026-09-12. No GA announcement/release note
  was found: write "published to npm 2026-09-11/12", NOT a vendor "GA" claim.
- Exact v2 shapes:
  - Promise: `export default Plugin.define({ id, setup(ctx): Promise<Cleanup|void> |
    Cleanup | void })`, `Plugin` imported from "@opencode/plugin"; `Cleanup = () =>
    Promise<void> | void`. `define()` is an identity function.
  - Effect: `{ id, effect: (ctx) => Effect<void, never, Scope> }`, imported from
    "@opencode/plugin/effect" (error channel `never`).
  - Dual export (documented): `{ ...Plugin.define({id, setup}), async server() {...} }`.
  - Loader: reads config key "plugins"; globs `{plugin,plugins}/*.{ts,js}`; `import()`;
    validates `default` is `{id, effect}` or `{id, setup}`; Promise plugins wrapped with
    `fromPromise`; a plugin that fails to load is skipped.
  - IMPORTANT: repo source imports "@opencode-ai/plugin/v2/*"; do NOT copy that import
    path — the published, installable path is "@opencode/plugin" (+ "/effect").
- Adoption is real but PARTIAL — do not overclaim:
  - Weekly downloads (2026-09-25→10-01): `@opencode/plugin` 174,464; `@opencode/cli`
    183,569; v1 `@opencode-ai/plugin` 25,688,212. v1 is downloaded ~147x more than v2,
    so v2 has NOT replaced v1 in practice. Say this plainly.
  - "v1 packages remain v1-only" is INEXACT: `@opencode-ai/plugin` 1.18.34 (2026-09-30)
    still ships and also exposes "./v2/effect" and "./v2/promise" subpaths.
  - Eight dated third-party issues/PRs (2026-08-15→10-01) show migration underway; the
    common failure is the load-error about a missing default `{id, effect|setup}`.
- Verified-only vs documented-only: hook names tool/shell/model.request/http.request/
  http.response are confirmed in the .d.ts; prompt/context/compaction/title/generate/
  retry and permission "evaluate" are docs-only. Subdirectory autoload
  (`.opencode/plugins/example/index.ts`) is documented but the loader glob matches only
  direct files — show `.opencode/plugins/example.ts`. The load-error string and the
  "v1 silently skipped under v2" behavior are reported, not source-confirmed. Mark all
  of these as documented/reported, not verified, where the piece uses them.

Revised angle: a walkthrough of the v2 default-export plugin API (Plugin.define with
setup, or the Effect form), published to npm in Sept 2026 and in real but early
migration (v1 still dominates downloads). The reader finishes able to write a minimal
v2 plugin and port a v1 one, with every signature taken from the verified record.
