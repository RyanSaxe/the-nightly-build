# writer brief: daily-brief/2026-10-03 (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; draft only from it.
- commission.md (../../commission.md)
Output: ../../writer/01/draft-handoff.md (edit the article in place at
  .nb-work/daily-brief/2026-10-03/library/daily-brief/2026-10-03.html)
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-10-03/library/daily-brief/2026-10-03.html --series daily-brief --repo /home/user/the-nightly-build

Work from these inputs. Documented markup only (`.nb-context/`). This series is STRICT:
exactly six items in order (Word, News, News, News, Technology, Technology), and each
item carries EXACTLY ONE primary plus AT LEAST ONE independent secondary (>=12 sources
total). Ask me if the evidence cannot supply something.

The final six items are settled (the orchestrator has made the slate calls the
researcher flagged). Use exactly these; do not add, drop, or swap:

1. Word of the Day — robot. Merriam-Webster (primary) + Etymonline (secondary). Noun,
   pronunciation \ˈrō-ˌbät\, a one-sentence definition, then the origin: coined for Karel
   Capek's R.U.R., from Czech robota "forced labour," with Josef Capek credited for
   proposing the word. The two sources differ (M-W: first use 1922, Josef "proposed";
   Etymonline: 1923, Josef "coined" it, used first in a short story). State it cleanly
   and honestly; do not paper over the difference. Keep the card lively, the item short.

2. News — AI-server export-control case (SDNY). Primary: the DOJ OPA release (justice.gov
   /opa/pr/...). Secondary: manufacturing.net (and/or eweek) as the independent account.
   FRAME IT HONESTLY: the indictment is dated 19 March 2026, so this is a standing case,
   not this-week news — write it as the case against the three defendants and its current
   status, not as a fresh event. Keep $2.5B (Company-1's total 2024-25 purchases) and
   $510M (the late-April-to-mid-May-2025 diverted tranche) distinct. Chang is the Taiwan
   office "general manager" (DOJ's word), not "sales manager." Super Micro itself was not
   charged. Current status: Liaw arrested in CA and bailed; Sun detained; Chang at large.

3. News — U.S. Attorney reinstated in Seattle (Rogoff). Primary: the W.D. Wash. docket
   (Rogoff v. Trump, 2:26-cv-02566, Judge Bastian), which GRANTED a preliminary injunction
   on 1 Oct 2026; defendants appealed to the 9th Circuit (26-6445) the same day. Secondary:
   Bloomberg Law or NC Lawyers Weekly for the underlying facts (court-appointed 15 July,
   removed ~54 minutes later). Attribute the "exceeded its authority" to the suit's
   ultra-vires / Appointments-Clause theory and the implied basis of the grant; do NOT
   quote a holding from an opinion no one read. Note the reinstatement is contested and
   could be stayed on appeal.

4. News — overseas-voter form change and the DNC suit. Primary: the Department of War
   emergency OMB information-collection request revising the Federal Post Card Application
   (OMB 0704-0503) — the government's own filing that owns the change. Secondary: NPR and
   AP. The change removed the checkbox letting U.S. citizens who never resided in the U.S.
   identify themselves (a 2016 estimate put that group at ~11,590). The DNC sued on 1 Oct
   2026, calling it "arbitrary and capricious" under the APA. Use the department's current
   name ("Department of War," formerly Defense) accurately; the court/docket for the suit
   was not pinned, so attribute the suit to AP/NPR and do not invent a docket.

5. Technology — PostgreSQL 19. Primary: postgresql.org (Beta 4 announcement and/or the
   Beta 1 feature highlights). Secondary: the Bytebase feature write-up. Headline feature:
   the new REPACK ... CONCURRENTLY command for online table rebuilds (use inline <code>
   for the literal tokens REPACK and CONCURRENTLY). State the status EXACTLY: 19 is still
   in beta (Beta 4, 24 Sept 2026), with a release candidate expected in early October and
   GA targeted around autumn 2026 — NOT yet released. Do NOT present SQL/PGQ property-graph
   queries as a 19 feature: Beta 4 reverted it.

6. Technology — Visual Studio 2026 bring-your-own-key. Primary: Microsoft's VS 2026 release
   notes (learn.microsoft.com) and/or the VS team devblog. Secondary: The New Stack. VS
   2026 v18.10.0 (8 Sept 2026) added BYOK/BYOM: use models from Microsoft Foundry, OpenAI,
   Anthropic, Ollama or a custom endpoint, with or without a GitHub sign-in; it is in
   preview, enabled by default. Report it as a preview capability, not a finished GA
   guarantee.

Recent-habit notes to break (this desk; the editor compares):
- Title molds to avoid: "Six developments for <Weekday>, <Month D>" and "<Month D>: Title
  Case Headline." Title the issue for a genuine through-line or its strongest item.
- Dek mold to avoid: the semicolon-plus-"while" chain ("X lifts A; B hears C, while D and
  E publish F"). Write one lean sentence that is this issue's own.
- Each news item leads on the hard, attributed fact; attribute every unsettled claim to
  its named source and make the status of the evidence clear (the voice guide shows this).

Number sources in first-citation order; carry each kind into `data-nb-kind` (exactly one
`primary` per item). Prefer a locator that lands on the passage. Fill the nb-meta dates,
harness and writer model. Run the proof with `--no-check-links` while iterating, then
`nb stamp` and the exact `nb check` above until BLOCK: 0. Put the one-sentence original-
work note (what this issue's selection/framing does) in draft-handoff.md.
