# writer brief: expert-tools/atuin (01)

Inputs:
- `agent-artifacts/expert-tools/atuin/editorial-direction.md` — house standard, press voice, series prompt, declared reader
- `agent-artifacts/expert-tools/atuin/writing-coach/01/voice-guide.md` — how this piece should sound
- `agent-artifacts/expert-tools/atuin/researcher/01/evidence.md` — the complete claim set available to you
- `.nb-work/expert-tools/atuin/library/expert-tools/atuin.html` — the initialized article to edit in place
- `.nb-work/expert-tools/atuin/.nb-context/` — effective template contract, runtime assets, furniture catalogs

Output: `agent-artifacts/expert-tools/atuin/writer/01/draft-handoff.md`
Proof: `./nb check .nb-work/expert-tools/atuin/library/expert-tools/atuin.html --series expert-tools --library /home/user/library-checkout`

Focus this round: show, on a concrete shell example, what the recorded context
(directory, exit code, duration) lets a user ask that a flat `.bash_history`
cannot answer at all, and weigh honestly whether that is worth the shell hook and
daemon for a terminal-native engineer. The example proves the value; it is not an
install tutorial. Cover maintenance and the sync-server trust question because the
prompt requires them. Name Atuin and the work it changes in the headline and
section titles. Use `nb-code`/`nb-code-head` for the shell example.

Recent habits to break (see commission): vary the tool-name-plus-verb headline
construction rather than copying recent pieces' rhythm, and do not reuse the
maintenance-closer heading mold ("What it costs, and whether to trust it", the
install-count-in-the-headline device).
