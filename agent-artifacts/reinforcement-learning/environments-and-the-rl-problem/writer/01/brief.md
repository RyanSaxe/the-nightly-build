# writer brief: reinforcement-learning/environments-and-the-rl-problem (01)

Inputs:
- `../../editorial-direction.md` (house + press + lesson-template + series direction)
- `../../commission.md` (scope, the four ideas, the running gridworld, required visuals and code)
- `../../writing-coach/01/voice-guide.md` (how this lesson sounds)
- `../../researcher/01/evidence.md` (the pinned equations, locators, notation clashes, and known-answer tables)
Output: `/home/user/the-nightly-build/.nb-work/reinforcement-learning/environments-and-the-rl-problem/library/reinforcement-learning/environments-and-the-rl-problem.html`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/environments-and-the-rl-problem/library/reinforcement-learning/environments-and-the-rl-problem.html --series reinforcement-learning --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. The effective markup contract and furniture catalogs are
under `.nb-work/reinforcement-learning/environments-and-the-rl-problem/.nb-context/`;
read them and `spec/charts.md` for chart provenance. Where something you need is
missing, ask me (the orchestrator) rather than inventing.

This is lesson 1 of the course and the library holds no prior lessons, so there
are no recent openers or shapes to break; you set the patterns. Edit the article
`nb start-article` initialized at the output path.

This round's decisions and caveats (these come from the evidence record's limits
and are not negotiable sourcing points):

- **Discount.** Use gamma = 0.9 for the running gridworld. Every cited
  convergence and contraction argument (Silver, Szepesvari) needs gamma < 1, so
  do not use gamma = 1. Say in prose that the discount is what makes the cited
  convergence apply.
- **Derive in full.** The Bellman expectation equation for v_pi: supply the
  Markov-property step S&B's p.59 derivation skips (replacing
  E[G_{t+1}|S_{t+1}=s'] with v_pi(s')). For the matrix solve, derive that
  (I - gamma P_pi) is invertible from the unique fixed point of the affine
  operator T_pi in one line; no source states invertibility, so do not cite one
  for it. The q_pi Bellman equation is not numbered in S&B (its Exercises 3.17,
  4.3); cite Silver Lecture 2 or Spinning Up for q_pi's form.
- **One notation.** Use S&B's convention throughout: reward R_{t+1}, the
  four-argument dynamics p(s',r | s,a), and P_pi and r_pi arrays defined from p.
  Do not copy Spinning Up's ambiguous r(s,a)-inside-an-expectation form.
- **Code that ran.** Write the gridworld MDP and the policy-evaluation code as
  Python with PEP 723 inline script metadata so `uv run file.py` works, numpy the
  only dependency, each run finishing in seconds on a laptop CPU. Run every
  listing as printed and report only the numbers it produced. Sanity-check your
  implementation against the known-answer tables the evidence record gives (S&B
  Figure 3.2 right at gamma=0.9 and Figure 4.1); if your gridworld differs from
  S&B's, verify by agreement between the direct solve and iterative evaluation on
  your own grid. The prose numbers and the heatmap must be the exact values the
  code printed.
- **Visuals (draw before explaining).** (1) the agent-environment loop as inline
  SVG with the real quantities (state and reward in, action out, clock advancing);
  (2) the gridworld drawn as a grid with goal, step reward, and one policy's
  arrows, inline SVG; (3) the computed state-value heatmap via `nb chart` from the
  values the code produced, caption citing the lesson's own computation; (4) the
  Bellman expectation equation as an annotated `nb-math` figure, every symbol
  defined in the legend. Use theme variables (`var(--ink)` etc.) and the SVG
  sizing the press direction specifies. Run `nb preview` and look at every visual
  for overlapping labels or arrows that stop short.
- **Structure.** Why-this-matters bookend, orientation, 2-5 flex sections, The-
  takeaway bookend, Sources. Write the body first; write both bookends last so
  they describe the lesson actually written. End the body with an `nb-note` of
  two or three problems answerable from the lesson alone, each answer and its
  working inside a `details` element. Background band points outside this paper
  (no earlier lesson exists); Go-deeper names which part of each paper to read
  next and why.
- **nb-meta.** date `2026-10-31`; keep mode `open`; set `order` to `1`; set
  `tags` to `["markov-decision-process","bellman-equations","value-functions"]`;
  `harness` to `claude-code-routine`; `model` to `claude-opus-4-8`. Make the
  `nb-meta` dek and the rendered dekline identical. `nb stamp` writes the counts.
- **Banned terms** (merged list): em-dash max 4, "leverage" max 1, "load-bearing"
  0, "mechanism"/"mechanisms" max 1. The series is not strict so these warn, but
  honor them; rewrite rather than synonym-swap.

Do the original work: say in one sentence (in `draft-handoff.md`, not the
article) what this lesson does with the sources that the sources do not do.
Iterate the proof with `--no-check-links`, fix warnings in batches, then run
`nb stamp` and the exact proof command above with links until `BLOCK: 0`. Write
`draft-handoff.md` in `writer/01/` with the original-work sentence, the final
proof result and any warning you left on purpose, the actual code outputs you
reported, and any open question. Report the handoff path and any warning left.
