# Evidence: expert-tools/visidata (01)

This record supports an article built on one changing move: exploratory analysis
done as interactive keystrokes over a loaded sheet in VisiData (`vd`), replacing
the write-run-tweak loop of a throwaway pandas or SQL session. Every keybinding
the article will show is confirmed against current source on the `develop` branch
(the base for release v3.4, 2026-06-30) and against the official docs at
visidata.org: frequency table (`F`), add aggregator (`+`), Python-expression
computed column (`=`), pivot (`W`), melt (`M`). The async/incremental loader
claim — that you can explore a sheet before a large file finishes loading — is
grounded firsthand in both the source (`Sheet.reload` is `@asyncthread`; loaders
are generators that `yield` rows one at a time) and the loaders docs, and in the
author's own 2020 blog post. Maintenance is healthy and single-vendor-light:
creator Saul Pwanson plus one docs/packaging maintainer, GPL-3.0, regular
releases. The evidence is thin in one place worth flagging to the writer: the
exact thread-control keystrokes (Ctrl+T threads sheet, Ctrl+C cancel) come from
the docs/manpage layer, not re-verified line-by-line against source, so the piece
should lean on the loader mechanism it can prove rather than on cancel-key
trivia. No legitimate spendable source-asset visual exists; the demonstration
belongs in authored code/transcript furniture, not a screenshot.

## Sources

```text
URL:         https://www.visidata.org/
Kind:        primary — the project's own home page, authored by the project
Establishes: current release and date; one-line description; supported I/O formats
Paraphrase:  VisiData is "an interactive multitool for tabular data" that combines
             "the clarity of a spreadsheet, the efficiency of the terminal, and the
             power of Python." Latest version v3.4, released Jun 30, 2026.
             © Saul Pwanson 2017-2026. Input formats listed include CSV, TSV, fixed-
             width text, Excel (.xls/.xlsx), JSON/JSON-Lines, HTML, YAML, HDF5,
             NumPy (.npy/.npz), pandas DataFrame, SAS/SPSS/Stata, Shapefile (.shp),
             pcap, SQLite (.db), .zip, and git repos. Output formats include TSV,
             CSV, fixed-width, JSON, JSONL, GeoJSON, HTML tables, SQLite, Markdown,
             org-mode Markdown, and NumPy.
Locators:    landing page; version banner; "Supported formats" listing
Quote:       "an interactive multitool for tabular data"
```

```text
URL:         https://www.visidata.org/docs/
Kind:        primary — official documentation index
Establishes: the documentation topic set past the README; that the getting-started
             page carries a video demo link, not an inline usage screenshot
Paraphrase:  The docs index lists dedicated pages for Loading data, Navigation,
             Rows, Columns, Grouping data and descriptive statistics (frequency
             table, pivot table, aggregators), Creating sheets/rows/columns,
             Combining datasets, Graphs, Supported formats, and more. Full command
             reference is reachable via `man vd`, the quick reference, or Ctrl+H in
             the app. The page links a "VisiData video demo" (youtu.be/N1CBDTgGtOU)
             and shows only the logo image (/img/s9TnkaZwpa-1000.jpeg); no inline
             screenshot or demo GIF of the TUI in use.
Locators:    docs index; getting-started body
```

```text
URL:         https://www.visidata.org/docs/group/
Kind:        primary — official "Grouping data" documentation
Establishes: the user-facing keystrokes for frequency table, pivot, and the
             aggregator-add flow, as documented (not just as coded)
Paraphrase:  Shift+F opens the frequency table. `+` followed by an aggregator name
             (e.g. `+ sum`) adds that aggregator to the current column. Shift+W
             (pivot) builds a pivot table, pressed on the column holding the
             dependent categorical variable to pivot.
Locators:    "Grouping data and descriptive statistics"
```

```text
URL:         https://www.visidata.org/docs/columns/
Kind:        primary — official "Columns" documentation
Establishes: the documented keystroke for a Python-expression computed column
Paraphrase:  `=` (addcol-expr) creates a new column from a Python expression, with
             existing column names available as variables; the entry syntax is
             `name=expr`, e.g. `total = Units * Unit_Cost`.
Locators:    "Creating derivative columns"
Quote:       "create new column from Python expression, with column names as variables"
```

