# Editorial review: tech-news/2026-08-02 (editor/01)

## Skeptic

Thesis of the brief: four in-technology developments moved on 2026-08-02, and
each one collapses a familiar assumption about how the field works. The dek
carries the lead claim (GPT-5.6 rewrote its own serving code; OpenAI cut its
cheapest tier 80% in the same release), and every item heading is a claim in
its own right. All four headings state a finding with a named actor and a
concrete number, not a scope. The brief geometry holds: four items, each with
one primary and at least one independent secondary.

Load-bearing claims tested against their owning primaries:

- **GPT-5.6 / Luna (item 1).** Luna $0.20/$1.20 at an 80% drop, Terra 20% to
  $2/$12, Sol's Fast mode at 2.5x speed / 2x price, serving cost -20% and
  efficiency +15% — all match the OpenAI post (s1) and the numbers record. The
  Gemini 3.1 Flash-Lite undercut is carried by the independent Willison
  secondary (s2), which is the source that confirms the price where OpenAI owns
  it. The engineering claim (Sol rewriting kernels) is OpenAI-only; the price is
  independently confirmed. The unverifiable Opus 4.8 $25/M comparator the brief
  warned about is absent. Held, with two cuts (see Cut).

- **DeepSeek V4-Flash (item 2).** $0.28/M output is confirmed against DeepSeek's
  own pricing page (s3); the ~50% cut, the missing V4-Pro companion, and the
  "trails Kimi K3" framing are Caixin's (s4); the price-war framing and the
  adviser quote are Axios's (s5), quoted verbatim against the record. The
  284B/304B parameter ambiguity the record flagged never enters the prose — the
  writer avoided the bare figure as instructed. Held.

- **RFC 10015 (item 3).** The MUST-NOT for RSA and finite-field DH in TLS
  1.2/DTLS 1.2, the 175-suite / 17-document scope, and the untouched TLS
  1.2/TLS 1.3 branches all check out (s6 primary; s7 Tech Times). One break: the
  closing sentence claimed the ban "targets exactly the two key-exchange
  families the Raccoon-class attacks exploited." I fetched RFC 10015 to verify.
  The RFC cites Raccoon as rationale for banning finite-field DH **only**; RSA
  key exchange is banned for unrelated reasons (no forward secrecy,
  Bleichenbacher/ROBOT/DROWN, lack of domain separation). The article's own body
  sentence states this correctly ("the rationale for banning finite-field DH"),
  so the closing both overreached the primary and contradicted the item's own
  earlier line. Fixed by cutting the false clause (see Edits). The s6 citation on
  the body Raccoon sentence is correct — the RFC does cite Raccoon.

- **Gemini Robotics 2 (item 4).** "Fewer than 200 examples," the five named
  hardware partners, ER 2's multi-minute / hundreds-of-decisions planning on the
  ASIMOV-Agentic benchmark, and Engadget's teleoperation caveat all trace to s9
  (primary) and s10 (secondary). The "real-time, fully autonomous" phrase is
  attributed through Engadget, and the Tesla Optimus comparison is Engadget's
  too. The closing carries an honest boundary rather than a verdict. Held.

Boundary confirmed: the brief does not touch the EU AI Act Article 50
enforcement or the Anthropic supply-chain ruling — both correctly left to the
same-day Current Events brief. The lead is genuinely new (self-optimizing
inference pricing), not the crypto-flaw / AI-agent-CVE mold the last several
editions ran; the record confirms nothing advanced that story on 08-02.

data-nb-kind audit: every primary owns its claim; every secondary is an author
outside the authoring party. The one soft spot is s8 (Hacker News), labeled
secondary but used only for practitioner reaction ("Practitioners flagged...")
— which is the legitimate use the record prescribes, and item 3 already has Tech
Times (s7) as its independent secondary, so geometry does not lean on it.

## Cut

Three cuts, all removing unsupported or self-grading material rather than
trimming survivors:

1. **Item 1 opening sentence** — "OpenAI attributes the cut to an internal,
   unverified engineering claim." This opened the whole brief on a meta-frame
   grading the evidence rather than on the claim, violating the voice guide's
   "open on the claim" move. It was also redundant: the very next sentence's
   "OpenAI says" carries the attribution, and "OpenAI's own production kernels"
   / "the model's own experimentation" carry the "internal." Cutting it lets the
   lead item open on the news; the honesty flag survives in the attribution.

2. **Item 1 closing clause** — "...without the quarter of margin a lab usually
   banks before passing a gain to customers." An unsupported generalization about
   industry norms found nowhere in the evidence. The earned consequence chain
   ("turns an internal efficiency claim into a retail price the same day")
   stands without it.

3. **Item 3 closing clause** — the false Raccoon-both-families claim (see
   Skeptic), which also happened to be a two-clause comma-and-"and" shape the
   voice guide flags. The accurate, earned consequence ("A decade of informal
   warnings just became something a compliance scanner can fail you on")
   survives as the closing.

Worst tell found: the item-1 opener — a self-grading throat-clear standing where
the lead sentence should be. No repeated cross-item formula: the four closings
run genuinely different shapes (a mechanism chain, a competition synthesis, a
compliance consequence, an honest boundary). No prompt leakage — comparing the
prose against the writer brief, nothing copies instruction language, planning
labels, or "fulfilled the assignment" claims. No furniture is present, and none
is owed: the evidence for these four items is prose-shaped, not chart- or
table-shaped, and the record's only chartable asset (Wafer.ai throughput) sits
in a candidate the writer correctly did not carry.

## Reader

Read straight through as the paper's declared reader (an ML engineer who
already saw the headlines), the brief gives what the sources alone would not:
the connective judgment. It links Sol's kernel rewrite to a same-day retail
price cut, then reads items 1 and 2 together to argue the inference floor is now
set by competition rather than by any one lab's engineering headroom; it turns
RFC 10015's normative shift into an enforcement consequence; and it holds Gemini
Robotics 2's few-shot number against the autonomy DeepMind's framing implies.
The original-work sentence in the handoff claims exactly these chains, and they
survive in the article. The prose sits closer to the voice-guide exemplars
(number-first sequencing, consequence-chain closes, the honest boundary in item
4) than to a median summary. The headline-as-largest-claim (the dek) is true and
supported, if close in wording to item 1's own heading — acceptable for a brief
whose dek teases the lead story.

## Edits

- Item 1: cut the opening sentence "OpenAI attributes the cut to an internal, unverified engineering claim."
- Item 1: cut the closing clause ", without the quarter of margin a lab usually banks before passing a gain to customers."
- Item 3: cut the false closing clause "The ban targets exactly the two key-exchange families the Raccoon-class attacks exploited, and "; capitalized the surviving "A decade...".
- Byline: corrected "4 min read" to "3 min read" to match the re-stamped reading_minutes (stale after the cuts).
- Ran `nb stamp`: words 817 to 779, reading_minutes 4 to 3, sources 10 (unchanged).

## Required work

- **writer:** run the full proof (`nb check ... --series tech-news`) over the
  cut article to confirm PUBLISHABLE after `nb stamp`. No new prose is owed —
  all editor changes were pure cuts plus a stale-label and count correction.

## Decision

approve — all findings, including the one factual break (item-3 Raccoon
overreach), were fixable by surgical cut; geometry, numbers, boundaries, and
sourcing hold, and the writer need only re-run the proof.
