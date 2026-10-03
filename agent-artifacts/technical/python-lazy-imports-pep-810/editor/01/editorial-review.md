# Editorial review: technical/python-lazy-imports-pep-810 (editor/01)

## Correct

Thesis: Python 3.15's `lazy` keyword defers an import by binding a proxy at the
statement and running the real import only at first use, which moves the
import's errors and side effects out of startup and into the running program.
The claims under it, each stated from the draft alone:

1. A lazy import binds a `types.LazyImportType` proxy and records the name in
   `sys.lazy_modules`; the module stays out of `sys.modules` until reification.
2. First use (any ordinary access, not `globals()`/`__dict__` inspection)
   reifies the proxy into the real module; `resolve()` forces it.
3. Deferral is safe unless something between the import and first use relied on
   an import-time side effect having already run; that is why eager is the
   default and `lazy` is opt-in per statement.
4. The keyword is performance-neutral by PEP 810's own measure; the large
   production gains in the record belong to Meta's earlier *implicit* Cinder
   design, not to this keyword.

I tried to break each against the opened sources rather than the record.

- **Mechanism (PEP 810, opened).** The soft keyword, `__lazy_import__` in place
  of `__import__`, the `types.LazyImportType` proxy, `sys.lazy_modules` as a set
  "for diagnostics and introspection", absence from `sys.modules` until
  reification, the reification trigger, the `globals()`/`__dict__` exemption, and
  `resolve()` all read exactly as the draft states them. Held.
- **The restriction set (hardest test).** PEP 810's Rejected Ideas explicitly
  rejects disallowing `lazy` inside `with` blocks ("`with` statements have much
  broader semantics than `try/except` blocks"), and the SyntaxError list names
  functions, classes, try/except, and `import *`. The draft states this
  correctly and names the implementation PR's prose summary as the secondary
  account that loses to the spec. I confirmed the PR (#142351, merged
  2026-02-12) does carry with-block-restriction material (a commit
  "Make imports in with blocks syntax errors"), which is the known contradiction
  the orchestrator already adjudicated in the brief: PEP 810 governs, `with` is
  allowed. The draft follows that adjudication. Held, with a flag to the
  orchestrator below about the shipped implementation's actual behaviour.
- **Modes, precedence, filter, `__lazy_modules__`.** Three modes
  `normal`/`all`/`none`, precedence `sys.set_lazy_imports()` > `-X lazy_imports`
  > `PYTHON_LAZY_IMPORTS`, `get_lazy_imports()`, the filter signature with
  `None` removing it, and `["*"]` rejected: all confirmed against the PEP. The
  draft correctly does not assert the filter's boolean polarity. Held.
- **Figures and their scope.** The ~17% / ~3,500 imports / 730 files stdlib
  statistic is PEP 810's own Motivation. The Instagram figures (~28,000 modules,
  ~70% p50, ~60% p90, ~12x fewer modules, ~80/day to zero) are confirmed in the
  2022 Méndez Bravo post and scoped to the implicit Cinder mechanism; the ML
  figures (up to 40% TTFB, 20% Jupyter) are confirmed in the 2024 post and kept
  in a separate sentence. PEP 810's own claim is reported only as
  performance-neutral. The draft does not merge the two Meta posts or present any
  gain as the keyword's own. Held.
- **Dates and status.** rc3 dated 2026-10-02, final 2026-10-09, accepted
  unanimously 2025-11-03 (Barry Warsaw for the SC), implementation merged
  2026-02-12, docs live at rc3: all confirmed against PEP 790, the acceptance
  post, the PR, and the 3.15 What's New page. "Accepted and shipping, not yet
  stable" is accurate for 2026-10-03. Held.

**Break found (fixed by narrowing).** The draft said hgdemandimport is "built on
a custom `LazyFinder`". Reading the raw mercurial-devel page, Mercurial's own
self-description of its mechanism is "our way of doing lazy imports (using
LazyLoader)"; the `class LazyFinder` on the page is a minimal reproducer
construct, not stated to be hgdemandimport's production class. The evidence
record quotes that sentence as "(using LazyFinder)", which is a misquote. I did
not propagate either into a contested production-class claim: I narrowed the
body and the s6 source description to "a custom meta-path import hook,"
which the page's reproducer (`sys.meta_path.insert(0, LazyFinder())` wrapping
`importlib.util.LazyLoader`) and hgdemandimport's known design both support. The
load-bearing facts of that paragraph are all confirmed verbatim on the page: the
3.15 stdlib lazily imports `heapq.nlargest`, the collision with Mercurial's
system, the symptom `cannot import name 'nlargest' from 'heapq'`, and Mads
Kiilerich's 2026-03-28 patch adding `heapq` and `copy` to the ignore list.

**Citations.** I opened all nine `href`s as printed. Each lands on its source and
establishes what it is cited for. `data-nb-kind` is defensible throughout: PEP
810/790/690, the SC acceptance post, the CPython PR, and the 3.15 docs as
`primary`; the Meta blogs as `primary` for Meta's own figures; mercurial-devel
as `secondary` (a practitioner adapting to the behaviour).

## Reads well

Three cuts, each a small slop trim rather than a rewrite:

- "Every other access reifies, which is the subject of the next section." The
  tail is a structural self-reference to the article's own layout, and the next
  heading already announces it. Cut to "Every other access reifies."
- "The episode is two signals in one:" is a built-to-be-quoted frame. Recast to
  "The episode shows two things at once:", stating the two facts plainly.
- The `LazyFinder` narrowing above also removed an over-committed identifier;
  that was correctness, not prose.

The antithesis the writer flagged, the heading "A lazy import binds a proxy, not
a module," stays: the misconception it corrects (conflating "name bound" with
"module imported") is real and stated in that section's first sentence, and the
voice guide builds the whole piece on that distinction. The headline's parallel
construction ("binds a proxy instead of running an import") earns its place on
the same test. Nothing else read as borrowed from the briefing or a quoted
passage; the edges and the last sentence survive the placeholder test.

## The experience

The rendered page reads top to bottom as a single trace: one binding (`json`)
followed from proxy to inspection to reification across two paired code
listings, then the one failure mode grounded in the dated Mercurial collision,
then the controls, then the when-to-use judgment. The two code listings, the
modes table, and the stat strip each show something faster than prose would, and
the stat strip's figures match the 2022 source exactly and sit inside scoped
prose that names them as the implicit mechanism's results. No component
overreaches its caption.

What the piece gives beyond its sources: it follows a single lazy binding
through its whole lifecycle in one continuous trace and ties PEP 810's abstract
"errors and side effects move to first use" to a dated, fixed in-the-wild
instance the PEP never connects (the March 2026 Mercurial/`heapq` collision
caused by the stdlib's own lazy imports). That answer survives, and it matches
the writer's original-work sentence. The piece is not a spec paraphrase.

## Edits

- Narrowed "built on a custom `LazyFinder`" to "built on a custom meta-path import hook" (body), to what the opened source supports.
- Narrowed the s6 source description "hgdemandimport's `LazyFinder`" to "hgdemandimport's import hook" for the same reason.
- Cut the self-referential tail from "Every other access reifies, which is the subject of the next section."
- Recast "The episode is two signals in one:" to "The episode shows two things at once:".
- Ran `nb stamp` (words=2146, reading_minutes=9, sources=9) and the exact `nb check` to BLOCK: 0, WARN: 0, PUBLISHABLE.

## Decision

approve — the mechanism, figures, dates, and restriction set are correct against
the opened primaries, the required scoping and no-benchmark disclosures hold, and
the only correctness slip (an over-committed Mercurial class name) was fixable by
narrowing to what the source supports.
