# Create your paper

A paper is the published result. Its press is the configuration under `press/`
that produces it. A fresh press has three series. Dispatches publishes what you
ask for, and News Brief and Feature make a morning paper once you schedule a
run. Until you say otherwise, both are about technology.

## Make it yours

Ask your AI to make the paper yours, or to change what it covers. It asks two
questions, one at a time: what news you want, and what you want to read about.
Your answers rewrite the paragraph that opens each series prompt, the one that
says what the series covers, and the sentence in `editorial.md` that says who
reads the paper when your answers say something about you. Nothing else changes.
The press is validated, committed, and pushed to `main`, and the next scheduled
run reads it from there.

Asking for an article never triggers the questions. The article goes ahead, and
the paper's shape waits until you ask for it.

## A paper of your own design

This is for when you want more: series with beats of their own, a voice, a
reading rhythm. You do not need answers prepared. Start the conversation and
expect the assistant to propose directions, test them with representative
article ideas and counterexamples, and simulate a first week before asking for
approval. Every decision the press encodes gets settled this way. At a minimum:

- what the paper is for and who reads it
- the territory each series owns, and what it refuses to cover
- what counts as evidence and which sources qualify
- how the paper should sound, tested against real examples
- the reading rhythm: how often, how long, how visual
- how the runtime is billed and how much production usage you can sustain

The output becomes a small configuration tree:

```text
press/
├── site.yaml
├── editorial.md
├── production.yaml
└── series/<id>/
    ├── series.yaml
    └── prompt.md
```

Use [Series reference](../reference/series.md) for the exact configuration
contract. Use
[appearance and voice](../guides/customize/appearance-and-voice.md) when the
editorial concept needs a distinct visual system.

Once the proposed press validates, commit it and push to `main`. Both the
publishing check and the scheduled run read the press from the remote `main`
branch, so a press that exists only in a working tree publishes nothing. Then,
when you want articles without asking, continue to
[Schedule publication](../guides/operate/schedule.md).
