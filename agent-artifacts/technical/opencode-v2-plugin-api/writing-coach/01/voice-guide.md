# Voice guide: technical/opencode-v2-plugin-api (01)

## How this piece should sound

This is a walkthrough of a plugin API for people who write TypeScript and run a terminal coding agent. The reader wants to write a plugin or move an existing one, and will have the source or the type definitions open next to the article. The register is a working engineer explaining what they just read and ran: plain declarative sentences, first person where the author did something ("here is what I get"), and the project's own identifiers spelled exactly as they appear in the code. All three writers below treat the reader as someone who can follow a stack of mechanism if each step is shown. None of them reassures, sells, or announces what is coming.

Show the code and then say what it does. Willison's toolbox passage and Abramov's ColorPicker passage both put a snippet in front of the reader and then read it back in sentences: which part moved, what is passed where, what therefore does not happen. For a plugin API, that means a hook signature, a tool definition or a plugin entry point appears first, and the paragraph after it names what each part is for and what the host does with it. Evans does the same thing with command output, and shows how one number in the output ties to the next command. Where a result is observed, say it was observed and give the output. Where it comes from the source, say which file or type declaration says so.

Define a term where the reader first meets it, in the clause that uses it. Evans introduces DWARF by saying what it is and where it is stored in the same breath that she needs it. Abramov glosses "the children prop" as "JSX content" in passing. A plugin walkthrough has many such terms (plugin, hook, tool, session, event, context object, whatever the project calls them), and each one can be glossed once, in the sentence that first needs it, and then used by that name only. Keep one word per concept. If the source calls it a hook, it is a hook all the way down.

Keep the line between what was checked and what the project says. Evans's correction about libunwind is the model: what she had claimed, what she was told, who told her it, and the revised statement. In this piece the same separation can be made with plain attributions: "the docs say", "the type declaration shows", "I ran this and got". Willison does it by pointing out that the search tool he built is crude and what a better one would do. Where something about the new plugin API was not tried, or where the project's migration notes and the code disagree, say that in one sentence with the specifics and keep going.

State limits and rough edges as a person who hit them would. Evans reports that the library she used was slow and gives the measured time. Willison reports that the model guessed a query that failed and then fetched the schema. Concrete numbers, names and error text carry these, and no adjectives about difficulty are needed. When the release has a sharp edge, report it that way. Neither enthusiasm about the release nor complaint about it fits this genre, and the passages below contain neither. Give the plain facts about what changed for someone who has to port a plugin.

The explanation of mechanism can run long where the reader needs it, and the prose between snippets can stay short. Sentences like "Problem solved" and "we're done" appear in these passages because a step really did finish. A joke or an exclamation point is available where the author was in fact surprised, as with Evans's "WELL", but this is a reference piece that will be reread with the editor open, and the reader's trust depends on the code being right, so nothing should compete with that. Paragraphs introduce nothing they do not then show and do not end on a summary of themselves.

## Simon Willison, "Large Language Models can run tools in your terminal with LLM 0.26"

Source: https://simonwillison.net/2025/May/27/llm-tools/

> "The syntax here is slightly different: the Datasette plugin is what I’m calling a “toolbox”—a plugin that has multiple tools inside it and can be configured with a constructor.
>
> Specifying --tool as Datasette("https://datasette.io/content") provides the plugin with the URL to the Datasette instance it should use—in this case the content database that powers the Datasette website."

Checked: https://simonwillison.net/2025/May/27/llm-tools/ (raw HTML via curl), retrieved 2026-10-04
He names the new concept, says in the same sentence what it contains and how it is configured, and then says what the argument in the command does. The "I'm calling" marks the term as his own coinage, so the reader knows it is not established vocabulary.

> "A better search tool would have more detailed instructions and would return relevant snippets of the results, not just the headline and first paragraph for each result. This is pretty great for just four lines of Python though!"

Checked: https://simonwillison.net/2025/May/27/llm-tools/ (raw HTML via curl), retrieved 2026-10-04
After a deliberately crude example, he says what is wrong with it and what a real version would do, then says what the crude one still achieves. The author is visible as someone who ran it and judged the result, with the limitation stated as a fact about the code.

