# Create your paper

A paper is the published result. Its press is the configuration under `press/`
that produces it.

Do not begin by filling fields. Begin with an editorial conversation that
establishes:

- the change the paper should make in the reader;
- the reader's existing knowledge, appetite, and constraints;
- the territory each recurring series owns and deliberately excludes;
- the evidence standard and source mix;
- a voice described through concrete examples and anti-examples;
- the pace, length, and visual language that fit the reading habit;
- what would make the first week feel coherent rather than repetitive.

A strong assistant will form hypotheses, test them with representative article
ideas and counterexamples, synthesize a proposed paper, and simulate a first
week before asking for approval. The output becomes a small configuration tree:

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
contract. Use [appearance and voice](../guides/customize/appearance-and-voice.md)
when the editorial concept needs a distinct visual system.

Once the proposed press validates, commit it and push to `main`. The scheduled
run reads the press from the remote `main` branch, so a press that exists only
in a working tree publishes nothing. Then continue to
[scheduled-runtime verification](first-run.md) if you want to test the
automation before relying on it.
