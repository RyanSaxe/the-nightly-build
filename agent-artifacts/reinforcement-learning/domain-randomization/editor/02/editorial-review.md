# Editorial review: reinforcement-learning/domain-randomization (editor/02)

This round answers the first reader check.

## Correct

The main-idea sentence in the handoff reads: "When a physical parameter drawn
each episode is hidden, the best policy is one policy for the whole range, which
loses return wherever the best move depends on the parameter." The reader's
restatement gets the first half right: one move per observation, the averaged
Dock, its optimum as the best a mass-blind policy can do, the 0.22 s at 1 kg,
and Q-learning landing there through equation (4) with shares fixed at ¼. The
restatement leaves out the condition, that the cost falls only where the best
move depends on the mass. The reader reads the cost as a fact about the
heaviest load, and place 4 shows why: the page offered the `--no-limit` run as
evidence for the condition, and that run cannot carry it. That is a mismatch,
so the page changed in two places. The removal-test paragraph now says what the
run shows and what it cannot. The averaged-dock section now states the
condition as derived: the cost is zero at every load exactly when one policy is
optimal for each. "Exactly when" holds in both directions. If an averaged
optimum lost return at some load, its average would fall short of the
right-hand term.

Each place, worst first, and what I did:

1. **No discount, and no argument that the solution is unique.** The page cited
   the SARSA and Q-learning lesson's contraction by γ, which does not hold at
   γ = 1. I cut that citation from the Q-learning section. In the averaged-dock
   section I added one paragraph with the argument that does hold here. In any
   solution of the Bellman optimality equation, each value equals its best
   move's reward plus the next value. Every decision costs 0.1 s, so values
   rise by 0.1 along best moves. Those moves therefore never revisit a state
   and must end the episode, which makes each value one path's return. The
   equation also puts each value at or above every finished path's return, so
   only the optimal values solve it. The argument uses only the page's own
   rules. To check that exact.py's sweeps actually reach that solution, I
   reran its solve off the page with a stop-when-unchanged test. From the
   x = 0.2 start the values stop changing after 25 to 27 sweeps, and from
   (0.8, 1.0) after 3 or 4. V at the start equals each greedy return the page
   prints. The page states this as "Its values stop changing long before the
   500th sweep", without the numbers, as the series prompt allows for checks.
   The page now also gives the reason for dropping the discount: every cost
   reads in seconds. Value iteration is linked at first use to "Two
   improvements find the best policy" and added to the Background band, and
   band 04 now says its argument used the discount.
2. **Held-out masses that aren't held out in the earlier lesson's sense.** Cut.
   The reader is right. 5 kg and 6 kg lie outside the training range, so they
   test extrapolation, not the in-distribution question the held-out levels
   lesson asked. The limit column also predicts the result before anything
   runs. I removed the 5 and 6 kg rows, `TESTS` and `--masses` from exact.py,
   the paragraph, the takeaway's sentence on it, and the held-out half of
   Fig. 2, which I redrew for 1 to 4 kg. The commission asked for a connection
   to held-out levels. It survives in the card and in the bound's middle term,
   which is the substantive link, but the page no longer has a held-out-range
   test.
3. **"Best for all" in two senses.** Rephrased both. One is now "the policy of
   (x, v) with the best return averaged over the four loads". The other is
   "exactly when a single policy is optimal for each load separately".
4. **The `--no-limit` run can only come out one way.** Kept, as the commission
   and the brief require. The paragraph now says plainly that the rule is the
   mass's only effect, so the run could come out no other way. It confirms
   that nothing else in the code makes the loads pay. It cannot show that a
   mass changing the reward but not the best move costs nothing, because
   removing the rule removes both. That case rests on the derivation. I cut
   "Without the rule, LoadedDock's mass changes nothing at all" and the
   opening sentence that restated the section heading.
5. **What randomization buys is never shown.** Added two sentences from
   exact.py's speed and limit columns. The 1 kg load's own policy arrives at
   0.91 m/s, above every heavier load's limit, so a light guess would crash the
   other three loads, while the averaged policy docks all four. "Light guess" is
   deliberate. A 4 kg guess is the averaged policy here, so "any single guess
   is worse" would be false. The card's motivation is tightened, and the
   takeaway carries one clause of this.