> "The model.chain() method is new: it’s similar to model.prompt() but knows how to spot returned tool call requests, execute them and then prompt the model again with the results. A model.chain() could potentially execute dozens of responses on the way to giving you a final answer."

Checked: https://simonwillison.net/2025/May/27/llm-tools/ (raw HTML via curl), retrieved 2026-10-04
A new method is defined by its difference from a method the reader already knows, and then by the consequence that matters when calling it (it can make many requests). The identifiers are written exactly as in the code.

## Julia Evans, "How does gdb work?"

Source: https://jvns.ca/blog/2016/08/10/how-does-gdb-work/

> "What’s that we see? Could it be 0x48a7f0? Yes it is! So!! If we want to find the address of a global variable in our program, all we need to do is look up the name of the variable in the symbol table, and then add that to the start of the range in /proc/whatever/maps, and we’re done!"

Checked: https://jvns.ca/blog/2016/08/10/how-does-gdb-work/ (raw HTML via curl), retrieved 2026-10-04
She has just run two commands and compared two numbers, and here she states the procedure the comparison shows, in terms of the real file and tool names. The enthusiasm is attached to a step that worked.

> "So. The name of the type of ruby_current_thread is rb_thread_struct. It has size 0x3e8 (or 1000 bytes), and it has a bunch of member items. stack_size is one of them, at an offset of 24, and it has type 31. What’s 31? No worries! We can look that up in the DWARF info too!"

Checked: https://jvns.ca/blog/2016/08/10/how-does-gdb-work/ (raw HTML via curl), retrieved 2026-10-04
She reads a block of dump output aloud, field by field, converting hex to decimal as she goes, and anticipates the reader's question ("What's 31?") before answering it from the same dump. The reader can follow it with the dump in view.

> "In an earlier version of this post, I said that gdb unwinds stacktraces using libunwind. It turns out that this isn’t true at all! Someone who’s worked on gdb a lot emailed me to say that they actually spent a ton of time figuring out how to unwind stacktraces so that they can do a better job than libunwind does."

Checked: https://jvns.ca/blog/2016/08/10/how-does-gdb-work/ (raw HTML via curl), retrieved 2026-10-04
She states what she had claimed, that it was wrong, and who corrected her and what they said. The correction stays in the published text where the reader meets it.

## Dan Abramov, "Before You memo()"

Source: https://overreacted.io/before-you-memo/

> "The problem is that whenever color changes inside App, we will re-render <ExpensiveTree /> which we’ve artificially delayed to be very slow. I could put memo() on it and call it a day, but there are many existing articles about it so I won’t spend time on it. I want to show two different solutions."

Checked: https://overreacted.io/before-you-memo/ (raw HTML via curl), retrieved 2026-10-04
This follows a code listing and says in one sentence what in that listing causes the problem. He then says what he will not cover and why, so the reader knows the scope of the piece. The identifiers are quoted from the code on the page.

> "We split the App component in two. The parts that depend on the color, together with the color state variable itself, have moved into ColorPicker. The parts that don’t care about the color stayed in the App component and are passed to ColorPicker as JSX content, also known as the children prop. When the color changes, ColorPicker re-renders. But it still has the same children prop it got from the App last time, so React doesn’t visit that subtree. And as a result, <ExpensiveTree /> doesn’t re-render."

Checked: https://overreacted.io/before-you-memo/ (raw HTML via curl), retrieved 2026-10-04
He has just shown the refactored code and now narrates it in the order the runtime acts: what moved, what stayed, what happens on a state change, what is skipped. Terms are glossed in passing ("also known as the children prop") and then used by one name.

> "This is not a new idea. It’s a natural consequence of React composition model. It’s simple enough that it’s underappreciated, and deserves a bit more love."

Checked: https://overreacted.io/before-you-memo/ (raw HTML via curl), retrieved 2026-10-04
He says plainly that the technique is not his invention and attributes it to how the framework already works. The sentences are short and there is no claim about the technique beyond what the article showed.
