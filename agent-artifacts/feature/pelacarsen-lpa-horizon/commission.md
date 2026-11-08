# Commission: feature/pelacarsen-lpa-horizon

Authorized by `nb duty` for 2026-11-08: open section `feature`, no commissions queued, "choose a topic within the beat; do not repeat a published slug". Template `article`, strict, 600 to 1,200 words, two to four flex sections, at least five sources.

## Topic and why now

Novartis's pelacarsen, an antisense drug that lowers lipoprotein(a), failed the primary endpoint of its phase 3 outcomes trial, Lp(a)HORIZON. Full results were presented at the American Heart Association's Scientific Sessions on 7 November 2026 and, per early coverage, published the same day in the New England Journal of Medicine. Novartis had announced the miss on 4 September 2026. Coverage reports a 78% fall in Lp(a) on the drug and no difference in major cardiovascular events over almost five years. No published article in this paper covers Lp(a) or pelacarsen (checked with `nb history`).

## The question the piece answers

Lp(a) was the case genetics made. Mendelian randomization studies estimated how large a reduction in Lp(a) should be needed for a given cut in coronary risk, and they expressed it in absolute terms (mg/dL or nmol/L), not as a percentage. The piece puts the absolute reduction pelacarsen achieved in this population next to the reduction those genetic estimates said would be needed for a detectable effect, and next to the trial's own powering assumptions. The reader comes away able to say whether a null result here contradicts the genetic evidence, or whether the trial tested a smaller dose of the hypothesis than the 78% suggests. Settle which from the documents.

This is the angle to test, not the conclusion to reach. If the NEJM paper or the investigators show that the absolute reduction was large enough that the genetics predicted a clear benefit, then the null result is a contradiction of the genetic case and the piece says so. Find what would break each reading: subgroups by baseline Lp(a), on-treatment achieved levels, the per-protocol or on-treatment analysis, adherence and dropout, the placebo-arm change, LDL and background therapy, and any statement by the investigators or Novartis on why.

## Required contribution

The piece does arithmetic the sources do not: the trial's achieved absolute reduction, in the units the genetic estimates use, set against those estimates. Units matter. Lp(a) in mg/dL and nmol/L do not convert by a fixed factor because particle size varies, so the piece states which unit each figure comes in and does not convert unless a source gives the basis.

It also names what comes next: the other Lp(a) outcome trials (Amgen's olpasiran in OCEAN(a)-Outcomes, Lilly's lepodisiran, and others the researcher confirms) with their enrollment thresholds and expected readout dates from their registry entries, so a reader can see which of them enrolled people with higher Lp(a) or targets a larger absolute reduction.

## Visuals

Each section builds around a visual, per the series prompt. Candidates the material should support: the trial's primary-endpoint curves or hazard ratio from the NEJM paper, a drawing comparing achieved absolute reduction with the genetic estimates, and a comparison table of the pending outcome trials. A drawing of how an antisense drug and an siRNA reduce apo(a) production in the liver is allowed only if the argument uses it. Use `nb asset` for a figure from the paper where the original shows the idea best and the source permits capture.

## Boundaries

- Do not write a general explainer on Lp(a) or a health-advice piece. The audience is technical, not clinical: introduce only the clinical context needed to follow the argument.
- Do not attribute motives. Report what the investigators, Novartis and named outside cardiologists said, with their exact titles.
- Avoid the recent feature pattern of deks that open with a framing prepositional phrase ("By METR's arithmetic,", "Sorted by the price each one measures,", "Across a CMU preprint's...", "Priced at Marvell's 28 October close,"). Four of the last seven deks open this way.
- Avoid the recent headline shape "X does A and B the rest" with two contrasting halves joined by "and" ("agree on wholesale costs and split on household rates", "froze ... and had no reach over the rest").

## Neighbours in this edition

The Daily Brief of 2026-11-08 leaves this story out. The Reinforcement Learning lesson trains an off-the-shelf agent on a gridworld. No overlap.

## Production

Profile balanced. Writing coach: capable tier (Sonnet), low effort. Researcher: capable tier (Sonnet), high effort. Writer: capable tier (Sonnet), high effort per the series. Editor: inherited model (the orchestrator's), high effort, required. Harness: Claude Code, cloud session.

## Decision after researcher/01

The evidence settles the angle against the "smaller dose than 78% suggests" reading. The derived absolute fall (about 66 to 84 mg/dL, depending on method, labelled as derived in the record) is at or above Lamina and Kronenberg's 65.7 mg/dL and below Burgess's 101.5 mg/dL. The NEJM Evidence landmark analysis shows no gradient by size of fall or achieved level. The confidence interval for the primary endpoint excludes a 20% reduction. The piece therefore reports that the trial lowered Lp(a) by roughly the absolute amount the genetic estimates tie to a clinically meaningful benefit and ruled out that benefit over 4.7 years. It names duration (lifelong genetic exposure against 4.7 years of treatment) as the open explanation, attributes it to Nissen as his explanation, and states that no source quantifies it. The derived mg/dL range and any scaling are labelled as the article's own arithmetic, with the method stated. Neither "contradicts the genetics" nor "dose too small" is presented as settled. NEJM itself could not be opened; cite the documents that were opened and say nothing a reader would take as quoting the paper directly unless a source reproduces it. The pending-trials table uses the registry records the researcher found (four trials, with thresholds in nmol/L).

## Decision after editor/01

Accepted: the treatment-scale prediction stays, because it rests on the genetic papers' own equivalence to a 1 mmol/L LDL cut and the statin-trial meta-analysis's 0.78 for that cut, not on an article-made discount. The headline keeps "as far as one genetic study required": every derived value reaches Lamina and Kronenberg's 65.7 mg/dL, and the dek states the derived range.
