# Voice guide: feature/top500-ageing-installed-base (01)

## How this piece should sound

This is a short data feature for engineers who build ML systems, written by someone who parsed the list files themselves and is reporting what the files show. The register is the one Dan Luu and Brendan Gregg use with a technical reader: first-hand, plain, specific, and confident where the measurement supports it. Luu says what he did ("carried around a high-speed camera and measured") before he says what he found. Where this piece rests on the paper's own computation across the xlsx files, it can say so in the same plain way, and say how a field like first appearance was defined before leaning on it.

Treat the reader as someone who knows what HPL, Rmax, a GPU generation and a cluster are, and who has not looked at how the list's population changes from edition to edition. Gregg takes a number the reader already trusts (%CPU, an IPC of 0.78) and walks it one step at a time to what it really means. An edition count or a share of systems five years old may need the same walk: what the figure counts, then what it does and does not tell an engineer about where new compute is going.

Luu's tables and Ritchie's charts are read aloud in the prose: he tells the reader which column should darken if the hypothesis held, and then reports that it does not. With 2–4 sections each built around a chart, the prose around a chart can do that work, saying what the reader should look for and whether it is there, rather than restating every value.

Ritchie keeps a contrary reading in view and gives it its due. Where a rival explanation, such as a pause before the next GPU generation, has a case, the piece may state it in its holder's terms and then test it against the series, at the same even temperature as the rest. Where the series does not settle something, the piece can say so in a short flat sentence, as Ritchie does ("Of course, we don't know."), and move on. Neither writer raises their voice; a strong finding stays in the same plain register as a weak one.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower than the computers I used as a kid. As a rule, I don't trust this kind of feeling because human perception has been shown to be unreliable in empirical studies, so I carried around a high-speed camera and measured the response latency of devices I've run into in the past few months."

Checked: https://danluu.com/input-lag/ (raw HTML via curl), retrieved 2026-11-20
The opening states a suspicion, says why he will not trust it, and names the instrument he used instead, in one plain run of two sentences. Luu is visible in the admission of the "nagging feeling" and in the distrust he applies to his own impression.

> "In the year column, the background gets darker and purple-er as devices get older. If older devices were slower, we'd see the year column get darker as we read down the chart. The next two columns show the clock speed and number of transistors in the processor. Smaller numbers are darker and blue-er. As above, if slower clocked and smaller chips correlated with longer latency, the columns would get darker as we go down the table, but it, if anything, seems to be the other way around."

Checked: https://danluu.com/input-lag/ (raw HTML via curl), retrieved 2026-11-20
He tells the reader what the table would look like if the obvious hypothesis were true, then reports that it does not look like that. The coined "purple-er" and the hedge "if anything" are his; the passage teaches reading the visual rather than repeating its numbers.

> "It's a bit absurd that a modern gaming machine running at 4,000x the speed of an apple 2 , with a CPU that has 500,000x as many transistors (with a GPU that has 2,000,000x as many transistors) can maybe manage the same latency as an apple 2 in very carefully coded applications if we have a monitor with nearly 3x the refresh rate."

Checked: https://danluu.com/input-lag/ (raw HTML via curl), retrieved 2026-11-20
The conclusion stacks exact ratios against one comparison the reader can hold, and the verdict is a mild "a bit absurd" rather than a superlative. The qualifiers "maybe" and "very carefully coded" keep the claim to what he measured.

## Brendan Gregg, "CPU Utilization is Wrong"

Source: https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html

> "The metric we call CPU utilization is really "non-idle time": the time the CPU was not running the idle thread. Your operating system kernel (whatever it is) usually tracks this during context switch. If a non-idle thread begins running, then stops 100 milliseconds later, the kernel considers that CPU utilized that entire time."

Checked: https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html (raw HTML via curl), retrieved 2026-11-20
He defines what a familiar metric actually counts, then makes it concrete with one 100-millisecond instance. The parenthetical "(whatever it is)" is Gregg talking directly to a mixed-platform reader.

> "The key metric here is instructions per cycle ( insns per cycle : IPC), which shows on average how many instructions we were completed for each CPU clock cycle. The higher, the better (a simplification). The above example of 0.78 sounds not bad (78% busy?) until you realize that this processor's top speed is an IPC of 4.0."

Checked: https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html (raw HTML via curl), retrieved 2026-11-20
A number from real output is read the way a reader would first read it, and then set against the ceiling that changes its meaning. He flags his own simplification in passing, which tells the reader exactly how far to trust the rule of thumb.

> "This has been getting worse. For a long time processor manufacturers were scaling their clockspeed quicker than DRAM was scaling its access latency (the "CPU DRAM gap"). That levelled out around 2005 with 3 GHz processors, and since then processors have scaled using more cores and hyperthreads, plus multi-socket configurations, all putting more demand on the memory subsystem."

Checked: https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html (raw HTML via curl), retrieved 2026-11-20
A four-word claim of a trend, followed by the history that produced it, dated to a year and a clock speed. The hardware vocabulary is left exactly as a practitioner says it.

## Hannah Ritchie, "What's the impact of artificial intelligence on energy demand?"

Source: https://www.sustainabilitybynumbers.com/p/ai-energy-demand

> "How much energy could AI use in the future? Of course, we don't know. And I'd be very sceptical of any projections more than a decade into the future. Even five years is starting to get highly speculative."

Checked: https://www.sustainabilitybynumbers.com/p/ai-energy-demand (raw HTML via curl), retrieved 2026-11-20
The section opens on its question and answers with the limit of what is known before any projection appears. Ritchie's own judgment is stated in the first person and graded by horizon.

> "Microsoft has made a deal to reopen Three Mile Island. An entire nuclear power plant to power one company's operations? That seems big. At least until you run the numbers."

Checked: https://www.sustainabilitybynumbers.com/p/ai-energy-demand (raw HTML via curl), retrieved 2026-11-20
She voices the reader's likely first reaction as a short question and grants it ("That seems big") before taking it to the arithmetic. The sentences are short and conversational, and the reaction belongs to a person, not to an abstract "some".

> "I don't want to paint the picture that AI energy demand is a "nothingburger" because we don't know how these trends are going to evolve. Having more transparency from tech companies on current energy demands — and how they're changing over time — would allow researchers to keep up."

Checked: https://www.sustainabilitybynumbers.com/p/ai-energy-demand (raw HTML via curl), retrieved 2026-11-20
Having argued one side, she marks where her argument stops and names the missing data that would settle it. The colloquial "nothingburger" in quotation marks shows her distance from the dismissive reading of her own case.
