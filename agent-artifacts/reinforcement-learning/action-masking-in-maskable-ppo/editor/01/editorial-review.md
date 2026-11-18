# Editorial review: reinforcement-learning/action-masking-in-maskable-ppo (editor/01)

## Correct

Thesis, from the draft alone: MaskablePPO removes illegal moves only from the distributions it is
handed a mask for, and its training never pushes the network away from them, so every call that
picks a move after training has to pass the mask. Four claims carry it.

1. In training, MaskablePPO fetches `action_masks()` before every move, replaces each illegal logit
   with −10^8, stores the mask, and applies it again in the update, so no gradient reaches a logit
   at a state where its move is illegal. Held. Every cited line was read in the installed 2.9.2
   wheel (utils.py 5 and 8–19, distributions.py 59 and 61, ppo_mask.py 76–102, 216–233, 262–270,
   286–307, 339–343, 428–453, policies.py 269–323 and 355–368) and matched. `th.where` against a
   constant gives the masked positions a zero gradient. Break: the Why this matters card said
   "Before every move it asks the environment for the mask", and the second section's heading
   said "asks for the mask before every move". Both contradict the lesson's own fourth section,
   where predict fetches nothing. Fixed to training moves in the card and by a new heading.
2. The trained networks still give illegal moves about 0.3 of their probability (the headline).
   Held across seeds and length. My rerun of `compare.py` printed the page's table byte for byte;
   `compare.py 5` gave 0.28 to 0.34 for seeds 5 to 9. At 151,552 steps, seeds 0, 2 and 5 gave
   0.308, 0.325 and 0.290, with 18, 24 and 20 states whose most probable move is illegal and 0
   illegal training moves (`longcheck.py`). The draft never said why one illegal move could reach
   0.657 at the start if no gradient reaches it there. I added one sentence: the logit still
   changes, because the same weights compute every state's logits. The record supports it (the
   one-hot observation into MlpPolicy) and the stage 6 boundary is untouched.
3. PPO under hanoi.py's no-op rule spends 28 to 32 of every 100 training moves on no-ops and still
   learns the puzzle. Held (rerun identical; seeds 5 to 9: 0.29 to 0.35 and 10.0 to 12.5 moves).
