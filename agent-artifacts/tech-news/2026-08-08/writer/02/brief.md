# writer brief: tech-news/2026-08-08 (02)

Inputs:
  ../../editor/01/editorial-review.md       the finding to apply (read the Required work + Skeptic)
  ../../researcher/01/evidence.md           the claim set (Novee s1; The Hacker News s3; the article's table)
  ../../writer/01/draft-handoff.md          prior handoff
  the article: .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html
Output: writer/02/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

Single required fix (editor/01): the headline and the identical item-1 `<h3>` claim one
issue "reached code execution in Claude Code, Gemini CLI, and Codex," but the record and the
article's own table establish code execution only for **Gemini CLI**; Claude Code's
CVE-2026-54316 is **credential theft** and Codex's flaw is **instruction injection**, not
direct code execution. Rewrite BOTH the headline and the item-1 `<h3>` to a claim the piece
establishes (e.g. that one untrusted GitHub issue subverted all three agents' harnesses,
reaching code execution in Gemini CLI and credential theft / instruction injection in the
others — phrase it precisely and without the triad-headline mold). The dek and body are
correct and stay; keep nb-meta `dek` identical to the rendered dekline. Do not expand the
claim set or touch the other three items. After the edit, make the display-text pass again
(headline + subhead against the evidence) and run the full proof to BLOCK: 0. Keep nb-meta
harness "claude-code-routine" / model "Opus 4.8". Note in the handoff exactly what you
rewrote.
