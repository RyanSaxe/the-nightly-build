# Evidence record: technical/python-lazy-imports-pep-810 (01)

The owning documents establish the mechanism, the syntax, the API surface, the
dates, and the release status firsthand. PEP 810 and the live Python 3.15
What's New fix every identifier the walkthrough needs (`lazy` soft keyword,
`types.LazyImportType`, `sys.lazy_modules`, `__lazy_modules__`, `__lazy_import__`,
the `-X lazy_imports` / `PYTHON_LAZY_IMPORTS` / `sys.set_lazy_imports` controls,
and the three modes `normal`/`all`/`none`). The Steering Council acceptance,
the merged CPython implementation PR, and the PEP 790 release schedule pin the
status: 3.15 is at release candidate 3 as of today (2026-10-03), with 3.15.0
final dated 2026-10-09 — shipping through betas/RCs, stable imminent, not yet
released. The record is thin in exactly one place that matters for the original
contribution: no Python 3.15 interpreter (beta or RC) is reachable in this
environment through `uv` or on PATH, so the writer must use the
mechanism-demonstration fallback, not a measured before/after run. The
production figures all come from Meta's earlier *implicit* Cinder mechanism (and
PEP 690's lineage), not from PEP 810's own benchmarks; PEP 810 claims only that
its mechanism is performance-neutral.

## Sources

```text
URL:         https://peps.python.org/pep-0810/
Kind:        primary — the specification itself; it owns the syntax, semantics, API, and restrictions.
Establishes: Title "PEP 810 – Explicit lazy imports". Header fields: Status: Final; Type: Standards Track;
             Created: 02-Oct-2025; Python-Version: 3.15; Post-History: 03-Oct-2025; Resolution: 03-Nov-2025.
             Syntax: a soft keyword `lazy` placed before `import`/`from` at module level: `lazy import json`,
             `lazy from json import dumps`. A lazy import binds a `types.LazyImportType` proxy instead of the
             module/name; proxies are "resolved to the real object (reified) before they can be used."
             Mechanism: when an import is lazy, `__lazy_import__` is called instead of `__import__`; it adds the
             fully-qualified name to `sys.lazy_modules` (a set, "primarily for diagnostics and introspection")
             and returns a `types.LazyImportType`. A lazily imported module does NOT appear in `sys.modules`
             until first use; after reification it must appear in `sys.modules`.
             Reification trigger: "Accessing a lazy object (from a global variable or a module attribute)
             reifies the object." Reification is usually automatic but can be forced by calling the lazy
             object's `resolve()` method. `globals()` and accessing a module's `__dict__` do NOT trigger
             reification — they return the dict and lazy objects fetched through it stay lazy.
             Placement restrictions (SyntaxError otherwise): not inside functions, not inside classes, not
             inside try/except blocks, and `lazy from ... import *` is not allowed. `with` blocks ARE allowed
             (see Contradictions). Star imports are always eager.
             Error/side-effect timing: "Exceptions that would have occurred during an eager import ... now
             occur at the use of the lazy name." "Import-time side effects in lazily imported modules occur at
             first use of the binding, not at module import time."
             Global control + precedence: `-X lazy_imports=<mode>`, `PYTHON_LAZY_IMPORTS=<mode>`, and
             `sys.set_lazy_imports(mode, /)` (noted "primarily for testing"). Modes: "normal" (respect the
             `lazy` keyword only — the default), "all" (force all imports potentially lazy), "none" (force all
             eager). Precedence: `sys.set_lazy_imports()` highest, then `-X lazy_imports`, then
             `PYTHON_LAZY_IMPORTS`. `sys.get_lazy_imports()` returns the current mode as a string.
             Filter escape hatch: `sys.set_lazy_imports_filter(func)` with signature
             `func(importer: str, name: str, fromlist: tuple[str, ...] | None) -> bool`; `func=None` removes it.
             `sys.get_lazy_imports_filter()` returns the installed filter or None.
             Module opt-in without the keyword: a `__lazy_modules__` module-global sequence of fully-qualified
             names makes those imports potentially lazy; `["*"]` is NOT supported as built-in syntax (rejected).
             Performance claim (PEP's own): "Lazy imports have no measurable performance overhead ...
             performance-neutral"; after a successful reification "lazy imports have zero overhead."
             Motivation figures (NOT PEP 810's own benchmark — see Numbers/Contradictions): deferring until use
             "can reduce startup time by 50-70% in practice"; "Memory savings of 30-40% have been observed in
             real workloads." Stdlib analysis: "approximately 17% of all imports outside tests (nearly 3500
             total imports across 730 files) are already placed inside functions or methods ... to defer their
             execution."
Locators:    Header block (top of page); "Specification" syntax examples; "Lazy import mechanism"; the
             reification / `resolve()` / `__dict__` examples; "Global lazy imports control"; "Rejected Ideas"
             (the `with`-block decision); "Motivation"; "Performance".
Quote:       "A new soft keyword lazy is added ... only when it appears before import statements."
             "Accessing a lazy object (from a global variable or a module attribute) reifies the object."
             "Import-time side effects in lazily imported modules occur at first use of the binding, not at
             module import time."
```

