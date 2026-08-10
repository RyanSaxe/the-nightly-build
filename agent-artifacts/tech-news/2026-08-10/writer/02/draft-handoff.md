# Draft handoff: tech-news/2026-08-10 (writer 02) — revision

## Original work

The article separates each vendor's framing from its own primary record — most
sharply on the OpenAI lead, where it holds the Lean 4 certificates to what they
actually guarantee (the formalized theorems compile) and stops there, reporting
that no named mathematician is on record as having worked through the informal
arguments and that peer review is still to come — and builds a side-by-side
table of the EU Article 50 and California transparency regimes that neither
source constructs, showing one shared operative date against two different
scopes.

## Editorial requests resolved

- **Item 1 / lead realigned to researcher/03.** Rewrote the verification passage
  to the ten-advances (Story B) status exactly as recorded: Lean 4 certificates
  are machine-checkable and compile; whether each Lean statement encodes its
  informal claim is unsettled; no named mathematician is documented as having
  worked through the informal arguments; full peer review is still to come. The
  May Erdős human-verification (Story A) is not imported.
- **Item 1 / independent source replaced.** Dropped the misidentified Understanding
  AI / Timothy B. Lee entry and the "reaction, not verification" quote with the
  Gowers/Bloom named reactions (all tied to the May event). s2 is now Simon
  Willison's 1 August 2026 post (correct byline Simon Willison), the account that
  actually covers the ten-advances release and asserts no human verification.
- **Item 1 / s2 author label fixed.** Source entry now reads "Simon Willison ·
  Ten advances in mathematics" at the simonwillison.net href.
- **Item 1 / Astra and $2,000 restraint preserved.** Neither is printed; the dek
  and title still say "internal OpenAI model" and "advances."
- **Item 4 / "$119 billion" verified and cut.** Opened the Electrek href (s9): the
  figure does not appear; s9 says only "future expansion phases bringing total
  investment much higher." Cut the number and rewrote the sentence to the
  multi-phase claim s9 carries.

## Preserved settled work

Items 2, 3, 5 unchanged. The editor's two in-place fixes kept: item 2 "thirteen
days"; item 3's "to line up with the EU" clause remains cut. Dek and dekline
unchanged and identical.

## Proof result

`./nb check ... --series tech-news --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warning left
standing. `nb stamp`: words 794, reading_minutes 3, sources 11. nb-meta keeps
`harness: claude-code-routine`, `model: Opus 4.8`.

## Open question

None blocking. Carried caveat unchanged: the EUR 15M / 3% Article 50 penalty is
attributed to Cooley (s4) as reported context, stated as a ceiling ("can reach"),
since Article 99 was not read firsthand.
