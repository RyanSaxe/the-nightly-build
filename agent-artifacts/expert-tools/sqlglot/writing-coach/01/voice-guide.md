# Voice guide: expert-tools/sqlglot (01)

## How this piece should sound

This is an essay for a machine-learning engineer who already writes SQL and,
when a query needs rewriting, reaches for string manipulation. The register
stays calm and precise, first-person where a first-person observation is honest.
The reader is a peer who will judge SQLGlot by whether the code on the page earns
its keep, so the writing's work is to put that code where they can watch it run
and to be straight about where it stops working.

Let one worked example reach the capability that changes the work: that SQLGlot
turns a query into a syntax tree a program can read, rewrite, and reason about,
where string manipulation only lets you match patterns in text. A tour that
visits the dialect list, then the optimizer, then lineage in turn will dilute
that. Willison proves shot-scraper with the single annotated screenshot he
actually needed; this piece can pick one job, a dialect migration or a lineage
walk or a programmatic rewrite, and let that job carry the argument the way his
screenshot carries his.

Where the example includes a step that did not come cleanly, the Willison
passage about fiddling in the developer console shows the worth of saying so. If
parsing a real query needed a dialect told to it, or a round-trip through the AST
reformatted the SQL or dropped a comment, that can stay in the example instead of
being smoothed away.

State the cost of adoption in the shape Gallant uses in his anti-pitch: name the
concrete situation where SQLGlot is the wrong reach and say what to use instead.
Parser coverage gaps, dialect fidelity that is close without being exact, and how
pure-Python parsing compares against sqlglotrs are limits worth conceding
outright. Evans naming what dnspeep cannot do and pointing at dnssnoop is the
same honesty at the size of one feature; where SQLGlot hands a job back to the
database's own parser or to sqlglotrs, the piece can say so and move on.

Give the tool's size and scope in plain numbers, as Evans gives dnspeep's line
count and Willison gives shot-scraper's: a count of supported dialects, what a
call to the parser hands back, how much code one transformation takes. When a
claim is one the reader would want to check, ground it in something runnable, the
way Evans shows a block of real tcpdump output and then what her tool does with
the same queries.

Whether SQLGlot is maintained well enough to trust is part of what the reader
came for. Report what the repository, the issue history, and the dependents
actually show, and let that reporting stand on its own. A verdict dressed as a
finding would only restate it. The example carries the value; an
install-and-import paragraph placed before anything interesting happens is the
part to cut.

## Simon Willison, "shot-scraper: automated screenshots for documentation, built on Playwright"

Source: https://simonwillison.net/2022/Mar/10/shot-scraper/

> "As software changes over time, screenshots get out-of-date. I don't like the idea of stale screenshots, but I also don't want to have to manually recreate them every time I make the tiniest tweak to the visual appearance of my software."

He states the problem as his own irritation before naming any tool, in two plain
sentences a reader recognizes from their own work. The "I don't like... but I
also don't want to" is a person weighing two things he actually feels, and it
sets up why the tool exists without a word of pitch.

> "I then fiddled around in the Firefox developer console for quite a while, working out the JavaScript needed to trim the page down to the bit I wanted, open the menu and position the arrow."

The worked example is preceded by an admission of how much manual fiddling it
took, which keeps the demonstration honest instead of magical. "fiddled around...
for quite a while" is Willison declining to pretend the result came cleanly, so
the reader learns both what the tool does and what it still leaves to them.

> "Thanks to Playwright, the entire implementation of shot-scraper is currently just 181 lines of Python code—it's all glue code tying together a Click CLI interface with some code that calls Playwright to do the actual work."

A single exact figure, 181 lines, carries the claim that the tool is thin glue
over something else, and he names what the glue ties together rather than calling
it small in the abstract. Crediting Playwright for most of the value is where you
see a writer comfortable saying his tool's worth is largely borrowed.

## Julia Evans, "A tool to spy on your DNS queries: dnspeep"

Source: https://jvns.ca/blog/2021/03/31/dnspeep-tool/

> "Over the last few days I made a little tool called dnspeep that lets you see what DNS queries your computer is making, and what responses it's getting. It's about 250 lines of Rust right now."

The first sentence says exactly what the tool does in the reader's own terms, and
the second gives its size in plain numbers before any argument for it. "about 250
lines of Rust right now" is Evans scoping the thing honestly, small and
unfinished, with nothing inflated and nothing hidden.

> "I think what makes this format the most difficult to deal with (as a human who just wants to look at some DNS traffic) though is that you have to manually match up the requests and responses, and they're not always on adjacent lines. That's the kind of thing computers are good at!"

She locates the exact friction the tool removes, matching request to response by
hand, inside a real example of the old tool's output, so the value is shown and
not asserted. The closing line is light and depends on the specific complaint
before it, and the parenthetical keeps the reader's actual goal in view.

> "One thing this program doesn't do is tell you which process made the DNS query, there's a tool called dnssnoop I found that does that. It uses eBPF and it looks cool but I haven't tried it."

She names something her own tool cannot do and points to the tool that can,
without defensiveness. "it looks cool but I haven't tried it" reports the exact
limit of her knowledge instead of rounding it up, and the reader trusts the rest
of the piece more for it.

## Andrew Gallant, "ripgrep is faster than {grep, ag, git grep, ucg, pt, sift}"

Source: https://blog.burntsushi.net/ripgrep/

> "I'd like to try to convince you why you shouldn't use ripgrep. Often, this is far more revealing than reasons why I think you should use ripgrep."

He gives a labeled section to arguments against his own tool and says plainly why
that is worth doing. The move builds trust because the reader sees the author is
not only selling, and it reads as a practitioner's habit rather than a rhetorical
flourish.

> "You need a portable and ubiquitous tool. While ripgrep works on Windows, macOS and Linux, it is not ubiquitous and it does not conform to any standard such as POSIX. The best tool for this job is good old grep."

The trade-off is stated as a concrete situation, needing a ubiquitous tool, and
then conceded outright, naming the competitor that wins it. "good old grep" hands
the win over without grudging it, and the reader comes away with a real rule for
when not to reach for the tool.

> "Coming up with a good and fair benchmark is hard, and I have assuredly made some mistakes in doing so. In particular, there are so many variables to control for that testing every possible permutation isn't feasible. This means that the benchmarks I'm presenting here are curated, and, given that I am the author of one of the tools in the benchmark, they are therefore also biased."

Before presenting his evidence he states its limits and his own stake in it, in
his own voice. Naming himself as the tool's author and therefore biased is a
person taking responsibility for the framing, and the honesty is specific:
curated, incomplete, and authored by an interested party.
