# Architecture

![The Nightly Build production flow](../../assets/architecture.svg)

The diagram shows the normal scheduled path from an editorial specification to
a published paper. The important boundary is the Article PR: agents may choose
and produce work, but only the deterministic engine and CI decide whether that
work is safe to publish.

## Setup creates the publication boundary

`nb setup` prepares a fork for both configuration and publication. It
scaffolds `press/`, creates the orphan `library` branch, seeds that branch with
the validation and publication workflows, enables GitHub Actions and Pages,
and protects `library` with the required validation check. The setup command
performs these jobs before an unattended agent receives permission to publish.

The resulting repository has two long-lived branches. `main` holds trusted
engine code and the owner's press. `library` holds published articles, local
article assets, production records, and the protected workflow triggers. A
generated site is a Pages artifact. It is never committed to either branch.

## The press defines intent

The paper owner describes the publication under `press/` on `main`:

- `site.yaml` defines paper-wide identity, appearance, and delivery
- `editorial.md` defines the shared editorial direction
- each `series/` entry defines a recurring section, its cadence, article mode,
  source policy, prompt, and publication policy
- production policy selects the model profile and reasoning effort available
  to each article-making role

This is desired publication behavior, not publication state. Scheduled work
always starts from the current `main` branch. Published articles, assets, and
production records live on `library`.

## A scheduled run resolves exact work

The external scheduler carries a small prompt that names the repository-owned
scheduled-publication entrypoint. The scheduled agent updates the `main`
checkout before reading the press or prompts. It then runs `nb sync` so the
protected workflow files on `library` match their trusted copies on `main`.
When synchronization needs a PR, the run completes that narrow PR and repeats
the command before producing articles.

The agent refreshes a separate checkout of `library` and passes it to
`nb duty`. Duty compares every configured series with published state. It
applies pauses and UTC cadence, advances collection and sequence queues,
detects completed series, and prevents a series from publishing twice on the
same UTC date. A `manual` series never becomes due on its own.

Duty returns the exact authorized work for the run and explains why every
other series is idle. It also refuses a stale checkout or a tree with no
press. These checks keep calendar math and rerun safety outside model
judgment. The orchestrator may choose a subject for an open series or select
among authorized candidates. It may not add another series or publish more
than one article for a returned series.

## Commissioning turns duty into article assignments

The scheduled agent follows the repository's scheduled-publication prompt,
resolves the work list, and then loads the orchestrator skill in the same
context. It does not launch an orchestrator subagent. The orchestrator turns
each authorized item into a precise commission. A manual article enters at
the same boundary after the user assistant configures it.

The orchestrator plans the complete edition before launching an editorial
role. It checks targeted publication history, chooses distinct subjects and
article shapes, resolves source and production policy, and prevents two
articles in the same run from making the same contribution. This shared pass
keeps the edition coherent without putting one article's working context into
another article.

`nb start-article` then creates one workspace per article. It copies the
selected template skeleton and assembles the exact editorial direction from
the current checkout revision. That direction layers the house standard,
headline standard, press direction, template identity, series prompt, tag
fragments, and configured item when each applies. Generated template
contracts, runtime assets, and furniture catalogs give later roles the
remaining deterministic context without an orchestrator paraphrase.

When the runtime supports isolated child agents, separate articles can proceed
in parallel. A runtime without that capability can execute the same commissions
sequentially. Isolation prevents one article's sources, drafts, or instructions
from leaking into another article's context. It does not change the published
result or the CI contract.

## One article run has four editorial roles

The large box in the diagram expands one isolated article run. Every article's
writing coach and researcher begin together. The writer begins after both
outputs exist, and the editor begins after the writer proves the draft. The
orchestrator prepares the exact input for each role, and each role records its
exact output:

1. The **writing coach** studies strong writing relevant to the commission and
   produces a practical voice guide.
2. The **researcher** finds and reads sources, verifies usable claims, and
   produces the evidence record.
3. The **writer** drafts from the commission, voice guide, evidence, and chosen
   template. The writer also runs the deterministic article proof and fixes
   failures.
4. The **editor** reads as skeptic, line editor, and reader. It can request
   prose changes, more evidence, or better source support before approval.

The arrows returning to earlier roles are deliberate. A question about voice
returns to the writing coach, an unsupported claim returns to research, and an
editorial revision returns to the writer. The orchestrator carries those
requests with exact context instead of asking one general-purpose agent to keep
the whole production process in memory.

Each later invocation gets the next numbered artifact directory. No repair
overwrites the brief or output that came before it. The role artifacts preserve
the commission, evidence, voice guidance, draft handoff, editorial review, and
repair history that produced the submitted article. They are evidence of the
run, not executable content.

## The CLI supplies deterministic operations

Agents use the repository-owned `nb` command for operations that should not
depend on model judgment. The right side of the diagram calls out four common
ones:

- searching published history for narrowly requested prior coverage
- checking article structure, metadata, sources, prose, and PR shape
- rendering charts and capturing permitted article assets
- previewing the article with its real template and site styles

The same proof code runs locally and in CI. Local success is therefore useful
evidence before delivery, but it never replaces the server-side gate.

## Preparing an Article PR fixes the delivery shape

After editorial approval, `nb prepare-pr` starts from the current remote
`library` branch. It copies the article bundle into a generated branch, commits
one narrow change, and runs proof against that exact commit. It then pushes the
branch and opens the Article PR or gives the connected GitHub tool an exact PR
request. A normal new article PR contains one HTML article, its local assets,
and its complete role record.

Generated branches and `.nb-work/` are disposable working state. The PR
commit is the proposed publication. Merging that commit is the only way an
article becomes part of the paper.

## CI is the trust boundary

Article HTML and assets are untrusted input. The Article PR workflow uses the
trusted engine and press configuration from `main`, read-only repository
permissions, and no scheduler secrets. It verifies the narrow diff shape,
article metadata, source and prose contracts, artifact history, rendered site,
and article behavior in a browser.

If CI fails, the failure returns to the orchestrator for a targeted repair and
another proof. If it passes, GitHub automatically merges every new article, as
it does an exact workflow-synchronization PR. The orchestrator delivers each
finished article immediately and monitors its PR while other articles continue.
Revisions and owner curation always require human review.

See [Publishing and security](publishing-and-security.md) for the complete
permission and threat model.

## Publication is a static build

Merging the Article PR changes `library`. The protected publication workflow
checks out the published content from that branch and the trusted engine,
templates, and press from `main`. It then rebuilds article pages, local assets,
indexes, search data, feeds, and `catalog.json`. GitHub Pages serves the result
without an application server or publication database.

The public directory can discover papers through their published catalog, but
the fork remains the source of truth for its press and archive. See
[Ownership and branches](ownership-and-branches.md) for the exact division of
state.

## Manual articles and revisions use the same gate

A manually commissioned article skips only the cadence decision. Once its
series configuration admits it, the orchestrator and Article PR path are the
same as for scheduled work.

A revision may be as small as a typo correction or as large as a new
LLM-assisted treatment of the article and its figures. The owner chooses the
process. The submitted PR changes one article's HTML and/or matching local
assets, records why the revision was needed, and passes the normal proof and
browser checks before a person can merge it.
