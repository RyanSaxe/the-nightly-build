# Voice guide: Outlines (expert-tools/outlines, 01)

## How this piece should sound

This piece reconstructs a mechanism: an FSM compiled from a schema, a mask
built from that FSM's current state, logits zeroed at each decoding step. The
reader is a machine-learning engineer who can check the reconstruction
against the implementation. Nelson Elhage opens his tail-call interpreter
piece by naming the surprising finding in one sentence before he has earned
it, then spends the piece earning it. This piece can do the same with whatever
verdict it reaches about the index or the maintenance record: state it early
and plainly, then build the case under it, rather than saving the judgment for
a closing paragraph the reader has to trust on arrival.

The guarantee can be proved before it's explained, the way Julia Evans runs
the function from inside gdb, three lines of output and a returned value,
before she opens up how the call actually happens underneath. This piece
already has its worked example: constrained generation against a schema,
shown valid by construction, against the retry-and-parse path it replaces.
That demonstration can do the same work Evans's three lines do: earn the
reader's attention for the mechanism section that follows, rather than serve
as an installation step on the way to the real content.

The mechanism itself has room to be built the way Dan Luu builds his fsync
example: one version of the code, the exact failure it doesn't handle, the
one change that fixes that failure, repeated until the full protocol is
standing. The FSM-over-vocabulary approach has the same shape available to
it, naive sampling, then masking, then the reason masking alone isn't cheap,
then the index that makes it cheap, with each step earning its place by
naming the specific problem the previous step left open, rather than the
finished mechanism presented whole and narrated after the fact.

Wherever the piece states what the implementation does, where the mask
actually gets applied, what the index precomputes, where the cost of
building the index actually lands, the artifact that proves it can stand in
for the assertion, the way Elhage counts indirect jumps with objdump and
grep rather than asserting the compiler optimized the loop. A code excerpt
from the library, the shape of an array, a number from a benchmark or a
release log can do more work here than a sentence asserting the same thing.

The piece can also afford Evans's plain admission when the reconstruction hits
a real limit, a place the implementation doesn't fully explain itself from
the outside. Saying so plainly costs nothing next to a paper that read past
the README to get here, and a confident sentence papering over a genuine gap
is exactly what breaks trust with this reader.

The maintenance-and-adoption judgment is one section of this piece, not its
register throughout. Luu's dry treatment of the ext manpage's citation to
"rumor" is the model for that section specifically: state exactly what the
release history, the issue tracker, or the documentation does and doesn't say,
and let the specific gap or the specific figure carry the judgment, rather
than reaching for a word like "concerning" to do that work for it.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "Let's look at a simple example of what it takes to save data in a way
> that's robust against a crash. Say we have a file that contains the text
> `a foo` and we want to update the file to contain `a bar`. The pwrite
> function looks like it's designed for this exact thing. It takes a file
> descriptor, what we want to write, a length, and an offset. So we might try
>
>     pwrite([file], "bar", 3, 2)  // write 3 bytes at offset 2
>
> What happens? If nothing goes wrong, the file will contain `a bar`, but if
> there's a crash during the write, we could get `a boo`, `a far`, or any
> other combination."

Luu opens the technical argument with the smallest version of the problem, a
single pwrite call, and lets the failure case do the work of showing why it's
insufficient. The prose doesn't tell the reader the naive approach is wrong;
the three garbled outcomes do. This is the first rung of a ladder the piece
climbs one fix at a time, and each rung is a runnable line of code, not a
description of one.

> "The authors find issues with most of the applications tested, including
> things you'd really hope would work, like LevelDB, HDFS, Zookeeper, and
> git. In a talk, one of the authors noted that the developers of sqlite have
> a very deep understanding of these issues, but even that wasn't enough to
> prevent all bugs. That speaker also noted that version control systems were
> particularly bad about this, and that the developers had a pretty lax
> attitude that made it very easy for the authors to find a lot of issues in
> their tools."

The judgment here ("a pretty lax attitude") is dry and specific rather than
inflated, and it's attached to a named group of developers and a named piece
of research, not floated as a general complaint. The sentence about sqlite
does real work too: it sets up a contrast (deep understanding, still not
enough) instead of a flat list of who failed.

> "Hardware memory ordering semantics are usually well documented in a way
> that makes it simple to determine precisely which operations can be
> reordered with which other operations, and which operations are atomic. By
> contrast, here's the ext manpage on its three data modes... The manpage
> literally refers to rumor. This is the level of documentation we have."

