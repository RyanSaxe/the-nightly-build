# Set up

## What you need

- A GitHub account.
- Access to an AI model or agent capable of doing the editorial work.
- A public fork for free GitHub Pages, or a GitHub plan that supports Pages for
  a private repository.
- Only for a morning paper: a scheduled runtime that can check out the
  repository, browse research sources, push a work branch, and open a pull
  request. An article you ask for needs none.

The AI you talk to during setup and the runtime that works overnight can be
different products. Treat their capabilities separately.

## Recommended setup

Start with [Ask your AI](ask-your-ai.md). A capable assistant should:

1. Establish access to your GitHub account and create a fork with only `main`.
2. Clone the fork and run `./nb setup`.
3. Help you define the first version of `press/`.
4. Configure one scheduled runtime using
   [Schedule](../guides/operate/schedule.md).
5. Offer to [verify that runtime](first-run.md) with a non-publishing smoke
   test.

When the assistant cannot perform a step itself, expect one exact manual action
from it, and it continues from your result.

`nb setup` scaffolds `press/` with one on-demand series, creates the `library`
branch, and seeds its publishing workflows. It requires `git`, `uv`, and Python
3.10 or newer. With an authenticated `gh` it also enables Actions, configures
GitHub Pages, and protects `library`; without one it prints those as clicks to
make in the fork's settings, and the first two must be made before an article
can publish. Re-running `nb setup` is safe; it repairs what is missing.

Forks start with workflows disabled. If `nb setup` lists Actions as a click to
make, or warns that it could not enable them, enable workflows from the fork's
Actions tab: without them the `validate` check never runs and no article can
merge.

## Manual fork-and-clone fallback

Fork this repository with **Copy the main branch only** enabled, then:

```sh
git clone https://github.com/<you>/<your-paper>.git
cd <your-paper>
./nb setup
```

Enable Actions in the fork if GitHub asks. Then ask an AI in the checkout to
help create your paper and configure its schedule.

Local validation does not prove the scheduled environment. Run the optional
smoke test there to verify its tools, research access, GitHub permissions, and
CI trigger without publishing an article.
