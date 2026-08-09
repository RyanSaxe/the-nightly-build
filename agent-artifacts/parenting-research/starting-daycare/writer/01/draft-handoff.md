# draft handoff: parenting-research/starting-daycare (01)

## Original work

One sentence: the piece puts all three evidence tiers on a single decision
axis, "does this finding change whether or when to enroll?", and shows that
only the front-loaded run of respiratory and ear infections clears it, because
the gastrointestinal excess nets to zero over six years, the famous asthma
protection fails to replicate in the larger cohorts, and the developmental
effects are too small and too confounded to weigh, so the choice returns to
family logistics and room quality rather than a lasting health verdict. The
work is visible in the closing section and the Verdict note, which rank the
tiers against that one test rather than restating each study.

## How the three corrections were carried

- GI effect: presented as small and net-neutral (IRR 1.13 in year one, 12.2 vs
  13.3 per 100 child-years over six years, null in Cote), with the older
  "threefold" review figure named and set against the prospective cohorts. No
  large near-certain GI claim.
- Asthma: carried as a shift in the timing of wheeze, not a durable asthma
  change. Ball/Tucson steelmanned first (RR 0.4, CI touching 1.0, one cohort),
  then Caudri (aOR 0.99) and Swartz (pooled 0.98, NS) weighed over it. Stated
  plainly that all of it is observational and no randomized evidence exists.
- Desk close: no group-care-avoidance guideline invented. Close built on what
  the AAP bronchiolitis guideline actually says (KAS 1b risk factors, hand
  hygiene, breastfeeding) and routes the high-risk infant to a pediatrician.
  The piece explicitly declines to issue an RSV-season avoidance instruction.

## Furniture

- Table (infection reversal, Cote + de Hoog): the respiratory/ear rate ratios
  crossing 1.0 from early to later windows.
- Chart (chart-1.py -> chart-1.png, forest plot from Swartz Tables 3-4): the
  asthma OR by age band, showing protection only at 3-5 and the wheeze
  sign-flip. Built from the evidence's verified pooled series; inspected.
- One plain note marks the randomized-vs-observational line; one strong Verdict
  note lands the decision.

## Proof

`nb check ... --series parenting-research --library <checkout>`: BLOCK: 0,
verdict PUBLISHABLE.

Warnings intentionally left: 2 x W-SENTENCE-DENSITY, both 41-42 word sentences
with 2 clause joins. One is the effect-size comparison for the developmental
d = 0.10 (a point and a half on an IQ-type scale, the gap that vanishes between
two classrooms); the other is a cited decision/recommendation sentence. Both
are controlled long sentences carrying data appositives that read as one
thought; splitting either would break the comparison it exists to make. Left
per the editorial standard's allowance for a long sentence under control.
Started at 8 density warnings; the other 6 were split.

## Open questions

- Evidence gap (recorded by researcher, not blocking): the exact standardized
  coefficient for hours-of-care predicting risk-taking/impulsivity at 15 was
  not captured to a number, so that effect is given as direction and magnitude
  ("modest", continuing the externalizing pattern), not a point estimate.
- Evidence gap: no accessible primary confirms a pediatric body advising
  high-risk infants to avoid group care in RSV season. Honored by not
  asserting one; if the editor has an accessible AAP 2025 RSV statement, the
  close could name it, but it should not be sourced from a secondary summary.
- No open voice question. The Nuzzo/Carroll/Gawande moves (caveat sharpening
  the number, naming the appraisal before weighing, arithmetic to a verdict)
  map cleanly onto the three tiers.
