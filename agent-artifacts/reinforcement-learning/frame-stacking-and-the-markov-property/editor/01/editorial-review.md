# Editorial review: reinforcement-learning/frame-stacking-and-the-markov-property (editor/01)

## Correct

Thesis, from the draft alone: a table keyed on an observation that hides part of
the state gives one entry to several hidden states, Q-learning's entry rests at
the visit-weighted average of their targets, and stacking frames that fix the
hidden part restores the Markov property. Four claims carry it.

1. Pitch's cell is not Markov at cell 2. A slow ball from cell 3 and a fast
   ball from cell 4 both show 2 and need opposite moves. Held: checked against
   pitch.py's step rule.
2. Q-learning's one-frame entries rest at Singh, Jaakkola and Jordan's equation
   (4), with visit shares as weights. Held. I reopened the paper (PDF pp. 4–5).
   The page's equation matches their (4) term for term. P(s | X, a) reduces to
   the page's w(s | X) because the policy depends only on X, and the page now
   says why π(a | X) cancels. The caption's convergence attribution matches
   Theorem 2's conditions: a fixed stationary policy that tries every action,
   with non-increasing step sizes, which N^-0.7 satisfies. Recomputed 2/3, 0.6383
   at ε = 0.1, 7/9 and 0.7649 at cell 3, and the 0.551 crossing. All match the
   printed eq. 4 columns and Fig. 3.
3. Exploration moves the cell-2 entry and flips the move past ε = 0.55. Held
   against the five-rate output, which I reran.
4. Two Gymnasium frames give optimal values at every ε, with padding made
   harmless by the starts. Held. The output reruns byte for byte, and the
   padding behaviour matches the Gymnasium 1.4.0 documentation's own examples.

Breaks and fixes:

- **A changing ε-greedy policy.** The draft said the proof needs a fixed policy
  "so for Pitch the runs show what happens", and closed the exploration section
  with "An agent that lowers ε as it trains therefore moves the shares on its
  aliased entries while it learns them." No run backs the second sentence. I cut
  it. The first was looser than the runs: in Pitch a swing from cell 3 up
  always misses, so ties break to a wait and the greedy move there never
  changes. The shares at cells 2 and 3 are therefore set by ε alone from the
  first episode. A throwaway check counted greedy swings at cells 3 and up
  across 20 runs at ε = 0.1, 0.5 and 0.9, for one and two frames, and found
  none. The greedy move at cell 2 does flip during learning, but only cell 1's
  visits depend on it, and every ball at cell 1 wants a swing. The page now
  says the runs test equation (4) at shares that ε alone sets. That narrows
  the claim to what the runs show, and nothing in the reporting was thin
  there. The runs.py docstring for `exact` now notes that cell 1's weights skip
  the cell-2 move and why that is harmless.
- **Cell 3 and its removal flag.** The draft compared the 0.76 entry with
  "any average of the balls' values under those arrows", after a Monte Carlo
  sentence about values "under the policy". Under ε = 0.1 an on-policy Monte
  Carlo estimate would sit near 0.92, not 1. The comparison only holds for the
  greedy moves, so the page now says that directly. A wait at cell 3 is worth
  1 to every ball under the greedy moves that follow it, and the entry is 0.76
  because a slow ball's target is cell 2's 0.64, which counts fast balls that
  never pass cell 3. The removal flag `--starts 5 7 9` takes those fast balls
  out of cell 2. It also drops the slow balls from cells 4, 6 and 8, which are
  worth 1 at cell 3 either way, so nothing else the explanation uses changes.
  Equation (4) then predicts 1.00 exactly, and the run prints it. I added that cell 3 still holds both
  speeds under the flag. That rules out cell 3's own aliasing as the cause, so
  the flag tests the mechanism the prose names. The Monte Carlo sentence now
  cites equation (2) and footnote 2, which is where the Monte Carlo claim sits
  in the paper.
- **DQN in the card.** "DQN's network sees the last four Atari screens at once"
  said more than the record supports. Mnih et al. stack preprocessed frames,
  each the maximum over two emulator frames, with an action repeat of 4, and
  the record could not settle whether they are consecutive. The card now says
  "four most recent frames" and gives the authors' stated reason, cited to
  Methods, Preprocessing and Algorithm. The DQN coda in the body is gone (see
  Reads well). The velocity attribution to Hausknecht and Stone went with it,
  so the page makes no velocity claim about DQN.
- **Gymnasium's MultiDiscrete space** was cited to a documentation page that
  doesn't state it, and no printed output shows it. I cut the phrase.
