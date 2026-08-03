# writer brief: paper-of-the-day/double-descent (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `paper` template identity, series prompt
- commission.md (artifact root) — the papers, the reconstruction owed, and shapes to break
- writing-coach/01/voice-guide.md — the two registers (builder/reviewer), licenses, do-not-reuse list
- researcher/01/evidence.md — the ONLY claim set available; use its Numbers, Source assets (figure numbers + PDF pages), and Contradictions exactly
- The initialized article at `library/paper-of-the-day/double-descent.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/paper-of-the-day/double-descent/library/paper-of-the-day/double-descent.html`   (file arg only)
  `./nb check .nb-work/paper-of-the-day/double-descent/library/paper-of-the-day/double-descent.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- Rebuild the double-descent claim with the papers' own artifacts. Capture the
  figures the argument spends as SOURCE ASSETS with `nb asset` (Belkin Fig. 1
  schematic p3, Fig. 2 RFF/MNIST p5; Nakkiran Fig. 1 model/epoch-wise p1, and
  the label-noise Fig. 4 p5 if the argument spends it), each with
  `data-nb-locator`/`data-nb-url` to the exact figure/page, and prose that says
  what each settles. FIGURE-NUMBERING TRAP: the free arXiv Belkin PDF numbers
  figures differently from the canonical PNAS version past Fig. 2 — cite the
  version whose URL you actually link, and keep locator/number consistent with
  that document. Fig. 1 and Fig. 2 are stable across both.
- Set the reconstruction's core math (the interpolation threshold; effective
  model complexity) with the equation furniture; at most one annotated equation.
- STEELMAN BOTH SIDES (load-bearing here): the phenomenon is real and reproduced,
  but its "extends the classical U-curve / it's a law in parameter count"
  framing is the contested part. Weigh: Curth 2023 (much of Belkin's
  tree/boosting/linear case is an x-axis/complexity-axis artifact — but this
  does NOT touch Nakkiran's deep-network results); optimal L2 regularization
  provably removes it for linear models; and the live mechanistic tension
  (Nakkiran: misspecification drives it, vs Mei & Montanari producing the full
  curve with none). Do NOT use the "follow-up work disagrees" catalog device.
- Keep reported fact, estimate, and synthesis distinct. A single nb-note-strong
  "Verdict" note is apt: the effect is real; the universal-U-curve reading is
  what the after-record qualifies.
- Paper template: abstract card + link up front (use the title/version you link),
  2-8 flexible sections, ending on the verdict. Word band 1800-3400. min 8 sources.
