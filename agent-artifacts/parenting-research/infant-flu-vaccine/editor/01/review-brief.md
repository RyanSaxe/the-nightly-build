# editor review-brief: parenting-research/infant-flu-vaccine (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/commission.md
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writer/01/brief.md
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/researcher/01/evidence.md
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/writer/01/draft-handoff.md
  Article: /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/library/parenting-research/infant-flu-vaccine.html
  Template context: /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/.nb-context/

Output:
  /home/user/the-nightly-build/.nb-work/parenting-research/infant-flu-vaccine/agent-artifacts/parenting-research/infant-flu-vaccine/editor/01/editorial-review.md

Round focus: this is a medical-evidence piece, so push hardest on the numbers and
what each study design can support. Recompute and check against the owning primary
every effect size, confidence interval, and denominator: the Cochrane inactivated
RR ~0.36 and LAIV RR ~0.22 (and that LAIV is correctly excluded at this age), the
Hoberman 66%-to-minus-7% season swing, the pooled maternal ~35% (CI 19-47) waning
to a CI-crossing ~19% by 4-6 months, and the febrile-seizure IRR ~3.5 with the ~30
per 100,000 absolute excess. Confirm absolute and relative measures are never
conflated, that cocooning carries no efficacy number, and that no claim rests on
the 2026-27 MMWR as an unread page. Inspect the table and the chart: the chart's
committed provenance (chart-1.py) and its numbers must match the evidence record
and cited primary, and its axes/scale must be honest; route any chart correction to
the writer, who holds the tooling.

Recent-pattern notes to compare edges, dek, and headings against (catch formula):
- The last parenting pieces leaned on deks built as "the evidence settles X and
  little else" and "X does Y, and by Z in a hundred" (large-relative/small-absolute).
  The absolute-vs-relative move may be honest here, but flag it if the dek or a
  heading is built to the prior wording.
- The last piece opened on "The child turns six months old this August"; confirm
  this one does not reuse that entry.

Open every citation href as printed and confirm it lands on the source's own page
(note: several primaries are gated and were verified via PubMed/PMC mirrors — the
printed href should be the source's own page per the evidence record).
