# Draft handoff — unbiased/should-the-fed-hike (writer, round 02)

## Scope
Dek fix only, per brief and editorial-review.md. Body untouched (editor
cleared it).

## Original-work sentence
Unchanged from round 01: the article's original work is separating the
equivocal Chair's own words from the sharper "supply shock, wrong tool"
argument that actually belongs to named outside economists (Zandi, Yellen),
rather than letting the two get collapsed into one "the committee/majority
believes X" voice, as most single-source coverage does.

## What was wrong
The dek (both `nb-meta.dek` and the visible `nb-dekline`) attributed the
clean "a tariff-and-energy supply shock a hike cannot fix" argument to "the
rest of the committee" — i.e., to Warsh's 9-3 majority. The evidence record
and the body itself establish that Warsh's own transcript words are more
equivocal (he declines to call the dissenters wrong, strikes a hawkish note
on the target, and frames the hold around market-driven tightening and
"watchful thinking, not watchful waiting" rather than a settled anti-hike
doctrine). The sharp, textbook "supply shock / wrong tool" case is carried by
named economists — Zandi and Yellen — not by the majority or the Chair. The
dek contradicted the body's own honest attribution in the most-read line of
the piece.

## Old dek (both fields, identical)
> Lorie Logan and two fellow regional Fed presidents dissented from Kevin
> Warsh's 9-3 hold, arguing that five years of above-target inflation
> requires a preemptive rate increase the rest of the committee says a
> tariff-and-energy supply shock cannot fix.

## New dek (both fields, identical)
> Lorie Logan and two fellow regional Fed presidents dissented from Kevin
> Warsh's 9-3 hold, arguing that five years of above-target inflation demands
> a rate increase, while economists such as Mark Zandi and Janet Yellen call
> the inflation a tariff-and-energy supply shock no hike can fix.

Both the dissenters' persistence argument and the economists' supply-shock
argument are stated as claims each side/its advocates make ("arguing,"
"call") — the dek takes no side and does not resolve which is right, matching
the body's own unresolved divide. No hedged-contrast mold (no semicolon
reversal, no suspended question, no comma-triad); one sentence; does not
restate the declarative headline.

## Files changed
- `.nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html`
  — `nb-meta.dek` (line ~29) and visible `nb-dekline` (lines ~43-48) only.
  No other lines touched.

## Proof result
```
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```
Result: `BLOCK: 0` / `WARN: 0` / `verdict: PUBLISHABLE`. No warnings to
record or waive.

## Editorial requests addressed
- The single required change from `editor/01/editorial-review.md` ("Required
  work by owner — Writer") is addressed: the dek no longer puts the
  economists' sharp supply-shock argument in the FOMC majority's mouth; it now
  attributes it to Zandi and Yellen by name, alongside the dissenters'
  persistence argument, with neither side privileged.

## Remaining questions
None. Scope was dek-only and is complete; body was not touched per
instruction.
