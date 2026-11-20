# Commission: reinforcement-learning/potential-based-shaping

Run: scheduled edition of 2026-11-20. Neighbours in this edition: daily-brief/2026-11-20 (news brief) and one feature (topic not reinforcement learning). Nothing in either overlaps this lesson.

## Topic and place in the course

Stage 3, "Potential-based shaping and the limits of its guarantee". The stage-3 topics taught so far: observation scale, frame stacking and the Markov property, action frequency, action discretization, action masking in Q-learning and in MaskablePPO, and reward specification with specification gaming (2026-11-19). That last lesson's Go deeper entry on Ng, Harada and Russell says a later lesson builds the progress reward that leaves the optimal policy unchanged. This is that lesson.

## The one idea

A shaping reward of the form F(s, a, s') = γΦ(s') − Φ(s) telescopes along any trajectory, so the shaped discounted return equals the original return minus Φ(s₀) plus a discounted term in the potential of the state where the return stops. Every policy's value from a given state therefore shifts by the same amount, and the optimal policy is unchanged, as long as that final term vanishes. The limits of the guarantee are exactly the cases where it does not vanish or where the statement is about something other than what the agent does while it learns.

The lesson derives this in full (Ng, Harada and Russell 1999 is the paper that introduced it) and checks the derivation with runs.

## The case to start from

Lesson 2026-11-19's eight-cell race (reinforcement-learning/specification-gaming, race.py): checkpoint crossing 1→2 pays 1 on every forward crossing, finish pays 10, and at γ = 0.99 the optimal policy loops. Start from that loop. Replace the repeatable checkpoint with a potential-based progress reward and show the loop's net shaping reward around one cycle. Link that lesson for the race's rules and reuse or import its code where the course rules allow (a later lesson may import a file printed in an earlier lesson if it links it).

The race may be extended (more cells, a time limit) where a limit of the guarantee needs it. The writer may add a second small environment if a limit cannot be shown on the race, but should not add one for variety.

## Limits the lesson should cover (the writer chooses which make the two reported results)

- The terminal state's potential: in an episodic task the derivation needs Φ = 0 at termination (or a fixed convention); a nonzero terminal potential changes which policies are optimal.
- Truncation by a time limit (link reinforcement-learning/termination-and-truncation): what the leftover γ^T Φ(s_T) term does when episodes are cut.
- The guarantee is about the optimal policy of the MDP. It says nothing about how fast or whether a learner finds it, and a bad potential can slow learning. Wiewiora (2003) shows potential-based shaping is equivalent to initializing Q with Φ for a class of learners; mention or use it if the researcher confirms it.
- Ng, Harada and Russell also show necessity: a shaping term not of this form has some MDP whose optimal policy it changes. State it, give it a sentence, do not derive it unless it is cheap.

## Boundaries

- Outside a project lesson: at most two experimental results, each with its removal test on the page.
- Do not teach PPO, DQN or any algorithm the course has not taught. Q-learning and value iteration are taught; Stable-Baselines3 PPO may be used as an off-the-shelf agent without explaining its algorithm.
- Mention only (one sentence, a pointer at most): dynamic potentials (Devlin and Kudenko), and shaping in language-model RL. Do not give them sections.
- Sim-to-real and procedural generation belong to the next stage-3 topic. Leave them out.

## Production

- Voice guide: pinned series guide (writing-coach/01, written by nb start-article). No coach invoked.
- Policy is required: researcher, writer and editor at the orchestrator's model ("inherit") and effort xhigh. Recorded actuals: researcher, writer, editor run as subagents on the orchestrator's model with effort xhigh.
- Sources floor is 1. The researcher gathers only what the page will use: Ng, Harada and Russell (1999) with locators for the theorem, its proof and the necessity direction; Wiewiora (2003) if it supports the initialization equivalence; Sutton and Barto passages on shaping if they help. Grimm/other later critiques only if they establish a limit the lesson states.

## Recent-pattern notes for writer and editor

From the last five lessons (specification-gaming, action-masking-in-maskable-ppo, action-masking-in-q-learning, action-discretization, action-frequency):

- Headlines are almost all "<finding with a number> in/on <named environment>" sentences. A headline built around a number and a named environment is now the house pattern; find a different build if the finding allows.
- "Why this matters" bookends recently close with "You will ..." (maskable-ppo, discretization) or "...let you find ... before any agent trains" (spec-gaming). Avoid both closes.
- Several takeaways end with a two-sentence reversal: "By its return, the looping agent is the best possible. A count of finishes shows that it fails the task." Do not close on a by-X/by-Y pairing again.
- Section headings recently lean on "<agent/method> learns/finds the X that Y found" and on a cell number as subject ("Cell 2 heads for the finish..."). Vary.
- Phrases recurring across lessons: "the course's grid", "an off-the-shelf agent", "from the rules alone". Use them only where plain reference needs them.

## Decisions after research (researcher/01)

- Cite the trajectory-sum form of the derivation to Grześ (2017, Eq. 3) where it is taken from there; Ng, Harada and Russell's own proof goes through the Bellman equation and is cited for the theorem, its necessity direction and the bicycle. The lesson's own derivation on the page needs no citation.
- The "zero net shaping around a loop" statement is Ng's for γ = 1 only. At γ < 1 the lesson states and shows the actual value (negative for a positive potential), not the γ = 1 claim.
- Truncation: no source covers a learner that bootstraps past a time-limit cut. Decided: the writer derives it (and checks it by a run if it is one of the two results): under bootstrapping, the cut state keeps its potential; setting it to 0 at a cut is the error. Sources saying "potential 0 at the end" treat the cut as termination, and the lesson says so where it uses them.
- Wiewiora's equivalence is stated for tabular Q-learning only, with its conditions.
- Pins: gymnasium 1.4.0, stable-baselines3 2.9.2 if used.

## Decisions during drafting (writer/01)

- Potential Φ = −(moves left to the finish), which is 0 at the finish without a special terminal rule. With that potential a lap of the loop at γ = 0.99 nets a positive shaping amount (+0.12 on the page), not the negative amount the commission's example assumed for a positive potential. Accepted: the page gives the value and the general (γ^k − 1)Φ formula, and the lesson must make clear why a positive lap amount does not make looping optimal.
- Source titles and authors read from the recorded URLs where the evidence record gave only venues: accepted; the editor verifies them.
- Shaping in language-model RL: not mentioned, since nothing was gathered on it. Accepted (it was mention-only).
