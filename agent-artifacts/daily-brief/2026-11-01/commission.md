# Commission: daily-brief/2026-11-01

The day's Daily Brief. Six items in fixed order: Word of the Day, three news,
two technology. Strict template: 300-700 words total, one citation per item,
min 6 sources. A three-minute quick read; leave analysis to the other sections.

Last brief (2026-10-31) already covered: the DOJ California ballot challenge
(Judge Thompson TRO + Ninth Circuit 20,000-ballot ruling), Q3 GDP at 3.4%, the
VA loan-modification story, the Anthropic robots.txt AI-training draft, and
Mistral Large 4. Do not repeat any of these. The slate below was chosen to be
fresh (last two days) and not to overlap them or the day's Feature (a Jepsen
database-testing piece — a different world).

## The slate (chosen; verify each to a solid source before writing)

### Word of the Day — bafflegab
`bafflegab`, noun, /ˈbæfəlˌɡæb/: confusing, jargon-filled, deliberately or
pompously obscure official language. Coined by Milton A. Smith, assistant
general counsel of the U.S. Chamber of Commerce, in the Chamber's *Washington
Report* in 1952, attacking the wording of an Office of Price Stabilization price
order; he said he had first tried "legalfusion", "legalprate", "gabalia" and
"burobabble". Document the story in three or four sentences (the prize/plaque
detail and the January 1952 date if the researcher confirms them). Caveats to
respect: Merriam-Webster hedges the coiner as "possibly" Smith and dates first
use to 1952; Green's Dictionary of Slang dates it to May 1952. Cite a dictionary
authority for the definition and an independent word-history for the coinage.
A technical readership will enjoy a word aimed at jargon. Backup word if
bafflegab cannot be sourced cleanly: `grawlix` (Mort Walker, the #$%! swearing
symbols). Do NOT use `eggcorn` (ran last week).

### News 1 — Alaska U.S. Senate certification suit
The Justice Department's suit to block certification of Alaska's U.S. Senate
race (over voter confusion from a second candidate named Daniel/Daniel J.
Sullivan): on 2026-10-31 the state moved to dismiss; on 10-30 DOJ asked the
court to segregate ballots listing the independent Sullivan. Judge Sharon
Gleason is weighing it. Distinct from last week's California case. Attribute
DOJ's legal theory (NVRA) and note that scholars (e.g. Derek Muller) question
whether the statute lets DOJ enjoin certification. Find the primary filing or
the court docket; Democracy Docket's case tracker and CBS coverage are starting
points, not the citation of record.

### News 2 — DC and Virginia sue to block the arch
On 2026-10-31 the District of Columbia and Virginia sued the National Park
Service and Interior to stop a planned 250-foot "triumphal arch", invoking the
Commemorative Works Act, APA, NEPA and historic-preservation law; Judge Tanya
Chutkan is weighing a halt before the National Capital Planning Commission's
scheduled 2026-11-05 approval vote. Find the complaint or a court record; the
Time and Manila Times reports are starting points.

### News 3 — William Nordhaus dies
William Nordhaus, the Yale economist who shared the 2018 Nobel Memorial Prize
for integrating climate change into long-run macroeconomic analysis (the DICE
model), died 2026-10-30 at 85. Primary source: the Yale announcement. One or two
sentences on who he was and the one thing he is known for (DICE / the economics
of climate). Non-political range for the slate, and a strong fit for a technical
readership.

Ranked backups if any news item cannot be verified to a solid source (tell me if
you substitute): (a) the Iran war — Revolutionary Guard mine claims in the
Strait of Hormuz, a fired Pentagon planner, US casualties — attribute Iran's
claims to Iran and find a primary statement; (b) the FOMC hold at 3.75-4.00% on
2026-10-28 with the Lisa Cook removal inquiry (primary: the Fed statement and
the White House action).

### Technology 1 — VOLTA infostealer ranks victims with an LLM
On 2026-10-31 Cisco Talos reported that the VOLTA infostealer sends stolen data
through an LLM prompted as a "forensic intelligence analyst" to rank the
victim's own stolen assets by monetization value (NOT to rank victims against
each other — correct wording per the researcher), defaulting to a hosted Claude
model with fallbacks, and failing over when it hits refusal-like phrases.
Primary: the Talos blog. Report it neutrally, as a finding about malware design;
attribute to Talos.

### Technology 2 — trojanized Claude Code extension in Cursor's marketplace
On 2026-10-29 two builds of the `Anthropic.claude-code` extension in Cursor's
marketplace were modified to add an SSH key, attempt a reverse tunnel, and
exfiltrate host details; they were live about 11 hours. Primary: Cursor's
security notice (which states Anthropic did not build the modified versions).
Report neutrally, as a supply-chain compromise; the consequence worth the line is
that uninstalling does not remove the planted key or persistence. Backup tech
item if this cannot be solidly sourced or reads as too inside-baseball: a
well-sourced release or research result from the window that is NOT Mistral
Large 4 or the Anthropic robots.txt draft.

## Standing instructions for this brief

- One strong source per item, the underlying record where it can be opened and a
  reputable report where it cannot; a second source only where the first is
  disputed or cannot settle the claim (the Word of the Day naturally takes two:
  a definition authority and a coinage history).
- Attribute every unverified or contested claim to whoever makes it (Iran's mine
  claims, DOJ's allegations, a vendor's figure).
- The two technology items both touch Anthropic's models incidentally (one abuses
  a Claude model, one compromises a Claude Code extension). Keep the framing
  strictly neutral and factual; the piece never refers to itself or its own
  newsroom, and nothing here is promotional.
- Total 300-700 words, hard limits. Keep each item to two or three sentences
  (the Word of the Day's story may run three or four). Headlines obey
  `spec/headlines.md`.

## Production (model and effort; tier→model deviations recorded)

Tiers map to named subagents: "inherit" → Opus (orchestrator's model),
"capable" → Sonnet. Recorded actuals:
- writing-coach: Sonnet, low (done).
- researcher: Sonnet, high.
- writer: Sonnet, medium (policy: capable / medium).
- editor: Opus, high, required (policy: inherit / high — honored).

## Edition neighbours

Published alongside: the Feature (Jepsen vs ParticleDB) and the Reinforcement
Learning lesson (finding optimal policies). No overlap; this is the quick read.