Luu doesn't say the filesystem documentation is bad; he quotes it, and the
manpage's own word ("rumoured") is left to make the case. The two-sentence
verdict that follows is short because the quotation already did the
persuading. This is judgment earned by evidence placed right before it, not
judgment substituting for evidence.

## Julia Evans, "How does gdb call functions?"

Source: https://jvns.ca/blog/2018/01/04/how-does-gdb-call-functions/

> "First, let's see that this is possible. I wrote a tiny C program that
> sleeps for 1000 seconds and called it `test.c`... Finally, let's attach to
> the `test` program with gdb:
>
>     $ sudo gdb -p $(pgrep -f test)
>     (gdb) p foo()
>     $1 = 3
>     (gdb) quit
>
> So I ran `p foo()` and it ran the function! That's fun."

The claim ("you can call C functions from gdb") gets demonstrated before it
gets explained. Four lines of terminal output are the evidence; the mechanism
section that follows earns its length because the reader already knows the
end result is real. The exclamation isn't filler here. It's attached to an
actual result the reader just watched happen.

> "I kind of said this already but – you can't just find the address of the
> function you want to run and then jump to that address. I tried that in
> gdb (`jump foo`) and the program segfaulted. Makes sense!"

This is a failed attempt reported plainly, with the specific command and its
specific result, not summarized as "a naive approach doesn't work." The voice
stays casual without losing precision: the segfault is the point, and it's
named directly.

> "Here are some of the system calls that gdb uses to set a breakpoint. It's
> really simple! It replaces one instruction with `cc` (which
> [...] means `int3` which means `send SIGTRAP`), and then once the program
> is interrupted, it puts the instruction back the way it was... This
> `PTRACE_POKEDATA` is how gdb changes the code of running programs."

Rather than describing what a breakpoint is, Evans shows the actual strace
output: the syscalls, the addresses, the before-and-after values. She lets
that stand as the explanation. The technical vocabulary (`PTRACE_POKEDATA`,
`int3`, `SIGTRAP`) is kept exact rather than softened, because the exact names
are what let a reader go verify it themselves.

## Nelson Elhage, "Performance of the Python 3.14 tail-call interpreter"

Source: https://blog.nelhage.com/post/cpython-tail-call/

> "Unfortunately, as I will document in this post, these impressive
> performance gains turned out to be primarily due to inadvertently working
> around a regression in LLVM 19. When benchmarked against a better baseline
> (such GCC, clang-18, or LLVM 19 with certain tuning flags), the performance
> gain drops to 1-5% or so depending on the exact setup."

The surprising finding is stated in the second paragraph, well before it's
earned, with the specific numbers already attached. Nothing is held back for
a reveal. The rest of the piece is free to spend its length on the mechanism
because the reader already knows where the argument is going.

> "For performance reasons (performance of the compiler, not the generated
> code), it turns out that Clang and LLVM, internally, actually merges all of
> the `goto`s in the latter code into a single `indirectbr` LLVM instruction,
> which each opcode will jump to. That is, the compiler takes our hard work,
> and deliberately rewrites into a control-flow-graph that looks essentially
> the same as the `switch`-based interpreter!"

The parenthetical at the start ("performance of the compiler, not the
generated code") heads off a specific misreading before it can happen, which
is a different move from hedging. "That is" introduces a restatement in
plainer terms rather than a new claim, and the exclamation point lands on an
actual reversal (the compiler undoing the programmer's optimization), not on
a sentence with nothing under it.

> "In addition to the performance impact, we can observe the bug directly by
> disassembling the resulting object code and counting the number of distinct
> indirect jumps:
>
>     $ objdump -S --disassemble=_PyEval_EvalFrameDefault ${clang18}/bin/python3.14 | egrep -c 'jmp\s+\*'
>     332
>     $ objdump -S --disassemble=_PyEval_EvalFrameDefault ${clang19}/bin/python3.14 | egrep -c 'jmp\s+\*'
>     3

When the argument needs proof that a compiler change collapsed many dispatch
points into one, Elhage doesn't assert it. He runs a command that counts
them, 332 against 3, and lets the two numbers make the case. The claim about
internal compiler behavior becomes checkable by anyone with the same binary
and the same shell.
