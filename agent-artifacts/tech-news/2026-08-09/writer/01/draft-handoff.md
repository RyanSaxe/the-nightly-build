# Draft handoff: tech-news/2026-08-09 (writer 01)

## Original work

This edition audits the week's biggest claimed advances by what has actually
held up to outside checking as of Sunday: it leads with the one peer-reviewed
result (the rhombohedral-graphene superconductivity paper) and, for each vendor
claim the paper already broke as a weekday item, separates what the vendor did
from what still cannot be verified — Astra's Lean certificates against the
absence of any referee, and Qwen3.8-Max's specification against its still-unshipped
open weights. The ordering and each item's caveat placement are that act.

## Proof

`./nb check … --series tech-news --library <checkout>` (links included):
BLOCK: 0, WARN: 0, PUBLISHABLE. Stamp: 10 sources, 1040 words, 5 min.
No warning left standing.

The `nb render-check` visual probe was skipped: no Chrome in this environment.
The one furniture piece (an `nb-stat-strip` on the GPT-4 item) uses catalog
markup verbatim, so it renders from the engine CSS; it was not visually inspected.

## Editorial decisions worth the editor's eye

- Continuity. The daily paper already covered Astra (08-04), Qwen3.8-Max
  (08-05), and the AISI rogue-agent report (08-07). Per the brief, this Sunday
  edition still runs the two vendor items, written from the weekend vantage as
  build-on updates (Astra: checkable but unrefereed; Qwen: promised open weights
  now overdue) rather than as fresh breaks, and no item implies a story broke
  today. AISI was held out entirely — recapping a two-day-old lead adds nothing
  and would tip the mix back toward the AI-security beat the brief warns off.
- Lead. Graphene, not Astra. Astra was our own 08-04 lead; graphene is fresh to
  the paper, peer-reviewed, and non-AI-security, which the brief and the press
  both permit as the more consequential lead here.
- Lane separation held: the open-weights security-review exemption and the
  New Mexico Meta order stay in Current Events; Terafab (optional) left out to
  keep a lighter five-item Sunday inside the field.
- Five items, source floor met (10 sources, 5 primary + 5 secondary; each item
  one primary + one independent secondary). Both vendor items mark the vendor
  claim plainly and keep no vendor benchmark on the page as an established
  number.

## Open questions

1. Dek attribution "MIT physicist Long Ju and collaborators." The evidence lists
   MIT first and quotes Long Ju (via graphene-info, s2) but does not state he is
   the lead/first author. I named him as the MIT figure, not as first author.
   The gated Nature author list would settle whether a stronger "MIT-led"
   framing is warranted.
2. Astra primary. The series requires exactly one primary per item, so I made the
   OpenAI announcement (s3) the single primary and dropped the separate GitHub
   source, citing the repository `openai/ten-proofs` by name to the announcement
   (which links it). The direct GitHub URL is therefore no longer a numbered
   source. If the editor wants the verifiable Lean object linked directly, it
   would have to replace the announcement as the item's one primary.
