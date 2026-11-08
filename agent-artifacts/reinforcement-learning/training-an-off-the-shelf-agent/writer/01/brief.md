# writer brief: reinforcement-learning/training-an-off-the-shelf-agent (01)

Inputs:
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editorial-direction.md: the standing directions
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/commission.md: the assignment, boundaries and the recent patterns to break
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/writing-coach/01/voice-guide.md: how it sounds
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/researcher/01/evidence.md: the complete claim set
- .nb-context/: the effective template contract, runtime assets and furniture catalogs
- library/reinforcement-learning/training-an-off-the-shelf-agent.html: the initialized article you edit

Output: agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/writer/01/draft-handoff.md, and the edited article
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/library/reinforcement-learning/training-an-off-the-shelf-agent.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Read the "Decisions after researcher/01" section of the commission first. Earlier lessons' text: `/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>`. Reuse their files by import, and print in full any file a listing needs that no earlier lesson printed. Run every listing exactly as printed with `uv run` in a scratch folder under /tmp/claude-0/rl-lesson/, and keep the runs to a few minutes on CPU. List each seed, cell and removal check in draft-handoff.md so the editor can rerun it. Draw charts of the lesson's own runs as inline SVG with theme variables and check them against the printed output. Write the 30-word main-idea sentence in draft-handoff.md first. The voice guide is the series' pinned guide.

Preview: `/home/user/the-nightly-build/nb preview --preview <workspace> --out <scratch-dir>`, then `cd /tmp && node /home/user/the-nightly-build/.nb-work/tools/capture.cjs <scratch-dir> library/<series>/<slug>.html <shots-dir>` saves phone and desktop screenshots in light and dark plus the visible text, and prints any horizontal overflow. Do not run scripts/install-figure-capture.sh; Playwright and Chromium are preinstalled.

All relative paths are under /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/. Writer model: record the model you run on and the harness "Claude Code" in nb-meta.