6. **Why the observation is exact integers.** Added: the integers survive the
   `int()` that qlearn.py's `key()` applies, so the table gets one entry per
   (x, v) with nothing behind it but the load.
7. **Skipped steps at the parting state.** The parting-state paragraph is
   rewritten. A push leaves the cart at 1 m/s with 0.3 m to go, and braking
   would need 0.33 m to reach the 3 kg limit. I checked this against the rules:
   (1 − 1/3)/2 m. So the 3 kg and 4 kg loads crash, in half of all episodes, a
   cost of 1 on average. "Goes on braking" became "following the 4 kg load's
   path", and the weighing now covers all four loads. The 2 kg and 3 kg losses
   are the 0.14 s and 0.08 s that exact.py prints.
8. **Wording and labels.**
   - The second definition of domain randomization is cut. Tobin is now
     credited with naming it.
   - "Is called sim-to-real transfer" became "transferred the policy from
     simulation to the real arm". That keeps the commission's mention-only
     clause with Peng as the pointer, and the term stays in the Go deeper
     titles.
   - "Right/left" became "push/brake", with "brakes by pushing left" at first
     use.
   - exact.py's ambiguous column header "arrives" is now "speed".
   - Fig. 3's caption says "darker bar". I did not name the colors, because
     every bar carries a brake or push label and the colors already match
     Figs. 1 and 2.
   - The cut-off line: train.py's label is now 73 characters. At 1280 px no
     output block overflows. At 390 px every code block scrolls sideways, as
     all listings do.

The sections the reader could skip:

- **History paragraph:** kept, shortened. The commission requires the Tobin
  citation and the sim-to-real mention.
- **loads.py listing:** kept, because exact.py and train.py import it and the
  series prompt requires every needed file to be printed. Its caption now says
  what passing the checker establishes: the API, not the cart's rules. The
  evidence record's check_env entry supports that.
- **`--no-limit`:** kept (see 4).
- **5 to 6 kg:** cut (see 2).
- **Mass-observed half of train.py:** kept. It is the commission's "exposing
  the parameter" demonstration made by a learner, and Fig. 3 contrasts one
  entry for all loads with one entry per load.

Results reported without saying what they mean:

- **check_env:** answered in the caption.
- **The 3 kg-path sentence:** cut. The parting-state paragraph now carries the
  four-load weighing.
