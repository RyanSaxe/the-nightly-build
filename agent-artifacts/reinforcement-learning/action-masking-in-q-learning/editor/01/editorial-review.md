# Editorial review: reinforcement-learning/action-masking-in-q-learning (editor/01)

Editor model: claude-opus-5-5 (Opus 5.5), harness Claude Code. Scratch work is in
`/tmp/claude-0/-home-user-the-nightly-build/84eccc3f-e59d-500c-be1e-12104b5380af/scratchpad/rl-editor/`.

## Correct

Thesis, from the draft alone: when legality depends on the state, Q-learning has to
mask the max in its target as well as its choice, because a move it never makes keeps
its initial estimate and a max over all actions still reads that estimate. The claims
under it:

1. On the four-disk puzzle, masking both places learns q* (0.08 mean error) and the
   greedy agent takes the fewest moves. Masking only the choice ends 2.45 from q*,
   puts every legal estimate nine or more moves out at −1, and loops beside the start.
2. The choice-only agent can rest only at the solution of the Bellman optimality
   equation for a puzzle where every state also offers an episode-ending move that pays
   Q0. That equation has one solution, and it matches v* out to eight moves and is −1
   beyond.
3. Starting every estimate at −1/(1 − γ) = −10 removes the effect. The two targets
   then give identical tables.

How each held:

- Listings. I extracted `hanoi.py`, `masked_q.py` and `leak.py` from the HTML and ran
  them with `uv run`. Both printed outputs match byte for byte. leak.py takes 45 s.
- Seeds 5–14 (`seeds/myseeds.py`, my own script). Masked target: the start is solved
  in 15 moves in 10 of 10 runs, and seed 5 misses one start (state 52 takes 16 moves
  against 15). Target over all six: 0 of 10 runs solve the start, 29 starts in every
  run, every legal estimate nine or more moves out is exactly −1.0, the same loop
  0→1→7→6→7 every time, and the extra start is state 12. Random tie-breaks give 147.5
  on average, with single runs from 127 to 162. Init −10: the two targets' tables are
  identical in every seed. The conclusions stand. Two sentences generalized past the
  seeds, and I fixed both (Edits 7 and 9).
- Derivation, line by line. The Fig. 1 arithmetic holds against the computed q*:
  −5.42, −5.88 and −5.88, and −5.88 + 0.5 × 4.88 = −3.44. Every state has three or
  four illegal moves, and 240 of 486 pairs are legal. The equation's right side is
  max{Q0, ·}, which is non-expansive, so the γ contraction and its single solution
  hold. The eight-move argument was incomplete. It explained why the best move keeps
  its value but not why no other move overtakes it once Q0 lifts that move's target to
  −1. I rewrote the step and checked the fixed point directly (Edit 11). The −10
  argument holds by induction, since every target is at least −1 + 0.9 × (−10) and
  each update is a convex step. Problem 2's 54 states and Problem 1's −10 threshold
  are both correct.
- Figures. Fig. 1 matches the computed q*. I checked Fig. 2 point by point
  (`seeds/figcheck.py`). All 80 non-goal dots in each panel carry the largest legal
  estimate of run 0 for their own state, in the colour and opacity the legend gives.
  The 120 drawn lines are exactly the legal-move graph. Each thick line is that run's
  greedy path, and the loop edge 7↔6 is the right one.
- Breaks I fixed:
  - "In every run … all 80 starts" did not survive seed 5. It now covers the five
    printed runs, and one sentence reports the new seeds.
  - "149 moves" carried more precision than repeats across seeds. It now reads "about
    150".
  - "An agent that masks both places never makes such a move" was wrong about the
    cause. Masking the choice alone prevents the move, and the choice-only agent never
    makes one either.
  - "The DQN agents in OpenSpiel" claimed more than the record holds, which is
    OpenSpiel's PyTorch DQN only. I narrowed it in the body and in the Why card.
  - Problem 1's closing line, "A max over all actions goes wrong only when some of its
    estimates are never updated", stated a general law. The very next problem goes
    against it: every estimate is updated there, and the greedy agent still quits from
    54 states. I cut it.
- Citations. I opened every href as the page prints it. The six GitHub addresses
  (curl through this session's proxy returns 403 for repositories not attached, so I
  used WebFetch), the two Gymnasium docs pages, PettingZoo, JAIR and both arXiv pages
  all land on the cited file or page. Each cited passage says what the sentence uses
  it for:
  - taxi.py at v1.4.0 has the `action_mask` key, the int8 mask, the −10 no-ops and
    the snippet that masks only the choice.
  - sb3-contrib calls `action_masks` and reads no info.
  - check_env calls `sample()` with no mask.
  - Discrete.sample asserts int8.
  - PR #1812 was merged 2026-10-23. The main docstring now maps the index back and
    still says nothing about the target.
  - The 1.4.0 tutorial lists the three places and skips the update on terminal steps.
    Main's tutorial updates every step with (1 − terminated).
  - The OpenSpiel and HLE targets mask their max.
  - Zahavy's Definition 3 and Proposition 1 are on p. 6 and Algorithm 1 on p. 7.
    Huang and Ontañón's Table 2 is on p. 5.
- Sutton and Barto's printed address, https://incompleteideas.net/…, failed here. curl
  reported a self-signed certificate and WebFetch got a 503, while the record's http
  address returns the PDF. The point is moot, because the sentence citing it held only
  that citation and I cut it (Edit 2).
- Every `data-nb-kind` is primary, and each source is the owner's own code, docs or
  paper. The page claims no independent corroboration.
- Headline, dek and headings. "Four-disk", "more than eight moves", "stay at 0" and
  "−1" match the output. "Four of the start's six estimates" matches the mask
  [1,1,0,0,0,0].

