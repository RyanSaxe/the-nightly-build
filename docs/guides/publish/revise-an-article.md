# Revise a published article

A revision changes one published article without erasing how it reached the
paper. It can be a spelling correction, a factual update, a substantial
rewrite, or a replacement for a bad figure. The process should fit the work;
the PR contract does not prescribe roles, prompts, or an editorial workflow.

Revisions always open a human-reviewed PR and never auto-merge.

## Decide what the revision needs

Start from the article and assets currently on `origin/library`. Establish the
requested outcome and inspect only the context needed to make it safely:

- correct spelling or markup directly when no judgment is required;
- reopen sources when a claim, citation, number, or interpretation changes;
- use a writer, editor, researcher, or writing coach when their judgment would
  materially improve the result; and
- regenerate, replace, add, or remove matching assets when the visual evidence
  or presentation is wrong.

Those are editorial choices, not CI requirements. A large LLM-assisted rewrite
and a one-character correction produce the same narrow kind of PR.

You may work in an ignored workspace, a detached worktree, or a local library
checkout. `nb start-article` is optional. Do not commit or push changes directly
to `library`; `nb prepare-pr` creates the generated revision branch from the
current remote branch.

## Record the reason

Add exactly one new Markdown file:

```text
agent-artifacts/SERIES/SLUG/revisions/NN.md
```

Use the next two-digit number: an article with no revision notes starts at
`01.md`, then `02.md`, and so on. This sequence is independent of any role
invocation numbers in the original production record.

There is no required heading or schema. Write for a future reader who needs to
understand the article's history. Explain why the revision was needed and what
materially changed; include the verification performed when it helps establish
trust. Keep the note about the revision, not the mechanics of operating an AI.

Do not edit or delete an earlier revision note or any historical role artifact.
If you use article-making roles during the work, their scratch output can stay
local; it is not part of the revision PR.

## Prove and deliver the result

Run the current full article proof. Preview the page whenever markup, layout,
furniture, or assets changed, and compare the result with both the published
page and the requested outcome. Then run:

```sh
nb prepare-pr library/SERIES/SLUG.html \
  --library PATH-TO-LIBRARY-CHECKOUT \
  --revision
```

The generated PR must:

- modify exactly `library/SERIES/SLUG.html`;
- add, modify, or delete files only under the matching
  `library/SERIES/SLUG/` asset directory;
- add exactly the next `agent-artifacts/SERIES/SLUG/revisions/NN.md`; and
- leave every other article and historical artifact untouched.

The article may change any prose, structure, title, metadata, citation, or
template choice that the normal current proof accepts. Its path remains fixed:
the `series` and `slug` metadata must still agree with
`library/SERIES/SLUG.html`. Moving or renaming an article is not an in-place
revision.

CI reruns the normal proof and browser-render check. It permits corrections to
paused and already-published series, but the series must still exist and the
result must satisfy its current configuration and template contract.
