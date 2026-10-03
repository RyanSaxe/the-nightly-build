# editor review-brief: technical/python-lazy-imports-pep-810 (editor/01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- voice-guide.md (../../writing-coach/01/voice-guide.md) — read first.
- evidence.md (../../researcher/01/evidence.md) — the claim set the draft must not exceed.
- commission.md (../../commission.md)
- the exact writer brief (../../writer/01/brief.md)
- draft-handoff.md (../../writer/01/draft-handoff.md) — the writer's original-work sentence,
  proof result, and two flagged notes.
Article under review (read the rendered page too):
  .nb-work/technical/python-lazy-imports-pep-810/library/technical/python-lazy-imports-pep-810.html
Output: ../../editor/01/editorial-review.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/python-lazy-imports-pep-810/library/technical/python-lazy-imports-pep-810.html --series technical --repo /home/user/the-nightly-build

Decide whether this publishes and edit it until it can. Effort: HIGH. You may change
anything except the facts; narrow a claim to what the evidence supports, but never invent
a fact, alter a number/title/date/quote, or change what a citation is cited for. Where the
record and a source you open disagree, ask me (the orchestrator).

Things to test hardest on this piece:
- Correctness of the mechanism against PEP 810 and the live 3.15 docs: the `lazy` soft
  keyword, `types.LazyImportType`, `sys.lazy_modules`, reification on first use, and the
  restriction set. The writer resolved a known contradiction: `with` blocks ARE allowed;
  only functions, classes, try/except and `import *` are barred (the implementation PR's
  summary is wrong; PEP 810 governs). Confirm the draft states this correctly.
- No invented benchmark and no claim that 3.15 was run here (no 3.15 interpreter is
  reachable; code is illustrative of behaviour PEP 810 defines). Confirm the draft says so.
- The Instagram/Cinder production figures must read as the earlier IMPLICIT mechanism's
  results, scoped, not as PEP 810's own; PEP 810's own claim is only performance-neutral.
- Release status stated precisely (rc3 as of 2-3 Oct; 3.15.0 final 9 Oct; not released).
- Open item from the writer (non-blocking): `sys.set_lazy_imports_filter` boolean polarity
  is NOT fixed by the evidence, so the draft leaves it unstated. Do not add a polarity
  claim the evidence does not support; leaving it unstated is correct unless you can source
  it (if so, ask me before asserting).
- The writer flagged one heading using antithesis ("binds a proxy, not a module"). Judge it
  by spec/slop.md: antithesis stays only where the misconception it corrects is real and
  stated in that section. Keep or recast on that test.

Recent-habit comparison (this paper's Technical desk; cut formula against these):
- Opener mold: "On a two-model DuckDB project.../In one daily npm queue..." + versioned
  tool + path:line.
- Dek molds: the limitation-clause tail ("while leaving X outside its proof", "but left X
  unclear", "calls for a targeted test").
- Closing mold: a bare scope-caveat section ("One adapter, one project and one patch
  version"). The last flex section should be the piece's own conclusion.
The writer reports breaking all three; verify, and check headings/dek against spec/headlines.md.

If you make direct cuts and approve, no writer round is owed for the proof alone. After
editing, run `nb stamp` and the exact `nb check` above yourself until BLOCK: 0. Send the
piece back only if it needs a different argument no edit can reach. Write editorial-review.md
in the required shape and report the decision.
