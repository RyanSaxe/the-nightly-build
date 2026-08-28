# writer brief: tech-news/2026-08-28 (01)

Inputs:
- editorial-direction.md — house standard, citation rules, press voice, series prompt (artifact root)
- commission.md — assignment, edition boundaries, recent habits to break (artifact root)
- writing-coach/01/voice-guide.md — how this brief should sound
- researcher/01/evidence.md — the complete verified claim set; select the final 4-6 items from it
- the initialized article: .nb-work/tech-news/2026-08-28/library/tech-news/2026-08-28.html
- template context under .nb-work/tech-news/2026-08-28/.nb-context/

Output: .nb-work/tech-news/2026-08-28/agent-artifacts/tech-news/2026-08-28/writer/01/draft-handoff.md
Proof: ./nb check .nb-work/tech-news/2026-08-28/library/tech-news/2026-08-28.html --series tech-news --library /home/user/library-checkout

Select the final four to six items by significance from the evidence. Where the
evidence marks a figure or claim UNVERIFIED (no owning primary), either drop the
item or state the uncertainty plainly in the item — never present an aggregator
claim as fact. Each item stands alone with a primary link and an independent
secondary, and stops on its own detail (the brief template bars a reader-facing
closer).

Selection steer (from the evidence report):
- Lead on the AWS–NVIDIA 2M-GPU expansion (Aug 26): the one candidate both
  primary-sourced and on-date.
- Treat Nvidia–Hugging Face (~$13B) and Broadcom's $60–80B AI-debt raise as
  reported-but-unconfirmed: single-origin/anonymous, no primary, unconfirmed by
  the companies. Drop them, or include only with the uncertainty stated plainly
  as the item's substance. The Broadcom–Anthropic backstop an aggregator
  attributed is NOT in Broadcom's 10-Q — do not repeat it.
- The Nevada robotaxi story fits this brief (AV tech reaching public roads). State
  it precisely: the firsthand NTA permit caps Tesla at ten vehicles on the Strip;
  the 5,000/8,000 ceilings are secondary-sourced from the later full approval,
  with no primary retrieved. Do not present the big number as fact.
- The OpenAI math-proofs manuscript is ~4 weeks stale (dated Aug 1); treat it as
  prior news to build on, not the day's development, if used at all. "Astra" and
  the ~$2,000 cost are secondary labels, not the paper's.
- Keep Nvidia's Aug 27 earnings OUT: that is a markets story, not this brief.

Recent habits to break (detail in commission): the desk has over-leaned on
AI-security and model-release framings — the day's weight is on chips/infra and
robotics, so lead there. Vary the dek from the two-clause "X, and Y" build.
