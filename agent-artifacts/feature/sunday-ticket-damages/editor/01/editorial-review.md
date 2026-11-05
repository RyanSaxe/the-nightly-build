# Editorial review: feature/sunday-ticket-damages (editor/01)

## Correct

Thesis, taken from the draft alone: the Ninth Circuit restored the
subscribers' economists and their liability verdict but agreed that the jury's
damages must be retried, because the awards are almost certainly class counts
times $294 minus $102.74, which the court calls "a discount, not an overcharge."
The claims under it:

1. The disposition, the panel and the author. Checked against the opinion PDF
   (pp. 5–7, 12, 32) and the memorandum (pp. 2–5). Johnstone wrote for Thomas
   and Lefkow, Lefkow sits by designation, and there is no separate opinion. The
   exclusions and the JMOL are reversed, the new damages trial is affirmed, and
   liability is reinstated. It held.
2. The $191.26 arithmetic and how the courts describe it. I recomputed it:
   24,105,049 × $191.26 = $4,610,331,671.74 exactly, and 506,788 × $191.26 =
   $96,928,272.88 against the $96,928,272.90 on the verdict form. I read the
   form's page image. Dkt. 1513 pp. 13–14 credits the reverse-engineering to the
   defendants ("Defendants proffer") and finds it "compelling". Opinion pp. 30–32
   carries "almost certainly", "Dr. Zona's disputed estimate" and the discount
   sentence. I read Instruction 41 from its page image, and the quoted words
   match, including the stray comma. It held. One break: the draft said the
   district court rejected the subscribers' alternative as "the same error".
   Dkt. 1513 n.10 says "a similar flaw", so I changed it to that.
3. On a per-subscription scale, the reinstated models bracket the residential
   award without producing it and sit far above the commercial award. I
   recomputed the divisions: $2.81B/24,105,049 = $116.57, $5.6B/24,105,049 ≈
   $232, $670M/506,788 ≈ $1,322, $1.3B/506,788 ≈ $2,565. The commercial
   multiples are 6.9 and 13.4. The claim held, with three breaks:
   - Zona's sentence read as if adding one licensee "costs" the classes $2.81
     billion and $670 million. Opinion p. 27 says the exclusivity cost them those
     sums, so I recast the sentence.
   - The draft's line "gives 24.6% and no dollar total" put the missing total on
     the model. All we know is that the opinion reports none (p. 29), so the
     sentence now says that.
   - Fig. 2 printed Zona's residential value as an exact "$116.57", from a
     total the opinion gives only as "$2.81 billion". I cut all four derived
     values to the precision of their inputs (≈ $117, ≈ $232, ≈ $1,320,
     ≈ $2,570) under the house rule on precision. The bars do not move.
4. What follows. The closer said the testimony "offers two" competitive prices,
   but the piece had already given three models, so the draft contradicted
   itself. I rewrote the closer to name all three and to rest the multiple on
   the two with dollar totals. "This opinion 'concerns only'" misquoted p. 19,
   which says "This appeal concerns only". I fixed it.

Other checks. The NFL quotes match the Yahoo copy of Deadline, and "did not
immediately respond" matches the Reuters copy at Insurance Journal. The cert
petition, printed p. 25, matches the quote, and so do Kavanaugh's statement
p. 2, §1291 and FRAP 40(d)(1). "Bars and restaurants" went beyond the opinion's
"Commercial subscribers like sports bars" (p. 15), and the sentence now uses the
opinion's words. All eleven hrefs return 200 from the printed address, and the
link-checking proof passes. Every `data-nb-kind` is correct. The two secondary
sources are separate outlets with separate authors (Patten/Deadline,
Scarcella/Reuters), and each is used only for what it reports.

The 13 November date: the timeline's heading stated "Rehearing petitions due"
as fact. It now reads "Rehearing deadline, by our count under Rule 40", and the
item text follows the rule's own condition, "unless an order changes it". The
arithmetic (30 October plus 14 days, and the 45-day period does not apply
because the United States is only an amicus) checks against the rule text.

Derived values: the caption already said "derived here". I made the prose say
so too: "Our own division of each total…". No claim was narrowed to hide thin
reporting. Every narrowing above brings a sentence back to what the documents
say.

