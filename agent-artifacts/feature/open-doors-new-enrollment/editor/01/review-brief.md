# editor brief: feature/open-doors-new-enrollment (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: story, boundaries, recent patterns to break (your
  recent-pattern notes), and decisions after research
- writer/01/brief.md: the exact writer brief
- writing-coach/01/voice-guide.md: the voice
- researcher/01/evidence.md: open when a concern calls for it
- writer/01/draft-handoff.md: the writer's notes
- the article: /home/user/the-nightly-build/.nb-work/feature/open-doors-new-enrollment/library/feature/open-doors-new-enrollment.html
  (chart scripts and PNGs beside it in library/feature/open-doors-new-enrollment/)
Output: editor/01/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/open-doors-new-enrollment/library/feature/open-doors-new-enrollment.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
You may use `nb history` to compare against the recent record.

Test hardest: the headline's "more than half" (the writer's 38,461 / 73,135
arithmetic: is the denominator the enrolled fall IIE's tables give, and is
"offset" fair when the two numbers are different populations' stocks?);
every component and India/China figure against IIE's Table 8 and Fast Facts;
the "other places" figures, which are by subtraction; whether the conceptual
flow drawing (Fig. 3) implies anything the record does not support. The
recent record's headlines lead with a ratio against a second quantity; judge
whether this headline repeats that formula and rewrite if so. Strict 600–1200
words.

Look at every figure rendered (nb preview; Playwright via
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`; never
`playwright install`), at phone and desktop width, both themes. Run nb as
/home/user/the-nightly-build/nb (export UV_SYSTEM_CERTS=1). After edits run
`nb stamp` and the proof until BLOCK 0. Keep scratch out of library/ and
agent-artifacts/. Do not commit or push.
Editor model: the orchestrator's model (inherit), effort high.
