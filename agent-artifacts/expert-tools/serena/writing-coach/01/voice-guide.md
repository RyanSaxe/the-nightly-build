# Voice guide: expert-tools/serena (01)

## Directive

Register: the paper's calm, first-principles baseline, pushed toward the
tool-demo voice of Simon Willison. Write to an ML engineer who already runs
coding agents and reads code for a living. The relationship is colleague to
colleague at a terminal, not teacher to newcomer. Assume the reader knows what
an MCP server, a language server, and a coding agent are; spend no sentence
defining them.

This piece proves exactly one claim: that semantic, LSP-backed symbol retrieval
changes how an agent works a codebase. It proves that by running the operation
on real code, not by describing it. Every general sentence about what Serena
does should be cashing out an example the reader has just watched, or setting
the next one up. If a paragraph explains a capability with no operation nearby,
it is describing a brochure.

Moves that will change sentences here, beyond what the house default already
forces:

- Let the example carry the argument. Before each command or config block, say
  the one thing it is about to show. Run it. Then read the result back in a
  sentence, so the reader sees the win instead of being told it. Prose between
  blocks narrates only what makes the next block legible.
- Give the win a before and an after on the same task. Show the old path an
  agent takes without Serena (grep, read the whole file, spend the context) and
  the new path (one symbol operation) against the identical goal. The
  comparison then reads as measured, not asserted.
- Report a number and its limit in the same breath. Token cost, first-run
  indexing time, and per-language language-server coverage each get a concrete
  figure and, immediately, where it fails to hold. Do not let a favorable
  number stand a sentence longer than its qualification.
- Meet adoption costs where the reader would hit them, in your own voice, not
  quarantined in a disclaimer paragraph. Name the language-server gap or the
  setup friction at the point in the workflow where it bites.
- Headings name Serena and the specific work of that step (indexing a project,
  finding a symbol, editing at the symbol, what it costs), and each previews
  the outcome of the step rather than labeling a topic. Vary their grammar so
  the set does not read stamped.

## Licenses

```text
## Licenses

form: second-person instructional address ("you configure", "you run")
move: Willison and Evans speak to the reader as the person at the terminal
      about to run the command, which keeps the operation the subject.
bar:  each "you" fronts a real operation the reader performs in this workflow;
      cut any "you" that only gestures at a hypothetical reader's reaction.

form: annotated transcript (command or config block, then its output read back)
move: Willison states a block's purpose, shows it, then quotes the result to
      prove the capability; the output, not the sentence, is the evidence.
bar:  the surrounding prose adds what the raw block cannot show on its own
      (why this call, what changed); a block that only decorates a claim is cut.

form: one named contrast at the pivot (symbol operation vs. grep-and-read)
move: Hashimoto names the wrong assumption plainly, then dismantles it with the
      worked example rather than with the contrast itself.
bar:  the misconception is one a real ML engineer holds (that this is fancier
      grep), it is named once, and the two transcripts do the actual work; the
      "not X but Y" shape appears at most once in the piece.
```

## Recently used, do not reuse

- The opener "Behind the single command sits an NNN-line script," and any
  variant that opens the piece on a raw line count or a default value. Open on
  the operation or the changed workflow, not on an implementation statistic.
- The fixed heading frame "TOOL does X to the work" repeated across every
  section. The series requires that headings name the tool and the work, and
  that stays; vary the grammatical shape from heading to heading so the set does
  not read as one stamped template.

## Simon Willison, "Symbex: search Python code for functions and classes, then pipe them into a LLM"
Source: https://simonwillison.net/2023/Jun/18/symbex/
Craft:
- cadence: terse declaratives to open a point, longer sentences only while a
  capability unfolds; momentum comes from short lead sentences, not connectives.
- argument: concentric demonstrations, each use case more ambitious than the
  last, so range is proven by escalation rather than by a claim of range.
- evidence: every capability is a terminal transcript introduced by its purpose
  ("I'm using the wildcard here to find...") and closed by reading the result.
- stance: enthusiasm disciplined by review ("obviously I wouldn't check this in
  without a comprehensive review"); credible because it names its own limits.
- notice: friction gets equal billing with success (the PyPI error, the naming
  problem), which reads as honest reporting rather than a frictionless demo.
- diction: conversational-technical, peer to peer; lineage stated plainly
  ("loosely inspired by ripgrep"); assumes shell and Python without condescending.
- reader: direct address to a developer already thinking about tooling;
  parenthetical pointers give unfamiliar readers an exit without stalling the flow.
- the important move: the example is the proof. The reader watches capability
  happen in the transcript and forms the judgment; the prose never argues for
  what the output already shows. Nearest exemplar to Serena's own domain
  (symbol-level retrieval, output piped to a model); study its restraint.

## Mitchell Hashimoto, "Everyone Should Know SIMD"
Source: https://mitchellh.com/writing/everyone-should-know-simd
Craft:
- cadence: staccato claim then elaboration ("SIMD has a reputation for being
  complex" / "I think that's wrong"), a rhythm that states a position before
  defending it.
- argument: dismantle the objection, build the shared foundation, show one real
  loop, then validate with measured numbers; structure does the persuading.
- evidence: a single real Ghostty loop, scalar version first (one line), then
  vectorized (twelve lines), so the cost of the win is visible on the page.
- stance: presses the claim firmly but with epistemic humility; concedes what
  the compiler cannot be trusted to do rather than overclaiming his method.
- notice: attention tracks what matters in practice (the scalar tail, where the
  pattern breaks, why predictability beats a compiler's theoretical win).
- diction: technical terms introduced through context, never dropped as jargon;
  plain affirmations of the reader's capacity ("it is easy to understand").
- reader: treats the reader as an intelligent skeptic, invites skipping known
  sections, anticipates the objection ("why can't the compiler do this?").
- the important move: descending honesty on numbers. Theoretical maximum, then
  real-world result, then the qualification ("you always lose some of the ideal
  speedup"). This is the paper's baseline voice; hold Serena's benchmarks to it.

## Julia Evans, "More practical uses for strace!"
Source: https://jvns.ca/blog/2014/02/27/more-practical-uses-for-strace/
Craft:
- cadence: short, fragmentary, spoken rhythm; enthusiasm carried by sentence
  length rather than by adjectives.
- argument: exploratory cataloguing, each use case a small case study of the
  tool's reach; discovery framed as shared rather than pronounced from authority.
- evidence: concrete commands and their real output, each grounding an abstract
  claim about the tool's usefulness in something the reader could run.
- stance: open curiosity that admits its own gaps ("I didn't know syscall
  tracing was a thing"), which lowers the barrier to the reader trying it.
- notice: catalogs actual use cases from real practitioners instead of
  theorizing about value, so the usefulness is demonstrated in specifics.
- diction: deliberately informal, democratizing; the register says these
  powerful tools are within reach.
- reader: fellow-explorer address, implicit invitations to experiment.
- the important move: borrow her instinct to notice and name exactly what
  surprised her about a tool, and her grounding of every claim in a runnable
  command. Do not borrow her exclamation-driven register; this piece stays
  calm. She is the model for what to notice, not for how loudly to say it.
  Her catalog structure is also not this piece's structure: prove value with
  one worked example, not a list of them.
