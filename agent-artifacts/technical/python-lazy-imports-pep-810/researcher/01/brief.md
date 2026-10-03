# researcher brief: technical/python-lazy-imports-pep-810 (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — the mechanism to confirm and the original-work
  target.
Output: ./evidence.md

Work from these inputs. Use web and document tools. Where something you need is missing,
say so and keep working.

This round: establish the mechanism and the facts from the documents that own them.
- PEP 810 text (peps.python.org/pep-0810): the exact syntax, the keyword, the proxy/
  reification semantics, where `lazy` is and is not allowed, error-timing behaviour,
  and the opt-in / escape-hatch design. Quote the exact wording where a detail is
  contested or precise.
- CPython 3.15 docs, What's New, and changelog, plus the relevant issue/PR/commit for
  any implementation detail (`sys.lazy_modules`, the proxy type name, how first-use
  triggers reification). Confirm the names rather than trusting secondary write-ups.
- Dates and status: Steering Council acceptance date, beta-1 date, and the 3.15 stable
  release date; report release status precisely (betas shipping, stable imminent).
- Production lineage: the Meta/Instagram lazy-imports results (startup/memory figures).
  Record the exact figures, the exact source, and that they came from an earlier
  implicit mechanism, so the writer does not present them as PEP 810's own measured
  results.
- Environment check for the writer's experiment: determine and record whether a Python
  3.15 interpreter (any beta/rc) is reachable in this checkout/environment, and if so
  how it is invoked (e.g. via `uv`), with the exact version string. This decides whether
  the writer can run a measured before/after demonstration or must use the mechanism-
  demonstration fallback. Note any sandbox/network limit that would block installing one.
Record contradictions in full. Minimum eight sources. A repetition supports only that
someone made a claim; pin the owning document.
