# review-brief: tech-news/2026-08-08 (editor/02)

Inputs:
  ../../editorial-direction.md
  ../../editor/01/editorial-review.md       your prior review (the finding that was routed)
  ../../writer/02/draft-handoff.md          what the writer changed this round
  ../../researcher/01/evidence.md           the claim set (Novee s1; The Hacker News s3; the table)
  the article: .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html

Focused round: writer/02 rewrote the headline, the <h1>, and the item-1 <h3> to
"One untrusted GitHub issue broke three coding agents at the harness, not the model,"
replacing the false "reached code execution in Claude Code, Gemini CLI, and Codex" line.
Everything else was approved in editor/01.

Verify only:
- The new headline/h1/item-1 h3 is a claim the piece and its table establish: code execution
  for Gemini CLI; credential theft (Claude Code) and instruction injection (Codex) — i.e.
  the "harness, not the model" framing is accurate and not itself an overclaim.
- nb-meta dek is byte-identical to the rendered dekline and unchanged; items 2-4, the table,
  and the body are untouched.
- No new banned mold in the rewritten headline (no triad).
Confirm no other required change remains. If clean, approve. After any direct cut, run
`nb stamp` (the writer runs the full proof). Write editor/02/editorial-review.md ending in a
Decision line.
