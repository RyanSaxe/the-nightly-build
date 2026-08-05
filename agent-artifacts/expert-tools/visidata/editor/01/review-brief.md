# review-brief: expert-tools/visidata (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/editorial-direction.md — governing standard, `article` identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/writer/01/brief.md — the exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/writing-coach/01/voice-guide.md — voice guide (read FIRST)
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/researcher/01/evidence.md — the evidence record (source-verified keybindings)
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/writer/01/draft-handoff.md — handoff + original-work sentence + open question
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/library/expert-tools/visidata.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (REQUIRED stage).

Recent-pattern notes:
- Compare the section shapes/headings against a recent expert-tools piece (`nb history --structure expert-tools/<a-recent-slug>`); confirm the outline is argument-shaped for VisiData, not a stock Overview/Usage/Verdict, and that the closer does not point away to a reading list.

This round's focus:
- **Technical accuracy is the core risk.** Every shown keybinding/command must match the evidence's source-verified set (`=`, `+`, `F`, `W`, `M`; group variants `gF`/`g+`/`gM`; `Ctrl+H` docs-backed). Any key NOT in the evidence must not be presented as a verified command. Writer's open question: the pivot walkthrough refers to marking a "key column" as "one more keystroke" WITHOUT naming the key, because the key command (`!`) was not source-verified. Rule: either accept the honest unnamed phrasing (fine to ship) OR, if you want the pivot fully reproducible, route to the researcher to verify `!` against source — do NOT let an unverified key be named on the page.
- Verify the honest claims are exactly as evidenced: version v3.4 (2026-06-30), GPL-3.0, ~9.2k stars, single-primary-author, `max_rows` 1e9 truncation, and especially the **async-loader caveat** (mid-load navigation fine; whole-column results correct only once loaded) — this must not be overstated.
- Audit every `data-nb-kind`: the tool's own docs/source/repo are primary; independent commentary is secondary. 15 primary / 2 secondary was stamped — confirm each labeled primary really is the owner of its claim, not a different site.
- Open every citation href as printed; each must land on the source's own page and resolve.
- Second read (cut): the demonstration must PROVE the one changing move and stop — cut any drift toward an install tutorial or full command tour; the two `nb-code` transcript listings and the comparison table each earn their place or go. Enforce prose/punctuation standards.
- Third read: what does the reader get that the docs alone would not (the original-work sentence in the handoff), and is the prose closer to the voice-guide exemplars (Evans/Willison/Gregg) than a median summary? Reread the headline as the largest claim (must name the tool and the work it changes).
- After any direct cuts run `nb stamp`. Decision: approve or revise, naming each required item's owner.
