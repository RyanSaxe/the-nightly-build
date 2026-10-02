# Voice guide: technical/dbt-v2-rust-engine (01)

## How this piece should sound

The model is a practitioner who ran something and is telling a colleague what happened. The reader is fluent in programming and systems and has not necessarily used dbt, so the register is the one Russ Cox and Julia Evans use for readers like that: plain declarative sentences, the exact term for each thing, no warm-up, and no explaining what a compiler or a type checker is. A term specific to dbt gets one definition at first use and is then used the same way every time.

The central discipline is keeping three kinds of statement apart: what the writer ran and saw, what the documentation or the maintainers say, and what the writer infers. Evans does this in the sentence itself. Her output block comes first, then "I noticed" and what she saw, then "I believe the reason" for the part she did not observe. Cox does it by saying where the claim comes from: he read the source of the shell, he tested Linux and not Windows, and he says so in a parenthesis. Willison says which feature is described in which document ("described in PEP 723 and implemented by uv run") and then says what he saw. Vendor benchmark figures and phrases like "agent-ready" belong on the maintainers' side of that line and are attributed to them by name. Where the writer ran the command, the sentence states the result flatly, with no hedge on a thing that was observed. Where the writer did not run something, one clause says so and the sentence moves on. Hedge only what is unobserved, and do not carry caution into the sentences that report a result.

Command output goes in the listing, and the prose beside it points at the lines that matter. Evans prints the raw bytes, then names three things in them. Cox gives one benchmark, states its two numbers, and moves to the next question. The listing is not paraphrased before or after it, and the writer cuts the output to the lines the argument uses. When a first guess turns out to be wrong, the walkthrough says so in the place it happens, as Cox does when he moves from `ls` to the shell. A diagram of the parse, compile and run stages is worth including only if it shows where each kind of error gets caught, and the prose does not repeat the labels.

Limits and costs (adapter coverage, what sits outside the Apache-licensed engine, migration from v1) are reported as the same kind of fact as the findings: what was checked, against which document, with which figure. They are not placed in a closing balance paragraph. The piece ends where the argument ends, on the last thing it established, and does not grade itself. Nothing in the examples below ends on a verdict about its own importance, and the Technical desk's habit of doing so is the thing to avoid. The person is visible through choices of what to try next and what to say is unknown, and not through announcements of effort or care. First person is fine where the writer ran something ("I ran", "I installed"). The writer may leave it out where a plain statement of the result works as well.

Matklad's opening shows a third thing worth borrowing: say at the start what the piece is for and what it assumes the reader already has, in a sentence or two, and then do not mention it again.

## Russ Cox, "Glob Matching Can Be Simple And Fast Too"

Source: https://research.swtch.com/glob

> "In fact it’s the shell that evaluates the glob pattern in the first command, not ls, so let’s repeat the experiment with a variety of shells."

Checked: https://research.swtch.com/glob (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
He has just reported a benchmark and attributed it to `ls`. Here he corrects that attribution in one sentence and uses the correction to set the next experiment. The writer shows a fix to his own framing without apologizing for it, and the experiment is the next step of the reasoning.

> "The exception seems to be the original Berkeley csh, which runs in linear time (more precisely, time linear in n). Looking at the source code, it doesn’t attempt to perform glob expansion itself. Instead it calls the C library implementation glob(3), which runs in linear time, at least on this Linux system."

Checked: https://research.swtch.com/glob (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
He explains an anomaly in the data by reading the source, says that is what he did, and bounds the last claim to the system he tested. "Seems to be" marks the one guess, and the sentences on either side of it are flat statements.

> "PHP is not shown in the graph, because its glob function simply invokes the host C library’s glob(3), so that it runs in linear time on Linux and in exponential time on non-Linux systems. (I have not tested what happens on Windows.)"

Checked: https://research.swtch.com/glob (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
He explains why a result is missing from the chart and gives the consequence for each platform. The parenthesis names the one thing he did not test and takes one sentence. The person shows in what he chose to report as untested.

## Julia Evans, "What happens when you press a key in your terminal?"

Source: https://jvns.ca/blog/2022/07/20/pseudoterminals/

> "But this past week I was using xterm.js to display an interactive terminal in a browser and I finally thought to ask a pretty basic question: when you press a key on your keyboard in a terminal (like Delete, or Escape, or a), which bytes get sent? As usual we’ll answer that question by doing some experiments and seeing what happens :)"

