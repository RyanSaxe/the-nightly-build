# Draft handoff: reinforcement-learning/action-masking-in-maskable-ppo (writer 01)

## Main idea (28 words)

MaskablePPO samples only the legal moves the environment reports before each move, so its network
never learns which are illegal, and every call choosing a move needs the mask.

## Original work

The lesson runs sb3-contrib's masking, which the source and the paper only describe, on the
course's own Hanoi environment across seeds, and shows that the masked network keeps about 0.3 of
its probability on illegal moves (PPO trained without the mask: 0.02 to 0.03), so SB3's
evaluate_policy, which drops the mask without a warning, raises its moves per episode from 10 to
34 to 63.

## Proof

`nb stamp` (words=3660, reading_minutes=16, sources=13), then the brief's `nb check` with links:
BLOCK 0, WARN 0, PUBLISHABLE. No warning left. Prose by the template's definition (cards, captions,
table cells, problems; no code, output, equations, drawings, reading bands or sources) is about
2,030 words by my count.

## Code and runs

All three listings were run exactly as printed, from one folder holding hanoi.py (byte-identical to
the 17 November listing), maskable.py and compare.py, with `uv run`: maskable.py about 53 s;
compare.py 2 min 49 s to 3 min 15 s on 4 cores (one seed per process); compare.py ran three times
with identical output. The page's run copies are in
`/tmp/claude-0/-home-user-the-nightly-build/efbdeaae-8835-5515-95b0-8d4030ac57a4/scratchpad/rl-writer/page/`.
Throwaway check scripts are in `.../scratchpad/rl-writer/checks/` (they import maskable.py and,
for BFS, leak.py and masked_q.py from the 17 November lesson; the saved models they read are in
`.../rl-writer/models/`, rebuilt by `trainsave.py` and `trainsave2.py`).

The illegal move rule for the unmasked baseline is hanoi.py's own: an illegal move leaves every disk
in place and pays −1 (a no-op). The page says the environment, not the agent, sets that rule, and
that MaskablePPO never triggers it.

## Result checks (series prompt)

1. New seeds. `uv run compare.py 5` (seeds 5 to 9): PPO illegal share 0.29 to 0.35; PPO 10.0 to 12.5
   moves per episode; MaskablePPO with mask 9.9 to 10.0, with no mask 16.7 to 51.0; illegal
   probability PPO 0.02 to 0.06, MaskablePPO 0.28 to 0.34. Both conclusions hold. The no-mask range
   widens across ten seeds (17 to 63), so the page gives seeds 0 to 4's table and says seeds 5 to 9
   "end the same way" without their numbers.
2. One seed, one state. Fig. 1's case (illegal 1 → 0 most probable at the start) is seed 0's. From
   the start, seeds 0 and 3 have an illegal most probable move, seed 2 reaches one after 4 moves,
   seeds 1 and 4 finish (checks/analyze.py). The page states the start only for seed 0 and generalizes
   only through the five-seed columns.
3. Removal test, on the page: PPO trained without the mask is the flag (Table 1 and Table 2 columns
   from compare.py). A second removal check off the page: MaskablePPO with `learn(..., use_masking=False)`,
   seeds 0 and 1 (checks/trainsave2.py, analyze2.py): 14,650 and 15,796 illegal training moves
   (PPO: 14,510 and 15,794), illegal probability 0.026 and 0.033, no state with an illegal most
   probable move. Same as PPO, so the cause is the mask in training, not a code difference between
   the two classes.
4. Worst case for "training never scores an illegal move": train longer, where rising legal logits
   could squeeze illegal probability down without any illegal signal. MaskablePPO seeds 0 and 1 at
   151,552 steps: illegal probability 0.308 and 0.292 (0.303 and 0.348 at 51,200); states with an
   illegal most probable move 18 and 15 (10 and 20 before). The explanation holds. Side finding, not
   on the page: seed 0 at 151,552 steps ends on a masked greedy policy that reaches the goal from no
   start (seed 1 is fine). Unexplained PPO instability at long budgets; the page only trains 50,000.
5. Untrained networks (seeds 0 to 4) give illegal moves 0.504 of their probability, the uniform
   value, with an illegal most probable move in 37 to 50 of 80 states. Masked training lowers the
   illegal share to about 0.3 only by raising the legal moves it prefers. Not on the page: the reader
   check may ask why 0.3 and not 0.5; a sentence would need these numbers printed.
6. Problem 1's answer (unmasked sampling is rejection sampling from the masked policy): simulated at
   states 0, 1, 5 and 40 with 20,000 draws each, the first legal move's distribution matches the
   masked one within 0.005, and mean no-ops match q/(1−q) (2.385 against 2.363 at the start). SB3's
   evaluate_policy with deterministic=False on seed 0: 14.2 moves per episode, none cut
   (checks/check_eval.py).
7. "Neither warns": SB3's evaluate_policy on a Monitor-wrapped env and predict with no mask, under
   `warnings.simplefilter("always")`, emitted no warning (checks/check_eval.py). compare.py's
   `warn=False` only silences the missing-Monitor notice, and the listing says so.
8. The environment's rule never reaches MaskablePPO's training: a Hanoi subclass that ends the
   episode at −10 on an illegal move trains a bit-identical seed-0 network (largest probability
   difference 0.0, 0 illegal moves); SB3's evaluate_policy then ends 35 of 100 episodes on the
   illegal move (checks/check_rule.py). Supports the page's statement; not printed there.
9. The scripted recursion takes the fewest moves (BFS from leak.py) from all 80 starts
   (checks/check_scripted.py). The page claims only its 9.9 moves per episode.
10. Fig. 2 is drawn by checks/fig3.py from checks/figdata.py (seed 0's saved model, identical to
    maskable.py's run); its 10 squares and 33 filled starts match maskable.py's printed counts.
    Fig. 1's bars are maskable.py's printed probabilities. Both checked at 390 px and 1280 px, light
    and dark (Playwright with the system Chrome).

## Evidence notes

- Researcher contradictions: #1 and #2 are weighed in "Without a mask, PPO spends three training
  moves in ten on no-ops"; #4 (docs say MaskablePPO behaves like PPO without ActionMasker) is
  answered in "MaskablePPO asks for the mask before every move"; #5 does not apply (the page names
  only the callable form of ActionMasker); #6 is off the page (SubprocVecEnv is not discussed); #7 is
  respected (Table 2 numbers only); #8: the page says Huang and Ontañón "call" it invalid action
  masking and never says they introduced it; #9 (their mask covered two action components) is not on
  the page, because their masking rows reached 40 either way and the lesson uses them only to show
  a penalty failing on larger maps; #3 left the page with the cut masking-removed paragraph, and the
  Go deeper line points to those rows.
- No open evidence or voice question.