```text
URL:         https://peps.python.org/pep-0790/
Kind:        primary — the official Python 3.15 release schedule; it owns the dates.
Establishes: PEP 790 "Python 3.15 Release Schedule", release manager Hugo van Kemenade.
             3.15.0 beta 1: Thursday 2026-05-07 ("No new features beyond this point.");
             beta 2: 2026-06-02; beta 3: 2026-06-23; beta 4: 2026-07-18;
             candidate 1: 2026-08-04; candidate 2: 2026-09-01; candidate 3: 2026-10-02;
             3.15.0 final: Friday 2026-10-09.
Locators:    "Release schedule" / "Actual" date list.
Quote:       "3.15.0 beta 1: Thursday, 2026-05-07"; "3.15.0 final: Friday, 2026-10-09".
```

```text
URL:         https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131/466
Kind:        primary — the Steering Council's own acceptance message (via the PEP author's quoted record).
Establishes: The SC "unanimously" accepted PEP 810, posted by Barry Warsaw on behalf of the Python Steering
             Council on 3 November 2025 (4:21pm). Conditions/recommendations attached: use `lazy` as the keyword
             (over `defer`); the keyword must appear first on the line (reject `from foo lazy import bar`);
             reject the dict-subclass alternative and reject `"*"` in `__lazy_modules__`; `.pth` files will not
             be adapted for lazy imports; ADD a `sys.get_lazy_imports()` to retrieve the active mode; the PEP
             must define the precedence order among env var, `-X` flag, and `sys.set_lazy_imports()`; take no
             position on import sorting.
Locators:    Acceptance post in the PEP 810 discussion thread, 2025-11-03.
Quote:       "The Steering Council is happy to unanimously accept 'PEP 810, Explicit lazy imports'."
Note:        The acceptance date (03-Nov-2025) matches the PEP header's Resolution field exactly.
```

```text
URL:         https://docs.python.org/3.15/whatsnew/3.15.html
Kind:        primary — the shipped CPython 3.15 documentation (served at 3.15.0rc3 as of today).
Establishes: What's New in Python 3.15 carries a "PEP 810: Explicit lazy imports" section with the same
             identifiers as the PEP: `lazy import json` / `lazy from pathlib import Path` examples; the
             `-X lazy_imports` option and `PYTHON_LAZY_IMPORTS` env var; `sys.set_lazy_imports()`,
             `sys.get_lazy_imports()`, `sys.set_lazy_imports_filter()`, `types.LazyImportType`, and the
             `__lazy_modules__` module attribute. Confirms the feature is documented and live in pre-release
             docs (RC stage), i.e. implemented, not merely proposed.
Locators:    "What's New In Python 3.15" → "PEP 810: Explicit lazy imports".
Quote:       example block: `lazy import json` / `lazy from pathlib import Path` with the comment "json and
             pathlib not loaded yet".
```

