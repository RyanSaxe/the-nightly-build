# Revise a published article

Read `docs/guides/revise-an-article.md` and the current article on
`origin/library`. Establish the requested outcome, then select the smallest
honest tier:

- **Mechanical:** meaning and evidence remain unchanged; run a fresh editor.
- **Substantive:** meaning, framing, or prose changes; run writer and editor,
  plus researcher whenever evidence, claims, figures, numbers, or sources
  change.
- **Full rework:** reconceive the piece; run all four roles.

If the request sounds mechanical but changes what a sentence claims, raise the
tier. Explain the consequence rather than treating the tier as a form choice.

## Prepare exact current state

Use `nb start-article` to create a fresh ignored workspace with current press,
template, and furniture context. Replace its skeleton with the exact published
HTML and replace its asset directory with the exact published asset directory.
The generated root artifacts in the workspace are context only and are not
part of the revision diff.

Determine the next invocation number for each selected role from the published
artifact tree. Start at `01` only when that role has no published artifacts.
Give each role an exact brief focused on the approved revision; never edit or
append to historical artifacts.

Run the selected roles and the full current proof. Preview the result in the
browser and compare it with both the published page and the user's request.
Keep the article's `series`, `slug`, `date`, `mode`, and `order` unchanged.

Deliver with `nb prepare-pr ... --revision`. Confirm that the PR contains one
modified article, only matching asset changes, and only new role artifacts.
Revisions never auto-merge. Present the changed meaning, evidence, and visual
result so the user can decide whether to merge.
