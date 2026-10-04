# Evidence: OpenCode v2 plugin API (researcher 01)

The record supports every API fact the walkthrough needs at code precision: the two default-export shapes, their exact TypeScript signatures, the loader's validation and load order, the config keys, the hook and domain surface, the documented V1/V2 dual export, and dated adoption evidence from eight third-party repositories. The signatures come from the published `.d.ts` files of `@opencode/plugin@2.0.22` and from the loader source on the repository's default branch (checked out at commit `907b3bc518fa48e90e8ec24dd327d13eee71c36c`, 2026-10-02). The docs examples I could run (Promise, Effect and dual shapes, plus a tool and a hook) type-check under `tsc --strict` against 2.0.22, and the Promise and Effect `define` calls run under Node 22. It is thin in four places: no GA announcement or release-note page for 2.0.0 was found (the date rests on npm publish times), the exact error-text origin in source was not found, the docs say a plugin in a subdirectory of `.opencode/plugins/` autoloads but the loader glob I read matches only direct files, and the commission's claim that v1 packages are "v1-only" is not quite right (see Contradictions).

## Sources

### Package registry (primary, owned by the publisher)

```text
URL:         https://www.npmjs.com/package/@opencode/plugin
Kind:        primary. The publisher's own package page. (npmjs.com returns 403 to scripted fetch, so it is gated, not dead. Data below was read from the registry JSON at https://registry.npmjs.org/@opencode/plugin, the same package's metadata.)
Establishes: name @opencode/plugin; dist-tags latest 2.0.22; 23 stable versions 2.0.0 to 2.0.22; MIT; repository git+https://github.com/anomalyco/opencode.git; exports map; dependencies.
Paraphrase:  2.0.0 was published 2026-09-12T00:15:29Z, 2.0.22 on 2026-10-02T04:22:07Z. Exports: "." resolves to dist/promise/index.js (Promise API), "./effect" to dist/effect/index.js, plus "./tui", "./host" and "./*". Runtime dependencies include effect 4.0.0-rc.112, zod 4.1.8, @opencode/client, @opencode/schema, @opencode/protocol (all 2.0.22). Peer dependencies: solid-js >=1.9.0, @opentui/core >=0.5.14, @opentui/solid >=0.5.14, @opencode/theme 2.0.22.
Locators:    registry JSON: versions["2.0.22"].exports, .dependencies, .peerDependencies; time["2.0.0"], time["2.0.22"]; dist-tags.
Quote:       none
```

```text
URL:         https://www.npmjs.com/package/@opencode/cli
Kind:        primary. Publisher's package page (registry JSON read at https://registry.npmjs.org/@opencode/cli; npmjs.com page gated 403).
Establishes: the v2 CLI package. Bin names "opencode" and "opencode2", both pointing at ./bin/opencode.exe. Latest 2.0.22. 2.0.0 published 2026-09-11T23:44:52Z, the earliest v2 stable timestamp.
Paraphrase:  The package is a launcher that installs a platform binary through optionalDependencies (@opencode/cli-linux-x64-musl and others, all 2.0.22). The plugin loader is in the binary, not in this package.
Locators:    registry JSON: bin, version, time["2.0.0"], optionalDependencies.
Quote:       none
```

```text
URL:         https://www.npmjs.com/package/@opencode/client  and  https://www.npmjs.com/package/@opencode/sdk
Kind:        primary (registry JSON read at registry.npmjs.org/@opencode/client and /sdk; pages gated 403).
Establishes: sibling v2 packages exist. @opencode/client 2.0.22, description "Private generation target for clients derived directly from OpenCode's authoritative Effect `HttpApi`." @opencode/sdk 2.0.22, description "In-process OpenCode host for Promise and Effect applications. The SDK executes Server's assembled HTTP router in memory, opening no listener and adding no network hop." Both 2.0.0 published 2026-09-11 or 2026-09-12 UTC.
Paraphrase:  @opencode/sdk is not a v1-style HTTP client wrapper. By its own description it hosts OpenCode in process.
Locators:    registry JSON: description, time["2.0.0"].
Quote:       the two descriptions above are exact registry strings.
```

