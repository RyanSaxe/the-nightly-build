# writer brief: feature/pelacarsen-lpa-horizon (01)

Inputs:
- agent-artifacts/feature/pelacarsen-lpa-horizon/editorial-direction.md: the standing directions
- agent-artifacts/feature/pelacarsen-lpa-horizon/commission.md: the assignment, boundaries and the recent patterns to break
- agent-artifacts/feature/pelacarsen-lpa-horizon/writing-coach/01/voice-guide.md: how it sounds
- agent-artifacts/feature/pelacarsen-lpa-horizon/researcher/01/evidence.md: the complete claim set
- .nb-context/: the effective template contract, runtime assets and furniture catalogs
- library/feature/pelacarsen-lpa-horizon.html: the initialized article you edit

Output: agent-artifacts/feature/pelacarsen-lpa-horizon/writer/01/draft-handoff.md, and the edited article
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/pelacarsen-lpa-horizon/library/feature/pelacarsen-lpa-horizon.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Read the "Decision after researcher/01" section of the commission first. Five-minute read: open with the finding in two or three sentences, then build each section around a visual. The required contribution in the commission is the arithmetic placing the achieved absolute Lp(a) reduction against the genetic estimates, with units stated; show it as a drawing or table. Look at every visual at phone and desktop width in both themes.

Preview: `/home/user/the-nightly-build/nb preview --preview <workspace> --out <scratch-dir>`, then `cd /tmp && node /home/user/the-nightly-build/.nb-work/tools/capture.cjs <scratch-dir> library/<series>/<slug>.html <shots-dir>` saves phone and desktop screenshots in light and dark plus the visible text, and prints any horizontal overflow. Do not run scripts/install-figure-capture.sh; Playwright and Chromium are preinstalled.

All relative paths are under /home/user/the-nightly-build/.nb-work/feature/pelacarsen-lpa-horizon/. Writer model: record the model you run on and the harness "Claude Code" in nb-meta.
