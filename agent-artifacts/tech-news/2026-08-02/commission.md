# Commission: tech-news/2026-08-02

## Assignment
The daily technology front page for **2026-08-02**. A `brief`: 4-6 items, each a
judgment about why a development matters. AI is central, but significance decides
the mix. Product promotion, incremental releases, and online attention do not
qualify on their own. Science and health belong when a result changes technical
knowledge or practice enough to deserve attention here.

## Reader / mode / template
House reader (ML-engineering background, well-read). Mode rolling; template
`brief`. Per-item citation: the development + a link to its **primary** source
(the original paper, release, filing, or announcement, over any coverage) plus
**at least one independent** account.

## Candidate leads (VERIFY and DISCOVER; slate is not fixed)
This is a same-day brief; discovery is the researcher's job. Confirm each against
its primary, drop stale/thin items, and find the day's genuinely most
consequential technology developments. Escalate the final slate if a swap
changes the brief's character.
- Recent signals (verify dates; many may be late-July and stale for 08-02):
  OpenAI field report on coding agents modernizing research software (claimed
  speedups up to 60x) with academic partners; Anthropic's open-weights position
  and expanded Cognizant enterprise partnership (~07-27). Use only if a genuine
  08-02 development or clearly still the live story.
- Look for 08-01/08-02: frontier-model releases or evaluations with independent
  benchmarking; consequential research (ML, or science/health that changes
  practice); chips/compute; security disclosures with real impact; major
  regulatory or standards actions in tech.
- Prior tech-news (07-26..08-01) covered: Claude's HAWK/post-quantum
  cryptanalysis finding; Ruflo agent RCE (CVSS 10); Nvidia AI-security alliance;
  Nvidia-SSI investment; Kimi K3; an OpenAI model's unprompted HuggingFace hack.
  Advance these only where they moved; do not re-report. Avoid another
  "model finds crypto weakness" or "agent RCE" item unless materially new.

Aim for 4-6 items that each clear the bar; run fewer strong items over padding.

## Source obligations
- Template floor: **minimum 5 sources total**; **per item exactly 1 primary + 1+
  independent secondary**. For a research result, the paper/preprint is primary;
  independent testing or reporting is the secondary. Verify benchmark numbers
  against the primary; note when a vendor's own chart omits an unfavorable figure.
- Every URL resolves; a paywall/403 is gated, try a browser fetch. Verify model
  names, versions, org names, and figures exactly.

## Structures not to inherit
Recent briefs lead with an AI-safety/security incident and stack AI items. Vary
the lead by significance; include a genuinely non-security item if the day
supports it. Vary item openers; no formulaic kicker; no handoff-to-reader closer.

## Neighboring articles tonight
current-events brief (public-consequence stories live there; keep tech-*field*
here), word-of-the-day, paper-of-the-day (the paper desk covers one older ML
paper in depth — do not duplicate its subject), investing, parenting. Coordinate
with current-events so no item runs in both.

## Output paths
- Article: `.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html`
- Artifacts under `agent-artifacts/tech-news/2026-08-02/`.

## Harness / model (balanced profile)
harness `claude-code`; writing-coach `claude-sonnet-5`/low; researcher
`claude-sonnet-5`/high; writer `claude-sonnet-5`/medium (record in nb-meta);
editor `claude-opus-4-8` (inherit)/high, required.
