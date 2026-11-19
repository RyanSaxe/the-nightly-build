# Editorial review: reinforcement-learning/specification-gaming (editor/02)

**This response rewrites a whole section.** The last section, "Positive-reward
cycles in CoastRunners and on a bicycle", is now "A boat in CoastRunners
circled through targets that kept reappearing". Its bicycle, Ng and Sutton and
Barto paragraphs are gone, and it keeps one paragraph on CoastRunners plus the
problems. The central explanation is unchanged: the derivation, the window,
the runs and the removal test still argue the same thing. Several of its steps
now carry the justification the reader asked for, and one paragraph of the
Q-learning section is cut. A second reader check is due.

## Correct

The reader's restatement matches the main-idea sentence in draft-handoff.md. It
has value iteration and Q-learning maximizing the reward as written, the
repeatable checkpoint making the loop optimal, the window, Q-learning
reaching the same loop, the separate task measure and the pay-once removal.
Nothing on the page needs to change for the main idea to come across.

The places, worst first, and what I did with each:

(a) The time-limit paragraph after window.py. Cut. The reader is right that "The
discount alone weighs the loop against the finish" sits badly beside an
undiscounted score of 50 against 11, and the γ = 1 sentences changed nothing
about the race. The one fact the page needs is why Q-learning's estimates can
be graded against value iteration's q* when episodes are cut at 100 moves. It
now sits where TimeLimit first appears, in the Q-learning setup. The limit is a
truncation, so the target still bootstraps at the cut and aims at the same
values as value iteration. The handoff's limit check (10, 20 and 1000 moves
give the same greedy moves) supports this. The first body use of "discount" now
links environments-and-the-rl-problem, since the cut paragraph held the only
body link to it.

(b) The constant step size. Explained, because it breaks a rule
sarsa-and-q-learning taught, and the main result rests on runs that use it. The
convergence proof needs step sizes whose squares have a finite sum, which is
there to average out noise in the targets. The race's targets have none, since
moves and rewards are fixed and the max target ignores which move the behavior
policy picks. A constant 0.1 therefore lets the estimates settle, and the
0.000 errors in the first two rows show that it did.

(c) The Krakovna and Turner paragraph. Cut whole. The weaker-algorithm caveat
was already answered by grading every run against the exact solve, and
"Value iteration read the rules. A learning agent ... might find the finish
first" says why at the top of the section. The misspecification sentence
restated what the lesson shows directly. Turner keeps his pointer in Go deeper,
which the commission allows ("one sentence and a pointer if it helps"), and the
row now says what his argument is. The body's claim stays scoped to value
iteration and Q-learning, so it conflicts with no published position.

(d) The forward reference to the flag. Fixed in one sentence: the flag records
whether a checkpoint that pays only once has paid, and it stays 0 until the
last row of learn.py tests that checkpoint.

(e) The peak with no step behind it. The page now names the step: setting the
derivative of γ^(D−2)(1 − γ²) to zero gives γ² = (D − 2)/D. I checked
d/dγ(γ³ − γ⁵) = 3γ² − 5γ⁴ = 0 at γ² = 3/5, which matches window.py's 0.775.

(f) Restricting cell 2 to three options. Two sentences added. Policy iteration,
taught in finding-optimal-policies, searches only one-move-per-cell policies
and still ends at an optimal one, so comparing those is enough. A paying cycle
has to cross from cell 1 to cell 2 and get back to cell 1, and the only way
back is cell 2's own move, so with one move per cell the only paying cycle is
the two-move loop. I checked this against the race's rules: the only paying
moves are the 1→2 crossing and arriving in the terminal cell.

(g) Notation. The Fig. 2 caption now writes (F/r)γ^(D−2)(1 − γ²) with D = 5.
The takeaway keeps γ⁴F, because a reader repeating the result needs the
number, but it now says "from cell 2" and "for the finish five moves away", so
the exponent explains itself.

(h) The Popov comparison in Problem 1. Cut. Explaining the grasp reward would
take a paragraph about another system, and the problem stands without it. The
Popov source entry went with it.

Sections the reader could skip:

