# Evidence: expert-tools/serena (invocation 01)

The evidence strongly supports the commission's core claim: Serena is an open-source
MCP server that gives a coding agent symbol-level, LSP-backed retrieval and editing
(find_symbol, find_referencing_symbols, replace_symbol_body, and symbolic insert/rename/
safe-delete) in place of grepping and reading whole files, and it enters the workflow by
being registered as an MCP server in the client's launch config. The exact run-as-server
config and a verbatim symbol-operation contract (with parameters and the `MyClass/my_method`
name-path locator) are both captured from primary sources. Maintenance is strong (27.4k
stars, ~3,200 commits, releases through v1.6.1 on 2026-07-21, an active `main`). The record
is thin in exactly one honest place, and it is the most important line for the writer: the
*default, free* language-server backend is materially less capable than Serena's headline
feature list implies. The marquee refactorings (move, inline, propagate deletions), type
hierarchy, and dependency search exist **only in the paid JetBrains plugin**; the LSP
backend's rename is symbol-only, find-implementations is language-dependent, and
find-declaration fails on external dependencies. Adoption cost is real: per-language
toolchain dependencies, multi-minute first indexing on large repos, and setup friction that
one independent reviewer put at ~30 minutes per new project. Contradictions section is
populated (language count, config-command drift across guides), so the writer should cite
config to the official docs, not third-party tutorials — the README itself warns those are
wrong.

## Sources

```text
URL:         https://github.com/oraios/serena
Kind:        primary — the project's own repository; owns all claims about what Serena is and does
Establishes: identity ("A powerful MCP toolkit for coding, providing semantic retrieval and
             editing capabilities - the IDE for your agent"), MIT license, and maintenance
             signals: 27.4k stars, 1.8k forks, 3,216 commits on main, 62 open issues,
             45 open PRs, owner org "oraios". A "Sponsor this project" affordance is present.
Paraphrase:  Serena is an actively maintained, MIT-licensed MCP toolkit by the oraios org that
             adds IDE-like semantic code tools to any MCP client.
Locators:    Repository landing page, "About" sidebar and header counters (read 2026-08-03).
```

```text
URL:         https://raw.githubusercontent.com/oraios/serena/main/README.md
             (source's own page: https://github.com/oraios/serena/blob/main/README.md)
Kind:        primary — the maintainers' README
Establishes: (1) What Serena is: "semantic code retrieval, editing, refactoring and debugging
             tools ... operating at the symbol level"; integrates "with any client/LLM via the
             model context protocol (MCP)". (2) Two backends: "Language servers implementing the
             language server protocol (LSP) — the free/open-source alternative which is used by
             default" and "The Serena JetBrains Plugin ... (paid plugin; free trial available)".
             (3) Support for "over 40 programming languages" with the full list. (4) The
             capability matrices splitting LSP vs JetBrains coverage (see Numbers/Contradictions).
             (5) Install path: `uv tool install -p 3.13 serena-agent`, then `serena init`.
             (6) An explicit warning against marketplace install commands.
Paraphrase:  The README is the canonical statement of scope, backends, language list, and install
             flow, and it draws the exact line between free LSP features and paid JetBrains ones.
Locators:    lines 17-19 (scope), 27-29 (marketplace warning), 100-103 (two backends),
             112-113 ("over 40" + language list), 141-176 (Retrieval/Refactoring/Symbolic Editing
             tables), 184-202 (basic tools + memory), 228-238 (install + init).
Quote:       "Do not install Serena via an MCP or plugin marketplace! They contain outdated and
             suboptimal installation commands." (lines 27-29)
             "Language servers implementing the language server protocol (LSP) — the free/open-source
             alternative which is used by default." (lines 100-101)
```

```text
URL:         https://oraios.github.io/serena/02-usage/030_clients.html
Kind:        primary — maintainers' official client-configuration docs
Establishes: The exact run-as-MCP-server configuration (see "The one concrete example" below):
             the Claude Desktop JSON block, the `claude mcp add` one-liner for Claude Code, the
             per-client `--context` flags, `--project-from-cwd` / `--project`, and stdio vs
             HTTP/SSE transport choice.
Paraphrase:  Clients either launch `serena start-mcp-server` over stdio with a context flag, or
             connect to a separately started HTTP/SSE server URL.
Locators:    "Clients" usage page: Claude Desktop JSON section, Claude Code command, transport modes.
```

