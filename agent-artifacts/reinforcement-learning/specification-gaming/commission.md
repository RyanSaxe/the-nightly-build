# Commission: reinforcement-learning/specification-gaming

Series: reinforcement-learning (template lesson, not strict). Words 2500 to 6000 including
code and printed output; 2 to 5 flex sections; at least one source. Voice guide is pinned
by the owner (writing-coach/01/voice-guide.md); no coach round.
Authorized by the scheduled `nb duty` result for 2026-11-19 (open section).

## Place in the course

Stage 3, Designing environments. Published so far in stage 3: observation scale, frame
stacking and the Markov property, action frequency, action discretization, action masking
in Q-learning, action masking in MaskablePPO. Stage 3's next topic is "Reward
specification, reward scale, and specification gaming". It holds more than one idea, so it
is split. This lesson takes reward specification and specification gaming. Reward scale
and potential-based shaping are later lessons; do not teach them here beyond one pointer
sentence if needed.

## Topic and the one idea

Topic: specification gaming.
The one idea: an RL agent maximizes the return of the reward it is given, not the task the
designer had in mind, so a reward that pays for a proxy of progress (an intermediate event
that can be repeated or reached without finishing) has an optimal policy that collects the
proxy instead of doing the task. The gap is a property of the MDP, visible in its exact
optimal policy before any learning, and a learner that works correctly finds it.

## Case to start from

A small tabular environment the writer builds, with a goal and a proxy reward for an
intermediate event that can be collected repeatedly, in the spirit of the boat-racing game
whose agent circled to hit respawning targets instead of finishing the race (OpenAI's 2016
"Faulty reward functions in the wild", Clark and Amodei). Solve it exactly with value
iteration (lesson `finding-optimal-policies`) and also learn it with tabular Q-learning
(`sarsa-and-q-learning`), so the reader sees the gaming policy is the optimum and not a
learning bug. Measure the true task (finishing) separately from the return. The writer
chooses the environment's details, its name, the experiments and the page structure. It
must be a new environment, not the slippery grid, the Tower of Hanoi, the pendulum, the
docking cart or the rolling ball.

Use the discount and episode length the course has taught (termination vs truncation) where
they decide whether looping beats finishing; that dependence is a fair result to derive.

## What the researcher supplies

Only what the page will use: the primary source for the boat-racing example; Krakovna et
al.'s specification-gaming examples list (DeepMind, 2020 blog and the shared list) with one
or two examples verified against their originals; and optionally Sutton and Barto's
statement that the reward signal should say what to achieve, not how (the passage and
section). No survey of reward hacking in language models; that is stage 8.

## Boundaries

- Do not teach potential-based shaping, reward normalization or reward scale beyond a
  pointer. Do not teach anything from stage 4 onward.
- At most two experimental results; any causal claim gets a removal test on the page.
- Neighbouring articles in this edition: the daily brief (news) and one feature on a
  current story; no overlap expected.

## Recent pattern notes (last three lessons: maskable PPO, masking in Q-learning,
discretization)

- The "Why this matters" band has closed three times running with "You will ... then
  ..." / "On a ... you will watch ... and derive ...". Close it differently.
- First sections have opened on "We train X with seed 0 ..." and on the environment's
  rules; headings lean on "X never/still/only ..." claim forms with a named library.
  Vary the heading shapes.
- Deks have stacked two numbers from runs in one long sentence with a named library
  ("Five MaskablePPO agents that average 10 moves ... need 34 to 63 once ...");
  make this dek one lean sentence.
- Phrases recurring across lessons: "the four-disk puzzle", "the course's grid",
  "a budget of N steps". Avoid carrying them in.

## Production

Required directives: researcher, writer and editor at the orchestrator's model ("inherit")
and xhigh effort. This runtime's subagents inherit the session model; effort is set to
xhigh on each Agent call where the runtime honours it. Recorded per role in this file
as each completes.

## Decisions after research (orchestrator)

- OpenAI's 2016 post could not be fetched from openai.com here (403; a further fetch was
  refused by this runtime). Cite it at its own URL for the boat example as the original
  report, describe it in the lesson's words, and do not quote it verbatim. Take its date and
  byline from DeepMind's 2020 post, which cites it, and say only what both agree on.
- Do not repeat the Krakovna list's descriptions of the bicycle or the Lego brick; if either
  is used, describe it from the original paper as the evidence records. The Lego paper's
  grasp-reward-ends-before-stack-reward case may be used as a second real example.
- "The agent maximizes the return" is stated for the tabular, convergent case the lesson
  works in; give Turner's counter-view one sentence and a pointer if it helps, no more.
- The claim that the gaming policy is optimal rests on the lesson's own value-iteration solve;
  the Q-learning run is checked against it.
- Researcher model: session model (inherit), effort xhigh, as required.

## Production record (orchestrator)

- Researcher 01, writer 01, editor 01–03: session model (inherit), effort xhigh, as required.
- Reader checks: two, as the lesson template sets. The first ran after editor 01's approval;
  editor 02 rewrote the last section, so a second, fresh reader ran; editor 03 answered it by
  cutting and correcting text and approved. The reports are copied verbatim in
  editor/02 and editor/03 review-brief.md.
- Decided: the OpenAI 2016 post is cited at its own URL, undated in quotation, with byline
  and year as DeepMind's 2020 post gives them, because openai.com refused every fetch here.
