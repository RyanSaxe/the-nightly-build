# Voice guide: explicit lazy imports in Python 3.15 (PEP 810)

## How this piece should sound

The reader can already read Python and reason about CPython. Write for someone
who wants to know exactly what `lazy import json` does to the interpreter, not
someone who needs to be sold on it. The register is exact, calm, and sure of
itself. Use the feature's own words without ceremony: a lazy statement binds a
proxy, first use of the bound name reifies it, the real module replaces the
proxy, an import error and any import-time side effect move from import to first
use. Define the words that belong to this feature where they first appear, and
assume the ones a Python reader already holds. Do not reach for a softer synonym
once you have named the proxy or named reification. Naming the two states once
and keeping the name is what lets the rest of the piece be short.

Keep the two states apart in every sentence that touches them. "The name is
bound to a proxy" and "the module has been imported" are different facts, and a
sentence that lets one slide into the other is where this subject goes wrong for
a reader. Batchelder's whole method is holding "rebinding a name" and "mutating
a value" apart and refusing to let informal English blur them; the proxy and the
reified module ask for the same discipline. When you walk code that shows the
binding, `sys.lazy_modules`, a `LazyImportType` proxy, or the moment of
reification, name the one line or object that carries the mechanism and tell the
reader what to take from the rest, the way Cannon points at a single C call as
the key bit and waves the reader past the stack manipulation. If the
demonstration shows `dis` output or interpreter internals a reader may not fully
parse, say plainly what they should get from it.

Say what the feature is for and why its default behaviour is what it is before
you weigh any cost. PEP 810 exists to defer the loading of modules a program may
never touch, chiefly heavy optional dependencies that inflate startup. State
that rationale in its own terms, the way Batchelder defends mutation-through-
shared-references as not a bug and gives the reason it has to work that way.
Then give the failure mode its exact boundary. Moving an import's errors and
side effects to first use is the one thing most likely to surprise a reader, so
name the condition under which it breaks a program, a project that relied on an
import running its side effect at import time, and say when it is otherwise
fine, rather than leaving a general unease. Smith's honesty about the lock
example, that it is impossible to know for certain and that only some programs
need the stricter approach, is the model: bound the risk, do not just gesture at
it.

Where reification is easier to hold as a staged handoff, a proxy, then first
use, then the real object, a plain analogy may carry it, as Smith frames signal
delivery as a chain of custody handed up from low-level to higher-level code.
Keep such an analogy only where the plain sequence cannot land on its own. Where
you show how the proxy is created or how it replaces itself on first use, the
order of operations may itself need explaining, not only the result, the way
Smith explains why CPython assigns the exception fields before dropping the old
references. If the original contribution measures import or startup cost, report
what was run and let the figures stand without rating them. Land the piece on
when a `lazy` import earns its place and when eager import is the right default,
given the behaviour you showed, and leave that as the reader's call the way
Batchelder leaves mutating versus rebinding to the effect you need.

## Brett Cannon, "Unravelling attribute access in Python"

Source: https://snarky.ca/unravelling-attribute-access-in-python/

> "Now there will be some C code in the beginning of this post, but I don't expect you to fully understand what's going on with it. I will explicitly say what you should get from the C code, so if you don't have any background in C it shouldn't hurt your understanding of what I'm about to talk about."

Checked: https://snarky.ca/unravelling-attribute-access-in-python/, retrieved 2026-10-03
Cannon tells the reader up front exactly how much of a hard listing they are
responsible for, and promises to extract the point for them. He is a CPython
core developer writing without any display of it; the confidence is in how
little he asks the reader to carry, not in vocabulary.

> "Most of that is just stack manipulation code that we can ignore. The key bit is the PyObject_GetAttr() call which is what truly implements attribute access."

Checked: https://snarky.ca/unravelling-attribute-access-in-python/, retrieved 2026-10-03
Faced with a block of C, he names the single line that matters and dismisses the
rest in one clause. The reader's attention is spent only where the mechanism
lives. This is how he walks every listing: find the load-bearing call, say so,
move on.

> "While I would say no individual part is overly complicated conceptually, all together it does lead to a lot going on. This is also why some people try to minimize attribute access in Python when in very performance-critical code to avoid all of this machinery."

