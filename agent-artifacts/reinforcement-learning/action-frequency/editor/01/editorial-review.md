# Editorial review: reinforcement-learning/action-frequency (editor/01)

## Correct

Thesis, from the draft alone: when a continuous-time system is controlled with decisions h
seconds long, two actions' values in one state differ by O(h), while Q-learning's estimation
error does not shrink with h, so at a fine step the error decides which action ranks first.
Holding each action for k steps widens the gap k-fold, and in Dock most of the improvement
comes from that wider gap.

Claims under it, and how each held:

1. **Q − V = O(dt), and Dock's gap is 2u·dt·∂V/∂v.** Held. I checked the derivation line by
   line: the substitution, γ = 1 − dt/τ + O(dt²), the cancellation of V/τ when two actions
   are subtracted, f = (v, ±u), and ∂V/∂v = e^(−T/τ)(1 − v/w)/u, which is e^(−1) at (0.5, 0)
   and gives 0.736·dt. gap.py reproduces it. Two fixes. "The bracket doesn't depend on dt" is
   not exact, because V is the value of the dt-step problem; Tallec et al. assume derivatives
   bounded uniformly in dt (evidence S1), so the page now says the bracket stays bounded. "The
   gap divided by h stays at 0.736 from dt = 0.1" contradicted the output, which prints 0.731
   at 0.1 and 0.735 at 0.03; the page now gives the range against the derived 0.736.
2. **The brink is where the derivation fails.** Held. One left push moves the stopping point
   by 2|v|·dt + u·dt² (my algebra from the exact step), which is 1.26 mm at dt = 0.001 and
   0.13 mm at 0.0001 for the brink state's |v| = 0.632. Against its 0.5 mm margin, that
   explains why the gap stays large down to 0.001 and drops onto the derived line at 0.0001.
   The page now says that directly. Break: "That band narrows with dt, which is why Tallec et
   al. say the result holds almost everywhere" credited the writer's band argument to the
   paper. S1 §6 reaches "almost everywhere" from a discontinuous value function in pendulum
   swing-up. The sentence now reports what Tallec et al. say and where.
3. **At dt = 0.01, Q-learning's estimates vary more than the gap.** Held (0.047 against
   0.0074). The section closed on "In Dock the error doesn't shrink with dt", and no run at
   another decision length had been shown at that point. The commission requires that a claim
   about noise in Dock come from the lesson's own runs. I moved the claim next to the repeat
   output, where 0.013 at h = 0.1 s against 0.047 at h = 0.01 s supports it.
4. **Most of repeat's gain comes from the wider gap.** Held for exploration. Narrowed for the
   horizon. Both removal flags reproduce exactly at seeds 0–9. On seeds 10–19 the four arms
   give 0.74, 0.93, 0.75 and 0.68, matching the handoff. `--explore-repeat 10` is a clean
   test. In my throwaway check the median ratio of exact cell-centre gap to the cross-run
   spread of Q(right) − Q(left) is 0.16, against 0.15 at baseline. That arm recovers 0.08 of
   the 0.23 share gain on seeds 0–9, 0.01 on seeds 10–19, and none of the docking. `--tau 0.1`
   is not a clean test, and the page said it was: "Two flags each keep one of these effects
   and leave the gap at its dt = 0.01 size" is false for that flag. Its median ratio falls to
   about 0.004. Its share stays at 0.70 anyway. In cells whose exact gap under τ = 0.1 is
   about 10⁻⁶, 74% of runs still push right, so once the gap is far below the noise the share
   sits at a floor near 0.6 to 0.75 that does not track the gap. That arm therefore cannot
   separate the horizon in decisions from the gap. The page now says so in one sentence and
   rests the conclusion on what both arms show: neither comes near repeat's 0.94 or its 10 of
   10 runs that dock from every start. This narrows the claim to what the runs support. The
   exploration side is tested and the horizon side is only partly tested, and the page says
   which is which. The commission kept the `--tau 0.1` test, and it stays.

Other breaks and fixes:

- "Each Dock episode already starts at a random state, so every cell gets visited without
  help from exploration" was a causal claim with no removal test, and the writer's own
  edge.py found cells just outside the start range with 0 to 24 visits per run. Cut.
- Tallec Theorem 4 proves that ε-greedy trajectories converge to one deterministic ODE. The
  paper says the agent "is likely not to explore". "Stops exploring" became "follows one
  deterministic path and explores little", in the body and in Go deeper.