```text
URL:         https://www.npmjs.com/package/@opencode-ai/plugin
Kind:        primary (registry JSON read at registry.npmjs.org/@opencode-ai/plugin; page gated 403).
Establishes: the v1 package. Latest dist-tag 1.18.34 (published 2026-09-30T22:41:27Z). 615 stable versions since 0.3.x. Still actively released after v2 GA. It also ships v2 subpaths.
Paraphrase:  1.18.34 exports "./v2/effect", "./v2/promise" and "./v2/effect/plugin" in addition to "." and "./tool". Its "." types still declare the v1 shape: `Plugin = (input: PluginInput, options?: PluginOptions) => Promise<Hooks>` and `PluginModule = { id?: string; server: Plugin; tui?: never }`. v1 1.18.29 (published 2026-09-04T23:47:51Z) is the first release the docs say accepts the object form with server().
Locators:    tarball https://registry.npmjs.org/@opencode-ai/plugin/-/plugin-1.18.34.tgz: package/package.json "exports"; package/dist/index.d.ts, "export type Plugin" and "export type PluginModule"; "export interface Hooks" (line 173 of the unpacked file).
Quote:       none
```

```text
URL:         https://registry.npmjs.org/@opencode/plugin/-/plugin-2.0.22.tgz
Kind:        primary. The shipped artifact. The type declarations are the exact contract.
Establishes: the code-exact Promise and Effect plugin shapes, the context interface, and the hook specs.
Paraphrase:  see "Code-exact shapes" below. dist/promise/plugin.js and dist/effect/plugin.js are each `export function define(plugin) { return plugin; }`, an identity function that exists for typing.
Locators:    package/dist/promise/plugin.d.ts (Context, Cleanup, Plugin, define); package/dist/effect/plugin.d.ts; package/dist/promise/{tool,shell,session,storage,registration,event,command}.d.ts; package/dist/promise/adapter.d.ts; package/dist/options.d.ts.
Quote:       package/dist/promise/plugin.d.ts:
             `export type Cleanup = () => Promise<void> | void;`
             `export interface Plugin { readonly id: string; readonly setup: (context: Context) => Promise<Cleanup | void> | Cleanup | void; }`
             `export declare function define(plugin: Plugin): Plugin;`
             package/dist/effect/plugin.d.ts:
             `export interface Plugin<R = Scope.Scope> { readonly id: string; readonly effect: (context: Context) => Effect.Effect<void, never, R>; }`
             `export declare function define<R = Scope.Scope>(plugin: Plugin<R>): Plugin<R>;`
             package/dist/options.d.ts: `export type PluginOptions = Readonly<Record<string, any>>;`
```

### Documentation (primary, authored by the project)

```text
URL:         https://opencode.ai/v2/docs/build/plugins/
Kind:        primary. The project's v2 plugin guide.
Establishes: the Promise-API default export, the config key and entry forms, the loading locations, lifecycle, domain APIs, hook examples, the manifest for a published plugin, and the V1/V2 dual export.
Paraphrase:  A plugin is a TypeScript module whose default export is `Plugin.define({ id, setup })`. `setup(ctx)` runs on load and may return a cleanup function that runs on unload. Local plugins under `.opencode/plugins/` load automatically. Config lists plugins under the key "plugins" as a package name, a relative or absolute path, a file:// URL, or an object { package, options }. ctx exposes app.version, location (directory, optional workspaceID, project), and options. Domains documented: agent, provider/model, command, integration, mcp, reference, skill, tool, vcs, session, storage, worktree, websearch, generate, permission, event. Hooks: session "prompt", "context", "compaction", "generate", "title", "http.request", "http.response", "retry"; permission "evaluate"; shell "create.before"; tool "execute.before" and "execute.after". Transforms are synchronous and replayed when a registry rebuilds; call the domain's reload() after external inputs change. A published package needs "type": "module", an exports map pointing at the entry, and a dependency on @opencode/plugin.
Locators:    headings "Lifecycle", "Context", "Options", "Transforms", the per-domain API sections, "Publish" (manifest), and the V1 note on the dual export (page tail).
Quote:       "`setup` runs when the plugin loads. It may return a cleanup function that runs when the plugin unloads."
             "The V1 object form is supported in OpenCode 1.18.29. Older V1 releases may expect function exports instead; test the installed package with the oldest V1 release you intend to support and with V2."
             (both read from the rendered HTML of the page; the lines are exact)
```

