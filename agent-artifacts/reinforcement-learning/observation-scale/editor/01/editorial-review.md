# Editorial review: reinforcement-learning/observation-scale (editor/01)

## Correct

Thesis, from the draft alone: a gradient learner applies one step size to every
input, so the input with the largest numbers caps the stable step and the
weight on the smallest learns slowest; the units an environment reports
therefore change what gets learned, and standardizing each component, with
statistics the agent keeps, removes that dependence.

Claim 1. For the expected linear update, the eigenvalues of A = E[xxᵀ] set the
bound 2/λmax and a pace governed by κ, and reporting an uncorrelated component
c times larger multiplies its eigenvalue by exactly c². Held. I followed every
line: the recursion, the eigenvector split, DAD, the condition E[xᵢxⱼ] = 0 that
makes eᵢ an eigenvector, the reading of "uncorrelated" against the constant as
a zero mean, and the expected-versus-per-sample distinction the commission
asked for. Two breaks, both mine to fix. "The same factor" for Goh's step was
loose: the two factors are equal in size and opposite in sign. And "its
eigenvalue moves by roughly c²" for correlated features is contradicted by the
writer's own every-visit check (checks/linear_checks.py, rerun): the position
eigenvalue grows 1.97 million times there, about twice c². Narrowed to "a factor
of the order of c², not exactly c²", which is what the record supports.

Claim 2. On Dock the linear runs land where the eigenvalues put them. Held. I
reran dock.py and linear.py exactly as printed and got byte-identical output,
then checked each figure against it: 999,997; 7.4 × 10⁻⁶; 1.01× above 10⁵ and
0.99× below it in every row; κ of 34, 1.03 and 9 million; 76 steps inside the
77.5 bound; 21 million; 3.8 of 19.6. Table 1 recomputes (−2.45, −475,002; the
per-sample factors 0.871 and −24,999). Fig. 2's three-to-one ellipses follow
from the eigenvalue ratio 9.15, and 3,000 from √(9.15 × 10⁶). The rerun of
linear_checks.py also reproduces the writer's new-start and per-sample numbers.
Problem 1 recomputes to 2.145 and 0.127 from the printed block (2.141 from the
data), κ near 72, 2/λmax near 0.93; problem 2 is exact.

Claim 3. PPO on raw millimetres ignores velocity and PPO through VecNormalize
uses it, with the cause left open. Held after one cut. agents.py, rerun as
printed, reproduced its output byte for byte in 3 min 33 s on four cores, and
`agents.py 5` reproduced the writer's seeds5 output. The headline survives both
seed sets: raw millimetres changes its move with velocity at no grid position in
seeds 0 to 4 and at most one in seeds 5 to 9, where raw metres ranges from 2% to
100%. The removal tests on the page are the normalized rows (units out) and the
fresh-statistics row (training statistics out); the page claims no mechanism
for the gap and names tanh saturation and Adam as unseparated. I simulated the
seed-0 raw-millimetre policy from 400 starts: right-of-centre starts dock 189
of 194 times after about nine bounces and left-of-centre starts 3 of 206, which
is the page's account. The break: "In most runs that speed falls as the cart
nears the dock, so the cart arrives slowly enough to stop." I printed all ten
normalized policy maps. The push-right threshold falls toward the dock in six,
rises in three (millimetres seed 0, the run Fig. 3 shows, among them) and is
flat in one, and grid rows 0.1 m/s apart cannot show an arrival speed. Cut.
"Seeds 5 to 9 split the same way" did not say what repeats; it now says.

Claim 4. The statistics are part of the policy and need saving, reloading with
the flags reset, and freezing. Held. Checked against the 2.9.2 and 1.4.0 source
pages at their tags and the SB3 examples page.