```text
URL:         https://github.com/python/cpython/pull/142351
Kind:        primary — the CPython implementation PR.
Establishes: Title "gh-142349: Implement PEP 810 - Explicit lazy imports"; state: merged; merged 2026-02-12;
             base python/cpython:main; references issue gh-142349; author pablogsal. This is the landing of
             the feature into CPython main ahead of the 3.15 beta series.
Locators:    PR header and merge banner.
Note:        Tracking issue is https://github.com/python/cpython/issues/142349 (gh-142349). The GitHub MCP
             tool is scoped to ryansaxe/the-nightly-build only and cannot read python/cpython; these fields
             come from the public PR page via web fetch. The PR page's prose summary mis-states one restriction
             (see Contradictions).
```

```text
URL:         https://developers.facebook.com/blog/post/2022/06/15/python-lazy-imports-with-cinder
Kind:        primary for Meta's own production figures; secondary relative to PEP 810. This is the EARLIER
             IMPLICIT mechanism (Cinder "Lazy Imports"), not PEP 810's explicit keyword.
Establishes: "Python Lazy Imports With Cinder", Germán Méndez Bravo, 2022-06-15. Instagram Server loads
             "about 28,000" modules at startup. Reload time was ~25 s (late 2021), regressed to as long as
             ~1.5 min by year-end 2021. With Cinder lazy imports: "~70% reduction in p50 reload time and a ~60%
             reduction in p90 reload time" for Instagram dev servers; "improvements between 50% to 70%" across
             other servers/tools, with "memory usage reduction of 20% to 40%"; "~12x less modules" loaded;
             daily circular-import errors fell "from ~80 ... every day to zero"; saved "hundreds of developer
             hours per day." Mechanism is implicit/transparent: every `import foo` creates a "deferred object"
             with no explicit keyword.
Locators:    Body sections on Instagram Server startup, reload metrics, and results.
Quote:       "~70% reduction in p50 reload time and a ~60% reduction in p90 reload time."
```

```text
URL:         https://engineering.fb.com/2024/01/18/developer-tools/lazy-imports-cinder-machine-learning-meta/
Kind:        primary for Meta's own figures; secondary relative to PEP 810. Also the EARLIER IMPLICIT Cinder
             mechanism, not PEP 810.
Establishes: "Lazy is the new fast: How Lazy Imports and Cinder accelerate machine learning at Meta", Germán
             Méndez Bravo, 2024-01-18. "up to 40 percent time to first batch (TTFB) improvements" on Meta's key
             AI workloads; "20 percent reduction in Jupyter kernel startup times." Mechanism explicitly
             transparent: Cinder "transparently deferring all imports as a default action." Does not report
             memory, module-count, reload-time, or developer-hour figures.
Locators:    Results / performance paragraphs.
Quote:       "up to 40 percent time to first batch (TTFB) improvements."
```

```text
URL:         https://lists.mercurial-scm.org/pipermail/mercurial-devel/2026-March/299426.html
Kind:        secondary — a practitioner (Mercurial) adapting production code to 3.15 behavior.
Establishes: Patch by Mads Kiilerich (2026-03-28; thread 2026-03-30). Mercurial's own lazy-import system
             (hgdemandimport / LazyLoader / LazyFinder) collides with Python 3.15's PEP 810 lazy imports once
             the CPython standard library itself lazily imports some attributes. Concrete failure:
             `cannot import name 'nlargest' from 'heapq'`. Fix: add `heapq` and `copy` to hgdemandimport's
             ignore list so Python's own lazy imports can work. This is direct evidence that (a) the 3.15
             stdlib is already using PEP 810 lazily and (b) practitioners are hitting and fixing real conflicts
             during the pre-release series — the "recent and in use" signal the series wants.
Locators:    Message body and patch description.
Quote:       "our way of doing lazy imports (using LazyFinder) and the PEP 810 way of doing lazy imports don't
             work well together."
```

```text
URL:         https://peps.python.org/pep-0690/
Kind:        primary — the predecessor PEP, for lineage.
Establishes: PEP 690 "Lazy Imports", Status: Rejected, Python-Version: 3.12. It proposed IMPLICIT, opt-in
             lazy imports (a `-L` flag / `importlib.set_lazy_imports()`) that deferred top-level imports
             transparently, from Meta's Cinder work. It was rejected; PEP 810's explicit per-import keyword is
             the design pivot that answers the objections to making laziness implicit/global. PEP 810's FAQ
             includes "How does this differ from the rejected PEP 690?"
Locators:    Header (Status: Rejected) and Abstract.
Quote:       Status: "Rejected".
```