- Kalyanakrishnan et al.'s Theorem 6 is a bound. "Show that a shorter horizon lowers what
  errors cost" became "bound what errors in the estimates cost by a term that falls as the
  horizon in decisions shortens".
- εz-greedy draws each hold's length at random (S19). `--explore-repeat 10` holds for exactly
  10 steps. "As ... εz-greedy does" became "a fixed-length form of ... εz-greedy".
- 0.013/0.073 is 0.18. "About a fifth" became "under a fifth of the 0.073 gap".
- Fig. 1's caption said the first step is "the only one in which the two runs differ". The
  positions differ at every later step. Only the push differs, and the caption now says that.
- T = (w − v)/u holds only for a cart that docks. Scoped to that case.
- "Matches its first" could mean either of gap.py's two tables. It now names the dt = 0.1 row.
- The repeat arm does not simulate the same 2,000 s. q_learning counts decisions, and an
  episode that ends inside a held push still uses up a full decision. On seed 0 the repeat
  arm simulates about 1,911 s against 1,994 s at baseline. This works against repeat, so the
  comparison is conservative. The page now says "the same budget of 2,000 s". No code change.
- The observation-scale lesson (13 Nov) published a different environment named Dock (2 m
  track, three actions, a dock that accepts only slow arrivals, a buffer) with its own
  dock.py. "Dock is a small environment built for this lesson" is wrong for anyone taking the
  course. The opener now says the lesson rebuilds that Dock, links it, and states that
  docking at any speed ends an episode. The name and files stay. If the orchestrator would
  rather have a distinct name, the change is mechanical, and the printed output does not
  contain the name.

Runs and visuals. I extracted every listing from the page and ran it as printed with
`uv run`: dock.py (check_env passes), gap.py, and runs.py with no flags, `--repeat 10`,
`--explore-repeat 10` and `--tau 0.1`. Every output is byte-identical to the page, and the
listings did not change in this round. I checked every printed number in prose against
those outputs. I checked Fig. 1's docking points and the 0.49 m dip, and Fig. 2's points and
both derived lines, against gap.py. I checked all 200 cells of Fig. 3 against counts
recomputed from the page's code, seeds 0–9 (no mismatches; means 0.71 and 0.94).

Citations. Every href opens the cited document. The Doya DOI resolves to the MIT Press
article page, which refuses scripted clients and serves browsers. The Nature href lands on
the article, and data-nb-url carries the readable PDF. All seven sources are correctly
marked primary for the claim each is cited for. None is used to corroborate another, so the
shared author of Bellemare et al. and Dabney et al. (Ostrovski) claims no independence the
page lacks. The headline's tenfold and the
dek's 71% and 94% match the printed output. Neither carries a title, role or affiliation.

## Reads well

- **Repeated the recent record.** The dek used the 14 Nov dek's construction ("Gymnasium's
  two-frame stack gives ..., and the agent then ..."). It now leads with Q-learning's share
  and states the cause. The card's last part opened "Here you", as 14 Nov's card did, and
  now opens on the worked case. The body's first sentence, "Dock is a small environment built
  for this lesson (Fig. 1)", copied the 14 Nov opener ("Pitch is a small environment built
  for this lesson (Fig. 1)") and the 13 Nov one. It was also wrong, as above.
- **Said nothing.** "It also shrinks what the agent has to learn" (card) became the concrete
  claim that a shorter step makes the actions harder to tell apart. "And a derivation gives
  its slope" was cut. The takeaway opened "How often the agent decides sets how much it has
  to resolve", which still reads as a sentence with the nouns removed. Rewritten.
- **Takeaway.** Besides that opener, its second sentence echoed the card almost word for
  word. It left out the lesson's own result, the removal tests, and it ended on a tacked-on
  sentence about the discount. It now restates the idea, gives the baseline and repeat
  results, and ends on what the two removal arms showed.
- **Garbled or overloaded.** "Estimate two numbers ... closely enough to separate them by
  less than 0.01" is fixed. "The two step lengths would learn with different step sizes"
  used "step" for two things, and it now reads as one clause about the step size.
- **Caption carrying interpretation.** Fig. 3's "Faint cells at the lower right are ones the
  cart seldom returns to" was an explanation, and edge.py supports it only in part: the faint
  cells border speeds that runs seldom reach. I cut it rather than move an untested cause into
  the prose.
- Nothing came from the briefing files or the voice guide's quoted passages. No section ran
  flatter than the guide. The derivation already says what each line is for before taking
  it, as the guide asks.

