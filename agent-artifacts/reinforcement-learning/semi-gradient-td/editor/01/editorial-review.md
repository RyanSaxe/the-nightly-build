# Editorial review: reinforcement-learning/semi-gradient-td (editor/01)

## Correct

Thesis, from the draft alone: when values come from weights, gradient Monte
Carlo takes true stochastic gradient steps on the μ-weighted value error and
settles at the best fit, while semi-gradient TD(0) drops the gradient through
its own target and settles at the TD fixed point, which on the 1000-state walk
with 10 groups has 4.61 times the best fit's VE.

1. Gradient Monte Carlo is SGD on VE and, with linear features, converges to
   w_MC, where each group's weight is the μ-weighted mean of its v_π. Held.
   Equations 9.1 to 9.8 and the p. 202 and p. 205 statements match the 2020 PDF.
   μ(100)/μ(1) = 3.15, −0.8301 and −0.8456 match the printed output.
2. Semi-gradient TD keeps ∇v̂(S_t) and drops −γ∇v̂(S_{t+1}). Its expected step
   b − Aw is zero at w_TD, and b − Aw = Σ μ(s) δ̄_w(s) x(s) when a terminal
   state's features are 0, so the two conditions differ only in the error
   inside. Held. The two-term gradient's sign and the δ = 0.19, 0.019 and
   −0.451 arithmetic in Fig. 1's case are right. The p. 202 quotation matches
   the PDF word for word. The book prints "not instances of true gradient
   descent" before that sentence, so "Sutton and Barto add" is now "say".
3. On the walk the two exact solutions differ (VE 0.01363 against 0.00296), the
   runs end on their own staircases, and `--true-next` puts the TD run on Monte
   Carlo's staircase. Held. I extracted `walk1000.py`, `exact.py` and `runs.py`
   from the rendered page into an empty folder and ran the four printed
   invocations with `uv run`. All four outputs match the printed blocks byte for
   byte. Fresh seeds 21, 22 and 23 give TD runs at VE 0.0120 to 0.0141, Monte
   Carlo runs at 0.0030 to 0.0032 and `--true-next` runs at 0.0030, so the
   conclusion survives. One run takes 6.2 s, as the page says.
4. The original result: the TD fixed point gives the start state its exact
   value under any grouping. The derivation on the page holds step by step.
   Summing TD's condition over the groups uses Σ_i x_i(s) = 1. Multiplying by
   Σ η turns it into Σ η(s) δ̄_w(s), the expected total of one episode's TD
   errors. With γ = 1 and v̂(terminal) = 0 those errors telescope to
   G_0 − v̂(S_0, w), whose mean is v_π(500) − v̂(500, w). `--start 250` reruns
   to the printed −0.4727. A throwaway sweep over 9 groupings (1, 2, 3, 7, 10,
   13, 20, 50, 1000) and 11 starts (1, 37, 100, 101, 250, 499, 500, 501, 731,
   999, 1000) puts the start group's w_TD within 4.8e-15 of v_π(start) in all 99
   cases. The result needs features that sum to 1 in every state, no discount
   and one start state. The page states the first two, and the third is its
   case.

Breaks and the fixes made:

- The draft said the start-state condition "makes the staircase lopsided around
  state 500". The derivation fixes only the 401–500 weight. Whether the pair
  401–500 and 501–600 straddles zero unevenly also depends on the 501–600
  weight, and no removal test on the page touches it. I narrowed the sentence
  to what the derivation gives: the condition holds TD's weight for 401–500 at
  about 0, where Monte Carlo's is −0.087. A separate sentence reports that the
  book's Figure 9.2 shows the same uneven straddle, as the evidence record's
  Figure 9.2 asset note and contradiction 7 describe. This narrows the claim to
  what the derivation proves. The reporting behind it is complete for the
  weight it names, so nothing was narrowed to avoid recording thin reporting.
- Convergence on the walk had no source. The book's "converges to this point"
  sits in an analysis it runs for the continuing case, and Tsitsiklis and Van
  Roy prove only the discounted case that never ends. The walk ends and has no
  discount. Their Section I (p. 675) says the extension to absorbing chains is
  in reference [16], Bertsekas and Tsitsiklis's Neuro-Dynamic Programming
  (p. 690). I opened both pages in the MIT copy and added one sentence citing
  them.
