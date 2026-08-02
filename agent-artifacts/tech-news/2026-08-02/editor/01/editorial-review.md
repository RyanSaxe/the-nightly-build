# Editorial review: tech-news/2026-08-02 (editor, round 01)

## Skeptic
Skeptic: thesis "Two AI-governance deadlines fell the same week — the EU's
Article 50 transparency regime took legal effect on schedule with published
compliance guidance behind it, while Washington's parallel 60-day executive-order
clock lapsed with no public deliverable — bracketed by two AI-technical reads
(OpenAI's coding agents run fast but can't self-validate; DeepSeek-V4-Flash's
number worth trusting is the independent benchmark, not the vendor's notes)";
tested the 4 item theses plus headline and dek plus every figure, name, and date
against the owning primaries in the evidence record; broke: none.

Verifications that mattered on this brief's risk surface:
- Every figure, model/version name, org name, and date checked against the
  evidence record's owning primary. Item 1: 2 Aug 2026 application date, four
  duties split provider/deployer, verbatim provider quote, grace to 2 Dec 2026,
  penalty up to EUR 15M or 3% worldwide turnover, K&L Gates scope list and the
  "generic references... unlikely to be sufficient" quote — all match. Item 2:
  8 case studies (5 Codex-only / 3 with Claude Code), RustQC 60x runtime / 25x
  disk I/O, FastQC-Rust 7x, Trim Galore 3x, STAR 20,000-line rewrite / 900
  outputs by eye, HI.SIM 31% with byte-identical output, METR ~50% rejection,
  Pedersen (cyvcf2) and Ewels (RustQC) quotes and roles — all match. Item 3:
  signed 2 June, Section 3 60-day clock to 1 Aug, official list, Forkast quote.
  Item 4: Intelligence Index 50 vs median 25, #3/101, 284B/13B MoE, $0.14/$0.28
  and cached $0.003 (-98%), Terminal Bench 82.7. No figure, name, or date is
  wrong in display text or body.
- Excluded claims confirmed ABSENT: the "1,610 to 27 seconds" HI.SIM figure and
  the Kush Desai "BREAKING" quote appear nowhere.
- Attributions honored: the 99.8% aligner-parity figure is attributed to The
  Decoder by name, not asserted as OpenAI's own; the EO deliverables gap is
  framed "as of July 31, per Forkast's reporting" (and the item's closer hedges
  "as of the last independently confirmed check"), not a flatly established
  government failure; DeepSeek's open-weight status is left explicitly unsettled,
  with the vendor agent benchmarks labeled vendor-stated and unreproduced.
- Per-item sourcing / data-nb-kind audited honest: each item carries exactly one
  primary and one or more independent secondaries. Item 1's two-primary conflict
  is resolved correctly — digital-strategy.ec.europa.eu (EC FAQ) is the primary
  for the penalty and grace-period facts, artificialintelligenceact.eu is
  labeled secondary as a third-party text mirror, and K&L Gates (National Law
  Review) is the genuinely independent secondary. This is the honest
  classification, not a relabel to dodge the one-primary-per-item rule.
- Item 3 note (not a break): the only independent account (Forkast) published
  2026-07-31, at the 00:00Z Aug 1 deadline boundary the evidence record uses for
  the "lapsed" framing. The body dates the check to July 31 and hedges the
  closer, so it does not overclaim a post-deadline confirmation it does not have.
  The headline compresses this to "passes without a public trace"; acceptable
  headline compression given the body's honest, dated, attributed framing.

## Cut
Cut: 1 clause; worst tell: the item-4 closer restated the exact rank and pricing
already given earlier in the same item. Removed the redundant trailing pricing
("...at $0.14 and $0.28 per million tokens for input and output"), so the item
now ends "...ran the model itself and ranked it third of 101." The earned
vendor-notes-vs-independent-run contrast (the item's designated verdict) stays.

Other cut-read findings, left standing as within bounds:
- No prompt leakage: no selection rules, planning labels, or "this brief covers"
  self-description; the item tags (EU Policy, AI Research, US Policy, AI Models)
  are fixed template furniture, not leaks.
- No reader-handoff closers; no formulaic kickers; no stock revelation frames.
- The lead is the non-security EU item, not an AI-security reflex; no stacked
  AI-safety items; the dek is a "while" contrast (a stance about the world), not
  a banned hedged-contrast mold (no semicolon reversal, suspended question, or
  comma triad).
- Item openings vary (event, actor action, artifact-and-clock, timing-and-
  independent-finding). Two of four item headlines share a loose comma-appended
  two-beat shape (items 1 and 2); borderline, not a formula, and recasting a
  headline is new prose that belongs to the writer — noted, not required.

## Reader
Reader: this gives me the explicit EU-hit-its-date / US-missed-its-date contrast
that no single source draws, plus three signed verdicts the individual sources
state as facts but not as judgments (OpenAI's own case studies and the outside
critics converge on the same validation gap from opposite directions; the
DeepSeek number worth trusting is the independent run, not the vendor changelog).
The draft-handoff's original-work sentence survives in the article. The prose
reads with the voice-guide exemplars (plain units, the complicating number beside
the claim, skeptical framing of vendor figures), not a median AI summary. The
headline, reread as the largest claim, is honest: item 1 establishes Article 50
has no high-risk gate and that chatbots fall inside its reach.

## Direct edits made
- Trimmed the redundant pricing restatement from the item-4 closer (prose cut, no
  new prose introduced). File:
  `/home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html`

## Required work by owner
- None. No evidence gap (researcher) and no prose/structure redraft (writer) is
  required to publish.

## Re-proof
Needed. The one prose cut lowers the word count (~11 words), so the `nb-meta`
`words` field (currently 1331) is now stale. The writer should re-run the proof
to recompute it and confirm BLOCK: 0:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html --series tech-news --library /home/user/library`

## Final decision
Publishable. No redraft required. One surgical cut applied; a re-proof is needed
only to refresh the measured word count.
