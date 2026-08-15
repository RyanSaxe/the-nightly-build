# writer brief: build-from-scratch/flash-attention (01)

Inputs:
- editorial-direction.md — house/press/series standard, declared reader
- commission.md — subject, the reconstruction to run, boundaries, and the
  "Habits to break" this piece must avoid
- writing-coach/01/voice-guide.md — how this piece should sound
- researcher/01/evidence.md — the confirmed math, claims, and its stated thin
  spots (real-number vs bit-exact equivalence; the non-comparable memory-Big-O
  exclusions between papers)
- the initialized article at
  .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html
  and its effective contract under
  .nb-work/build-from-scratch/flash-attention/.nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check --series build-from-scratch .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html --library /home/user/library-checkout

This round's focus: the runnable experiment is the argument. Actually write and
run the two implementations (naive full-matrix attention and the block-streaming
online-softmax version) in Python, show the real measured output in `nb-code`
(assert the outputs match to floating-point tolerance, not bit-identity, per the
evidence's thin spot), and if you build a peak-memory-vs-N chart, render it with
`nb chart` from your experiment's own measured numbers and commit its provenance.
Set the online-softmax recurrence as the one annotated `nb-math` equation. Do not
overclaim: say plainly the prototype reproduces the exact math and memory scaling
but not the kernel's wall-clock speedup, and note the papers' memory-Big-O
figures use different exclusions. Honor the commission's habits to break: no
"what X does not buy / what would have to change" closer, no default closing
`nb-note-strong` verdict box, no colon-subtitle headline; end on the conclusion
the experiment earned.
