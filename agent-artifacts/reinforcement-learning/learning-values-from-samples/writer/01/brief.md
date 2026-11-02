# writer brief: reinforcement-learning/learning-values-from-samples (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/reinforcement-learning/learning-values-from-samples/editorial-direction.md
- Commission: .../commission.md (teaching plan, visuals, code, and the recent-pattern notes to break)
- Evidence: .../researcher/01/evidence.md
- Voice guide: .../writing-coach/01/voice-guide.md
- Article to edit: /home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/library/reinforcement-learning/learning-values-from-samples.html
- Markup contract + furniture: .nb-context/template-contract.yaml and .nb-context/furniture/{engine,press}.md under the workspace root (/home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/)
- Lesson 1 and 2 full text: `./nb history --show reinforcement-learning/environments-and-the-rl-problem` and `... finding-optimal-policies` (from /home/user/the-nightly-build). Read them: you must import lesson 1's gridworld.py and build on, not repeat, their content.

Output:
- The article HTML above, edited in place.
- draft-handoff.md in .../writer/01/
- Only the chart script(s) `chart-N.py` and their rendered `chart-N.png` committed beside the article in the library dir, exactly as lessons 1 and 2 did (look: the library holds only the article HTML plus `finding-optimal-policies/chart-1.py` and `.png`). The code LISTINGS (gridworld.py, samples.py) are shown inline in the HTML as `nb-code` figures and are NOT committed as separate files. Lesson 2 imported lesson 1's gridworld.py "unchanged" and showed only control.py as a new listing; do the same with samples.py.
- To actually run the code: reconstruct lesson 1's gridworld.py (its full listing is in `./nb history --show reinforcement-learning/environments-and-the-rl-problem`) into a scratch working directory, write samples.py there, `uv run` it to get real output, then paste the verified listing and output into the HTML. The chart script you commit reads the same verified series.

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/library/reinforcement-learning/learning-values-from-samples.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive for background beyond lessons 1-2. Where something you need is missing, ask me (the orchestrator).

This round's focus:
- READ the commission's "Query decisions (orchestrator, after research 01)" section and follow it exactly. In short: the bias/variance contrast is earned from your runs (not asserted as a theorem) and "which converges faster" stays an open question; "MC is unbiased" means FIRST-VISIT MC (every-visit is biased at finite n); make the RMS curves actually converge using 1/N(s) for MC and a decaying step size for TD(0), or state the floor honestly if any constant alpha is used; frame TD-Gammon honestly (it learned a value function from self-play by TD, but is TD(lambda)+neural-net combined prediction/control, not this lesson's tabular TD(0) prediction — use Tesauro's own game counts).
- RUN ALL CODE. Every number on the page comes from an actual `uv run`. The MC and TD estimators must use only sampled episodes (gridworld.episode) and observed rewards/next-states; they must not read P, R, transitions, or fixed_policy. Import the exact linear solve only to SCORE the estimates (report error vs the known v_pi), never inside an estimator. Lesson 1's v_pi(13) = -2.01 is the yardstick. Scale runs to finish in a few minutes on a laptop CPU.
- Teach in the commission's order: the model is gone -> Monte Carlo prediction (first-visit vs every-visit, incremental and constant-alpha update, unbiased/high-variance/needs-complete-episodes) -> TD(0) (the update, the TD error, bootstraps/online, biased/lower-variance) -> the bias-variance contrast shown with real runs -> why this is not yet control (you'd need action values q and exploration; that is the next lesson).
- Draw the mechanism: an inline-SVG backup contrast (MC full trajectory vs TD one-step bootstrap), a computed `nb chart` learning-curve (RMS error vs episodes for MC and TD with across-seed spread), and a "what it learned" value-grid heatmap converging to lesson 1's exact grid. Annotated nb-math for the MC update and the TD(0) update/TD error. Look at every rendered visual (use nb preview) before handing off; check for overlapping labels and arrows that stop short.
- Note in prose that lesson 1 already averaged 20,000 sampled returns for cell 13 as a one-cell check with the model known; this lesson makes model-free estimation the subject and covers the whole value function and TD, which that one-cell average could not show. Do not reintroduce MC as brand new.

BREAK these recent shapes (the editor will compare against them):
- Do NOT open "Why this matters" on AlphaGo/AlphaZero/DeepMind. Lessons 1 and 2 both did. Use the real case the evidence confirmed (TD-Gammon, or the dopamine/TD-error result).
- Prior openers: L1 "A walker on a slippery grid follows a fixed rule for its moves. How good is each cell to stand on?"; L2 "Lesson 1 drew a policy on a slippery 4x4 grid by hand, worked out that standing on cell 13 is worth -2.01, and then said the obvious out loud..." Open differently.
- Prior dek mold (do not reuse): "On [the] slippery grid, [method/number] [verb] cell 13 from X to Y, while [contrast]." Build a different dek frame.
- Prior body-closers both end on "...the next lesson" / "the subject of the next lesson." Point forward in different words.
- Prior takeaways both close on a reflective "remember the pair of them" style line. Close on this lesson's own finding.
- Prior heading shapes to avoid echoing: L2's "A max in place of the average", "Evaluate, improve, repeat until the arrows stop". Build headings as this lesson's own argument steps and vary the construction.

Do original work: state in one sentence (in draft-handoff.md) what this lesson does to the sources that the sources do not do, and make it visible on the page. Fill the nb-meta dates/harness/model (writer model: the orchestrator model, Opus 4.8; harness: Claude Code). Run `nb stamp` then the full `nb check` (links included) until BLOCK: 0. Report the handoff path and any warning you left on purpose.