No disagreement between the record and a source I opened.

## Reads well

What went:

- "One more detail comes from the environment checker." It said nothing. It
  announced the paragraph, which now opens on check_env itself.
- "Its estimates explain the loop." Same fault. The paragraph now opens on the −1
  ties.
- "Sutton and Barto write the set of actions available in state s as A(s)." It
  repeated the Why card's definition and existed to hold a citation, which the series
  direction rules out.
- "MaskablePPO, which a later lesson trains, …" in the Why card. It was a second
  MaskablePPO sentence, and the commission allows one. The one in the environment
  section stays because the decisions log needs it.
- Problem 1's closing law (see Correct). It was built to be quoted.

What I rewrote: "That is a rule a designer could give step for illegal moves in place
of the no-op, with Q0 as the reward for ending" followed the commission's own framing
of designer conventions. The point under it, that choice-only masking equals the
episode-ending convention, is the article's own, so I rewrote it in the article's words.

Against the recent record nothing repeats. The headline leads with the illegal moves,
not the method or a measured quantity, and the dek does not open with "On". The Why
card opens on the puzzle's rule, not on a designer's choice. The takeaway opens on the
measured result. No section is a "most of X's gain" ablation. "Called X" appears once
and "the gap" not at all.

The draft mostly sits in the guide's register: short sentences, the purpose before the
step, numbers from one move before the general equation. One place ran flatter than the
guide asks. The eight-move step stated its conclusion without the reason next to it,
and I lifted it into one bound plus one reason (Edit 11). Takeaway, with its last
sentence read alone: it is the prescription the lesson built, and it stays.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 and 1280 px,
light and dark. There is no horizontal scroll and the console shows no errors. Fig. 1
and Fig. 2 keep their labels clear of the arrows and the dots in both themes. On a
phone the two Fig. 2 panels stack and the legend stays under them. The two figures
carry the case. Fig. 1 shows one update read through both maxes, and Fig. 2 shows where
the values break and where the agent loops. I found nothing to add or cut.

Prose words on the rendered page come to 2,231 by the identity's rule. That count
includes the cards, captions, legends, problems and answers. It leaves out code, output,
equations, figure text, the reading bands, the sources, the headline and the dek. The
draft sat at 2,217. My edits removed about as much as they added, and the additions are
the seed caveat and the missing reason in the derivation. At about 1% over the guide I
cut no further idea.

What the page gives beyond its sources: the derivation, checked against the page's own
runs, shows that Q-learning masking only its choice solves the optimality equation of a
puzzle where every state also offers an episode-ending move worth the untouched initial
estimate. That predicts exactly which values break (nine or more moves out, at −1), and
it shows that starting at −1/(1 − γ) removes the break. The handoff's original-work
sentence says the same, and no source in the record measures or derives it. The
headline's claim, illegal moves never made still set the values, is what the output and
Fig. 2 show, and the dek states the condition.

## Edits

1. Why card: "MaskablePPO, which a later lesson trains, and the DQN agents in OpenSpiel read the same kind of mask." → "DeepMind's OpenSpiel library masks both places in its PyTorch DQN."
2. Orientation: cut "Sutton and Barto write the set of actions available in state s as A(s)." and its citation, removed source 1 (Sutton and Barto), and renumbered sources 2–11 to 1–10.
3. Environment: "so that learning reaches every pair" → "every legal pair".
4. Environment: cut "One more detail comes from the environment checker." The next sentence now reads "The environment checker, check_env, steps with random actions …" (link kept).
5. Environment: "An agent that masks both places never makes such a move" → "An agent that masks its choice never makes such a move".
6. Choice-only: "The DQN agents in OpenSpiel and in the Hanabi Learning Environment's fork of Dopamine mask the target's max too." → "OpenSpiel's PyTorch DQN and the DQN in the Hanabi Learning Environment's fork of Dopamine also mask the target's max."
7. Results: "In every run its greedy agent …" → "In all five runs its greedy agent …", plus the added sentence "Ten more seeds solve the start just as fast, though one of those runs takes a move too many from one other start."
8. Results: cut "Its estimates explain the loop."
9. Results: "needs 149 moves on average" → "needs about 150 moves on average".
10. Resting point: "That is a rule a designer could give step for illegal moves in place of the no-op, with Q0 as the reward for ending." → "A designer gets that puzzle by making step end the episode on an illegal move and pay Q0, in place of the no-op."
11. Resting point: rewrote the eight-move paragraph. The solution is now "grouped by" distance. The paragraph states the −1 lower bound that Q0 puts under every target short of the goal and says why the bound leaves values out to eight moves at v*. "Q0 wins every max" and "exactly −1" are added. The long sentence is split in two.
12. Resting point: "The run's estimates end 0.07 from this resting point." → "The five runs end 0.07 from this resting point on average."
13. Problem 1 answer: cut "A max over all actions goes wrong only when some of its estimates are never updated."
14. Takeaway: "Q-learning that masked only its choice settled at −1 in every state nine or more moves from the goal and looped beside the start." → "… settled every legal estimate nine or more moves from the goal at −1, and its greedy agent looped beside the start."
15. Ran `nb stamp`: words 4404, sources 10, 19 min.

Proof after the last edit (links on): BLOCK 0, WARN 2. Both warnings are W-CITE-DENSITY,
on `resting-point` and now also on `orientation`. With Edit 2 gone, `orientation`
consists of the puzzle's rules and the worked update of the page's own numbers. The
series direction says a section made of derivation or printed runs needs no citation,
so both warnings stand. The code listings and printed outputs are unchanged by these
edits, and I compared the re-extracted files to confirm.

## Decision

approve. The argument is right and its derivation checks against the page's own runs,
and every change it needed was an edit I could make from the record and this checkout.