- "Positive-reward cycles in CoastRunners and on a bicycle". The bicycle,
  Ng's term and the Sutton and Barto paragraph are all cut, following the
  template's rule for a section the main idea doesn't need. I kept one
  CoastRunners paragraph, as the last section with the problems, for three
  reasons. The commission builds the case on it. It is the only place the page
  meets the published case it was modelled on. And its contrast carries the
  lesson's original work: DeepMind says the targets changed the optimal
  policy, OpenAI reports only scores, and the race is solved exactly. The
  bicycle and Lego facts survive only in the Go deeper row on the shared list.
- The Krakovna and Turner paragraph. Cut, see (c).
- window.py and its output. Kept. The series direction asks that a derivable
  idea be derived in full and checked with a run, and window.py is that check.
  Fig. 2's band edges come from its bisection.
- The Sutton and Barto chess paragraph. Cut with the section. The book remains
  in the Background band, reworded now that nothing on the page quotes it, and
  in Go deeper.

Results reported without saying what they mean:

- The third row's 0.116. The reader guessed the state is rarely visited. The
  rerun says otherwise. `code/checks/check_error_state.py` mirrors
  learn.q_learning with counters and asserts the same Q. The pair "back in
  cell 0 after the payment" is updated 2,143 to 9,548 times in the four runs
  where it holds the largest error, mostly early on, while the zero estimates
  make back the greedy tie-break. The greedy policy last chooses it in episode
  59 to 508, and after that only random moves update it, 11 to 50 times in the
  last 500 episodes. The greedy move there ends forward in every run. The page
  now says this without the counts: the greedy policy stopped choosing the move
  within a few hundred episodes, only random moves have updated it since, and
  the error changes no move.
- Fig. 1's non-monotone values. One sentence added: in both rows cell 1 is
  worth more than cells 0 and 2, because its forward move collects the
  checkpoint. I checked it against the printed values: 6.90 against 6.21 and
  6.56, and 50.25 against 49.75 and 49.75.
- Which states the 0.000 covers. learn.py's `live` holds cells 0 to 6 when the
  checkpoint pays every time, and adds the seven paid copies when it pays once.
  The text now says "in cells 0 to 6" for the first two rows and "This row also
  grades cells 0 to 6 after the payment" for the third.
- The headline's single threshold. Changed. "once the discount passes 0.94"
  read as one switch point, and the loop also wins below 0.514. The new
  headline, "Looping through a checkpoint worth 1 beats a finish worth 10 at a
  discount of 0.99", states the case the page solves, prints and learns. It
  implies no threshold, and every word holds. The window stays in the body and
  the takeaway.

Sources go from seven to two, the only ones still cited inline: DeepMind
(paragraphs 1 and 8) and OpenAI (paragraphs 3 to 5). Both are primary for
what they are cited for. DeepMind's locator now lists only the paragraphs the
page cites. Nothing new needed a source.

## Reads well

The deletions above were made because the reader could not say why the
sentences were there, or because the main idea stood without them, and not
for slop. I checked the additions against spec/slop.md. Each states something
checkable: a proof condition and why the race escapes it, a derivative, a
cycle argument, a value comparison, and where an error sits. None announces or
grades itself. The new heading, "A boat in CoastRunners circled through targets
that kept reappearing", is a clause in the piece's nouns and differs in shape
from the other three and from the recent record's "X never/still/only" form.
The new headline keeps subject, verb and surprise first and has no colon or
question. Its one number beyond 1 and 10 is the discount at which the page
solves, prints and learns the loop. The dek is unchanged.

## The experience

I rebuilt the page with nb preview and checked it with Playwright at 390 and
1280 px in light and dark. Nothing overflows the page; the only elements past
the edge are KaTeX's hidden MathML. Six of six inline math spans typeset with
no KaTeX errors. Both figures render as before, and the Fig. 2 caption's new
superscript sits cleanly at both widths. The contents list shows the four
headings in order. The new last section is one paragraph and the problems, so
the page ends sooner after the removal test, which is where its argument ends.

Prose on the rendered page comes to 2,029 words, down from 2,189, counted as in
editor/01: both cards, captions, the legend, problems and answers and
summaries in, and title, dek, code, output, equations, SVG text, reading bands
and sources out. That is under the ceiling. Stamp: 4,154 words, 18 minutes, 2
sources.

The page still gives what its sources don't. It derives and checks by value
iteration the discounts at which finishing beats a repeatable checkpoint, and
it shows that at 0.99 the looping policy is the optimum that a correctly
working Q-learner reaches.

## Edits

