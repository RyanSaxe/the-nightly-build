# Voice guide: expert-tools/visidata

Register: the house baseline holds — calm, first-principles, patient exactly
where a concept needs building. What changes is the reader relationship.
Write to a practitioner who already has a working answer to this problem — a
pandas session, a notebook, a one-off script — and has to be *shown*, not
told, that interactive keystrokes beat it on a real piece of work.
Demonstrate before you assert: a claim about what VisiData changes earns its
place only after the keystrokes that prove it, never before.

The moves below change specific sentences in this article:

- When the article claims a keystroke sequence replaces a step of the
  write-run-tweak loop, stage that sequence at the exact sentence making the
  claim, not in a boxed listing the reader can skip past. The command is the
  evidence; put the evidence where it's needed, not in an appendix to it.
- When you state what adopting VisiData costs, name the actual friction —
  which key, which modal behavior, how many keystrokes before the tool pays
  for itself — instead of a soft phrase like "there's a learning curve." A
  vague cost reads like a disclaimer; a specific one reads like a report.
- When the article compares VisiData to the pandas/notebook alternative it
  displaces, give that alternative its own working method before naming
  where it loses. A comparison against a strawman is not earned analysis; a
  comparison against a real one is.
- When a keybinding, command, or piece of behavior appears in prose, verify
  it did what the text says it did against the current docs or source before
  it goes in a walkthrough — a demonstration form gets no more slack on
  accuracy than a citation does, and less benefit of the doubt, because the
  reader is meant to be able to try it.

## Licenses

```text
form: live keystroke/shell walkthrough
move: Gregg stages a real terminal exchange (command typed, exact error or
      output returned) as the argument itself, not as an illustration of an
      argument made in prose around it; Willison runs one real command
      against a real target and reports the measured result instead of
      describing the feature in the abstract.
bar:  the walkthrough must prove the one changing move the commission names
      and stop the moment it's proven — no setup steps, no full menu of the
      tool's commands, nothing a reader would need only to get the tool
      running rather than to see it work. Every keystroke shown must pair
      with what visibly changed (on screen or in the data), verified against
      current docs or source. A walkthrough that would still make sense as
      the opening of an install guide has crossed into tutorial and must be
      cut back to only the keystrokes that carry the proof.
```

```text
form: direct address (second person), scoped to the walkthrough
move: Evans and Gregg narrate the reader's own action in second person only
      while staging a demonstration ("you type X" / "press F and the sheet
      becomes...") — never as a rhetorical aside about the reader's
      attention or feelings.
bar:  confined to sentences inside the walkthrough that describe an action
      the reader could reproduce keystroke for keystroke. The moment the
      sentence stops narrating a reproducible action and starts commenting
      on the reader ("you'll notice," "you might wonder"), the license is
      spent and the piece returns to the default third-person register.
```

## Recently used, do not reuse

No Overview/Usage/Verdict scaffolding, or any equivalent generic tour —
break the shape of the most recent expert-tools slug rather than inherit it.
No closing reading list or pointer away (template rule, no exception here).
No section that could be lifted into another tool's writeup unchanged; each
flex section must be reasoning this article specifically needs, built from
the one changing move, not a slot the series fills by habit.

## Julia Evans, "sqlite-utils: a nice way to import data into SQLite for analysis"
Source: https://jvns.ca/blog/2022/05/12/sqlite-utils--a-nice-way-to-import-data-into-sqlite/
Craft:
- cadence: opens on a specific, already-felt problem (a real work task,
  analyzing a messy Shopify export) before the tool is even named, so the
  reader arrives at the demonstration already wanting the fix.
- argument: argues by replacement — names the exact heavier setup being
  displaced (a custom Flask site wired to Plotly and pandas) and lets that
  comparison, not a stated verdict, carry the case.
- evidence: every claimed feature (the `alter` flag, `upsert_all`, CSV
  import) appears attached to the concrete data shape that needed it, never
  as an abstract line in a feature list.
