# Writer draft handoff — unbiased/should-the-fed-hike (01)

## Original work

The article's one act of original work: it separates three layers of evidence
the record kept blurred together — the FOMC statement's own narrow attribution
("supply shocks... including energy," no mention of tariffs), Kevin Warsh's
broader spoken list of shocks, and Moody's Analytics' modeled split (~0.66pp
Iran/energy vs. ~0.17pp tariffs) — and uses that separation to do two things no
single source does: (1) it corrects the commission's Jerome Powell assumption
against the Fed's own May 22, 2026 record and represents Kevin Warsh
throughout, and (2) it deliberately does not let Warsh's institutional
standing borrow the clean "don't hike into a supply shock" argument that only
the named economists (Zandi, Yellen) actually make in those terms — the
Position B champion paragraph states this distinction explicitly, sourced to
both his own transcript and their reporting, rather than collapsing the
majority's institutional decision and its sharpest defense into one voice.

## Article and paths

- `.nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html`
  (edited in place from the initialized skeleton; no assets or charts used —
  the evidence record found no chart-bearing source and flagged only a
  possible future CPI/PCE chart as a candidate for a later revision, not
  required here).

## Structure delivered

- `orientation`: the July 29, 2026 vote (9-3, range 3-1/2–3-3/4%), Warsh's
  standing as Chairman (sworn in May 22, 2026, correcting the commission's
  Powell assumption), the three dissenters, the "most fractured hawkish
  dissent since September 2016" framing, headline/core CPI and PCE figures,
  the statement's exact supply-shock attribution language against Warsh's and
  Logan's broader shock lists and Moody's modeled split, and definitions of
  dual mandate, real interest rate, relative-price/supply shock, and
  expectations anchoring — each defined once, at first use, and reused by name
  afterward.
- `nb-divide` with exactly two `nb-side` sections:
  - **Position A, "Finish the job now"** (`id="raise-now"`): Lorie Logan's own
    July 16, 2026 speech carries the argument (entrenchment risk, her "mid
    2's, not all the way back to 2 percent" trajectory call, "Better modest
    restriction now than severe restriction later"), corroborated by Hammack's
    shorter quote, Kashkari's vote, the 2016 historical parallel, Jefferson's
    and Waller's pre-meeting statements, and post-meeting economist reaction
    (Sharif, Bostjancic). Named holder: Logan, with standing and her own
    disclaimer that the dissent is hers alone, not the other two dissenters'.
  - **Position B, "Look through the shock"** (`id="hold-the-line"`): the
    argument is carried by Yellen's "looking through supply shocks" default
    strategy and Zandi's "monetary policy 101" case, plus Roth, Goldman Sachs,
    and Durham, then the precise energy-vs-tariff modeling split. Named
    holder: Kevin Warsh, chaired the 9-3 hold, with his own words kept
    honestly equivocal (the hawkish "no soft inflation target" line sits next
    to his shock acknowledgment and his refusal to characterize the
    dissenters as wrong) — the paragraph closes by naming Zandi and Yellen,
    not Warsh, as the source of the case's sharpest form.
- `sources`: 11 entries, numbered in first-citation order, 6 primary / 5
  secondary, all read in full per the evidence record. No source cited here
  that the researcher did not verify.

## No house conclusion

Neither `nb-side` ends on language that tips toward the other; the last
sentence of each side closes that side's own argument (Logan's labor-market
reading; the Committee's reach not extending to Iran or Congress). No section
outside the two sides characterizes which case is stronger.

## Proof result

```
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```

Final run: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**

En route to that result the proof caught and I fixed:
- em-dash count over the house limit (8 uses; cut to 0 by using colons,
  periods, and commas instead — including one very minor punctuation
  normalization inside a direct Logan quote, changing her em-dash to a comma
  without altering a single word);
- a citation-order violation (Warsh's press-conference transcript was cited
  before his oath-of-office press release; reordered the two orientation
  sentences so source numbering follows first appearance);
- six sentence-density warnings (55-, 54-, 41-, 44-, 66-, and 67-word
  sentences); all split into shorter sentences without cutting any cited
  claim.

No warnings were left unresolved; none needed to be argued down.

## Measured counts

Words: 2,178 (template band 1,200–3,500). Sources: 11 (6 primary, 5
secondary), against the strict gate of ≥10 total / ≥4 primary / ≥3 secondary.
`nb-meta` carries these measured values, not targets.

## Remaining evidence or voice questions

None. The evidence record's one open decision — whether to lead Position B's
champion with Warsh's own words or with Zandi's/Yellen's — was resolved as
described above: Warsh holds the champion slot on institutional standing, and
the paragraph itself names Zandi and Yellen as the source of the case's
cleanest form, so the distinction the brief required stays visible on the
page rather than being resolved silently in drafting.