- The gradient Monte Carlo equation's caption said it is "constant-step Monte
  Carlo" with a table. The walk revisits states, gradient Monte Carlo updates at every
  visit, and the linked lesson used first-visit. The caption now reads
  every-visit Monte Carlo with a constant step, as n-step-returns' takeaway
  does.
- "A TD error compares an estimate with the estimates one move later" left out
  the reward. Fixed.
- The VE pair was printed as 0.0136 against 0.0030 beside a ratio of 4.61.
  Those two numbers divide to 4.53. The page now prints the output's 0.01363
  and 0.00296.
- "1/(1 − γ) has no value here" now reads "no finite value".

Labels in the headline, dek and subheads: Example 9.1's rules, every equation
number, every page number and both #page offsets (book page + 22, Tsitsiklis and
Van Roy page − 673) match the PDFs I opened.

Every number in the prose and figures appears in or rounds from printed output,
or is arithmetic on Fig. 1's hypothetical weights or on γ = 0.9. The seed-check
conclusion is stated without numbers, as the series allows.

Citation addresses, opened as printed: `http://incompleteideas.net/book/RLbook2020.pdf`
and the Lisp file serve. Every "Open cited passage" link (`data-nb-url`) uses
those http addresses, and the PDF pages land on the cited passages. From this
environment, the source-list hrefs `https://incompleteideas.net/...` fail TLS
with a self-signed certificate issued by the sandbox egress, so I could not
prove them here. The orchestrator kept them in its decision on writer query 01,
and I left them. `https://doi.org/10.1109/9.580874` resolves to IEEE Xplore
document 580874. Both web.mit.edu PDFs serve. Every internal lesson link and
anchor exists in the library checkout. `nb check --check-links` passes.

`data-nb-kind`: s1 is primary for its own definitions, example and figures. The
page attributes the bound it reports to Tsitsiklis and Van Roy and also cites
their paper directly. s2 is primary because its authors prove the theorem. s3,
Sutton's own code, is primary. s1 and s3 share an author, and the page never
offers one as confirming the other.

Series limits: the page reports two results. The first is that the two methods
settle at different exact points and that runs land on them. The second is the
start-state condition, derived and checked at two printed starts. The one
causal claim about a run, that TD lands elsewhere because its target reads the
staircase, has its removal test on the page (`--true-next`). The lopsided
claim was the only other causal claim, and it is narrowed as described above.

## Reads well

- "One TD weight looked like a rounding accident at first." This came from the
  voice guide's example of a personal remark ("a result looked wrong at
  first"), reworded. The point under it is the article's own: −0.0009 reads
  like noise and is v_π(500). I rewrote it to state that point: "In `exact.py`'s
  output, TD's weight for 401–500 is −0.0009, close enough to 0 to pass for
  rounding."
