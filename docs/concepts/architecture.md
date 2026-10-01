# Architecture

![The Nightly Build production flow](../../assets/architecture.svg)

The diagram begins after the engine has decided what work is due and ends when
GitHub Pages serves the result. It shows the central split in the system: agents
make editorial judgments, while repository-owned code controls the publication
boundary.

## Before the diagram

The owner defines the press on `main`. Published articles live on `library`. An
article the owner requests enters production as a commission. The assistant
records that article as the authorized work. At the start of a scheduled run,
`nb duty` compares those two states and returns the authorized work. The
orchestrator may make editorial choices within that result, but it cannot add
work to it.

The duty calculation handles cadence and reruns without relying on model
judgment. [Schedule publication](../guides/operate/schedule.md) documents the
runtime, and [Ownership and branches](ownership-and-branches.md) explains the
state split.

## The orchestrator coordinates, and roles decide

The orchestrator plans the edition together, then creates one isolated workspace
per article. Isolation keeps sources, instructions, and drafts from leaking
between articles and lets independent work proceed in parallel. It is an
execution detail, not a different publication path: a runtime without child
agents preserves the same role sequence and records.

The orchestrator selects commissions only from the authorized work. The engine
assembles each commission's governing context from the current repository
revision. Each role reads the named files directly, so it does not depend on an
orchestrator's summary.

Within an article, each role handles one kind of judgment. A role that needs an
answer sends a question to the orchestrator. The orchestrator answers from the
commission, makes a decision, or starts a subagent and returns its result. The
role can continue its work while it waits. If the editor decides the article
needs a different argument, the writer drafts it again.

The writing coach is the one role a run may skip. A series that pins a standing
voice guide has already made the judgment the coach exists to make, so the
engine supplies that guide and production starts at research. Skipping it is a
cost decision the press owner makes, never a waived gate: the article carries
the same coach record either way, and the writer and editor read it as they read
any other.

Every invocation saves its exact input and output. Later repairs append to that
record rather than replacing it, so the submitted article carries the history
that produced it.

## The engine makes judgment enforceable

The CLI handles repeatable operations: assembling context, validating work,
creating permitted assets, previewing the page, and preparing the required
pull-request changes. Agents make editorial decisions. The engine checks whether
each result satisfies the press and publication requirements.

Local checks shorten the repair loop. They do not grant publication authority.

## The Article PR is the boundary

After editor approval, `nb prepare-pr` turns one workspace into one proposed
publication commit. CI evaluates that untrusted article with the trusted engine
from `main` and without scheduler secrets. A failure returns to the owning role,
a valid new article merges and triggers a static Pages build.

Manual articles enter through the orchestrator and skip only the schedule
decision. Revisions use the same validation boundary but require human review.

[Publishing and security](publishing-and-security.md) defines the complete trust
model. [Ownership and branches](ownership-and-branches.md) explains where the
press, engine, production records, and generated site live.
