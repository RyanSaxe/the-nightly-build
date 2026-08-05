# writer brief: expert-tools/visidata (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/editorial-direction.md — governing standard, `article` template identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/commission.md — the tool, the "one changing move", cost/maintenance obligations
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/writing-coach/01/voice-guide.md — craft standard and licenses (live keystroke walkthrough proving one move; cost stated in the same register)
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/researcher/01/evidence.md — source-verified keybindings, loader behavior, version, maintenance, limitations; cite only what it opened
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/library/expert-tools/visidata.html — the initialized article to edit
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/.nb-context/ — effective template contract and furniture catalogs (code/listing furniture)

Output: /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/expert-tools/visidata/library/expert-tools/visidata.html --series expert-tools --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

Focus:
- `article` template = original analysis. Outline the reasoning first; name flex sections for THIS argument (the one changing move and its cost), not a standard Overview/Usage/Verdict outline. Remove any section whose deletion leaves the reasoning unchanged. Do NOT close on a reading list or a pointer away. Name VisiData and the work it changes in the headline and section titles.
- Build the piece around the source-verified "one changing move": exploratory analysis as interactive keystrokes over a loaded sheet, replacing the pandas/SQL write-run-tweak loop. Show it with the exact confirmed keystrokes — `F` (freq-col), `+` (aggregate-col), `=` (addcol-expr), `W` (pivot), `M` (melt) — in ONE small real session, per the voice guide's license (prove the move and stop; no full command tour, no install tutorial). The demonstration is AUTHORED code/transcript furniture (the researcher found NO legitimate source-asset visual — do not use a screenshot; use the code/listing furniture documented in .nb-context).
- Be honest and precise per the evidence: current version v3.4 (2026-06-30); GPL-3.0; ~9.2k stars; effectively single-primary-author (Saul Pwanson) — state this as the maintenance-trust cost in the same flat register as the capability. State adoption cost concretely (modal keystrokes to learn; where a notebook/SQL is still the right tool; cmdlog replay narrows but does not close reproducibility). 
- **Do not overstate the async loader:** "explore before it finishes loading" is real for navigation/viewing, but whole-column results (counts, sorts, totals) are correct only once loading completes. Say this exactly.
- Do NOT show thread-control keystrokes (Ctrl+T/Ctrl+C) — the researcher did not re-verify them against source and the five core moves do not need them.
- Every command/keybinding shown must match the evidence (source-verified); do not ship a remembered API. Confirm every citation href resolves to the source's own page (visidata.org docs, the GitHub repo/changelog, the author's post).
- Name the piece's one act of original work in draft-handoff.md (the analysis, not a feature list). Run `nb stamp` then the exact proof to BLOCK: 0, links included. Use `nb preview` and inspect the rendered page (especially the code/transcript furniture).
