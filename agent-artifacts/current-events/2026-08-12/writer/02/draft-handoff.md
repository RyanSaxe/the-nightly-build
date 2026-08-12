# draft handoff: current-events/2026-08-12 (02)

## Original work

The article converts a date-conflicted, primary-thin evidence record into an
honestly framed 12 August publication of the day's most consequential recent US
news: it ties each court item's holding to the order's own docket as the item's
single primary, and reframes the inflation item so that no unposted July CPI
figure is printed while the firsthand-verified June baseline and the Fed's live
hike posture carry it. No reported development is dated to Wednesday.

## Proof result

`./nb check ... --series current-events --library /home/user/library-checkout`
(full, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
Stamp: sources 9, words 721, reading_minutes 3. nb-meta harness
"claude-code-routine", model "claude-opus-4-8"; dek identical to the rendered
dekline; zero em-dashes in body.

## Editor's two direct edits preserved

- s1/s2 Epstein wire: kept the "Bloomberg News (Bob Van Voris)" byline the editor
  set, and made the URL match it (the Bloomberg article), replacing the AP link
  that had carried the corrected byline.
- Voting item close: kept the Talwani quote and the sourced "fewer than 90 days
  before the 3 November midterms" as two sentences, with no rationale attributed
  to the judge.

## Editorial requests resolved

- Gilman (FIX 1): removed "arrived Wednesday" and the Texas military-hospital
  claim. He was back in the United States Tuesday night and was expected at
  Andrews Air Force Base; release owned to State (primary), return details to NBC
  (secondary); detained 2022, sentence 3.5 to about 10 years, no exchange.
- Preska/Epstein (FIX 2): the holding now rests on Preska's SDNY order, cited to
  its CourtListener docket (Giuffre v. Maxwell, 1:15-cv-07433) as the item's
  primary, with the Bloomberg wire as secondary. Scope stated only as far as the
  evidence supports (Giuffre 2015 civil records); no grand-jury materials asserted.
- Talwani/mail voting (FIX 3): the holding now rests on Talwani's D. Mass. order,
  cited to its CourtListener docket (League of Women Voters of Massachusetts v.
  Trump, 1:26-cv-11549) as primary. The wrong "federal roster of citizens" claim
  is gone; the mechanism is stated accurately (delivery conditioned on voter-list
  requirements the Postal Service enforces) and the injunction is framed as the
  new, distinct, nationwide district-court action.
- CPI (FIX 4): removed the "released this morning" contradiction. The July index
  is stated as due Wednesday morning with June as the most recent published
  reading; the verified June baseline (+3.5% YoY, -0.4% m/m, core +2.6%) carries
  it, with the Fed's hold and hike dissents as attributed secondary context. No
  July figure printed. A firsthand BLS check at draft time confirmed the live
  release still showed June.

## Constraint that shaped the sourcing (needs an editor/orchestrator note)

The series enforces `per_item_sources: primary [1, 1]` — the proof BLOCKS any item
that cites more than one primary. Two of the round-02 fixes named two primaries
for a single item, so I chose one primary per item and carried the second
document within the one-primary budget:

- Mail voting: the Talwani order is the single primary (the editor's must-fix was
  that the holding rest on a primary). Executive Order 14399's exact Section 3(b)
  text (state-submitted list, USPS-enforced) is owned by the Federal Register
  primary; I could not add it as a second primary here, so the mechanism is stated
  accurately and attributed to the reading secondary (Democracy Docket, which read
  the 27-page ruling). If the desk wants EO 14399 cited in-item as a primary, the
  per-item policy or the item's structure needs a decision.
- CPI: the BLS June release is the single primary; per the evidence record that
  page also carries the July release-schedule note, so it owns both the June
  figures and the "due Wednesday, not yet posted" fact. I did not add the separate
  BLS release-schedule page as a second primary.

## No warnings left standing

Zero WARN in the full proof; nothing intentionally left.

## Open question

The Epstein order's exact docket home is unresolved in the evidence (civil docket
1:15-cv-07433 vs. a possible grand-jury miscellaneous docket); I cited the civil
docket per the brief and kept the document scope to Giuffre-civil records only. A
retrievable order PDF for either court item would let the holdings link the
opinion text directly rather than the gated docket landing page.
