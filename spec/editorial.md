# Editorial standard

This is the editorial standard every article meets, whatever its template.

The standard is prescriptive on purpose. Its job is to make the default professional:
research-grade writing. It reads in two registers.

- **Standards a paper cannot loosen.** The quality bar below: sourced claims, teach don't
  summarize, earned analysis, and prose free of fluff, slop, and run-ons.
- **Defaults a paper may override.** Everything that is taste rather than quality:
  register, formality, the assumed reader and that reader's background, how far to
  press a judgment, and any other choice of that kind. These belong to
  `press/editorial.md` and the series prompts. This standard sets the quality of those
  choices, never the choices themselves.

The standard bans failures, never forms. Any form is open to a voice that
earns it and a paper that licenses it.

The standard does not legislate trivia: no paper-wide rule on the Oxford comma. Be
consistent within a piece.

## Teach, don't summarize

The reader finishes knowing how to think about the topic. Each
section spends what the last one taught. A section the reader could have read first is in
the wrong place. Cut any sentence that adds nothing new. Define each term of art the
declared reader does not hold in the sentence where it first appears. Assume the rest.
Ground abstract claims in a worked example.

The declared reader centers the paper: the profile chooses what to cover and when, and
what background to assume. Write each piece for the natural audience around that center.
A paper declaring a new parent gets articles any parent could be handed. A declared
practitioner gets pieces worth forwarding to a colleague. Narrowing a series to
the reader personally takes an explicit ask in `press/editorial.md` or the series prompt.

## Report and analyze

Report what is true and analyze what it means. Hold the analysis to the same bar as the
reporting. Analysis must be earned: grounded in the cited evidence, its reasoning shown.
Keep three things distinct: reported fact, estimate, and synthesis. Never write that
someone hinted, implied, or signalled. That is the writer's guess wearing attribution.
Synthesis with a point of view is welcome. Cut unsupported opinion. How hard to
press a view is the paper's call, and a press that wants opinion may have a
column or an opinion series. The standard bans the unearned verdict, never the
verdict: an opinion meets the same bar as any analysis, cited, reasoned, shown.

## Citations

- Every claim the argument rests on carries an inline citation linking to a source entry.
- Prefer primary sources: the document that owns the claim, whatever form the document
  takes. Secondary reporting is acceptable for context. Contested figures need a
  primary source.
- Never fabricate, pad, or decorate citations. If you cannot source a claim, cut it or
  state the uncertainty plainly.
- Cite only what you have read. Open the source, find the passage that supports the
  specific claim, and cite that. Its URL must resolve.
- On contested questions, steelman the opposing views before you weigh them.

## Numbers

Concrete figures beat vague magnitudes. Ranges with sources beat false precision. Give
every number a comparison the reader already knows. Say plainly what is unknown.

## Clarity

An article is understood on the first read or it has failed. Abstraction is the usual
reason it fails: every abstract noun asks the reader to carry something unstated, and each
is a place a weak argument hides. Prefer the concrete. Reach for an abstraction only when
the abstraction itself is the subject, and build it up like any other term.

Name a thing one way and keep that name. Once a term is set, reuse it exactly. A synonym
reached for variety reads as a new thing.

Default to short, single-purpose sentences, and vary length for rhythm: a long
sentence in control is craft, and a page of uniform declaratives is a metronome. If a
sentence can be misread, rewrite it rather than trust the next one to rescue it.
Shorten by cutting, never by packing ideas denser. A paragraph carrying more ideas
than sentences has stopped explaining.

## Prose

The register is a serious paper, not a feed. `spec/slop.md` is the standard for
prose that reads as machine-written. It binds every article, and nothing a press
sets below loosens it.

That is the default register. An expressive form beyond it (e.g., direct
address, fragments, open humor, etc.) is licensed, never free.
`press/editorial.md` or the article's voice guide grants the license by naming
the form, the exemplar move being transferred, and the bar any single use must
meet. An unlicensed form is cut. A licensed use still meets every test above.

Break any rule here sooner than write a sentence no honest voice would say aloud.

## Punctuation

Punctuation sets the pace of a thought, and each mark has one job. Reach for the
plainest mark that does the job. When two marks would both work, the plainer one
is right, and when in doubt the period is the default.

- **Period.** The default. Two thoughts are two sentences. Most of the em-dashes,
  semicolons, and colons a draft reaches for are a period avoiding itself.
- **Comma.** Joins within a single thought, and sets off a short aside. It is not
  a splice: two independent clauses joined by a comma alone are two sentences.
- **Colon.** Introduces what the clause before it promises, a list or a
  definition or the payoff. The clause before it stands on its own. It is not a
  general connector between two thoughts.
- **Semicolon.** Rare. Two independent clauses so tightly bound that a period
  would over-separate them. Never a chain, never a patch on a comma splice, never
  a way to keep a run-on running.
- **Em-dash.** A real interruption or a sharp aside, at most once in a stretch.
  It is not a connective and not a semicolon in disguise. When you delete one,
  the fix is usually the period the thought wanted, not another mark in its place.
- **Parentheses.** A true aside the sentence survives without. If the sentence
  needs what is inside them, it is not an aside, so fold it back in.

A press extends this section for its own paper. It does not loosen it.

## Form

Each template's identity sets its own form: paragraph length, how the dek reads, how the
piece closes. A press may shadow them. This file holds those choices to a standard. Keep
the writing easy to follow. End on the conclusion the argument built. Skip the generic
moral. Let the teaching and the citations equip the reader to go further.

### Literal strings

Use inline `<code>` only when the reader must preserve a string's exact spelling: something
they could type, paste, execute, match, or distinguish character-for-character. It is not
technical emphasis. Ordinary terms, product names, model names, and prose do not wear it;
neither does every repeat of a literal once the sentence has established it. When several
tokens need comparison, give them a table or a code listing instead of turning a paragraph
into labels.

An article's form comes only from its template and its own content. Reading the published
library informs content and context: what a series has covered, what not to repeat. It
never informs form. A shape you find in an older piece records what the format was, not
what it should be now. A template that has moved on leaves its old structure in the
back-catalog, and copying that structure forward is how a retired section reappears where
it no longer belongs.

## Charts

Use a chart when a trend or comparison is the point. Charts are PNGs
rendered from the committed `chart-N.py` script beside the article
(spec/charts.md), never hand-drawn images or script blocks. Keep them honest:
label axes, note a non-linear scale, and cite the data source in the caption.
