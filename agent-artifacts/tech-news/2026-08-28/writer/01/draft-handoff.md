# Writer draft handoff: tech-news/2026-08-28 (01)

## Original work

The brief ranks the day's developments by consequence and, for each, separates
what the primary record actually establishes (AWS's own two-million-GPU
commitment, the NTA permit's ten-vehicle cap, OpenAI's public Lean certificates)
from the larger figures that live only in secondary reporting (the reported
5,000-robotaxi ceiling, the ~$2,000 proof cost and the "Astra" name, and
Broadcom's unconfirmed debt raise), so the reader can see how far each claim's
primary reaches.

## Selection

Four items, ordered by consequence, per the brief's steer:

1. **AWS–NVIDIA two-million-GPU expansion** (lead) — the only candidate both
   first-party-primary and on-date. Primary: AWS newsroom (s1). Secondary: AI
   Business (s2), which supplies the platform names and the >3M running total.
2. **Nevada robotaxi authorization** — AV tech on public roads. Primary: the NTA
   interim permit (s3), which caps Tesla at ten vehicles. Secondary: TechCrunch
   (s4) for the Aug 20 full approval and the reported 5,000/1,000 ceilings.
   Stated plainly that no primary order for the higher caps is public, and that
   Tesla's own engineer calls 5,000 a ceiling (~2,500 realistic).
3. **OpenAI's ten Lean-verified results** — treated as prior news built on, not
   the day's development. Framed around what is now public and checkable (the
   Apache-2.0 Lean 4 certificates). Primary: the openai/ten-proofs repo (s5).
   Secondary: The Decoder (s6). "Astra" and the ~$2,000 cost are attributed to
   the announcement/secondary layer, not the artifact; noted as unrefereed.
4. **Broadcom's reported AI-debt raise** — included only with the uncertainty as
   the item's substance. Primary: Broadcom's Q2 FY2026 10-Q (s7), which contains
   no reference to the arrangement (and closed before the reported June deal, so
   it neither confirms nor disconfirms). Secondary: Yahoo Finance (s8) for the
   reported $70–80B figure. The false $29B-backstop aggregator claim is not
   repeated.

**Dropped:** Nvidia–Hugging Face acquisition (no primary exists — single-origin,
unsigned, uncommented; cannot satisfy the per-item one-primary rule, so cut
rather than run as fact). Nvidia's Aug 27 earnings (markets, routed to
current-events). Thomson Reuters "Thomson" model (product launch, no independent
secondary opened).

## Furniture

None. The wire-brief identity favors terse prose items, and no item carries a
comparison, sequence, or derivation that prose hides; the AWS figures read
clearly inline. A stat strip for the GPU counts was considered and judged
decorative given the prose already carries the scale.

## Proof

Final command (links included) run exactly as the brief specifies:
`./nb check ... --series tech-news --library /home/user/library-checkout`
Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings intentionally
left. (Four W-SENTENCE-DENSITY warnings during iteration were resolved by
splitting the long sentences, not waived.) `nb stamp`: words 618, reading 3 min,
sources 8. Display-text self-test done: meta `dek` and the rendered dekline are
identical; every date, number, and name in title/dek/headings traces to its
owning primary, and no disputed figure (5,000 robotaxis, $80B, $2,000, "Astra")
appears in display text.

## Open questions

- OpenAI item: the manuscript's own date (Aug 1, updated Aug 6) is not stated,
  because with the repository as the single primary the date is not
  repo-sourced. The item avoids implying same-day news, but if the editor wants
  the staleness dated explicitly, the manuscript (evidence has it) would need to
  be the item's primary instead of the repo, at the cost of the "certificates
  are public" hook.
