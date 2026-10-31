# editor review-brief: reinforcement-learning/environments-and-the-rl-problem (editor/01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md` (lesson 1; the four ideas; the running gridworld; required visuals and code)
- `../../writer/01/brief.md`
- `../../writer/01/draft-handoff.md` (the code outputs, the sanity checks, and the sourcing note)
- `../../writing-coach/01/voice-guide.md`
- `../../researcher/01/evidence.md` (the pinned equations with locators, the notation clashes, the known-answer tables)
- The article: `/home/user/the-nightly-build/.nb-work/reinforcement-learning/environments-and-the-rl-problem/library/reinforcement-learning/environments-and-the-rl-problem.html`
- The code beside it: `.../library/reinforcement-learning/environments-and-the-rl-problem/gridworld.py` and `evaluate.py`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/environments-and-the-rl-problem/library/reinforcement-learning/environments-and-the-rl-problem.html --series reinforcement-learning --repo /home/user/the-nightly-build`
Output: `editorial-review.md` in `editor/01/`

Decide whether this lesson publishes and edit it until it can. The writer reports
a clean proof at 3588 words (band 2000-3600, so near the ceiling: do not grow it,
trim where you can), 5 sources, four visuals, code that runs in under a second.

Correctness is the bar that never loosens, and this is a math lesson, so:
- **Re-run the code.** `uv run` both files yourself (numpy only, seconds). Confirm
  the printed v_pi matches the prose numbers and the heatmap values, that the
  direct solve and iterative evaluation agree, and that the S&B Figure 3.2 (γ=0.9)
  and Figure 4.1 sanity checks reproduce as the handoff claims. The running grid
  uses γ=0.9; confirm γ<1 holds everywhere so the cited convergence applies.
- **Check the derivation.** The Bellman expectation equation for v_pi must supply
  the Markov-property step S&B's p.59 skips; the invertibility of (I−γP_pi) must
  be argued (one line from the unique fixed point, no cite); q_pi's equation is
  cited to Silver/Spinning Up because S&B leaves it to exercises. Verify one
  notation convention holds throughout (S&B's R_{t+1}, p(s',r|s,a), P_pi and r_pi
  from p). The annotated Bellman `nb-math` legend must define every symbol it uses.
- **Display text** against the evidence record: the title, dek, and every section
  heading. Headings are argument steps in the lesson's own nouns, built
  differently from one another (this is lesson 1, so there is no recent record to
  compare against; set a good pattern). Check the dek and headings against
  spec/headlines.md.

Sourcing decision (settled by me, the orchestrator — do not reopen it): source 1
is the MIT Press publisher page for Sutton & Barto (https, authoritative). The
authors' free full-text PDF is http-only, so it stays on the Background/Go-deeper
reading links, not as the source href. Confirm source 1 carries `data-nb-locator`
text that lands the reader on the exact section/page/equation (the evidence record
has them), so the homepage-level href is backed by a precise locator. Confirm the
reading-band links resolve.

The lesson template specifics: the Why-this-matters and The-takeaway bookends are
citation-exempt and are the one place the lesson addresses the reader; judge them
like any other sentence (each must say something particular to THIS lesson, not a
generic motivation), and read them back to back as setup and resolution. The body
speaks to no one. The body ends on an `nb-note` of two or three problems
answerable from the lesson alone, each answer and working inside a `details`
element; verify the answers against the lesson and the code.

Read the rendered page in `nb preview` top to bottom: every visual for overlapping
labels or arrows that stop short (the proof catches neither), and the prose for
slop at the section and paragraph edges. The series is not strict, so banned terms
and length WARN rather than BLOCK, but hold the limits anyway (the writer reports
all at zero).

Make the edits you can from the evidence and this checkout; return to me only if
the lesson needs a different argument or a fact nobody gathered (a wrong number in
the code is yours to fix by re-running, not a send-back). After edits run
`nb stamp` and the exact proof command to BLOCK: 0, keeping the word count in band.
Report the review path, the decision (approve | redraft), the final proof result
and word count, and whether the code reran clean.
