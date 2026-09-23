# Troubleshoot setup and scheduling

## Setup cannot create or configure the fork

Confirm the current assistant is connected to the intended GitHub account and
repository. Without `gh`, `nb setup` cannot change or read Pages and Actions. It
lists both under "Still to do" with their GitHub settings links, even if you
already enabled them. Make any missing changes in GitHub. Do not paste a token
into chat.

## The first article's check reports an unknown series

The check reads the press from remote `main`. If `press/` exists in the checkout
but was never pushed, because the push was refused or setup predates the push,
get that commit onto `main`, then close and reopen the pull request so the check
runs again.

## Article PR checks never register

If an Article PR sits with no `validate` check and never merges, the fork's
workflows are probably disabled: forks start that way, and GitHub runs no
Actions until they are enabled. Enable workflows from the fork's Actions tab (or
re-run `nb setup`, which enables them when it can), then close and reopen the
stalled PR so the check triggers.

## The schedule starts but produces no work

Run `nb duty` in the scheduled checkout and read its idle reasons. A series may
have no work because it is paused, does not run on the current UTC day, has
already published for that day, or uses `cadence: manual`. An empty due list is
expected when every series is idle.

## Research cannot reach sources

Test outbound access inside the scheduled environment. Changing access in the
setup chat or local machine does not change the schedule. Enable the provider's
network capability for that runtime, then rerun the failed test step.

## The run cannot push or open a PR

Verify the scheduled identity can push a generated branch and create a PR
against `library`. Confirm GitHub Actions are enabled for the fork and that the
identity's pull requests start the `validate` check. Provider-hosted tasks may
need separate repository app permissions.

## A local check works but the scheduled task fails

The local environment may have different repository access, tools, and network
permissions. Check the scheduled task's run details. If they do not identify the
problem, use the
[optional scheduled runtime check](../guides/operate/verify-scheduled-runtime.md)
in the same environment.
