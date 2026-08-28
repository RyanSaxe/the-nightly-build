# Editorial review: tech-news/2026-08-28 (editor/01)

## Skeptic

The brief carries no single thesis. It is four self-standing judgments, and its
working claim is the running order: the day's real weight is compute
infrastructure, so AWS leads and a reported megaraise closes. The title makes the
largest claim, that AWS has committed to two million more NVIDIA GPUs. Each item
rests on one load-bearing figure or fact, and I tested each against the primary I
opened.

AWS item. The two-million-GPU commitment across 2027 and 2028, the 100,000 GPUs
for U.S. government AI factories at Impact Level 6 and above, the Blackwell
Ultra/Rubin/Rubin Ultra platforms, and the more-than-three-million running total
for the year all hold against the AWS newsroom primary (s1) and the AI Business
secondary (s2), both of which I opened. The figures and their owners match. The
"none deployed yet" caveat follows from the forward-dated 2027-2028 window the
primary states, so it is a sound inference rather than a new fact.

Robotaxi item. I opened the NTA permit PDF (s3) and read it firsthand: it is the
signed Interim Order and Permit, AVNC 002, Docket 26-05015, dated July 27, 2026,
and it caps Tesla at a maximum fleet of ten fully autonomous vehicles, bars
transport above 45 mph, confines service to the Las Vegas Strip corridor, and
prohibits pickups within a quarter mile of Harry Reid International Airport. Every
term the item states is in the document. The item correctly treats the reported
5,000/1,000/1,000 ceilings from the August 20 full approval as secondary-only
(TechCrunch, s4, which I opened and which carries the caps and the Eric Early
"ceiling, not a plan / ~2,500 realistic" quote), and says plainly that no primary
order for the higher caps is public and that the only permit document available
caps the fleet at ten. The unverified figure is stated as unconfirmed, as the
round focus required. It held.

OpenAI item. The Lean 4 certificates, the Apache-2.0 license, the four named
results, and the repository's own framing of the certificates as verification for
an accompanying manuscript all check against the openai/ten-proofs repository
(s5), which I opened. The "Astra" name and the ~$2,000 cost are correctly
confined to the announcement-and-secondary layer and attributed to The Decoder
(s6), which I opened; neither appears in the repository. This item's break is not
in what it sources but in when it happened. The manuscript and The Decoder both
date to August 1 (the manuscript updated August 6), roughly four weeks before this
edition, which the evidence record and s6's own dateline confirm. The item is
written in present-and-recent framing ("open-sources," "OpenAI released") with no
date, so in a brief dated August 28 alongside genuinely current items a reader who
arrived from a link reads four-week-old work as today's development. The
commission, the writer brief, and my round focus all required this item to be
framed as prior news being built on, and it is not. The repository carries no
date, so the fix cannot come from the cited primary as it stands. This is routed
to the writer below; the writer already flagged it as an open question.

Broadcom item. I opened the Q2 FY2026 10-Q (s7) and confirmed it contains no
reference to Anthropic, to a special-purpose vehicle, to the reported raise, or to
the false "$29B backstop" an aggregator attributed to it. The item asserts none of
those as filing-confirmed; it says the opposite, that the filing is silent and
that the quarter closed before the June deal so it neither confirms nor rules the
raise out. The reported $70-80B (toward $100B in some accounts), the SPV, the
Anthropic tie, the $35B June Apollo/Blackstone arrangement, the anonymous
sourcing, and the no-comment responses all match the Yahoo Finance secondary (s8),
which I opened. The unverified figure is carried as the item's substance, marked
reported throughout. It held.

Sourcing audit. Every item carries exactly one primary and at least one
independent secondary; every data-nb-kind label is correct (AWS newsroom, NTA
order, OpenAI repo, and Broadcom 10-Q are genuine first-party primaries; AI
Business, TechCrunch, The Decoder, and Yahoo Finance are independent secondaries).
All eight hrefs resolve to the source itself. Nvidia's August 27 earnings are
absent, as required. The Nvidia-Hugging Face acquisition, which had no primary, was
correctly dropped rather than run as fact.

