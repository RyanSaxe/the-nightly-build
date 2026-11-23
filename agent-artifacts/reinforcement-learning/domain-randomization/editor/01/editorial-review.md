# Editorial review: reinforcement-learning/domain-randomization (editor/01)

## Correct

Thesis, from the draft alone: when a parameter drawn at every reset is left out
of the observation, one policy has to serve the whole range, and it gives up
return at a value only where the best move depends on the parameter. Three
claims carry it.

1. In LoadedDock the load changes only the reward of the move that docks, so a
   policy's return averaged over loads equals its return in one averaged Dock,
   and that Dock's optimal policy is the best policy of (x, v). The derivation
   holds. The paths a policy produces do not depend on the mass, and the rewards
   before the dock do not either. That also makes the equality hold for a
   policy with memory, which the draft never said (see the break below).
2. From rest at x = 0.2 the averaged policy follows the 4 kg path. Hiding the
   mass costs 0.22, 0.14, 0.08 and 0.00 s for 1 to 4 kg, the buffer rule
   causes all of it, and the policy crashes the held-out 5 and 6 kg loads. I
   reran `uv run loads.py`, `uv run exact.py` and `uv run exact.py --no-limit`
   from the listings as printed, with dock.py and qlearn.py. All three outputs
   match the page byte for byte. Fig. 1 and Fig. 2 match exact.py point by
   point. I checked the 9-push parting state (0.605 m, 0.9 m/s), the 0.3 m
   braking argument (0.375 m needed), the 4 kg push 11.5 cm from the dock, the
   −1 averaged penalty at 0.63 m/s, and the 3 kg-path alternative (−1.93
   against −1.51) by hand. I reran handoff checks 4, 6 and 7
   (`--start 0.9 0`, `--start 0.8 1.0`, `--masses 1 2 3 4 5 6`,
   `--masses 1 2`) and they print what the handoff records. Problem 1's answer
   (0.77 m/s, only 1 kg savable, 0.03 s on each doomed load) matches
   `--start 0.8 1.0`.
3. Q-learning with the mass hidden settles on the averaged Dock's policy, and
   with the mass observed on each load's own policy. `uv run train.py` as
   printed reproduced the page's output exactly in 4 min 0 s. As a seed check I
   ran runs 20-29, which neither the writer nor the page used. Every greedy
   return is identical. The hidden push estimate is −1.50 and the 4 kg push
   estimate −2.27, both within the page's "up to 0.09" of exact.py, and every
   run ranks the moves as exact.py does. Fig. 3's bars match the output.

dock.py and qlearn.py in scratch match the listings in
`nb history --show` for action-frequency and frame-stacking-and-the-markov-property,
apart from whitespace before comments, which the history text collapses.
Equation (4), Pitch's ε-set shares, and the held-out-levels bound are what the
page says those lessons taught.

Breaks and fixes:

- Why this matters said that with the parameter hidden "the best the agent can
  do" is one policy for the range. The bound it cites covers policies of the
  current observation. Evidence (Peng §IV.D; Chen §4.2 and after Theorem 2)
  shows memory can recover a parameter that changes the dynamics, and Go deeper
  points readers to Chen on exactly that. I narrowed the card to "a policy that
  acts on it". I added one sentence to the averaged-dock section saying memory
  can't stand in for m here, because every load follows the same path. A
  second sentence says that where the load changes the motion a remembered path
  can reveal it, and points forward to the recurrent-policy lesson. The
  commission's boundaries allow that one pointer. This narrows the claim to
  what the derivation supports. It does not hide a gap in the reporting.
- The paragraph after Fig. 3 explained the hidden push value (−1.51) by saying
  that after a push the 3 kg and 4 kg loads crash. They crash after a push
  under their own policies too. The averaged value is lower because the single
  policy brakes after the push, so the doomed loads crash later than their own
  best and the 1 kg load docks later. The explanation was incomplete. The main
  idea does not need it, and the page sits at the word cap, so I cut the
  paragraph rather than extend it.
- Problem 2's answer said "no averaged Dock gives the best policy". That is
  stronger than the argument shows. It now says the argument for the averaged
  Dock fails.
- "Here the policy is safe only up to the heaviest load it was built from" now
  carries "Here". From (0.9, 0) the averaged policy docks the held-out 5 kg
  load, so the statement holds for this start and not in general.
- "Following the 3 kg load's path would dock every load 0.08 s sooner and crash
  the 4 kg load" contradicted itself. It now says "bring every load in".

Citations: all six arXiv hrefs and the Gymnasium /v1.4.0/ Env.reset address
open on the cited documents. The Env.reset anchor exists, and its text supports
the seeding sentence. All five sources are correctly marked primary. Each is
the authors' own paper or Farama's own documentation, and the body credits
Tobin only with the name and a detector, as the commission requires. The Go
deeper descriptions match the evidence record's locators. The headline, dek and
headings carry no title, role or date. Every quantity in them (1 kg, 4 kg,
0.22 s) matches exact.py.

## Reads well

What went:

- "No load's own value for the push", with the rest of the paragraph after
  Fig. 3. The explanation was incomplete (above) and outside the main idea.
- "The agent that sees the mass keeps each load's own values." It repeated the
  previous paragraph and Fig. 3, and said nothing new at a paragraph's end.
