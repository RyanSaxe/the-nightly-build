# Editorial review: reinforcement-learning/domain-randomization (editor/03)

This round answers the second and final reader check. Under the template, I
answered it only by cutting or correcting text. I reran the lesson's code and
started no new experiment.

## Correct

The reader's restatement now matches the main-idea sentence in full. It
includes the condition the first reader missed: the policy "only loses return
at states where the best move depends on the mass". Nothing about the central
explanation needed to change.

Each place, and what I did:

1. **The undiscounted Bellman paragraph, and whether value iteration
   converges.** I took the orchestrator's narrower option.
   - I dropped "value iteration finds it".
   - exact.py's `solve()` now sweeps until no value changes, instead of a
     fixed 500 times. The page states only what a run shows: the list of
     reachable states is finite, because building it ends, and `solve()`
     stops on every run, so its values solve the Bellman optimality equation.
   - I rewrote the uniqueness paragraph so every step it uses is on the page:
     - the SARSA and Q-learning lesson's argument needs γ, so it is gone;
     - in a solution, a value equals its best move's reward plus the next
       value;
     - every move that doesn't end the episode pays −0.1, so values rise
       strictly along best moves and never revisit a state;
     - among finitely many states those moves must end the episode, so each
       value is one finished path's return;
     - adding V(s) ≥ r + V(s′) along any other finished path bounds that
       path's return by the value;
     - the conclusion carries over to action values through
       Q(s, a) = r + V(s′).
   - "The cost of time takes its place" is cut. The paragraph now comes after
     the sentence on `solve()`, so it is clear what it is for, and the
     Q-learning section's "the equation's one solution" points back to it.
   - I changed the code, not the results. All four exact.py runs (default,
     `--no-limit`, `--start 0.8 1.0`) and train.py (4 min 18 s) print exactly
     what they printed before.
2. **The `--no-limit` paragraph.** I reduced it to what it supports. It now
   reads "As a check on the code", names the flag, says the rule is the mass's
   only effect, and gives the printed result: 1.26 s and no cost. The output
   block stays. The ambiguous "both" went with the cut sentences. The section
   heading "Only the buffer's rule makes the light loads pay" was true by
   construction, so it is now "The light loads pay for docking at the 4 kg
   load's speed". That is what the section shows, and it still matches its
   `who-pays` label.
3. **Why the blind policy brakes at (0.605, 0.9).** The comparison is now on
   the page:
   - pushing crashes the 3 kg and 4 kg loads, an expected cost of 1;
   - braking costs no load more than 0.22 s, because no load docks sooner
     than the 1 kg load's 1.29 s;
   - crashing only the 4 kg load still costs 0.5 on average.

   Both exceed 0.22 s, so the policy brakes for the heaviest load, and the next
   section's "follows the 4 kg load's own path" now follows from this. I checked
   the 0.5 case against exact.py's numbers. A policy that crashes only the 4 kg
   load can save that load at most 0.25 s (1.51 s against 1.26 s), so its net
   cost stays well above braking's.
4. **The blind agent's entry is not the average of the per-load entries.** I
   added a short paragraph after Fig. 3, as the orchestrator directed:
   - after either move the blind agent follows the averaged Dock's policy with
     every load, so its value for braking, −0.61, is the 4 kg load's;
   - each per-load entry follows that load's own best;
   - as the frame-stacking lesson (linked) found, equation (4) does not give
     the share-weighted average of the hidden states' values.

   This also answers the results item asking what −0.61 and −1.47 are.
5. **The two estimates that miss exact.py.** Corrected. They "have not reached
   exact.py's values in these runs". The sizes and directions are spelled out
   (0.04 too low for the blind agent, 0.09 too high for the 4 kg entry). The
   page says the runs don't show why, and that neither gap changes the greedy
   move. That squares with "can rest only at": these two estimates are not yet
   at rest. The reader asked why the 3 kg entry matches and the 4 kg entry
   doesn't. No existing run explains that, so the page gives no cause.
6. **"The 500th sweep".** Gone with the new stopping rule.
7. **Why 0.63 m/s.** I replaced it with 0.6 m/s. It is above the 3 kg and
   4 kg limits and below the 2 kg limit, so the −1 holds and nothing points
   ahead to the table.
8. **Why integer observations matter.** The page now says why: `key()`
   applies `int()`, which would cut a float position to 0 or 1.
