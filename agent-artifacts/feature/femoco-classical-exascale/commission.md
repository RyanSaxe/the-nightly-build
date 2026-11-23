# Commission: feature/femoco-classical-exascale

Authorized by `nb duty` for 2026-11-23: feature, open section, no commissions.
Template `article`; strict, 600–1,200 words, 2–4 flexible sections, at least 5
sources. Each section is built around a visual.

## Topic and angle

The 2026 ACM Gordon Bell Prize, awarded at SC26 on 19 November to Shang et al.
(USTC / CAS / SYSU), went to an exascale classical computation of the FeMoco
active space, CAS(113e,76o). FeMoco, the iron-molybdenum cofactor of
nitrogenase, has served since Reiher et al. (2016/17) as the standard example of a
chemistry problem said to need a fault-tolerant quantum computer.

The angle to test: a classical machine has now solved the benchmark active space
end to end, in a time shorter than published projections for a single
fault-tolerant quantum run (scouting read 105 minutes against an 8.6-hour
projection; both unverified). The piece places the benchmark's history in order
(which active space, which method, which hardware, when) and shows what the
result does and does not settle about quantum advantage in chemistry.

What must be established firsthand, or the angle narrowed:
- What exactly was computed (active space, method, accuracy reached, whether the
  energy is converged / chemically accurate, and against what reference).
- Time to solution and machine figures from the paper or ACM release.
- The source and assumptions of any quantum run-time projection compared
  against, and whether the comparison is like for like (same active space, same
  accuracy target).
- The rival positions in their holders' words: Garnet Chan's argument that the
  quantum advantage case on FeMoco was overstated, and whoever argues the result
  does not settle it (the ACM release or named researchers).

If the paper does not support a like-for-like time comparison, the piece leads
with what it does support. The researcher says so in the report.

## Boundaries

- Not a quantum-computing industry roundup. One benchmark, its history, this
  result, and the argument about what it shows.
- The audience knows CS and ML systems, not quantum chemistry; define active
  space, orbitals/electrons notation and chemical accuracy where first needed.
- Recent features covered TOP500 ageing machines (20 Nov) and Epoch's inference
  index (21 Nov). Do not revisit TOP500 rankings beyond identifying the machine.

## Neighbouring articles this run

- daily-brief/2026-11-23: must not carry this story.
- reinforcement-learning/domain-randomization: no overlap.

## Recent-pattern notes (writer and editor)

- Recent feature headlines lead with a number or a named actor and a verb
  ("Epoch averages…", "A slow entry bar keeps…", "Enrolled international
  students… fall 8.3%"). Deks repeatedly run "X, which…, does not…/has…" and close
  on what a source has not published or not separated (21, 19, 17, 12 Nov). Avoid
  the "has published no such check / does not separate" closer.
- Section headings recently are short noun phrases built on a number ("13.6×
  from the chip, 1.85× from the rack", "A harmonic mean of four ratios"). Build
  headings as steps of this argument.

## Roles

- writing-coach: capable tier (Sonnet), low effort.
- researcher: capable tier (Sonnet), high effort.
- writer: capable tier (Sonnet), high effort (series setting).
- editor: inherited model, high effort (required).

## Angle decision after researcher/01 (orchestrator)

The evidence does not support a like-for-like "classical beats quantum by 5×"
claim, and the piece does not make it. Decided angle: the prize abstract's
"about one-fifth" compares a measured 105-minute classical run with the 8.6-hour
phase-estimation projection of Low et al. (2025), which the same group revised to
about 2.5 hours for the same CAS(113e,76o) Hamiltonian in May 2026; and a
classical chemical-accuracy estimate for that Hamiltonian already existed
(Zhai, Chan et al., January 2026). The piece places these in order, shows what
each side computed or assumed (measured vs projected, existing vs hypothetical
hardware, extrapolated estimate vs phase estimation that assumes a prepared
state), and states what the prize result adds: the first exascale classical
solution and its time to solution.

Limits the piece must respect: the full prize paper was not opened, so its
method, accuracy and reference energy are not stated beyond the abstract; do not
infer Shang et al.'s method from Zhai et al. Whether the prize paper predates
the May 2026 revision is not established; say the abstract cites the 8.6-hour
figure and do not claim the authors ignored the revision. Treat the 105 min /
2.5 h ratio as this paper's arithmetic, labelled as such, and only alongside the
differences that keep it from being a race. Chan's position goes in his own
words, with his concession about guarantees; Babbush et al. and Low et al. state
the quantum side, noting both predate the prize.

## Decision on the editor's query (orchestrator)

arXiv:2605.30455 Table XXVII gives 2.50 h as the expected runtime and 2.36 h
per shot. The article keeps 2.5 h and the 1.4 ratio, labelled as the expected
run time where first given; the evidence record's "single-run" reading of 2.5 h
is superseded by the editor's reading.
