# Editorial review: reinforcement-learning/factored-action-spaces (editor/01)

## Correct

Thesis, from the draft alone: when an action value is a sum of one table per
component, Q-learning's maximum splits into one maximum per table and a state
needs Σ n_d entries instead of Π n_d; trained on one shared TD error, each table
ranks its levels by the target averaged over the other components at the rates
the agent tries them, so the per-component choice is optimal wherever every
component has a level that is best whatever the others do, and it can settle on
a pair no joint learner picks where they interact.

1. The maximum of a sum is the sum of the maxima, with the Σ/Π count. Held. The
   inequality and its equality case are right; 9/27 and 18/729 check.
2. The resting point. Held. With exploration independent across components,
   μ_-d does not depend on b, so the solved entry is right. The drive's γV̂(s′)
   term is additive, so the arm's ranking depends on the reward alone. I
   recomputed every number: the cell-2 averages −6.20, −5.20, −5.70 (mast down
   28/30, half and up 1/30 each), the 0.5 gap (1 against 45/30), cell 5 (6/30,
   0.8 ahead), ε = 0.05 (45/60 = 0.75, so extended 0.25 ahead), and the
   "farthest from a sum" gaps 20.00 = 45·4/9 and 2.67 = 6·4/9. Problem 1's
   answer works out the same way.
3. Speed. Held, with one sentence broken. rover.py and scale.py, run as printed
   with `uv run`, reproduce the page byte for byte. fresh.py (seeds 100–109) gives
   the same ordering and 57,000 against 4,500 at six (12.7×). The page said
   "From three components up, the slowest factored run beat the fastest joint
   run. Ten fresh seeds agreed." On the fresh seeds at D = 3 the slowest
   factored run took 4,500 steps and the fastest joint run 4,000. The handoff
   read the fresh seeds as holding from D = 2, but they break at D = 3. From
   D = 4 it holds on both sets, and the page now says so. jointcount.py 0
   reproduces the shrinking-step sentence (10,000 against 4,250 at six, level up
   to four).
4. The departure. Held. ledges.py and `--flat` as printed, `--first-seed 100`,
   epscheck.py 0.05 and snapshot.py all reproduce the handoff. A new check,
   code/checks/editor_settled_eps.py 0.05, shows the settled pair at ε = 0.05 is
   (2, 1, 0) in all 20 runs, so "settled on half" is right there too.

Breaks and fixes:

- The page's central result, that all 20 runs settle with the arm at half, and
  Fig. 4's "From ledges.py" rested on settledpair.py, an off-page check.
  ledges.py printed only departure counts. I added five lines so it prints the
  settled (drive, arm, mast) wherever a run departs, reran it and `--flat` as
  printed (about 2 min 20 s each), and put the new output line on the page:
  `factored in cell 2 settled on (drive, arm, mast) (2, 1, 0) in 20 runs`.
- "Neither ledge changes Q* in another cell" is true, but only because neither
  ledge's optimum tips; the sentences after it argued something else, that Q*
  is a sum away from the ledges. Cut it. The paragraph now says only what its
  argument shows, and its last sentence says a ledge's estimate can change the
  factored learner's choices elsewhere only through the drive term, which is
  what the resting formula gives.
- The ε = 0.05 paragraph opened by saying the rates follow the agent's own
  greedy choices "and two checks show the difference", which credits rate drift
  with a departure that no removal test isolated (handoff check 10 failed to).
  The commission asked for no cause. It now states the fixed-rate assumption,
  the run that contradicts it, and that the runs do not show why.
- "The only evidence that it converges here": with a constant step nothing
  converges, and the page itself says the estimates wander. Now "settles".
- Tavakoli et al.'s target "averages the branches' maxima": eq. 6 averages each
  branch's target-network value at its online argmax. Now "greedy values".
- Go deeper, Tang et al.: "Theorem 1 says when a sum is exact" read as if and
  only if. The theorem's conditions are sufficient, and p. 4 says none is
  necessary. Reworded.
- Go deeper, Kanervisto et al.: §IV gives guidelines and compares nothing.
  Reworded to what §III and §IV each do.
- "whose sample() draws each component independently" is in Gymnasium's source,
  not on the cited documentation page, and nothing later used it. Cut, and the
  s1 locator narrowed to the cartesian-product definition.

Citations. I opened every printed href. The Gymnasium, Stable-Baselines3, NeurIPS,
arXiv and HAL addresses return 200 and land on the source, and both Gymnasium
anchors exist. https://incompleteideas.net/book/RLbook2020.pdf fails: the server
presents Dreamhost's self-signed certificate for that name, so a reader gets a
certificate error. The evidence record's http address works, but the proof blocks
non-https hrefs (B-SOURCES-FORM). The sentence it supported, that tabular
Q-learning converges to Q* under the usual conditions, is what the SARSA and
Q-learning lesson teaches (Watkins and Dayan, with the step conditions), and this
section already relies on that lesson. I linked the lesson there and removed the
Sutton and Barto source. The five remaining sources are primary: each is the
library maintainer or the method's author describing their own work, and the
page claims no independent confirmation.

Headline, dek and headings: every number and label checked against rover.py,
scale.py and ledges.py output.

## Reads well

What went:

- The Gymnasium flatten sentence and its source. It is accurate, but the main
  idea does not need it, and the listing already shows `ravel_multi_index`. It
  went as part of the length cut.
- "By the split above, this target costs one maximum per table." It repeated the
  caption that ends the previous section.
- "...and the sum for any other joint action by αδ for each level it shares."
  The six-components section gives the same mechanism where it is used.
