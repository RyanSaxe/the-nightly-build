# editor review-brief: paper-of-the-day/double-descent (editor/01)

Inputs:
- editorial-direction.md (artifact root) — the standard to enforce
- writer/01/brief.md (the exact writer brief — for instruction-leakage detection)
- commission.md (artifact root) — the papers, the reconstruction owed, shapes to break
- writing-coach/01/voice-guide.md — the two registers, licenses, do-not-reuse list
- researcher/01/evidence.md — the evidence to open as an opponent (figure numbers, the arXiv-vs-PNAS numbering trap, the contested-ubiquity nuance)
- writer/01/draft-handoff.md — open the original-work sentence only on the third read
- The article at `library/paper-of-the-day/double-descent.html` (workspace root), its assets in `library/paper-of-the-day/double-descent/`, and `.nb-context/` template context
Output: editor/01/editorial-review.md

Recent-pattern notes: the "follow-up work disagrees" catalog device (used for
grokking, emergent-abilities) is barred; grokking is already published — do not
retread it. Vary heading shapes.

Round focus:
- Inspect all SIX source assets: compare each against its cited figure, confirm
  the crop retains the evidence and omits printed page-captions, the
  `data-nb-locator`/`data-nb-url` point to the exact figure/page of the document
  actually linked, and the arXiv figure numbers are consistent with the linked
  version (Belkin uses only Fig.1/Fig.2, stable across arXiv/PNAS).
- Check the two equations: the interpolation-threshold display and the annotated
  EMC equation (Nakkiran Def. 1) verbatim with its five-term legend.
- STEELMAN check: confirm Curth's x-axis critique is scoped honestly to
  non-deep methods (does NOT touch the deep results); label-noise dependence
  (peak survives without noise, sharpens with it); regularization removal; and
  the Nakkiran-vs-Mei/Montanari misspecification tension left open. The Verdict
  (single nb-note-strong) must say the effect is real while the universal-
  U-curve reading is what the after-record qualifies.
- Abstract card: confirm it uses the arXiv title/link (PNAS DOI 403s the
  checker) with the canonical PNAS venue in the meta line.
- DISPLAY TEXT incl. the byline: confirm the byline reads "11 min read" (the
  stamped reading_minutes), NOT the "N min read" placeholder. Verify every
  number/name/date in headline, dek, subheads against the evidence, and audit
  data-nb-kind. Open every citation href as printed.
- Make surgical cuts; route any redraft. After direct cuts run
  `./nb stamp <article-path>` (file arg).
