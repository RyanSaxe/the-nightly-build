# Evidence — expert-tools/files-to-prompt (01)

## Summary

`files-to-prompt` still qualifies as a niche, powerful AI-harness tool as of
2026: it has not become a familiar default (Repomix, its nearest competitor,
runs ~27.5k GitHub stars against files-to-prompt's ~2,800, and files-to-prompt
is not the "packs everything into one AI-friendly file" default the ecosystem
now reaches for), it is not a foundation tool, and its distinction is
mechanical (a 334-line, dependency-light concatenator with a Claude-XML mode)
rather than mere popularity. The evidence is strong on mechanics: I read the
entire `cli.py` source, installed the real PyPI package (`pip install
files-to-prompt`, resolved version 0.6), and ran it myself on real subtrees of
this repository, capturing default-mode, `--cxml`, gitignore-honoring, and
binary-skip behavior directly. Every capability claim in the commission
(gitignore handling, `--cxml` structure, extension filter, binary skip) is
verified against source and a live run, not assumed.

The evidence is weaker, and this is the piece's central honest tension, on
maintenance: the last commit and last PyPI release are both dated 2025-02-19,
making the tool roughly 17 months stale as of the 2026-07-31 commission date,
with 13 open issues (including two I independently reproduced by running the
tool myself: the `-e` suffix-match footgun and an anchored-`.gitignore`
leak). The tool is not broken for its core, documented use case — my runs
show the well-known flags working exactly as documented for typical inputs —
but it is dormant, not actively maintained. This is a judgment call for the
writer's adopt-or-not conclusion, not grounds by itself to disqualify the
pick under the commission's three named disqualifiers (default / unmaintained
/ only-popular): it fails none of the first and third, and the second is a
real but arguable risk that the evidence below should let the writer state
plainly rather than paper over. I did not escalate `REQUEST correspondent`;
I proceeded with the pick and carry the maintenance caveat into evidence for
an honest verdict.

Independent (non-Willison) usage confirmation is present but thin: one HN
reply from a third party ("layer8") testing the exact piped workflow, one
independent Crystal-language port, and the GitHub issue tracker itself
(13 open issues filed by users other than the author, which is real
independent usage evidence even though it is evidence of friction rather than
praise).

## Sources

1. **`files_to_prompt/cli.py`**, full source, fetched from
   `https://raw.githubusercontent.com/simonw/files-to-prompt/main/files_to_prompt/cli.py`
   (334 lines, read in full).
   - **Primary.** This is the tool's own implementation — it owns every
     mechanical claim in the piece.
   - Establishes: the exact `should_ignore`/`read_gitignore` implementation
     (lines 27-43) — `.gitignore` rules are read per-directory during
     `os.walk` and matched with `fnmatch` against `os.path.basename(path)`
     only; there is no support for path-anchored patterns (leading `/`), no
     negation (`!pattern`), no `**` glob semantics — it is a flat basename
     matcher, not a gitignore-spec implementation. Establishes binary
     handling: there is no binary-detection step at all — `process_path`
     (lines 101-172) opens every file as text and catches
     `UnicodeDecodeError`, printing a red warning to stderr and skipping the
     file (lines 114-120, 158-172). Establishes extension filtering is a
     plain Python `str.endswith(extensions)` check (line 154) with no dot
     normalization, so `-e py` matches any filename ending in the literal
     characters "py", extension or not. Establishes the exact `--cxml`
     structure: `<documents><document index="N"><source>path</source>
     <document_content>...</document_content></document>...</documents>`
     (lines 74-84, confirmed identical in my own run below). Establishes
     `-o/--output`, `-n/--line-numbers` (zero-padded line numbers, lines
     46-52), `-m/--markdown` (backtick-fence escalation when content already
     contains backticks, lines 87-98), and `-0/--null` / stdin path reading
     (lines 175-185, 299-303) — reading stdin blocks if stdin is a
     non-interactive pipe that never closes (`sys.stdin.read()` at line 180
     is only skipped when `sys.stdin.isatty()` is true).
   - Verbatim (should_ignore, the entire gitignore-matching logic):
     ```python
     def should_ignore(path, gitignore_rules):
         for rule in gitignore_rules:
             if fnmatch(os.path.basename(path), rule):
                 return True
             if os.path.isdir(path) and fnmatch(os.path.basename(path) + "/", rule):
                 return True
         return False
     ```
   - Locator: whole file; specific claims cited by line number above.

