# Draft handoff — writer/01 — tech-news/2026-07-31

## Original work
This piece's one act of original work: it separates what each vendor/institution
claimed from what an independent party could confirm, in every one of the four
items, and carries forward the specific caveat the evidence record flagged for
each (DeepMind's own unflattering multi-finger success-rate range next to its
92% headline number; the EU's "sovereignty" framing next to Euronews's finding
that most of the "committed" public funding is not yet committed and the named
chip suppliers are non-EU; Noma's marketing-adjacent scale claims held apart
from the GitHub advisory's audited technical facts, plus the advisory's own
admission that patching does not undo prior compromise; and Nature's News desk
correction that HRL was not the sole entrant in this result, and that silicon
spin qubits still trail rival platforms on raw scale). None of these
juxtapositions exist pre-assembled in any single cited source; building them
required reading each item's primary against its independent secondary and
keeping the two voices separate on the page.

## Article changed
`.nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html` (initialized
skeleton replaced with 4 items, no assets/charts added — none of the four
evidence items had a chart-ready primary visual or a clean asset-capture
candidate per the evidence record's "Source assets" section, so the brief
runs as pure wire-service prose, matching the template's own minimalist
recent examples).

## Selection judgment
Wrote all four items the researcher verified; none padded, none dropped.
Order (not significance-ranked by the researcher, my call): Ruflo/RufRoot
leads because it is the most immediately actionable and highest-severity
verified fact of the night (CVSS 10.0, unauthenticated RCE, in production
right now for any unpatched deployment), ahead of Gemini Robotics 2 (major
AI capability step, but bounded by DeepMind's own disclosed limits and an
early-access-only release), the EU Gigafactory call (consequential
industrial policy with real technical substance — chip-scale infrastructure
— but a multi-year runway before anything ships), and the HRL quantum result
(a genuine peer-reviewed physics advance, but the field context makes clear
it moves relative fidelity, not absolute standing). Title and dek center on
the Ruflo item, following the pattern in the recent library (title
foregrounds the lead item, not a summary of all four).

One evidence-record judgment call worth flagging explicitly: the "at least
100,000 AI chips per site" figure the commission's candidate brief asked
for is NOT in the article. The evidence record itself flags this figure as
attested only by unread search-snippet convergence across outlets, not by
a source the researcher actually opened and read in full — citing it would
have violated "cite only what you have read." I cut it rather than invent
a citation; the item stands on the funding and timeline figures, which are
fully sourced.

Similarly, for item 1, the "Noma disclosure + GitHub Security Advisory
(primary)" wording in the commission read to me as the correspondent
already deciding GHSA is the item's anchor primary. I followed that: GHSA
is the sole `data-nb-kind="primary"` source in item 1 (the series enforces
exactly one primary per item), with Noma's blog and The Hacker News both
filed as independent secondaries. Noma is where the "233 tools" and
attack-scope detail originate, so it is cited by name in the prose with
its own citation, just tagged secondary for the per-item accounting — it
is not being hidden or under-credited, only structurally counted as the
supporting account alongside the vendor's own official advisory.

I also addressed the evidence record's flagged contradiction on Ruflo's
scale numbers directly in the first two sentences of item 1: the ~10
million downloads / 1 million active users figures are attributed to Noma
by name and explicitly marked as coming from the disclosing firm, not an
independent audit, rather than adopted as narration.

## Counts
- Items: 4 (template band 4–6, per the commission's own floor of 4–6 and
  the researcher's honest four-item slate)
- Sources: 9 (5 primary, 4 secondary; template floor is 5 minimum)
- Per item: item 1 has 1 primary + 2 independent secondaries; items 2–4
  each have 1 primary + 1 independent secondary
- Words: 934; reading time: 4 min

## Proof result
```
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```
Final result: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**

Two WARNs surfaced mid-draft and were fixed, not left standing:
- `B-SOURCE-KIND` (a BLOCK, not a WARN): item 1 initially carried 3 sources
  tagged `primary` against the series' "exactly 1 primary per item" rule.
  Fixed by reclassifying as above.
- `W-SENTENCE-DENSITY` (multiple instances): several sentences ran past 40
  words with 2+ clause joins. Split throughout; confirmed a following
  `nb check` run showed zero remaining density warnings.
- `W-SELF-COUNT`: `nb-meta` words/reading_minutes were left at placeholder
  0 during drafting; updated to the tool's counted 934 words / 4 minutes
  after the text was final.

No warnings remain unresolved.

## Remaining evidence or voice questions
None blocking. One item for the desk's awareness rather than a request: the
Nature News piece (item 4's secondary) sits behind a cookie/redirect wall
that required following a multi-hop redirect chain to read; I re-verified
it resolves directly via `nb check`'s own link check (included in BLOCK: 0
above), so it is not a live risk, just worth knowing if a future revision
re-fetches it.
