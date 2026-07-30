# Editorial review — company-analysis/boeing (editor invocation 01)

Skeptic: thesis "Boeing's Q2 2026 operational recovery is real, but the reported
swing to positive operating cash flow is a customer-advances (working-capital)
inflow, not delivered-jet margin, and free cash flow for the half is still
negative $823M"; tested 4 claims; broke: none.
- Claim 1 (the swing is the advances line). Recomputed from the owning primaries:
  H1 2026 operating cash flow $1,185M [S3 10-Q; also S1 release]; change in advances
  and progress billings +$4,660M [S3, cash-flow statement working-capital line];
  inventories $(3,859)M [S3]; the advances inflow alone exceeds the whole $1,185M.
  Ex-advances: $1,185M − $4,660M = $(3,475)M ≈ "$3.5B" used; year-ago $(1,389)M −
  $(616)M = $(773)M ≈ "$0.8B". Both check. Holds.
- Claim 2 (free cash flow still negative). $1,185M − $2,008M capex = $(823)M [S1
  defines FCF and reports the figure; S3 owns the GAAP components]. Q2 alone +$631M
  vs $(200)M a year ago [S1]. Holds; the piece does not overstate the quarter.
- Claim 3 (seasonality; not one green quarter). Q1 2026 FCF $(1.5)B [S6]; FY2025 FCF
  $(1,877)M [S7]. The half is $(823)M. Directionally and arithmetically correct.
- Claim 4 (advances build is steady, not a blip). $59,404M (Dec 31 2025) → $62,591M
  (Mar 31 2026) [S5] → $64,059M (Jun 30 2026) [S3]. Verified against both filings.
- Scope check: the waterfall and "$435M net loss" use the six-month total net loss
  [S3]; the orientation's "$444M net loss" is the Q2 figure attributable to
  shareholders [S1]. Different periods, each labeled correctly; no conflict.
- data-nb-kind audit: S1, S3, S4, S5, S6, S7 primary (Boeing's own SEC filings and
  self-statements); S2 (AeroTime) and S8 (FlyingMag) secondary. No Boeing financial
  figure rests on a secondary: S8 carries only the FAA 737 production cap (a
  regulator's action, context), S2 only the "recovery" framing the piece then
  tests. GAAP working-capital lines cite the 10-Q; the non-GAAP free-cash-flow
  figures cite the releases that define them. Correct.
- Headline/dek as claims: headline "…customer deposits, not delivered jets" is a
  defended claim with one earned contrast, no colon-subtitle, no question. Dek
  states a fact about the world ($4.7B advances > all reported operating cash;
  FCF still $823M negative), not a grade of the piece; no banned dek mold. Both
  pass spec/headlines.md.

Cut: 1 sentence recut (no net deletion); worst tell: a three-clause semicolon
chain ("…by themselves; the inventory build…; everything else…"), which the house
punctuation standard bans. Fixed directly to a period plus a single "and" join. Ran
the delete test across the piece: no self-grading, no stock-revelation frames ("the
real story is / the catch is"), no signposts narrating the article, no reader
address. "The question is what produced the cash" sets up the analysis the piece
actually performs and survives. Checked all authored text against the writer brief:
no prompt leakage — the section heading "Borrowed from future deliveries" and terms
like "delivered-jet margin" are the argument's own nouns, not copied instructions
or planning labels. Em-dash use: none; the one remaining semicolon ("Cash arrives
early; the obligation is settled later, in airplanes") joins two tightly bound
clauses and is within the standard. Headings reconstruct the argument and vary in
shape. Furniture audited: the stat strip, the H1 comparison table, the waterfall,
and the single Verdict note each carry evidence and none makes the page a stack of
blocks; the chart image and its chart-1.py provenance are honest (labeled axis,
values match the primaries, the +819 "all other" bar is a stated identity plug).

Reader: this gives me a reconciliation the filings never assemble — that Boeing's
entire year-over-year operating-cash improvement is the customer-advances line, that
underneath it the business consumed ~$3.5B of cash on an inventory build, and that
after capital spending the half still burned $823M — so I can judge for myself
whether a "positive cash quarter" is delivered-jet margin or a deposit against jets
not yet built. That matches the writer's original-work sentence, and the piece
delivers it in the filings' own numbers. The voice is calm and first-principles,
grounded in a specific figure at every turn, closer to the guide's exemplars
(Damodaran's skepticism-then-materiality, Rubinstein's read-the-liability move) than
to a median summary. Reread the headline as the largest claim: it commits to
exactly what the body proves.

Direct edits made: split two 42/43-word dense sentences (writer, in proof round);
replaced one three-clause semicolon chain with a period and a single conjunction.
No new prose was written past a clause.

Required work by owner: none.

Decision: DONE. No redraft required. Post-edit proof: BLOCK 0, WARN 0, verdict
PUBLISHABLE.
