# writer brief: current-events/2026-08-28 (02)

The two blocked items now have resolvable primaries (researcher/02/evidence.md).
Apply them and re-prove to BLOCK: 0. No prose rework beyond wiring the primaries
and the one date correction; keep the two valid items and all settled prose.

- Item 3 (Hormuz/CENTCOM): add the primary
  https://www.dvidshub.net/video/1020941/centcom-commander-provides-operational-update
  (CENTCOM operational update, Adm. Brad Cooper, Aug 27 2026) as the item's one
  primary. Keep it framed as a contested US claim (Iran/JMIC dispute the "lanes
  open" reading). The two US secondaries (gCaptain, The Hill/UPI) quote the wording.
- Item 4 (ballroom): add the primary
  https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/26a203.html
  (SCOTUS docket, Application No. 26A203, Roberts' Aug 21 stay). CORRECTION: cite
  the docket's date — the stayed injunction was "entered on April 16, 2026", not a
  March ruling. Fix any date/framing that relied on the SCOTUSblog gloss.

Inputs:
- researcher/02/evidence.md — the two secured primaries with locators and the date correction
- writer/01/draft-handoff.md — your round-01 draft state and the two blocking items
- the article: .nb-work/current-events/2026-08-28/library/current-events/2026-08-28.html

Output: writer/02/draft-handoff.md.
Proof (rerun complete, links included):
./nb check .nb-work/current-events/2026-08-28/library/current-events/2026-08-28.html --series current-events --library /home/user/library-checkout
until BLOCK: 0 (nb stamp if counts change). Do the display-text self-test on the two changed items.