```text
URL:         https://opencode.ai/v2/docs/build/plugins/effect/
Kind:        primary. The project's Effect plugin guide.
Establishes: the `{ id, effect }` shape, the import path @opencode/plugin/effect, install command, and Scope lifetime.
Paraphrase:  The Effect plugin is imported from "@opencode/plugin/effect" and installed with `bun add @opencode/plugin effect`. Context operations return Effects or Streams, callbacks return Effects, and plugin lifetime is a Scope that closes on reload or unload. Plugin options go under the same "plugins" config key.
Locators:    page intro and first code listing (".opencode/plugins/concise/index.ts"), "Plugin lifecycle", "Publishing".
Quote:       "`@opencode/plugin/effect` is the Effect-native version of the OpenCode plugin API. Its context operations return Effects or Streams, callbacks return Effects, and plugin lifetime is represented by Scope."
Note:        a search-engine snippet of this page showed the text with "@opencode-ai/plugin/effect". The live page says "@opencode/plugin/effect". The package export "./effect" confirms the latter.
```

```text
URL:         https://opencode.ai/v2/docs/build/plugins/migrate-v1/
Kind:        primary. The project's own migration guide.
Establishes: what breaks, the config rename, the entrypoint diff, the V1-hook-to-V2-domain mapping table, and the documented dual export.
Paraphrase:  Config can be normalized automatically but implementation code must be ported. Rename "plugin" to "plugins" and replace the [path, options] tuple with { package, options }. V2 discovers local plugins in both `.opencode/plugin/` and `.opencode/plugins/`, and the guide says to use plugins/ for V2 files. V1 returns one object of tools and hooks. V2 default-exports a definition with id and setup(ctx). Hook callbacks receive one mutable event, not (input, output). V1 tools built with tool() become registrations through the synchronous ctx.tool.transform editor with JSON Schema `input`. Mapping, abridged: tool.execute.before to ctx.tool.hook("execute.before"); shell.env to ctx.shell.hook("create.before"); chat.params to ctx.session.hook("context"); chat.headers to ctx.session.hook("model.request"); chat.message to ctx.session.hook("prompt"); permission.ask to ctx.permission.hook("evaluate"); event to ctx.event.subscribe(); dispose to the cleanup function setup returns. No direct V2 hook exists for experimental.compaction.autocontinue, experimental.provider.small_model, experimental.text.complete, or command.execute.before. The $ Bun shell helper has no V2 equivalent.
Locators:    headings "Migrate plugin configuration", "Replace the entrypoint", "Migrate the context" (table), "Register hooks in setup", "Migrate custom tools", "Migrate events and cleanup", "Support V1 and V2 from one package".
Quote:       "V1 plugin implementations do not run in V2. Moving a file or renaming its config entry is not enough."
             "V1 object entrypoints are supported in OpenCode 1.18.29 and newer. If you support older V1 releases, use separate package versions or entrypoints and test the oldest release you claim to support."
             "Every V2 plugin needs a stable id. Plugin storage is scoped by this ID, and the ID also identifies the plugin in status and diagnostics."
```

### Repository source (primary)