- The four-cost sentence in who-pays ("It is 0.22 s for the 1 kg load,
  0.14 s for 2 kg…"). It restated the printed output and Fig. 2. The prose now
  gives the range's two ends, per the template's "use few numbers".

Nothing came from the briefing files or the voice guide's quoted passages.
I read the commission's idea and decision sentences against the card, the
takeaway and the derivation paragraphs, and found no clause lifted from them.

Against the recent record: the headline leads with the policy's finding and not
the learner, as the commission's note asks. Three of the last twelve headlines
open "A …", which is a common shape and not a template. The old dek's second half
("braking for a 4 kg load the agent can't rule out") restated the headline.
I rewrote it to carry what the headline leaves out, the cause shown by the
removal test. It has none of the ", while" or ", and" joins that the last four
deks used. The card opens on the simulator and not on an agent in a grid, and
the takeaway opens on the general statement and not on a measured number.
Three-in-a-row "The X's Y" headings: none.

Lifted or tightened:

- Why this matters stated a solution before its problem ("so one answer is").
  It now says a policy tuned to one guess can fail with another. Its last
  sentence listed what "the lesson" does. Now it says what the reader does,
  as the template asks.
- "as ε moved Pitch's" needed a reminder for anyone who has forgotten the
  frame-stacking lesson. It now reads "as ε moved the slow balls' share in
  Pitch", which also makes Problem 2's "as in Pitch" readable.
- The opposite-pushes paragraph switched between "the 4 kg cart" and "the 4 kg
  load" for the same thing. It now uses "load" throughout, as the rest of the
  page does.
- "Every run … docks each load at its own best return" became "earns each
  load's own best return".
- The takeaway's "because every load visits the same states as often" did not
  say as often as what. It now reads "because the load never changes which
  states the cart visits". Two comma-and joins became separate sentences.

The register matches the voice guide. The prose says what each step is for
before taking it, sentences are short, and it carries no borrowed phrasing.

## The experience

Prose counted on the rendered page as the template defines it: 2,164 words
without the section headings, 2,211 with them (47). The card is 150 words and
the takeaway 111. That is at the template's line. My edits cut slightly more
than they added.

At 390 px and 1280 px, in light and dark, nothing scrolls sideways. Fig. 1's and
Fig. 2's labels clear their marks. Fig. 2's legend sits close to the limit
curve but does not touch it. In Fig. 3, brake was drawn in --chart-1 and push in
--chart-2, the reverse of Fig. 1 and Fig. 2. In Fig. 1 the 1 kg path that keeps
pushing at the parting state is --chart-1 and the 4 kg path that brakes is
--chart-2. In Fig. 2 the averaged policy, which brakes, is --chart-2. I swapped
Fig. 3's colors, so pushing and braking keep one color across all three
figures. The captions are factual labels. No component needed adding. The three
figures and three equation blocks each show something the prose would take a
paragraph to say.

The piece is weighted toward the setup and the derivation, which is where the
idea lives, and the run section is now shorter. It ends on the problems, then
the takeaway.

What it gives beyond its sources: the papers measure a hidden parameter's cost
only with trained deep-RL policies, which mix that cost with optimization
error. This lesson builds a case where the best blind policy is exactly one
averaged MDP. It solves which loads pay and why, shows that the buffer rule
causes all of the cost, and shows that Q-learning lands on the same policy.
The writer's original-work sentence says the same, so it stands.

Headline, reread last: "A cart that can't see its load brakes for the heaviest
one" is the page's largest claim. It holds for the training range from the
lesson's start state. Problem 1 shows the start where it fails, which is honest.

## Edits

- Dek (visible and nb-meta) rewritten: "Domain randomization over Dock's load costs the 1 kg cart 0.22 s, all of it from a dock buffer that stops heavier loads only at lower speeds."
- Why this matters: added the problem ("a policy tuned to one guess can fail with another").
- Why this matters: narrowed "the best the agent can do" to a policy that acts on the observation.
- Why this matters: spelled out "the bound from the held-out levels lesson".
- Why this matters: the last sentence now says what the reader does.
- Orientation, opposite-pushes paragraph: "cart" became "load" for the 1 kg and 4 kg cases, and a stray line wrap was fixed.
- Averaged-dock: added two sentences on why memory can't stand in for m here and where it could, pointing to a later lesson.
- Who-pays: replaced the four-cost sentence with "from nothing at 4 kg to 0.22 s at 1 kg".
- Who-pays: "dock every load 0.08 s sooner" became "bring every load in 0.08 s sooner".
- Who-pays: added "Here" to "the policy is safe only up to the heaviest load it was built from".
- Q-learning: "as ε moved Pitch's" became "as ε moved the slow balls' share in Pitch".
- Q-learning: "docks each load at its own best return" became "earns each load's own best return".
- Q-learning: cut the paragraph after Fig. 3 on the hidden push value.
- Fig. 3: swapped --chart-1 and --chart-2 so brake and push colors match Figs. 1 and 2.
- Problem 2 answer: "no averaged Dock gives the best policy" became "the argument for the averaged Dock fails".
- Takeaway: "so that policy is exactly the optimum" became "so the best such policy is the optimum".
- Takeaway: "because every load visits the same states as often" became "because the load never changes which states the cart visits".
- Takeaway: split the two comma-and sentences, and named the averaged policy as what crashes the heavier loads.
- Ran `nb stamp` (words=4529, reading_minutes=20, sources=5).
- Proof: BLOCK: 0, WARN: 3. The warnings are the three W-CITE-DENSITY on derivation and run sections, which the series prompt allows.

## Decision

approve. Every claim reproduces from the printed listings and fresh seeds, and
the edits above fixed every break without changing the argument.
