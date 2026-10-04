# writer brief: technical/opencode-v2-plugin-api (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — angle, boundaries, the original work owed
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md) — the complete, verified API facts; do
  not go beyond it, and do not invent an API signature it does not carry
- recent-patterns.md (../../recent-patterns.md) — recent technical shapes to break
- Template contract + furniture: ../../../../.nb-context/template-contract.yaml and
  ../../../../.nb-context/furniture/engine.md (nb-code, nb-table, nb-figure)

Output:
- The article HTML (edit in place):
  .nb-work/technical/opencode-v2-plugin-api/library/technical/opencode-v2-plugin-api.html
- ./draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/opencode-v2-plugin-api/library/technical/opencode-v2-plugin-api.html --series technical --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive
for background. Where the evidence record cannot supply an exact API detail, ask me —
never invent a signature, package name or version.

This piece's job (confirm or sharpen, then state it in draft-handoff.md): a reader
finishes able to write a minimal working OpenCode v2 plugin and to port a v1 plugin,
with the v2 API surface explained from the source. READ THE "Orchestrator decision
(after researcher/01)" section at the end of commission.md FIRST — it carries the
code-exact, verified facts and several corrections. Non-negotiables from it:
- Use `Plugin.define({ id, setup })` imported from "@opencode/plugin" and the Effect
  form `{ id, effect }` from "@opencode/plugin/effect". Do NOT copy the repo's internal
  "@opencode-ai/plugin/v2/*" import path.
- Do NOT claim a vendor "GA"; say "published to npm 2026-09-11/12."
- Do NOT overclaim adoption: v1 (`@opencode-ai/plugin`, ~25.7M weekly downloads) is
  downloaded ~147x more than v2 (`@opencode/plugin`, ~174k). State plainly that v2 has
  not displaced v1 yet; migration is real but early (8 dated issues/PRs).
- Do NOT say "v1 is v1-only" — v1 1.18.34 still ships and exposes ./v2 subpaths.
- Mark documented-but-unverified details (several hook names, subdirectory autoload,
  the load-error string, "v1 silently skipped under v2") as documented/reported, not
  verified, wherever you use them. Use only signatures the evidence record carries; if
  you need one it does not, stop and ask me rather than inventing.

Specifics:
- Lead with concrete code (nb-code with data-language, a file/context header, a cited
  caption). Label illustrative code as illustrative. Every API name, package name,
  version string and path must match the evidence record exactly.
- Ground "recent and in use" in the dated GA and the record's concrete adoption
  evidence (named migrating plugins, dated issues/PRs) — not vendor adjectives.
- Consider a small nb-table (v1 vs v2 package/export) and a conceptual nb-figure of
  the CLI load path — use each only if it shows more than prose.
- Set nb-meta: series `technical`, slug `opencode-v2-plugin-api`, mode `open`, date
  `2026-10-04`, template `article`; fill harness/model; dek identical to dekline; run
  `nb stamp`.
- Headline/dek per spec/headlines.md: a precise claim with one concrete verifiable
  detail (a package@version or the export shape), no colon-subtitle, no antithesis
  "X not Y" mold (see recent-patterns.md).
- Iterate with `nb check --no-check-links`, then full proof with links until BLOCK: 0.
  Write draft-handoff.md (original-work sentence; proof result + any intentional
  warning; any open question).

Report the handoff path and any warning you left.
