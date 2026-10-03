# Commission: technical/python-lazy-imports-pep-810

## Assignment
A technical walkthrough of explicit lazy imports in Python 3.15 (PEP 810). Template
`article`: 800-6000 words, two fixed anchors (orientation, sources) plus two to six flex
sections you name, every section cited. Minimum eight sources. The series wants recent
work that is actually in use, opened up with a concrete example, code, or experiment,
explained well enough that a reader could try it, question it, or build on it.

## Why this now
PEP 810 adds a `lazy` keyword before an `import` or `from ... import` statement that
defers loading the module until a bound name is first used. The Steering Council
accepted it (reported 3 November 2025) for 3.15; it has shipped in the 3.15 beta series
(beta 1 reported 7 May 2026); the 3.15 stable release is dated 9 October 2026. It is in
active use through the betas and sits on a real production lineage (Meta/Instagram's
earlier implicit lazy-imports work). Confirm each of these dates and the keyword/syntax
against the PEP text and the CPython changelog/docs; the stable date means report status
honestly (shipping in betas, stable imminent), not "released" if it is not yet.

## The mechanism to walk through (confirm all against PEP 810 and CPython)
- Syntax: `lazy import json`, `lazy from json import dumps`.
- A lazy import binds a proxy, not the module; the deferred name is tracked (reported as
  a `LazyImportType` proxy and `sys.lazy_modules` rather than `sys.modules`).
- Reification: on first use of the bound name, the import actually runs and the proxy is
  replaced by the real object. Walk through what "first use" means and what triggers it.
- Scope and limits: where `lazy` is allowed, how it interacts with `__getattr__`/module
  side effects, what happens to import errors (they move from import time to first use),
  and the opt-in/escape-hatch story (how a project turns it on or forces eager).

## Required original contribution
A concrete, reproducible demonstration this checkout can run, not a paraphrase of the
PEP. The strongest candidate, if a 3.15 interpreter is reachable in this environment:
measure import/startup cost for a small program with a heavy optional dependency, with
and without `lazy`, and show the numbers and the method. If a 3.15 interpreter is NOT
reachable (confirm before assuming), fall back to a precise mechanism demonstration: a
minimal, correct code walkthrough that traces exactly when the proxy is created and when
it reifies, plus the one failure mode a reader is most likely to hit (an import whose
side effect a project depended on at import time). Say in one sentence what the piece
does that the PEP does not; put it in draft-handoff.md.

## Boundaries
- Fair to the design. State what PEP 810 is for and the problem it solves before
  weighing its costs; represent the design's own rationale before any critique.
- Do not oversell. Report the production figures (e.g. Instagram-era startup/memory
  gains) only with the exact source and scope the record gives; those came from an
  earlier, implicit mechanism, so do not present them as PEP 810's own measured results
  unless the record does.
- Recent technical pieces in this paper lean on one house move: open with "On a
  two-model project.../In one daily queue..." and close on a bare scope-caveat section
  ("One adapter, one project and one patch version"). A concrete opening experiment is
  welcome, but do not reuse that exact cadence, and land the piece on the conclusion it
  built (fold scope limits into prose), not a stock "limits" closer.
- No self-reference.

## Furniture
Code listings are the natural furniture here (`nb-code`, with `data-language="python"`
and HTML-escaped source). A small table or stat strip for before/after numbers if the
experiment runs. A figure only if a diagram shows the proxy/reification flow faster than
prose. Any measured series in a chart must come from a run the researcher or writer can
reproduce, built with `nb chart`.

## Neighbouring articles this run
Daily Brief and a Feature on the AI & Economy ATLAS. The brief deliberately does not
carry a Python item, so this walkthrough owns Python 3.15 for the edition. Stay on the
lazy-imports mechanism; PostgreSQL 19 and other releases belong to the brief.

## Source policy
Minimum eight sources. Primary = PEP 810, CPython docs/changelog/what's-new for 3.15,
the discuss.python.org acceptance/thread where it establishes a fact, and any CPython
commit/issue that owns a detail. Secondary = independent write-ups and the
production-lineage reporting. Resolve each link to the document that owns the claim.

## Production
Researcher high / capable. Writer medium / capable. Writing-coach low / capable. Editor
required, high effort, correspondent's model.

## Decisions log
- Template is `article` (a mechanism walkthrough), not `paper`: PEP 810 is a language
  feature with a spec and implementation, not a single research paper to review.
- The measured-experiment original contribution is contingent on a reachable 3.15
  interpreter; the mechanism-demonstration fallback is authorised if it is not.