```text
URL:         https://www.visidata.org/docs/api/loaders
Kind:        primary — official developer docs on how loaders work
Establishes: THE async/incremental loader claim firsthand — exploration begins
             before the file finishes loading
Paraphrase:  The basic TableSheet reload/iterload structure yields an asynchronous
             loader by default. Because rows are yielded one at a time they become
             available as they load, and `reload` is decorated `@asyncthread`, which
             launches it in a new thread; the UI stays responsive during load.
Locators:    loaders overview, "asynchronous loader by default" section
Quote:       "the basic TableSheet `reload` and `iterload` structure results in an
             asynchronous loader by default."
             "Since rows are yielded one at a time, they become available as they
             are loaded, and `reload` itself is decorated with an `@asyncthread`,
             which causes it to be launched in a new thread."
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/freqtbl.py
Kind:        primary — VisiData source (frequency-table feature)
Establishes: exact keybinding + command longname + helpstr for the frequency table,
             confirmed in code (not from memory)
Paraphrase:  Verbatim source:
             Sheet.addCommand('F', 'freq-col', 'vd.push(makeFreqTable(sheet, cursorCol))',
               'open Frequency Table grouped on current column, with aggregations of other columns')
             Sheet.addCommand('gF', 'freq-keys', ...,
               'open Frequency Table grouped by all key columns on source sheet, with aggregations of other columns')
             Sheet.addCommand('zF', 'freq-summary', ...,
               'open one-line summary for all rows and selected rows')
             So the frequency table is `F` (freq-col); `gF` groups by all key columns.
Locators:    module-level addCommand block at end of freqtbl.py
Quote:       "Sheet.addCommand('F', 'freq-col', 'vd.push(makeFreqTable(sheet, cursorCol))', 'open Frequency Table grouped on current column, with aggregations of other columns')"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/aggregators.py
Kind:        primary — VisiData source (aggregators feature)
Establishes: exact keybindings for adding aggregators, and the built-in aggregator set
Paraphrase:  Verbatim source:
             Sheet.addCommand('+', 'aggregate-col', 'addAggregators([cursorCol], chooseAggregators())', 'Add aggregator to current column')
             Sheet.addCommand('z+', 'memo-aggregate', ..., 'memo result of aggregator over values in selected rows for current column')
             ColumnsSheet.addCommand('g+', 'aggregate-cols', ..., 'add aggregators to selected source columns')
             Sheet.addCommand('', 'addcol-aggregate', ..., 'add column(s) with aggregator of rows grouped by key columns')
             So `+` adds an aggregator to the current column and prompts for which
             (chooseAggregators); `g+` adds to multiple selected columns on the
             Columns sheet. Registered aggregators include min, max, avg, mean,
             median, mode, sum, distinct, count, stdev, list, keymin, keymax, and a
             family of quantile/percentile aggregators (q3/q4/q5/q10, p10..p99).
Locators:    module-level addCommand block; aggregator registrations
Quote:       "Sheet.addCommand('+', 'aggregate-col', 'addAggregators([cursorCol], chooseAggregators())', 'Add aggregator to current column')"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/expr.py
Kind:        primary — VisiData source (expression columns)
Establishes: exact keybinding for the Python-expression computed column, confirmed in code
Paraphrase:  Verbatim source:
             Sheet.addCommand('=', 'addcol-expr', ..., 'create new column from Python expression, with column names as variables')
             Sheet.addCommand('g=', 'setcol-expr', ..., 'set current column for selected rows to result of Python expression')
             Sheet.addCommand('z=', 'setcell-expr', ..., 'evaluate Python expression on current row and set current cell...')
             Sheet.addCommand('gz=', 'setcol-iter', ..., 'set current column for selected rows to the items in result of Python sequence expression')
             So `=` is the computed-column-from-expression command; `g=` overwrites
             the current column for selected rows via expression.
Locators:    module-level addCommand block in expr.py
Quote:       "Sheet.addCommand('=', 'addcol-expr', ... , 'create new column from Python expression, with column names as variables')"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/pivot.py
Kind:        primary — VisiData source (pivot feature)
Establishes: exact keybinding + longname + helpstr for pivot
Paraphrase:  Verbatim source:
             Sheet.addCommand('W', 'pivot', 'vd.push(makePivot(sheet, keyCols, [cursorCol]))',
               'open Pivot Table: group rows by key column and summarize current column')
             So pivot is `W` (Shift+W): it groups by the sheet's key columns and
             summarizes the current column.
Locators:    module-level addCommand in pivot.py
Quote:       "Sheet.addCommand('W', 'pivot', 'vd.push(makePivot(sheet, keyCols, [cursorCol]))', 'open Pivot Table: group rows by key column and summarize current column')"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/features/melt.py
Kind:        primary — VisiData source (melt/unpivot feature)
Establishes: exact keybindings + longnames + helpstrs for melt and melt-regex
Paraphrase:  Verbatim source:
             Sheet.addCommand('M', 'melt', 'vd.push(openMelt())',
               'open Melted Sheet (unpivot), with key columns retained and all non-key columns reduced to Variable-Value rows')
             Sheet.addCommand('gM', 'melt-regex', 'vd.push(openMelt(vd.inputRegex("regex to split colname: ", value="(.*)_(.*)", type="regex-capture")))',
               'open Melted Sheet (unpivot), with key columns retained and regex capture groups determining how the non-key columns will be reduced to Variable-Value rows')
             So melt (unpivot) is `M` (Shift+M); `gM` is the regex-driven variant.
Locators:    module-level addCommand in features/melt.py
Quote:       "Sheet.addCommand('M', 'melt', 'vd.push(openMelt())', 'open Melted Sheet (unpivot), with key columns retained and all non-key columns reduced to Variable-Value rows')"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/sheets.py
Kind:        primary — VisiData source (base Sheet class)
Establishes: that async loading is the DEFAULT at the base-class level, and how rows
             are added incrementally during load
Paraphrase:  The base Sheet.reload is decorated `@asyncthread` and documented "Async."
             Its loader iterates iterload() and calls addRow on each row inside a
             Progress context, yielding as it goes. Verbatim:
               @asyncthread
               def reload(self):
                   'Load or reload rows and columns from ``self.source``.  Async.  Override resetCols() or loader() in subclass.'
             and:
               def _iterloader(self):
                   self.rows = []
                   with vd.Progress(gerund='loading', total=0):
                       max_rows = self.options.max_rows
                       for i, r in enumerate(self.iterload()):
                           if self.precious and i >= max_rows:
                               break
                           self.addRow(r)
                           yield r
             The `max_rows` option defaults to 1_000_000_000:
               vd.option('max_rows', 1_000_000_000, 'number of rows to load from source')
Locators:    Sheet.reload, Sheet.loader, Sheet._iterloader; option registrations
Quote:       "'Load or reload rows and columns from ``self.source``.  Async.  Override resetCols() or loader() in subclass.'"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/visidata/loaders/csv.py
Kind:        primary — VisiData source (CSV loader)
Establishes: that a concrete loader is a generator yielding rows one at a time, so
             rows appear as they parse rather than after a full read
Paraphrase:  CSVSheet.iterload reads with csv.reader and `yield row` inside a loop,
             wrapping parse errors as TypedExceptionWrapper rather than aborting.
             There is no @asyncthread on iterload itself; the async behavior comes
             from the base reload wrapping it (see sheets.py).
Locators:    CSVSheet.iterload
Quote:       "while True: ... row = next(rdr) ... if row: yield row"
```

