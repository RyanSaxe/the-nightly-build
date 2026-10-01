# Voice guide

## How this piece should sound

Write for readers who know operating systems and APIs but may not know OpenShell. Keep the register direct and technically exact. Name the actor at each boundary: the agent chooses an action, a local control mediates it, a remote service receives or rejects it. When describing the task trace, let the configuration and implementation carry the detail; label an illustrative path as illustrative, not as a test result.

Use Brendan Gregg's habit of explaining a system at the level where it acts, then showing a concrete trace. Use Dan Luu's attention to what evidence does and does not establish. Use Julia Evans's plain explanations and her willingness to identify a useful omission. These are separate tools, not voices to imitate. The walkthrough may call for comparing a documented component with its implementation, and for naming precisely what the sources leave untested. Keep vendor descriptions, observed deployments, and security conclusions visibly distinct.

## Brendan Gregg, “strace Wow Much Syscall”

Source: https://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html

> “strace is the system call tracer for Linux.”

Checked: https://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html, retrieved 2026-10-01. The definition is short and pins the explanation to a specific interface. Gregg’s next move is to describe what the tracer does to a target process; the passage shows how a system label can quickly become an observable operation.

> “The output starts by showing program initialization:”

Checked: https://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html, retrieved 2026-10-01. Gregg introduces a trace by telling readers what they are looking at before interpreting individual calls. His accompanying `ls` example connects raw events to a familiar command, making the output inspectable instead of treating it as a black box.

## Dan Luu, “What to learn”

Source: https://danluu.com/learn-what/

> “To say that someone should look for those things is so vague that's it's nearly useless”

Checked: https://danluu.com/learn-what/, retrieved 2026-10-01. Luu tests abstract advice by asking what information it actually gives a reader. The sentence is useful here because claims about “security” or “isolation” need the specific mechanism and boundary that make them meaningful.

> “I find it totally plausible that Forth (or Lisp or Haskell or any other tool or technique) does work very well for some particular people”

Checked: https://danluu.com/learn-what/, retrieved 2026-10-01. Luu grants the narrower possibility before questioning whether an experience generalizes. That measured distinction suits a piece weighing an integration or vendor demonstration: a real example can show use without proving broad adoption or a general guarantee.

## Julia Evans, “New zine: How DNS Works!”

Source: https://jvns.ca/blog/2022/04/26/new-zine--how-dns-works-/

> “DNS has a really cool decentralized design!”

Checked: https://jvns.ca/blog/2022/04/26/new-zine--how-dns-works-/, retrieved 2026-10-01. Evans states the design property in ordinary language, then explains what it lets a domain owner control. Her enthusiasm is tied to an actual property and consequence, not generic praise.

> “The main thing that isn’t in the zine is DNS security”

Checked: https://jvns.ca/blog/2022/04/26/new-zine--how-dns-works-/, retrieved 2026-10-01. Evans names the boundary of her explanation and gives the reason she left that material out. That is a useful model for marking which OpenShell controls, platform components, or threat cases the available implementation evidence does not cover.
