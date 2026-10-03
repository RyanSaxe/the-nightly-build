# writer brief: technical/python-lazy-imports-pep-810 (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — the full standing standard.
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this piece sounds.
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; draft only from it.
- commission.md (../../commission.md) — angle, boundaries, original-work target.
Output: ../../writer/01/draft-handoff.md (edit the article in place at
  .nb-work/technical/python-lazy-imports-pep-810/library/technical/python-lazy-imports-pep-810.html)
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/python-lazy-imports-pep-810/library/technical/python-lazy-imports-pep-810.html --series technical --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for
background. The effective contract and furniture catalogs are under `.nb-context/`; use
documented markup only. Where the evidence cannot supply a fact you need, ask me (the
orchestrator) and keep working.

This round's focus and settled decisions:
- No Python 3.15 interpreter is reachable here (see evidence Environment check), so use
  the mechanism-demonstration fallback: a minimal, correct code walkthrough that traces
  exactly when the `LazyImportType` proxy is bound and when first use reifies it, plus
  the failure mode. Do NOT fabricate benchmark numbers or claim to have run 3.15.
- The Instagram/Cinder production figures belong to Meta's earlier IMPLICIT mechanism
  (PEP 690 lineage), not PEP 810's explicit keyword. Report them only as that lineage's
  results with the scope the evidence gives; PEP 810's own performance claim is only
  "performance-neutral." Do not present the gains as PEP 810's measured results.
- Strong "recent and in use" anchor the evidence supports: the 3.15 stdlib itself now
  uses `lazy` (e.g. heapq/copy), and that collided with Mercurial's hgdemandimport — a
  real adoption signal and a real failure mode in one. PEP 810 also reports ~17% of
  non-test stdlib imports (~3500 across 730 files) already manually deferred. Use these
  to make the walkthrough about code in use, not a spec paraphrase.
- Get the restriction right: `with` blocks ARE allowed for lazy imports (a GitHub PR
  summary says otherwise and is wrong; PEP 810 rejected disallowing `with`). Only
  functions, classes, try/except, and `import *` are barred. The evidence Contradictions
  section has this.
- Report release status precisely: as of 2026-10-03, 3.15 is at rc3; 3.15.0 final is
  dated 2026-10-09. Shipping through RCs, stable imminent — not "released."

Recent-habit notes to break (this paper's Technical desk; the editor will compare):
- Opener mold to avoid: "On a two-model DuckDB project.../In one daily npm queue..." +
  a versioned tool + a path:line. A concrete opening is good; this exact cadence is worn.
- Dek molds to avoid: the limitation-clause tail ("while leaving X outside its proof",
  "but left X unclear", "calls for a targeted test").
- Closing habit to avoid: a bare scope-caveat section ("One adapter, one project and one
  patch version"). Per the article identity, the last flex section is the piece's own
  conclusion; fold scope limits into prose and land on what the piece established.

Code is the natural furniture (`nb-code`, `data-language="python"`, HTML-escaped). Use a
small table/stat strip only if it reads faster than prose. Number sources in first-
citation order, carry each kind into `data-nb-kind`, and prefer a locator that lands on
the passage. Put the one-sentence original-work claim in draft-handoff.md. Run the proof
with `--no-check-links` while iterating, then `nb stamp` and the exact `nb check` above
until BLOCK: 0 before handing off.