```text
URL:         https://github.com/saulpw/visidata/blob/develop/CHANGELOG.md
Kind:        primary — VisiData's own release changelog
Establishes: release history and cadence; that development is active and versioned
Paraphrase:  Recent releases: v3.4 (2026-06-30), v3.3 (2025-09-07), v3.2
             (2025-06-15), v3.1 (2024-10-14), v3.0 (2023-12-30), v2.11.1
             (2023-07-16), v2.11 (2023-01-15). The 3.x line ships roughly every
             2-3 quarters. The changelog also records the `max_rows` "stop loading
             early" option (#2356) and cmdlog moving to longnames instead of
             keystrokes.
Locators:    top of CHANGELOG.md; per-version headers
```

```text
URL:         https://github.com/saulpw/visidata
Kind:        primary — the project's repository page
Establishes: maintainer identity, license, community scale, open-issue posture
Paraphrase:  About: "A terminal spreadsheet multitool for discovering and arranging
             data." License GPL-3.0. ~9.2k stars, 61 open issues at time of reading.
             Credits: "VisiData is conceived and developed by Saul Pwanson
             <vd@saul.pw>. Anja Kefala <anja.kefala@gmail.com> maintains the
             documentation and packages for all platforms." Active `develop` branch
             with thousands of commits.
Locators:    repo header (About, license, issue count); README credits
Quote:       "VisiData is conceived and developed by Saul Pwanson <vd@saul.pw>. Anja Kefala <anja.kefala@gmail.com> maintains the documentation and packages for all platforms."
```

