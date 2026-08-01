# Verify the scheduled runtime

Run the verification in the exact environment that will execute the schedule,
not in the setup chat or a different local shell.

The smoke run must:

1. Check out current `main` and `library` state.
2. Install or verify `uv` and run the checkout-owned `nb` command.
3. Reach real web sources from the scheduled runtime.
4. Push a temporary branch and open a draft diagnostic PR against `main`.
5. Confirm CI starts, then close the PR and delete the temporary branch.

The smoke run never creates an article, targets `library`, loads the production
orchestrator, or publishes the paper. If a capability fails, fix only that
boundary and resume from it; do not silently substitute the setup environment.

The first real article is ordinary product usage. When its CI passes, it merges
and publishes automatically.
