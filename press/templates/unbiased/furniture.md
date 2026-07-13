# The unbiased template's bespoke furniture

The two-sided layout this template renders, styled in `furniture.css` beside
this file on the `rs-` prefix. It is bespoke to the unbiased template — only
an unbiased article puts two cases side by side — so it lives in the
template's folder rather than in `press/furniture/`. The engine concatenates
it into `assets/theme.css` whenever this template is present.

## The split (`rs-divide` + `rs-side`)

Exactly two sides across an accent spine: left and right on wide screens,
stacked but still allegiant on phones. `skeleton.html` beside this file is the
markup — the single source of truth; fill it rather than rebuilding it from
memory. Each side is four slots, in order: **camp** (`rs-side-camp`, who
holds it), **thesis** (`rs-side-thesis`, the position in one sentence), the
**argument** (`rs-side-argument`, a wrapper holding the cited prose in the
form its best advocate would recognize), and the **champion**
(`rs-side-champion`, the vetted holder and in one clause why it has standing
on this question, cited). One accent, mirrored across both sides, never a
color per team.