Checked: https://jvns.ca/blog/2022/07/20/pseudoterminals/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
The opening states one concrete question, says how she came to ask it, and says the method is to run things. The reader knows after two sentences what will be measured. This piece is more casual than ours should be, so take the sequence (question, origin, method) and not the smiley or the tone.

> "When I press Ctrl+C, the client sends \x03. If I look up an ASCII table, \x03 is “End of Text”, which seems reasonable. I thought this was really cool because I’ve always been a bit confused about how Ctrl+C works – it’s good to know that it’s just sending an \x03 character."
>
> "I believe the reason cat gets interrupted when we press Ctrl+C is that the Linux kernel on the server side receives this \x03 character, recognizes that it means “interrupt”, and then sends a SIGINT to the process that owns the pseudoterminal’s process group. So it’s handled in the kernel and not in userspace."

Checked: https://jvns.ca/blog/2022/07/20/pseudoterminals/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
The observed fact ("the client sends \x03") is stated without a hedge, and the explanation of the mechanism behind it is introduced with "I believe". The reader can tell which part was logged and which part is her understanding of the kernel. The second sentence of the first paragraph is a lookup she did herself.

> "I noticed that this didn’t work in fish on my computer though – if I typed Escape and then [, it just printed out [ instead of letting me continue the escape sequence. I asked my friend Jesse who has written a bunch of Rust terminal code about this and Jesse told me that a lot of programs implement a timeout for escape codes – if you don’t press another key after some minimum amount of time, it’ll decide that it’s actually not an escape code anymore."

Checked: https://jvns.ca/blog/2022/07/20/pseudoterminals/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
A result that did not match her expectation is reported with the exact keystrokes and what appeared. The explanation is credited to a named person and not presented as her own finding. A reader can see which claims she tested and which she was told.

## Simon Willison, "Building Python tools with a one-shot prompt using uv run and Claude Projects"

Source: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/

> "Crucially, I didn’t have to take any extra steps to install any of the dependencies that the script needed. That’s because the script starts with this magic comment:"

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
He reports what he did not have to do, then names the mechanism that explains it, and a code block follows directly. The reader sees the behavior and the cause in adjacent sentences.

> "This is an example of inline script dependencies, a feature described in PEP 723 and implemented by uv run. Running the script causes uv to create a temporary virtual environment with those dependencies installed, a process that takes just a few milliseconds once the uv cache has been populated."

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
The feature is named, the specification and the implementation are credited separately, and the timing claim carries its precondition (a populated cache). The sentence is about the tool, not about how significant the tool is.

> "The pattern here that’s most interesting to me is using custom instructions or system prompts to show LLMs how to implement new patterns that may not exist in their training data. uv run is less than a year old, but providing just a short example is enough to get the models to write code that takes advantage of its capabilities."

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
His own interest is stated as his, with "to me", and the support is a fact with an age attached to it. It is the nearest thing to a conclusion in the post, and it is a finding about the method.

## Matklad (Alex Kladov), "Simple but Powerful Pratt Parsing"

Source: https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html

> "Understanding the algorithm myself for hopefully the last time. I’ve implemented a production-grade Pratt parser once, but I no longer immediately understand that code :-)"

Checked: https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
This is the last of four stated goals at the top of the post. He lists what the post is for in one short bullet each, including one that concerns his own memory. The reader learns the post's purpose and the writer's relationship to the material before any code.

> "Traditionally, text-books point out left-recursive grammars as the Achilles heel of this approach, and use this drawback to motivate more advanced LR parsing techniques."

Checked: https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
The standard view is stated in the terms its holders use, with a source named (textbooks), before he disputes it. The next paragraphs show the failing code and the loop that fixes it.

> "A theoretical fix to the problem involves rewriting the grammar to eliminate the left recursion. However in practice, for a hand-written parser, a solution is much simpler — breaking away with a pure recursive paradigm and using a loop:"

Checked: https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html (raw HTML fetched with curl and compared against the stripped text), retrieved 2026-10-02
He distinguishes what the theory says from what works in a hand-written parser, in the vocabulary of the field, and the sentence ends on a colon that leads directly into the code. The sentence leaves him one em-dash, and it is an actual aside. This house limits em-dashes, so the dash here is not a model.