```text
URL:         https://raw.githubusercontent.com/oraios/serena/main/src/serena/tools/symbol_tools.py
             (source's own page: https://github.com/oraios/serena/blob/main/src/serena/tools/symbol_tools.py)
Kind:        primary — the tool implementations; the docstrings ARE the tool descriptions the agent sees
Establishes: The verbatim tool contracts for the writer's example: find_symbol's name-path
             semantics and parameters, find_referencing_symbols' parameters and behavior, and
             replace_symbol_body's contract. Also documents the fuller tool set (get symbols
             overview, find implementations/declaration, get diagnostics, insert before/after,
             rename, safe delete).
Paraphrase:  find_symbol matches a symbol-tree "name path" (e.g. MyClass/my_method), optionally
             returning bodies and locations; find_referencing_symbols returns referencing symbols
             with a code snippet around each reference; replace_symbol_body swaps a symbol's whole
             definition. These are the primitives that replace grep + whole-file reads.
Locators:    class FindSymbolTool (def apply lines 144-193, name-path doc 162-172);
             class FindReferencingSymbolsTool (apply 260-278);
             class ReplaceSymbolBodyTool (apply 590-607); GetSymbolsOverviewTool 36-91;
             InsertAfterSymbolTool 618-641; RenameSymbolTool 670-695; SafeDeleteSymbol 698-738.
Quote:       "A name path is a path in the symbol tree *within a source file*. For example, the
             method `my_method` defined in class `MyClass` would have the name path
             `MyClass/my_method`." (lines 162-163)
             "IMPORTANT: Only replace symbol bodies if you have previously made a retrieval with
             include_body=True and thus know what constitutes the body!" (lines 599-600)
```

```text
URL:         https://raw.githubusercontent.com/oraios/serena/main/CHANGELOG.md
             (source's own page: https://github.com/oraios/serena/blob/main/CHANGELOG.md)
Kind:        primary — maintainers' changelog
Establishes: Maintenance cadence and depth. Latest tagged release v1.6.1 (2026-07-21); a dense
             "Unreleased (main)" section shows continuous per-language-server fixes (TypeScript
             tsserver race, gopls type/var duplication, Java JDT-LS runtimes, Erlang name/arity,
             Rust rust-analyzer memory), new client support (Grok Build), and a config rename
             (`languages` -> `language_servers`, auto-migrated). Confirms an added minimal,
             no-PII usage telemetry on startup.
Paraphrase:  Development is active and detailed, concentrated on hardening individual language
             servers rather than churn; recent work adds clients and fixes correctness bugs.
Locators:    "# Unreleased (main)" (lines 1-73); "# v1.6.1 (2026-07-21)" (line 76 ff);
             typescript indexing race (lines 52-58); gopls fix (v1.6.1, lines 107-111).
```

```text
URL:         https://github.com/oraios/serena/releases/tag/v1.6.1
Kind:        primary — the release record
Establishes: v1.6.1 exists, tag v1.6.1, dated 2026-07-21, commit bcac096. Confirms the latest
             tagged version underlying the "Unreleased (main)" changelog head.
Locators:    Release page header (title, tag, date, commit).
Note:        Automated curl returns 403 (GitHub gates scripted requests); the page resolves
             normally in a browser and via the markdown-fetch transport. Not dead.
```

```text
URL:         https://oraios.github.io/serena/02-usage/040_workflow.html
Kind:        primary — maintainers' workflow docs
Establishes: Project activation (`--project <path|name>` at launch, or "Activate the project ..."
             in conversation) and the indexing story: `serena project index`, run once in the
             project directory, "pre-caching symbol information provided by the language server(s)"
             for larger projects; thereafter the index auto-updates on file changes. The docs do
             NOT quantify how long first indexing takes.
Paraphrase:  Serena is project-scoped; for big repos you pre-index once, but the docs leave the
             duration unstated (the number comes from the independent review below).
Locators:    "Workflow" usage page: project activation section; "serena project index" section.
```

