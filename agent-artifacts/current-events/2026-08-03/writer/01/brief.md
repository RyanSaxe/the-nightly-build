# writer brief: current-events/2026-08-03 (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `brief` template identity, series prompt
- commission.md (artifact root) — what the brief is, per-item sourcing, coordination, shapes to break
- writing-coach/01/voice-guide.md — compression standard, licenses (consequence line, complication turn, dry wit), do-not-reuse list
- researcher/01/evidence.md — the ONLY claim set available; use its per-item primary+secondary, Numbers, and Contradictions exactly
- The initialized article at `library/current-events/2026-08-03.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/current-events/2026-08-03/library/current-events/2026-08-03.html --series current-events`
  `./nb check .nb-work/current-events/2026-08-03/library/current-events/2026-08-03.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- Build from the strongest researched items (each exactly one primary in the
  headline link + at least one independent secondary): (1) Spokane/Washington
  wildfire emergency; (2) Iran-affiliated cyberattacks on US water systems
  (CISA/FBI advisory) — this earns its Current Events slot on the public-
  consequence test and does NOT overlap tonight's Tech News items; (3) Capital
  One's motion to dismiss the Trump Org debanking suit; (4) US-Iran talks
  resuming 2026-08-03 + the Hormuz arrangement (carry-forward: report what is
  NEW on 8/3, not the already-covered canceled strike).
- Item 5 (the House stopgap/CR) is SOFT: the 8/3 movement is a scheduled
  cloture vote whose outcome the evidence could not confirm, and the
  House/Senate end-dates conflict. Include it ONLY if you can state precisely
  what is confirmed as of 8/3 without asserting an unconfirmed vote outcome;
  otherwise drop it (four items still meets the floor) rather than pad. Do not
  use the In-N-Out shooting (routine tragedy, fails the standard).
- Accuracy cautions from the evidence: wildfire counts are preliminary and vary
  by hour/source (~600-700 structures, ~60,000-65,000 evacuated) — attribute to
  source/time, do not state a single settled number. Water-attack attribution
  is contested (standing Iran attribution for the campaign, no definitive
  federal attribution of these specific breaches; Trump blamed Minnesota's
  governor) — say plainly what is and isn't established. The two Iran-linked
  items (diplomacy vs. infrastructure) are distinct, not duplicative.
- Each item's prose leads on the consequence/complication, not the recap; one
  judgment per item; no feed-style bold axiom labels.
- Dek is the night's through-line in one sentence, a stance; avoid the banned
  dek molds and the paired-adjective-triad headline.
- Brief template: 4-6 `nb-brief-item` blocks + Sources. Shortread. min 5 sources
  overall (the per-item primary+secondary rule is the real constraint).
