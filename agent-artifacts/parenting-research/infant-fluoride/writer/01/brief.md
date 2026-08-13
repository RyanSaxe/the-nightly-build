# writer brief: parenting-research/infant-fluoride (01)

Inputs:
- editorial-direction.md (house standard, slop, headlines, press voice, article
  template identity, series prompt) — at the artifact root
- commission.md (the two household decisions, the evidence spine, the required
  close, the do-not-let-policy-take-over boundary) — at the artifact root
- writing-coach/01/voice-guide.md (how this piece should sound)
- researcher/01/evidence.md (the complete set of claims; use its Numbers section
  exactly)
- the initialized article: library/parenting-research/infant-fluoride.html
- template context under .nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/parenting-research/infant-fluoride/library/parenting-research/infant-fluoride.html --series parenting-research --library /home/user/library-checkout

This round's substance (from the evidence record): two decisions frame the piece
— fluoride toothpaste (a smear from the first tooth) and fluoride supplementation
(which depends on water-fluoride level). Two bounds the evidence forces you to
carry honestly: (1) no trial in the Cochrane toothpaste or varnish reviews
enrolled a child under age one, so the "start at first tooth" guidance for a
six-month-old is guideline extrapolation, not direct trial evidence, and none of
AAP/ADA/USPSTF says so; (2) as of 2025-10-31 the FDA has recommended against
ingestible fluoride drug products for children under three, which conflicts with
the AAP/ADA/CDC supplement schedule that remains standing guidance for a
fluoride-deficient-water household — treat this conflict as substantive on the
supplementation decision, not as background. Keep the water-fluoridation policy
dispute as brief context only. Weigh the fluorosis evidence honestly (risk tracks
concentration, not start age or amount, per the newer Cochrane review).

Recent shapes to break (from the commission): recent parenting pieces close on a
"From the trials to this child" / "what to act on, what to leave to a
pediatrician" heading with an nb-note + nb-note-strong stack. Keep the required
substance (what the evidence changes at home; when it is a matter for a
pediatrician or dentist), but do not build the closing heading or phrasing on
that mold, and vary the furniture if the material allows. Find this piece's own
finding for the headline.

nb-meta: date "2026-08-13", harness "claude-code-routine", model "claude-sonnet".
Run `nb stamp` before the final links-checked proof.