## Contradictions

- **`with` blocks: secondary summary vs the PEP.** The GitHub PR page's prose
  summary says the implementation restricts lazy imports "in try/except blocks
  and with statements." PEP 810 contradicts the `with` part directly: in
  "Rejected Ideas" it lists "Disallowing lazy imports inside with blocks" as
  rejected, reasoning that "with statements have much broader semantics than
  try/except blocks ... commonly used for resource management." The PEP's own
  SyntaxError list names only functions, classes, and try/except (plus
  `import *`). Primary wins: `lazy` is allowed inside `with` blocks and barred
  inside try/except. The writer must state this precisely; do not repeat the PR
  blurb.
- **Production figures are not PEP 810's results.** PEP 810's Motivation quotes
  "50-70%" startup and "30-40%" memory, but these describe the implicit Cinder
  lineage and real-workload observations, not a benchmark of the `lazy` keyword.
  PEP 810's own performance claim is the opposite kind of statement: the
  mechanism is "performance-neutral" with "no measurable performance overhead."
  No source presents an end-to-end startup benchmark produced by PEP 810's
  explicit mechanism. Presenting 50-70% as "PEP 810 made programs 70% faster"
  would be unsupported.
- **Meta's two posts measure different workloads.** The 2022 post (Instagram
  web monolith: reload time, module count, memory) and the 2024 post (ML
  workloads: TTFB, Jupyter startup) report non-overlapping metrics. Do not merge
  them into one blended "up to X%" claim.

## Numbers

```text
Figure: Status today — Python 3.15 at release candidate 3 (3.15.0rc3, 2026-10-02); 3.15.0 final 2026-10-09
Owner:  PEP 790 (schedule) + docs.python.org/3.15 (served at rc3)
Scope:  As of 2026-10-03, the feature ships in the beta/RC series; stable is 6 days out, not yet released.
```

```text
Figure: PEP 810 header — Status Final; Resolution 03-Nov-2025; Created 02-Oct-2025; Python-Version 3.15
Owner:  PEP 810
Scope:  PEP lifecycle; "Final" = accepted and the spec is frozen, distinct from the interpreter's release state.
```

```text
Figure: beta 1 2026-05-07; b2 06-02; b3 06-23; b4 07-18; rc1 08-04; rc2 09-01; rc3 10-02; final 2026-10-09
Owner:  PEP 790
Scope:  CPython 3.15 release schedule (actual dates).
```

```text
Figure: CPython implementation merged 2026-02-12 (PR #142351, gh-142349)
Owner:  github.com/python/cpython PR 142351
Scope:  Landed on main ~3 months before beta 1.
```

```text
Figure: ~17% of stdlib imports outside tests (nearly 3500 imports across 730 files) already deferred in functions
Owner:  PEP 810 (Motivation)
Scope:  CPython standard library, non-test code; the PEP's own static analysis. Good original-analysis anchor.
```

```text
Figure: startup "50-70%" reduction "in practice"; memory "30-40%" observed
Owner:  PEP 810 Motivation, drawn from the implicit Cinder/PEP 690 lineage (NOT a PEP 810 benchmark)
Scope:  General, real-workload claim; attribute to the lineage, not to the `lazy` keyword's own measurement.
```

```text
Figure: Instagram Server ~28,000 modules at startup; reload ~25 s (late 2021) -> up to ~1.5 min (year-end 2021);
        ~70% p50 and ~60% p90 reload reduction; 50-70% across other servers/tools; 20-40% memory; ~12x fewer
        modules; ~80 -> 0 daily circular-import errors; "hundreds of developer hours per day" saved
Owner:  developers.facebook.com 2022 (Méndez Bravo)
Scope:  Meta/Instagram production, implicit Cinder lazy imports. Lineage context only.
```

```text
Figure: up to 40% TTFB improvement (Meta AI workloads); 20% reduction in Jupyter kernel startup
Owner:  engineering.fb.com 2024 (Méndez Bravo)
Scope:  Meta ML workloads, implicit Cinder lazy imports. Lineage context only.
```