## The experience

- Fig. 3 sat at the end of the baseline section, and its second panel showed repeat results
  before the page had introduced repeat. It now sits beside the repeat result it compares.
- The last section held the repeat result, two removal tests, the cost of control and the
  problems. I split it. The new section, "Most of repeat's gain in Dock comes from the wider
  gap", holds the removal tests, the cost of control and the problems. Read alone, the five
  headings now give the argument in order. Five flex sections is within the commission's
  range.
- Prose on the rendered page is 2,281 words counting headings, the card names, the Problems
  and Answer labels and the code-listing summaries, or about 2,210 without them. Before this
  round the same count gave 2,243. The narrowing above added words. To pay for them I cut the
  fixed-per-step γ example (problem 2 has the reader do that calculation), the docking-time
  sentence (Fig. 1 labels both times), the clause restating τ in the opener, and the closing
  line of problem 1's answer. With code and output the page is 4,996 words, inside the
  commission's 2,500 to 6,000.
- Rendered with `nb preview` and captured at 390 px and 1280 px in light and dark: no
  horizontal page overflow, seven KaTeX blocks with no errors, no overlapping labels.
  `--chart-4` is red in both themes, so Fig. 3's "red curve" holds.
- What it gives beyond its sources: an exact, runnable check of Tallec et al.'s O(dt) result
  in a small environment, including a state where it fails and why. It also shows, for
  tabular Q-learning, that action repeat helps mainly by widening the gap. Exploration is
  separated cleanly and the horizon only partly. The handoff's original-work sentence claims
  the same, except that it calls the horizon test a full separation, and the page now does
  not.

## Edits

- Dek rewritten (meta and page) to break the 14 Nov mold and state the cause.
- Why this matters: replaced "It also shrinks what the agent has to learn" with the concrete claim; rewrote the "Here you" ending.
- Opener: Dock now presented as a rebuild of the observation-scale lesson's Dock, linked, with docking at any speed stated.
- Opener: "so a second spent at time t costs e^(−t/τ)" shortened to "a horizon of 1 s at every dt".
- Fig. 1 caption: "only one in which the two runs differ" → "only step in which the two runs push differently".
- Orientation: docking times folded into "0.21 s later ... 0.02 s later"; "two numbers ... separate them by less than 0.01" rewritten.
- Derivation: opening sentence names the smoothness condition and drops "gives its slope".
- Derivation: legend and following paragraph say the bracket "stays bounded as dt shrinks".
- Derivation: fixed-per-step γ example cut to one clause.
- Derivation: T formula scoped to a cart that docks.
- gap.py result: "stays at 0.736" → "between 0.731 and 0.736 ... against the derived 0.736".
- Brink paragraph: split the 0.001 and 0.0001 cases; replaced the "which is why Tallec et al." attribution with what S1 §6 says.
- Q-learning section: step-size sentence rewritten; closing "In Dock the error doesn't shrink" moved to the repeat result with its numbers.
- Repeat section: "also called frame skip" dropped (the card names it); "matches its first" → "matches the dt = 0.1 row"; "same 2,000 s" → "same budget of 2,000 s".
- Repeat section: "about a fifth of the gap" → "under a fifth of the 0.073 gap", plus the 0.047 comparison.
- Fig. 3 moved from the Q-learning section to the repeat section; caption's faint-cells sentence cut; repeat panel's alt text "nearly every" → "most".
- New section "Most of repeat's gain in Dock comes from the wider gap" (`most-of-the-gain-comes-from-the-gap`) split from the repeat section.
- Removal-test paragraph: Tallec Theorem 4, Kalyanakrishnan Theorem 6 and εz-greedy narrowed to what the sources state; "leave the gap at its dt = 0.01 size" → "while every greedy move still lasts 0.01 s".
- Removal-test results: cut the untested random-start explanation; added the sentence on what the tau arm cannot separate; conclusion rests on neither arm approaching 0.94 and 10 of 10.
- Cost-of-control paragraph lightly trimmed.
- Problem 1: "Where does V jump" → "Where does V gain a new jump"; answer's closing line cut.
- Takeaway rewritten.
- Go deeper, Tallec: "stops exploring" → "explores little".
- `nb stamp` rerun: words 4,996, reading time 22 min, sources 7.

## Decision

approve. Every break was fixable from the record and the lesson's own runs, the proof passes,
and the narrowed claims leave the argument intact, so nothing needs to go back to the writer.
