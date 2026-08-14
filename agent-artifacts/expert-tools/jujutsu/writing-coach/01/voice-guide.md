# Voice guide: expert-tools/jujutsu (01)

## How this piece should sound

This is a piece for an engineer who already runs Git commands from muscle
memory and is being asked to trust a different model of what a change is.
The job is to make that model concrete before it is judged, the way Mary Rose
Cook's opening commits to working from the graph structure itself rather than
"hypotheses constructed from evidence gathered while experimenting with the
API" — say what the working-copy commit and the operation log actually do to
files on disk at each step, not what they let the user "feel," before drawing
any conclusion from it. A reader who lives in Git will not take `jj undo`'s
safety on your word; show the op log entry it is restoring.

Julia Evans's branches post opens by telling the reader directly what she
noticed and what she is about to walk through, in two sentences, before any
git-branch vocabulary appears. This article can open the same way on its own
central surprise — the working copy already being a commit, or the operation
log recording every command — without a wind-up paragraph of context first.
State the surprise, then build it.

The honest-cost section is where Tommi Virtanen's plain declaratives earn
their place: "Don't rebase branches that others have created new commits on
top of. It is possible to recover from that, it's not hard, but the extra
work needed can be frustrating." No hedge, no "it should be noted," just the
cost and its size. The commission asks for the same judgment on the Git-interop
caveats, the muscle memory that stops transferring, and the project's
maintenance state — each one can be stated in that register: what breaks, how
bad it is, done.

Where the muscle memory does transfer, Evans's move — holding "the intuitive
model isn't wrong" and "git doesn't know what you mean" as both true at once
— is the shape to reach for rather than a flat verdict either way. A reader
who has rebased a thousand times in Git is not starting from nothing with
`jj`'s @ revision or its conflict-as-commit model; some of what they already
know still applies, and saying exactly which parts do is more useful than
declaring the whole model foreign.

Cook allows herself exactly one line of color inside an otherwise precise
paragraph — "Git has a fading memory that must be jogged with increasingly
vicious prods" — and earns it by having spent the surrounding sentences on
plain description first. The house register is calm and precise; a piece
that wants a phrase like that for the op log or for first-class conflicts can
have one, planted the same way, after the mechanism is already on the page
rather than instead of it.

Virtanen introduces "post-it notes" once, defines exactly what it stands for,
and then reuses it instead of reaching for a new figure each time a ref comes
up. Whatever concrete image this piece picks for the working-copy commit or
the op log — and it should pick one, since the reader needs something to hold
onto that is not the word "snapshot" repeated — the same discipline applies:
name it once, keep the name, and only reuse it where the thing itself
recurs.

## Julia Evans, "git branches: intuition & reality"

Source: https://jvns.ca/blog/2023/11/23/branches-intuition-reality/

> "Hello! I've been working on writing a zine about git so I've been thinking
> about git branches a lot. I keep hearing from people that they find the way
> git branches work to be counterintuitive. It got me thinking: what might an
> "intuitive" notion of a branch be, and how is it different from how git
> actually works?"

The post opens with what she noticed and the question it raised, not with
background on what a branch is. The two clauses at the end of the paragraph
are the actual table of contents for the piece — she names the comparison
she's about to run before running it, instead of building up to it. The
"I" throughout is a specific person reporting what she has been thinking
about, not a narrator addressing a reader.

> "I think it's pretty popular to tell people that their intuition about git
> is "wrong". I find that kind of silly – in general, even if people's
> intuition about a topic is technically incorrect in some ways, people
> usually have the intuition they do for very legitimate reasons! "Wrong"
> models can be super useful."

