# Agent and scheduler integrations

The Nightly Build does not depend on one model provider or agent product. It
depends on capabilities in the actual unattended environment: a repository
checkout, access to `main` and `library`, live web research, non-interactive
tool use, and permission to push a branch and open a pull request. See
[Schedule](../guides/operate/schedule.md) for the complete contract.

An automation product's existence does not prove that it meets that contract.
Provider behavior, permissions, and billing change independently, so this
project does not yet claim end-to-end support for a provider-specific setup.
Use the [scheduled-runtime smoke test](../getting-started/first-run.md) in the
same environment that will publish the paper.

## Provider entrypoints to evaluate

These first-party pages are starting points for configuring and testing a
runtime. They are not Nightly Build setup recipes or support certifications.

| Provider or agent | First-party starting point                                                                     | Nightly Build status    |
| ----------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| Claude Code       | [Routines](https://code.claude.com/docs/en/routines)                                           | Not verified end to end |
| Codex             | [Automations](https://openai.com/academy/codex-automations/)                                   | Not verified end to end |
| Jules             | [Scheduled Tasks](https://jules.google/docs/scheduled-tasks/)                                  | Not verified end to end |
| Cursor            | [Automations](https://cursor.com/automate)                                                     | Not verified end to end |
| Devin             | [Scheduled sessions](https://docs.devin.ai/product-guides/scheduled-sessions)                  | Not verified end to end |
| GitHub Copilot    | [Automations](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations) | Not verified end to end |
| OpenCode          | [GitHub integration](https://dev.opencode.ai/docs/github/)                                     | Not verified end to end |

Before documenting a provider-specific path, verify repository authentication,
both required branches, research access, tool approvals, `uv` availability or
installation, on-demand and scheduled invocation, the non-publishing smoke
test, and one real publication. State whether the path uses subscription
allowance or metered API billing and record when it was last verified.

## Harness independence

The orchestrator does not require a provider-specific team feature. A harness
may isolate bounded editorial roles in child contexts or execute the same
recorded sequence in one context. See [Architecture](../concepts/architecture.md).

Model names are harness-specific. Portable tiers and exact provider overrides
are defined in [Production reference](../reference/production.md).
