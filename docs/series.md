# Series — modes, rhythm, and governing your paper

A series is one section of your paper: a folder under `press/series/<id>/`
holding `series.yaml` (the rules), `prompt.md` (the editorial instructions),
and optional `sources/`. Working examples of everything below live in
`examples/series/`.

## The four modes

| Mode | You declare | Each night publishes | Ends? |
|---|---|---|---|
| `collection` | an item list | the next unpublished item (or any, with `selection: random`) | when the list is done |
| `sequence` | an ordered syllabus | the lowest-numbered missing item, building on the published ones | when the syllabus is done |
| `rolling` | nothing — the date is the item | today's UTC date | never (until paused) |
| `open` | a *beat* in prompt.md | a topic the agent picks within the beat, in the template it judges fits best | never (until paused) |

**Open mode is the hands-off paper.** You describe a beat ("under-covered
corners of the AI stack"); the night shift reads the desk's back catalog,
picks something new, and chooses its form from the series' declared
`templates:` choice list (or its single `template:`). Want ~6 varied reads a
day without curating items? Run several open desks with distinct beats — one
edition per series per night is the invariant, so desks are how a paper gets
breadth.

**Commissioning:** an open desk may still carry `items:` — that's its
commission queue. Anything you add must be published (in any order, with its
own prompt/sources if given) before the desk freestyles again. The proof
enforces this, so "cover X next" is a one-line edit with a guarantee.

## Rhythm

```yaml
cadence: daily        # default · weekdays · weekends · [mon, thu]
paused: true          # skip this series entirely; the archive stays up
```

Cadence is why one nightly schedule is enough forever: the run itself asks
`engine/duty.py` what is due tonight, so a weekly deep-dive desk and a daily
brief coexist under the same schedule. Pausing is the vacation switch — the
proof refuses new editions for a paused series, so nothing publishes by
accident.

## Quality and sources

Per series: `words: [low, high]` (may tighten, never loosen below the
template's registry floor), `min_sources`, `strict: true` (every WARN becomes
a BLOCK), `autopublish: false` (a human merges instead of the editor), and
the source policy — `required_docs`, `consult`, `sources_exclusive` — described
in the [README](../README.md) and demonstrated in `examples/series/ai-rules/`.

## Governing without YAML

Day to day you steer by talking to your agent (the librarian skill): *"pause
frontier-compute"*, *"make the wildcard desk weekly"*, *"commission a dossier
on ASML"*, *"less policy in the brief for a while"* (a prompt.md edit). Every
change is one small diff on `main`, validated by
`python3 engine/validate_config.py`.
