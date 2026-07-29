# The Nightly Build

This repository is The Nightly Build: scheduled AI agents research topics and publish
cited HTML articles to a GitHub Pages library, gated by CI.

- If you were invoked by a **schedule to produce an article**: read
  `PROTOCOL.md`, then load `skills/correspondent/SKILL.md`. The protocol governs
  the shift; the skill defines the correspondent's judgment within it.
- If a **human is asking for setup, series configuration, or curation help**: load
  `skills/librarian/SKILL.md`.
- Never push to the `library` branch directly. Never edit files under `library/` in
  place. All content lands via Article PRs validated by `nb check`.
- Before any PR, run the proof through the checkout-owned `nb` command.
