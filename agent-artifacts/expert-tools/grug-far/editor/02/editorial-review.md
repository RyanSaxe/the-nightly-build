# Editorial review: expert-tools/grug-far (editor/02)

Confirmation re-read after the writer's round-02 repair. Round 01 approved the
piece on the merits and routed two display/structure formula items to the
writer; this round confirms both are resolved and nothing settled regressed.

## Skeptic

No new claims were added, so the round-01 skeptic verdict stands. I re-checked
the settled technical content descriptor by descriptor and every mechanism claim
is intact and unchanged: ripgrep is the default engine and no sed backend
exists; capture syntax is `$1`/`${1}`, never `\1`; the ripgrep engine runs
`rg --replace='${1}Client' --passthrough`; the edit-and-sync move is
ripgrep-engine only and disabled under `--multiline`/`--multiline-dot-all`; the
ast-grep engine runs `ast-grep run --pattern=… --rewrite=… --update-all` and
ships no sync path; version 1.6.76 dated 2026-07-28 (ten days before the article
date, arithmetic still checks); Neovim >= 0.11.0 with tag 1.6.3 for 0.10;
ripgrep required (14+/15), ast-grep optional (0.36+); `maxSearchMatches` = 2000;
two open issues filed 2026-08-04, ~2,000 stars, single maintainer; three
engines. Sources, `data-nb-kind` labels, and hrefs are unchanged. The dek is
unchanged and remains identical across the nb-meta `dek` and the rendered
dekline.

One new heading claim to test: "Swapping in ast-grep drops the sync buffer." It
compresses the settled fact that the ast-grep engine has no sync path. The
section body disambiguates it precisely ("the ast-grep engine ships no sync path
at all, so on it you edit the Replace field and run Replace, never the result
lines"), so the heading commits to a claim the section defends. Held.

## Cut

Required item 1 — headline. Recast to "grug-far opens a project-wide search as
an editable buffer and writes your edits back across files." It is off the
visidata "[Tool] turns [X] into [Y]" frame (new verb pair, opens/writes-back)
and distinct from the rest of the recent shelf. It is identical across the
`<title>` (bar the standard " · Expert Tools" series suffix), the nb-meta
`title`, and the `<h1>`. It commits to a claim the piece defends, in the piece's
own nouns. Length sits within this series' established headline register.
Resolved.

Required item 2 — heading cadence. Of the three "clause, and clause" headings,
two are recast ("Why Replace runs ripgrep, not sed"; "Swapping in ast-grep drops
the sync buffer"), leaving one ("What it costs, and whether to trust it"). A
single instance is not a formula; the drumbeat is broken. The five headings now
vary in shape and each names a step of the argument. The writer also turned two
"not X" contrasts into declaratives — the heading "Editing the matches, not a
replace field" → "Editing the matches themselves," and the orientation body "not
a transient quickfix list but text you can change" → "is editable text" (the
quickfix contrast is carried earlier in that paragraph, so nothing is lost).
Both changes reduce the contrast drumbeat I flagged in round 01 and read clean.
Resolved.

All four round-01 direct cuts are preserved (", not after"; "the thing prose
cannot show and"; the comma-splice "and"; the ast-grep re-tread clause). No new
tell, no new formula: the two gerund-led headings ("Editing…", "Swapping…") are
different shapes and two of five do not stamp.

## Reader

The piece still gives what the sources scatter: the boundary that the
edit-and-sync buffer is a ripgrep-engine feature the ast-grep engine drops,
staged at the pivot. The revisions sharpened the display surfaces without
touching that synthesis. The prose still sits in the voice-guide's anti-pitch
register. The new headline reads as the largest claim and is true and defended.

## Edits

None. Both required items are resolved and no new issue surfaced, so no
surgical cut and no re-stamp were needed. (Writer's stamp: words 1292, reading 6
min, sources 10.)

## Required work

None.

## Decision

approve — both routed items are resolved, the new headline and recast headings
meet the standard, and every settled technical claim and round-01 cut is intact
with no new issue introduced.
