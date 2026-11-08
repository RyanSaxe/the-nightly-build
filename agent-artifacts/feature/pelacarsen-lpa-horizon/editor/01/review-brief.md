# editor brief: feature/pelacarsen-lpa-horizon (01)

Inputs:
- agent-artifacts/feature/pelacarsen-lpa-horizon/editorial-direction.md: the standing directions
- agent-artifacts/feature/pelacarsen-lpa-horizon/commission.md: the assignment, its decisions, and the recent-pattern notes (section "Recent patterns to break" or "Boundaries")
- agent-artifacts/feature/pelacarsen-lpa-horizon/writer/01/brief.md: the exact writer brief
- agent-artifacts/feature/pelacarsen-lpa-horizon/writing-coach/01/voice-guide.md: how it sounds
- agent-artifacts/feature/pelacarsen-lpa-horizon/researcher/01/evidence.md: the claim set, opened only when a concern calls for it
- agent-artifacts/feature/pelacarsen-lpa-horizon/writer/01/draft-handoff.md: the writer's handoff
- library/feature/pelacarsen-lpa-horizon.html: the article you edit in place

Output: agent-artifacts/feature/pelacarsen-lpa-horizon/editor/01/editorial-review.md, and the edited article
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/pelacarsen-lpa-horizon/library/feature/pelacarsen-lpa-horizon.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Open every citation href as printed. This round's focus: the article's own arithmetic (the nmol/L to mg/dL conversion, the 0.41 trial-length discount, the 0.21 to 0.27 bound, the Schoenfeld power figures). Recompute each from the handoff, and cut any step that rests on an assumption no source supports, rather than leaving it labelled. The headline claims "as far as one genetic study required": test it against the record. After direct edits, run `/home/user/the-nightly-build/nb stamp` on the article and the proof until BLOCK: 0.

Preview: `/home/user/the-nightly-build/nb preview --preview <workspace> --out <scratch-dir>`, then `cd /tmp && node /home/user/the-nightly-build/.nb-work/tools/capture.cjs <scratch-dir> library/<series>/<slug>.html <shots-dir>` saves phone and desktop screenshots in light and dark plus the visible text. Playwright and Chromium are preinstalled.

All relative paths are under /home/user/the-nightly-build/.nb-work/feature/pelacarsen-lpa-horizon/.
