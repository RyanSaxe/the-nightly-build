# writer brief: daily-brief/2026-10-02 (01)

Inputs (read all; do not tour the repo or history beyond these):
- editorial-direction.md (../../editorial-direction.md) — the binding standard
- commission.md (../../commission.md) — the assignment and boundaries
- voice-guide.md (../../writing-coach/01/voice-guide.md) — the two registers
- evidence.md (../../researcher/01/evidence.md) — the complete claim set and the
  researcher's recommended six plus backups
- commission.md "Recent patterns" section — desk habits to break

Article to edit (in place):
/home/user/the-nightly-build/.nb-work/daily-brief/2026-10-02/library/daily-brief/2026-10-02.html

Output: draft-handoff.md (./draft-handoff.md)

Proof (run verbatim, links included, until BLOCK: 0):
/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-10-02/library/daily-brief/2026-10-02.html --series daily-brief --repo /home/user/the-nightly-build

Work from these inputs. Where something you need is missing, ask me (the
orchestrator); do not invent evidence.

Build the six items in the template's fixed order: Word of the Day, then three
news, then two technology. Use the researcher's recommended six, which already
fit that order:
1. Word: quagmire.
2-4. News: the Supreme Court granting review of the no-bond mandatory-detention
   case; Tennessee's failed execution of Christa Pike and Governor Lee halting
   the remaining 2026 execution; the completed U.S. exit from Iraq / end of
   Operation Inherent Resolve there. Order the three by importance of what
   happened, strongest first.
5-6. Technology: Google Gemini 4 Argon (limited release); Cloudflare Clef and
   Clef-flash open-weight decision models.
If you judge a backup stronger or find a recommended item does not hold up in
the record, tell me before swapping; do not substitute silently.

Carry the record's limits into the prose as the honest evidence-status line each
item needs, and VARY the construction item to item (see recent-patterns.md; do
not let two items close on the same "X; it does not establish Y" shape):
- Iraq: the CENTCOM/Pentagon release is gated; attribute the withdrawal wording
  to the independent reporting the record cites, and note a U.S. official would
  not say how many personnel remain. Anchor the item on the primary records the
  researcher kept (the 2024 joint statement, the Iraqi PM statement).
- Tennessee: Governor Lee's written statement is not on tn.gov; his words come
  through AP/NBC/WSMV. Attribute them. Use the Supreme Court docket/order and the
  TDOC statement as the primaries.
- Both technology items rest on benchmark figures the companies produced
  themselves; say so, and name any independent evaluation the record has (Vals,
  Artificial Analysis for Gemini; The Register's self-reported-scores caveat for
  Cloudflare).

Standards and mechanics:
- Every item cited with at least one primary and one independent secondary;
  number sources in first-citation order; data-nb-kind honest; 12+ sources total.
  Add data-nb-locator where the record gives one.
- Word card is fixed furniture: one-sentence definition cited to the dictionary
  authority, then origin and one documented moment cited to the independent word
  history. Tell quagmire's history in whatever order its story wants.
- Set nb-meta slug and date to 2026-10-02 (the skeleton still shows a
  placeholder), fill harness and model, write a title and a dek that are NOT a
  semicolon/comma roundup of the items (recent-patterns.md); make the nb-meta dek
  and rendered dekline identical.
- Keep each item tight. Your prose meets spec/slop.md; check headline/dek and
  every item head against spec/headlines.md. Run ./nb stamp then the proof until
  BLOCK: 0. Put your one-sentence original-work statement (selection + honest
  status) in draft-handoff.md.
