# Writer brief — opinion/mail-in-voting-order (01)

## Your job
Draft the argued opinion from the commission, voice guide, and evidence record,
then prove it to BLOCK: 0.

## Exact inputs (start here)
- `agent-artifacts/opinion/mail-in-voting-order/commission.md`
- `agent-artifacts/opinion/mail-in-voting-order/editorial-direction.md`
- `agent-artifacts/opinion/mail-in-voting-order/writing-coach/01/voice-guide.md`
- `agent-artifacts/opinion/mail-in-voting-order/researcher/01/evidence.md`
- Initialized article: `library/opinion/mail-in-voting-order.html`
- `.nb-context/` (template contract, runtime assets, furniture)

## Write
1. `library/opinion/mail-in-voting-order.html`:
   - `opinion` geometry: `position` anchor (the `nb-position` card) + 2–5 flex
     argument sections + `counter` (mandatory) + `Sources`. Words **900–2500**
     (measured). Every section cited.
   - **Position card**: the stance in one sentence (the Elections-Clause argument
     from the commission), and under it the **named holders who actually hold it**,
     cited (the state AGs / the judges / named scholars from the evidence record).
     The card does the disclosing; the **title and dek must NOT restate it** — they
     sell the question or the consequence.
   - Build each argument section from the cited record (EO text, district order,
     1st Circuit majority, filings). Quote precisely; get the mechanics exactly
     right (distinguish the citizenship-list provisions from the mail-ballot
     provisions; state which remain blocked). Keep reported fact / synthesis
     distinct; no "hinted/implied/signalled".
   - **Counter section**: state the strongest opposing case (the DOJ/SG's actual
     argument + named defenders) in the form its believers would sign, cited, then
     answer it on the law. A knock-down strawman fails the piece.
   - Close on what the argument earned and **name what evidence would change the
     desk's judgment** (from the commission's accountability note).
   - `nb-meta` ACTUAL values: title, dek, date `2026-08-01`, mode `open`, order
     null, tags, measured sources/words/reading_minutes, harness `claude-code`,
     model `claude-sonnet-5`.
   - Number sources first-citation order; honest `data-nb-kind` (court opinions,
     the EO, filings = primary; reporting = secondary). Only verified sources;
     every URL resolves.
2. `writer/01/draft-handoff.md`: the visible original work (the specific legal
   argument the piece advances and the steelmanned counter it answers), warnings
   resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/opinion/mail-in-voting-order.html --series opinion --repo /home/user/the-nightly-build` → **BLOCK: 0**.

## Rules
- Legally sensitive: argue only what the cited record supports; do not overstate.
  Documented furniture only; no active content; preserve fixed engine
  assets/classes/labels (incl. the position card chrome). Begin with named inputs;
  `REQUEST researcher` for a missing citation rather than assert. No repo/archive tour.

## Report
End with: `DONE writer library/opinion/mail-in-voting-order.html`
