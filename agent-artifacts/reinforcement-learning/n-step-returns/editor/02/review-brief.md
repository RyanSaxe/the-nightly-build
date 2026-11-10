# editor brief: reinforcement-learning/n-step-returns (02)

Inputs:
- ../../editorial-direction.md — standing directions (template identity: Reader check section governs this round)
- ../../commission.md — topic, idea, boundaries, decisions, recent-pattern notes
- ../../writer/01/brief.md — the exact writer brief
- ../../writing-coach/01/voice-guide.md — pinned series voice
- ../../researcher/01/evidence.md — claim set
- ../../writer/01/draft-handoff.md — writer's handoff and main-idea sentence
- ../01/editorial-review.md — your first review
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/n-step-returns/library/reinforcement-learning/n-step-returns.html
Writer's code and checks: /tmp/claude-0/-home-user-the-nightly-build/f459be86-7567-53db-a107-d49609878cc2/scratchpad/rl-writer/code/
Output: editor/02/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/n-step-returns/library/reinforcement-learning/n-step-returns.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

This round: answer reader check 1, copied below verbatim. Compare the reader's
restatement with the main-idea sentence. For each place, first ask whether the
passage can be cut; add explanation only where the main idea needs it; record
your action on each place in the review. Prose must stay at or under about
2,200 words (it was 2,176), so most fixes should cut or replace, not add.
Note the factual point in the first item: if the stated reason for the n = 3 vs
n = 6 difference is wrong, correct it from a rerun of the printed code. If the
`--expected` removal test is close to guaranteed by construction, say what it
does and does not show, or cut the causal claim it supports. Rerun any listing
you change and update numbers to match. Then `nb stamp` and the proof (links
included) to BLOCK: 0. Tell me in your report whether your changes alter the
lesson's central explanation or rewrite a whole section, since that decides
whether a second reader check runs.

## Reader check 1 (verbatim)

**Reader report: "Four-step TD learns a 19-state random walk faster than TD(0) or Monte Carlo"**

**1. Main idea**
n-step TD moves a state's estimate toward the next n rewards plus the current estimate of the state n moves later. With n = 1 it is TD(0); when n reaches past the end of the episode it is constant-step Monte Carlo. On the 19-state walk over the first 10 episodes, a middle n (4) does best, each n at its own best step size. TD(0) passes the outcome back one state per pass. Monte Carlo's ±1 returns are so noisy that its best step size is tiny.

**2. Where I got lost (worst first)**

- **The n = 3 versus n = 6 numbers.** The lesson says "n = 6 also moves V(16), and it moves V(17) and V(18) twice, to 0.75, because it updates on every visit." But n = 3 also updates on every visit. Its first targets for 17 and 18 just read estimates that were still 0. I had to replay the episode by hand to see why V(17) ends at 0.5 under n = 3. The stated reason points me the wrong way.
- **Undefined terms in "Why this matters."** "n-step SARSA, DQN's multi-step targets and the λ-return behind generalized advantage estimation are built from these targets." The earlier lesson mentions DQN only by name. SARSA, the λ-return and GAE appear nowhere. I can't tell what the sentence is meant to tell me. The same paragraph's "code the update's n-move delay" uses "delay" before the lesson has explained it.
- **Time-subscripted estimates.** "V_{t+n−1}(S_{t+n})" and "V_{t+n}(S_t)" appear without a definition. The earlier lesson always writes plain V. The caption "as it stands when the target is complete" helps, but the very next derivation drops the subscripts again with no comment.
- **"A return that stops where it starts is the estimate there."** This reads as a definition stated as if it were a fact. Saying "define G_{t+n:t+n} = V(S_{t+n})" would be clearer.
- **"Three unused sets of 100 seeds keep n = 4 lowest, and n = 3 and n = 5, which the sweep skips, do as well."** I can't tell what "unused" means (held out? not plotted?). "Do as well" could mean they tie with n = 4 or that they also beat TD(0) and Monte Carlo. Nearby, "set up as in Sutton's code for that figure" doesn't say what that setup changes. I can't say why that phrase is there.
- **The `--expected` test.** Monte Carlo's expected target from state s is exactly s/10 − 1, the true value. So "the longest target does best" looks close to guaranteed, not a test of anything. The lesson doesn't address this. It also doesn't explain why "α = 1 is best for every n." I assume it is because with no noise there is nothing to average, but the lesson leaves that to me.
- **"A short target wins when the outcome has little distance left to travel."** "Distance left to travel" is a metaphor. For episodes 91–100 I had to work out that it means the estimates already carry the outcome. The reasoning is only half stated.
- **The code.** Three things stopped me:
  - `update(tau, float("inf"))` uses infinity to mean "the episode hasn't ended," with no comment.
  - The guard `0 < s < len(V) - 1` isn't explained.
  - The running sum C silently assumes γ = 1, while the formula shown keeps γ.

  The sentence "Sutton and Barto's version keeps only the last n + 1 states and rewards" is an aside whose purpose I can't name.
- **"Online updates."** The phrase in "Online updates change the estimates during an episode" isn't defined. The earlier lesson only said "if V stays fixed during an episode."
- **Monte Carlo's small step.** "A walk from the middle passes the middle states many times, and every visit moves toward the same outcome…" I had to supply the missing link myself: many same-direction updates in one episode act like one very large step, so α must be small.

**3. Sections I could skip**
- "The n-step error is the first n TD errors": the main idea doesn't use it.
- Most of "The target for time t is complete at time t + n" (the delay mechanics and the code). The results don't depend on it.
- Watkins' attribution and the "Sutton's code" detail.

**4. Results reported without their meaning**
- "Three unused sets of 100 seeds keep n = 4 lowest… do as well." I can't tell how robust the result is or how wide the margins are.
- "TD(0) is best on a 5-state walk… and… over episodes 91 to 100." There are no numbers, no best n for the other settings and no margins. The code and outputs behind them are in a collapsed section.
- "The error falls as n grows, from 0.28 for TD(0) to 0.06 for Monte Carlo, and α = 1 is best for every n." The lesson never says what α = 1 being best implies, or what the leftover 0.06 is.
- "At α = 1, TD(0) has the lowest error, and at α = 0.05, n = 32 does." The meaning is given in the next sentence, so this one is fine.
- "from −0.47 to 0.64 at state 10" (the Monte Carlo spread). The range is given, but there is no comparison to the n = 4 band, so I have no sense of scale.

## Orchestrator note

The code and delay mechanics stay: the series prompt requires every listing a
lesson relies on to be printed and run, and the commission asks for the τ
bookkeeping to be taught with the code. Answer the reader's code questions
inside the listing (comments) or by a few words in prose, not by cutting it.
