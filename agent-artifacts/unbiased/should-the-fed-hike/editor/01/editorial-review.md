# Editorial review — unbiased/should-the-fed-hike (01)

## Verdict
One required change, owned by the writer: the dek misattributes the sharp
"a hike cannot fix a supply shock" argument to the FOMC majority, contradicting
the article's own body and the evidence record's explicit warning. Everything
else clears. Three small self-reference cuts made directly; proof re-run to
BLOCK: 0.

## Skeptic
Thesis: on July 29, 2026 the FOMC held rates 9-3, and the live question — hike
now or hold — has a genuinely contested, strongly cited case on each side
(Logan et al. for "raise"; the holding majority plus Zandi/Yellen for "hold"),
which the paper presents without choosing. Tested claims: (1) headline
event facts (9-3 hold at 3-1/2 to 3-3/4%, three regional-president dissenters,
Warsh as Chair); (2) each side carries a direct cited quote from a named holder
who holds it; (3) the sharp supply-shock argument is not put in Warsh's mouth;
(4) equal scrutiny, no unsupported support, strict source floors.

Broke: the **dek only**. It reads "...a preemptive rate increase the rest of
the committee says a tariff-and-energy supply shock cannot fix." The FOMC
statement attributes inflation to "supply shocks... including energy" but never
claims a hike cannot fix it; Warsh explicitly declined to call the dissenters
wrong ("I'm going to let the dissenters speak for themselves") and struck
hawkish notes on the target. The clean "don't hike into a supply shock" case
belongs to the economists (Zandi, Yellen), which the body states outright — the
hold champion block says the sharp version "comes from outside the boardroom,
from Zandi and Yellen," and the draft-handoff names this distinction as the
article's one act of original work. The dek therefore contradicts the piece's
own careful attribution, in the most-read line, and inflates the majority's
stated position beyond the record. This is the load-bearing fairness defect.

Verified and cleared:
- Event facts all match source #1 (9-3 vote, target range, Hammack/Kashkari/
  Logan each preferring +25bp) and Warsh's chairmanship match source #2/#3.
  Warsh, not Powell, correctly used throughout.
- Every quote checked verbatim against the evidence record: Logan ("Better
  modest restriction now than severe restriction later," "finish the job,"
  "mid 2's," the "puck" reasoning, 4.3% unemployment, +20% equities); Hammack;
  Jefferson; Waller; Sharif; Bostjancic; Yellen ("looking through supply
  shocks," "cannot tame supply-driven inflation," "skyrocket" exception);
  Zandi ("monetary policy 101," "dangerous game," "I don't think they should
  raise rates"); Roth; Goldman; Durham; Warsh ("no soft inflation target,"
  "shocks make this job... tougher," "let the dissenters speak for themselves,"
  "watchful thinking, not watchful waiting," 63 months). No misquote found.
- Figures match owning primaries: CPI +3.5% / core +2.6% / energy +15.7% /
  −5.7% one-month (BLS, #7); PCE +4.1% / core +3.4% (BEA, #8); Moody's split
  0.66pp energy vs 0.17pp tariffs and ~0.25pp AI (CNN, #9). The orientation's
  "energy is doing more of the work than tariffs" synthesis is supported and
  neutral.
- Tariff nuance handled exactly as the record demands: the piece states the
  statement names only energy, tariffs enter via Warsh's spoken remarks and
  Logan's speech, and gives the modeled split. No casual attribution of the
  statement's words to tariffs.
- `data-nb-kind` audit: 6 primary (FOMC statement, Warsh oath, transcript,
  Logan speech, BLS, BEA), 5 secondary (Yahoo, Tech Times, CNN, Reuters/
  Spokesman, Reuters/Globe and Mail). Yellen/Zandi reported by CNN correctly
  labeled secondary. Floors met: 11 total (>=10), 6 primary (>=4), 5 secondary
  (>=3). Meta `sources: 11` matches.
- Each `nb-side` ends on its own argument, not the piece's (Logan's "my views
  ... not necessarily those of my FOMC colleagues"; the hold side's honest note
  that Warsh does not make the sharp case). No house conclusion after the
  divide.
- Two reasoning chains are distinct, not mirrored: raise runs on expectations/
  entrenchment/cost-of-delay; hold runs on shock diagnosis/wrong-tool/labor-
  market risk. Scrutiny is symmetric; neither side padded or trimmed.

Note on the title: it is a declarative news headline, not the neutral question
the writer brief suggested. This is the stronger choice under `spec/headlines.md`
— a "Should the Fed hike?" question the piece deliberately does not answer would
be a Betteridge tell. The declarative headline states the finding with actors
named and does not pre-judge the merits. Kept.

## Cut
Cut: 3 sentences trimmed (5 words), pure deletions of structural self-reference,
no fact or claim lost. Worst tell: forward/back signposts — "the disagreement
that follows" (→ "the disagreement"), "the anchor described above gives way"
(→ "the anchor gives way"), "more equivocal than the economists' case above"
(→ "...the economists' case"). No prompt leakage found: headings use the
question's own nouns ("Finish the job now," "Look through the shock"), no
component vocabulary (camp/thesis/argument/holder) appears as visible text, no
self-narration, no claim that the article met its assignment. Punctuation clean
(no em-dashes in authored prose, no semicolon chains, no comma splices). No
manufactured punchlines. Furniture (the two-side split) carries genuine
reasoning, not decoration.

## Reader
This gives me a usable decision-frame no single source provides: the three
defined tools (real rate, relative-price shock, expectations anchoring) that let
a numerate non-economist weigh both cases; the precise energy-vs-tariff
attribution most coverage blurs; and the honest separation of the equivocal
Chair from the clean economist argument. The original-work sentence in the
draft-handoff survives in the body verbatim in substance. Prose sits closer to
the voice-guide exemplars (calm institutional analyst, terms defined once,
quotes folded into load-bearing sentences) than a median AI summary. Not a
redraft — only the dek needs to be brought into line with the body it currently
contradicts.

## Direct edits made (proof re-run: BLOCK: 0, WARN: 0)
1. Orientation: "the disagreement that follows" → "the disagreement".
2. Raise side: "the anchor described above gives way" → "the anchor gives way".
3. Hold champion: "the economists' case above" → "the economists' case".
4. Meta `words` updated 2178 → 2173 to keep the count honest after the cuts.

## Required work by owner
**Writer** — Rewrite the dek so it frames the disagreement without asserting
that the FOMC majority *says* a hike cannot fix the supply shock: keep that
sharp "cannot fix" claim as the hold side's / economists' case (as the body
does), and update both the `nb-meta` `dek` and the `nb-dekline` identically,
then re-run the strict proof to BLOCK: 0. One sentence, no side, no
hedged-contrast mold.

## Decision
Not approved this pass. One required writer change (dek). Proof currently
BLOCK: 0 with the editor's direct cuts in place.
