# Draft handoff: tech-news/2026-08-12 (02)

## Original-work sentence

The article states the day's honest through-line that the evidence only records
item by item: with model releases quiet across the window, the movement was
observational and laboratory, and it orders three separately-dated developments
under that reading — the 12 August coronal-observing campaign, Dyna-1's
inversion of an NMR spectrum's missing peaks into a motion signal, and
Anthropic's text-marking — while keeping each fact next to what it is (a
campaign not a result, a self-report attributed to its owner, a disclosure with
its non-disclosures named).

## Final proof result

`./nb check ... --series tech-news --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 1 — PUBLISHABLE.**

## Warning intentionally left

- `W-LENGTH-LOW` — brief expects 4-6 items; 3 present. Left standing by
  direction. Honest verification (researcher/03) yields exactly three qualifying
  items for 10-12 August, each with a primary and an independent secondary; the
  azine C-H coupling paper was dropped for want of any independent secondary.
  Padding to four would require a misdated, product, markets, or aggregator
  item, which the brief and series prompt forbid. Three short beats four padded.

## Round-01 requests resolved

- Independent secondary per item: each of the three items now cites one primary
  plus at least one independent secondary (eclipse: NASA + AFP/phys.org; Dyna-1:
  Nature + CBIRT + Kiin Bio; Anthropic: support page + TechCrunch). The prior
  `B-SOURCE-KIND` blocks and `W-SOURCES-MIN` warning are cleared (7 sources).
- Azine C-H coupling item removed from the article and the Sources list.
- Anthropic item added and framed as the technical AI development: the prose
  states what Anthropic disclosed (text is marked, the mark survives copy-paste
  and may persist through some editing, C2PA metadata for SVG/PNG/JPG, the
  2 August model cutoff, a detected mark is non-conclusive) and what it did not
  (how the text mark is built, how much editing removes it). The headline names
  the non-disclosure rather than overclaiming a provenance guarantee.
- Dyna-1 secondaries' preprint-era status stated in the prose (CBIRT 5 Apr 2025,
  Kiin Bio 6 Nov 2025 both predate the 10 August Nature paper; the work
  circulated as an early-2025 preprint).

## Open questions

- The Dyna-1 independent secondaries cover the March 2025 preprint, not the
  10 August Nature publication that is the news event. They are genuine
  independent accounts of the same result, and the prose flags them as
  preprint-era, but whether preprint-era coverage satisfies the per-item
  secondary rule in spirit is an editor call (noted in researcher/03's
  contradictions). The proof accepts them.
