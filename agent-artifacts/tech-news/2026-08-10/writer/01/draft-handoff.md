# Draft handoff: tech-news/2026-08-10 (writer 01)

## Original work

The article separates each vendor's framing from its own primary record — most
sharply on the OpenAI item, where it reports that the Lean 4 certificates verify
only that the formalized theorems compile while no named mathematician had
publicly worked through the informal claims (reaction, not verification) — and
builds a side-by-side table of the EU Article 50 and California transparency
regimes that neither source constructs, showing one shared operative date
against two different scopes.

## Items and lead

Five items, one `nb-brief-item` each, in first-citation order:

1. **Lead — OpenAI ten math/TCS advances** (primary: OpenAI manuscript s1;
   independent account: Understanding AI / Timothy B. Lee s2). Sets the brief
   headline and dek. Chosen as lead over the two in-window items (Terafab 6 Aug,
   HBF 4 Aug) because for the declared ML-engineer reader it is clearly the most
   consequential development, which the brief permits.
2. EU AI Act Article 50 transparency obligations (primary: EC guidelines s3;
   independent: Cooley LLP s4).
3. California AI Transparency Act (primary: AB 853 enrolled text s5; independent:
   CalMatters s6). Carries the EU-vs-California comparison `nb-table`.
4. Terafab, Tesla/SpaceX $16.8B Texas fab (primary: Texas Governor s7;
   independent: TechCrunch s8, Electrek s9).
5. First HBF standard, SK hynix/Sandisk (primary: SK hynix newsroom s10;
   independent: HPCwire s11).

Each item carries exactly one primary and at least one independent account. One
table (EU/California), placed in item 3, is the only furniture; the HBF numbers
read cleaner as prose.

## Risk notes honored

- OpenAI: framed as "advances," not "solved ten open problems"; the "Astra" model
  name and the "$2,000" compute figure are **not printed** (both live only in the
  gated announcement blog, which is not cited). The skeptical line is the
  reaction/verification distinction, with Gowers and Bloom named as reactions.
- Dating: the dek and body do not imply every item broke on 2026-08-10; item
  headings and prose date each development to its own day (1-2 Aug, 2 Aug, 6 Aug,
  4 Aug).

## Proof result

`./nb check ... --series tech-news --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warning left
standing. `nb stamp`: words 820, reading_minutes 4, sources 11. nb-meta records
`harness: claude-code-routine`, `model: Opus 4.8`; dek and rendered dekline are
identical.

## Open question

None blocking. One carried caveat from the evidence record: the EUR 15M / 3%
Article 50 penalty is attributed to the independent legal analysis (Cooley, s4)
as reported context, since Article 99 was not read firsthand. It is stated in the
item as a ceiling ("can reach"), matching the record's own caveat.