## Reads well

Cut because it said nothing: "The restored testimony answers the question the
jury was asked." It is the section heading restated as an opener. Also cut:
"The league's legal ground predates the trial." The next sentence dates the
petition, so the line was a transition with nothing in it. Cutting it left
"exempts its pooled sale" with no referent, and it now reads "the league's".

Cut as redundant: Fig. 1's second caption sentence, which repeated the bar
labels and the prose and also carried the piece's one semicolon.

Lifted: "The right panel shows the formula where nothing lines it up" was
unclear, and it now says that the commercial award falls below the range.
Rascher arrived with no introduction and with an undefined "yardstick". He is
now "the other economist" who "compares the NFL with" college football, and the
term is gone. The $232-against-$102.74 comparison left the reader to work out
why one is twice the other. It now carries the opinion's own explanation, that
$102.74 averages "a group that included the Subscribers" (p. 32), and adds no
speculation.

Recent record: the headline does not use "<Court> rules against", and it does
not open with an institution and a figure. The dek has no "where" contrast. No
heading is a count phrase. The closer is the conclusion and not a caveat. I
found nothing borrowed from the voice guide's quoted passages or from the
commission's phrasing.

## The experience

The two figures carry the argument and render cleanly at 390 px and 1280 px in
both themes. Nothing overlaps and the page has no horizontal scroll. I checked
in `nb preview` with Playwright after the final edits. The timeline adds little
beyond dates, but the section needs it as its visual, and the 13 November item
is now attributed. I added no component, because the word ceiling (1,194 of
1,200) has no room for one.

What the piece gives beyond its sources: it divides every expert total by the
count the jury used. That puts the award and the models on one scale, which
shows the residential award inside the models' range by coincidence and the
commercial award an order of magnitude below them. Neither court sets that out.
It matches the writer's original-work sentence. The headline holds, since the
court's own word for the $191.26 is "discount".

## Edits

- Dek (meta and dekline): "almost certainly subtracts an average price paid from a list price" → "almost certainly comes from a list price minus an average price paid".
- "although bars and restaurants paid" → "although commercial subscribers such as sports bars paid" (opinion p. 15).
- "rejected it as the same error" → "rejected it for a similar flaw" (Dkt. 1513 n.10).
- Fig. 1 caption cut to "One $191.26, placed two ways."
- Cut "The restored testimony answers the question the jury was asked."
- Rascher introduced as "the other economist, compares the NFL with top-25 college football telecasts…"
- Zona sentence recast: the 49.7% cut, then "Against that world, exclusivity cost the residential class $2.81 billion and the commercial class $670 million."
- NFL Tax: "gives 24.6% and no dollar total" → "cuts it 24.6%, and the opinion gives no dollar total."
- "Divide each total…" → "Our own division of each total…", which labels the derivation in the prose.
- Added the opinion's "a group that included the Subscribers" (p. 32, cited) after "more than twice the $102.74".
- "Zona's is half of that, which is what…" → "Zona's is about half of that, as…".
- "The right panel shows the formula where nothing lines it up" → "On the right, the commercial award falls below that range".
- Fig. 2 values and aria labels: $116.57 → ≈ $117; ≈ $1,322 → ≈ $1,320; ≈ $2,565 → ≈ $2,570.
- Timeline heading: "Rehearing petitions due under Rule 40" → "Rehearing deadline, by our count under Rule 40". Item text: "unless extended" → "unless an order changes it".
- "broadcast strategy" → "media distribution strategy" (the NFL's words).
- Cut "The league's legal ground predates the trial." "exempts its pooled sale" → "exempts the league's pooled sale", and "its 2020 Supreme Court petition" → "the NFL's 2020 Supreme Court petition".
- "This opinion 'concerns only'" → "The 2026 appeal 'concerns only'" (p. 19).
- Closer rewritten to give all three competitive prices and "The smaller of the two dollar totals puts the commercial claims at about seven times the first commercial award."
- Restamped: 1,194 words, 5 minutes, 11 sources. Proof with link checks: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. With the edits above, every claim matches the document that owns it,
and the argument needed no change.
