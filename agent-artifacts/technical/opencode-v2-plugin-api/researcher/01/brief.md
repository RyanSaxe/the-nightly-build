# researcher brief: technical/opencode-v2-plugin-api (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md)

Output: ./evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive
for background. Where something you need is missing, ask me.

Establish, from primary sources (the OpenCode v2 docs, the published npm packages,
and the repository source/release notes), the exact current shape of the v2 plugin
API so a writer can show correct, runnable code:

1. The GA date and version lineage: when v2 went GA, current `@opencode/*` versions
   (e.g. `@opencode/plugin`, `@opencode/cli`, and any `@opencode/sdk`/`@opencode/client`),
   and the status of the v1 `@opencode-ai/*` packages. Record exact package names and
   a representative version string each, with the npm page URL (primary).
2. The v1 plugin shape: how a v1 plugin was declared (the named export / hooks
   object) — enough to show the before.
3. The v2 plugin shape, verified against the docs/source: that a plugin is a default
   export of either `{ id, setup }` (promise/async) or `{ id, effect }` (Effect API).
   Confirm the exact field names and the signatures: what `setup`/`effect` receive
   (the context/hook object), what they return, and which hooks/events a plugin can
   handle. Quote the authoritative doc/source lines where wording is the evidence,
   with locators (file path + section/heading or line).
4. How the CLI discovers and loads a plugin (config entry, package, directory) —
   enough to describe the load path in a diagram.
5. Adoption evidence that this is in use, not a pitch: name specific community
   plugins migrating to v2, with dated GitHub issues/PRs or release notes (primary),
   and any download/usage signal. This grounds the "recent and in use" requirement.
6. Migration specifics: what breaks when a v1 plugin loads under v2, and the minimal
   diff to port. If a dual v1/v2 adapter pattern exists in the wild, confirm it with
   a real source.

Build the evidence record sections (Sources, Contradictions, Numbers, Limits, Source
assets, Discarded). Reach the `article` floor of 8 sources, favoring primaries (docs,
npm, repo, release notes, real issues/PRs). For any API detail you cannot confirm
against a primary, record it under Limits so the writer states the uncertainty rather
than inventing a signature.

Confirm every URL resolves (403/paywall = gated, not dead; record the canonical
page). Report the record's most important limit — above all, any part of the v2 API
shape you could NOT verify to code-exact precision.
