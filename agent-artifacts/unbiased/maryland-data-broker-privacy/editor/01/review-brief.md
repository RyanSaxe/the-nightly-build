# Editor review brief: unbiased/maryland-data-broker-privacy (01)

Inputs:
- `../../editorial-direction.md` — the governing standard, including the unbiased template identity (two evidence-backed positions, no house verdict) and strict-mode gates.
- `../../commission.md` — the contested question, the two positions to steelman, the anchoring event (2026-08-20), the strict source floor (min 10; >=4 primary, >=3 secondary), and the recent patterns to break.
- `../../writer/01/brief.md` and `../../writer/01/draft-handoff.md`.
- `../../researcher/01/evidence.md` — per-side claims with resolving URLs and primary/secondary marks; note the writer's flag that the filed complaint PDF is not publicly reachable and its contents are sourced through NPR and the We Are CASA release.
- The article: `.nb-work/unbiased/maryland-data-broker-privacy/library/unbiased/maryland-data-broker-privacy.html`.

Proof: `./nb check .nb-work/unbiased/maryland-data-broker-privacy/library/unbiased/maryland-data-broker-privacy.html --series unbiased --library /home/user/library-checkout`

## Round focus (strict mode — structure and citation are hard gates)
Fresh-eyes read at high effort. This is the edition's hardest neutrality test:
- Both positions must be genuinely steelmanned from real evidence, not one built
  as a strawman. Check that Position B (the data broker / commercial-speech /
  statutory-scope side) is argued at the same strength as Position A, and that
  the piece reaches no house verdict.
- Verify no claim rests on the un-reachable complaint PDF beyond what NPR and the
  CASA release actually support; a claim the argument leans on that is sourced
  only to a secondary paraphrase should be softened to what the source carries or
  cut. Confirm the statute text, Sorrell v. IMS Health, and the DPPA are cited to
  primary records that resolve.
- Confirm the strict structure: exactly two flex side sections built from the
  nb-side-* components, min 10 sources with >=4 primary and >=3 secondary.

## Recent patterns to catch
Compare against recent unbiased pieces (`NB_LIBRARY=/home/user/library-checkout ./nb history --series unbiased`):
- Title/dek: reject the blunt-statement-then-reframe two-sentence combo and any
  "leaving open whether" / "where Y left it" participial close.
- Reject two short opposing noun-phrase side headings built the same way.
- The no-verdict close must not read as a stamp; confirm the two camps are built
  differently and the piece does not lean solely on dueling quotes.

Fix prose, structure, and documented furniture in place; route to the writer only
for something needing new evidence or a re-argued side.