## Cut

The prose is clean and does the voice guide's central move well: it credits each
claim only as far as its source reaches and closes each item on the specific
open caveat rather than a reader-facing line. I found no empty conclusions, no
negative-parallelism reflex (the one "rather than" in the OpenAI item corrects a
real misreading, that Lean certificates are themselves the discoveries, which the
repository's own framing names), no vague attribution, and no self-reference. The
edges are carried by facts: the article's last sentence gives the reasoning for
why the 10-Q is silent, and survives the delete test.

Four small changes. The AWS closer joined two independent clauses with a semicolon
and repeated "2027 and 2028" from the item's own first sentence; I cut the
redundant clause and kept the open caveat as its own sentence. The Broadcom
no-comment sentence used the same reflex semicolon between two independent clauses;
I made it a period, per the punctuation standard. The lead item's heading repeated
"across 2027 and 2028" verbatim from the dek directly above it; I trimmed the date
from the heading, which the dek and body both still carry. The Broadcom heading
called the raise a "megaraise," feed-register puffery in display text where the
figure ($70-80B) is already stated; I cut it to "raise."

No slop sentences required deletion. No borrowed phrasing from the voice guide's
quoted writers appears in the draft. No prompt leakage: the sourcing-provenance
sentences read as the wire brief's honest reporting to the reader, not as lifted
instructions. Against the recent-pattern notes, the desk's AI-security and
model-release lean is broken (the lead is infrastructure), the dek uses an "X,
with Y" build rather than the flagged two-clause "X, and Y," and the four item
headings vary in construction. No furniture is present; I considered a stat strip
for the AWS numbers and judged it optional, since the cumulative relation (one
million at GTC plus two million new, past three million this year) reads more
clearly as prose than as a list of separate figures, and the brief identity favors
terse prose.

## Reader

Read straight through, the brief gives more than its sources do: a
provenance map of the day, separating what a first-party record actually
establishes (AWS's own commitment, the ten-vehicle permit, the public Lean
certificates, the silent 10-Q) from the larger figures that live only in
secondary reporting (the 5,000-robotaxi ceiling, the "Astra" name and $2,000
cost, the $70-80B raise). That is the writer's stated original work, and it
survives. The prose sits closer to the voice-guide exemplars than to a median
summary, because a median summary would flatten those provenance distinctions
into flat assertions. The one place the map fails is time rather than source: the
OpenAI item maps where its claims came from but not when they happened, so its
"what moved today" premise does not hold for that item until it is dated.

## Edits

- Trimmed the AWS item's closer from "The commitment covers 2027 and 2028; none of the two million has been deployed yet." to "None of the two million has been deployed yet." (removed the redundant clause and the reflex semicolon; kept the open caveat).
- Changed the Broadcom item's "The figures trace to anonymous sources; Broadcom and Apollo did not comment" to a period between the two independent clauses.
- Trimmed the lead item's heading from "AWS and NVIDIA to add two million GPUs across 2027 and 2028" to "AWS and NVIDIA to add two million more GPUs" (removed the date already carried by the dek directly above it).
- Cut "megaraise" to "raise" in the Broadcom heading (puffery in display text; the figure is already stated).

## Required work

- **Writer** — Date the OpenAI item and frame it as prior news being built on, not the day's development. The manuscript is dated August 1, updated August 6 (in the evidence record, and confirmed by The Decoder's own dateline), roughly four weeks stale for this edition; as written, the item reads as current to a fresh reader. Per the writer's own open question, dating the staleness explicitly means bringing the manuscript in as a cited primary for this item (the evidence record holds its URL and date), since the repository carries no date. No researcher work is needed: the evidence is complete. Re-run the proof after the change.

## Decision

revise — the article is sound on sourcing, numbers, and prose, but the OpenAI item presents four-week-old work as current and must be dated and framed as prior news before it can publish.
