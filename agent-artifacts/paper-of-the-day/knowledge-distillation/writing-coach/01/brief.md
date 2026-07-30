# Writing-coach brief — paper-of-the-day/knowledge-distillation (01)

## Your task
Study how the best expository writers on machine learning reconstruct a
technical idea, and turn it into a practical voice guide for this one article.
Produce `voice-guide.md` in this directory. Do not restate the subject, the
findings, or template rules.

## Exact inputs
- This brief.
- `editorial-direction.md` (house floor, headline standard, press voice,
  template identity, series prompt) in the artifact root. Read the press
  "Voice" and "Reader" sections: baseline register is Mitchell Hashimoto's
  technical writing (calm, first-principles, structure persuades); where the
  piece teaches, take the patience of Chris Olah and Lilian Weng and build each
  concept before the sentence that needs it.
- The named outputs: `voice-guide.md` only.

## The article, in one line (for craft calibration only)
A `paper` reconstruction of Hinton, Vinyals & Dean 2015 ("Distilling the
Knowledge in a Neural Network"), rebuilding the temperature-softmax / soft-target
mechanism, then weighing it as a reviewer against a 2021 measurement that found
students rarely match the teacher's predictive distribution. Register: house
reader (graduate ML, comfortable with softmax, logits, gradients).

## What the craft has to do here
- Teach a mechanism from first principles (a temperature-scaled softmax, soft vs
  hard targets) so the concept is built before the sentence that spends it.
- Then turn skeptical: hold a beloved 2015 intuition against 2021 evidence and
  land a reviewer's verdict without hedging or manufactured drama.
- Handle equations and numbers as prose the reader reads, not decoration.

## Study at least three writers the field itself rates
Real technical/ML expositors, primary pieces, not commentary or influencers.
Chris Olah and Lilian Weng are named by the press voice; add at least one more
genuine ML expositor. Read each as a writer studies a writer. Cite each with a
real, resolving URL on a `Source:` line.

## Constraints
- Extract transferable craft, never a persona, catchphrase, or reusable line.
- End the lead directive with `Recently used, do not reuse:` carrying the habits
  the commission flags: the "the paper's own table/proof already recorded the
  limit" opener; the bare "weigh the claim against the follow-on" spine as a
  visible scaffold; colon-subtitle headlines; the banned dek molds (semicolon
  reversal, suspended question, comma triad); heading cadence that keeps joining
  two clauses with a comma and "and".

## Return
`DONE writing-coach <voice-guide-path>` after writing the file, or
`REQUEST orchestrator <one-sentence need>`.
