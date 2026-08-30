# Voice guide

## How this piece should sound

Write for a technically literate reader who knows what an API call and a
model-generated transcript are, but who should not have to infer the security
boundary from shorthand. Teach one distinction at a time: what the model says,
what the harness displays, and what an independent system can attest happened.
Use concrete examples before abstractions. Let the argument move from the
incident's evidence to a small, legible design rule.

Keep the voice calm and exact. Do not dramatize the agents or treat a spoofed
record as proof of successful historical erasure. Mark reported facts,
estimates, and the article's synthesis separately. Prefer short paragraphs and
specific verbs. The ending should state the condition that would change the
position, not add a generic lesson.

Julia Evans is a useful model for reader-centered explanation. She writes:

> “Who cares about how other version control systems implement branching?”

The lesson here is to name the reader's actual question and answer that one,
not to show every adjacent fact. Her advice to “pick 1 specific person” also
supports a direct, concrete address without fake intimacy.

Lilian Weng is a useful model for building a technical concept in layers. She
defines the agent's parts before discussing architectures:

> “A complicated task usually involves many steps.”

And she warns that the “reliability of natural language interface” is a live
engineering problem. Use that same order: define the record, show how it can be
altered, then explain the control that follows.

Simon Willison is a useful model for compact, durable terminology. His agentic
engineering writing starts by naming the term and its scope:

> “I’m using Agentic Engineering to refer to building software using coding agents”

He also captures the exploratory but disciplined energy to aim for:

> “There is so much to learn and explore about this new discipline!”

Borrow the clarity, not the phrasing. Do not quote these exemplars in the
article. The article should feel like a careful column, not a stitched source
summary.

## Source and argument handling

- Put the first citation after the first material claim from a source, then keep
  later citations close to the claim they support.
- Explain METR's uncertainty in the same paragraph as its figures.
- Use OpenAI's account for the benchmark and monitoring claims, and Hugging
  Face's account for independent forensic reconstruction.
- Treat the authenticated collector and reconciliation design as the column's
  synthesis, supported by the audit-log standard, not as a quoted incident
  remedy.
- Give the countercase its strongest form: raw-capability evaluations need
  minimal interference, and chain-of-thought can carry signal that actions do
  not. Answer with a narrower requirement: independently recorded effects,
  without making raw reasoning the trusted audit log.