```text
URL:         https://oraios.github.io/serena/01-about/020_programming-languages.html
Kind:        primary — maintainers' language-support docs
Establishes: Per-language adoption cost. Directly supported with minimal setup: Java, JavaScript,
             TypeScript, Bash, Lua. Require external toolchains: Go ("requires installation of
             gopls"), Rust ("requires rustup"), C/C++ ("provide a compile_commands.json at the
             repository root"), C# (".NET v10+" and "pwsh (PowerShell 7+)"), the Python LSPs
             Pyright/BasedPyright/ty/pyrefly ("require uv/uvx in PATH"), GDScript ("requires the
             Godot editor to be running with its built-in LSP enabled"), Kotlin ("uses the
             pre-alpha official kotlin LS, some issues may appear"). Experimental tier: Angular,
             Ansible, HTML, LaTeX, Markdown, SCSS/Sass/CSS, Solidity, TOML, JSON.
Paraphrase:  "Over 40 languages" is real but tiered: a handful are turnkey, many need a toolchain
             installed, and a cluster is explicitly experimental.
Locators:    "Programming Languages" page: per-language requirement notes; experimental list.
```

```text
URL:         https://oraios.github.io/serena/01-about/035_tools.html
Kind:        primary — maintainers' tool catalog
Establishes: The public one-line descriptions of each tool (find_symbol "Performs a global (or
             local) search using the language server backend."; find_referencing_symbols;
             replace_symbol_body). Parameter detail is in the source (above), not here.
Locators:    "Tools" about page, tool list.
```

```text
URL:         https://modelcontextprotocol.io/docs/concepts/architecture
Kind:        primary — the MCP protocol's own documentation; owns the MCP integration claims
Establishes: MCP is a client-server protocol where an MCP host (e.g., Claude Code, Claude Desktop)
             creates one MCP client per MCP server; servers expose Tools ("Executable functions
             that AI applications can invoke to perform actions"). Two transports: "Stdio transport"
             (local subprocess, "no network overhead") and "Streamable HTTP transport" (remote,
             HTTP POST + optional SSE). This is exactly the two ways Serena's README says to
             connect (launch command vs HTTP URL).
Paraphrase:  MCP defines the tool-exposure and transport model Serena plugs into; Serena is one
             MCP server exposing code tools, reached over stdio or HTTP.
Quote:       "MCP defines three core primitives that servers can expose: Tools: Executable
             functions that AI applications can invoke to perform actions..."
             "Stdio transport: Uses standard input/output streams for direct process communication
             between local processes on the same machine..."
Locators:    "Participants", "Transport layer", and "Primitives" sections.
```

```text
URL:         https://andrew.ooo/posts/serena-mcp-coding-agent-ide-review/
Kind:        secondary — independent hands-on review; author "Andrew" discloses no oraios affiliation
Establishes: Real-usage value and honest friction. Value: a TypeScript-monorepo cross-file rename
             the reviewer reports dropping from ~38K tokens across iterations to ~4K tokens in one
             operation (single-reviewer anecdote, not a benchmark). Costs, in the reviewer's words:
             first-time setup "fiddly" (~30 min per new project); "On a fresh checkout, language
             servers index from scratch. For a large monorepo this can be several minutes.";
             "move, inline, and propagate deletions only exist in the JetBrains backend" (paid);
             install reliability: "I give Claude the URL and 25% of the time it can get Serena
             working. 75% it takes some finagling."
Paraphrase:  An outside practitioner corroborates the token/step savings and, independently,
             the two costs the docs downplay: first-index time and free-vs-paid feature split.
Locators:    Review body: setup section, "limitations"/friction section, monorepo rename example.
Caveat:      This review's config commands (`serena mcp start`, `~/.claude/mcp.json`,
             `--prerelease=allow`) DIVERGE from the current official docs (`serena start-mcp-server`,
             `claude mcp add`); treat the official docs as authoritative for the config snippet
             (see Contradictions).
```

