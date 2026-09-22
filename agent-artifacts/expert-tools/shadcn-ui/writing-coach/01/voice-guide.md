# Voice guide: expert-tools/shadcn-ui (01)

## Julia Evans, “git branches: intuition & reality”

Source: https://jvns.ca/blog/2023/11/23/branches-intuition-reality/

> “That seems pretty reasonable, but that’s not how git defines a branch.”

Checked: https://jvns.ca/blog/2023/11/23/branches-intuition-reality/, retrieved 2026-09-22

She states the reader's plausible model before correcting it. The sentence makes the correction precise without treating the earlier model as foolish. The UI article should do the same when it moves from a package-centered view of components to an ownership-centered one.

> “people usually have the intuition they do for very legitimate reasons!”

Checked: https://jvns.ca/blog/2023/11/23/branches-intuition-reality/, retrieved 2026-09-22

The exclamation mark is earned by the specific defense of a useful mental model, not by enthusiasm for the writer's own conclusion. Preserve the reader's reason for choosing a styled library before describing the cost that appears later.

## Mitchell Hashimoto, “My Approach to Building Large Technical Projects”

Source: https://mitchellh.com/writing/building-large-technical-projects

> “The goal is to always give yourself a good demo.”

Checked: https://mitchellh.com/writing/building-large-technical-projects, retrieved 2026-09-22

He gives a working rule and then makes it concrete with a terminal project. The article should treat the shadcn CLI command and the local component file as an observable change in the workflow, not as an installation recipe.

> “I’m always more motivated working on a problem I’m experiencing myself”

Checked: https://mitchellh.com/writing/building-large-technical-projects, retrieved 2026-09-22

The first-person qualification keeps a process claim from becoming a universal law. When the article recommends a stack, identify the product and team conditions that make the recommendation useful.

## Simon Willison, “Simon Willison on Technical Blogging”

Source: https://simonwillison.net/2026/Aug/6/simon-willison-on-technical-blogging/

> “lower your standards!”

Checked: https://simonwillison.net/2026/Aug/6/simon-willison-on-technical-blogging/, retrieved 2026-09-22

The short imperative has force because the surrounding passage names the cost of waiting for a perfect draft. Keep recommendations operational and let the evidence explain the limit.

> “The flaws you see in your writing are invisible to everyone else.”

Checked: https://simonwillison.net/2026/Aug/6/simon-willison-on-technical-blogging/, retrieved 2026-09-22

He distinguishes the author's private standard from the reader's actual experience. Use the same distinction for component tooling: a local API that feels inelegant may be easier to maintain than a polished abstraction whose internals nobody owns.

## How this piece should sound

Write for an experienced engineer who has already tried at least one component library and wants to know where future customization will live. Start with a concrete failure such as wrapping a component until its API and visual rules no longer match the product. Then define the ownership boundary before naming tools.

Use the calm, corrective structure in Evans's examples: state why a conventional choice is reasonable, then show the exact point where its model stops matching the work. Use Hashimoto's habit of tying a recommendation to a visible result. Treat the CLI, a copied component file, a headless primitive, and a Storybook state as things a team can inspect.

Keep the comparison conditional. Say which tool owns styles, behavior, source and updates, then say what work remains with the team. The article can prefer shadcn/ui as a starting point, but it must give a real reason to choose Base UI, Radix, React Aria, Zag, Catalyst, MUI, Mantine or Chakra instead. End with a stack and its maintenance boundary, not a slogan.
