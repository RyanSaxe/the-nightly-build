# Evidence record: dbt v2.0 Rust engine (researcher 01)

Fetched 2026-10-02. The primary record supports the commission's mechanism and also
changes it in three ways the writer must carry. (1) The compile-time column and
reference checking is real, but it is the "static analysis" engine, and that engine
is NOT in the Apache 2.0 build. It ships only in the `dbt` distribution under a
proprietary dbt product license. The Apache 2.0 build is called dbt OSS (formerly
"dbt Core v2"), and it does not do the column check. (2) The default mode
(`baseline`) did not catch a misspelled column in my run. Only `--static-analysis
strict` did. (3) dbt Labs' headline "up to 10x" speed claim is stated for a
10,000-model project, but the same company's own GA post reports 70 s to 17 s
(about 4x) for a 10k-node compile, and "2x or more" for normal projects. I ran a real
local test with dbt-duckdb-in-v2, so the worked example is reproducible; those
outputs are recorded below as my own run. Independent adoption evidence is thin:
one merged dbt Labs agent-skills PR carrying a practitioner's migration lessons,
plus commentary articles, mostly not first-hand. No independent speed reproduction
other than mine was found.

Naming warning for the writer: the commission says "dbt Core v2.0 ... 'Fusion' ...
under Apache 2.0." At GA (16 Sep 2026) dbt Labs renamed things. Fusion became
"dbt" (v2). "dbt Core v2" became "dbt OSS". See Contradictions.

## Sources

### 1
URL:         https://docs.getdbt.com/blog/dbt-v2-is-ga
Kind:        primary. dbt Labs dev blog, written by dbt Labs staff, owns the GA, speed and static-analysis claims and has a stake in them.
Establishes: firsthand: GA date, the 70 s / 17 s benchmark, the description of static analysis, install options.
Paraphrase:  Post by Joel Labes, Staff Developer Experience Advocate at dbt Labs, dated September 16, 2026. States the Fusion engine "graduated into General Availability under its new name: dbt." Lists v1 problems: dbt did not understand the SQL it generated, parse times "as long as 20 minutes" on very large projects, giant JSON artifacts. Static analysis: a local SQL compiler produces a logical plan, validates sources, UDFs, seeds, vendor functions, and detects invalid column references, function signatures and argument types before warehouse execution. Two modes named: `baseline` (default for existing projects) and `strict`. Speed section gives the benchmark in Numbers. Install: `brew install dbt`, winget, curl installer with `dbt system update`, or `pip install dbt`.
Locators:    section "The biggest new features" > "Find your (and your agents') mistakes faster" and "Speed"; section "Installation instructions".
Quote:       "In some ways, dbt's static analysis is even more capable than the system built into your warehouse itself. Your warehouse can only evaluate the single query in front of it at any given moment; dbt knows that despite a query remaining valid on its own after removing a column, it would break 4 downstream models when deployed."
Quote:       "My benchmarking project with 10k nodes takes 70 seconds to compile on dbt 1.12.0, and just 17 seconds on dbt v2."
Note:        Also says performance gains need the new artifact formats (`--no-write-json`, `--write-index`) and dbt State needs `--manage-state`. It points to a separate post on dbt vs dbt OSS and does not itself say which distribution holds static analysis.

### 2
URL:         https://docs.getdbt.com/blog/comparing-dbt-and-dbt-oss
Kind:        primary. dbt Labs, same author, owns the distribution and licensing boundary.
Establishes: firsthand: what is and is not in the Apache 2.0 build.
Paraphrase:  Dated September 16, 2026 (Joel Labes). Two distributions: dbt (formerly dbt Fusion engine), the default, and dbt OSS (formerly dbt Core v2), "the Apache 2.0 open source subset." Both free and locally installable. Comparison table: "Advanced local features for free (SQL comprehension, linting, dbt LSP support)" is a check for dbt and a cross for dbt OSS. "100% Apache 2.0 open source" is a cross for dbt and a check for dbt OSS. Seat-based paid features (dbt Mesh, dbt Catalog) are only in dbt. Usage-based paid features (dbt State, dbt Wizard) are supported in both. dbt contains proprietary code alongside Apache code, needs no login or payment to use.
Locators:    "Feature Comparison Table"; "Key Distinctions"; "Recommendation".
Quote:       "The free distribution of dbt v2 is our default recommendation over dbt OSS. It has more capabilities and its license is designed to permit the same real-world use cases for free without ever paying or talking to dbt Labs."