- **SB3 citation.** The docs anchor doesn't say "zeros". The StackedObservations
  source page, one click from the anchor, shows `np.zeros` and the Box/Dict-only
  TypeError. The locator now names that page.
- **Locators.** I removed §16.5 p. 438 from Sutton and Barto, since the page no
  longer uses it. I added footnote 2 to Singh et al. and dropped the
  Fig. 1 caption from Mnih et al.

Headline, dek and headings check against the page. "Q-learning values a rolling
ball's cell by how often each speed reaches it" is what equation (4) says and
what cell 2's 0.64 and 0.36 show. The dek's "all 12 pitches at every
exploration rate tried" matches every two-frame block.

Every printed href, opened as printed:

- Springer (Whitehead and Ballard) lands on the article. The abstract names
  "Perceptual aliasing".
- Singh's site PDF, the DeepMind PDF, arXiv 1507.06527, the Gymnasium 1.4.0
  anchor and the SB3 2.9.2 anchor all land on the source, and the five course
  links resolve in the preview build.
- The RL Zoo GitHub file lands on v2.9.2's wrappers.py, with the masked indices
  the Go deeper row describes. This machine's proxy refuses github.com, so I
  read it through a fetch.
- **Source 3, https://incompleteideas.net/book/RLbook2020.pdf, fails for
  whoever clicks it.** The host serves a self-signed Dreamhost certificate
  (CN sni.dreamhost.com) that doesn't match the name, so a browser shows a
  certificate warning. The http address works and is printed in Go deeper
  row 02. `data-nb-note` renders nowhere on the page. B-SOURCES-FORM requires
  https, and no https host serves this PDF; I could not reach an archive copy.
  The published course carries the same pattern (semi-gradient-td). This needs
  the orchestrator or the press owner. It does not block this lesson more
  than it blocked those.

Kinds: all six sources are `primary` and each is cited for its own authors'
statement or code. The page claims no independent corroboration. Hausknecht
and Stone are no longer cited in the body, so I removed them from Sources and
renumbered by first appearance. They stay as a Go deeper link.

## Reads well

What went, and why:

- "An agent that lowers ε as it trains therefore moves the shares..." and "With
  the stack, the resting point is the optimal values at every rate tried." The
  first claimed past the runs, and the second repeated the sentence before it.
- "For an observation, the property reads as follows." This only introduced
  the equation that follows it.
- The paragraph after the Markov equation ("At cell 2 the left side, for a
  wait, splits..."). It restated in symbols the instance that the "Suppose"
  paragraph and the sentence before the equation already give.
- Fig. 2's second caption sentence, which interpreted the bars. The prose under
  the figure already says it.
- "Its reset takes options that fix the start..." The docstring and hit_rate
  show the same thing.
- The DQN and libraries section. A reader can explain the main idea without it,
  and it opened after the argument had ended. Its one teaching point, the
  authors' stated reason, moved into the card's DQN sentence. The SB3 sentence
  moved into the stacking section, where it now says that VecFrameStack can't
  wrap Pitch's Discrete cells and that its zero padding leaves the first stack
  aliased too. The time-awareness pointer went, and Go deeper row 04 still
  points to recurrent policies.
- "the first lesson" in the card. The template asks for references by idea,
  and pages show no lesson numbers.

Lifted or clarified:

- "greedy arrows" became "greedy moves" in prose, docstring and printed output.
  In a game about hitting a ball, "the agents' arrows hit every ball" reads
  literally.
- "Entry" meant both a row X and a pair (X, a). It now means the row, and
  "estimate" is the per-action number.
- "the dashed arrow the next move" became "where the ball goes next". "Move"
  is the agent's wait or swing everywhere else. Problem 2's "move's length"
  became how far the ball rolls, for the same reason.
- "Pitch's cell fails at cell 2" and "far starts cover the first" in the
  takeaway were rewritten. The takeaway now opens on the mechanism rather than
  restating the definition first, which the orchestrator's notes flag as the
  recent takeaway shape.
- "Every ball starts out of reach of a fast ball's first move" became a plain
  statement: cell 4 or farther, so not even a fast ball reaches cell 0 on the
  first step.
- The rules paragraph now defines a pitch. The draft used "12 pitches" from
  the dek on without saying a pitch is one start-and-speed pair.

Checked against the recent record. The headline uses "values", not the
keeps/sends/passes construction. The dek opens on its subject, not a
prepositional frame. The card makes no "you will be able to" promise and names
no later lesson. Neither problem opens with "Suppose", and no heading states a
run's verdict with a number. The headings stay distinct from each other and
from the last five lessons'. Nothing in the draft read as lifted from the
commission or from the voice guide's quoted passages.

## The experience

Rendered with `nb preview` and captured with Playwright at 390 and 1280 px, in
light and dark. The page doesn't scroll sideways, and no text overflows at
phone width. Each chart matches the printed output. Fig. 2's bars are the
ε = 0.1 means: 0.64/0.36 at cell 2, 1.00/0.00 at (3, 2) and 0.00/1.00 at
(4, 2). Fig. 3's dots, read back from SVG coordinates, are 0.64, 0.58, 0.52,
0.45, 0.40 for a wait and 0.36, 0.43, 0.48, 0.54, 0.62 for a swing, as printed.
Its lines reproduce `exact`, recomputed at 19 points, and its crossing marker
sits at 0.551. Fig. 1's speed-2 arrow ended outside the track, past cell 0. It
now ends at cell 0, where the ball arrives, to match the speed-1 arrow. Fig. 3
had 20 empty units under its axis title, and I trimmed them.

Prose on the rendered page, by the template's definition (cards, captions,
legend text, problems and answers; no code, output, equations, drawing text,
reading bands or sources): 2,011 words, or 2,094 with title, dek and headings.
The draft came to about 2,130 and 2,215 by the same count. The lesson now
ends on the ε result and the problems, not on a coda.

