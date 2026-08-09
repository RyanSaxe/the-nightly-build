# Editorial review: paper-of-the-day/deep-q-network (editor/01)

## Skeptic

Thesis: DQN carried two claims the abstract runs together — an aggregate slogan
("human-level control across 49 games") and an operational, narrow result
(a single pixels-and-score network reaching at least 75% of a professional
human on 29 of 49 games) — and the decade of scrutiny that followed left the
operational claim standing while dismantling the slogan. The piece stands on
four load-bearing claims: (1) the divergence problem is real and comes from
correlated updates plus a self-moving target; (2) two devices, experience
replay and a frozen target network, make the standard Q-learning objective
trainable, and the ablation shows the effect is large; (3) the per-game spread
is enormous (Video Pinball 2,539% to Montezuma's Revenge 0%), so "human-level"
describes the top of a column, not a level reached everywhere; (4) the
after-record refines rather than overturns, with each study aimed at the claim
it actually touches.

I pushed hardest on claim 2, the one the headline rests on, and it is where the
draft broke. The ablation paragraph asserted, "Replay is the larger of the two
levers on every game in the table." The article's own Extended Data Table 3 row
for Seaquest contradicts it: replay-only scores 822.6, target-only scores
1003.0, so on Seaquest the single device that gets the agent furthest is the
target network, and removing the target network (down to replay-only 822.6)
costs more than removing replay (down to target-only 1003.0). The "every game"
generalization is false by the piece's own numbers. Cut directly; the paragraph
now stops at the Breakout walk-through, which stands on its own, and the
following paragraph's surviving point — the direction across columns is
unambiguous, the devices are not tuning knobs — is untouched.

The rest of claim 2 holds. The Breakout figures (316.8 full; 240.7 without
target; 10.2 without replay; 3.2 with neither) are correct, 3.2 is roughly a
hundredth of 316.8, and I confirmed against the Nature full text that Extended
Data Table 3 was run for 10 million frames across the four on-off combinations
and three learning rates, which is what the table caption and the follow-on
paragraph say. One minor imprecision, not blocking: the paper reports the
*highest* average episode score over the three learning rates, and the table
caption says only "average episode score." The cell values and the directional
argument are unaffected.

Equations check out against the evidence. The Bellman optimality equation, the
TD error with the target read from the frozen weights, and the squared-error
loss with its five-term colored legend all match the Nature Methods form. The
legend is honest term by term: the only trained term is the online Q, the
target uses the frozen weights, the sample is drawn uniformly from replay, the
reward is clipped, gamma is 0.99. The Huber-loss characterization of error
clipping is the paper's own ("absolute value loss for errors outside the
interval") and is correctly stated.

Numbers and directions: 49 games, 43 of 49 beating the best prior RL methods,
29 at or above 75% of the human tester, two-hour human practice, 75% threshold,
50M-frame headline training versus 10M-frame ablation — all trace to the
evidence record and, where firsthand, to the Nature full text I re-opened. I
verified the per-game percentages against the captured Figure 3: Video Pinball
2,539%, Breakout 1,327%, Montezuma's Revenge 0%, and counting the games above
the figure's own human-level divider (Video Pinball down through H.E.R.O. at
76%) gives exactly 29, corroborating both the 29-of-49 count and the 75% bar.

Display text: headline states a finding with its actors and no colon subtitle;
the dek adds the who and the after-record turn without restating the headline
and makes claims about the world, not about the article's method; every section
heading is a concrete step of the argument in the piece's own nouns. The paper
card meta (Nature 518, 529–533, 2015; Mnih, Kavukcuoglu, Silver et al.) matches
the source. The verbatim abstract is word-for-word against the Nature text
(British "behaviour," "optimize," the exact final sentence); see the Reader note
on the dropped reference superscripts.

`data-nb-kind` audit: all eight sources are the documents that own their
claims — the two Mnih papers, Bellemare's ALE, Machado, Agarwal, Henderson, van
Hasselt, Schaul — and each is correctly marked primary. No secondary reporting
stands in for a primary, and no independent-source gap is hidden. Citation
hrefs resolve to the sources themselves; the Nature link 303-redirects to the
publisher's SSO, which is the paywall gateway for the correct article URL, not a
miscitation.

