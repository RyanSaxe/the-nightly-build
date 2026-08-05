# Draft handoff: expert-tools/visidata (writer 01)

## Original work
This piece runs VisiData's five documented transforms (`=`, `+`, `F`, `W`,
`M`) as one continuous session on a single sales CSV to show that the
exploratory loop a notebook spends in write-run-reread, VisiData spends in
move-the-cursor-and-press-a-key, then locates exactly where that trade stops
paying — whole-column results during async load, reproducibility, out-of-core
work — and ties the capability to its single-primary-author cost.

## Proof
`./nb check ... --series expert-tools --library <library-checkout>` (links
included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped words=1658,
reading_minutes=7, sources=17 (15 primary, 2 secondary). No warnings left
standing.

## Construction notes for the editor
- The demonstration is authored code/transcript furniture (two `nb-code`
  listings), not a screenshot — the researcher found no legitimate spendable
  source-asset visual. The transcript numbers reconcile: six rows give West
  sum 46 / East sum 47; the pivot cells (West Widget 28, West Gadget 18, East
  Widget 20, East Gadget 27) are the same rows regrouped, and the melt is that
  pivot folded back to tall. A comparison table sets each pandas idiom beside
  the VisiData keystrokes it replaces.
- Every keybinding shown is source-verified per the evidence (`F`, `+`, `=`,
  `W`, `M`). No `Ctrl+T`/`Ctrl+C` appears. `Ctrl+H` is used once as the
  discoverability pointer and is backed by the docs index (s7).
- The async loader is stated precisely per the brief: mid-load navigation and
  viewing are correct immediately, but a frequency count, sort, or aggregate is
  final only once loading finishes (called out in a labelled `nb-note`). The
  `options.max_rows` default of 1,000,000,000 is named as the truncation bound.
- Honesty items carried: v3.4 (2026-06-30), GPL-3.0, ~9,200 stars, effectively
  single-primary-author (Saul Pwanson; Anja Kefala on docs/packaging), release
  cadence; adoption cost stated as the modal-keystroke learning stretch; the
  notebook/SQL boundary (reproducible pipelines, custom plotting, out-of-core)
  with cmdlog narrowing but not closing reproducibility.

## Open question for the orchestrator
- Pivot and melt both group relative to VisiData's *key columns*. The article
  states plainly that marking a column as a key is "one more keystroke" without
  naming the exact key, because the key-marking command (`!`) was not
  source-verified in the evidence record and the brief forbids shipping a
  remembered API. If the editor wants the pivot walkthrough fully
  reproducible keystroke-for-keystroke, the researcher should verify the
  key-column command against source; otherwise the current honest phrasing
  stands.