## The one concrete example (verbatim, for the writer)

Two pieces, both from primary sources: the exact config to run Serena as an MCP server, and
the exact symbol-operation contract.

**Run Serena as an MCP server.** Install once (README lines 228-238):

```
uv tool install -p 3.13 serena-agent
serena init
```

Register it with the client. Claude Desktop / desktop-app clients use a JSON block
(030_clients.html):

```json
{
  "mcpServers": {
    "serena": {
      "command": "serena",
      "args": [
        "start-mcp-server",
        "--context=desktop-app"
      ]
    }
  }
}
```

Claude Code uses a single command (030_clients.html):

```
claude mcp add --scope user serena -- serena start-mcp-server --context claude-code --project-from-cwd
```

Transport: stdio by default (the client launches `serena start-mcp-server` as a subprocess);
alternatively start the server in HTTP/SSE mode and give the client the URL. `--project-from-cwd`
activates the current directory as the project; `--project <path>` names one explicitly.
(Source alignment: MCP docs confirm these are precisely the two MCP transports — stdio for a
local subprocess, Streamable HTTP for a remote URL.)

**A symbol operation.** The agent addresses code by *name path*, not by line number. From the
source docstrings (symbol_tools.py):

- `find_symbol` — parameters `name_path_pattern`, `depth`, `relative_path`, `include_body`,
  `substring_matching`, `max_matches`, `include_kinds`/`exclude_kinds`, `max_answer_chars`.
  A name path is "a path in the symbol tree *within a source file*"; the method `my_method` in
  class `MyClass` has name path `MyClass/my_method`. Calling it with
  `name_path_pattern="MyClass/my_method"`, `relative_path="src/foo.py"`, `include_body=True`
  returns the symbol with its location and body — no whole-file read.
- `find_referencing_symbols` — parameters `name_path`, `relative_path` (+ kind filters). Called
  with `name_path="MyClass/my_method"`, `relative_path="src/foo.py"`, it returns each referencing
  symbol plus a `content_around_reference` snippet — replacing a project-wide grep.
- `replace_symbol_body` — parameters `name_path`, `relative_path`, `body`. Called with
  `name_path="MyClass/my_method"`, `relative_path="src/foo.py"`, and the new `body`, it swaps the
  whole definition. Its docstring warns: "Only replace symbol bodies if you have previously made
  a retrieval with include_body=True and thus know what constitutes the body!"

This is the workflow shift in one arc: locate by name path, inspect references semantically,
edit the symbol in place — instead of reading files, grepping, and text-patching.

## Contradictions

- **Language count: "over 40" (primary) vs "20+" (secondary).** The current README (line 112)
  and language-support page say over 40 and enumerate them; multiple third-party writeups and
  aggregators still say "20+ languages." The README is primary and current — the 40+ figure
  reflects recent growth; the 20+ figure is stale secondary reporting. Use 40+, cite the README.
- **Config command drift across guides.** Official docs (030_clients.html) use
  `serena start-mcp-server` with `--context ...` and `claude mcp add --scope user serena --
  serena start-mcp-server --context claude-code --project-from-cwd`. The independent review uses
  `serena mcp start ...` and a `~/.claude/mcp.json` block; older marketplace/tutorial guides use
  a `uvx --from git+https://github.com/oraios/serena serena start-mcp-server` form. The README
  explicitly warns marketplace commands are "outdated and suboptimal." Resolution: the writer's
  one config example must come from the official docs, not from reviews or aggregators.
- **Feature-list optimism vs default-backend reality.** The README's headline "refactoring and
  debugging tools" and the 40-language banner read as fully available, but the same README's own
  capability tables (lines 141-176) show move/inline/propagate-deletions/type-hierarchy/dependency-
  search and interactive debugging are JetBrains-plugin-only (paid), and LSP rename is symbol-only.
  This is internal to the primary source, not a source conflict, but it is the gap most likely to
  mislead a reader; the writer should state the free-backend scope plainly.

## Numbers

