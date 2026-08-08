# Set up a paper

Use `docs/getting-started/setup.md`, `docs/guides/operate/schedule.md`, and the
[capability audit](../references/capability-audit.md) as the current setup
contract. Inspect the repository before creating or replacing anything.

## Establish the boundaries

Distinguish the conversational assistant, scheduled runtime, and GitHub. The
same provider may use different identities, tools, network rules, and approval
modes in chat and on schedule. Verify only what the active environment can
demonstrate.

Preserve a valid fork, checkout, press, branch, or schedule. Resume from the
first incomplete requirement instead of restarting setup.

Offer the `main` protection choice once, plainly: unprotected keeps the
owner's quick direct edits; protected routes every change through a reviewed
PR and keeps the scheduled identity out of trusted configuration entirely.
The tradeoff lives in `docs/concepts/publishing-and-security.md`. Either
answer is valid. Record which the user chose.

## Connector-only ChatGPT route

When the user wants ChatGPT Scheduled Tasks to operate through the connected
GitHub app without a checkout or shell, follow
`docs/integrations/chatgpt.md`. Do not send that runtime through the ordinary
`nb sync` and `nb duty` path or claim it ran local commands.

The owner must complete three external prerequisites that the assistant cannot
safely infer:

1. Fork this repository into the account where the paper will live.
2. Enable GitHub Actions for pull-request workflows in that fork and approve the
   first run when GitHub presents an approval gate.
3. Install or enable ChatGPT's GitHub connector for that fork with permission to
   read repository and Actions state, create branches and commits, and open or
   update pull requests.

Verify each prerequisite through the connected surface before relying on it.
Read access is not proof of write access. Use a disposable draft PR to prove the
branch, commit, PR, Actions-read, and cleanup surfaces.

Keep `WEB_TASK.md` on `main`. It is the connector-only execution contract. The
Scheduled Task performs all subject selection, research, source verification,
drafting, bounded repair, and pipeline observation. GitHub Actions only
validate, gate merge, and publish. Remove any GitHub Models,
`actions/ai-inference`, or repository generation cron from this route.

If the fork has not yet been bootstrapped with `library`, branch protection,
validation, auto-merge, and Pages, perform the setup through an authorized
checkout or ask the owner for that one manual action. A connector-only runtime
must not pretend that repository reads prove those controls exist.

## Minimize handoffs

Perform every safe action already authorized. Ask the user only for a sign-in,
provider authorization, billing-bearing choice, or setting that automation
cannot change. Give one manual action at a time, state its expected result, and
verify it before continuing. Never ask for a pasted token.

Run `nb setup` to create or repair the publishing boundary when the active
runtime has a checkout and shell. It is idempotent and safe to re-run over a
healthy setup. Hand editorial definition to [create paper](create-paper.md),
then configure the scheduled runtime with the repository's publication prompt.

## Offer scheduled verification

Offer a one-off smoke run in the exact scheduled environment. Use the
capability audit and `.agents/prompts/verify-scheduled-runtime.md` for
checkout-based runtimes. For connector-only ChatGPT, use the smoke test in
`docs/integrations/chatgpt.md`. Do not turn the smoke into an article, cadence
change, or production run. Present its evidence and repair the narrow failed
boundary when the user wants help.

The user may proceed with unverified capabilities. State them plainly rather
than manufacturing confidence or withholding unrelated setup work.
