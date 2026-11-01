# researcher brief: daily-brief/2026-11-01 (01)

Inputs:
- `../../editorial-direction.md` — the standing editorial standard and the Daily Brief series direction.
- `../../commission.md` — the chosen six-item slate, the ranked backups, and the standing instructions.
Output: `evidence.md` (write it beside this brief).

Work from these inputs. You have web search/fetch. Do not tour the repository.
Where something you need is missing, ask me (the orchestrator).

Your job is to confirm each of the six chosen items against a strong source and
to hand the writer a clean citation per item (min 6 sources total). The slate is
already chosen in the commission; do not swap an item for a different story on
your own taste. You MAY substitute from the commission's ranked backups if and
only if a chosen item cannot be verified to a solid source — if you do,
say so explicitly in your summary and explain why.

For each of the six items, record:
- The one fact that anchors it (what happened, who did it or claims it, what
  follows), in the form the writer needs.
- The exact date (confirm it is within the last two days where the commission
  says so; for the Word of the Day the dates are historical).
- One strong source: prefer the underlying record (court filing/docket, agency
  or company statement, the vendor's own security notice, the Yale announcement,
  a dictionary authority) over coverage of it. Give the exact URL, the
  publisher, a short verbatim quote of the key clause, and the retrieval date.
  Add a second source only where the first is disputed or cannot settle the
  claim; the Word of the Day takes two (definition authority + coinage history).
- Any figure that is disputed or is a single party's claim, flagged for
  attribution (Iran's mine claims if used; DOJ's allegations; any vendor figure).

Specific checks:
- **bafflegab**: confirm the Merriam-Webster definition and 1952 first-use, and
  an independent coinage history (Worldwide Words / Wordsmith) for Milton A.
  Smith and the OPS price-order story. Note the M-W "possibly" hedge and the
  Green's May-1952 date. If the coinage cannot be cleanly sourced, verify the
  backup `grawlix` (Mort Walker) instead and tell me.
- **Alaska Senate suit**: find the court docket or a filing for the motion to
  dismiss (filed ~10-31) and the ballot-segregation request; confirm Judge
  Gleason and the NVRA theory. Democracy Docket's tracker is a pointer to the
  primary docket, not the citation of record.
- **Arch lawsuit**: find the complaint or court record for DC + Virginia v. NPS/
  Interior (filed ~10-31), the 250-foot figure, and the 2026-11-05 NCPC vote.
- **Nordhaus**: confirm the Yale announcement, the 2018 Nobel, the DICE model,
  age 85, and the 10-30 date.
- **VOLTA (Talos)**: confirm the Cisco Talos post (dated ~10-31), the LLM-ranking
  behavior, and the default model/fallback detail; quote the key line.
- **Cursor / claude-code extension**: confirm Cursor's security notice, the two
  affected build numbers, the ~11-hour window, and the line that Anthropic did
  not build the modified versions and that uninstalling does not remove
  persistence. If this reads as too inside-baseball or cannot be solidly
  sourced, verify a backup tech item (NOT Mistral Large 4 or the Anthropic
  robots.txt draft) and tell me.

Organize `evidence.md` by item (Word, News 1-3, Tech 1-2), each with its anchor
fact, date, source(s) with quote+URL+retrieval date, and any attribution flag.
End with a one-line note of any substitution you made and why. Never invent a
URL, date, outlet, or figure; if you cannot verify an item, say so plainly.
Your own prose meets `spec/slop.md`. When done, reply with a 4-6 sentence
summary and confirm the output path.