Labels. Headline, dek and every heading checked against the output and the
sources. The takeaway compared a run (76 steps) with a bound (21 million); it
now compares the two runs. "Ignored velocity in all five seeds" became "all but
ignored velocity in every seed", since two later seeds use it at one grid
position. "About three minutes" for agents.py became "three to four minutes"
(3:17 to 4:00 across the writer's and my runs).

Links. Every printed href opened. PyPI, arXiv, Distill, the ICLR blog and the
SB3 docs return the cited pages. The proxy refuses curl on GitHub, so I read the
four GitHub source pages through WebFetch: each shows its tag and the cited
code. The SB3 docs link now points at /en/v2.9.2/, which matches its label.
Source 1, https://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf, resets during
the TLS handshake here, as it did for the researcher; the http address in the
evidence record returns the PDF, and the proof refuses http in Sources
(B-SOURCES-FORM). I left the https href in Sources and put the working http
address in Go deeper, where the proof accepts it. This is the one open item: the
orchestrator has to rule on whether the reset is this environment's, or have a
researcher find an https address for Efficient BackProp (the record names the
Springer DOI, which resolves to a paywalled chapter page and would need its
wording and locators checked).

Kinds. All ten audited. Goh is secondary, an exposition of a classical result;
the rest are primary. Sources 4, 5, 6, 8 and 9 all come from the SB3
maintainers, and the page never offers one as independent support for another.

## Reads well

Went because they said nothing or repeated the page:
- The LeCun quotation "convergence time is proportional to the condition
  number", which restated the sentence before it.
- "Through VecNormalize ... 54 to 120 steps and 49 to 129", which repeated
  Table 2.
- The appositive defining a frozen greedy policy, already taught in the linked
  PPO lesson.
- The reward-scaling pointer at the end of the statistics section; the PPO
  section already says `norm_reward=False` isolates the observation.

Went for accuracy or clarity:
- Sutton and Barto's rule of thumb, whose τ the page never defined and which
  repeated the per-sample point. Source 3 went with it and the list renumbered.
- The dek: one 36-word sentence ending in "which ... undoes", carrying two
  asides and mixing the linear learner with the agent's saved statistics. It now
  states the stance in 24 words, with no number, and builds differently from
  the recent "On <environment>" and method-name deks.
- In Why this matters, "The spread of each component then predicts ...": after
  normalization every spread is 1, and spread is not what sets the largest
  eigenvalue in metres (the constant's is). Rewritten as what the eigenvalues
  give before a run. "The one with the smallest learns slowest" now names the
  weight.
- Abstractions acting: "the fresh statistics row ... plays", "the figure ...
  drags", "SB3's network adds what that learner lacks". "Collapse" became
  "fail".
- "Would hold the position weight steady" read as "would not move it".

From the briefing: the takeaway opened with the commission's clause "a gradient
learner uses one step size for every input" taken whole, and the last section's
heading was the commission's "statistics belong to the agent". The takeaway now
opens on the linear case the lesson derived, and the heading states the step
the section shows. No borrowed clause from the voice guide's passages.

Against the recent record: the headline is built around the units choice and
avoids the recent "sends/learns/no longer" verbs; headings do not pair clauses
with ", and"; the card neither opens on an earlier method's property nor closes
on a second-person roadmap; Background 04 is the environment-checker lesson.

The commission's length decision: I cut repetition first, then shrank the
NormalizeObservation paragraph to one sentence, keeping the after-construction
detail, which is the trap. The metres row stays.

## The experience

Rendered with nb preview and captured with Playwright at 390 and 1280 px in
light and dark. No horizontal page scroll. Figures 1 to 3 and all four
equations fit at both widths with no overlapping labels; Fig. 2's "step 6" label
sits a little below its dot, between steps 5 and 6, which reads acceptably. On
a phone Table 2 scrolls sideways and its "Uses velocity" column, the headline's
evidence, started off screen; it now sits next to Observation. The cut
threshold sentence had told the reader to see something Fig. 3's normalized
panel does not show, so the prose and the figure now agree.

Word count on the rendered page, counting the cards, captions, table cells,
problems and answers and leaving out code, output, equations, drawings, bands
and sources: 2,210 words containing a letter, 2,490 whitespace tokens with
numerals counted (from 2,250 and 2,534 before this review). That sits at the
template's 2,200 threshold by the first measure and above it by the second. What
remains is commissioned: the per-sample bound, the unseparated-causes sentence,
the fresh-statistics test, the metres row and two problems. I found no further
repetition, and the next cut would remove one of those. agents.py runs to 116
lines with its metadata, at the series' "about 100".

Beyond its sources: the sources give 2/λmax and κ for a quadratic and advise
normalizing. The lesson derives how a change of units moves one eigenvalue by
c², which the record says no source states, checks it on an environment whose
units can be switched, and shows the PPO policy that results: one that steers
by the position's sign in millimetres and uses velocity once normalized, and
that fails again when evaluated without its own statistics. The writer's
original-work sentence says the same, so it survives. Reread last, the headline
holds across ten seeds and claims only the effect of the units, which the
normalized rows test.

## Edits

- nb-meta model: "claude-opus-5-5 (effort xhigh)" to "claude-opus-5-5".
- Dek (meta and page): rewritten as one 24-word sentence.
- Why this matters: rewrote the eigenvalue and "spread" sentences; "the weight on the smallest".
- Orientation: "would hold the position weight steady" to "would undo that".
- Eigenvalues: cut the LeCun condition-number quotation.
- Eigenvalues: Goh's step gives "factors of the same size", and "no single step size does better".
- Eigenvalues: D has "1 elsewhere".
- Eigenvalues: correlated case narrowed to "a factor of the order of c², not exactly c²".
- Eigenvalues: per-sample paragraph tightened; Sutton and Barto sentence and source cut; sources renumbered 1 to 10.
- Linear runs: merged the dock.py sentences.
- PPO: cut the frozen-greedy appositive; "three to four minutes".
- PPO: Table 2 caption tightened and "Uses velocity" moved to the second column.
- PPO: cut the step ranges repeated from Table 2 and the falling-threshold sentence; seeds 5 to 9 now say what repeats.
- PPO: "SB3's PPO has neither"; "so they show".
- PPO: Fig. 3 normalized-panel aria-label matched to the grid.
- Statistics: heading now "Evaluating a normalized policy needs its saved, frozen statistics".
- Statistics: "agents.py plays" in place of "the row plays"; "fail" in place of "collapse".
- Statistics: NormalizeObservation paragraph cut to one sentence; reward pointer cut.
- Takeaway: opens on the linear case; compares two runs; "all but ignored velocity in every seed".
- Go deeper 01: http address from the evidence record. Go deeper 02: "lets you drag". Go deeper 04 and source 9: /en/v2.9.2/.
- nb stamp rerun; proof BLOCK 0, with the one W-CITE-DENSITY the commission kept.

## Decision

approve: the argument stands and every other fix is made, but publication waits
on the orchestrator's ruling on source 1's https address.