9. **Minor wording.**
   - "At a value" became "at a value of the parameter".
   - Problem 2 now says "1 m/s² divided by the load's mass in kg", not
     "1/m m/s²".

Sections the reader could skip:

- **History paragraph:** kept, because the commission requires the Tobin
  citation and the sim-to-real mention. I moved it to the end of the first
  section, after loads.py's output, so it no longer sits between the reasoning
  and the code. It now names EPOpt and CAD2RL directly. The move put the
  Gymnasium citation first, so I renumbered the sources in order of first
  appearance: Gymnasium 1, Tobin 2, EPOpt 3, CAD2RL 4, Peng 5. I checked every
  marker against its source after renumbering.
- **loads.py material:** kept. The other listings import it, and the series
  prompt requires every needed file to be printed.
- **`--no-limit`:** reduced (see 2).
- **The light-guess paragraph:** cut as a separate paragraph. One sentence of
  it now sits in the who-pays opening, because it supports the card's claim
  that a single guess can fail. The takeaway's clause on it is cut.

Results reported without saying what they mean:

- **The push-estimate gaps:** corrected (see 5).
- **The 500 sweeps:** see 1.
- **The blind agent's exact values:** see 4.
- **`--no-limit`:** now framed as a check on the code, which is all it is.
- **Own-best speeds a little under each limit:** left as printed. The
  likely reason is that pushes change only every 0.1 s, but no existing run
  tests that, and the main idea does not use the gap. Under this round's rule,
  the page gives no unsupported cause.

## Reads well

Cuts for the prose band:

- the "as when that lesson held each push for ten steps" callback;
- the 4 kg path's "12 cm from the dock, so that it doesn't crawl" clause.
  Fig. 1 still shows that zigzag.

The rewritten paragraphs keep to one step a sentence. I added nothing in the
grammar of a finding that the page doesn't establish.

## The experience

Prose counted on the rendered page as the template defines it: 2,195 words
without the section headings, 2,245 with them (50). The card is 136 words and
the takeaway 98. That is inside the band.

At 390 px and 1280 px, in light and dark, nothing scrolls the page sideways.
No output block overflows at desktop width. Figs. 1 to 3 are unchanged from
round 2 and render cleanly.

The page now shows every step of its uniqueness argument. It says what the
removal test is: a check on the code. It explains why the blind agent's values
differ from the per-load values, and states its one unexplained gap as
unexplained.

## Edits

- Why this matters: "at a value of the parameter only where the best move depends on it".
- Orientation P2: cut the RepeatAction callback.
- Orientation P3: shortened the 4 kg path's last steps.
- Orientation, parting-state paragraph: the expected-cost comparison now covers pushing, braking and crashing only the 4 kg load.
- Orientation, loads.py paragraph: added why integers (`int()` in `key()`).
- Orientation: moved the history paragraph to the section's end and named EPOpt and CAD2RL.
- Sources renumbered in order of first appearance; all five markers relabelled.
- Averaged-dock P2: 0.63 m/s became 0.6 m/s; cut "and value iteration finds it".
- Averaged-dock: replaced the exact.py paragraph and the uniqueness paragraph with a paragraph on what `solve()` shows and a rewritten argument whose every step is on the page.
- exact.py: `solve()` now sweeps until no value changes; docstring updated.
- exact.py and train.py: reran all of them; outputs are identical to round 2.
- Who-pays heading: now "The light loads pay for docking at the 4 kg load's speed".
- Who-pays P1: added the 1 kg-only policy sentence.
- Who-pays: the removal paragraph cut to "As a check on the code…" plus its output.
- Who-pays: cut the light-guess paragraph.
- Q-learning results paragraph: the push-estimate gaps are restated as not yet reached, with sizes and directions, and no cause.
- Q-learning: added the paragraph after Fig. 3 on why the blind agent's entry isn't the per-load average, linking the frame-stacking lesson.
- Problem 2: "1 m/s² divided by the load's mass in kg".
- Takeaway: rephrased the buffer clause and cut the 1 kg-guess clause.
- Ran `nb stamp` (words=4467, reading_minutes=19, sources=5).
- Proof: BLOCK: 0, WARN: 3, the three W-CITE-DENSITY warnings on derivation and run sections, which the series prompt allows. The proof also passes with `--check-links`.

## Decision

approve. Every place in the final report is cut or corrected and recorded
above. The edits change no result and add no experiment.