- stance: commits without qualification once the tool has earned it ("I was
  really delighted... it did everything I wanted") — the enthusiasm follows
  the demonstration; it doesn't open the piece.
- notice: catches the moment a tool anticipates a problem before the writer
  finishes stating it ("sqlite-utils thought of that") — noticing a design
  decision, not just cataloguing a feature.
- diction: plain, unpolished admissions of friction ("this seemed like a lot
  of boring work") sit next to precise CLI syntax; neither gets hedged.
- reader: a colleague being shown a shortcut, not a student — assumes the
  reader has hit the same wall and skips justifying that the wall exists.
- the move the axes miss: she narrates the tool solving her actual, current
  problem in real time rather than a constructed example, so the
  demonstration and the argument are the same paragraph.

## Simon Willison, "monolith"
Source: https://simonwillison.net/2025/Mar/6/monolith/
Craft:
- cadence: one command, one measured result, one stated limit — the whole
  post is shorter than a single section of a longer piece, so nothing pads
  the demonstration.
- argument: proves the tool by running it once against a real target (his
  own site) and reporting what actually came out, rather than describing
  its capabilities in the abstract.
- evidence: the size of the resulting file (roughly 1.5MB) stands in for a
  claim about how much got inlined — a measured number instead of a
  paraphrase of a feature.
- stance: states the limitation as flatly as the capability ("doesn't
  currently attempt to run any JavaScript") — the cost gets no softer verb
  than the praise did.
- notice: catches which dependency does which job in the pipeline (fetch,
  parse, rewrite) at a resolution most users of the tool would never look
  past.
- diction: unhedged present-tense verbs for what the tool does; the
  limitation is one plain sentence, not a paragraph of caveats around it.
- reader: assumed to be about to run the same command themselves — the post
  gives exactly enough to reproduce the result and stops there.
- the move the axes miss: "I ran it and this is what came out" functions as
  the entire argument, with no framing sentence asserting the result is
  good; the reader is left to see that for themselves.

## Brendan Gregg, "Linux Crisis Tools"
Source: https://www.brendangregg.com/blog/2024-03-24/linux-crisis-tools.html
Craft:
- cadence: a reference table of tools gives way to a narrated real-time
  scenario, so the piece shifts from cataloguing to demonstrating without
  announcing the shift with a transition sentence.
- argument: makes the case for pre-installation by staging the failure mode
  itself — a missing binary, a command not found, a blocked repository —
  rather than asserting that missing tools are risky.
- evidence: the imagined terminal exchange (the exact command typed, the
  exact error returned) does the work a citation would do elsewhere: it is
  the proof, not a decoration on the proof.
- stance: names the real counterargument ("Can't I just install them
  later?") and defeats it with the scenario instead of waving it off.
- notice: catches the layered obstacles a rushed install actually meets (no
  package manager, no repo access, an immutable filesystem) instead of the
  single obstacle a reader would guess on their own.
- diction: plain and procedural through the technical narration, with one
  blunt aside ("Ugh") marking exactly where the frustration is the point.
- reader: treated as a peer who has been on call during an outage, so the
  piece skips explaining why an outage is stressful and goes straight to
  what breaks.
- the move the axes miss: he states the cost of his own recommendation
  before a reader can raise it ("the main downside... is their on-disk
  size") and quantifies it, so the piece argues against itself before it
  argues for itself.

## Self-test

The house default already bans hedging, demands concrete numbers, and calls
for furniture wherever evidence has a shape. Left there, an expert-tools
piece about VisiData would still default to a features paragraph — VisiData
supports frequency tables, pivots, and computed columns — with a code block
parked afterward as illustration, because that is the shape every tool
writeup falls into absent a specific counter-pressure. What this guide adds:
the keystrokes are not illustration, they are the argument, placed at the
sentence that makes the claim, proving the one piece of real work the
commission names rather than touring the command set. And the cost is
stated as a measured fact — which key, how many of them, what breaks — in
the same flat register as the capability, the way Gregg quantifies his own
recommendation's downside before a reader can object to it. A writer working
from the default alone would produce a competent survey of VisiData's
commands. This guide is aimed at one proof, staged in real time, with its
price named in the same sentence as its power.