Checked: https://snarky.ca/unravelling-attribute-access-in-python/, retrieved 2026-10-03
He closes by conceding the cost he just traced, and ties it to a real thing
people do about it. The judgment is specific and checkable, and he states it
flatly rather than dressing it as a lesson.

## Ned Batchelder, "Facts and myths about Python names and values"

Source: https://nedbatchelder.com/text/names.html

> "Here we haven't changed which value nums refers to. At first, the name nums refers to a three-element list. Then we use the name nums to access the list, but we don't assign to nums, so the name continues to refer to the same list. The append method modifies that list by appending 4 to it, but it's the same list, and nums still refers to it."

Checked: https://nedbatchelder.com/text/names.html, retrieved 2026-10-03
Batchelder narrates the code one operation at a time and uses the exact verb
for each: the name refers, we access, we don't assign, append modifies. Nothing
is approximate, so the reader can follow which thing changed and which did not.
The repetition of "refers to" is deliberate, one idea kept under one word.

> "Keep in mind, this is not a bug in Python, however much you might wish that it worked differently. Many values have more than one name at certain points in your program, and it's perfectly fine to mutate values and have all the names see the change. The alternative would be for assignment to copy values, and that would make your programs unbearably slow."

Checked: https://nedbatchelder.com/text/names.html, retrieved 2026-10-03
He anticipates the reader's complaint about a surprising behaviour and answers it
by giving the reason the design has to be this way. He is fair to the design
before the reader can decide it is wrong, and the reason is concrete, not a
reassurance.

> "It's really important to keep in mind the difference between mutating a value in place, and rebinding a name. augment_twice worked because it mutated the value passed in, so that mutation was available after the function returned. augment_twice_bad used an assignment to rebind a local name, so the changes weren't visible outside the function."

Checked: https://nedbatchelder.com/text/names.html, retrieved 2026-10-03
He has just shown two near-identical functions, one that works and one that
does not, and he explains the difference in terms of the single distinction the
whole piece rests on. The contrast does real work because the misconception it
corrects is the one the code was built to expose.

## Nathaniel J. Smith, "Control-C handling in Python and Trio"

Source: https://vorpus.org/blog/control-c-handling-in-python-and-trio/

> "most Python code has dozens of these kinds of dangerous moments when a KeyboardInterrupt will violate invariants. Our running example uses a lock because trio is a concurrency library, but the same thing applies to open files, database transactions, any kind of multi-step operation that mutates external state... usually you're lucky enough to get away with it, especially since the program usually exits afterwards anyway, but it's basically impossible to know for certain, so if you need 100% reliability then you need a different approach."

Checked: https://vorpus.org/blog/control-c-handling-in-python-and-trio/, retrieved 2026-10-03
Smith generalizes from one concrete example to the class of cases it stands for,
then bounds the risk honestly: usually fine, impossible to be sure, and here is
the exact condition under which you must do something else. The caveat states
something checkable instead of advertising caution.

> "And then we have to make sure that our program checks this flag on a regular basis at places where we know how to safely clean up and exit. The best way to think about this is that we set up a "chain of custody" where responsibility for handling the signal gets handed along from tricky low-level code up to higher-level code whose execution context is better-defined"

Checked: https://vorpus.org/blog/control-c-handling-in-python-and-trio/, retrieved 2026-10-03
He describes the mechanism plainly, then offers one analogy that makes the
handoff easier to hold, and the analogy is doing explanatory work rather than
decorating. He is a Trio author and CPython contributor, and the register stays
unforced.

> "You'll notice this is written in a slightly complicated way, where instead of simply overwriting the old values, they get saved in temporaries etc. There are two reasons for this. First, we can't just overwrite the old values because we need to decrement their reference counts, or else we'll cause a memory leak. But we can't decrement them one by one as we assign each field, because Py_XDECREF can potentially end up causing an object to be deallocated, at which point its __del__ method might run, which is arbitrary Python code, and as you can imagine you don't want to start running Python code at a moment when an exception is only half raised."

Checked: https://vorpus.org/blog/control-c-handling-in-python-and-trio/, retrieved 2026-10-03
He walks a listing by explaining why it is ordered the way it is, not just what
each line does, carrying the reader from the odd-looking code to the exact
hazard the order avoids. Each step hands off to the next, so a reader arrives at
"arbitrary Python code at the wrong moment" having been shown why it matters.
