# Editorial review — tech-news/2026-08-01 (editor 01)

Three ordered reads at high effort. Four items, each 1 primary + ≥1 independent
secondary, mix spanning cryptography/AI-safety, an open-weight model, quantum
hardware, and a health result. The 403-gated GPT-5.6 Sol item flagged in the
evidence was correctly dropped by the writer (I re-confirmed both openai.com
index URLs are still gated by relying on the researcher's documented 403 record
and the item's absence), so nothing in the piece rests on an unread primary.

## Skeptic

Skeptic: thesis "a production model now discovers cryptanalysis that survived
years of NIST review, evidence model capability is starting to outpace the
process meant to check it"; tested ~16 figures/labels across 4 items; broke: 4
(all fixed directly, none required a redraft).

Reopened every primary and re-verified against it, not aggregators:

- **Item 1 (Anthropic Claude Mythos, s1).** Verified against the primary post:
  HAWK-256 2^64 → 2^38, ~60 hours, two rounds of expert review over two years,
  200–800x on 7-of-10-round AES-128, Möbius Bridge, ~$100k per result, and the
  "no production software will have to change" caveat — all exact. The one figure
  I suspected (draft's "roughly a billion output tokens") checks out: the post
  says "several hundred million tokens" mid-run but "a total of one billion
  output tokens" at completion, so the draft is right. CyberScoop (s2) confirms
  the NIST-review status, the key-doubling-erases-appeal framing, and "neither
  flaw affects software now in use." No change.

- **Item 2 (Kimi K3 model card, s3).** Re-verified against the Hugging Face card
  directly (brief requirement): 2.8T total, 104B active, 16 of 896 routed experts
  (+2 shared), 1,048,576-token context — exact. License is the "Kimi K3 License";
  I pulled the actual LICENSE file (part of the primary repo) and confirmed
  Section 2 imposes the >$20M/12-month MaaS commercial-agreement threshold the
  draft states, so citing s3 for it is correct. Fortune (s4) confirms the July-16
  "2.7 trillion" figure, the $15-vs-$50 output pricing, and Moonshot's
  self-reported wins over Opus 4.8 / GPT-5.6, which the draft properly labels
  "unverified." One miscitation fixed (below). Note: the card lists Text/Image in
  its spec table and mentions video only in prose; "understands text, image, and
  video natively" is within the card's own claims but leans on the prose, not the
  spec table — left as grounded, flagged here.

- **Item 3 (HRL, arXiv s5).** Verified against the arXiv abstract: three-rail
  array of 54 exchange-coupled quantum dots, up to 18 EO qubits, "advances the EO
  state of the art by an order of magnitude," distance-5 repetition code compared
  to simulation — exact. The ~5x error suppression, 4-kelvin operating point, and
  "first time" framing are correctly carried on the secondary (s6, Quantum
  Insider). No change.

- **Item 4 (HOPE-3, EurekAlert s7).** Confirmed the EurekAlert release is issued
  by "The Lancet Press Office" (so the primary label is right, not a sponsor
  release). Verified 106 patients (54/52), ages 10–22, 54% slower PUL 2.0 decline,
  64/22 cardiac sub-cohorts, 42%-vs-15% infusion reactions, and the "expected by
  22nd August 2026" FDA date. Three fixes made (below).

`data-nb-kind` audit: all eight correct — s1/s3/s5/s7 primary (authoring party
owns the claim), s2/s4/s6/s8 independent secondary. s7 stands as primary because
it is the journal's own authorized summary, with the true article of record
(Lancet paper) subscriber-gated.

## Cut

Cut: 0 full sentences; the brief is already wire-tight with no self-grading,
signposts, stock revelations, or prompt leakage against the writer brief. Worst
tell: item 3's closer "is what a fault-tolerant machine actually needs" flirts
with the significance-announcing family, but it carries a concrete contrast
(on-chip control vs. racks feeding thousands of wires into the cryostat) and
names who it changes something for, so it earns its place — kept. No em-dash
reflex, no semicolon chains, no colon-subtitle headlines, no paired-adjective
triads; item shapes vary. One parenthetical removed for sourcing, not tell
(below).

## Reader

Reader: this gives me four late-July developments each resolved into a judgment
about who must now act — NIST reviewers facing a key-size tradeoff that guts
HAWK's appeal, a developer weighing a cheaper open-weight model under a
conditional license, engineers handed on-chip cryogenic control against the
wiring bottleneck, and DMD patients/FDA ahead of an August 22 decision — plus the
caveats the announcements buried (reduced-round AES, the $20M license threshold,
the 2.7→2.8T correction, the non-ambulatory population, the 42/15 safety
tradeoff). That is beyond a restatement. It matches the draft-handoff's
original-work claim (resolve 5→4, drop the unread 403 item, write each as a
self-contained judgment naming a decision-maker). Voice sits closer to the
guide's exemplars (numbers carry the claims; the judgment names a specific actor)
than a median AI summary. Headline retest: the four item heads are
subject–verb(–number) with no colons; the dek makes a real-world claim and does
not restate any headline.

## Direct edits made

1. **Item 4 — removed "(p=0.03)".** The p-value is real and verifiable (PUL 2.0,
   p=0.03; confirmed in CGTlive and NeurologyLive reporting and consistent with
   the Lancet abstract), but it is NOT in the cited s7 EurekAlert release, which
   reports the primary endpoint qualitatively. Attaching it to s7 decorated the
   citation, so I cut it. The 54% claim it modified remains supported by s7. If
   the writer/researcher want to restore the p-value, add a source that carries
   it — optional, non-blocking.
2. **Item 4 — "clears FDA review at an August 22 target action date" → "reaches
   its August 22 FDA target action date".** August 22 is the PDUFA decision
   deadline (release: "expected by 22nd August 2026"), not a pass; "clears"
   implied approval.
3. **Item 4 — swapped two swapped cites.** The non-ambulatory / advanced-disease
   sentence is UC Davis's framing (s8: "largely composed of non-ambulatory
   patients"), not EurekAlert's, so [7]→[8]; the Aug-22 date and 42/15 safety
   figures are in EurekAlert (s7), not UC Davis (confirmed absent from s8), so
   [8]→[7]. s8 remains cited once, preserving item 4's independent secondary, and
   first-citation order still holds.
4. **Item 2 — "Fortune reported 2.7 trillion" cite [3]→[4].** The claim is
   Fortune's (s4, confirmed: "It boasts 2.7 trillion parameters"), but was cited
   to the Hugging Face card (s3), which reports 2.8T. Repointed to the source that
   owns the claim; 2.8T stays cited to s3 on the prior sentence.

## Required work by owner

None. All four issues were miscitations/overstatements fixable directly with the
right source at hand or a surgical cut; none is a broken central claim, missing
evidence, or structural problem.

## Proof

`nb check library/tech-news/2026-08-01.html --series tech-news --repo
/home/user/the-nightly-build` → **BLOCK: 0, WARN: 0, PUBLISHABLE** after edits.

## Decision

Approve. No redraft required.
