# writer brief: parenting-research/infant-fever (01)

Inputs (paths relative to the workspace root `.nb-work/parenting-research/infant-fever/`):
- `agent-artifacts/parenting-research/infant-fever/editorial-direction.md`
- `agent-artifacts/parenting-research/infant-fever/writing-coach/01/voice-guide.md`
- `agent-artifacts/parenting-research/infant-fever/researcher/01/evidence.md` — the complete claim set, figures in absolute terms
- `agent-artifacts/parenting-research/infant-fever/commission.md` — the question, boundaries, habits to break
- `library/parenting-research/infant-fever.html` — the initialized article to edit in place
- `.nb-context/` — effective template contract (article) and furniture catalogs

Output: `agent-artifacts/parenting-research/infant-fever/writer/01/draft-handoff.md`

Proof (from repo root, workspace-prefixed; iterate with `--no-check-links`, links on until BLOCK: 0):
`./nb check .nb-work/parenting-research/infant-fever/library/parenting-research/infant-fever.html --series parenting-research --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check.

Evidence cautions to honor (from the researcher):
- The febrile-seizure non-prevention finding is the sharpest correction, but Strengell 2009's arms are badly unbalanced (197 antipyretic vs 34 placebo). Lean on the guideline consensus (AAP 2008 and AAP 2021 both back it), not one trial presented as decisive. State what the trial alone can and cannot rule out.
- The folk belief that antipyretics prolong the illness is unsupported: Purssell & While found fever cleared about 4 hours faster with antipyretics (pooled MD -4.16 h). The honest read is that they neither meaningfully shorten nor lengthen the illness. Record the tension with AAP 2011's own hedge that fever may help recovery.
- Combining/alternating acetaminophen and ibuprofen genuinely lowers temperature more (PITCH; Cochrane ~0.70°C at 4 h) but no trial showed a comfort benefit, and guidelines decline to endorse routine combining because comfort is the endpoint and misdosing is common (~half of parents misdose). This guideline-versus-thermometer conflict is worth landing plainly.
- The young-infant emergency threshold is 38.0°C (100.4°F) rectal, identical across AAP 2021 and NICE. The "softening" across 3-6 months is a change in guideline category, not a single new bright line; do not invent a clean number for the 3-6 month band. Mark the warning signs as clinician/emergency matters.
- Give every figure in absolute terms with its denominator. Ibuprofen's lower age limit is from the OTC label.
- Some guideline owner pages return 403 to fetching (restricted, not dead); the link check will not block on those. Cite each source's own canonical page as the evidence record records it.

nb-meta: set `date` 2026-08-16, `harness` `claude-code-routine`, `model` `claude-opus`, `tags` []. Keep nb-meta `dek` identical to the rendered dekline.

Boundaries: research desk, not individual medical care. End on what the evidence might change at home and where a specific situation is a pediatrician or emergency matter. The threshold and warning signs are safety lines.

This round's focus (recent parenting-desk shapes to break, per the commission):
- Recent pieces open on "the guidance rests on trials that do not fit this baby / the evidence settles only X." Do not open on that mold.
- Recent pieces close on the two-sentence "X is settled. Y is not." form with a holds-up block. Vary the closer from that couplet.
- The absolute-versus-relative-risk move fits the febrile-seizure numbers; use it once, plainly, without making it the article's signature.
