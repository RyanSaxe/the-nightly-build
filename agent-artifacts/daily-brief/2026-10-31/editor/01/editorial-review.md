# Editorial review: daily-brief/2026-10-31 (editor/01)

## Correct

The brief has no single thesis; it is six dated items sorted from a two-day
record, so I audited each item's claims, figures, dates, citation hrefs and
`data-nb-kind` against the evidence record and the owning documents, hardest on
the six binding caveats.

**Word (eggcorn).** Definition cited to Merriam-Webster (s1, primary). The story
(Liberman posts 23 Sep 2003; Pullum suggests the name after "mondegreen";
Liberman's 30 Sep update carries it; the OED cites that update) is pinned by
M-W's word history and by Language Log's "'Eggcorn' makes the OED" (s2,
secondary). The record pins every step without the unopened 2003 post, as the
caveat requires. The self-referential close is Zimmer's observation and is true.
Held.

**California.** Thompson's order (30 Oct), its terms and the 16 Nov expiry match
NBC (s3, secondary). The order's geographic scope is NOT stated, per the caveat;
the body says "election officials" with no geographic limit. The Ninth Circuit
2-1 vote and the "more than 20,000 people it alleges are noncitizens" both match
NBC (s4, secondary), with the DOJ figure attributed ("it alleges"). CBS (s5,
secondary) carries the 21-24 Oct Los Angeles County subpoenas. All three kinds
are secondary and correct; a wrong "primary" here would have claimed a court
document the piece never opened. I confirmed the chronology: the subpoenas
(21-24 Oct) precede both 30 Oct rulings, which disciplined the item-2 headline
rewrite below. Held.

**Economy.** 3.4% annualized Q3 GDP (up from 2.2%) to BEA (s6, primary); 3.6%
twelve-month September PCE to BEA's September personal-income release (s7,
primary). The 2.1% annualized-quarterly PCE is absent, so the two measures are
not conflated, per the caveat. "five days before the midterm elections" checks
out: the 29 Oct releases fall five days before Election Day, Tuesday 3 Nov 2026.
I narrowed "the same morning" to "the same day": the record dates the September
PCE release to 29 Oct but does not pin a release time, and only the GDP release
carries a time (8:30 a.m. EDT). Held.

**Veterans.** More than 15,000 veterans up at least $150/month since VASP ended
1 May 2025, and the 63%-against-2% comparison, both match NPR (s8, secondary).
Framed as NPR's analysis, not new policy; "steered" does not appear, per the
caveat. Held.

**robots.txt.** The `__usage_ai-training` token, the robots.txt mechanics, the
no-IETF-standing and the wildcard-does-not-opt-out points all match the IETF
draft (s9, primary); Google's planned 2027 support matches Google's post (s10,
primary). Reported as a proposal, not a standard. Held.

**Mistral.** ~1 trillion parameters and the 29 Oct date to TechCrunch (s11,
secondary, which owns the date because Mistral's page is undated); the modified
MIT / hosted-service license and the 41% Terminal-Bench 4.0 figure to Mistral
(s12, primary). The benchmark is attributed as Mistral's own, per the caveat,
and the active-parameter figure (the 49B/52B ambiguity in the record) is omitted.
Held.

All twelve printed hrefs match the evidence-recorded URLs exactly, and the proof
run with link validation lands every one.

## Reads well

The body items were tight and specific; the placeholder test turned up no empty
sentence, and the one line that survives it on the nouns alone (the eggcorn
self-reference) is the word item's earned delight, which the voice guide invites.
Nothing read as lifted from the briefing or from the voice guide's quoted
passages. I cut no body sentence.

The display lines were where the work was. The dek restated the headline: its
first clause ("a federal order now shields California election workers from
Justice Department threats") said what the title already said, against the rule
that the dek carries what the headline left out. I rewrote it to the one court
action the title omits (the Ninth Circuit's 2-1 refusal), kept the DOJ figure
attributed, and added "more than" so the dek no longer flattens "more than
20,000 ... it alleges" into a bare "20,000 ballots."

## The experience

A brief is a text read, and no item wanted a table or chart; adding furniture
would have fought the three-minute read the series is built for.

I rebuilt the second item's headline. "Thompson's order and the Ninth Circuit
leave DOJ's California ballot push stalled" leaned on a weak stative verb
("leave ... stalled") and a vague noun ("push"), and "stalled" sat awkwardly
against an item that also reports grand-jury subpoenas and DOJ calling criminal
action its next step. The replacement states the item's strongest fact plainly
and defensibly: two federal courts ruled against DOJ on one day. It is built
differently from the other four item headlines, and no two of them now share a
connective. The title ("Judge bars DOJ ...") is a court lead, which the recent
record over-uses, but it is the day's dominant item by importance (two courts,
ballots in an election four days out) and states a real finding with a live verb,
so it stands rather than being swapped for a weaker non-court item. Title, dek
and item-2 headline now descend from the order, to the Ninth Circuit specifics,
to the two-court frame without any one restating another.

What the piece gives beyond its sources: it sorts a thin, scattered two-day
record into six dated, attributed facts and keeps every contested or self-reported
claim (DOJ's 20,000, Mistral's benchmark, Google's 2027 target) with its owner
while dropping what no document pinned (the order's scope, the 2.1% quarterly
PCE). That matches the writer's original-work sentence and is real curatorial
work, not a restatement of one source.

## Edits

- Rewrote the dek (nb-meta and dekline, kept identical): removed the restatement
  of the headline; it now carries the Ninth Circuit's 2-1 refusal with the DOJ
  figure attributed and hedged to "more than 20,000."
- Rewrote the item-2 headline from "Thompson's order and the Ninth Circuit leave
  DOJ's California ballot push stalled" to "Two federal courts rule against DOJ's
  California ballot challenge in a single day."
- Economy item: "the same morning" to "the same day" (release time not pinned by
  the record for the September PCE release).
- Ran `nb stamp` (words=676, sources=12) and the proof with links: BLOCK 0,
  WARN 0, PUBLISHABLE.

## Decision

approve. Every claim holds against the record, the six caveats are met, the
display lines are now defensible and built differently, and the proof is clean at
676 words inside the 300-700 band.
