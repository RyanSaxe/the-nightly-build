# Editorial review: reinforcement-learning/environments-and-the-rl-problem (editor/01)

## Correct

Thesis: once an action changes the next state, scoring a fixed policy on a
Markov decision process means solving a coupled system of Bellman equations, and
on one 4x4 gridworld that value can be computed two independent ways that agree.
Claims under it: (1) the gridworld is a finite MDP built from the four-argument
dynamics; (2) the Bellman equation for v_pi follows from the return's recursion,
with the Markov property supplying the conditional-independence step S&B skips;
(3) `(I - gamma P_pi)` is invertible because gamma < 1 makes the induced map a
contraction; (4) the direct solve and iterative policy evaluation reach the same
v_pi.

I re-ran both files with `uv run` (numpy, under a second each). Everything the
prose and the heatmap assert reproduces:

- `v_pi` by direct solve rounds to the grid printed in the prose and drawn in
  Fig. 4 (top-left -9.4, the two goal-adjacent cells -5.8, goal 0.0; symmetric
  across the diagonal, cells 3 and 12 both -8.8, cells 11 and 14 both -5.8).
- Direct vs iterative: `max |direct - iterative| = 6.71e-10` in 187 sweeps, which
  the prose gives as 6.7e-10 / 187 sweeps and the takeaway as agreement to nine
  decimal places. All correct.
- Cell-14 hand backup: the code prints -5.7572 on both sides; the prose rounds to
  -5.76 and lists the right neighbours (up to cell 10 = -7.42, left to 13 =
  -7.97, right to goal = 0, down bumps the wall back to 14 = -5.76). I checked the
  transition row for cell 14 against `next_state` and the arithmetic holds.
- Sanity checks reproduce: S&B Figure 3.2 (5x5, gamma=0.9) matches to one
  decimal; Figure 4.1 (4x4, gamma=1) matches as integers; k=2 gives -1.75, which
  the book rounds to -1.7, so no mismatch to claim. The running grid uses
  gamma=0.9, so gamma < 1 holds wherever the cited convergence and contraction
  arguments are invoked.
- gamma=0 nb-note answer: the code confirms v_pi = -1 for every non-terminal
  cell.

The one correctness break was in the invertibility argument. The matrix solve is
stacked over the non-terminal states, where the rows of `P_pi` adjacent to the
goal sum to less than one (mass leaks into the terminal cell, as the code's
`direct_solve` and the third nb-note both say). The draft justified the
contraction with "each row of `P_pi` is a probability distribution," which is
false for that restricted, substochastic matrix. The contraction holds for
substochastic rows just as well, so I narrowed the premise to "nonnegative and
sums to at most one." This makes the body agree with the code and with the
nb-note; the conclusion is unchanged.

Derivation, checked line by line: the Markov step is supplied explicitly (the
inner expectation is conditioned on everything known at t+1, then reduced to
conditioning on S_{t+1}=s' because G_{t+1}'s distribution no longer depends on
the path). The q_pi equation matches Silver slide 34's printed form and is cited
to Silver and Spinning Up, as the record requires (S&B leaves it to Exercises
3.17 and 4.3). Notation is S&B's throughout: R_{t+1}, the four-argument
p(s',r|s,a) as (3.2), and P_pi, r_pi defined from p as the lesson's own arrays.

Display text against the record: title, dek, and all five body headings check
out. I opened every citation's locator against the evidence record's Locators
lines; each lands on the stated section, page, or equation (footnote 4 p.48,
3.2 p.48, 3.4/3.5 p.49, 3.8 p.55, 3.12/3.13 p.58, 3.14 p.59, 4.1/4.5 p.74,
Figures 3.2 p.60 and 4.1 p.77; Silver slides 4, 12-13, 24, 27, 33, 34, 36, 38-40;
Szepesvari Appendix A pp.77/79). Every `data-nb-kind` matches the record's Kind
line (S&B, Silver x2, Szepesvari primary; Spinning Up secondary). Source 1's
homepage-level MIT Press href is backed by precise per-citation locators; the
free S&B PDF stays on the Background and Go-deeper reading links. The proof with
links resolves all hrefs. I did not reopen the sourcing decision.

## Reads well

Two slop tells, both at paragraph edges, both cut rather than repaired:

- "That choice is not cosmetic" (return section) is an empty conclusion dressed
  as a finding and states nothing checkable; the sentence after it carries the
  real point. Cut. I also removed the abstraction "the argument a later section
  rests on," rewriting as "A later section's convergence argument needs
  gamma < 1."
- "that makes the point of the whole section" (hand-backup opener) grades the
  passage's own importance and gestures at the lesson's structure, which the body
  is not to do. Cut; the paragraph's closing sentences already deliver the point
  (cell 14's value sits on both sides, so the sixteen equations are coupled).

Nothing was lifted from the briefing or the voice-guide exemplars: I read the
opener, the orientation definitions, and the Karpathy-style code read ("A move
up lands in the cell above with probability one") for borrowed clause order and
found none. The body keeps one word per idea (transition, return, discount,
Bellman equation for v_pi) and defines each RL term in the sentence that first
needs it, as the voice guide asks. This is lesson 1, so there is no recent record
to repeat; the five headings are built on different frames and a reader skimming
them alone recovers the argument in order.

## The experience

The rendered page holds up top to bottom. The four visuals each draw the idea
before the prose leans on it: the loop SVG carries the real quantities
(R_{t+1} = -1, the clock advancing), the gridworld SVG shows the equiprobable
policy's arrows inside every non-goal cell with the goal marked terminal, the
annotated Bellman `nb-math` legend defines each colour-coded term, and the
heatmap prints the computed values. I checked the SVG geometry for arrows that
stop short or labels that overlap and found neither; the heatmap PNG is legible,
symmetric across the diagonal, and its cell values match the direct solve.

What the lesson gives beyond its sources: no source in the record works the
matrix solve, its invertibility, and iterative policy evaluation together on one
gridworld. This lesson derives the invertibility in a single uncited line from
the contraction, computes v_pi both ways on the running grid and shows the
6.7e-10 agreement, and closes with a by-hand backup on cell 14 whose own value
appears on the right-hand side, which is the concrete reason the equations are a
coupled system and not sixteen formulas. That matches the draft-handoff's
original-work sentence and survives the read.

## Edits

- Invertibility premise: "each row of `P_pi` is a probability distribution"
  changed to "is nonnegative and sums to at most one," so the body matches the
  substochastic matrix the code inverts and the nb-note describes.
- Return section: cut "That choice is not cosmetic"; rewrote "The convergence
  argument a later section rests on needs" as "A later section's convergence
  argument needs."
- Hand-backup opener: cut "that makes the point of the whole section."

## Decision

approve. The lesson is correct (code reran clean, one imprecise premise fixed by
narrowing, not by changing a number), teaches its four ideas completely, and does
work the sources do not. Final proof with links: BLOCK 0, WARN 0, PUBLISHABLE;
3576 words.