```text
URL:         https://www.visidata.org/blog/2020/unloaded/
Kind:        primary — the author's own blog post ("Unloaded Sheets")
Establishes: the design intent behind deferred/async loading, in the creator's words
Paraphrase:  Saul Pwanson (posted 2020-02-10; edited by Anja Kefala 2020-02-11)
             explains that a freshly created sheet is "unloaded" and stays dormant
             and lightweight until it is about to be drawn, at which point
             sheet.reload() runs in a separate thread and keeps VisiData responsive.
             To avoid thrashing on huge inputs, VisiData loads lazily: given 100GB
             of CSVs opened with `vd *.csv`, it loads only the top sheet, and others
             load on demand (e.g. select sheets on the Sheets Sheet and press
             g Ctrl+R, reload-selected).
Locators:    body; "100GB of .csv files" example
Quote:       "as it's about to be drawn for the first time, the sheet starts its
             loading process ... in a separate thread"
```

```text
URL:         https://news.ycombinator.com/item?id=28826348
Kind:        secondary — community discussion (context for critiques)
Establishes: the common, credible caveat that VisiData is not a general spreadsheet
Paraphrase:  Commenters frame VisiData as built for exploring and reshaping tabular
             data at speed, and note that for spreadsheet-style work (formulas,
             presentation, collaborative editing) Excel or Google Sheets remain the
             right tool. Repetition here supports that the caveat is widely held,
             not that any single figure is true.
Locators:    thread "VisiData is not a spreadsheet..."
```

```text
URL:         https://news.ycombinator.com/item?id=36502435
Kind:        secondary — community discussion (context for adoption cost)
Establishes: the learning-curve caveat around modal, vim-style keystrokes
Paraphrase:  Users describe VisiData as vim-keybinding-driven: early on you look up
             most commands, but it then lets you work much faster; the built-in menu
             and Ctrl+H command list ease discovery. Supports the "modal keystroke
             learning curve" adoption cost, as reported opinion, not as measured fact.
Locators:    top-level thread comments
```

## Contradictions

- **"Async loader" vs. a hard row cap.** The loaders docs sell responsive,
  load-while-you-explore behavior, but source shows precious sheets stop at
  `options.max_rows`. The default is 1,000,000,000 rows, so in practice the cap
  rarely bites, yet the article should not imply unbounded streaming: past a
  billion rows (or a lowered `max_rows`) the sheet is truncated, not merely slow.
- **"Explore before it finishes loading" is real but bounded by the operation.**
  Navigation and viewing are immediate while a background thread appends rows, but
  operations that must see the whole column (a complete frequency count, a sort,
  an aggregate total) are only correct once loading finishes; running them mid-load
  reflects rows loaded so far. The blog and loaders docs support incremental
  availability; neither claims mid-load aggregates are final. The writer should not
  overstate this.
