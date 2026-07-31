# Draft handoff — expert-tools/files-to-prompt (writer, round 01)

## Original work

The piece's one act of original work: it takes the researcher's real, captured
runs of `files-to-prompt` against this repository's own tree (and disposable
scratch directories) and uses them, alongside a full read of the 334-line
`cli.py`, to build an argument the README does not make on its own — that
the tool's two documented strengths (clean binary exclusion, a citable
`--cxml` structure) and its two undocumented failures (the `-e` suffix-match
footgun, the anchored-`.gitignore` leak) trace to the *same* implementation
choice: `should_ignore`/`process_path` do exactly what a straightforward
`fnmatch`-on-basename and `UnicodeDecodeError`-catch would do, no more and no
less, and reading those seven lines of source explains every real behavior
demonstrated in the piece, working and broken alike. That causal chain (source
→ real run → independently filed issue confirming the same run in the wild) is
the connective tissue the README, the release notes, and any one of those
sources individually do not supply.

## Article and asset paths changed

- `library/expert-tools/files-to-prompt.html` (drafted from the initialized
  skeleton; no pre-existing assets in this slug's directory, none added).

No source assets or charts: the evidence record found no chart-worthy series
and no primary-document image, matching its "Source assets: None found"
section. Furniture used: two `nb-code` real-run listings (default mode,
`--cxml`), one `nb-code` source listing (`should_ignore`, verbatim), one
`nb-stat-strip` (17 months / 13 open issues / ~200-a-day installs), and one
`nb-note nb-note-strong` Verdict closing the piece.

## Proof result

```
./nb check .nb-work/expert-tools/files-to-prompt/library/expert-tools/files-to-prompt.html \
  --series expert-tools --library /home/user/library
```
`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

Two rounds of warnings were fixed before the clean run, not carried forward:
- `W-BANNED-TERM 'em-dash': 12 uses` (limit 4) — rewrote every non-quoted
  instance into a period, comma, or colon per the house punctuation rules;
  one em-dash inside a verbatim-quoted `nb.css` comment (the real captured
  stdout) was deliberately left as the one unavoidable literal quotation, and
  the final count came in under the limit without needing to touch it.
- Three `W-SENTENCE-DENSITY` warnings (53, 44, 43 words) — split each flagged
  sentence in place; no content was cut, only re-sentenced.

No warnings were left unresolved.

## Sourcing

20 sources, all read directly per the researcher's evidence record: the
tool's own `cli.py` (full source), its README, its test suite, six of the
writer's/researcher's own real runs (default mode, `--cxml`, the `-e`
footgun, the working unanchored-gitignore case, the anchored leak — all
cited against the PyPI project page as the installed artifact, since these
are first-hand executions rather than URL-hosted documents), two GitHub
issues independently filed by non-author users (#46, #60), the PyPI JSON API
version history, the GitHub release and commit-history pages, the open
issues list, PyPI Stats download counts, three Simon Willison posts (origin,
the 0.5 announcement with the daily-use quote and piped `llm` commands, and
the April 2025 post confirming continued personal use), the files-to-prompt
and Repomix GitHub landing pages (star-count comparison), and one Hacker
News comment from an independent adopter (`layer8`) on context-size limits.
Every capability claim in the piece (binary handling, `--cxml` structure,
extension filtering, gitignore honoring and its anchored-pattern gap) traces
to source code or a real, captured run, not to the README's description of
itself, matching the evidence record's own finding that the README and the
implementation agree except where the CLI's own stale `--help` text does not
(a discrepancy the piece deliberately routes around by quoting the real run
and the README instead of `--help`).

The maintenance verdict carries the honest caveat forward exactly as the
evidence stated it: last commit and last release both 2025-02-19, ~17 months
stale as of 2026-07-31, 13 open issues, against continued author use and
roughly 200 PyPI installs a day. The closing `nb-note-strong` Verdict weighs
this as a real, arguable risk rather than a disqualifier, consistent with the
evidence record's own framing (the pick fails none of the commission's three
named disqualifiers — default, unmaintained, only-popular — even though the
second is a genuine open question) and consistent with the researcher's
choice not to escalate `REQUEST correspondent`.

## Remaining question

None. Evidence and voice guide were sufficient throughout; no researcher or
writing-coach request was needed.
