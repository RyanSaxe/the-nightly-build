# Editorial review: investing/valuation-multiples (editor/01)

## Skeptic

Thesis: a valuation multiple is a discounted cash flow compressed into one
number, so growth, return on capital, and risk are the only things a multiple
prices, and a low multiple is therefore a claim about a business, not a verdict
that it is cheap. The claims it stands on:

1. The headline claim, that every multiple hides a DCF. Damodaran's Relative
   Valuation notes (s1) state it outright: embedded in every multiple are all
   the variables that drive a discounted cash flow valuation. The derivation
   section then shows the mechanism for the P/E. The claim is owned by a primary
   authority and demonstrated in the body. It holds.

2. The derivation, that the justified forward P/E is (1 - g/ROE)/(r - g). Traced
   to s2 (Ch. 18) and the evidence's formula block: forward P/E = payout/(r - g)
   with payout = 1 - g/ROE. The article's two figures reproduce this exactly. The
   verbal restatement in the takeaway ("one minus growth over return on equity,
   all divided by risk minus growth") matches. Holds.

3. The worked contrast across NVIDIA, The Coca-Cola Company, and Verizon. This is
   the claim I pushed hardest on, recomputing every figure against the evidence's
   Numbers and each owning filing:
   - NVIDIA: last-FY P/E 45.7 ($223.96 / $4.90), trailing 34.3, forward 22.4;
     ROE 76.3% (120,067/157,293); op margin 60.4%; revenue +65%. Every figure
     printed with its denominator. Correct.
   - Coca-Cola (KO, not COKE the bottler): P/E last-FY 28.6 (87.05/3.04),
     trailing 26.2; ROE 40.7% (13,107/32,169); revenue +1.9% reported / +5%
     organic; op margin 28.7%. The prose correctly names "The Coca-Cola Company"
     on first use and the dek's "41 cents on the equity dollar" matches ROE.
     Justified plug (1 - 0.04/0.41)/(0.07 - 0.04) = 30.1, and the draft says
     "near 30." Correct.
   - Verizon: P/E last-FY 11.6 (47.06/4.06), trailing 12.3; ROE 16.4%
     (17,174/104,460); revenue +2.5%; EPS fell to $4.06 from $4.15; net income
     attributable slipped to $17.2B from $17.5B; ~$158B debt; $17B capex.
     Justified plug (1 - 0.025/0.16)/(0.085 - 0.025) = 14.1, and the draft says
     "about 14." Correct.
   All three-company table cells match the evidence's worked-contrast table.

4. The safe-claim boundary, that the derivation yields the multiple a business
   *deserves* and does not prove the market's quoted multiple equals it. This is
   the round's central correctness watch-item and the draft carries it honestly.
   KO's justified ~30 is called "in the neighborhood of what the market quotes"
   and its r and g are owned in prose as the researcher's estimates that move the
   answer. Verizon's ~14 is "close to what the market pays" and "roughly where
   the observed one sits." The cheap-is-not-cheap section then states the caution
   directly: the formula "does not prove the market's quoted multiple equals that
   number," and relative valuation inherits whatever mispricing sits in its
   comparables. No sentence claims observed = justified. Holds.

Denominator discipline: every multiple in the running text, the stat strip, both
table columns, the opener, and the takeaway carries its denominator (last full
year / trailing / forward). No bare multiple survives. The watch-item is met.

Display text, descriptor by descriptor: headline is a committed claim supported
by s1; dek makes a world-claim (ROE gap justifies a ~2x multiple spread) with
correct figures and no banned mold; every subhead is an argument step in the
piece's nouns. The dek isolates the ROE gap as the justifier while the body
notes risk (r) also pulls Verizon down; "the kind of gap" hedges this to an
illustrative claim, so it is defensible, not a false label. Reviewed, kept.

Sourcing: six sources, five primary (Damodaran x2, NVIDIA release, KO 8-K, VZ
FOI) and one secondary (stockanalysis.com). The one secondary is correctly
`data-nb-kind="secondary"` and its note explains the split cleanly: the market
owns the price and the ready-made trailing/forward P/E, this source reports them.
The filing-owned fundamentals are all on primaries. No kind is mislabeled and no
missing independent source is hidden behind a wrong label. Citation-to-claim
mapping spot-checked at the load-bearing figures (NVIDIA EPS to s3, prices and
ready-made P/E to s4, KO equity/net income to s5, Verizon EPS/debt to s6) and
each lands on the owner. `nb check` with links passed at BLOCK: 0, so the printed
hrefs resolve.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routes to the researcher.

## Cut

One dedicated slop pass over every sentence including display text and furniture
prose. The findings:

- **Voice-guide leakage.** The three-companies section opened "A formula stays
  abstract until it is spent on a real case," which is the voice guide's own
  instruction ("A derived formula stays abstract until it is spent on a real
  case") copied almost verbatim into the article. It is also a bare signpost for
  what the section is about to do. Cut; the section now opens on the concrete
  "Take three businesses whose growth alone spreads them far apart."

- **Unearned punchline.** The justified-multiple note ended "and the gap between
  the two is the whole reason to do the work," an instance of the "X is the whole
  Y" family named in spec/slop.md. The point (the gap is what the derivation is
  for) is already made where the derivation is introduced. Cut the trailing
  clause; the note now ends on the clean distinction it exists to draw.

- **Negative-parallelism density.** The "not X, it is Y" construction is the
  paper's most common tell, and this draft leaned on it hard, with three
  instances clustered in three consecutive paragraphs of the climactic
  cheap-is-not-cheap section. Because the misconception each corrects (low
  multiple = cheap) is the lesson's named subject, spec/slop.md exempts the
  contrast in principle, but the cluster read as a tic. I cut the two most
  redundant closers, both of which failed the delete test (each only restated
  "the low multiple is deserved by weak fundamentals," which the section's real
  conclusion already carries): "The low multiple is not a discount to Verizon's
  fundamentals. It is a fair reading of them," and "A shrinking numerator sitting
  on a heavy balance sheet is not value hiding behind a low multiple. It is a low
  multiple doing its job." The remaining contrasts (multiples vs DCF in the
  opener, the inputs folded into the multiple, justified vs observed in the note,
  hypothesis vs verdict in the caution, the takeaway's cheap/dear line) are each
  load-bearing, tied to the subject, and spread across the whole piece. Reviewed
  and kept; the density is now within reason.

- **Signpost and self-grading.** The caution paragraph opened "One caution keeps
  this honest, and it is the difference between a useful tool and a dangerous
  one," which announces a caution is coming and grades the stakes without stating
  the caution; the real caution is in the sentences that follow. Cut. And "The
  safe claim is the narrow one, and it is still strong" self-graded the claim;
  trimmed to "The safe claim is the narrow one," keeping the teaching frame
  (narrow on purpose) and dropping the self-grade.

Six direct cuts in total. No sentence needed a rewrite: each removal left the
paragraph ending on its harder factual or argumentative sentence.

Recent-pattern check. The draft does not open on the DCF lesson's share-of-value
number, and it does not close on a "tool broken or the hand" turn; the takeaway
closes on "you are reading the discounted cash flow the multiple was hiding all
along," a distinct shape. It anchors on NVIDIA, Coca-Cola, and Verizon, not
Costco or Apple; the sole Apple mention is a Background cross-link to a prior
lesson, which is correct. Headings are argument steps in the piece's nouns with
no scaffolding slots. Bookends: Why-this-matters situates the reader in the
course and poses the Verizon question this lesson answers; The takeaway resolves
exactly that question with this lesson's figures. Both are specific to this
lesson and would not transport to another; they meet the template's own belongs-
only-here test. The required furniture (bookends, Sources) is furniture, not
formula.

Register: the prose holds the voice guide's calm, term-defining, objection-
anticipating register throughout ("The market already quotes a multiple, so why
derive one from a model?"; "Cheap compared to what?"). No flattening was needed
and none was introduced.

Grammar and syntax across body, display text, and furniture: clean; no breaks
found. Punctuation is period-led; the one semicolon (comparables / whole-sector-
dear) joins two tightly bound independent clauses and is a defensible rare use,
not a required fix.

## Reader

Read straight through, what the piece gives beyond its sources: the sources hold
the definitions, the formula, and each company's filing separately; the article
sorts the three companies into "the single-stage formula explains this" (KO and
Verizon, both plugged and landing near their quotes) and "the formula would
misprice this" (NVIDIA, deliberately not plugged, its multiple diagnosed instead
through the trailing-to-forward gap as the fingerprint of two-stage growth). That
sorting is a judgment the evidence supplies parts for but does not itself make,
and it matches the original-work sentence in draft-handoff.md. A reader finishes
able to read any multiple as an encoding of growth, ROE, and risk, and to treat
"low" as a hypothesis to test rather than a discount. That is more than the
sources alone give. The prose sits closer to the voice-guide exemplars than to a
median summary. The headline, reread as the largest claim, is true and owned by a
primary.

No chart and no source asset. The writer's reasoning is sound: the verified
series is only three companies (a thin scatter), and the one genuinely teachable
curve, forward P/E against growth, would have to be drawn from the estimated r
and g the evidence says not to print as fact. The three-company table and the two
annotated equations carry the contrast on verified numbers. I do not request a
chart. The two math figures could not be eyeballed in a browser (no Chrome in the
environment, per the handoff), but their TeX matches the evidence's formulas
term for term; this is not publication-blocking.

## Edits

- Cut voice-guide-leaked signpost "A formula stays abstract until it is spent on a real case." opening the three-companies section.
- Cut unearned-punchline clause "and the gap between the two is the whole reason to do the work" from the justified-multiple note.
- Cut redundant negative-parallel closer "The low multiple is not a discount to Verizon's fundamentals. It is a fair reading of them."
- Cut redundant negative-parallel closer "A shrinking numerator sitting on a heavy balance sheet is not value hiding behind a low multiple. It is a low multiple doing its job."
- Cut signpost/stakes sentence "One caution keeps this honest, and it is the difference between a useful tool and a dangerous one."
- Trimmed self-grade "and it is still strong" from "The safe claim is the narrow one, and it is still strong."
- Ran `nb stamp`: 2105 words (band 1200-2200), 6 sources, 9 min. `nb check` with links: BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

None. All findings were resolved by direct surgical cut; no item routes to the
researcher, writer, or orchestrator.

## Decision

approve. The thesis is owned by a primary and demonstrated in the body, every
figure recomputes against its owning filing with its denominator named, the
justified-versus-observed boundary is held honestly, and the six cuts cleared the
leakage, the unearned punchline, and the negative-parallelism cluster without
touching the piece's math, markup, or voice.