This is a correction of a common claim rather than of a reader's belief, and
she names the claim before she disputes it. The judgment ("I find that kind
of silly") is stated once and then backed by a reason in the very next
clause, rather than left to stand alone as an assertion.

> "Internally in git, branches are stored as tiny text files which have a
> commit ID in them. That commit is the latest commit on the branch. This is
> the "technically correct" definition I was talking about at the
> beginning."

Three short sentences, each doing one job: what the thing is, what it means,
and how it connects back to the claim made earlier in the post. Nothing here
is qualified or softened; the definition is stated flatly because by this
point in the piece she has already earned it with the picture and the
example above it.

## Mary Rose Cook, "Git from the inside out"

Source: https://maryrosecook.com/blog/post/git-from-the-inside-out

> "The essay assumes you understand Git well enough to use it to version
> control your projects. It focuses on the graph structure that underpins
> Git and the way the properties of this graph dictate Git's behavior.
> Looking at fundamentals, you build your mental model on the truth rather
> than on hypotheses constructed from evidence gathered while experimenting
> with the API. This truer model gives you a better understanding of what
> Git has done, what it is doing, and what it will do."

This states a method, not just a topic: the essay will work from the
underlying structure rather than from observed command behavior, and it says
why that produces a better mental model. The contrast in the third sentence
— truth versus "hypotheses constructed from evidence gathered while
experimenting with the API" — is precise enough to name exactly what usually
goes wrong when people learn a tool by trial and error.

> "git init makes the current directory into a Git repository. To do this,
> it creates a .git directory and writes some files to it. These files
> define everything about the Git configuration and the history of the
> project. They are just ordinary files. No magic in them. The user can read
> and edit them with a text editor or shell. Which is to say: the user can
> read and edit the history of their project as easily as their project
> files."

Every sentence reports what a single command actually did to the
filesystem, then the two-word sentence "No magic in them" breaks the rhythm
to state the point the paragraph has been building toward. The final
sentence translates the mechanism into what it means for the user, and does
so only after the mechanism has been shown in full.

> "Graph property: the working copy and the commits pointed at by refs are
> readily available, but other commits are not. This means that recent
> history is easier to recall, but that it also changes more often. Or: Git
> has a fading memory that must be jogged with increasingly vicious prods."

The first two sentences are as plain as the rest of the essay. The third
adds one image and stops — it does not keep extending the metaphor into the
next paragraph. The label "Graph property" that opens it is doing real work
across the piece: everything that follows a label like that is a
consequence being derived, not a new claim being introduced.

## Tommi Virtanen, "Git for Computer Scientists"

Source: https://eagain.net/articles/git-for-computer-scientists/

> "References, or heads or branches, are like post-it notes slapped on a
> node in the DAG. Where as the DAG only gets added to and existing nodes
> cannot be mutated, the post-its can be moved around freely. They don't get
> stored in the history, and they aren't directly transferred between
> repositories. They act as sort of bookmarks, "I'm working here"."

The post-it image is introduced with a definition attached to it — what
moves, what doesn't, what it isn't — rather than left as decoration. The
closing quotation, "I'm working here", is the only first-person voice in the
whole piece, dropped in for one clause to say what a ref means to the person
using it before the essay returns to describing the mechanism.

> "Here's what the tree will look after a few commits on both branches and
> another merge. See the "stitching" pattern emerge? The git DAG records
> exactly what the history of actions taken was."

A rhetorical question sits in the middle of an otherwise flat description,
timed to land right as a diagram would show the pattern it's asking about.
The sentence after it states the conclusion in eight words and moves on
rather than lingering on it.

> "Your old commit(s) will remain in the DAG until garbage collected. Ignore
> them for now, but just know there's a way out if you screwed up totally.
> If you have extra post-its pointing to your old commit, they will remain
> pointing to it, and keep your old commit alive indefinitely. That can be
> fairly confusing, though.
>
> Don't rebase branches that others have created new commits on top of. It
> is possible to recover from that, it's not hard, but the extra work needed
> can be frustrating."

"Screwed up totally" is the one piece of loose language in an otherwise
formal glossary, and it lands exactly where the essay is naming a real risk
rather than a mechanism. The instruction that follows it — don't rebase
branches other people have built on — is stated as a plain rule with its
cost sized in the same breath: recoverable, not hard, but extra work.