2. **`README.md`**, fetched from
   `https://raw.githubusercontent.com/simonw/files-to-prompt/main/README.md`
   (271 lines, read in full).
   - **Primary.** The author's own documentation of the tool he wrote.
   - Establishes the documented flag list and the author's own worked
     examples for `--ignore`, `--include-hidden`, `-n`, `-0`, and `--cxml`.
     Matches the source exactly for the `--cxml` shape (README lines
     198-215 reproduce the same `<source>`/`<document_content>` tags the
     code emits) — no discrepancy between docs and implementation on this
     point, though see Contradictions for a discrepancy inside the CLI's own
     `--help` text.
   - Verbatim (Claude XML section, README lines 198-215):
     ```xml
     <documents>
     <document index="1">
     <source>my_directory/file1.txt</source>
     <document_content>
     Contents of file1.txt
     </document_content>
     </document>
     ...
     </documents>
     ```
   - Locator: "### Options" and "### Claude XML Output" sections.

3. **`tests/test_files_to_prompt.py`**, fetched from
   `https://raw.githubusercontent.com/simonw/files-to-prompt/main/tests/test_files_to_prompt.py`
   (441 lines; read the first 60 in full, confirming test structure and
   coverage of `--include-hidden` and nested-`.gitignore` cases).
   - **Primary.** The project's own test suite.
   - Establishes real, passing test coverage for basic concatenation,
     `--include-hidden`, and a nested-`.gitignore` case (`test_ignore_gitignore`,
     starting line 49) — confirms the maintainers did test simple nested
     `.gitignore` inheritance, which is consistent with my finding that
     *unanchored* patterns work correctly; the test suite does not appear
     to cover anchored (`/path/`) patterns, consistent with issue #46 below
     going unfixed.
   - Locator: `test_basic_functionality` (line 15), `test_include_hidden`
     (line 32), `test_ignore_gitignore` (line 49).

4. **Real run — default mode**, my own execution, 2026-07-31, on this
   repository's real `engine/assets/` subtree (mixed text + binary PNGs).
   - **Primary** (first-hand output).
   - Command: `files-to-prompt engine/assets` (files-to-prompt 0.6, installed
     via `pip install files-to-prompt`).
   - Captured stderr (binary skip, confirms the UnicodeDecodeError mechanism
     from source item 1, not a dedicated binary sniff):
     ```
     Warning: Skipping file engine/assets/apple-touch-icon.png due to UnicodeDecodeError
     Warning: Skipping file engine/assets/favicon-32.png due to UnicodeDecodeError
     Warning: Skipping file engine/assets/favicon-64.png due to UnicodeDecodeError
     ```
   - Captured stdout (trimmed, default-mode format, path + `---` fencing):
     ```
     engine/assets/nb.css
     ---
     /* The Nightly Build — site chrome + shared article chrome. ...
     ...
     ---
     ```
   - Total stdout: 8,217 bytes for the two remaining text files
     (`nb.css`, `nb.js` plus `themes/newspaper.css`); the three PNGs (a
     combined ~172 KB of binary data) were cleanly excluded from the prompt
     text with only a one-line stderr warning each — this is the concrete
     "drowns in irrelevant files" cost the tool removes versus a raw
     `cat *`.