- **1.96 and 1.91:** gone with the held-out rows.
- **The push-estimate gaps:** I cut the stated cause ("the agents push there
  only when they explore"). The reader's 3 kg counterexample breaks it, and no
  existing run tests it. The page now says the two gaps run in opposite
  directions (hidden low, 4 kg high), that these runs don't show why, and that
  neither changes which move is greedy. That last point is true in every run:
  every run's ranking matches exact.py. The commission's decisions allow
  stating the gap without a cause.

Reruns: I changed exact.py (`TESTS` and `--masses` removed, header "speed",
docstring) and train.py (imports, exact values over `MASSES`, shorter label).
I then reran `uv run loads.py`, `uv run exact.py`, `uv run exact.py
--no-limit`, `uv run exact.py --start 0.8 1.0` and `uv run train.py`. train.py
took 4 min 18 s, so "about four minutes" stands. Every number is identical to
round 1. The listings on the page are byte-identical to the files that
produced the printed output, which I confirmed by extracting them again and
rerunning. The `--start 0.8 1.0` rows still match Problem 1's answer. I
started no new experiment.

## Reads well

What went, and why:

- "Drawing a physical parameter like this mass at every reset is called domain
  randomization." It repeated the card's definition.
- "Moving a policy from simulation to a robot is called sim-to-real
  transfer." It defined a term the body never used again.
- The 3 kg-path sentence. It is a second, unexplained version of the
  parting-state weighing.
- "Without the rule, LoadedDock's mass changes nothing at all." It closed the
  paragraph on a line that dressed up a run that could come out only one way.
- "The buffer's rule is what makes the best braking point depend on the
  mass." It restated the heading.
- The held-out paragraph. Its comparison was false (see 2).

None of these came from the briefing files or the voice guide's quoted
passages. The new text keeps to one or two clauses a sentence. A 41-word
sentence in the parting-state paragraph raised W-SENTENCE-DENSITY, and I split
it.

## The experience

Prose counted on the rendered page as the template defines it: 2,203 words
without the section headings, 2,250 with them (47). The card is 134 words and
the takeaway 104. Before the cuts the reader's places would have added about
230 words. Cutting the held-out result and the sentences above brought it back
to the template's line.

At 390 px and 1280 px, in light and dark, nothing scrolls the page sideways.
The redrawn Fig. 2 (1 to 4 kg) has its legend clear of the limit curve and its
cost labels clear of the markers. Fig. 1 and Fig. 3 are unchanged from round
1. train.py's output fits its block at desktop width.

The page now pays for its derivation at the point where the reader lost it.
It also says what randomization buys as well as what it costs, and it no longer
claims evidence from a run that could not have gone otherwise. What it gives
beyond its sources is unchanged: an exact case where the best blind policy is
one averaged MDP, the loads that pay and why, and Q-learning landing on it.

## Edits

- Background band 02: "and held-out tests, here applied to masses" became "here applied to loads".
- Background band 04: now notes that its argument used the discount.
- Background band: added 05, "Two improvements find the best policy" (value iteration).
- Why this matters: motivation tightened to "a policy tuned to one guess can fail at the real value".
- Why this matters: "the middle term of that lesson's bound"; last sentence trimmed.
- Orientation P2: reason for dropping the discount ("so that every cost below reads in seconds").
- Orientation P3: "brakes by pushing left"; "best move there is to push… is to brake".
- Orientation, parting-state paragraph: rewritten with the 0.3 m and 0.33 m step, the four-load weighing, and the 4 kg path.
- Orientation, history paragraph: cut the repeated definition and the sim-to-real definition; Tobin "named" domain randomization; Peng "transferred the policy from simulation to the real arm".
- Orientation, loads.py paragraph: added why the observation is two integers (`int()` in `key()`, one entry per (x, v)).
- loads.py caption: added what passing the environment checker establishes.
- Averaged-dock P2: "the policy of (x, v) with the best return averaged over the four loads"; value iteration linked to its lesson.
- Averaged-dock: new paragraph on why the undiscounted Bellman optimality equation has one solution here.
- Averaged-dock: "That policy's return" became "The averaged Dock's best return".
- Averaged-dock P4: "exactly when a single policy is optimal for each load separately"; round 1's memory sentences cut for length (the card's narrowing stands).
- Averaged-dock, exact.py paragraph: "plays each greedy policy with every load"; "Its values stop changing long before the 500th sweep."
- exact.py: removed `TESTS`, `--masses` and the held-out marker; "arrives" header became "speed"; docstring updated.
- exact.py outputs (default and `--no-limit`): replaced with the rerun, 1 to 4 kg.
- Who-pays P1: cut the 3 kg-path sentence.
- Fig. 2: redrawn for 1 to 4 kg; new aria-label; caption reworded.
- Who-pays, removal paragraph: rewritten to say what the run shows and what it does not.
- Who-pays: the held-out paragraph replaced by the light-guess paragraph.
- Q-learning P2: cut the γ-based support; "can rest only at the averaged Dock's optimal action values, the equation's one solution".
- Q-learning results paragraph: the push-estimate gaps are stated without a cause, with their directions and "Neither gap changes which move is greedy".
- Fig. 3 caption: "solid" became "darker".
- train.py: imports and exact values over `MASSES`; output label shortened to fit; output replaced with the rerun.
- Takeaway: dropped the held-out sentence and "without the rule nothing was lost"; added the 1 kg-guess clause.
- Ran `nb stamp` (words=4464, reading_minutes=19, sources=5).
- Proof: BLOCK: 0, WARN: 3, the three W-CITE-DENSITY warnings on derivation and run sections, which the series prompt allows.

## Decision

approve. Every place the reader raised is either answered on the page from the
existing runs and the page's own rules, or cut, and nothing publication-blocking
remains. One caution for the orchestrator: the no-discount paragraph replaces a
step of the central derivation, and no reader has seen it yet.
