# writing-coach brief: reinforcement-learning/finding-optimal-policies (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard for this article.
- `../../commission.md` — what this lesson teaches and how it sits in the course.
- Lesson 1's voice guide, to carry the course's voice forward unchanged. Read it with:
  `git show origin/library:agent-artifacts/reinforcement-learning/environments-and-the-rl-problem/writing-coach/01/voice-guide.md`
  (run from the repo root `/home/user/the-nightly-build`).
Output: `voice-guide.md` (write it beside this brief).

Work from these inputs. Do not tour the repository, the Git history or the
archive for background beyond the one lesson-1 file named above. Where something
you need is missing, ask me (the orchestrator).

This is lesson 2 of a running course whose voice is already set by lesson 1.
Your job is continuity, not reinvention. Keep the same exemplars and the same
registers lesson 1 settled: the body as a patient colleague working the problem
on paper, speaking to no one and never referring to itself; the two bookends as
one particular teacher addressing the reader directly, plain not loud. Reaffirm
the three exemplar writers lesson 1 used (Chris Olah on carrying a rule down to
a checkable number; Gregory Gundersen on quoting an unsatisfactory explanation,
asking what the vague phrase must mean, then deriving line by line; Andrej
Karpathy on defining an object by what goes in and comes out before its
insides). You may reuse the same quoted passages; if you quote anything new,
fetch the page and record the URL and retrieval date beside the quote.

What is specific to lesson 2, and what the voice guide should orient around:
- The lesson's move is comparison and improvement: ranking actions by their
  value, picking the greedy one, and iterating. The voice should show how to
  narrate a `max` and an argmax in plain words before the notation, and how to
  present "this policy beats that one at every cell" as arithmetic the reader
  can check, not as a claim.
- The one allowed "is not X, it is Y" correction should be spent only on a real
  misconception a careful reader would reach here (for example, that you must
  re-run full policy evaluation to improve a policy, when one greedy step
  already helps). Name it only if it is real.
- Keep the guidance on leaving out any aside that does not help the reader
  compute, check or understand the next quantity. Lesson 2 runs code and has a
  word budget.

Keep the voice guide short and usable: how the piece should sound, then the
exemplar passages with what to copy from each. Meet `spec/slop.md` in your own
prose.
