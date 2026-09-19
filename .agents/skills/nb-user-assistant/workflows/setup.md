# Set up a paper

Read `docs/getting-started/setup.md` and the
[capability audit](../references/capability-audit.md). Inspect the repository
before creating or replacing anything, and resume from the first incomplete
requirement instead of restarting setup.

## Which way in

Run the audit's current-assistant half first, because its answer picks the path.
A chat with no sandbox has no way in: it cannot run `nb`, so say so and point
the owner at `docs/integrations/README.md`.

With `gh` signed in and admin rights on the fork, do everything from here: fork
with only `main`, clone, and run `nb setup`, which makes the fork settings
itself and prints "The presses are ready". Nothing needs the owner's hands.

Without `gh`, in a sandbox with push credentials or a checkout where `gh` is not
signed in, run `nb setup` anyway. It scaffolds the press and pushes it to
`main`, creates and seeds `library`, and prints under "Still to do" the fork
settings only an admin can make: Pages with Source "GitHub Actions", and
workflows enabled on the Actions tab. Give the owner those two as one action
each, with the URL setup printed for it, and continue when they confirm. The
third item, protecting `library`, is recommended and can wait. Before
production, open one real source page from the sandbox, because research needs
the web and a sandbox may not have it.

`nb setup` is idempotent. Re-run it after the owner makes a setting and it
verifies what it can read back.

## Minimize handoffs

Perform every safe action already authorized. Ask the owner only for a sign-in,
a provider authorization, a billing-bearing choice, or a setting automation
cannot change. Give one manual action at a time, say what result to expect, and
verify it before continuing. Never ask for a pasted token.

## Then the first article

Setup ends when `nb setup` prints "The presses are ready", or when the owner has
made the two required settings. Hand to [publish now](./publish-now.md) for the
article the owner came for; the scaffolded Dispatches series takes it without
any change to `press/`. Offer [create paper](./create-paper.md) to make the
paper theirs, two questions that rewrite what the default series cover, and
[schedule](./schedule.md) when they want articles to arrive without asking.