### 3
URL:         https://docs.getdbt.com/docs/local/install-dbt-v2
Kind:        primary. dbt Labs install doc, owns what dbt-oss includes.
Establishes: firsthand: dbt-oss install and its exclusions.
Paraphrase:  `python -m pip install dbt-oss` installs the open-source Rust runtime. Version output should begin with `2.`. Includes the language, DAG semantics and `run`, `build`, `test`, `compile`, `parse`. Explicitly NOT included versus standard dbt: SQL comprehension and static analysis, LSP features, `dbt lint` and error diagnostics, VS Code extension integration. Most users are told to use the standard install instead.
Locators:    sections "What's Included" and "What's NOT Included".

### 4
URL:         https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2
Kind:        primary. dbt Labs upgrade guide. (The path `.../core-upgrade/upgrading-to-v2` I first fetched redirects here; this is the page's own address.)
Establishes: firsthand: what v2 enforces at parse time vs compile time, static-analysis modes, breaking changes, adapter tiers.
Paraphrase:  "In v1, misspelled configs, unexpected YAML keys, and invalid flags were silently ignored. In v2, dbt enforces a tightly-defined language specification at parse time and raises explicit errors for any violation." Parse-time failures (not compile) for nonexistent macro invocations, nonexistent adapter methods, missing generic tests, missing variables, duplicate docs blocks. Static analysis: `baseline` (default) "Parses SQL at compile time; findings are warnings"; `strict` "Fully resolves column types; requires authentication via `dbt login`". Removed flags: `--models/--model/-m` (use `--select`), `--partial-parse`. All unit tests run first in `dbt build`. Adapters listed GA: BigQuery, Databricks, Redshift, Snowflake; beta/private beta: ClickHouse (private), Apache Spark (CLI only, beta), DuckDB (CLI only). Writes a v12 manifest compatible with v1. Adapters connect via ADBC; drivers download from the dbt Labs CDN on first run. Packages need `require-dbt-version` containing 2.0.0.
Locators:    headings "Strict Validation", "Parse-Time Failures", "Static Analysis", "Supported Adapters in v2", "ADBC Drivers", "Manifest Compatibility". Page text fetched through a summarizing tool; check wording before quoting.

### 5
URL:         https://docs.getdbt.com/reference/resource-configs/static-analysis
Kind:        primary. dbt Labs reference doc, owns the semantics of the `static_analysis` config.
Establishes: firsthand: what each mode means and when analysis cannot run.
Paraphrase:  Modes `strict` (previously `on`), `baseline` (default), `off`. Baseline is "the recommended starting point for users transitioning from dbt v1, providing a smooth migration experience while still catching most SQL errors", produces a partial analyzed schema, no UDF registration. Strict: "Statically analyze all SQL before execution begins. ... nothing runs until the entire project is proven valid." Custom materializations are automatically set to `static_analysis: off` and all downstream models become ineligible. A child cannot be stricter than its parent, so a baseline parent cannot have a strict child. Doc says analysis "can fail in some cases (for example, dynamic SQL constructs or unrecognized UDFs)" and you may need `off`. CLI override: `dbt run --static-analysis off|baseline`. The doc does not enumerate which checks run in baseline.
Locators:    sections "Definitions of Each Mode", "Cascading Rules", "Important Caveat".

### 6
URL:         https://docs.getdbt.com/blog/dbt-core-v2-is-here
Kind:        primary. dbt Labs dev blog, authors Joel Labes (Staff Developer Experience Advocate, dbt Labs) and Grace Goheen (Product Manager, dbt Core, dbt Labs), dated June 1, 2026. Owns the licensing and one-engine claims at alpha.
Establishes: firsthand: the pre-GA decision to collapse two engines and the license history. It is an ALPHA announcement, not the GA record.
Paraphrase:  "As always, dbt Core's code is completely open source under the Apache 2.0 license." Code moved from the ELv2-licensed dbt-fusion repo into dbt-core under Apache 2.0. Fusion described as the enhanced precompiled binary with some proprietary code, "Which v2 distribution should you choose for your use case? Almost certainly Fusion." Parse time: "Significant parse time improvements, especially on the largest dbt projects" (no multiplier). Language spec claim: "makes it impossible to accidentally configure a `desciptin` instead of a `description`". Try-before-migrate: `dbt parse --use-v2-parser` on v1.12. Upgrade is optional.
Locators:    section "Putting all our efforts behind a single engine", "Recap: what's changing, what's staying the same".

### 7
URL:         https://github.com/dbt-labs/dbt/blob/main/docs/roadmap/2026-06-announcing-v2.md
Kind:        primary. dbt Labs roadmap doc in the repo, signed "JEG" (the three authors' initials), June 2026.
Establishes: firsthand: the single-engine decision, the open/proprietary line at alpha, and the stated plan to reach GA. Raw text read via raw.githubusercontent.com; the github.com page returns 403 to curl from this sandbox (gated, not dead).
Paraphrase:  "One engine, under the Apache 2.0 license, indivisible, with faster parsing and modern interfaces for all." Two-engine duplication slowed the team and "risks divergence of behavior". Alpha because conformance against v1 needed community testing; programmatic Python interface was a parity gap to close before GA. Open vs proprietary: "In v2.0, that includes things (available in Fusion only) like advanced SQL comprehension, linting, and column-level lineage." Thin Apache-licensed clients in dbt-core call login-gated features. "Core v1 is not going away tomorrow, or any time soon."
Locators:    "Present", "The path from alpha to GA", "A vision to work towards".
Quote:       "...advanced SQL comprehension, linting, and column-level lineage" described as "available in Fusion only".

### 8
URL:         https://github.com/dbt-labs/dbt
Kind:        primary. The repository README, owned by dbt Labs. Repo was `dbt-labs/dbt-core`; the README and docs now use `dbt-labs/dbt`. Fetched via a summarizing tool and raw README text (github.com itself returns 403 to curl here).
Establishes: firsthand: license of the repo and the claim that main is v2.0 Rust.
Paraphrase:  "The `main` branch now contains all the Apache 2.0 source code of dbt v2.0, a ground-up rewrite of dbt in Rust." v1 Python lives on `1.latest`. "dbt is a distribution of the dbt repository with dbt-specific customizations released under a dbt product license" (linked to the dbt Product Licensing Agreement). Platform table: macOS x86-64 and ARM, Linux x86-64 and ARM supported; Windows ARM not yet. Parquet artifacts, JSON still produced for backward compatibility.
Locators:    top warning box; "About dbt v2.0"; "Supported operating systems and architectures"; "License".
Note:        I could not read repo issue counts, release list or contributor stats (GitHub API access to this repo was refused in this environment).

### 9
URL:         https://www.getdbt.com/dbt-product-license-agreement (the address `https://www.getdbt.com/dbt-fusion-engine-license-agreement` that the README links to resolves here)
Kind:        primary. dbt Labs' own license text.
Establishes: firsthand: the `dbt` distribution is under a proprietary license, not an OSI one.
Paraphrase:  Permits download, install, run and use of dbt and the VS Code extension, and redistribution with conditions. Account with verified email needed for "Platform Features". Redistributors must not block telemetry or interfere with communication between dbt Labs and end users. Prohibits reverse engineering. Liability capped at $10.00. States dbt OSS source is separate, under Apache 2.0.
Locators:    summarized by fetch tool; sections on use, redistribution, restrictions. Re-open before quoting the clauses.

### 10
URL:         https://docs.getdbt.com/docs/local/connect-data-platform/duckdb-setup
Kind:        primary. dbt Labs adapter doc, last updated Sep 16, 2026.
Establishes: firsthand: DuckDB is built into v2, the profile, limitations.
Paraphrase:  "The DuckDB adapter is built into dbt v2" and needs no warehouse account. Built-in driver cannot load DuckDB extensions (`httpfs`, `parquet`, `spatial`); to use them install the driver with `dbc`. Minimal profile is `type: duckdb` (in-memory) or `type: duckdb` plus `path: './my_project.duckdb'`. Limitations: feature parity with dbt-duckdb v1 tracked in dbt-fusion#1593, SQL-analysis gaps in dbt-fusion#1464. Static analysis "may not infer schemas" for models that read local files via `read_csv()`, `read_parquet()` or `read_json()`, and you may see type-resolution warnings or compile errors even when the query works at run time. The browser tab title in search results reads "Connect DuckDB to Fusion Beta"; the body I fetched does not carry a beta banner.
Locators:    "Installation", "Limitations (dbt v2)", "Static Analysis with Local Files".
Note:        The install snippet in the fetched text is only a comment (recommends VS Code extension). The pip route comes from sources 1 and 4 and my run.

### 11
URL:         https://docs.getdbt.com/docs/dbt/supported-features
Kind:        primary. dbt Labs feature matrix and adapter list.
Establishes: firsthand: adapter GA list and known limitations.
Paraphrase:  GA adapters: BigQuery, Databricks, Redshift, Snowflake, and "DuckDB (CLI only)" with no authentication. Beta/preview: ClickHouse (private beta), Apache Spark (CLI only, beta). Feature rows: semantic and syntax error detection and fast linter and LSP listed as not needing login; column-level lineage, full Docs v2 and data diff listed as needing a (free) login. Known limitations: some materialization features not fully supported, tooling that depends on v1 log format may break, model-level notifications not yet supported, SQLFluff not natively compatible (`dbt lint` rule parity differs).
Locators:    adapter list and "Known Limitations".

### 12
URL:         https://docs.getdbt.com/docs/local/install-dbt
Kind:        primary. dbt Labs install page.
Establishes: firsthand: install commands and `dbt login`.
Paraphrase:  `python -m pip install dbt`; Homebrew `brew tap dbt-labs/dbt` then `brew install dbt-labs/dbt/dbt`; curl installer; winget `winget install --id dbtLabs.dbt --exact`; verify with `dbt --version`. `dbt login` creates a free account for VS Code extension features. States dbt v2 "includes proprietary runtime" and the Apache 2.0 runtime is an alternative.
Locators:    "Install Commands by Platform", "Optional: Sign In for Full v2 Features", "Key Caveats".

### 13
URL:         https://www.fivetran.com/press/fivetran-dbt-labs-announces-new-capabilities-to-make-enterprise-data-agent-ready-at-dbt-summit-2026
Kind:        primary for the claim that dbt Labs announced GA on 16 Sep 2026 and made the 10x statement; NOT independent. Joint press release of Fivetran + dbt Labs, who have merged and who have a sales stake.
Establishes: firsthand (as the vendor): the GA announcement and the marketing form of the speed claim. Repeats everything else.
Paraphrase:  16 Sep 2026, Las Vegas. "...announced the general availability of dbt v2 and dbt State". "It parses a 10,000-model project up to 10x faster than v1." "Both versions remain Apache 2.0-licensed and security-supported." Quotes Anjan Kundavaram, Chief Product Officer, Fivetran + dbt Labs.
Locators:    opening paragraphs. The press release gives no footnote or benchmark method for "up to 10x".
Quote:       "It parses a 10,000-model project up to 10x faster than v1."
Note:        "Both versions remain Apache 2.0-licensed" refers to dbt v1 and dbt v2 as products; Source 2 and Source 9 say the `dbt` v2 binary is under a proprietary license and only dbt OSS is Apache 2.0.

### 14
URL:         https://duckdb.org/2026/09/22/dbt-fusion
Kind:        secondary. Post on duckdb.org by Geertjan Wielenga, dated September 22, 2026; reports on dbt Labs' product from outside dbt Labs. Not firsthand testing as far as the fetch shows. The author's affiliation was not shown in the fetched text; check before labeling.
Establishes: merely repeats and illustrates dbt Labs' docs on DuckDB; adds that DuckLake and Iceberg catalog support is v2-only behind the `use_catalogs_v2` flag.
Paraphrase:  Calls dbt v2 "the first dbt release that ships with a built-in DuckDB adapter", adapter lives in a Rust monorepo and connects via ADBC, driver auto-downloaded and cached on first run. Gives `dbt parse --use-v2-parser`, `dbt parse --generate-info-schema`. Provides no benchmarks.
Locators:    post body.
Quote:       "Either way, running dbt on DuckDB means you develop, test, and publish your models on your own machine."

### 15
URL:         https://github.com/dbt-labs/dbt-agent-skills/pull/164
Kind:        secondary for adoption, and the strongest independent-ish item. A merged PR in dbt Labs' own agent-skills repo by "b-per", dated September 23, 2026, recording lessons from "a production dbt-core migration to v2". The repo is dbt Labs', so it is not independent of dbt Labs, but the content is a practitioner's field report that contradicts the marketing in places. I cannot confirm b-per's employer from the fetch.
Establishes: firsthand report of real migration friction (as relayed by the PR text).
Paraphrase:  Default the repro command to `--static-analysis strict` because plain `dbt compile` misses errors strict mode catches. Case-sensitive column identifier mismatches (dbt0227/dbt0209) were "the most common v2-strict-mode pattern seen in a real migration". Static analysis only reports the first error per node. Autofix sometimes put valid changes in structurally wrong places. Checker results were seen to differ between an isolated `--select` compile and a full-project compile with unchanged code. Warehouse verification queries are used to tell genuine bugs from stale static-analysis caches. Guidance extended to `static_analysis: off` with sign-off for production models.
Locators:    PR description and changelog entries (version 1.3.4 to 1.3.5). github.com returns 403 to curl here, text read via the fetch tool.

### 16
URL:         https://datacoves.com/post/dbt-fusion
Kind:        secondary. By Noel Gomez, Datacoves co-founder, dated July 22, 2026. Datacoves sells managed dbt in private clouds, so it has a commercial stake against dbt Labs' platform. Not firsthand testing per the fetch; it relies on dbt Labs' benchmarks and user reports.
Establishes: the "open-source framing is contested" position, from a competitor.
Paraphrase:  "dbt 2.0 collapsed two engines into one Rust foundation. The split moved from the codebase to the license." The recommended path carries proprietary code on top of the open core, "the fully open one now requires choosing it deliberately". Notes dbt lint "roughly 50x faster than single-threaded SQLFluff" but that SQLFluff usually runs multi-threaded. Migration limits: Python models in public preview, packages may fail to parse until updated.
Locators:    article sections on licensing and migration. Written pre-GA (alpha period).

### 17
URL:         https://brainsandbots.substack.com/p/dbt-summit-2026-wrap-up-level-up
Kind:        secondary. Sonny Rivera, Brains & Bots newsletter, dated September 23, 2026, attended the summit in person. Reports the keynote; the "10x faster parsing" statement is a repeat of dbt Labs' claim, not a test.
Establishes: that someone outside dbt Labs attended and recommends testing v2 in controlled domains first.
Paraphrase:  Calls the engine "the BIG ONE", says it "replaces Python entirely and provides 10x faster parsing", and that it catches errors before warehouse execution. Recommends piloting in controlled domains.
Locators:    section on the engine.

### 18
URL:         https://byteiota.com/dbt-core-2-rc2-migration-guide/
Kind:        secondary. Byteiota, byline "ByteBot", dated September 9, 2026, pre-GA (RC2). Advice article; no measured tests shown. (curl to this host timed out from the sandbox; the text was read through the fetch tool.)
Establishes: repeats dbt Labs' migration points (strict YAML, removed flags, parse check). Gives "a 70 MB manifest compresses to roughly 6 MB" with Parquet, a figure I could not trace to a primary.
Paraphrase:  Four issues to fix before GA: YAML strictness, manifest.json to Parquet, removed `--models` and `--partial-parse`, run `dbt parse --use-v2-parser` on v1.12.
Locators:    the four numbered issues.

### 19
URL:         https://pypi.org/project/dbt/ and https://pypi.org/project/dbt-oss/
Kind:        primary for what the packages are called and which versions exist; I verified by installing. PyPI pages themselves were only checked for HTTP 200.
Establishes: my own run, Section "My local reproduction" below.

## My local reproduction (own run, 2026-10-02, Linux x86-64, 4 cores, Python 3.11)

Not a dbt Labs claim. Commands run in clean virtualenvs.

Installs: `pip install dbt` gave `dbt 2.0.6`; `pip install dbt-oss` gave `dbt-oss 2.0.5`; `pip install "dbt-core<2" dbt-duckdb` gave dbt-core 1.12.5 with dbt-duckdb 1.11.0. No `dbt login` was run. The DuckDB driver is fetched by dbt on first run (needs network).

Project: `dbt_project.yml` (name toy, profile toy, model-paths models), `profiles.yml` with `type: duckdb`, `path: ./toy.duckdb`. Model a: `select 1 as id, 'x' as name`. Model b: `select id, nme from {{ ref('a') }}` (typo: `nme`).

Results for the misspelled column `nme`:
- `dbt compile` (dbt 2.0.6, default baseline): "Finished 'compile' successfully ... 2 total | 2 success". No warning printed. Same with `--static-analysis baseline`.
- `dbt compile --static-analysis strict` (dbt 2.0.6): fails at compile, before any query: `[error] [UnresolvedIdentifier (dbt0227)]: No column nme found. Available are toy.main.a.name, toy.main.a.id --> models/b.sql:1:12`. Summary "2 total | 1 success | 1 error". The error is followed by a long Rust stack trace in the terminal output.
- `dbt run` (dbt 2.0.6, default): model a succeeds, model b fails at DuckDB: `Database Error in model b ... Binder Error: Referenced column "nme" not found in FROM clause! Candidate bindings: "name"`.
- dbt-oss 2.0.5: `--static-analysis strict` does not check; it prints `[warning] [Generic (dbt1000)]: static analysis was requested with --static-analysis strict but did not run: this distribution of dbt OSS does not include the static analysis engine. Install the full dbt distribution to enable it: dbt system upgrade-distribution` and the compile "succeeds". `dbt run` then fails at the database exactly as above.
- dbt-core 1.12.5 + dbt-duckdb 1.11.0: `dbt compile` passes; `dbt run` fails with `Runtime Error in model b ... Binder Error: Referenced column "nme" not found`. So the bad column is a run-time failure in v1, and also in v2 unless strict is on.
- Bad `ref('missing_model')`: caught at parse by BOTH dbt 1.12.5 (`Compilation Error ... depends on a node named 'missing_model' which was not found`) and dbt-oss 2.0.5 (`[DependencyNotFound (dbt1048)]: Ref 'missing_model' not found in project`). A missing ref was already a pre-run error in v1. The v1-vs-v2 difference in the example is the column check, not the ref check.
- Misspelled YAML key `desciptin: oops` under a model in a `.yml`: dbt-oss 2.0.5 `dbt parse` errors `[UnusedConfigKey (dbt1060)]: ... Ignored unexpected key "desciptin"`. dbt-core 1.12.5 `dbt parse` printed no error in my run (I tailed only the last lines and did not see a deprecation warning; rerun with full output before claiming it is silent).

## Contradictions

1. Naming and license: the commission says "dbt Core v2.0 ... Fusion ... Apache 2.0." At GA the Fusion engine became "dbt" under a proprietary product license (Sources 2, 9, 12) and "dbt Core v2" became "dbt OSS", the Apache subset (Sources 2, 3). The press release says "Both versions remain Apache 2.0-licensed" (Source 13) while the docs say the default `dbt` v2 distribution is proprietary with Apache-licensed code underneath (Sources 2, 8, 12). The alpha roadmap's "One engine, under the Apache 2.0 license, indivisible" (Source 7) is true of the shared code, not of the distribution that does static analysis.
2. Where the compile-time check lives: the GA post (Source 1) presents static analysis as dbt v2's headline feature without saying it is absent from the Apache build; Sources 2, 3 and 7 say it is Fusion/`dbt` only; my run confirmed dbt-oss refuses to run it.
3. Default mode does not catch the example error: the upgrade guide says baseline produces warnings (Source 4) and the config doc says baseline catches "most SQL errors" (Source 5). In my run baseline printed nothing for a plain misspelled column on DuckDB; only strict raised it. Source 15 independently says plain compile "misses errors caught in strict mode".
4. Strict and login: Source 4 says strict "requires authentication via `dbt login`"; Source 11 lists semantic error detection as no-login. In my run on DuckDB, strict worked with no login.
5. Speed: the press release says "parses a 10,000-model project up to 10x faster than v1" (Source 13). The GA blog's own benchmark is 70 s to 17 s compile on a 10k-node project, which is about 4.1x, and "2x or more" for normal projects (Source 1). The parse-vs-compile difference and the "up to" are not reconciled in any document I read. No document I read gives the parse-time pair that would produce 10x.
6. DuckDB status: Source 11 lists "DuckDB (CLI only)" in the GA adapter group; Source 4 lists DuckDB under "Beta/Private Beta"; the setup page's browser title was "Connect DuckDB to Fusion Beta" and its body says some dbt-duckdb v1 features are not yet supported and static analysis may not infer schemas from `read_csv()` and similar (Source 10). DuckDB is not a clean "GA adapter" in the primary record.
7. Commission says "GA within the last 90 days at dbt Summit 2026 (September 2026)": consistent. GA post and press release are both dated 16 Sep 2026 (16 days before today).

## Numbers

Figure: 70 seconds to compile on dbt 1.12.0 vs 17 seconds on dbt v2, on "my benchmarking project with 10k nodes". Ratio computed by me: about 4.1x.
Owner:  Source 1 (Joel Labes, dbt Labs). dbt Labs' claim; not independently reproduced.
Scope:  one custom project of 10,000 nodes; compile, not parse; hardware, adapter, thread count and run count not stated.

Figure: "parses a 10,000-model project up to 10x faster than v1".
Owner:  Source 13 (Fivetran + dbt Labs press release, 16 Sep 2026). dbt Labs' claim, marketing form; "up to" and no method given.
Scope:  10,000 models, parse, v2 vs v1; no benchmark, hardware or baseline version disclosed in the release.

Figure: "2x or more faster compilation" for "more normal-sized projects".
Owner:  Source 1. dbt Labs' claim.
Scope:  unspecified project size.

Figure: parse times "as long as 20 minutes" in v1 at very large scale.
Owner:  Source 1. dbt Labs' claim, no project named.

Figure: batch tests "reduce test command runtime by 40%, queries issued by 65%, and warehouse cost of running tests by 15%".
Owner:  Source 4 (dbt Labs upgrade guide). dbt Labs' claim; scope not stated. Off-spine; do not use unless needed.

Figure: Parquet information schema "can reduce file sizes by over 10x"; separate 70 MB manifest to about 6 MB (Source 18, untraced).
Owner:  first by Source 1 (dbt Labs); the 70 MB to 6 MB figure by byteiota, secondary, no primary found.
Scope:  artifact size, not speed.

Figure (my measurement, single machine, not dbt Labs'): synthetic 3,000-model DuckDB project, each model a join of two earlier models by `ref`, 4-core Linux box. Parse, wall-clock seconds, run 3 times each, full parse with v1 `--no-partial-parse` and `target/` deleted before each run: dbt-core 1.12.5 15.8, 15.2, 15.8; dbt-oss 2.0.5 2.1, 2.2, 2.0; dbt 2.0.6 2.3, 2.3, 2.6. Compile, 2 runs each: dbt-core 1.12.5 32.2, 32.5; dbt-oss 2.0.5 4.0, 4.2; dbt 2.0.6 4.4, 4.2. That is about 7x on parse and 7-8x on compile at 3,000 simple models.
Owner:  this record (own measurement). Scope: wall-clock including process startup, simple one-line SQL models, one thread default, no warehouse work in parse/compile, no static analysis strict in the timing runs; not comparable to dbt Labs' 10k-node project. Uses `date` timing around the CLI. Treat as an illustration only.

Figure: dbt-core 1.12.5 / dbt-duckdb 1.11.0 / dbt 2.0.6 / dbt-oss 2.0.5 version strings from `dbt --version` and pip.
Owner:  my run.

## Limits

- Is a faithful local run of v2.0 with dbt-duckdb reproducible from the documented install path? YES. `python -m pip install dbt` (documented in Sources 4 and 12) installs a self-contained v2 CLI with a built-in DuckDB adapter; `profiles.yml` with `type: duckdb` and `path:` is documented in Source 10. I did it end to end with no account and no warehouse, in under a few minutes, and got the outputs above. The writer should run a real experiment, and may reuse the toy project and commands exactly as listed. Caveats: needs network on first run for the driver download from the dbt Labs CDN (Source 4); outputs include very long Rust stack traces under errors, which the writer will have to trim and say so; behavior may change between 2.0.5/2.0.6 and later patches, so name the version.
- The most important limit: the checks the commission's angle depends on (column-level, type-aware compile-time analysis) are NOT in the Apache 2.0 build. They are in the `dbt` distribution under a proprietary dbt product license (Sources 2, 3, 7, 9, 12; confirmed by my run). The piece cannot say "the open-source Rust engine catches column errors before the warehouse." It can say the single Rust code base parses everything and the proprietary distribution adds the SQL-comprehension layer. Also, even in that distribution the default `baseline` mode did not flag my misspelled column; `strict` did.
- The v1-vs-v2 contrast for "bad ref" does not exist: v1.12.5 also fails a missing `ref` before the run (my run). The sharper contrast I could reproduce is the misspelled column (run-time failure in v1, and in v2 baseline; compile-time failure only in v2 strict with the full distribution) and the strict YAML spec (v2 errors on a misspelled config key; the v1 result needs recheck).
- Did NOT establish: any independent reproduction of dbt Labs' 10x or 70 s/17 s numbers on their benchmark project; the benchmark project is not named or published in anything I read. My 7x figure is a different, synthetic workload.
- Did NOT establish: adoption numbers (downloads, stars, issue counts, contributor activity). GitHub API reads on dbt-labs/dbt and dbt-fusion were refused in this environment, and the PyPI pages were only checked for HTTP 200. Independent adoption evidence is limited to Source 15 (one production migration, relayed through a dbt Labs repo PR), Source 17 (summit attendee, repeats the claim) and commentary (Sources 16, 18) that is not first-hand. Two further candidate articles (a Medium migration piece "dbt Core v2.0 Just Rewrote Itself in Rust — Here's What Actually Breaks When You Migrate", and Rittman Analytics' summit write-up) returned 403 and were not read; a search-result snippet of the Medium piece reports a silent 4x duplication of production rows, which I could not verify, so do not cite it.
- Did NOT establish: the exact content of the dbt-fusion#1464 and #1593 issue lists. #1464 as fetched is an open epic "[EPIC] DuckDB #14393" by dataders (March 17, 2026) with no enumerated gaps in the text I got; the DuckDB analysis gaps are in sub-issues I did not open.
- Did NOT verify: the full text of the license agreement beyond the summary (Source 9); re-open before quoting clauses.
- Did NOT verify whether dbt-core 1.12.5 prints a deprecation warning for the `desciptin` key. My tail of its output showed no error.
- Several docs pages were read through a page-summarizing fetch; wording I marked as quotes is from that text. The writer should reopen the cited section before using a verbatim quote.
- Static analysis behaviors beyond DuckDB (Snowflake, BigQuery, Databricks, Redshift) were not tested. Per Source 5 they have function-support pages; the analysis quality can differ by adapter.

## Source assets

Asset: none verified as an official parse/compile/run pipeline diagram. The GA post (Source 1) has "logical plan" prose and linked sub-posts on SQL comprehension levels that I did not open; the repo README (Source 8) embeds `etc/dbt-transform.png` (a generic architecture image, not a Rust pipeline) and the roadmap (Source 7) has `assets/upvoted-feature-requests.png`. I did not open any of these images.
Shows:  nothing I can vouch for.
Crop:   not applicable. The writer should build the pipeline figure from the documented behavior (Sources 4, 5) and label it as a drawing.

Asset: benchmark chart: none found. The only benchmark is two numbers in prose in Source 1 (70 s, 17 s).
Shows:  a two-bar comparison could be rebuilt, but it is one vendor-run data point; a chart would need to say so. My own 3-run series above could be charted as a separate, labeled own-measurement series.
Crop:   if charted, keep the scope "10k nodes, compile, dbt 1.12.0 vs dbt v2, dbt Labs benchmark" in the caption.

Asset: the terminal outputs in "My local reproduction" (real command output).
Shows:  the same file failing three different ways: baseline compile passes, strict compile fails at `models/b.sql:1:12` with the available columns, run fails inside DuckDB.
Crop:   keep the command line, the error code (dbt0227), the file:line:column pointer and the summary line; trim the stack trace and say it was trimmed.

## Discarded

https://medium.com/tech-with-abhishek/dbt-core-v2-0-just-rewrote-itself-in-rust-heres-what-actually-breaks-when-you-migrate-fbd16c84b666: 403 to fetch, not read; search snippet only, unverified.
https://blog.rittmananalytics.com/dbt-summit-2026-whats-new-and-what-s-coming-from-dbt-labs-fivetran-and-the-agentic-data-stack-52bbef9334a9: 403, not read.
https://www.businesswire.com/news/home/20260916136480/en/Fivetran-Dbt-Labs-Announces-New-Capabilities-to-Make-Enterprise-Data-Agent-Ready-at-dbt-Summit-2026: 403, not read; the same release is read at Source 13.
https://blog.damavis.com/en/dbt-2-0-guide-to-new-features-and-improvements/: read through the fetch tool (Antoni Casas for Damavis, 22 Sep 2026); no tests, no numbers, repeats dbt Labs docs; adds nothing citable. curl timed out from this sandbox.
https://dataengineerhub.blog/articles/dbr-fusion-engine-migration-guide: seen only as a search result; its title claims "30x faster parsing", which no primary supports. Not opened. Do not cite.
https://medium.com/@karthikrajashekaran/6-things-from-dbt-summit-2026-that-actually-matter-and-which-ones-you-can-use-today-5b327f89a82b: seen as a search result only, not opened.
https://releases.sh/collections/data-engineering/digest/2026-07-20: seen as a search result only; aggregator, not a primary.
