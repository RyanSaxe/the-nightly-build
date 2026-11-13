# editor brief: reinforcement-learning/observation-scale (02)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editorial-direction.md: the standing directions, series prompt and lesson template (see "Reader check")
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/commission.md: topic, idea, case, boundaries, recent patterns and decisions (source 1 ruling at the end)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/brief.md: the exact writer brief
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writing-coach/01/voice-guide.md: the pinned series voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/researcher/01/evidence.md: the evidence record
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/draft-handoff.md and /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/code/: the handoff, code and checks
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editor/01/editorial-review.md: your first review
- The article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editor/02/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Source 1 ruling: keep the https address in Sources and the http address in
Go deeper (commission, last decision). No further action on it.

This round is the reader check. Compare the reader's restatement with the
lesson's main idea; for each place, first ask whether the passage can be cut,
add explanation only where the main idea needs it, and record your action on
each place. The lesson is at the prose target, so prefer cuts. Note the
reader's point that the headline reads as causal while the body leaves the PPO
cause open: decide whether the headline and takeaway claim only what the
removal tests show (the units and normalization rows), and fix them if not.
Rerun any listing you change, as printed. After any edit, run
`/home/user/the-nightly-build/nb stamp <article>` and the proof until BLOCK: 0.

## Reader report (verbatim)

**1. Main idea**
Gradient descent with one step size on a linear value estimate is governed by the eigenvalues of A = E[xxᵀ]. The largest eigenvalue caps the step size at 2/λmax, and the ratio κ = λmax/λmin sets how slowly the slowest weight learns. Reporting a feature in units c times larger multiplies its eigenvalue by about c², so a change of units alone can stall learning. Standardizing each component removes this, and for PPO the normalization statistics then count as part of the trained agent: you save them, reload them and freeze them to evaluate it.

**2. Where I got lost (worst first)**

- **The millimetre row of linear.py's output.** The text says "After a million, the velocity weight has reached 3.8 of its 19.6." The same row also shows the position weight at +0.003922 against w* = +0.02097, which is under 20% of the way there. The lesson had led me to expect the large-eigenvalue direction to converge fast. I eventually worked out why it doesn't: at α = 2/(λmin+λmax), the fastest direction's factor is about −(κ−1)/(κ+1) ≈ −1, so it oscillates and barely shrinks. The lesson never says this, and the prose talks only about velocity. On screen the output box also cuts these columns off ("+3.8", "+19.5").
- **"bound" means two things.** "Each bound sits where the eigenvalues put it" refers to 2/λmax. The next paragraph's "inside the bound of 77.5 that κ sets" refers to a step count. The formula behind 77.5, ln(100)/−ln((κ−1)/(κ+1)), appears only in the code, so I couldn't check the prose number without reading linear.py.
- **"A run that updates on one sample at a time multiplies that sample's error by 1 − α‖x‖², 0.87 and −24,999 in Table 1".** The lesson has just defined "error" as e = w − w*. Here it means the residual G − v̂ for one state. I had to recompute Table 1 to see that.
- **Raw metres versus PPO.** In metres the position (±0.9) and velocity (±0.3) are already zero-mean and similar in scale, with κ = 34 for the linear learner. Yet Table 2 shows raw metres at 125–198 steps for four of five seeds, against 54–120 normalized. The text only says "Raw runs in metres vary more." That doesn't follow from the eigenvalue story, and the lesson doesn't address it.
- **"A start right of the centre docks after bouncing".** The policy always pushes right on that side. After a bounce, constant acceleration should bring the cart back to the dock at the same speed, so I couldn't see how it ever arrives slowly enough to dock. The "always pushing right, 127 steps" baseline has the same puzzle.
- **The title's claim versus the body's hedge.** The title says millimetres "keeps PPO from using a cart's velocity". The PPO section ends: "These runs do not separate either effect from conditioning, so they show what the units do to PPO and leave the cause open." The linear analysis is therefore an analogy for PPO, not an explanation, but the title and takeaway read as causal.
- **"Averaged over the starts".** The gradient Monte Carlo lesson updates at every visited time step. linear.py fits only each episode's start state. That's fine for a regression, but the lesson doesn't say it departs from the earlier update.
- **"standardized components make A their correlation matrix bordered by a 1".** I had to work out what "bordered" means here: a block-diagonal matrix with 1 for the constant feature and the correlation matrix beside it.
- **"Against the constant feature, uncorrelated means a mean of zero."** Correct but too terse. One clause explaining that E[xᵢ·1] = E[xᵢ] would fix it.
- **Table 2's "USES VELOCITY" column.** It shows a range over seeds of the "share of 41 grid positions at which the move changes with velocity". The lesson doesn't say over which velocity grid, or what threshold counts as "changes".
- **"Seeds 5 to 9, from uv run agents.py 5".** The script is collapsed, so I can't tell what the argument means.
- **NormalizeObservation and obs_rms.** "obs_rms" is never defined, and I can't say why this Gymnasium paragraph is in a lesson that uses SB3 throughout.

**3. Sections I could skip and still explain the main idea**
- The single-sample paragraph ("The runs below apply the expected update…").
- The Gymnasium NormalizeObservation paragraph.
- The seeds 5–9 sentences.
- The Problems.
- The dock.py listing; its prose summary is enough.
- Fig. 1; Table 1 carries the same point.

**4. Results reported without saying what they mean**
- "seed 2 is the weakest in both". The lesson never says why this matters.
- "One of those seeds almost never docks after training through VecNormalize in either unit system." This sits beside the claim that normalization helps, with no comment on it.
- "Four of the five networks from seeds 5 to 9 fail the same way." Nothing is said about the fifth.
- Raw metres versus normalized metres in Table 2 (see section 2). Normalization clearly helps even in metres, and the lesson doesn't say what that implies.
- The millimetre position weight still far from w* after 10⁶ steps (see section 2).
- "one of them pushes toward the centre from both sides and never docks". The lesson doesn't say what this shows beyond "ignores velocity".

(Orchestrator note: the Problems and the dock.py listing are template- and series-required; do not cut them.)
