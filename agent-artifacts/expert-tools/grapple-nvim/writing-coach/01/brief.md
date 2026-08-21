# Writing-coach brief: expert-tools/grapple-nvim

## What this piece has to do that the last five didn't

The last five expert-tools pieces (jujutsu, outlines, atuin, grug-far,
oil.nvim) all converge on the same shape by the end: mechanism, then a worked
example, then a comparison table, then a two-column holds-up/careful box,
then a "Verdict" note. Four of five use `nb-table`. Three of five close on
`nb-note nb-note-strong` labeled Verdict. That's not a template requirement,
it's a habit, and this piece has to visibly not have it.

Concretely, for grapple.nvim:

- No comparison table. The grapple/harpoon/marks/`:b` contrast is a real
  distinction in addressing scheme (name vs. position), not a spec sheet of
  parallel features. It reads as prose, in the section that makes the
  point, not as a grid the reader scans instead of reading.
- No holds-up grid, no "Verdict" note. The maintenance material is strong
  enough to carry its own section and its own earned closing paragraph
  without needing a labeled box to tell the reader how to weigh it.
- A stat strip stands in for the recap-with-a-grade move: two dated
  figures (months since last commit, months since last merge) that let the
  final section make its point in numbers instead of adjectives.
- Vary heading construction: a comma-and clause, a stated fact, a colon
  lead, one plain declarative, one semicolon contrast. No two headings
  built the same way, and none of them open with What/Whether/Where.
- Avoid the "the project's own docs say so plainly" tic entirely. The
  maintenance claims here aren't drawn from Grapple's own framing of
  itself. They're drawn from commit and PR timestamps and an open issue,
  so there's no self-report to hedge about.

## Register

Press baseline: Mitchell Hashimoto's calm, precise, first-principles
register. For this piece that means naming the actual code path (a
resolver function, a names_index hash, a JSON file keyed by scope id)
rather than describing Grapple's behavior in marketing language borrowed
from its own README. Where the README asserts a design goal ("frictionless
first-time configuration"), the piece either shows the code that produces
that result or leaves the claim out.

## Standing risk to watch

The maintenance section is the one place this piece could tip into
unsupported opinion. Every claim there is pinned to a specific commit hash,
PR number, or issue number with a date, precisely so the closing paragraph's
synthesis ("adopting the repository roughly as it stood in 2024") is earned
from evidence already on the page, not asserted ahead of it.
