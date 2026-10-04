# Editorial review: technical/opencode-v2-plugin-api (editor/01)

## Correct

Thesis, stated from the draft alone: OpenCode 2's plugin loader accepts a file
whose default export is `{ id, setup }` or `{ id, effect }` and silently skips
anything else, so a v1 plugin (a named export, or an object carrying only
`server`) fails the decode; the piece shows how to write a v2 plugin and port a
v1 one, with every signature taken from the source.

Claims under it:

1. A v2 plugin is the default export of `Plugin.define({ id, setup })` (or the
   Effect form `{ id, effect }`), imported from `@opencode/plugin` and
   `@opencode/plugin/effect`. Held. The two shapes, the `Context` argument, the
   `Cleanup` return, and `define` as an identity function all match the 2.0.22
   `.d.ts` declarations in the record. The reader-facing import is
   `@opencode/plugin` throughout; the repo-internal `@opencode-ai/plugin/v2/*`
   path does not appear anywhere in the article. Checked the loader source href
   (s8) directly: the schema is a union of `{ id, effect }` and `{ id, setup }`
   and the glob is `{plugin,plugins}/*.{ts,js}`, exactly as printed.

2. The loader decodes `default` against that schema, wraps a `setup` plugin with
   `PluginPromise.fromPromise`, runs every plugin as the Effect shape, and skips
   a failure under `Effect.ignoreCause`. Held against s8/s9. The figure (checked
   against the record and rendered) reproduces this path without adding anything
   the source does not show; its caption is a factual, cited label and keeps the
   interpretation out.

3. Adoption is real but early, and v2 has not displaced v1. Held. Downloads
   (174,464 v2 plugin vs 25,688,212 v1, ~147:1) recompute from s7, which I
   opened and which returns exactly those figures for 2026-09-25 to 2026-10-01.
   The piece says plainly that v1 is installed about 147 times as often and
   keeps shipping (1.18.34). No vendor "GA": it says "published to npm" on
   2026-09-11/12 and states that no 2.0.0 release note was found. Eight dated
   items across six repositories, each with its state shown; "a sample, not a
   count" is stated.

Tried to break the hardest claim — that a v1 plugin is skipped — since the
binary was not run. The piece does not overreach: it derives the skip from the
loader schema and attributes the observed behavior (silent skip, a warning only,
MCP tools surviving) to three named user reports, and says the binary was not
run. The load-error string, the subdirectory autoload, the host warning, and the
docs-only hook names (`prompt`, `context`, `compaction`, `generate`, `title`,
`retry`, permission `evaluate`) are each marked documented or reported, not
verified, where used — in the prose, the hook table's Evidence column, and the
migration table's third column. The commission's inexact "v1-only" claim is
correctly handled: the piece says the v1 package keeps the v1 shape at its root,
still ships, and exposes `./v2/*` subpaths.

Headline, dek and subheads: every version string, package name, date, export
shape and figure in them checks against the record. The dek attributes the
decode to "OpenCode 2.0.22" as a reader-facing summary; the accepted shapes are
the 2.0.22 declarations and the decode is the loader's behavior, and the body
and figure caption carry the exact commit provenance (907b3bc), so this is a
summary, not an overclaim. Every `data-nb-kind` is `primary`: the npm registry,
tarballs, docs and repository source are the publisher's own, and each
third-party issue or PR is primary for what its author reported, which is how the
article cites them.

Opened citation hrefs as printed. Verified by fetch that each lands on the cited
content: s2 (migrate-v1, the "do not run in V2" line and the dual-export
section), s3 (v2 plugins, `Plugin.define({ id, setup })` and the cleanup line),
s8 (external.ts at 907b3bc, the union schema and the glob), s11 (effect docs,
the `@opencode/plugin/effect` import and the quoted line), s12 (the v1 page, with
the v2 banner — correctly used for the "before"), s7 (the 174,464 figure), s10
(gortex 830, the error and the inactive-hooks report), s16 (gortex PR 852, the
`{ id, setup, server }` export and the 1.18/2.0.21 claim). The remaining hrefs
match the record's URLs exactly and passed the proof's link resolver.

One break, minor and fixed: the first code caption claimed the snippet
type-checks under `tsc --strict`, but the record verified all snippets under
`tsc --strict --module nodenext`, and the import resolves through an exports map
where the module-resolution flag is load-bearing for reproduction. Aligned the
caption to the verified invocation (and to the Effect caption, which already
carried it).

## Reads well

Nothing was cut. The prose is in the voice guide's register: a snippet appears,
then the paragraph reads it back part by part; terms (plugin, hook, tool,
domain, context) are glossed once where first met and then used by one name; the
checked/documented line is drawn in plain attributions ("the docs say", "the
type declaration shows", "was not read"). I ran the placeholder test on the
edges — the first and last sentence of each paragraph and section, and the
article's last line. Each survivor depends on its nouns: "That file is a complete
OpenCode 2 plugin", the downloads sentences, and the closer naming
`opencode2 api get /api/plugin` as a check that does not depend on the log all
reduce to nothing when the nouns are removed. No empty conclusion, no performed
carefulness, no puffery, no reach for the generic. The limitation phrasings
("was not read", "was not exercised here", "for this article") are honest
qualifications the voice guide asks for, not self-promotion, so they stay.

Checked against the recent record for repetition. The headline avoids the
antithesis "X not Y" mold and the paired "X binds a Y / First use turns the Y
into the Z" heading rhythm flagged in recent-patterns; the six headings are built
from this piece's own nouns with varied grammar, and a skim of them alone
reconstructs the argument in order. No dek built from negative parallelism, no
comma-triad heading. Nothing ran flat enough to need lifting.

## The experience

Read the rendered page from the top. The code-first opening, the load-path
figure, the v1/v2 contrast table, the hook-evidence table, the dual-export diff
and the download table each show something faster than prose would, and none
plots more than the record supports. The figure earns its place: it collapses a
91-line loader into one legible path and is labelled conceptual. What the piece
gives beyond its sources: it reads the loader source, the 2.0.22 declarations and
eight scattered migration reports against each other to say exactly which default
exports pass the check, what happens to those that fail, and the smallest diff
that carries a v1 plugin across — which no single source states in one place.
That matches the original-work sentence in the handoff, and it survives.

## Edits

- First code caption: `tsc --strict` changed to `tsc --strict --module nodenext`,
  to match the record's verified invocation and the Effect caption.

## Decision

approve — correct against the evidence record, in the voice guide's register,
and giving the reader a synthesis no single source holds; the one break found was
a caption imprecision, now fixed, with the proof at BLOCK: 0.
