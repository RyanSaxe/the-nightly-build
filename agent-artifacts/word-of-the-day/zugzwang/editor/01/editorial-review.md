# Editorial review — word-of-the-day/zugzwang (editor, round 01)

## Decision
APPROVE. All direct edits below made in the article; `nb check` holds at
BLOCK: 0, WARN: 0. No redraft or evidence request required.

## Skeptic
Skeptic: thesis "zugzwang names the case where the compulsion to move — not the
existence of a bad option — is itself the disadvantage; and the documented
English record starts earlier than the usually-credited citation"; tested 5
claims; broke: none.

Reopened the two load-bearing chess-history sources as an opponent and matched
every dated claim descriptor by descriptor:

- **1894 Ulster Echo (lead claim / dek).** Winter, "Earliest Occurrences of
  Chess Terms" (s2): Ulster Echo, 19 December 1894, p. 4, "The position is a
  perfect example of what the Germans call Zugzwang." Draft quote and date
  exact. Winter does **not** call it a "chess column"; he cites only "page 4,"
  and the evidence record (entry 6) calls it a "notice." Corrected the draft's
  unsupported descriptor (see edits). Dek arithmetic checks: 1905 − 1894 = 11
  years, "eleven years before the citation historians usually credit." The
  claim rests on Winter (secondary, honestly labelled), which the commission's
  own source policy allows as a scholarly history for the origin dates; this is
  Winter's archival find, not repeated folklore.
- **1858 Deutsche Schachzeitung (s3).** "Zugzwang, Zugwahl und Privilegien,"
  pp. 353–358 — verified against Winter's "Zugzwang" page. "Six pages" =
  353–358, correct. Kind `secondary` is honest: the researcher could not reach
  the 1858 primary and rests on Winter.
- **1905 Lasker's Chess Magazine (s3).** p. 166, Marshall–Janowsky, "White has
  struggled bravely and only loses by 'Zugzwang.'" — exact against Winter.
- **1896 "died of Zugzwang" (s3).** Winter: p. 368, Steinitz–Lasker. The draft
  adds "world championship match"; the 1896–97 Moscow Steinitz–Lasker rematch
  was in fact for the world title, so the added context is accurate, not
  folklore. Left standing.
- **Nimzowitsch, My System p. 36 (s4, primary).** Exact phrase "the necessity
  of making a move" and the step-by-step collapse match the evidence quotation;
  author's own text, correctly `primary`.
- **Heidenfeld 1972 (s3).** "true zugzwang requires the compulsion to flip the
  result … calling the label 'nonsense'" matches Winter's report of Heidenfeld
  (BCM, Jan 1972) rejecting the Sämisch–Nimzowitsch "Immortal Zugzwang Game."
  A properly steelmanned opposing view.
- **Dictionaries.** Merriam-Webster (s1) card definition verbatim; Oxford
  Learner's (s5) definition verbatim and the "common symptom / no piece lost"
  critique is sound. Both correctly `primary` (each owns its entry).
- **Transfers.** Freedman (s6) and FIIA (s7) quotations exact against the
  evidence; both use the term for a worsening compulsion to act, not a loose
  "dilemma"; both correctly `primary` (authors using the term).

`data-nb-kind` audit: all seven correct (s1/s4/s5/s6/s7 primary; s2/s3 Winter
secondary). No misclassification hiding a missing independent source. The 1604
Salvio study was deliberately omitted by the writer because the specific
endgame could not be verified — the right call; no folklore printed.

## Cut
Cut: 3 sentences plus two reflex openers trimmed; worst tell: the section-1
punchline "Both dates are real. Only one of them is first." — a quotable pair
that graded the point instead of adding a fact already carried by the two
sentences before it.

Direct edits (prose/word-level only; no markup, assets, or structure touched):
1. "An unsigned **chess column**" → "An unsigned **notice**" — descriptor not
   owned by the source; matches Winter ("page 4") and the evidence record.
2. Deleted "Both dates are real. Only one of them is first." — manufactured
   punchline / self-grading; the 1894-first / 1905-later facts are already
   established in the preceding sentences.
3. "**Read that closely:** the position is not yet lost…" → "The position is
   not yet lost…" — removed direct reader-address (banned self-reference).
4. "**Imagine** the rules let a player pass instead: the same position holds
   indefinitely." → "If the rules let the player pass, the same position holds
   indefinitely." — removed the banned lecturing opener while preserving the
   pass-counterfactual, which is the crux of the teaching.
5. "**This piece follows** the broader definition … because it is the sense
   that travels beyond chess." → "The broader definition … is the one that
   travels beyond chess." — removed piece-narrating self-reference; keeps the
   substantive bridge into the transfer section.

No prompt/instruction leakage found on comparison with the writer brief and
commission. Punctuation is clean (en-dashes for name pairs and ranges only; no
em-dash reflex, no semicolon chains). The one earned hedged contrast
(stalemate vs zugzwang, source-supported by FIIA) is within the ceiling.
Word count fell 794 → 774 (measured via `nb`); updated `nb-meta.words` to 774
to keep the declared count honest. Still inside the 550–800 band.

## Reader
Reader: this gives me one corrected origin timeline (1858 German print → the
overlooked 1894 English attestation that displaces the Lasker-1905 default →
1929 naturalization), a usable test derived from Nimzowitsch rather than from
stacked dictionaries (would passing help? then it is zugzwang), and that same
test checked against two real non-chess uses — none of which any single cited
source assembles on its own. This matches the writer's original-work claim in
draft-handoff.md and is not a restatement of the sources; no redraft. Voice sits
closer to the Winter exemplar (dated evidence inline, claim held separate from
its degree of certainty) than to a median AI summary, and the cuts sharpened
that. Headline retested as the largest claim ("Zugzwang means having to move is
the disadvantage") — it is the thesis the piece defends; no colon subtitle, no
Betteridge. Dek is one concrete origin sentence, not a restatement of the
definition, and clears spec/headlines.md.

## Sources re-checked (result)
- Winter, "Earliest Occurrences of Chess Terms" — fetched; 1894 Ulster Echo
  p. 4 confirmed; "column" descriptor not supported (fixed).
- Winter, "Zugzwang" — fetched; 1858 pp. 353–358, 1905 p. 166, 1896 p. 368,
  Heidenfeld 1972, and 1929 My System all confirmed exact.
- Merriam-Webster, Oxford Learner's, Nimzowitsch p. 36, Freedman, FIIA —
  verified against the evidence record; quotations and kinds correct.

## Proof
`nb check … --series word-of-the-day` → BLOCK: 0, WARN: 0, PUBLISHABLE
(after edits and the word-count update).
