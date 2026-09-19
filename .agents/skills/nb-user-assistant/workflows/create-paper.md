# Create a paper

Read [prompt authoring](../craft/prompt-authoring.md). Read
[interview craft](../craft/interview.md) only for a paper of the owner's own
design, below. Load [furniture design](../craft/furniture-design.md) or
[template design](../craft/template-design.md) only when the concept calls for
custom presentation or an enforceable new structure.

## Make the default paper theirs

A fresh press already has a paper: News Brief and Feature run daily once
scheduled, and Dispatches takes requests. The first paragraph of each series
prompt is its territory, and the scaffold's territory is technology. Making the
paper theirs is two questions and three paragraphs. It happens when the owner
asks to build or change their paper, never when they ask for an article.

Ask what news they want and what they want to read about, one at a time, each
from a hypothesis: the subject of the article they asked for, the fork's name,
and anything they have said are enough to propose an answer they can correct. An
answer the owner gave before being asked counts as given; write the paragraph
from it and show it instead of asking the question again. The first answer
rewrites the territory paragraph of `press/series/news-brief/prompt.md`. The
second rewrites the territory paragraph of `press/series/feature/prompt.md`.
When the answers say who the owner is, rewrite the reader sentence that opens
`press/editorial.md` to match; otherwise leave it. Write each paragraph under
`spec/prompting.md`: a territory is the principle that admits and excludes work,
and a short list of subjects reads as the complete set unless the owner means it
that way.

Show the rewritten paragraphs, then run `nb validate`, commit the press, and
push to `main`; the publishing check and the scheduled run both read the press
from remote `main`. When `main` is protected, open a pull request against it and
tell the owner it waits for their merge. Then offer [schedule](./schedule.md)
for the mornings. The rest of this workflow is for an owner who wants series of
their own, a voice, and a reading rhythm.

## Discover before configuring

Inspect `examples/`, the current `press/` if one exists, and the public docs.
Conduct a contextual interview, not a field-by-field questionnaire, and reach
the outcomes the interview craft requires.

Ask from hypotheses. If the user wants a daily paper on AI, propose two or three
meaningfully different editorial shapes and test them with candidate headlines.
Use their reactions to learn the underlying standard.

## Synthesize and pressure-test

Present a compact press proposal in the user's language. For each series, give
its job, boundary, representative article, counterexample, mode, cadence, and
template choice. Simulate a first week. Look for topic collisions, articles that
would repeat one structure, impossible evidence requirements, and a reading load
the user will not sustain.

Propose a production policy alongside the lineup instead of letting the default
stand unexamined. Say which roles earn an expensive model in each section and
why, and which sections should pin a voice guide rather than run the writing
coach every night. The reasoning is per section: research dominates wherever
claims are contested and change quickly, drafting dominates wherever the piece
is carried by its argument or its voice, and a section can be settled enough in
one of those and not the others. Show the user what a section costs in role work
before they approve a cadence that multiplies it.

Do not turn approval into a vague "looks good?" Ask the user to decide the few
open choices that materially change the paper. Revise the concept until its
parts cohere.

## Implement the approved press

Write the smallest `press/` that expresses the approved concept. Keep schema in
YAML and editorial judgment in prose. When an editorial standard has an engine
gate (e.g., source policy fields, bands, strict, banned terms, etc.), prefer the
gate over prompt prose, and confirm with the user which standards are enforced
and which stay advisory. Apply `spec/prompting.md` to `editorial.md`, every
`prompt.md`, item prompt, template identity, and custom catalog entry. Do not
duplicate cadence, source bands, template sections, or other config inside
prompts.

Ask how each series should sound, not only what it covers. Record register
intent where production can act on it: `editorial.md` for the whole paper, or a
register line in the series prompt for one section. `spec/editorial.md` states
how far a press may move the house register. When two series share a border,
write the settled boundary into both prompts so the next scheduled run inherits
the resolution instead of the ambiguity.

Run `nb validate`, build a preview where presentation changed, and show the user
the material consequences. Commit the press configuration separately from any
Article PR. Then, when the owner wants articles to arrive without asking,
continue to [schedule](./schedule.md).
