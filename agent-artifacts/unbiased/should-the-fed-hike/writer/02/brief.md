# Writer brief — unbiased/should-the-fed-hike (02, dek fix)

## Why this round
The editor approved the body (accurate, fair, symmetric, no house conclusion,
BLOCK: 0 after three direct self-reference cuts) but found one required change,
and it is display text so it is yours: **the dek misattributes** the economists'
sharp "a tariff-and-energy supply shock a hike cannot fix" argument to "the rest
of the committee" / the FOMC majority. That contradicts the body and the evidence
record, which keep the clean "cannot fix" case with Zandi/Yellen (the hold side's
economists), not the equivocal majority under Warsh.

## Begin with these exact inputs
- `agent-artifacts/unbiased/should-the-fed-hike/editor/01/editorial-review.md`
  (the required change and the editor's reads)
- `agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md`
  (who actually holds the sharp supply-shock argument)
- The article: `library/unbiased/should-the-fed-hike.html`

## Required change (only this)
Rewrite the **dek** in BOTH places — the `nb-meta.dek` field and the visible
`nb-dekline` — so it does not claim the FOMC majority *says* a hike cannot fix
the tariff/energy supply shock. Frame the disagreement neutrally (the dek must
take no side and match the body): the hold side (with its economists) argues the
inflation is a supply shock a hike cannot fix, while the dissenters argue the
persistence demands a hike now. Keep it one lean sentence, no hedged-contrast
mold (no semicolon reversal, no suspended question, no comma-triad), and don't
restate the neutral-question headline. Do not touch the body — the editor cleared
it.

## Proof (strict, run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```

## Also write
`agent-artifacts/unbiased/should-the-fed-hike/writer/02/draft-handoff.md`: the
old and new dek text and the proof result.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/unbiased/should-the-fed-hike/writer/02/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work only. Do not tour the repo/archive.