4. Through SB3's evaluate_policy, the five masked agents need 34 to 63 moves per episode instead of
   10, because a deterministic agent repeats an illegal argmax until the time limit, and PPO
   trained without the mask does not. Held. I rebuilt Fig. 2's sets from a fresh seed-0 run by
   stepping the environment rather than the writer's argmax walk: the same 10 squares and the same
   33 cut starts, state for state, and the page's SVG is exactly `fig3.py`'s output. The removal
   test is on the page (PPO's columns).

Other breaks and fixes:
- The dek printed seed 0's 0.66 as a fact about "it", the network. The writer's own check found an
  illegal most probable first move only in seeds 0 and 3. Replaced (see Reads well).
- The first heading, "The trained network's most probable first move is illegal", generalized the
  same single seed. Now "Seed 0's trained network rates an illegal first move most probable".
- Fig. 2's caption said "From the output of maskable.py". That output prints only the two counts;
  the marks come from the same seed-0 network through an off-page drawing script. The caption now
  says so.
- Huang and Ontañón, checked in arXiv v3: p. 4 gives 2/16 = 0.125 and 2/576 = 0.0034 for a valid
  Source Unit picked at random; Table 2 (p. 5) gives −0.01 at 40.00 on 4×4, every penalty row
  0.00 to 1.00 on the three larger maps, and masking at 40.00 throughout. "A unit chosen at random"
  became "a unit to command, picked at random from the 16 cells of the 4×4 map", which is what the
  paper measured. This narrowed the wording to the source; nothing about the reporting was thin.
- Every `href` lands. readthedocs, PyPI and arXiv returned 200. The ten GitHub blob pages return
  403 to curl through this session's proxy and loaded through WebFetch, each at the cited tag with
  the cited code. The docs' line numbers were checked against docs/modules/ppo_mask.md at v2.9.2.
  PyPI still lists 2.9.2 as the latest sb3-contrib.
- `data-nb-kind`: all 13 are primary and correctly so. Each is the maintainers' own code, docs or
  index entry, or the authors' paper for its own experiments. The page claims no independent
  corroboration anywhere.

The orchestrator's concerns:
1. "Never" holds across ten seeds at 51,200 steps and three seeds at 151,552. The stage 6 material
   is one forward-pointing sentence with no derivation.
2. PPO stays a library. The page names its 2,048-step batches, the course's term from the
   off-the-shelf lesson, and says the update reapplies stored masks. Nothing about the objective,
   advantages or clipping appears.
3. Stamped at 3,690 words. Prose by the template's definition is 2,058 by my count.
4. The long-budget instability is wider than the handoff says. At 151,552 steps seed 0's masked
   greedy policy reaches the goal from 0 of 80 starts, seed 2's from 41, seed 5's from all 80
   (mean 10.2 moves); the writer's seed 1 was fine. Nothing on the page claims a budget past
   51,200 steps, and I added that budget to Table 1's caption so the table cannot be read as
   general. The page needs no change for it; a reader check may ask, and the answer is not on
   the page.

## Reads well

What went:
- "The wasted moves are enough for PPO to learn the puzzle." It credited the no-ops with the
  learning, which no run tests. Now "PPO learns the puzzle anyway." The takeaway's "by spending"
  became "while spending" for the same reason.
- "training that never scored an illegal move" became "never sampled", since "scored" read as
  reward and the next clause is about what PPO sampled.

From the briefing: the commission's "wherever the agent chooses an action" survives reworded in the
card and the closing line, and its sentence on the environment defining an illegal move survives in
the third section's opener. The runs on the page establish both, and the wording is the article's
own, so they stay. I found nothing taken from the Olah, Karpathy or Weng passages.

From the recent record: the dek was built "After X, it does A, and only B", the shape of the 17
November dek ("When only the choice is masked, A, and B") and close to the 14 November one. It now
reads as one clause with no "since", "because" or "so", and it carries the lesson's second half,
the evaluation cost, which the old dek left out. The second heading, "MaskablePPO asks for the mask
before every move", copied the slot and build of 17 November's "The environment sends a fresh mask
with every observation". It is now "MaskablePPO's training depends only on legal moves' logits",
with the section label changed to match. The headline shares "never" with 17 November's but not its
construction, and I kept it. It is the lesson's largest claim, and the runs above support it.

The draft is close to the guide's register: plain verbs, one step per sentence, and each section
answers the one before. It ran thin in one place, the mechanism paragraph, where a reader meets
"no gradient reaches the logit" right after seeing that logit's move rated most probable. The added
sentence closes that gap.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 and 1280 px in both
themes. The page never scrolls sideways (scrollWidth 390). Fig. 1's panels stack on a phone, and
Fig. 2's marks, legend and labels do not overlap in either theme. Tables 2 and 3 scroll inside the
house table wrapper on a phone (549 and 541 px in 348), which is the house behavior. The headings
now read as the argument in order: one network rates an illegal first move most probable, training
reads only legal logits, PPO pays three moves in ten without a mask, and SB3's evaluate_policy runs
the network unmasked. No component needed adding or cutting; Table 2 holds five rows and a chart
would show nothing more.

What it gives beyond its sources: the code and the paper describe the mechanism, and the docs give
the trap one line ("manual and optional outside of learning"). The lesson measures on the course's
own environment, across seeds, how much the masked network still favors illegal moves against a PPO
trained without a mask, what evaluating without the mask costs (34 to 63 moves against 10), and
which library call drops the mask. That matches the writer's original-work sentence.

## Edits

- Dek (header and nb-meta): replaced with "Five MaskablePPO agents that average 10 moves per episode on the four-disk Tower of Hanoi need 34 to 63 once Stable-Baselines3's evaluate_policy plays them without the mask."
- Why this matters: "Before every move" became "Before every training move".
- First heading: "Seed 0's trained network rates an illegal first move most probable".
- First section: "MaskablePPO never makes that move" became "In training, MaskablePPO never makes that move".
- Second heading: "MaskablePPO's training depends only on legal moves' logits"; data-nb-section and id "mask-every-move" became "legal-logits".
- Second section: added "The logit still changes, because the same weights compute the logits of every state."; the next sentence now reads "No part of training depends on its value where the move is illegal".
- Table 1 caption: added "after 51,200 training steps".
- Third section: "The wasted moves are enough for PPO to learn the puzzle." became "PPO learns the puzzle anyway."
- Third section: the µRTS sentence now reads "A unit to command, picked at random from the 16 cells of the 4×4 map, was valid with probability 0.125, and on that map a penalty of −0.01 matched masking's return of 40."
- Fig. 2 caption: "From the output of maskable.py." became "Drawn from seed 0's network as maskable.py trains it, whose output prints the two counts, 10 and 33."
- Fourth section: "never scored an illegal move" became "never sampled an illegal move".
- Takeaway: "by spending" became "while spending".
- `nb stamp` (words 3,690, reading 16 min, sources 13), then the brief's `nb check`: BLOCK 0, WARN 0, PUBLISHABLE.

Reruns, all in /tmp/claude-0/-home-user-the-nightly-build/efbdeaae-8835-5515-95b0-8d4030ac57a4/scratchpad/rl-editor/run/,
from listings extracted from the page and hanoi.py extracted from the 17 November page: `uv run
maskable.py` and `uv run compare.py` printed output identical to the page's; `uv run compare.py 5`
matched the handoff's seed 5 to 9 ranges; `fig2check.py` and `longcheck.py` are the editor's checks
described above. No listing changed, so the printed output still stands.

## Decision

approve: the argument holds on rerun across seeds and three times the budget, and every
required fix (the "every move" contradiction, two single-seed generalizations, a caption's
provenance and the dek's mold) was an edit I made.
