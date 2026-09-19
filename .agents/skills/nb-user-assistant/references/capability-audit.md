# Capability audit

Audit the conversational assistant and scheduled runtime separately. Record each
requirement as `passed`, `failed`, or `not verified`. Never infer that one
environment has another environment's tools, identity, network, or approvals.

## Current assistant

Identify the intended GitHub account, fork, and checkout without exposing
credentials. Then find out which of three situations this is, because setup and
delivery differ:

- `gh` signed in with admin rights on the fork: everything runs from here.
- A sandbox or checkout with push credentials but no `gh`: `nb setup` does the
  git side and prints the fork settings for the owner, and `nb prepare-pr`
  prints `NB_ARTICLE_PR_REQUIRED` for the connected GitHub tool to open the PR.
  Check research egress before production by opening one real source page.
- A chat with no sandbox: it cannot run `nb` and cannot produce an article. Say
  so and point the owner at `docs/integrations/README.md`.

Verify with reversible checks every action this assistant claims it can perform:
inspecting or creating the fork and clone; running `git`, the checkout-owned
`nb`, and GitHub operations; creating and validating `press/` changes. When a
permission boundary requires the user, give one precise action in the provider's
secure UI, say what result to expect, and wait for confirmation. Never request a
token in chat.

## Scheduled runtime

Inspect the actual schedule's repository, checkout ref, working directory,
GitHub identity, network policy, tool approvals, and the billing plan it runs
under. Configuration is useful evidence but does not prove that the runtime can
execute.

Offer an on-demand smoke test using
`.agents/prompts/verify-scheduled-runtime.md`. Configure the provider to run
that prompt in the same repository, identity, network, and approval mode as
normal scheduled publication. Trigger the provider's real on-demand entrypoint.
A local simulation or setup-chat run is not a substitute.

The smoke test installs or verifies `uv`, exercises the checkout-owned command,
opens real research pages, and proves branch-push, draft-PR, and CI-trigger
permissions against `main`. It closes the PR and deletes its temporary branch.
It never creates an article or touches `library`.

## Interpret the result

Give the user the smoke report and distinguish three things:

- capabilities proven by the exact scheduled runtime
- failures with one corrective action and rerun boundary
- publication behavior intentionally left for ordinary article production,
  including article proof, automatic merge, and Pages deployment

Verification is explicit and repeatable, not a requirement to manufacture a test
article. If the user declines the smoke test, preserve those capabilities as
`not verified` and continue according to their request.
