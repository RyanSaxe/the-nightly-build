# Draft handoff — word-of-the-day/shibboleth (writer, round 01)

## Original work

This piece's one act of original work: it separates the *phoneme* from the
*word* as the thing being tested — stating plainly that the Ephraimites were
caught by a sound their dialect lacked, not by any secret they failed to
learn, and that shibboleth's own literal meaning (a live scholarly dispute
between "ear of grain" and "stream") was never the point of the test at the
ford. No single source states this distinction as the article's throughline;
the researcher's sources establish the phonetic fact (Jewish Encyclopedia)
and the literal-meaning dispute (BDB/Strong's, Balashon) separately. The
article's contribution is holding those two facts apart on purpose — an
involuntary, identity-bound tell versus a chosen secret — and then showing
that same structure, not just the same word, at work in the PLOS ONE 2023
paper's Ukrainian/Russian phonology example. That distinction is stated
explicitly in the closing lines ("A password is a secret... A shibboleth
offers no such choice") and is what the piece does to the evidence that the
evidence does not do itself.

## Files changed

- `.nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html`
  — full draft written into the initialized skeleton. Word card + orientation
  section (scene at the Jordan fords), four flex sections (`a-sound-not-a-password`,
  `what-the-word-meant`, `test-word-to-test-of-belonging`,
  `what-counts-as-a-shibboleth-now` — the last doubling as the piece's
  conclusion), and the Sources section with 8 sources in first-citation order.
  No chart, no source-image asset (per the evidence record's own assessment:
  no chart-worthy series, no distinctive primary-document visual — the Hebrew
  is rendered inline as text beside its transliteration, as the brief
  permitted).

## Proof result

```
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```
`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. No warnings were suppressed or
argued away — there were none to address.

Measured word count via the engine's own `Article.word_count`: **677** words
(band 550–800). Source count: **8**, all carried from the researcher's
evidence record; none of the Discarded items (NYT lines, arXiv PDF,
Wikipedia, the SEO listicles, the paywalled OED) were cited. `nb-meta.sources`
and `nb-meta.words` reflect these measured values, not placeholders.

## Evidence and voice decisions worth noting

- Definition: Merriam-Webster sense 2a, "a use of language regarded as
  distinctive of a particular group" — the evidence record's own recommended
  cleanest card definition.
- Pronunciation: rendered as IPA `/ˈʃɪbələθ/` in the word card, per the
  brief's correction that MW's `ˈshi-bə-ləth` is MW's respelling system, not
  IPA, and should not be printed as IPA.
- Origin: Judges 12:5–6 quoted from the JPS (2023) translation via Sefaria
  (source 2), including the exact dialogue and the "forty-two thousand"
  line as a direct quotation; the piece states plainly that Judges is the
  only record of that count (no independent corroboration), per the
  evidence record's caution against treating it as an externally verified
  historical toll.
- The English-attestation dates (late 14th c. word entry vs. 1630s/1638
  figurative sense) are kept as two distinct milestones, not collapsed into
  one "coined in YEAR" sentence, per the brief and evidence record.
- The Hebrew literal-meaning dispute (ear of grain vs. stream/flood) is
  presented with both named positions (Klein, Speiser, Guralnik) and no
  side taken, per the evidence record's explicit instruction not to pick a
  winner.
- Modern use: the PLOS ONE 2023 paper (source 9 in evidence, source 8 in
  this article's numbering) is the sole modern-usage citation, including its
  Ukraine/Russia phonology example, exactly as the brief specified. The NYT
  citations and the arXiv PDF listed under Discarded were not used anywhere
  in the draft.
- Headline and dek avoid a coiner-as-subject opening, the "named for the
  wrong person" reveal, the eponym frame, and the dek's banned hedge/
  semicolon-reversal/comma-triad molds, per `spec/headlines.md` and the
  commission's explicit list of structures not to repeat.
- The press's added banned term `mechanism` (max 1 use) is not used at all
  in the draft; the piece names the phonetic/identity distinction in plain
  words instead throughout.

## Unresolved warnings

None. `nb check` returned `WARN: 0`.

## Remaining evidence or voice questions

None outstanding. The evidence record and voice guide fully supported the
draft; no researcher or writing-coach request was needed.
