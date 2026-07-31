# Draft handoff — word-of-the-day/shibboleth (writer, round 02, recast)

## Original-work sentence

The piece holds the involuntary phoneme test at the Jordan fords and the PLOS
ONE Ukraine/Russia example in a single line of argument — a phoneme an
outsider's mouth cannot produce, then and now — a throughline no single cited
source draws; that observation is unchanged from round 01 and this round does
not touch it.

## What changed, and why

The editor's skeptic read (round 01) found the headline and origin paragraph
attributed all 42,000 Ephraimite deaths in Judges 12 to the shibboleth/
sibboleth pronunciation test. The researcher's round-02 evidence addendum
confirmed the correction: Judges 12:4 records a battle — "the Gileadites
defeated Ephraim" — that Gilead wins *before* anyone reaches the river; the
fords test in 12:5-6 catches fugitives from that already-lost fight; and
12:6's "forty-two thousand ... fell at that time" is the summary toll of the
whole episode (battle plus fords), with no text-given split between the two.

Three surfaces recast, nothing else touched:

1. **Headline.** "A Mispronounced Consonant Cost 42,000 Ephraimites Their
   Lives" → "A Sound No Ephraimite Could Fake Decided Who Crossed the Jordan
   Alive." The new headline keeps the piece's real surprise — an involuntary,
   unfakeable phonetic tell deciding who lived — without pinning a body count
   on the test. It states a finding, names the actor (Ephraimite), fronts the
   concrete image, carries no colon and no coiner-opener.

2. **Dek.** "The biblical origin of the word shibboleth, and the same
   involuntary test a 2023 study finds still sorting Ukrainian speakers from
   Russian ones" → "Judges counts forty-two thousand Ephraimite dead across
   the whole war with Gilead, and a 2023 study notes the same involuntary
   test still sorting Ukrainian speakers from Russian ones." Two fixes: the
   verb is now "notes" (the PLOS ONE paper cites the Ukraine/Russia point to
   its own reference [3] rather than establishing it, matching the body's
   "note"), and the 42,000 is now framed as the whole-war toll, not the
   fords-test body count — the correction the editor required.

3. **Origin paragraph** (`orientation` section). Added one clause of battle
   context before the fords scene: "Gilead had already beaten Ephraim in
   battle before anyone reached the river — 'the Gileadites defeated
   Ephraim,' the text says, giving no separate count for that fight." The
   paragraph then moves to "The survivors ran for the Jordan, and Gilead held
   the fords against them" (previously the paragraph opened here, with no
   battle mentioned at all) before the existing fords-test text. The closing
   sentence now reads: "'Forty-two thousand from Ephraim fell at that time'
   — the toll of the whole war, battle and fords together. The text does not
   divide it between the two." This replaces the prior framing, which
   juxtaposed the fords killings directly against the 42,000 with nothing
   between them, letting the number read as the test's own body count.

   Source entry `s2` (Sefaria) was widened from "Judges 12:5–6" to "Judges
   12:4–6" (href updated to `Judges.12.4-6`) since the paragraph now cites
   v.4 as well as v.5-6.

Per the brief, no other section was touched: the sh/s mechanism section, the
Hebrew literal-meaning dispute, the sense-development timeline, the PLOS ONE
modern-use section, the IPA pronunciation, and all `data-nb-kind` values are
unchanged from round 01/the editor's punctuation-fixed version. The two
editor punctuation fixes (semicolon splices → periods) from round 01 remain
in place. I did not add the v.1-3 Ephraimite-quarrel backstory the evidence
record mentions as scene-setting context — the brief's required change and
the editor's routed work both name only the v.4 battle clause as the fix, the
voice guide favors a tight scene-first opening over a fuller backstory, and
the correction (42,000 is the whole-episode toll, not a fords-only number) is
fully supported without it.

## Files changed

- `.nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html`
  — `<title>`, `nb-meta.title`, `nb-meta.dek`, `nb-meta.words`, `<h1>`,
  `.nb-dekline`, the `orientation` section's body paragraph, and source entry
  `s2`'s locator/href.

No asset or chart changed; no new sections or furniture added.

## Word count

Measured via the same `Article`/`word_count` path `nb check` uses:
**742 words** (was 677 before this round's additions). `nb-meta.words`
updated from 677 to 742 to match. 742 is inside the 550-800 band the brief
sets.

## Proof result

```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

Run both before nb-meta.words was updated (742 vs. stale 677, still within
the 20% self-count tolerance so it did not block or warn) and again after the
update (742 vs. 742). Both runs: `BLOCK: 0`, `WARN: 0`, `PUBLISHABLE`.

## Editorial requests addressed (round 01 review, routed for round 02)

- [x] Headline no longer claims the pronunciation test alone cost 42,000
  lives.
- [x] Origin paragraph now reflects that a battle (v.4) precedes the fords,
  so the 42,000 is not presented as the test's body count.
- [x] Dek verb changed from "finds" to "notes" to match the body's own
  framing of the PLOS ONE citation.
- [ ] Optional, non-blocking tightening the editor flagged (cite the
  root-dispute clause to source 5 instead of 4; cite the 1638 date to source
  1 instead of 6) — left as-is. The editor marked this explicitly optional
  and outside the required correction; both citations are defensible as
  written since the cited sources discuss those exact points, and the brief
  scopes this round to the 42,000 correction only.

## Remaining questions

None. The evidence record's guidance on safe/unsafe 42,000 phrasings was
followed directly (whole-episode toll, no fords-only count, no claim that
the test alone accounts for all 42,000), and the proof is clean.
