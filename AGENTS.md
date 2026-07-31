# The Nightly Build

Route by intent:

- **Scheduled production or a request to produce an article:** read
  `PROTOCOL.md`, then load `.agents/skills/correspondent/SKILL.md`.
  `PROTOCOL.md` is self-sufficient if skill discovery is unavailable.
- **A paper owner asking for setup, configuration, manual publication,
  revision, design, curation, or maintenance:** load
  `.agents/skills/nb-user-assistant/SKILL.md`.
- **An engine, documentation, or test contribution:** work normally from the
  repository and its public documentation; do not load a production role.

Never push to `library` or edit its files in place. Article publication and
revision go through Article PRs. Before any Article PR, run the proof through
this checkout's `nb` command.
