# Editorial review: current-events/2026-08-09 (editor/01)

## Skeptic

The edition's spine is a selection judgment: four federal-power stories ordered
so one question — who decides — carries the brief, led by the Senate handing the
Justice Department to the president's former criminal-defense lawyer. The four
load-bearing claims are the 50-49 Blanche confirmation, the 2-1 D.C. Circuit
ruling keeping the ballroom blocked, the July payroll contraction with a larger
downward revision to the prior two months, and the executive order narrowing
birthright citizenship. Each headline and dek is a claim; each holds on its own
terms.

I opened all eight cited hrefs as printed and reopened each as an opponent.

Blanche (item 1). The Senate roll-call primary (s1) lands on the tally and shows
"Confirmation: Todd Blanche, of Florida, to be Attorney General," Yeas 50, Nays
49, Not Voting 1, recorded 8 August. NPR (s2) independently carries the two
Republican defections (Collins, Murkowski), the 2 August written assurance that
the $1.8 billion Anti-Weaponization Fund "is rescinded and shall have no force or
effect," and Cassidy as the decisive vote. The item calls Blanche "acting
attorney general," not conflating this vote with his 2025 Deputy AG
confirmation, which the evidence flagged. Display text checks clean: the "by one
vote" headline matches a one-seat margin, and the dek's actor, department, and
$1.8 billion price are all sourced. Nothing retired this item.

Jobs (item 3). This is the correctness watch-item, and it holds against the BLS
primary (s5), which I opened: July -23,000, unemployment 4.1 percent, May revised
+129,000 to +63,000, June +57,000 to +20,000, combined 103,000 lower. The article
and its table print the primary's post-revision figures, not NBC's transcription
(NBC's live text repeats the "cut by 66,000 to 129,000 total" error the evidence
called out; the writer correctly did not follow it). The +83,000 Dow Jones
consensus is attributed to NBC (s6), which carries it. Arithmetic recomputes:
66,000 + 37,000 = 103,000.

Birthright (item 4). The White House primary (s7) lands on the specific order,
carries the "no executive department or agency shall issue documents recognizing
United States citizenship" directive verbatim, the same-day "Ending Birth
Tourism" companion, and the reference to the 30 June 2026 Supreme Court decision.
One break: the article printed that the Court "struck down 6-3" the 2025 order,
citing NPR (s8), but the NPR page as it now reads confirms the strike-down and
the date and does not state a 6-3 margin. The margin is a nonessential specific
and I could not confirm it at the cited source, so I cut it (see Edits).

Ballroom (item 2) is where the item breaks, on sourcing rather than substance.
Two failures, both owned upstream:

1. The primary href, `https://media.cadc.uscourts.gov`, does not land on the
   opinion. Opened as printed, it resolves to the D.C. Circuit's generic Media
   Archive directory — a hub linking to "Opinions," "Orders," "Recordings" — with
   no case-specific content for No. 26-5123. It is a bare host, not the source; a
   reader who clicks it never reaches the ruling. The same bare host is the item's
   headline link. The proof passed it because the host returns 200, but the
   standard is that the link lands on the source, and this one does not. The
   draft handoff pre-flagged this substitution honestly; it remains a
   source-policy failure.

2. The sentence "the majority held that the Constitution's Property Clause gives
   Congress control of federal property and that a 1912 statute bars erecting any
   building on federal parkland" is cited to NPR (s4). Opened, NPR (s4) supports
   the 2-1 result, the 14-day stay, and the 90,000 sq ft / 1,000-seat figures,
   but does not mention the Property Clause or the 1912 statute. This legal
   reasoning is the item's teaching core and naturally belongs to the opinion
   (the primary), not the secondary — but the opinion link is the broken bare
   host above, and the evidence record's own opinion paraphrase does not list
   this reasoning either. So no opened source at hand supports the claim as
   printed. It is central, not nonessential, so I did not cut it; it routes to
   the researcher to nail the opinion source and confirm the reasoning.

The other watch-items pass. No hard page count appears for the opinion (NPR's
live text says 136 pages and Volokh said 100; the writer printed neither,
correctly). The FDA narcolepsy approval did not slip in. The AFGE "employees
covered" figure does not appear, because the VA item was dropped. Every
`data-nb-kind` is right: each of the four items carries one primary and one
genuinely independent secondary (Senate/NPR, opinion/NPR, BLS/NBC,
White House/NPR), no secondary standing in for a missing outside author.

