# Writer handoff: paper-of-the-day/generative-adversarial-networks (writer/03)

Revision round, per `editor/02/editorial-review.md`'s one required item plus a
re-proof. Only the dek's time interval and the stale measured counts
changed; nothing else.

## The dek date fix

Old dek (both `nb-meta` and the rendered dekline): "A fair-budget study **a
decade later** found that none of the fixes proposed since consistently
outperforms the non-saturating loss the paper itself patched in when its
proven objective wouldn't train." The dek's subject is the fair-budget study,
which the body cites as source 7, Lucic et al., "Are GANs Created Equal? A
Large-Scale Study" — submitted 2017, three years after the GAN paper (2014),
not a decade. The editor caught this correctly: the body itself is precise
about a different interval elsewhere ("Seven years after the paper" for the
2021 diffusion result), so "a decade later" was simply the wrong number
attached to the right finding.

New dek (both `nb-meta` `dek` and the rendered `.nb-dekline`, identical):

> A fair-budget study three years later found that none of the fixes
> proposed since consistently outperforms the non-saturating loss the paper
> itself patched in when its proven objective wouldn't train.

Only "a decade later" → "three years later" changed; every other word is the
same as the round-02 dek that already cleared the banned-mold and
dek-shape checks. It stays off the banned "proved X for a setting practice
never occupied" mold and its close cousins (no semicolon reversal, no
suspended question, no three-clause comma triad), and it does not restate
the headline, for the same reasons `editor/02/editorial-review.md` already
verified for the round-02 wording.

## Constraints honored

Changed only the dek's interval (both locations, kept identical) and the two
stale `nb-meta` counts. Did not touch the editor's cuts from either round
(confirmed the round-02 cut — the "this record does not assert a conference"
sentence — was already absent from the file before this round started), the
verbatim abstract, any equation, any table, or any citation.

## Refreshed counts

Recomputed with the engine's own `Article` parser, since both the editor's
round-02 cut and this round's dek edit changed the counted prose:

- `words`: 2468 → **2444**
- `reading_minutes`: `max(1, round(words/230))` = 11, unchanged
- `sources`: unchanged at 8

## Proof result

Exact brief command:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`

Result: **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE (link checking on, network
reachable).

## Remaining questions

None.
