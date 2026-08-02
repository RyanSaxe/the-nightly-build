# Writer handoff: paper-of-the-day/generative-adversarial-networks (writer/02)

Revision round, per `editor/01/editorial-review.md`'s one required item plus a
re-proof. No new claims introduced; only the dek and the stale measured
counts changed.

## The dek fix

Old dek (both `nb-meta` and the rendered dekline): "The 2014 paper proved a
clean equilibrium in the space of functions, and the decade after measured
exactly how far training practice sat from that space." This is the voice
guide's explicit do-not-reuse formula, "proved X for a setting practice never
occupied," verbatim in shape.

New dek (both `nb-meta` `dek` and the rendered `.nb-dekline`, identical):

> A fair-budget study a decade later found that none of the fixes proposed
> since consistently outperforms the non-saturating loss the paper itself
> patched in when its proven objective wouldn't train.

Why it clears the bar:
- Not the banned mold: it does not open on "proved X," and it does not scope
  a proof against a setting practice lacked. It opens on a finding (the
  fair-budget verdict), one of the three themes the brief named.
- Not an effect-size hook and not a "N follow-ups disagree" line: it states
  one specific, sourced result (Lucic et al.'s conclusion, already cited in
  the body as source 7) rather than a magnitude or a list of disagreeing
  parties.
- Not a restated headline: the headline ("Goodfellow's GAN Paper Named Its
  Own Failure Mode and Never Fixed It") is about the paper naming mode
  collapse and not fixing it. The dek adds a different, later fact — that the
  paper's own practical patch (the non-saturating loss) still hasn't been
  consistently beaten a decade on — which is new information, not a restatement.
- Checked against the other banned dek molds in `spec/headlines.md`: no
  semicolon reversal, no suspended question, no three-clause comma triad.

## Constraints honored

Changed only the dek (both locations) and the two stale `nb-meta` counts. Did
not touch the editor's four direct cuts, the verbatim abstract, any equation,
any table, any citation, or any other sentence. Diffed the file against the
pre-revision version mentally section by section while editing; the only
non-dek, non-meta lines touched were the two numeric fields below.

## Refreshed counts

Recomputed word count with the engine's own `Article` parser (same method
used in writer/01) rather than eyeballing it, since the editor's four cuts
plus the dek recast both change the counted prose:

- `words`: 2522 → **2468**
- `reading_minutes`: `max(1, round(words/230))` = 11 either way, unchanged
- `sources`: unchanged at 8 (no citation added or removed)

Updated in `nb-meta` only; the rendered byline already read "11 min read" and
needed no change.

## Proof result

Exact brief command:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`

Result: **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE (link checking on, network
reachable).

## Remaining questions

None. The editor's review found no other required changes; this round
touched nothing else.
