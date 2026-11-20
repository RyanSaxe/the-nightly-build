# editor brief: reinforcement-learning/potential-based-shaping (01)

Inputs:
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/editorial-direction.md — standing directions, template contract and series prompt
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/commission.md — the commission, decisions after research and during drafting, and the recent-pattern notes (headline, bookend, takeaway and heading habits of the last five lessons)
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/writer/01/brief.md — the exact writer brief
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/writing-coach/01/voice-guide.md — the pinned series voice guide
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/researcher/01/evidence.md — evidence record
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/writer/01/draft-handoff.md — writer's handoff, with the checks it ran and the warnings it left
- The article: .nb-work/reinforcement-learning/potential-based-shaping/library/reinforcement-learning/potential-based-shaping.html; extracted listings in .nb-work/reinforcement-learning/potential-based-shaping/lesson-code/
- Prior lessons it links, via `./nb history --show reinforcement-learning/<slug>`
Output: .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/potential-based-shaping/library/reinforcement-learning/potential-based-shaping.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Rerun every listing exactly as printed (uv run) and check each printed number and each SVG chart against the output. Check the derivation line by line, in particular the sign of the per-lap shaping amount with Φ = −(moves left) and the truncation argument, which no source covers. Look at the rendered page (`nb preview`, pre-installed Playwright; do not run playwright install). After any edit rerun `nb stamp` and the proof until BLOCK: 0. Prefix nb commands with `export UV_SYSTEM_CERTS=1; unset UV_NATIVE_TLS;`.