## Limits

- **No Python 3.15 interpreter is reachable in this environment.** The writer
  cannot run a measured before/after startup demo; the commission's
  mechanism-demonstration fallback is the authorised path. Evidence of the check
  is in the note below.
- **No PEP 810-native performance benchmark exists in the sources.** Any
  before/after numbers would have to come from the writer's own run (impossible
  here per the above) or be attributed to the implicit Cinder lineage. The
  mechanism-demonstration fallback should trace proxy creation and reification
  and show the one failure mode (import-time side effect deferred to first use),
  which the sources fully support without a 3.15 interpreter.
- **Everything else the brief asked for is established:** syntax, keyword,
  proxy type (`types.LazyImportType`; runtime repr `LazyImport`), `sys.lazy_modules`,
  reification trigger and `resolve()`, placement rules, error/side-effect
  timing, the three modes and their precedence, the filter escape hatch,
  `__lazy_modules__`, acceptance date, beta-1 date, stable date, and the
  production lineage with exact sources and scope.

### Environment check for the writer's experiment (run 2026-10-03)

Commands run in this checkout and their exact results:

```text
$ python3.15 -V
/bin/bash: line 1: python3.15: command not found

$ python3 -V
Python 3.11.15

$ uv --version
uv 0.8.17

$ uv python install 3.15
error: No download found for request: cpython-3.15-linux-x86_64-gnu

$ uv run --python 3.15 python -V
error: No interpreter found for Python 3.15 in managed installations or search path
```

`uv python list` tops out at `cpython-3.14.0rc2` as a download; installed
interpreters are 3.11.15 (default `python`/`python3`), 3.13.14, 3.12.11, 3.10.20.
No 3.15 build (beta, RC, or final) is available through uv's managed downloads or
on PATH, and 3.15.0rc3 only tagged on 2026-10-02, so python-build-standalone /
uv had not published a 3.15 artifact by the time of this check. Building 3.15
from source is not a reliable option inside the sandbox (network via the agent
proxy, compile time). Conclusion: the measured before/after experiment is not
runnable here; use the mechanism-demonstration fallback.

## Source assets

```text
Asset: PEP 810 "Specification" code examples (lazy import / lazy from, and the SyntaxError cases)
Shows: The exact surface syntax and the placement restrictions at a glance.
Crop:  Keep the valid forms and the four SyntaxError comments; these are the feature's contract. Prose can carry
       them as an `nb-code` listing rather than a screenshot.
```

```text
Asset: PEP 810 reification example (type(...) printing <class 'LazyImport'>, then .resolve(), then 'json' in sys.modules)
Shows: When the proxy exists vs when it becomes the real module, and that __dict__/globals() access stays lazy.
Crop:  Keep the three type() prints and the sys.modules check in order; this is the clearest trace of the lifecycle.
```

```text
Asset: developers.facebook.com 2022 — Instagram reload-time regression/improvement figures
Shows: The scale of the problem (25 s -> 1.5 min reloads; 28,000 modules) that motivated lazy imports.
Crop:  If used, label it clearly as the implicit Cinder mechanism, not PEP 810. Prefer reproducing the figures in
       a small stat strip over lifting the vendor's chart.
```

None of the sources carries a visual that beats a code listing for the core
mechanism; the natural furniture is `nb-code`, per the commission.

## Discarded

```text
URL: https://pydevtools.com/handbook/explanation/what-is-pep-810/ — secondary explainer; every fact it carries is owned by PEP 810 / the 3.15 docs, which are cited directly.
URL: https://simonwillison.net/2025/Nov/3/barry-warsaw/ — useful pointer to the SC acceptance, but it quotes the discuss.python.org post, which is cited as the owning primary.
URL: https://pie.gravitywell.xyz/... and piefed.nullspace.lol/... — aggregator reposts of the acceptance news; no independent facts.
URL: discuss.python.org PEP 690 thread — the PEP 690 page itself owns the status and proposal; the thread adds only discussion.
URL: https://github.com/python/peps/pull/4633 (and 4656/4674/4677) — edits to the PEP source text; the rendered PEP at peps.python.org is the authoritative artifact.
```