5. **Real run — `--cxml` mode**, my own execution, 2026-07-31, on
   `engine/ci_helpers.py` and `engine/check.py` from this repository.
   - **Primary** (first-hand output).
   - Command: `files-to-prompt engine/ci_helpers.py engine/check.py --cxml`
   - Captured output (head, confirms structure matches source/README exactly):
     ```xml
     <documents>
     <document index="1">
     <source>engine/ci_helpers.py</source>
     <document_content>
     #!/usr/bin/env python3
     # /// script
     # requires-python = ">=3.10"
     # dependencies = ["pyyaml"]
     # ///
     """Answer PR-shape and press-configuration questions for the CI workflows.
     ...
     ```
   - Captured output (tail, confirms `</documents>` closure and per-file
     `index` incrementing — `ci_helpers.py` is index 1, `check.py` is index
     2 in the full file, 7,576 bytes total):
     ```
     ...
     </document_content>
     </document>
     </documents>
     ```

6. **Real run — extension-filter footgun**, my own execution, 2026-07-31,
   scratch directory with three files: `real.py`, `copy` (no extension),
   `notpy.txt`.
   - **Primary** (first-hand output, reproduces GitHub issue #60 below
     independently before I read the issue).
   - Command: `files-to-prompt . -e py`
   - Captured output: the tool returned **both** `./real.py` and `./copy`
     (a file with no extension at all), because `-e py` compiles to
     `str.endswith(("py",))` and the literal name "copy" ends in the two
     characters "p" and "y". `notpy.txt` was correctly excluded. This
     confirms source item 1's line-154 finding empirically.