```text
Figure: 27,400 stars (27.4k); 1,800 forks (1.8k)
Owner:  github.com/oraios/serena repository counters
Scope:  Cumulative totals as displayed on 2026-08-03.
```

```text
Figure: 3,216 commits on main; 62 open issues; 45 open PRs
Owner:  github.com/oraios/serena
Scope:  Snapshot on 2026-08-03; evidence of active, ongoing development, not a rate.
```

```text
Figure: over 40 programming languages (LSP backend)
Owner:  README, line 112 (full enumerated list follows)
Scope:  Count of languages with a language-server integration; tiered by setup cost and
        experimental status per 020_programming-languages.html. Not a claim of equal quality.
```

```text
Figure: latest tagged release v1.6.1, dated 2026-07-21 (commit bcac096); prior v1.5.3 (2026-05-26);
        v1.0.0 reached "after exactly a year of hard work since the initial release"
Owner:  CHANGELOG.md / releases/tag/v1.6.1
Scope:  Release cadence over 2026; `main` carries a large post-1.6.1 "Unreleased" changelog.
```

```text
Figure: ~38K tokens -> ~4K tokens for one cross-file rename (roughly 10x)
Owner:  andrew.ooo review (SECONDARY, single reviewer, TypeScript monorepo, one task)
Scope:  Anecdotal illustration of token efficiency, not a controlled benchmark. Attribute as
        one reviewer's measurement; do not present as Serena's general or guaranteed number.
```

```text
Figure: first-project setup ~30 minutes; large-monorepo first index "several minutes";
        install success "25% ... 75% it takes some finagling"
Owner:  andrew.ooo review (SECONDARY)
Scope:  One practitioner's experience. The official docs confirm indexing is a one-time pre-cache
        step but give no duration, so these figures are the only concrete cost estimates found
        and must be attributed to the reviewer.
```

## Source assets

```text
Asset: Block diagram, README (resources/serena-block-diagram.svg), rendered under
       "How Serena Works" (README line 79).
Shows: The integration topology the article turns on: MCP client/host -> MCP -> Serena ->
       language server(s)/LSP. Good anchor for "where it enters the workflow."
Crop:  Keep the client -> Serena -> language-server chain and the MCP label; omit surrounding
       README chrome. Do not redraw as decoration.
```

```text
Asset: The three capability matrices in the README (Retrieval / Refactoring / Symbolic Editing),
       README lines 141-176, each a table with "Language Servers" vs "JetBrains Plugin" columns.
Shows: Exactly which features are in the free default backend vs the paid plugin — the single
       most useful piece of furniture for the honest-cost section. This is tabular data, not an
       image; the writer can reproduce it as an HTML table (evidence, not decoration).
Crop:  Preserve the two-column free/paid distinction and the footnotes (* external-dep caveat,
       ** language-limited implementations). Do not drop the JetBrains column — the contrast is
       the point.
```

```text
Asset: Quick-demo video and the 5-minute YouTube intro (README lines 33-35).
Shows: Live tool use in a client. Motion content; usable as a linked reference, not a static crop.
Crop:  None (video). Cite as a link if the writer wants a "see it run" pointer.
```

## Discarded

```text
URL: https://deepwiki.com/oraios/serena — auto-generated wiki (secondary, AI-synthesized); useful
     only as a pointer to source files, which were then read directly. Not cited on its own.
URL: https://skywork.ai/... , https://smartscope.blog/... , https://www.agensi.io/... ,
     https://itecsonline.com/... , https://mcp.directory/... , https://lobehub.com/... ,
     https://mcpservers.org/... , https://crossaitools.com/... , https://alguidelines.dev/... —
     third-party setup/aggregator guides. Rejected for config claims: the README explicitly warns
     such marketplace/tutorial commands are "outdated and suboptimal," and several already carry
     the stale "20+ languages" figure. Not read past search snippets; not cited.
URL: https://github.com/mcp-research/oraios__serena — a mirror, not the source of record.
URL: https://raw.githubusercontent.com/oraios/serena/main/roadmap.md — returned empty (0 bytes);
     no roadmap content to cite.
```