On consequence: the four stand as the day's most consequential US developments,
and the "who decides" through-line is real for three of them, with the jobs
print carried as the required macro item rather than the lead. On the dropped VA
union-contract order, I did not force it back. The writer dropped it for want of
an openable primary (the D.R.I. order), and I cannot point the researcher to a
resolvable locator for that order, so the condition the orchestrator set for
restoring it is not met. If the researcher can later supply an openable D.R.I.
order URL, it is a strong fifth candidate and the brief has room within the 4-6
band; that is not a blocker on this edition.

## Cut

I made a dedicated slop pass over every sentence including display text, docket,
and table caption. The prose is disciplined wire writing and almost nothing
failed. Zero sentences fell to the slop test. The ledes lead on the action and
seat the figure inside the sentence that carries it ("fell by 23,000 ... held at
4.1 percent"; "voted 2 to 1 ... to uphold the injunction"), matching the voice
guide's exemplars rather than trailing the number. "The larger revision was in
the back numbers" reads like a signpost at first but earns its place: it makes a
specific claim these numbers support — the 103,000 revision dwarfs the 23,000
print — and it is followed by that figure, so it survives the delete test.

Checked against the recent-pattern notes: the dek does not use the banned
three-clause comma-and-"and" mold and does not pair the lead with a "same
day/week, also" second clause; it is one lean sentence naming the actor. The lead
is Blanche, not the jobs print, breaking the desk's recent macro-lead habit. The
headings are each written in the item's own nouns and do not repeat a prior
comma-and-"and" pattern. No formula to break.

No prompt leakage: nothing in the authored text echoes the writer brief's
selection rules, the "4-6 band," or the Tech News boundary. No borrowed phrasing
from the voice-guide exemplars. Grammar and punctuation are clean, including the
bracketed "[e]ach President" lowercasing and the docket prose.

One observation I did not act on: the revision table renders its figures with a
space thousands-separator ("+129 000") while the prose uses commas ("103,000",
"23,000"). Both are valid, and space-grouping in a data table may be a deliberate
`nb-table` convention, so I left the furniture untouched rather than risk
fighting a template style on a cosmetic point. Flagging for awareness, not as
required work.

## Reader

Read straight through, the brief gives what the sources alone would not: a
one-sitting reading of four separation-of-powers moves as a single week's answer
to who holds federal power — the Senate installing the president's lawyer, a
court telling the executive it cannot build on the People's House without
Congress, and the executive rewriting citizenship by order — with the ballroom
item's docket furniture stating the Property Clause question the wire coverage
buries under "construction halted." That matches the draft handoff's stated
original work, and it is a genuine selection-and-framing contribution, which is
the bar a brief's original work is held to. The prose sits closer to the
voice-guide exemplars than to a median summary: compressed, action-first,
figures inside the sentences, exact nouns (the named judges, the fund, the
statute) rather than category nouns. The headline, reread as the largest claim,
delivers exactly what the piece defends.

## Edits

- Item 4: cut "6-3" from "the Supreme Court struck down 6-3 on 30 June"; the
  cited source (s8, NPR) confirms the strike-down and date but not the margin,
  and the margin is a nonessential specific.
- Ran `nb stamp`; recomputed to words=657, reading_minutes=3, sources=8.

## Required work

- **researcher.** Supply a resolvable locator for the D.C. Circuit opinion in No.
  26-5123 (a court media / opinion-PDF URL, or a working docket entry) that lands
  on the opinion itself, not the `media.cadc.uscourts.gov` archive root. From that
  opinion, confirm the Property Clause and 1912-statute reasoning the item
  attributes to the majority, since NPR (s4), currently cited for it, does not
  carry it. Until an openable opinion supports it, that reasoning has no source at
  hand.
- **writer.** Once the researcher supplies the locator: update the s3 href in both
  the ballroom item's headline link and the s3 source entry, and re-cite the "the
  majority held ... Property Clause ... 1912 statute" sentence to the opinion (s3)
  rather than NPR (s4).

## Decision

revise — the ballroom item's primary link lands on a court directory rather than
the opinion, and the majority's legal reasoning is cited to a secondary that does
not carry it; both need the researcher's opinion source before the item can ship.