- The steep-ledge section's closing line, "the pair the factored learner settles
  on depends on how often it tried each pair, and so on its own history". It
  restated the derivation in a quotable form; the takeaway already carries the
  claim.
- Fig. 2's "tipping puts extended with the mast up 45 below the row-plus-column
  pattern". It was interpretation in a caption, and the prose says it.
- "mostly in the drive". On the page it was a detail with no meaning attached.

What changed:

- The card said "part" where the body says "component". Now "component"
  throughout.
- Problem 2 asked for the feature vector that the body's semi-gradient sentence
  already gives. It now asks why the joint learner stays optimal on the steep
  ledge although it also tries the tipped pair. That tests the contrast the
  lesson rests on and brings back the Q-learning resting point, with a link.
- Fig. 2's "right-hand column" was ambiguous, since cell 3's right-hand column
  is the arm term. It now names cell 2's average column.
- "The shallow ledge keeps it extended" gave the ledge the action. Now every run
  keeps the arm extended there.
- The speed paragraph opened on the D = 1 identity. It now opens on the result.

Against the recent record: the headline drops the 17-word "err" version for the
orchestrator's "settle wrong" wording in 10 words, with a method, not a
character, as its subject. The dek carries no run figures and does not open
"On <environment>". The takeaway had opened on a general rule as recent ones do;
it now opens on the six-component figure and closes on the steep-ledge departure,
not on the learner succeeding. The last result heading, "Only the steep ledge
pulls the arm in", gave the ledge the action. It is now "On the steep ledge alone,
the factored learner's arm settles at half". The speed heading now carries its
condition ("the same α"), since the shrinking-step check cuts the ratio to about
two.

The register matches the guide. No passage ran flat enough to need lifting beyond
these changes.

## The experience

Built with `nb preview` and captured with Playwright at 390 and 1280 px in light
and dark. There is no horizontal page scroll, and the output blocks scroll inside
their frames on a phone. Every label in Figs. 1–4 is readable in both themes. I
checked Fig. 3 point by point against scale.py's output (through figures.py's
data), Fig. 2 against rover.py and the averages above, and Fig. 4 against the new
ledges.py line. No component was added or removed. The four drawings already show
the mechanism, the table, the scaling and the learned policy.

Prose words, counted with code/wordcount.py by the identity's definition (cards,
body, captions, table cells, problems): 2,162, down from 2,260. With headline and
dek, 2,206.

What it gives beyond its sources: it derives where per-component tables trained
on one shared TD error come to rest, builds a tabular environment where that can
be checked against exact Q*, and confirms both the Π-to-Σ saving and the one
predicted departure with seeds and a removal test. No cited source does this for
tabular Q-learning. This matches the handoff's original-work sentence.

The headline is its largest claim. It holds at ε = 0.1 on two seed sets and at
0.05 and 0.2. It is scoped to the rover and to the averaged (settled) choice,
which the page distinguishes from last-step readings.

## Edits

- Headline: "Per-component Q-tables settle wrong only on the rover's steep ledge" (title, meta, h1).
- Dek rewritten: 729 joint actions to six maxima over three levels each, with the dominance condition.
- Why this matters: "part" replaced by "component" throughout.
- Background row 02 note rewritten to name convergence and N(s, a)^−0.7.
- Orientation: cut the `sample()` clause; s1 locator narrowed.
- Fig. 2 caption: cut the interpretive sentence; named cell 2's average column.
- shared-td-error: cut "By the split above..." sentence.
- shared-td-error: Tavakoli target "maxima" → "greedy values".
- shared-td-error: Dαδ paragraph cut to one clause.
- shared-td-error: Sutton and Barto citation replaced by a link to sarsa-and-q-learning on "converges to Q*"; source s6 removed.
- shared-td-error: "converges here" → "settles here".
- shared-td-error: cut the Gymnasium flatten sentence; source s7 removed.
- averaged-levels: "right-hand column of Fig. 2" → "average column of Fig. 2".
- averaged-levels: cut "Neither ledge changes Q* in another cell"; last sentence now about the factored learner's choices.
- six-components heading: "The joint learner needs over ten times the steps at six components and the same α".
- six-components: results paragraph reordered to open on the result; "from three components up" → "from four components up, on these seeds and on ten fresh ones".
- steep-ledge heading: "On the steep ledge alone, the factored learner's arm settles at half".
- ledges.py: prints the settled (drive, arm, mast) wherever a run departs; listing and output updated on the page.
- steep-ledge: results paragraph names the settled pair (forward, half, down); shallow-ledge sentence recast.
- steep-ledge: ε = 0.05 paragraph rewritten with no cause claimed; "mostly in the drive" and the closing restatement cut.
- Problem 2 replaced (joint learner on the steep ledge, linking sarsa-and-q-learning).
- Takeaway rewritten: opens on the six-component result, closes on the steep-ledge pair.
- Go deeper: Tang row (conditions, none necessary) and Kanervisto row (§III compares, §IV advises) reworded.
- `nb stamp` rerun: 5 sources, 20 min.
- Code directory: ledges.py edited; ledges.out and ledges-flat.out replaced by the new runs; checks/editor_settled_eps.py added. page.html, page_body.html, page_head.html and page_tail.html no longer match the article. The article is the source of truth, so do not rerun assemble.py.

Proof after edits: `nb check ... --series reinforcement-learning` gives BLOCK 0,
WARN 4 (W-CITE-DENSITY on the four derivation and run sections, which the series
prompt exempts), PUBLISHABLE.

## Decision

approve. The argument holds and every break was fixable from the record, the runs
and the course. Nothing needs to go back to the writer.
