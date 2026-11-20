# writer brief: reinforcement-learning/potential-based-shaping (01)

Inputs:
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/editorial-direction.md — standing directions, template contract and series prompt
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/commission.md — topic, one idea, case, limits, boundaries, decisions after research, recent-pattern notes (read the notes: they list the openers, closers, headline and heading shapes to break)
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/writing-coach/01/voice-guide.md — the pinned series voice guide
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/researcher/01/evidence.md — the evidence record
- The prior lessons the page links, via `./nb history --show reinforcement-learning/<slug>`: specification-gaming (race.py, to reuse or import), termination-and-truncation, sarsa-and-q-learning, finding-optimal-policies
Output: .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/writer/01/draft-handoff.md, and the article at .nb-work/reinforcement-learning/potential-based-shaping/library/reinforcement-learning/potential-based-shaping.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/potential-based-shaping/library/reinforcement-learning/potential-based-shaping.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Run environment: keep lesson code and scratch runs under .nb-work/reinforcement-learning/potential-based-shaping/ (code files beside the article where the template contract expects them). Chromium and Playwright are pre-installed (require('playwright') in node, or python playwright if available); do not run playwright install or scripts/install-figure-capture.sh. Use `nb preview` and capture phone and desktop widths in light and dark to check every SVG. Prefix nb commands with `export UV_SYSTEM_CERTS=1; unset UV_NATIVE_TLS;`.