The page gives what neither Singh, Jaakkola and Jordan nor the library
documentation gives on its own. On a track a reader can hold in a table, it
computes the aliased fixed point by hand from visit counts, matches it to runs,
and shows that the exploration rate alone flips the learned move at ε = 0.55.
Two Gymnasium frames then remove the effect, and Pitch's starts handle the
first-step padding. That agrees with the handoff's original-work sentence, so
both survive.

## Edits

- nb-meta `model`: "Claude Opus 5.5" to "claude-opus-5-5", matching recent lessons; `harness` stays "Claude Code".
- Card: "the first lesson" to "so far asked of states"; frame stacking named in the sentence that defines it; DQN sentence rewritten to "four most recent frames" with the authors' stated reason and a citation.
- Background 04: "sets the weights" to "sets the shares".
- Pitch rules: defined a pitch as one of the 12 start-and-speed pairs.
- Fig. 1: speed-2 arrow now ends at cell 0; caption "the next move" to "where the ball goes next".
- Orientation: cut "For an observation, the property reads as follows." and the paragraph after the Markov equation.
- One-frame: cut the reset-options sentence; "Each entry's step size" to "Each estimate's step size"; "10 to 30 seconds" to "up to 30 seconds" (single-setting reruns took 12 to 27 s, and the five one-frame rates 47 s together).
- qlearn.py docstring: "Each entry's" to "Each estimate's".
- runs.py: `hit_rate` docstring and printed label "greedy arrows" to "greedy moves"; `exact` docstring notes cell 1's weights skip the cell-2 move harmlessly. runs.py is 100 lines.
- All six printed outputs updated for the new label; every listing rerun as printed, byte-identical.
- Averages heading: "averages the hidden states" to "averages over the hidden states".
- Derivation: "visits to an entry (X, a)" recast; said why π(a | X) cancels.
- Shares paragraph: replaced "so for Pitch the runs show what happens" with why Pitch's shares at cells 2 and 3 depend on ε alone, and what the runs therefore test.
- ε = 0.1 paragraph: "that cuts" to "the extra steps cut".
- Cell-3 paragraph rewritten: Singh et al.'s equation (2) against equation (4), the value under the greedy moves, cell 2's 0.64 as the slow ball's target, and the flag's result with cell 3 still holding both speeds; locator now cites footnote 2.
- Stacking: cut "as MultiDiscrete([10 10]) for Pitch"; "Library stacks" to "The library wrappers"; added VecFrameStack's Box/Dict restriction and its zero-padded first stack; rewrote the first-step sentence.
- Fig. 2 caption: cut the interpretive sentence.
- Exploration: cut the closing paragraph on lowering ε.
- Cut the "Frame stacks in DQN and in the libraries" section; the Problems note now ends the exploration section.
- Problem 1 answer: split the shared-stack sentence. Problem 2: "after each move" to "after each step"; the answer speaks of distances rolled.
- Takeaway rewritten from the mechanism to the result.
- Fig. 3: viewBox height 270 to 250.
- Sources: renumbered by first appearance (Mnih et al. now 1); Hausknecht and Stone removed from Sources (kept in Go deeper); locators updated for Sutton and Barto, Singh et al., Gymnasium, Mnih et al. and SB3.
- Reran `./nb stamp` and the proof.

## Decision

approve: the argument holds against Singh, Jaakkola and Jordan and against
every rerun, and the remaining href fault on source 3 belongs to the press's
https rule, not to this lesson's argument.
