# Revise a published article

Read `docs/guides/publish/revise-an-article.md`, the article and matching assets
on `origin/library`, and only the press or source context relevant to the
request.

## Establish the outcome

Understand what the user believes is wrong and what a successful correction
would make true. Inspect before proposing a method. Distinguish a literal fix
from a change to meaning, evidence, voice, structure, or visual communication,
and surface any consequence the user may not have intended.

Choose the smallest process that can produce a trustworthy result. Do not
assign a tier or require a questionnaire. A direct local edit can be right for
a typo; a researcher, writer, editor, writing coach, web search, or complete
redraft can be right for deeper work. No role is mandatory, and using a role
does not make its artifact part of the revision PR.

## Make and verify the change

Work from exact published HTML and exact published assets in a local workspace
or checkout. `nb start-article` is optional. Preserve unrelated content and
state the intended change precisely before delegating any part of it.

When another role or model would help, give it a purpose-built brief containing:

- the defect or requested outcome, with the exact relevant passage or asset;
- the current article, sources, and press constraints it actually needs;
- what may change and what must remain stable;
- factual, editorial, visual, and accessibility acceptance criteria; and
- the exact output to return for integration.

Reopen and verify evidence when claims, citations, numbers, or interpretations
change. For a figure, inspect its source data, labels, caption, alternative
text, article references, and narrow/wide rendering; regenerate or replace the
matching asset rather than preserving a misleading visual.

Run the full current proof. Preview every visual or structural change and
compare it with the published page and the user's requested outcome.

## Record and deliver

Add exactly the next
`agent-artifacts/<series>/<slug>/revisions/NN.md`. Write a concise durable
account of why the revision was needed, what materially changed, and any
verification a later reviewer would need. Do not impose a template on the
prose, modify prior notes, or rewrite historical role artifacts.

Deliver with `nb prepare-pr ... --revision`. Confirm that the PR modifies one
published article, changes only its matching assets, and adds only its one new
revision note. The article can change anything the normal proof permits, but
its path, series, and slug remain aligned. Revisions never auto-merge.

Present the changed meaning, evidence, and visual result—not an invented
workflow ceremony—so the user can decide whether to merge.
