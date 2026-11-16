# Commission: reinforcement-learning/action-discretization

Series: reinforcement-learning (Courses). Template: lesson. Strict: no. Word band 2500 to 6000, flex sections 2 to 5, min sources 1.
Production: required policy. Researcher, writer and editor run at the orchestrator's model at xhigh effort. Voice guide is pinned by the owner (writing-coach/01/voice-guide.md); no writing-coach run.

## Place in the course

Stage 3, Designing environments. Published stage-3 lessons: observation-scale (11-13), frame-stacking-and-the-markov-property (11-14), action-frequency (11-15). The remaining stage-3 action-space topics are removal, discretization, factoring and masking. This lesson takes discretization only. Factoring, removal and masking are later lessons; mention none of them beyond a sentence if needed.

## Topic and the one idea

Topic: discretizing a continuous action space for a learner that needs a finite action set.

The one idea: the number of bins trades the best return any policy over the bins can reach against the experience each action value needs. More bins lower the approximation error of the best discrete policy, and they also split the same experience across more estimates, so a fixed budget of samples learns a coarse set better and a fine set worse. The lesson should let a reader predict, before a run, which side of that trade a given budget falls on.

## Case to start from

Gymnasium's Pendulum-v1 (continuous torque in [−2, 2], swing-up and hold), with the observation discretized into a table so tabular Q-learning from earlier lessons applies, and the torque discretized into k evenly spaced levels with k varied (for example 2, 3, 5, 9, 17). Pendulum is a new environment for the course; introduce its rules inside the lesson. The writer may substitute a smaller custom environment with a continuous action if Pendulum cannot show the idea within a laptop-CPU budget, and must say why in the handoff.

Things the writer must verify, not assume: whether current Gymnasium ships an action-discretizing wrapper (and its exact name and behavior), and the exact Pendulum-v1 dynamics, reward and time limit in the installed version.

## Boundaries

- Teach only what lessons 1 to 18 taught plus the background in press/editorial.md. Continuous-action policies (Gaussian policies, SAC, DDPG) are stage 5: do not teach them. A one-sentence pointer that later lessons learn continuous actions directly is allowed.
- At most two experimental results, per the series prompt.
- Do not repeat action-frequency's material (action gap vs dt, RepeatAction). Linking it is fine where the bin spacing creates its own small gap between neighbouring actions, if that is part of the explanation.

## Required contribution

A derivation or computable bound that ties bin count to the best discrete policy's shortfall (for example, an exact or dynamic-programming solve of the discretized problem per k), set against a Q-learning run at a fixed sample budget, so the lesson shows both the ceiling and what learning reaches under it.

## Recent-pattern notes (from the last three lessons)

- Titles: three of the last four open with the learner's name ("Q-learning ..."). Do not open this title with "Q-learning" or "Tabular Q-learning".
- Arc: the last three lessons each ran "problem, then a Gymnasium wrapper fixes it" (VecNormalize, FrameStack, RepeatAction). Do not build the lesson on that arc even if a discretizing wrapper exists.
- Why-this-matters cards in the last two lessons closed on a sentence of the form "Here you predict ..." / "Working through X, you predict ...". That is now a catchphrase; do not use it.
- Definitions recur in the form "..., called X." in every recent opening card. Vary how terms are introduced.
- Recent headings often use a numeric-comparison claim ("... a tenth as much ...", "... tenfold"). Build headings differently from each other.

## Decisions log

- Researcher/01 found that on stock Pendulum-v1 the ceiling is flat in k (two levels {-2, 2} within about 1.5 return units of 65 levels), consistent with Seyde et al. 2021 on bang-bang control under a small action cost. Decided: keep Pendulum's dynamics, and make the torque cost the lesson's lever. Use a variant with a larger torque-cost coefficient (the researcher found 0.1 makes the ceiling depend on k; the writer picks the value that shows the trade plainly and states it), built by a few printed lines over Gymnasium's Pendulum, and say plainly it is a modification. The stock environment's flat ceiling appears as the case the explanation predicts: when the cost of torque is negligible the best policy is bang-bang, so extra bins buy nothing and only cost samples. One sentence and the Seyde citation, or a short check, not a third result.
- Levels: np.linspace(-2, 2, k) with nested k (for example 2, 3, 5, 9, 17), so the ceiling can only rise with k. Mention in a sentence that Gymnasium's DiscretizeAction returns bin centres, which never reach ±2 and, for even k, omit zero torque, so its ceiling changes for a reason other than spacing.
- Exploration confound flagged by the researcher (random ±2 actions swing harder, so coarse sets explore more): the writer must test it, for example by a removal test that equalizes exploration, before attributing the learned-performance gap to samples per action value.
- Results: (1) the dynamic-programming ceiling per k on the variant; (2) Q-learning at a fixed sample budget across k, against that ceiling, with seeds. Removal tests belong to the result they explain.
- Editor/01 rewrote the bound's derivation around the alternation argument (bound and printed numbers unchanged) and approved. Length: keep Fig. 3 and problem 2; the prose guide is advisory and the counted band is met. The writer handoff's original-work sentence is superseded by the review's wording.