- **Where a notebook or SQL still wins.** The commission's angle is that VisiData
  replaces the write-run-tweak loop. The honest boundary, supported by community
  discussion and by the tool's own scope: for reproducible multi-step pipelines,
  version-controlled analysis, custom plotting, or joins/aggregations over data too
  large for one machine's memory, a notebook (pandas) or a database (SQL) remains
  the better tool. VisiData's cmdlog can replay a session, which narrows but does
  not close this gap. This is a real limit on the commissioned claim, not a defect.
- No contradiction found on the keybindings themselves: docs and source agree on
  F, +, =, W, M across the checked pages.

## Numbers

```text
Figure: v3.4, released 2026-06-30 (current stable)
Owner:  visidata.org home page / CHANGELOG.md
Scope:  latest tagged release as of research date 2026-08-05
```

```text
Figure: release cadence ~ one minor release every 2-3 quarters in the 3.x line
Owner:  CHANGELOG.md (v3.0 2023-12-30 -> v3.1 2024-10-14 -> v3.2 2025-06-15 -> v3.3 2025-09-07 -> v3.4 2026-06-30)
Scope:  3.x series, Dec 2023 - Jun 2026
```

```text
Figure: options.max_rows default = 1,000,000,000 rows
Owner:  visidata/sheets.py (vd.option('max_rows', 1_000_000_000, ...))
Scope:  per-sheet load cap for "precious" sheets; above this the sheet truncates
```

```text
Figure: ~9,200 GitHub stars; 61 open issues
Owner:  github.com/saulpw/visidata repo header
Scope:  point-in-time reading on 2026-08-05; both drift over time
```

```text
Figure: 100 GB of CSVs handled by lazy per-sheet loading
Owner:  author's blog "Unloaded Sheets" (Saul Pwanson, 2020-02-10)
Scope:  illustrative example of deferred loading with `vd *.csv`, not a benchmark
```

## Source assets

```text
Asset: None found (no legitimate spendable visual)
Shows: The docs getting-started page carries only the VisiData logo and a link to
       a YouTube video demo; there is no official, argument-bearing screenshot of a
       frequency table, pivot, or expression column that a crop could carry. A
       decorative TUI screenshot would not advance the argument.
Crop:  n/a
```

Writer guidance (per commission and series prompt): show the changing move as
authored code/transcript furniture in the article's own code blocks — a short
shell session (`vd sample.csv`) followed by the exact keystrokes (`F`, then `+`
choosing `sum`/`avg`, then `=` for a computed column, then `W` for a pivot) — not
as an external screenshot asset. Every keystroke shown is confirmed above; render
them exactly (`F`, `+`, `=`, `W`, `M`; `gF`, `g+`, `gM` for the group variants).

## Discarded

```text
URL: https://www.visidata.org/docs/async/            reason: 404 — not the real path; async loading is documented at /docs/api/loaders and threads at /docs/api/async
URL: https://raw.githubusercontent.com/saulpw/visidata/develop/visidata/features/freqtbl.py   reason: 404 — freqtbl lives at visidata/freqtbl.py, not under features/
URL: https://raw.githubusercontent.com/saulpwanson/visidata/...   reason: wrong org — the repo is saulpw/visidata (owner handle "saulpw", not "saulpwanson")
URL: https://sphinx-visidata.readthedocs.io/en/latest/dev-guide.html   reason: stale VisiData 0.59 docs; superseded by visidata.org for a current-version article
URL: https://www.visidata.org/docs/api/commands (v2.0)   reason: version-stamped v2.0 API page; keybindings re-verified against develop source instead
```

## Note to the orchestrator on unresolved items

- Thread-control keystrokes (Ctrl+T Threads Sheet; Ctrl+C / z Ctrl+C / gz Ctrl+C
  to cancel) are documented in the async/threads docs and manpage but were not
  re-confirmed line-by-line against source in this pass. The article's argument
  does not need them; if the writer shows a cancel key, confirm it against
  visidata/threads.py before shipping. The core five moves (F, +, =, W, M) and the
  async loader mechanism are fully source-verified and safe to build on.