- Headline (title tag, nb-meta and h1): "once the discount passes 0.94" to "at a discount of 0.99".
- Background row 01: "value iteration, the Bellman optimality equation and the greedy policy" to "value iteration, policy iteration and the greedy policy".
- Background row 02: added "and the step sizes its convergence proof asks for".
- Background row 05: reworded to "on paying an agent for what it should achieve and not for how, with a chess agent paid for taking pieces that might take them and lose the game".
- Orientation: linked "discount" to environments-and-the-rl-problem.
- Orientation: added "In both rows cell 1 is worth more than cells 0 and 2, because its forward move collects the checkpoint."
- Orientation: "a flag that stays 0 until a test later in the lesson" to "a flag that records whether a checkpoint that pays only once has paid. The flag stays 0 until the last row of learn.py tests that checkpoint."
- Discount window: "The optimal policy picks one move per cell, as value iteration's greedy policy does, so from cell 2 it either loops" replaced by the policy-iteration sentence, the paying-cycle sentences, and "So from cell 2 a policy either loops".
- Discount window: "the left side peaks where γ² = (D − 2)/D, and the peak is 1.86" to "setting the derivative of γ^(D−2)(1 − γ²) to zero puts the left side's peak at γ² = (D − 2)/D, where it is 1.86".
- Fig. 2 caption: "(F/r)γ³(1 − γ²)" to "(F/r)γ^(D−2)(1 − γ²) with D = 5".
- Discount window: deleted the time-limit paragraph after window.py's output.
- Q-learning: added "The limit is a truncation, so the target still bootstraps at the cut and aims at the same values as value iteration", with "truncation" linked.
- Q-learning: replaced "The race has no randomness, so each target moves only as the estimates do, and a constant step size of 0.1 lets them settle" with a new paragraph on the step-size condition and why the race's targets escape it.
- Q-learning: "every run makes value iteration's move in every state, and its estimates end within 0.001" to "in cells 0 to 6, and its estimates there end within 0.001".
- Q-learning: deleted the Krakovna and Turner paragraph.
- Q-learning: the 0.116 sentence replaced by "This row also grades cells 0 to 6 after the payment. Its largest error, 0.116, is for moving back in cell 0 after the payment, a move the greedy policy stopped choosing within a few hundred episodes and only random moves have updated since. The error changes no move."
- Last section: id and label "published-cycles" to "coastrunners"; heading to "A boat in CoastRunners circled through targets that kept reappearing".
- Last section: deleted "and a high score was possible without finishing".
- Last section: deleted the bicycle and positive-reward-cycle paragraph.
- Last section: deleted the Sutton and Barto paragraph and the Ng pointer.
- Problem 1: deleted the Popov comparison.
- Takeaway: "worth γr/(1 − γ²), against γ⁴F for the finish" to "worth γr/(1 − γ²) from cell 2, against γ⁴F for the finish five moves away".
- Go deeper row 04: "gives the bicycle and a soccer robot as positive-reward cycles, and the rest derives the progress reward a later lesson builds" to "describes a bicycle and a soccer robot that cycled to collect their shaping rewards, and the rest derives a progress reward that leaves the optimal policy unchanged, which a later lesson builds".
- Go deeper row 05: added what Turner argues; "the deep RL agents his argument is about" to "the agents his argument is about".
- Go deeper row 06: "qualify the rule above" to "qualify Section 3.2's rule".
- Sources: removed Turner, Randløv and Alstrøm, Ng et al., Sutton and Barto, and Popov et al.; OpenAI renumbered from 3 to 2; DeepMind's locator narrowed to paragraphs 1 and 8.
- code/checks/check_error_state.py rewritten to count updates and the last greedy choice, asserting the same Q as learn.py; output in check_error_state.out.txt.
- Listings unchanged, rerun from the page as printed: race.py, window.py and learn.py match their printed outputs.
- Reran nb stamp: words 4154, reading_minutes 18, sources 2.

Proof after the last edit: BLOCK 0, WARN 2, PUBLISHABLE. Both warnings are
W-CITE-DENSITY, on discount-window and on q-learning. Each section now holds
only a derivation or the lesson's own runs, which the series direction exempts.

## Decision

approve: every place the reader raised is cut or explained from the reruns and
the record, and the writer has no required change. Because the last section
was rewritten, the template calls for a second reader check on this page.
