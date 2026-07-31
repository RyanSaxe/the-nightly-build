# Editor brief — unbiased/should-the-fed-hike (02, confirm dek)

## Role
Load and follow `skills/editor/SKILL.md`. You cleared the body in 01 and required
one change: the dek misattributed the economists' "supply shock a hike cannot
fix" argument to the FOMC majority. Confirm the writer's dek fix resolves it and
introduces no new problem, then approve or route again.

## What changed since 01
Per `writer/02/draft-handoff.md`, the writer rewrote the dek in BOTH `nb-meta.dek`
and the visible `nb-dekline` to attribute the supply-shock case to named
economists (Zandi, Yellen), paired neutrally with the dissenters' persistence
argument. Only the dek changed; the body is as you cleared it.

## Begin with these exact inputs
- `agent-artifacts/unbiased/should-the-fed-hike/editor/01/editorial-review.md`
- `agent-artifacts/unbiased/should-the-fed-hike/writer/02/draft-handoff.md`
- `agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md`
- The article: `library/unbiased/should-the-fed-hike.html`

## Focus this read
1. Does the new dek stop attributing the "cannot fix" argument to the FOMC
   majority, matching the body and the evidence record?
2. Is the dek neutral (takes no side), one lean sentence, free of the
   hedged-contrast molds (semicolon reversal, suspended question, comma triad),
   and not a restatement of the neutral-question headline?
3. No regression: the body is unchanged; `nb-meta.dek` and the dekline agree.

## Proof (strict)
Confirm still clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```

## Output
`agent-artifacts/unbiased/should-the-fed-hike/editor/02/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/unbiased/should-the-fed-hike/editor/02/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