```text
URL:         https://github.com/anomalyco/opencode/blob/907b3bc518fa48e90e8ec24dd327d13eee71c36c/packages/core/src/config/plugin/external.ts
Kind:        primary. The loader that runs in the CLI. (Checked out locally from the public repo at that commit, 2026-10-02. File is 91 lines.)
Establishes: how the CLI discovers, validates and starts a plugin. This is the load path for a diagram.
Paraphrase:  The loader walks config entries. For a config document it reads `entry.info.plugins` (the key is "plugins"); each item is a string or { package, options }. A "file://" item becomes a file path, and "./" or "../" items resolve against the config file's directory. For a config directory entry it globs `{plugin,plugins}/*.{ts,js}` (files directly inside, sorted) and adds each. Absolute paths are imported as file URLs; anything else goes through `npm.add(ref.package)` and uses the returned entrypoint. It then runs `import(entrypoint)` and decodes the module against a schema requiring `default` to be a struct that is either { id: string, effect: function } or { id: string, setup: function }. A value with an "effect" key is used directly; otherwise it is wrapped with PluginPromise.fromPromise. The plugin is registered as { id, effect: (host) => plugin.effect({ ...host, options: ref.options ?? {} }) }, which is how ctx.options gets the config options. Each plugin's load is wrapped in Effect.ignoreCause, so a plugin that fails to import or fails the schema is skipped and does not stop the CLI or the other plugins.
Locators:    lines 15-30 (PluginModule schema), 45-52 (config "plugins" items), 60-67 (directory glob), 78-87 (import, decode, fromPromise, ctx.plugin.add, ignoreCause).
Quote:       line 82: `const plugin = "effect" in value ? value : PluginPromise.fromPromise(value)`
             line 60: `.glob("{plugin,plugins}/*.{ts,js}", {`
Note:        source imports the types from "@opencode-ai/plugin/v2/effect" and "/v2/promise" (workspace names). The published scope for the same code is @opencode/plugin. A writer must not copy the import path from this file.
```

```text
URL:         https://github.com/anomalyco/opencode/blob/907b3bc518fa48e90e8ec24dd327d13eee71c36c/packages/core/src/plugin/promise.ts
Kind:        primary. The Promise-to-Effect adapter.
Establishes: a Promise plugin is run by converting it to an Effect plugin. setup's hook registrations attach to the plugin's scope.
Paraphrase:  fromPromise(plugin) returns define({ id, effect }). Its doc comment: registrations created during async setup attach to the plugin's scope, so unloading disposes them, and the captured fiber context keeps boot-time batching so Promise transforms coalesce into one reload per domain. The same text ships in the published dist/promise/adapter.d.ts.
Locators:    top-of-file doc comment above `export function fromPromise`.
Quote:       "Hook registrations created during the async `setup` attach to the plugin's scope, so unloading the plugin disposes them."
```

### Adoption evidence (third-party repositories; primary for what each author reported)

All were read through the GitHub web pages (a scripted request to github.com returned 403 for one, so I record them as gated and read through a browser-style fetch). Dates are the issue or PR creation dates shown on the page.

```text
URL:         https://github.com/plastic-labs/opencode-honcho/issues/46
Kind:        primary for the report. Issue author is a user (pMertDogan), not the maintainer.
Establishes: dated v1 plugin failing under v2.
Paraphrase:  2026-09-21. @honcho-ai/opencode-honcho 0.1.4 declares @opencode-ai/plugin ^1.18.23 and fails to load on @opencode/cli 2.0.12 (Node 22.23.2, Windows 11) with "Plugin must export a default definition with an id and an effect or setup function." Closed, linked to PR #50.
Locators:    issue body; state Closed.
Quote:       "Plugin must export a default definition with an id and an effect or setup function."
```

```text
URL:         https://github.com/zzet/gortex/issues/830
Kind:        primary for the report (author HonzaTuron, a user of the tool).
Establishes: the same error on OpenCode 2.0.15, and the failure being silent.
Paraphrase:  2026-09-28. Gortex v0.64.5 generates a V1-style hook-object plugin; under OpenCode v2.0.15 on macOS arm64 the plugin does not load, so its deny, enrich, nudge and session-briefing hooks go inactive while its MCP tools still work. The host logs a warning only. Open. Linked PR #852.
Locators:    issue body, "Error" block.
Quote:       "Plugin must export a default definition with an id and an effect or setup function. (cause: SchemaError(Missing key at [\"default\"]))"
```

```text
URL:         https://github.com/zzet/gortex/pull/852
Kind:        primary (author zzet is the Gortex repository owner, as shown on the page).
Establishes: a real shipped-style dual export in one file with no @opencode/plugin dependency.
Paraphrase:  2026-10-01. "fix(opencode): load the bridge plugin under OpenCode 2". Exports a single dependency-free definition that works on OpenCode 1.18 and 2.0.21. V2 gets { id, setup } and registers hooks on tool, permission and session domains. V1.18 keeps the classic server(input). State at read time: Open, not merged.
Locators:    PR description.
Quote:       `export default { id: "gortex", setup, server };`
```

```text
URL:         https://github.com/zzet/gortex/pull/851
Kind:        primary (author elazar; the maintainer's review comments are on the page).
Establishes: pitfalls in a first dual-port attempt, stated by the maintainer.
Paraphrase:  2026-10-01. Open, superseded by #852. The maintainer listed three problems: a fallback that exported undefined as default when @opencode/plugin could not be resolved, which OpenCode 1.18 rejected; field names read from v2 events that do not exist (the page says the PR used event.callID and event.output where the real fields are event.id and event.result); and an unneeded dependency, since @opencode/plugin is only `export function define(plugin) { return plugin; }`. The last point matches dist/promise/plugin.js in 2.0.22.
Locators:    maintainer review comments.
Quote:       none
```

```text
URL:         https://github.com/code-yeongyu/oh-my-openagent/issues/8489
Kind:        primary for the report (author tegarkalam). curl to this URL returns 403, so it is gated; WebFetch read it.
Establishes: a large plugin incompatible with v2, with its author's list of required changes.
Paraphrase:  2026-09-19. Closed. oh-my-openagent v4.19.4 and v5.0.0-beta.78 fail to load on v2. The issue lists the changes: move from @opencode-ai/plugin to @opencode/plugin, convert (input, output) hook signatures to mutable event drafts, replace ctx.client.* with domain APIs, move tool definitions to JSON Schema plus editor.add(), refactor the TUI entrypoint. It states there is no workaround and users stay on v1 until migration. It describes the V1 default export as `{ id: "oh-my-openagent", server: serverPlugin }`.
Locators:    issue body, "Critical API Shape Changes".
Quote:       none
```

```text
URL:         https://github.com/JochenYang/opencode-vision/issues/5
Kind:        primary for the report (author morpheus9393).
Establishes: a port request that names concrete mappings.
Paraphrase:  2026-09-26. Open. Maps tool.definition to ctx.tool.transform(), chat transforms to ctx.session.hook("context"), v1 FilePart.url base64 to a v2 MediaPart, and Bun globals to Node fs. Calls the port "mostly mechanical".
Locators:    issue body, "Migration Requirements".
Quote:       none
```

```text
URL:         https://github.com/TejasS1233/opencode-parser/pull/2
Kind:        primary (a merged change; contributor okhiroyuki, merged by repo owner TejasS1233, as shown).
Establishes: a merged real port that keeps both versions in one package.
Paraphrase:  2026-09-29. Merged. Replaced the @opencode-ai/plugin dependency with @opencode/plugin, added a Plugin.define entry whose setup registers a parse tool through ctx.tool.transform, and kept the v1 tool alongside. README split: v1 users keep the "plugin" config key, v2 users use "plugins".
Locators:    PR description, "API Migration" and "Configuration".
Quote:       none
```

```text
URL:         https://github.com/shekohex/opencode-pty/issues/55
Kind:        primary for the plan (author DanRioDev).
Establishes: a migration begun during the v2 beta, before GA.
Paraphrase:  2026-08-15. Closed with PR #59. Plans to keep the V1 entry point and add a separate V2 export; v1 dependency was @opencode-ai/plugin 1.3.13. Validation criterion: the plugin appears in `opencode2 api get /api/plugin`.
Locators:    issue body, "Proposed Migration Approach".
Quote:       none
```

```text
URL:         https://api.npmjs.org/downloads/point/last-week/@opencode/plugin  (and /@opencode/cli, /@opencode-ai/plugin)
Kind:        primary. npm's own download counter. The response is the exact reading.
Establishes: usage signal for the window 2026-09-25 to 2026-10-01.
Paraphrase:  @opencode/plugin 174,464; @opencode/cli 183,569; @opencode-ai/plugin 25,688,212. The v1 plugin package is downloaded about 147 times as often as the v2 one in that week.
Locators:    JSON "downloads", "start", "end".
Quote:       none
```

```text
URL:         https://github.com/anomalyco/opencode/releases
Kind:        primary. The project's release list.
Establishes: v1 continued shipping after GA. Releases listed: v1.18.25 (2026-08-28) through v1.18.34 (2026-09-30), including 1.18.29 (2026-09-04).
Paraphrase:  The listed releases are all 1.18.x. The page I read did not show 2.0.x release notes or a GA post. v2 versions appear on npm only.
Locators:    release list.
Quote:       none
```

## Code-exact shapes (for the writer)

Verified against `@opencode/plugin@2.0.22` declarations. Each snippet below type-checked under `tsc --strict --module nodenext` against that version with effect 4.0.0-rc.112. The Promise and Effect `define` calls also ran under Node 22.22.0 and returned `{ id, setup }` and `{ id, effect }` unchanged.

Promise API, default export `{ id, setup }`:

```ts
import { Plugin } from "@opencode/plugin"

export default Plugin.define({
  id: "example",
  async setup(ctx) {
    await ctx.storage.set("loaded", true)
  },
})
```

Effect API, default export `{ id, effect }`:

```ts
import { Plugin } from "@opencode/plugin/effect"
import { Effect } from "effect"

export default Plugin.define({
  id: "example",
  effect: (ctx) =>
    Effect.gen(function* () {
      const storage = ctx.storage
      yield* storage.set("loaded", true)
    }),
})
```

Minimal tool plus hook, Promise API (from the docs "Tools" and "Tool Hooks" sections and the migration guide; type-checks):

```ts
import { Plugin } from "@opencode/plugin"

export default Plugin.define({
  id: "greeting",
  async setup(ctx) {
    await ctx.tool.transform((editor) => {
      editor.add({
        name: "greeting",
        description: "Create a greeting",
        input: {
          type: "object",
          properties: { name: { type: "string" } },
          required: ["name"],
          additionalProperties: false,
        },
        async execute(input) {
          return { content: `Hello ${(input as { name: string }).name}!` }
        },
      })
    })
    await ctx.tool.hook("execute.before", (event) => {
      console.log(event.tool)
    })
  },
})
```

Dual V1/V2 export (migration guide, "Support V1 and V2 from one package"; type-checks):

```ts
import { Plugin } from "@opencode/plugin"

export default {
  ...Plugin.define({
    id: "example",
    async setup(ctx) {
      await ctx.tool.hook("execute.before", () => { console.log("A tool is about to run") })
    },
  }),
  async server() {
    return { "tool.execute.before": async () => { console.log("A tool is about to run") } }
  },
}
```

Facts from the declarations the snippets rely on:

- `setup` receives `Context` and returns `Promise<Cleanup | void> | Cleanup | void`, where `Cleanup = () => Promise<void> | void`.
- `effect` receives the Effect-flavored `Context` and returns `Effect.Effect<void, never, R>`, with `R` defaulting to `Scope.Scope`. The error channel is `never`, so a plugin must handle its own failures.
- `Context` members (both flavors): app, location, options, agent, aisdk, command, event, experimental.terminal, integration, mcp, model, generate, permission, plugin (only list), provider, reference, rpc, session, shell, skill, storage, tool, vcs, websearch, worktree.
- Hook registration type: `Hooks<Spec> = (name, callback: (input) => Promise<void> | void) => Promise<Registration>`, and `Registration = { dispose(): Promise<void> }`. Transform type: `Transform<Input> = (callback: (input: Input) => void) => Promise<Registration>`. Transform callbacks are typed synchronous, as the docs say.
- Tool hook names in the 2.0.22 `ToolHooks` type: "execute.before" (event fields tool, sessionID, agent, messageID, id, input) and "execute.after" (same fields plus a status of "completed" with result, or "error" with error).
- Shell hook: "create.before" with command, cwd, timeout, shell, env (all mutable).
- Session hooks in `SessionHooks` include "model.request", "http.request", "http.response" and three "experimental.ws.*" hooks; the docs add "prompt", "context", "compaction", "generate", "title" and "retry".
- StorageDomain: get(key), set(key, Schema.Json), remove(key), scan(options), all returning Promises; values must be JSON.
- Plugin ids scope storage (migration guide).

## Contradictions

- Commission says v1 packages "remain v1-only". Not exact. `@opencode-ai/plugin@1.18.34` (2026-09-30) exports "./v2/effect" and "./v2/promise" subpaths, and the v1 line still ships (about 25.7 million downloads in the week to 2026-10-01). The v1 root export is the v1 shape. The writer can say the v1 packages keep the v1 API at their root and are still released, and should not say they carry nothing from v2. Source: registry JSON for @opencode-ai/plugin 1.18.34, package/package.json "exports".
- Commission lists the `{ id, setup }` shape as "promise/async". Confirmed, but the loader converts it to the Effect shape at runtime with `PluginPromise.fromPromise`, so the Effect shape is the one the host runs (external.ts line 82; promise.ts doc comment).
- Docs say a plugin at `.opencode/plugins/example/index.ts` "loads automatically" (the docs listing is headed with that path). The loader glob read at commit 907b3bc is `{plugin,plugins}/*.{ts,js}`, which matches `.ts` or `.js` files directly in the directory, not `example/index.ts`. I could not find which code path loads a subdirectory entrypoint. For code the writer should show, use a direct file (`.opencode/plugins/example.ts`) or a config "plugins" entry, both of which the source supports, and say the subdirectory form is documented but not confirmed in the loader file I read.
- The repository's workspace imports use "@opencode-ai/plugin/v2/effect" while the published packages use "@opencode/plugin". Not a conflict in the API, but copying import paths from source would be wrong.
- Gortex PR #851 vs the docs: #851's maintainer says the V1 fallback must not default-export undefined, and the docs' dual shape works because both keys live on one object. Consistent, and a reason to show the docs shape.
- Doc discrepancy with source for the config key: the migration guide says V1 uses "plugin" and V2 "plugins". Source reads `entry.info.plugins` only for config documents. Consistent.

## Numbers

```text
Figure: @opencode/cli 2.0.0 published 2026-09-11T23:44:52Z; @opencode/plugin 2.0.0 published 2026-09-12T00:15:29Z (UTC)
Owner:  npm registry JSON, time["2.0.0"] on each package
Scope:  first stable version of each package. The two timestamps straddle midnight UTC, so the GA date is 2026-09-11 for the CLI and 2026-09-12 for the plugin package.
```

```text
Figure: latest versions 2.0.22 for @opencode/plugin, @opencode/cli, @opencode/sdk, @opencode/client; 23 stable versions each (2.0.0 to 2.0.22) in 21 days (2026-09-11 to 2026-10-02)
Owner:  npm registry JSON, dist-tags and versions
Scope:  registry state read 2026-10-04
```

```text
Figure: 2.0.22 publish times: @opencode/plugin 2026-10-02T04:22:07Z; @opencode/cli 2026-10-02T04:21:16Z
Owner:  npm registry JSON, time["2.0.22"]
Scope:  latest dist-tag at read time
```

```text
Figure: weekly downloads: @opencode/plugin 174,464; @opencode/cli 183,569; @opencode-ai/plugin 25,688,212
Owner:  npm downloads API https://api.npmjs.org/downloads/point/last-week/<package>
Scope:  7 days, 2026-09-25 to 2026-10-01; counts every install including CI and mirrors, not unique developers
```

```text
Figure: v1 @opencode-ai/plugin: 1.18.28 (2026-09-04T15:38Z), 1.18.29 (2026-09-04T23:47Z), 1.18.30 (2026-09-09T03:35Z), 1.18.34 (2026-09-30T22:41Z)
Owner:  npm registry JSON for @opencode-ai/plugin
Scope:  shows v1 continuing after v2 GA; 1.18.29 is the first version the docs say supports the object form with server()
```

```text
Figure: dated migration items: 2026-08-15 (pty #55), 2026-09-19 (oh-my-openagent #8489), 2026-09-21 (honcho #46), 2026-09-26 (opencode-vision #5), 2026-09-28 (gortex #830), 2026-09-29 (opencode-parser PR #2, merged), 2026-10-01 (gortex #851, #852)
Owner:  each GitHub page
Scope:  eight repositories with ids I opened; this is a sample, not a count of all migrations. The GitHub search page for the main repo lists "V2:" issues from 2026-10-03 and 2026-10-04 (#53025, #53039, #53047, #53049, #53074), which show v2 in use but are not plugin-specific.
```

## Limits

- No GA announcement, blog post or 2.0.0 release note was found. The only GA evidence is the npm publish times of 2.0.0. The commission's "GA 2026-09-11" holds for @opencode/cli, and the plugin package's 2.0.0 is 31 minutes into 2026-09-12 UTC. The writer should say "published to npm on 2026-09-11" for the CLI, and should not quote a vendor announcement.
- The error string "Plugin must export a default definition with an id and an effect or setup function" appears in three issues (honcho #46, gortex #830, oh-my-openagent #8489) but I did not find it in the source I checked out (a repo-wide grep over packages/ returned no match). Its origin is unconfirmed. The `Missing key at ["default"]` suffix is consistent with the schema decode in external.ts.
- The loader (external.ts) ignores a failed plugin through `Effect.ignoreCause`. I did not read what it logs. Gortex #830 says the host logs a warning. The warning text and level are unverified.
- The docs say `.opencode/plugins/<name>/index.ts` loads automatically. The glob I read matches only direct files. The subdirectory loading path is unverified (see Contradictions).
- `npm.add(ref.package)` resolves packages named in config. Its version-selection behavior (latest, pinned, cache location) was not read.
- The full per-domain event types (for example the `ctx.event.subscribe` event union, the Tool.Info input and result schema, the Session "prompt"/"context"/"retry" types beyond the ones in the 2.0.22 d.ts excerpts I read) were not each verified field by field. Verified field by field: Plugin, Context, Cleanup, Registration, Transform, Hooks, ToolHooks, ShellHooks, StorageDomain, SessionHooks key names, CommandDefinition. The tool `editor.add` example type-checked as written, which confirms `name`, `description`, `input` and `execute` returning `{ content }`, but I did not enumerate every optional field.
- Hook names from the migration table such as "evaluate" (permission), "prompt", "context", "compaction", "title", "generate", "retry" are taken from the docs. Only the tool, shell and session "model.request", "http.request", "http.response", "experimental.ws.*" names were confirmed in d.ts. Show the docs-only ones only with the docs as the citation.
- Whether the plugin command loads "plugin" from a v1 config under v2 is not established. The migration guide says plugin configuration "can be normalized automatically". Source reads only "plugins" in external.ts.
- Behavior when a v1 plugin loads under v2: the evidence is the three reports above (silent skip with a warning). I did not run OpenCode 2 myself. The `opencode2` binary is a platform executable I did not execute.
- Download counts are npm totals and do not separate CI or mirror traffic. The ratio of v1 to v2 downloads suggests v1 is still the larger install base, which cuts against any claim that v2 has replaced v1.
- The TUI plugin entrypoint ("@opencode/plugin/tui", CLI plugins) was not examined beyond the export map.
- The Gortex PRs #851 and #852 were open at read time. #852's final merged shape is not established.

## Source assets

None found. The docs and issues are text and code; the one candidate, the load path, is mechanism in source, not a visual in a document. A diagram of the load path can be built from external.ts lines 45-87: config "plugins" entries and `{plugin,plugins}/*.{ts,js}` files, then `npm.add` or file URL, `import()`, schema check on `default`, `fromPromise` if `setup`, `ctx.plugin.add` with options merged.

## Discarded

```text
https://byteiota.com/?p=23892: surfaced in search, not read; secondary coverage cannot own an API claim, and primaries were available.
https://www.mintlify.com/anomalyco/opencode/sdk/plugin-api: surfaced in search, not read; third-party mirror of docs of unknown version, and the v2 docs are first party.
https://learnopencode.com/5-advanced/12a-plugins-basics.html: surfaced in search, not read; third-party tutorial, likely v1.
https://opencode.ai/docs/plugins: read; this is the v1 plugin page (named export `async ({ project, client, $, directory, worktree }) => hooks`, `import type { Plugin } from "@opencode-ai/plugin"`, config key "plugin"). Used only to show the v1 before. Its text contains no v2 claims.
https://v2.opencode.ai/build/plugins and https://v2.opencode.ai/build/plugins.md: 404 / redirect to a 404; the working canonical pages are under https://opencode.ai/v2/docs/build/plugins/.
https://www.npmjs.com/package/@opencode/plugin (direct): 403 to scripted fetch; the registry JSON and tarball were used, and the npm page is recorded above as the canonical page.
https://github.com/Karnak19/fouine/issues/141 and https://github.com/joshuadavidthomas/opencode-handoff/issues/33: surfaced in search, not opened; the eight read items already cover the claim.
https://letsdatascience.com/news/opencode-reaches-eight-million-monthly-users-in-one-year-51652538: surfaced in search, not read; secondary user-count claim that does not concern the plugin API.
```
