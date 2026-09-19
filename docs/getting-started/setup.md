# Set up

## What you need

- A GitHub account, and a public fork for free GitHub Pages or a plan that
  supports Pages on a private repository.
- An AI tool that can work in your fork: a coding agent in a terminal with `gh`
  signed in, or a product connected to GitHub that runs commands in a sandbox
  and opens pull requests.
- Only for a morning paper: a scheduled runtime that can check out the
  repository, browse research sources, push a work branch, and open a pull
  request. An article you ask for needs none.

## Two ways in

### A terminal with gh

1. Fork with **Copy the main branch only**. A capable assistant does this for
   you.
2. Clone the fork and run `./nb setup`. It scaffolds `press/` with three series,
   Dispatches for the articles you ask for and News Brief and Feature for a
   morning paper, and pushes it to `main`, where the publishing check reads it.
   It creates the `library` branch, seeds the publishing workflows onto it,
   enables Actions, configures GitHub Pages, and protects `library` behind the
   `validate` check.
3. Ask for the first article. [Your first article](./first-article.md) says what
   happens next.

### No terminal

1. Fork in the browser with **Copy the main branch only**.
2. Make the two settings only an owner can: on the fork's Actions tab, enable
   workflows if GitHub asks; under Settings, Pages, set Source to GitHub
   Actions.
3. Name the fork in your message so the product's GitHub connector opens it, and
   ask for the first article. Its `nb setup` does the git side, then lists under
   "Still to do" what it cannot make itself, with the URL for each: the two
   settings above, and a recommended third, protecting `library` behind the
   `validate` check under Settings, Branches.

`nb setup` requires `git`, `uv`, and Python 3.10 or newer. Re-running it is
safe; it repairs what is missing and verifies what it can read back.

A fork may start with workflows disabled. If the Actions tab asks you to enable
them, or `nb setup` warns that it could not, enable them there: without
workflows the `validate` check never runs and no article can merge. Without
`gh`, setup cannot read settings back, so its "Still to do" list names the two
required settings whether or not you have made them; nothing is wrong if you
already did.

## Later

[Create your paper](./create-your-paper.md) gives the paper series of its own, a
voice, and a rhythm. [Schedule publication](../guides/operate/schedule.md) adds
the runtime that publishes while nobody is present, and
[Verify the scheduled runtime](../guides/operate/verify-scheduled-runtime.md)
proves that environment before it publishes anything.
