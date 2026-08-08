# Editorial review: tech-news/2026-08-08 (editor/02)

Focused second invocation. Scope is the writer/02 rewrite only: the headline,
the `<h1>`, and the item-1 `<h3>`, all now reading "One untrusted GitHub issue
broke three coding agents at the harness, not the model." Everything else was
cleared in editor/01; I confirm it stayed cleared.

## Skeptic

The routed finding from editor/01 was that the old display line ("reached code
execution in Claude Code, Gemini CLI, and Codex") distributed "code execution"
to all three named tools when the record and the article's own table establish
it for only Gemini CLI. I tested the replacement claim against the same record.

New display claim, broken into its parts and each tested:

1. **"broke three coding agents ... at the harness, not the model" — HELD.**
   "Broke" is an aggregate verb that commits to no per-tool outcome, so the
   overclaim editor/01 caught is gone. Each of the three was in fact compromised
   at the harness layer, and the table carries the per-tool detail the headline
   deliberately withholds: Gemini CLI OS command injection (code execution,
   CVE-2026-12537, CVSS 10.0), Claude Code API-key exfiltration (credential
   theft, CVE-2026-54316), and Codex instruction injection via a shared checkout
   (no CVE, workflow fix). The headline no longer says any specific thing
   happened to any specific tool; it says three agents were broken at the
   harness, which the table then itemizes. That is the correct headline/table
   division of labor. The severity asymmetry (Codex drew no CVE) does not falsify
   an aggregate "broke," because "broke" claims a trust failure, not a uniform
   outcome.

2. **"at the harness, not the model" — HELD, and it is the thesis.** Owned by
   Novee (s1): the flaws are in the harness around the agents, "not the models."
   Corroborated by eSecurityPlanet (s2): "hidden trust assumptions within AI
   agent harnesses rather than isolated implementation mistakes." This is the
   single best statement of the finding, and a headline is exactly where the
   finding belongs.

3. **"One untrusted GitHub issue" — HELD.** The single-untrusted-issue,
   zero-privilege entry vector is the primary's own framing (Novee, s1) and is
   corroborated by both independent secondaries as the shared "single GitHub
   issue -> harness trust failure" narrative. The per-tool mechanisms (a crafted
   `.gemini/.env`, the Hugging Face download counter, a first-pass `AGENTS.md`)
   are downstream of that one untrusted input, so naming the input in the
   headline is faithful, not a compression that outruns the sources. Editor/01
   already accepted this framing in the thesis paragraph; the rewrite lifts it
   into display text without stretching it.

Display-text descriptor audit: "three coding agents" = the Anthropic, Google,
and OpenAI agents named throughout (Claude Code, Gemini CLI, Codex). No named
person, title, place, date, or quantity appears in the new line, so there is no
label to mis-set. The line is present and byte-identical in all three required
locations (nb-meta `title`, `<h1 class="nb-title">`, item-1 `<h3>` anchor); the
`<h3>` still links s1 (Novee), the owner of the claim it makes.

Unchanged-surface checks, all confirmed:
- The dek is byte-identical between nb-meta `dek` and the rendered
  `nb-dekline`, and unchanged from editor/01. It still makes a claim about the
  world (Meged traced the flaw to the harness, reaching RCE and credential theft
  from one unprivileged issue) rather than grading the article's selection, and
  it adds who/what/where without restating the headline.
- Items 2-4 (Terafab, AMD/Taalas, Kioxia/SanDisk) are untouched and match
  editor/01.
- The CVE table is untouched, and the item-1 body is intact, including
  editor/01's split of the mis-attached relative clause ("The fix landed in
  release 2.1.163. The bug affected every release from 0.2.54 to that fix.").

## Cut

No new prose to cut; the change is a one-line replacement. I checked the new
line against the tells:
- **No triad.** The comma-list of three tool names that carried the old triad
  headline is gone. The line names no three-item series.
- **No colon subtitle, no Betteridge question, no house catchphrase.**
- **Hedged contrast.** "not the model" is a "not X" contrast, but it corrects a
  real, named misconception (that agent safety is a property of the model) and
  is a strawman for no one working in this area. It is the most earned contrast
  in the piece and sits at the top precisely because it is the finding.

One observation, not blocking and deliberately not acted on: the harness-vs-model
contrast now appears both in the headline ("not the model") and in the item-1
lede ("not in the model's weights"). Editor/01 evaluated the piece's body
contrasts and protected that lede sentence as earned. Cutting it now would
reverse a prior protected decision, touch a body sentence the brief scopes as
untouched, and impose a new standard late in the loop for what is at most
optional polish. For a brief whose entire spine is the harness-vs-model claim,
stating it in the headline and developing it in the first sentence is
acceptable, so I left the lede intact.

Grammar of the new line is clean: subject ("One untrusted GitHub issue"), fresh
verb ("broke"), surprise in the first words, qualifier last.

## Reader

Read as the largest claim, the headline now passes the one test it failed in
editor/01: it commits only to what the piece establishes. A reader who reads
nothing else leaves with the true and load-bearing point (an untrusted issue
broke three vendors' agents at the harness) and is not handed the false
distributed-RCE label. The dek then supplies the outcomes and the researcher,
and the table supplies the per-tool specifics. The synthesis editor/01 credited
as the article's original work is now correctly labeled by its own headline
instead of overrun by it. The line reads closer to the voice-guide exemplars
(claim-first, actors and mechanism named) than to a median summary.

## Edits

- None. The rewrite is correct and self-consistent; no direct cut or prose fix
  was needed, so no `nb stamp` run was required (writer/02 already stamped:
  words=890, sources=9, reading_minutes=4, consistent with the nb-meta block).

## Required work

- None. The single routed finding from editor/01 is resolved and no new
  publication-blocking issue is present.

## Decision

approve — the rewritten headline/h1/item-1 h3 states an aggregate claim the
piece and its table establish ("broke three coding agents at the harness, not
the model"), drops the false distributed-code-execution label and the triad
mold, and the dek and items 2-4 remain untouched and correct.
