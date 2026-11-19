# editor brief: reinforcement-learning/specification-gaming (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/editorial-direction.md: the layered editorial direction
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/commission.md: topic, one idea, case, boundaries, decisions after research, recent-pattern notes
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/writer/01/brief.md: the exact writer brief
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/writing-coach/01/voice-guide.md: the pinned series voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/writer/01/draft-handoff.md: including the seed, cell and removal checks to rerun
- The lesson: /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/library/reinforcement-learning/specification-gaming.html
- Code, outputs and throwaway checks: /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/code/
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/agent-artifacts/reinforcement-learning/specification-gaming/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/library/reinforcement-learning/specification-gaming.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me. Earlier lessons the page
links can be read with /home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>.

This round's focus: rerun every listing exactly as printed and the handoff's checks; verify the
discount-window derivation (including the lower edge near 0.514, which needs explaining, since
a looping policy beating finishing at a low discount is counterintuitive) against value
iteration; check every number on the page against printed output and both SVGs against it.
The headline is long; hold it to spec/headlines.md. Check the "Why this matters" close and the
headings against the recent-pattern notes. The writer reports prose at the template's ceiling.
The OpenAI post stays described, not quoted, per the commission. Confirm span.nb-math-in is
acceptable by the proof and the rendered page. Look at the rendered page at 390 and 1280 px in
both themes (nb preview plus Playwright; Chromium is preinstalled). Re-run nb stamp and the
proof after any edit.