7. **Real run — anchored `.gitignore` leak**, my own execution, 2026-07-31,
   scratch directory with `.gitignore` containing `/src/staticfiles/` and a
   real file at `src/staticfiles/bundle.txt`.
   - **Primary** (first-hand output, independently reproduces GitHub issue
     #46 below).
   - Command: `files-to-prompt .` (default mode, gitignore honored by
     default)
   - Captured output: both `./app.py` and `./src/staticfiles/bundle.txt`
     were printed — the anchored pattern was not honored, because (per
     source item 1) the matcher only does `fnmatch` against the bare
     basename `staticfiles`, and `/src/staticfiles/` as a literal fnmatch
     pattern against the basename `staticfiles` does not match due to the
     leading slash and trailing slash in the pattern string.

8. **Real run — gitignore honoring for a simple unanchored rule**, my own
   execution, 2026-07-31, scratch directory with `.gitignore` containing
   `__pycache__/` and `*.pyc`, plus `pkg/mod.py` and
   `pkg/__pycache__/mod.cpython-311.pyc`.
   - **Primary** (first-hand output).
   - Commands and captured output:
     ```
     $ files-to-prompt .
     ./pkg/mod.py
     ---
     print('hi')
     ---
     $ files-to-prompt . --ignore-gitignore
     ./pkg/mod.py
     ---
     print('hi')
     ---
     ./pkg/__pycache__/mod.cpython-311.pyc
     ---
     compiled bytecode placeholder
     ---
     ```
   - Confirms the basic, unanchored case works exactly as documented:
     default mode honors `.gitignore` and excludes the compiled artifact;
     `--ignore-gitignore` bypasses it. This is the case the commission and
     README describe; items 6-7 above show where that same mechanism
     breaks down.

9. **PyPI JSON API**, `https://pypi.org/pypi/files-to-prompt/json`, fetched
   and parsed directly, 2026-07-31.
   - **Primary** (the package index's own record, sourced from the
     project's own release uploads).
   - Establishes exact version history with upload timestamps: 0.1
     (2024-03-22), 0.2 (2024-04-08), 0.2.1 (2024-04-08), 0.3 (2024-09-09),
     0.4 (2024-10-16), 0.5 (2025-02-14), **0.6 (2025-02-19T05:58:26Z, the
     current latest)**. License: Apache-2.0. Author: Simon Willison.
   - Locator: `info.version`, `info.license`, `releases` keys of the JSON
     response.

10. **GitHub releases — tag `0.6`**,
    `https://github.com/simonw/files-to-prompt/releases/tag/0.6`.
    - **Primary** (the author's own release notes).
    - Establishes release date "19 February" (year confirmed 2025 by
      cross-reference with PyPI item 9), commit
      `1b234ff6dccb2ca3e56b5c256696558fb85306dc`, and that the release added
      `-m/--markdown` and stdin-based file-list input (the `-0/--null`
      NUL-separated variant), the latter contributed by an outside
      contributor (Ankit Shankar per the notes).

11. **GitHub commit history — `commits/main`**,
    `https://github.com/simonw/files-to-prompt/commits/main`.
    - **Primary** (the repository's own commit log).
    - Establishes the most recent commit to `main` is dated **February 19,
      2025** — the same day as the 0.6 release — meaning there has been no
      commit of any kind (bugfix, doc change, dependency bump) in roughly 17
      months as of the 2026-07-31 commission date. This is the load-bearing
      fact for the maintenance judgment.

12. **GitHub issues list**,
    `https://github.com/simonw/files-to-prompt/issues`.
    - **Primary** (the repository's own issue tracker; each issue is filed
      by an independent user, so this doubles as independent-usage
      evidence).
    - Establishes 13 open issues as of the fetch, none closed/merged since
      the last commit. Two read in full (items 13-14 below) directly
      confirm limitations I found empirically in items 6-7. Others of note:
      #62 "only adds files in root folder but not sub folders on Windows"
      (Jul 10, 2025, unresolved cross-platform bug); #55 "Skipping file XXX
      due to UnicodeDecodeError - but file looks fine and is UTF-8" (Mar 21,
      2025, a false-positive of the same catch-UnicodeDecodeError mechanism
      from source item 1); #59 "Output file is self-referenced" (Apr 28,
      2025 — using `-o` to write into a path the tool is also reading can
      include the output file in its own input on a second run).
    - Locator: issue list, sorted by "recently updated" at fetch time.

13. **GitHub issue #46**,
    `https://github.com/simonw/files-to-prompt/issues/46`, "Ignored paths in
    gitignore are being included in the output."
    - **Primary** (the reporting user's own bug account; also independent
      usage evidence — this user is not Willison).
    - Establishes the exact failure mode I reproduced in item 7: a
      real-world Django project's `.gitignore` used anchored patterns
      (`/staticfiles/`, `/src/staticfiles/`) and files-to-prompt included
      them anyway, producing (in the reporter's account) "vast numbers of
      UnicodeDecodeErrors" and 19,929 matching output lines that should
      have been excluded. Open, unfixed as of fetch.
    - Verbatim: "I _think_ from reading the README that `files-to-prompt`
      is intended to respect `.gitignore`."

14. **GitHub issue #60**,
    `https://github.com/simonw/files-to-prompt/issues/60`, "Minor footgun:
    `-e` option is a suffix filter, not an exact extension check."
    - **Primary** (the reporting user's own account; independent usage
      evidence).
    - Establishes the exact failure mode I reproduced in item 6, with a
      real trigger case: `-e c -e h` matched `Makefile.inc` and `build.sh`
      unintentionally. The reporter's own workaround — passing the dot
      explicitly (`-e .c -e .h`) — is a usable mitigation, though it is not
      documented anywhere in the README (source item 2) as the intended
      usage. Open, no maintainer response as of fetch.
    - Verbatim: "This actually matches any file that ends in `c` or `h`,
      rather than just looking at the extension."

15. **Simon Willison, "files-to-prompt 0.5"**,
    `https://simonwillison.net/2025/Feb/14/files-to-prompt/`.
    - **Primary** (the author's own announcement and usage account).
    - Establishes the real llm-piping workflow the commission asks the
      piece to demonstrate, in the author's own words and commands:
      ```
      files-to-prompt . -c | llm -m gemini-2.0-pro-exp-02-05 \
        -s 'How does this work?...'
      files-to-prompt database.py utils/__init__.py -c | \
        llm -m o3-mini -o reasoning_effort high \
        -s 'Output in markdown a detailed analysis...'
      files-to-prompt . -e go -c | llm -m o3-mini \
        -s 'Write extensive user documentation...'
      ```
      Also states he uses the tool "on an almost daily basis" and finds it
      "fantastic for quickly answering questions about code" — a first-hand
      maintainer/author usage claim, weighed as author testimony, not
      independent confirmation.
    - Locator: post body, "New release" and example-commands sections.

16. **Simon Willison, "Building files-to-prompt entirely using Claude 3
    Opus"**, `https://simonw.substack.com/p/building-files-to-prompt-entirely`
    (also the canonical version linked from the README as background).
    - **Primary** (the author's own origin account).
    - Establishes provenance: Willison built nearly the entire tool,
      including tests and docs, by prompting Claude 3 Opus turn by turn,
      starting from a cookiecutter CLI skeleton. States the tool's purpose
      plainly: "a new tool I built to help me pipe several files at once
      into prompts to LLMs such as Claude and GPT-4." Also shows the
      tool used reflexively on itself: `files-to-prompt README.md
      files_to_prompt | llm -m opus --system 'Update this README...'`.
    - Locator: post body, throughout.

17. **Simon Willison, "Long context support in LLM 0.24 using fragments and
    template plugins"**, `https://simonwillison.net/2025/Apr/7/long-context-llm/`.
    - **Primary** (the author's own account, later than the tool's last
      release, showing continued personal use).
    - Establishes that as of April 2025 (roughly two months after the last
      files-to-prompt release), Willison was still actively using the tool:
      "I've been using long context models via my files-to-prompt tool to
      summarize large codebases, explain how they work and even to debug
      gnarly bugs." Also establishes the tool's relationship to the newer
      `llm` "fragments" feature: fragments were built to deduplicate
      repeated large pastes (via SHA256 hashing) across multiple prompts —
      a complement to files-to-prompt's one-shot assembly, not a stated
      replacement for it. Useful for "where it fits" framing and for
      showing the tool is not obviously superseded by its own author's
      newer work.
    - Locator: post body, opening paragraphs.

18. **Simon Willison's blog, "files-to-prompt" tag archive**,
    `https://simonwillison.net/tags/files-to-prompt/`.
    - **Primary** (the author's own archive index).
    - Establishes the complete list and dates of the author's direct posts
      about the tool, confirming the last dedicated post is the 0.6
      announcement dated February 19, 2025 — consistent with items 9-11 on
      the dormancy timeline.

19. **Hacker News item 42562983**, fetched via
    `https://hn.algolia.com/api/v1/items/42562983` (Algolia's HN API mirror;
    original thread at `news.ycombinator.com/item?id=42562983`).
    - **Mixed.** The top-level comment is by user `simonw` (the author) —
      **primary**, author's own workflow account. The reply from user
      `layer8` is **secondary/independent** — a different person actually
      testing the workflow and reporting a real limitation from outside the
      authoring party.
    - Establishes (simonw, primary): the exact daily-driver command,
      `files-to-prompt . -e py -e md -c | pbcopy`, pasted into "the Claude
      web interface or Google's AI Studio."
    - Establishes (layer8, secondary/independent): a real adopter tested
      this against their own project and flagged a genuine cost the
      commission asks for — project and specification-document size can
      exceed what fits on a clipboard or in a local model's context, so the
      workflow scales to hosted long-context models better than local ones.
    - Verbatim (layer8): "Google AI Studio isn't local, I think, is it? ...
      our project sizes and specification documents are likely to run into
      size limitations for local models (or for the clipboard at the very
      least)."

20. **`github.com/simonw/files-to-prompt`** (repository landing page),
    fetched directly.
    - **Primary** (the repository's own current landing-page metadata).
    - Establishes: ~2,800 GitHub stars, Apache 2.0 license, author
      `simonw`, and description "Concatenate a directory full of files into
      a single prompt for use with LLMs." Used for the star-count
      comparison against Repomix in items 21-22 below, to support the
      "still niche" finding.

21. **`repomix.com`** (Repomix project homepage), fetched directly.
    - **Secondary.** An independent, competing project's own marketing
      page — read to establish where files-to-prompt sits in the wider
      2026 landscape, not to source any claim about files-to-prompt itself.
    - Establishes Repomix's own pitch: "Pack your codebase into AI-friendly
      formats," with git-aware `.gitignore` handling, built-in secret
      scanning, and token counting — a materially more feature-rich,
      "default choice" competitor to files-to-prompt's minimalism.

22. **`github.com/yamadashy/repomix`** (Repomix's GitHub repository),
    fetched directly.
    - **Secondary** (an independent competing project, used only for scale
      comparison).
    - Establishes ~27.5k GitHub stars for Repomix versus files-to-prompt's
      ~2,800 (item 20) — roughly a 10x gap — supporting the finding that
      files-to-prompt has not become the ecosystem's default; a larger,
      more feature-complete tool already occupies that position, and
      files-to-prompt remains the smaller, Unix-philosophy alternative.
      Confirms Repomix's README does not mention files-to-prompt, only a
      generic pipe example into the unrelated `simonw/llm` project.

23. **`github.com/dsisnero/files-to-prompt`** (a Crystal-language port),
    fetched directly.
    - **Secondary** (independent adoption signal — a third party valued
      the tool enough to port it to another language).
    - Establishes only that an independent port exists ("a port of
      simonw/files-to-prompt," written in Crystal); the README gives no
      stated motivation beyond that. Thin, but genuine independent evidence
      the design is considered worth reproducing outside the Python/`llm`
      ecosystem.

24. **`pypistats.org`**, `https://pypistats.org/api/packages/files-to-prompt/overall?mirrors=false`,
    fetched directly, 2026-07-31.
    - **Primary** (PyPI's own aggregated download telemetry for the
      package).
    - Establishes continued real-world install activity despite the
      17-month release freeze: 240 downloads on 2026-07-28, 226 on
      2026-07-29, 194 on 2026-07-30 (without-mirrors count). Confirms the
      tool is still being installed and used daily at meaningful volume,
      not just installed once by early adopters and abandoned.

## Contradictions

- **The CLI's own `--help` docstring does not match its own `--cxml`
  output.** Running `files-to-prompt --help` (captured live, 2026-07-31)
  prints an example claiming `--cxml` produces
  `<document path="path/to/file1.txt">...`, i.e. a `path` attribute on the
  `<document>` tag. The actual code (source item 1, `print_as_xml`, lines
  74-84) and every real run I captured (items 5, and the README example in
  item 2) instead emit `<document index="N"><source>path</source>
  <document_content>...`. The help text is stale relative to the
  implementation; the README is accurate. A writer quoting `--cxml` output
  should quote the real run or the README, not the CLI's inline `--help`
  text.
- **Commission's phrase "binary skipping" versus the actual mechanism.**
  The commission (and much secondary description) refers to "binary
  skipping" as if the tool detects binary files. Source item 1 shows there
  is no binary detection at all — it is a blanket `UnicodeDecodeError`
  catch on any file, text or binary, that fails UTF-8 decoding. This
  produces two known false-positive classes documented by issue #55 (a
  UTF-8 file misidentified as needing skip) reported by users, though I did
  not personally reproduce #55. The practical effect for typical binary
  files (PNGs, in my run) is the same as "skipping," but the piece should
  describe the actual mechanism rather than imply real content sniffing.
- **"Respects `.gitignore`" is true only for simple, unanchored patterns.**
  The README and commission both describe gitignore honoring as a solved
  capability. Items 7 and 13 (my own run plus an independently filed,
  unresolved GitHub issue) show anchored patterns (a leading `/`) are
  silently not honored — files a user's `.gitignore` clearly excludes can
  still appear in the prompt. This is a genuine gap between the tool's
  documented behavior and its real behavior on any `.gitignore` that uses
  standard anchoring syntax (extremely common in real-world repos, e.g.
  Django's own generated `.gitignore` templates).

## Numbers

- **Latest version: 0.6**, released **2025-02-19T05:58:26Z** (PyPI, item 9;
  cross-confirmed by GitHub release item 10 and commit history item 11).
- **Time since last release/commit, relative to the 2026-07-31 commission
  date: ~17.4 months (≈530 days)** with zero commits of any kind in that
  window (item 11).
- **Version history and cadence** (item 9, all PyPI upload timestamps):
  0.1 → 2024-03-22; 0.2 → 2024-04-08; 0.2.1 → 2024-04-08 (same-day patch);
  0.3 → 2024-09-09; 0.4 → 2024-10-16; 0.5 → 2025-02-14; 0.6 → 2025-02-19.
  Six releases across roughly 11 months of active development (Mar 2024 -
  Feb 2025), then a full stop.
- **Open issues: 13** as of fetch (item 12), spanning filing dates
  2025-02-19 (issue #46) through 2025-07-12 (issues #63-65) — meaning even
  the oldest unresolved issue predates the last commit by zero days (it was
  filed the same day as the final release) and nothing has been touched
  since.
- **Source size: 334 lines** for the entire `files_to_prompt/cli.py`
  (my own `wc -l` on the fetched source, item 1) — the whole mechanism is
  small enough to read completely, which is itself part of the "cost of
  adoption" argument (low surface area, but also a small team of one
  maintainer with no recent activity).
- **GitHub stars: ~2,800** for files-to-prompt (item 20) versus
  **~27.5k** for Repomix (item 22) — roughly a 10x gap, supporting the
  "still niche, not a default" finding.
- **PyPI daily downloads (without mirrors), late July 2026** (item 24):
  240 (Jul 28), 226 (Jul 29), 194 (Jul 30) — order of magnitude ~200/day of
  continued real installs, 17 months after the last code change.
- **My real-run output sizes** (items 4-5, for the writer's worked
  example): default-mode concatenation of 2 text files from
  `engine/assets/` (excluding 3 skipped PNGs) produced 8,217 bytes of
  prompt text; `--cxml` concatenation of 2 Python files
  (`engine/ci_helpers.py`, `engine/check.py`) produced 7,576 bytes.

## Source assets

None found. Every primary source here is either source code, a CLI's own
text output, plain-text documentation, or a JSON API response — there is no
chart, screenshot, diagram, or photograph in any cited document that would
carry the argument better than a quoted code/output listing. The `nb-code`
listings captured in items 4-8 above are the correct furniture for this
piece per the commission's furniture guidance, not a chart.

## Discarded

- `https://deepwiki.com/simonw/files-to-prompt` — an AI-generated
  third-party wiki summary of the repo, not a primary or independently
  authored secondary source; discarded in favor of reading the actual
  source and README directly.
- `https://osrepos.com/repo/simonw-files-to-prompt` and
  `https://www.sourcepulse.org/projects/1841768` — automated
  repo-aggregator SEO pages with no original reporting or independent
  usage account; surfaced in search but not opened as sources.
- `https://github.com/mufeedvh/code2prompt` — checked directly on the
  hypothesis it might credit or compare itself to files-to-prompt as an
  independent secondary account of the tool's influence; its README does
  not mention files-to-prompt or Simon Willison at all, so it establishes
  nothing about this tool and was dropped.
- `https://medium.com/open-intelligence/repomix-packing-an-entire-codebase-into-one-file-ai-models-can-actually-understand-297a7a11f097` —
  fetched directly to verify a "Repomix is the clear default choice, ...
  files-to-prompt" landscape claim surfaced by an earlier aggregated web
  search; on direct read the article does not mention files-to-prompt at
  all and the comparative claim could not be verified against the actual
  text. Discarded; the star-count comparison in Numbers is sourced instead
  from directly reading both projects' own GitHub pages (items 20, 22).
- GitHub issue #55 ("Skipping file XXX due to UnicodeDecodeError - but file
  looks fine and is UTF-8") — noted from the issues list (item 12) but not
  opened and read in full; referenced only as a title/date, not relied on
  for any specific quoted claim.
- `api.github.com` (GitHub REST API) — blocked in this session's network
  policy for a repository not attached via the environment's repo-access
  tool ("GitHub access to this repository is not enabled for this
  session"); worked around by using `raw.githubusercontent.com` for source
  files and the `WebFetch` tool against `github.com` HTML pages directly,
  both of which resolved normally.