After-record aim, the round's central watch-item, is correct throughout.
Machado is written as vindication ("a pure memorizing planner then collapses,
while learning agents such as DQN barely move ... closer to a vindication than a
rebuttal"), not a re-run that found DQN unstable. Agarwal is pinned to the
aggregate metric practice and the Atari 100k regime, "not a re-run of the
original agent." Henderson is marked MuJoCo continuous control bearing on DQN
"by analogy about fragility, not a re-test." Van Hasselt is correctly the one
study that tests DQN's exact algorithm (overestimation in all 49 games) and
refines it. No "DQN was debunked" framing anywhere; the mapping table and
verdict encode the same precise aim.

## Cut

I ran the slop pass over every sentence, including display text and the two
figure captions and the verdict furniture. Four sentences failed and were cut;
one was a correctness break (above), three were signposts or reader-gestures:

- The orientation section closed on a method preview — "Rebuilding the paper
  means rebuilding that objective first, then showing precisely what each device
  does to it" — which narrates the article's own plan and adds no claim. Cutting
  it lets the section end on the stronger line, that the contribution is two
  devices, not a new objective.
- The objective section carried "Read the term colors against the legend: this
  one equation carries the entire method, and both devices are visible inside it
  as a choice of where a symbol comes from." The first clause gestures at the
  reader; the rest duplicates the next paragraph's opener ("The two colored
  choices at the right of the loss are the whole argument"), which cashes the
  same idea out concretely. Cut the redundant, self-pointing sentence and kept
  the paragraph that does the work.
- The after-record opened on "A result this visible drew a decade of scrutiny,
  and it is worth being exact about what each study actually re-examined, because
  the honest reading is neither that the work was overturned nor that it went
  unchallenged." The middle clause is method self-grading, and the framing it
  states arrives more concretely in the very next sentence, "The two halves of
  the claim came apart under different pressures," which now opens the section.

On the negative-parallelism reflex, the paper's most common tell: the piece
uses the contrast form several times ("not a new objective ... two devices,"
"a claim about the top ... not a claim about the bottom," "describes a spread,
not a level the agent reached everywhere," "refined ... rather than replaced").
Each corrects a misconception that is real, named, and central to the argument
rather than a strawman, so they are earned and I left them. I watched the
density but did not find one that fails the test.

The two intentional long sentences the writer flagged (the ALE-normalization
sentence and the after-record framing) hold. The voice guide models exactly this
on Weng's long, carefully punctuated definition and the editorial standard
sanctions "a long sentence under control." Both are single-purpose, grammatical,
and cannot be misread; splitting them would flatten the register the guide
directs. Recorded as holding, not split.

Openers and headings against the recent-pattern notes: the piece opens on a
plain definition ("Q-learning tells an agent what a move is worth"), not the
"before it was asked to" reversal mold the notes flag, and the verdict block is
headed "What the after-record left of 'human-level'," this paper's own question,
not the recurring "A reviewer's verdict." Both recent formulas are broken.

## Reader

Read straight through, what the piece gives beyond its sources is the split
itself: it separates DQN's two non-identical claims and sorts each after-record
study by which one it actually bears on, so the operational 29-of-49 result
reads as surviving every direct test — including the stochasticity that breaks a
memorizer — while the aggregate slogan is the casualty. The evidence record
supplies the studies and their scopes but does not perform that sort; the
draft-handoff's original-work sentence claims exactly this, and the "Where the
later studies land" table and the verdict make it visible on the page. Both
answers survive, so the piece is a reconstruction, not a restatement. The prose
sits closer to the voice-guide exemplars than a median summary: the equations
are set and reasoned rather than paraphrased, and the after-record is weighed
with named, precise aim in Karpathy's even register rather than a vague "later
work raised questions." The headline, reread as the largest claim, is defended
by the body.

The two figures are evidence, not decoration, and both earn their place. Figure
3's crop keeps the full vertical list of 49 games, the human-level divider, and
the broken axis to 4,500% — the top-to-bottom spread the aggregate phrase hides,
which is precisely the argument it is spent on — and its caption is a factual
cited label. Figure 4 keeps the value color scale and the pinned Space Invaders
screenshots, so the "organized by value, not by pixels" reading the prose makes
is testable against the image; the interpretation stays in prose, the caption
stays factual. Neither crop omits load-bearing evidence or carries clutter.

On the dropped abstract superscripts: the Nature abstract does carry inline
reference numerals (normative account¹, psychological², neuroscientific³,
processing systems⁴,⁵, algorithms³, domains⁶⁻⁸, networks⁹⁻¹¹, games¹²), and the
card drops all of them while keeping every word. This is acceptable for a
verbatim quotation and needs no mark: the numerals are bibliographic pointers
into Nature's own reference list, not words of the sentence, and that list is
not reproduced here, so retaining them would dangle or collide with the article's
own citation numbering. The template's requirement is the original's words on
record, and the words are exact.

## Edits

- Cut "Replay is the larger of the two levers on every game in the table, and
  the target network adds a second, consistent gain on top." — false by the
  article's own Seaquest row (target-only 1003.0 > replay-only 822.6).
- Cut "Rebuilding the paper means rebuilding that objective first, then showing
  precisely what each device does to it." — method signpost.
- Cut "Read the term colors against the legend: this one equation carries the
  entire method, and both devices are visible inside it as a choice of where a
  symbol comes from." — reader-gesture plus duplication of the next paragraph.
- Cut "A result this visible drew a decade of scrutiny, and it is worth being
  exact about what each study actually re-examined, because the honest reading is
  neither that the work was overturned nor that it went unchallenged." — method
  self-grading; the concrete framing follows in the next sentence.
- Ran `nb stamp`: words 3016 → 2907, reading_minutes 13, sources 8.

## Required work

None blocking. Two optional items for the writer, neither a publication blocker:

- writer: the cut lever sentence removed a real and generally-true point (replay
  is the larger lever on four of the five games; only Seaquest inverts it). If
  the house wants it restored, it needs accurate prose that states the Seaquest
  exception rather than a universal claim. New prose is the writer's, so it is
  left as an option, not a requirement.
- writer: the ablation table caption says "average episode score"; Extended Data
  Table 3 reports the *highest* average over three learning rates. A one-word
  precision fix ("highest average") if the writer wants the caption exact. The
  cell values and the directional argument do not depend on it.

## Decision

approve — every publication-blocking issue is resolved by direct cut: the one
correctness break (the false "every game" lever claim) is gone, the signposts
are out, and the equations, figures, numbers, source kinds, links, verbatim
abstract, and after-record aim all hold on re-verification.