- The dek ("Its update treats ..., and on a 1000-state walk with 10 groups it
  settles at 4.6 times ...") repeats the recent record's mechanism-then-"on a
  <case>" mold, which the commission lists as spent. The new dek leads with
  its subject and adds what the headline leaves out: Monte Carlo finds the
  closest fit. I avoided "10-step staircase", which this course would read as
  n-step TD.
- "whose errors count most" became "which states' errors count most".
- "From the states next to it" became "From the states one jump away". The
  book's 0.17% belongs to the 200 states within one jump, not only to 499 and
  501.
- "Step" meant a step size, a gradient step and a stair. In prose, the stair
  now reads "weight" wherever it names a group's value.
- The runs paragraph called Monte Carlo's answer a "fixed point", a term the
  page reserves for TD. It now reads "its method's exact weights".
- Takeaway: "ignores that" became "ignores that dependence". Its close was a
  section-by-section run (commission note), and now states why the fixed point
  sits off v_π: a TD error never checks an estimate against v_π.
- I split the three-clause bound sentence and the divergence pointer into
  sentences of one or two clauses.

Headline, "TD(0) no longer converges to the best fit once states share
weights": kept. Subject, verb and surprise come first. It states the book's
general claim (pp. 205-206: linear TD converges, to a point that is "not the
global optimum"), and the walk shows that claim. It names no case and no
number, so it does not follow the last five headlines' "<method> <verb>
<result> on/than <case>" form. It has no colon and no question.

The headings form a chain of full-sentence findings with no repeated "X and Y"
pattern, and a reader who skims them can rebuild the argument. Read alone, the
edge sentences contain no slop beyond the items above. The register matches
the guide: plain verbs, the purpose stated before each step, and Fig. 1's
single move reused in the semi-gradient section.

## The experience

The bound, its scope and the divergence pointer sat at the end of "Runs of both
methods end on their own exact staircases", which they are not about. I moved
them into the fixed-point section, directly after the 4.61 ratio the bound is
compared with. The runs section now holds only the runs, and the body ends on
the removal test and the problems.

The start-state derivation now has its own section, "The TD fixed point gets
the start state's value exactly". The lesson's original result gets a heading
that skimmers see, and the explanation now comes before Fig. 3, whose dot marks
v_π(500).

The figures are unchanged. I checked them with `nb preview` and Playwright at
390 and 1280 px in light and dark themes: no overlapping labels, arrows reach
their targets, and the page has no horizontal scroll. Fig. 3's markers match
`runs.txt`, and Fig. 2's labels match `exact.txt`.

Prose word count on the rendered page: 2,132 (the two cards, body, captions,
legend text, the `details` note, problems and answers, without the header,
equations, code, output, SVG text, bands and sources). It was 2,070 before the
edits, and the template's limit is about 2,200.

What it gives beyond its sources: it writes the best fit and the TD fixed point
as one μ-weighted condition on two different errors, tests the cause by giving
TD's target v_π, and derives from TD's condition that the fixed point is exact
at the start state, which accounts for the near-zero 401–500 step in the book's
Figure 9.2. This matches the handoff's original-work sentence, except that the
handoff claims the derivation explains the whole lopsided pair. The page now
claims only the 401–500 weight.

## Edits

- Dek (header and nb-meta): rewritten as above.
- Gradient MC, P1: "whose errors" → "which states' errors".
- Gradient MC, Fig. 2 paragraph: "states next to it" → "states one jump away".
- Gradient MC caption: "constant-step Monte Carlo" → "every-visit Monte Carlo with a constant step".
- Semi-gradient, quotation sentence: "add" → "say".
- Fixed point, P2: added the Tsitsiklis and Van Roy pointer to Bertsekas and Tsitsiklis for tasks that end (s2, Section I, p. 675; reference [16], p. 690).
- Fixed point, aggregation paragraph: TD error compares "with the reward and the estimate one move later".
- Fixed point, ratio paragraph: "outer steps" → "outer weights"; VE pair now 0.01363 against 0.00296.
- Moved the eq. 9.14 paragraph, equation, scope paragraph and divergence pointer from the runs section into the fixed-point section after the ratio; "no value" → "no finite value"; split the long sentences; removed the restated "On the walk the ratio is 4.61", now stated one paragraph earlier.
- New section `start-state` with heading "The TD fixed point gets the start state's value exactly", holding the derivation and the `--start 250` output.
- Start-state, first sentences: replaced the "rounding accident at first" remark.
- Start-state, conclusion: replaced "pins ... and makes the staircase lopsided" with the narrowed statement and the Figure 9.2 comparison; "other steps" → "other weights".
- Runs, P1: "each run ends near its fixed point" → "a run can only end near its method's exact weights".
- Takeaway: "ignores that" → "ignores that dependence"; replaced the closing recap with the reason and the two findings.
- Rebuilt with `scratch/assemble.py` from `article.src.html`, then `nb stamp` (4,385 words, 19 min, 3 sources), then `scratch/finalize.py` for the byline. No listing or output changed.

## Decision

approve. The argument holds, every claim on the page is derived, sourced or printed, and no change remains for the writer.

Proof: `nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` gives BLOCK 0, WARN 0, PUBLISHABLE, with and without `--check-links`.
