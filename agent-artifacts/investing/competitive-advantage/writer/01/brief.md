# writer brief: investing/competitive-advantage (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/agent-artifacts/investing/competitive-advantage/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/agent-artifacts/investing/competitive-advantage/commission.md  — the concept, its place in the course, boundaries, and habits not to inherit
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/agent-artifacts/investing/competitive-advantage/writing-coach/01/voice-guide.md  — how this lesson should sound
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/agent-artifacts/investing/competitive-advantage/researcher/01/evidence.md  — the complete claim set; treat as evidence, not prose
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/library/investing/competitive-advantage.html  — the initialized article to edit in place
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/.nb-context/  — effective template contract and furniture catalogs

Output:
  /home/user/the-nightly-build/.nb-work/investing/competitive-advantage/agent-artifacts/investing/competitive-advantage/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/investing/competitive-advantage/library/investing/competitive-advantage.html --series investing --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

nb-meta: set harness to "claude-code-routine" and model to "claude-opus-4-8"; fill
dates; nb stamp writes the counts.

This round's focus, from the evidence record:
- Build the worked example on Copart (salvage-auction network, scarce permitted
  land, scale; ~30% ROIC) against Crocs (footwear brand exposed to taste; ~27% in
  FY2024). In the fade calculation, hold ROIC and growth equal by construction and
  vary only the fade of excess returns, so the reader sees durability, not the
  starting level, doing the work. The two firms are not at an identical real ROIC
  or in one industry, so make the "same ROIC, same growth, different fade" step an
  explicit modeling choice, not a claim that they are identical.
- Use Crocs's real fade evidence rather than a hypothetical: the 2007-to-2009
  operating collapse and the $737M HEYDUDE write-down on a brand it bought for
  $2.3B. Use it to make durability concrete.
- Present mean reversion as a wide-variance tendency, not a schedule: staples fade
  slowly, exposed businesses fast. Do not present fade as automatic.
- Keep the humility the concept demands: identifying a moat in advance is genuinely
  hard (Buffett's own Dexter Shoe misjudgment; Crocs looked high-return at its 2007
  peak). This sharpens the lesson; it does not undercut it.
- Buffett's durable-moat framing is from the 2007 Berkshire letter; use it
  verbatim where quoted. Costco does not anchor the example (the course leaned on
  it); it may appear only inside a verified Buffett quotation.
- Connect the fade assumption back to the DCF terminal value the course already
  taught. Do not open on a definition; enter through the problem the fade
  assumption creates. The `why` and `takeaway` bookend cards may address the
  reader; the body may not. Avoid the recent lesson dek and heading molds named in
  the commission, and pick fresh headings in this lesson's own nouns.
