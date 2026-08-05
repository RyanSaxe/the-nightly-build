# writer brief: investing/free-cash-flow (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/editorial-direction.md — governing standard, `lesson` template identity, series prompt, declared reader (smart, new to this subject)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/commission.md — the concept, the 2-3 ideas, worked-example obligation, bookend rules, Background links
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/writing-coach/01/voice-guide.md — craft (definition+figure as one motion; bookends = same argument at two altitudes; one bounded second-person license)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/researcher/01/evidence.md — verified definition, construction, and the Apple FY2025 worked figures; cite only what it opened
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/library/investing/free-cash-flow.html — the initialized lesson to edit
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/.nb-context/ — effective template contract and furniture catalogs (table/equation)

Output: /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/library/investing/free-cash-flow.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

Focus:
- `lesson` template, fixed order: **Why this matters** bookend → body → **The takeaway** bookend. Write the body FIRST; write both bookends after, describing the lesson actually written. Per the coach: opener names the specific way an FCF number gets misread/gamed; takeaway hands back the specific test that catches it (same argument, two altitudes). Neither bookend summarizes the body. Word band 1200-2200.
- Teach 2-3 ideas COMPLETELY (cut, don't shrink): (1) what free cash flow is and why it is the number that matters — the cash left for all capital providers after the investment needed to sustain/grow the business; build on the published `profit-versus-cash` lesson (link in Background, don't re-teach accrual-vs-cash). (2) How to build it from the statements, with the verified **Apple FY2025 worked example** line by line: operating cash flow 111,482 − capex (payments for acquisition of PP&E) 12,715 = FCF 98,767 (USD millions; FY ended 2026-09... use the evidence's exact dates: year ended Sep 27 2025, 10-K filed Oct 31 2025). Introduce each term (capex, working-capital change, non-cash add-back like D&A) with its real Apple figure in the next sentence (coach's "definition+figure as one motion"). (3) If it fits without shrinking 1-2: the honest trap — Apple's FCF FELL ~9% (108.8B FY2024 → 98.8B FY2025) even as net income ROSE ~19% (93.7B → 112.0B), driven by working-capital swings and higher capex — proving FCF ≠ profit and must be judged over time. If this crowds the lesson, make it a future lesson instead.
- **Accuracy/honesty from the evidence:** FCF is a CONSTRUCTED, non-GAAP measure with no uniform definition — say so plainly and cite the SEC C&DI (102.07) that says it. Teach WHICH FCF you mean (the SEC "operating cash flow − capex" version for the worked number; name FCFF vs FCFE distinction from Damodaran but do not conflate them with the OCF−capex number — they start differently). Note capex is not split maintenance-vs-growth in the filing. Every Apple figure must match the evidence's re-read primary; cite the 10-K/EDGAR page. Anchor the statement-of-cash-flows structure to IAS 7 (its page resolves); ASC 230 may be named in prose (FASB's codification is login-gated, so do not use a non-resolving FASB href).
- Background band = optional prior reading (link the relevant earlier investing lessons: profit-versus-cash, what-a-company-owns-and-owes, present-value). Go deeper = optional afterward reading beyond this paper. The lesson must stand for a reader who opens none.
- Use `nb history --structure investing/profit-versus-cash` (and return-on-capital) for continuity and to break their opener/closer/heading shapes.
- A small worked-calculation TABLE (the OCF→FCF bridge, and/or the FY2024-vs-FY2025 comparison) is welcome if it carries reasoning — build only from the verified numbers.
- Name the piece's one act of original work in draft-handoff.md. Run `nb stamp` then the exact proof to BLOCK: 0, links included.
