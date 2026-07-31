# Voice guide — expert-tools/files-to-prompt

Register: one CLI-fluent engineer telling another what actually changed in
the workflow. The reader already runs shells, greps repos, and pipes into a
model daily. Never explain what a flag is before showing what it does —
show the command, let its output do the explaining, and gloss only the one
choice that isn't obvious from the output itself. Nothing in this piece
should read as if written for someone who hasn't opened a terminal.

Open on the workflow problem, not the tool. Willison and Evans both start
from a live frustration — the credential that's too broad, the build that
needs a manual rerun — and name the tool only once the problem is concrete.
Do the same here: start from feeding a model too much or too little of a
codebase, then bring in `files-to-prompt` as the thing that resolved it, not
as the subject of an announcement.

Make one command carry the argument. Pick the single invocation that shows
the mechanism under discussion — the flag that scopes the slice, or the
`--cxml` structure that lets the model cite a file back precisely — and set
it as an `nb-code` listing with its real output beside it, run against the
actual repo used in the demonstration. Never narrate the command in prose
("first we run... then we..."); a sentence introduces why this exact
invocation matters, the listing shows it happening, and the next sentence
draws the conclusion the output supports. Prose carries what a terminal
can't: the reasoning, the cost, the workflow position. A second command
earns its place only if it shows a different mechanism, never a repeated
demonstration of the first.

Make "the right slice" concrete with the numbers this run actually produced:
how many files a glob or `--ignore` pulled in versus excluded, what that
did to file count or rough token volume, what got left out that would have
been noise. Argue from that one real count, not from the general idea of a
context budget.

Write the adoption cost in the same flat, declarative register as the
benefit — no "however," no softening. State each limit as a fact with a
consequence: it has no notion of relevance, so a glob left too wide feeds
the model files it didn't need, and there's no flag that catches that for
you — only the habit of scoping tight. Judge maintenance the same way: cite
the release cadence, the issue count, who merges, as facts, not a vibe.
The closing section renders the adopt-or-not verdict using only the facts
already shown in the piece — no new hedge introduced at the end to soften a
judgment the demonstration already earned.

Cut on sight, each for a reason: install-tutorial steps ("first, install...
then run...") bury the one mechanism that matters under setup the reader
didn't ask for, and the series exists specifically so the example proves
value instead of walking through a tutorial. Hype adjectives (powerful,
seamless, elegant) get discounted by this reader on sight — the demonstrated
output has to do the persuading, not the adjective in front of it. A
manufactured punchline ("here's the kicker," "the catch is") announces its
own stakes instead of making the argument, and this reader already caught
the argument in the command output. Scaffold headings (Installation, Usage,
Verdict) could sit over any tool's writeup; every heading here has to name
what this section of the argument does for `files-to-prompt` specifically.

Recently used, do not reuse: the last four expert-tools pieces (oil.nvim,
pydantic-monty, ast-grep, py-spy) each ran a single declarative headline
naming the tool and the concrete thing it did — keep that precision, but
don't reproduce their section shape or heading rhythm again in a row. None
of them used an Installation/Usage/Verdict scaffold; neither does this one.
If the tool ends up being the AST-based fallback, keep the framing on
assembling context for a model, not on AST mechanics — that ground belongs
to the ast-grep piece already published.

## Simon Willison, "s3-credentials: a tool for creating credentials for S3 buckets"
Source: https://simonwillison.net/2021/Nov/3/s3-credentials/
Craft:
- cadence: short paragraphs, one idea each, moving from problem to command to result without a transition sentence doing the work
- argument: the tool is justified by the specific annoyance it removes, stated once, plainly
- evidence: real commands run against a real bucket, with the actual generated output shown, not paraphrased
- stance: a builder describing his own tool without selling it — confidence comes from showing it work, not from claiming it works
- notice: introduces the simplest invocation first, then adds one flag at a time, each new flag justified by a slightly harder version of the same problem
- diction: plain nouns for AWS concepts, no jargon left unglossed and no jargon over-explained either
- reader: assumes AWS and IAM fluency; never defines a credential or a bucket
- the missed move: he states the security motivation once, up front, and then lets every subsequent example silently satisfy it rather than re-justifying the tool each time
Calibration: "I'm not at all keen on using my root-level credentials here: usually a project works against just one dedicated S3 bucket."

## Julia Evans, "entr: rerun your build when files change"
Source: https://jvns.ca/blog/2020/06/28/entr/
Craft:
- cadence: short declarative sentences, one command per short paragraph, almost no connective tissue between them
- argument: the case for the tool is the feedback loop it shortens, made once, then shown repeatedly at slightly higher difficulty
- evidence: a sequence of real invocations (`git ls-files | entr ...`), each a strict addition of one flag to the last
- stance: enthusiastic but never hyperbolic — the enthusiasm lives in how fast she moves to the next example, not in adjectives
- notice: flags a real limitation as soon as it comes up (untracked files aren't watched by default) and fixes it in the very next command rather than footnoting it
- diction: says "watch," "rerun," "restart" — verbs, not feature names — so the reader feels the mechanism instead of memorizing a term
- reader: assumes git and a build step already exist; teaches nothing about either
- the missed move: she never writes a sentence that only exists to introduce the next command ("now let's look at..."); the command follows the prose because the prose already needed it
Calibration: "quick feedback is amazing" — followed immediately by the command that produces it, not by more claims about it.

## Dan Luu, "Advantages of monorepos"
Source: https://danluu.com/monorepo/
Craft:
- cadence: long paragraphs built from short, unhedged sentences; conclusions stated flatly before the evidence that supports them
- argument: makes the positive case in full first, then explicitly declines to relitigate the well-known downsides rather than pretending they don't exist
- evidence: concrete organizational examples (Google, Facebook, Twitter) tied to a specific practice, not a general claim about "big companies"
- stance: opinionated and comfortable saying so, but every claim is a specific mechanism, never a vibe
- notice: names the exact operation a monorepo makes cheap (one commit refactors the API and every caller) instead of describing the benefit abstractly
- diction: no qualifiers stacked on a claim; a sentence commits or it gets cut
- reader: assumes familiarity with large codebases and cross-team dependencies; no onboarding
- the missed move: he draws the boundary of his own argument out loud ("I'm not going to discuss them because...") instead of quietly omitting the countercase, which reads as more honest than either arguing it away or ignoring it
Calibration: "With a monorepo, you just refactor the API and all of its callers in one commit."
