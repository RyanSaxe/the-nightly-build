# Commission: tech-news/2026-08-02

## Assignment

The technology front page for UTC date 2026-08-02, on the `brief` template.
Authorized by the scheduled `nb duty` result (rolling series, selected UTC date
unpublished). One brief, 4-6 items.

## Angle and required contribution

Select the day's most consequential developments *in* technology. AI is central
to the brief, but significance decides the mix; product promotion, incremental
releases, and online attention do not qualify on their own. Science and health
belong when a result changes technical knowledge or practice enough to deserve
attention here, treated as the development itself. Each item spends its reported
facts to explain, in the writer's own reasoning, why it changes what a field can
do or how a practitioner should act. This paper has extra appetite where a story
runs through technology.

## Boundaries and neighbors

A same-date Current Events brief also runs. Split by the press rule: a
development *in* technology (a model, a research result, a security disclosure, a
capability, a standard) belongs here; a story whose *public-policy consequence*
is the news belongs to Current Events. Do not run the same event in both briefs.
Coordinate any AI-policy story so it is covered once.

Additional neighbor: this edition's Paper of the Day reconstructs word2vec (a
2013 NLP paper). Keep Tech News on *current* developments; do not let an item
drift into a retrospective that overlaps the paper desk.

Prefer a reputable US newsroom for independent reporting of comparable quality;
use the primary record regardless of country.

## Recent shapes to break (from the published library)

Recent tech-news briefs have leaned hard on one recurring lead: Claude/Anthropic
finding cryptographic weaknesses in post-quantum candidates (HAWK, a NIST
candidate) across 2026-07-30, 07-31, and 08-01, plus an AI-agent RCE
disclosure. Do not re-lead on "a model found a crypto flaw" or an AI-agent CVE
unless 08-02 brings a genuinely new such event; if the story continues, lead on
what advanced. Vary the dek from the banned molds (semicolon reversal, suspended
question, comma-triad-with-"and").

## Source policy

Template floor: `min_sources: 5` overall. Per item: exactly one primary
(`primary: [1, 1]`) and at least one independent secondary (`secondary: [1,
null]`). Prefer the primary that owns a technical claim (the paper, the
release notes, the advisory, the benchmark). Confirm every URL resolves.

## Production (models and effort)

Balanced profile. Resolved roles and models this run assigns:

- writing-coach: capable → `sonnet`, effort low (not required)
- researcher: capable → `sonnet`, effort high (not required)
- writer: capable → `sonnet`, effort medium (not required)
- editor: inherit → `opus` (this correspondent's model), effort high, **required**

Runtime caveat: isolated children run at their model's default reasoning effort;
effort tiers are not separately tunable here. Model per role is the honored
lever; the required editor runs on `opus`, the closest available option to
"inherit at high effort."

## Original work

The selection-and-consequence judgment: which technical developments matter today
and the specific reason each changes what a field can do or how practice should
change. That per-item reasoning is the article's original work.
