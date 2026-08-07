# Voice guide: expert-tools/grug-far (01)

Write as an engineer who has read the plugin's source reporting to a peer who
could read it too. The house register already sets the temperature: calm,
precise, argued from first principles. This guide does not relax it. It sharpens
the two moves that decide whether this particular piece works, and leaves
everything else to the standard.

The reader holds the editor and the shell. Assume the mechanics of ripgrep, a
`:s` substitution, `:cdo` over a quickfix list, and shelling out to sed or
ast-grep. Spend no sentence teaching those. Every word buys the reader something
about what this tool does that those do not, and the authority comes from
inspection: press a judgment exactly as far as the code, docs, history, and
issues you actually read support it, and no further. A verdict about maintenance
health rests on the commit and issue record you saw; a verdict about a failure
mode rests on the behavior you reproduced. Confidence tracks evidence, sentence
by sentence.

Two moves carry the piece, and both are licensed below: the single example that
proves the tool's one move, and the plain statement of what that move costs.
When a sentence is neither of those, the house standard already governs it.

## Licenses

form: the worked example, as a code listing or a keystroke-and-buffer sequence
move: the studied writers stage an example at the exact instant the tool acts
      and cut everything before it. Willison's demonstration is three lines and
      its own output is the proof; Gallant drops a pattern's extracted literals
      into the middle of an argument to show an optimization exists, not to
      teach regex. Deploy the example at the pivot this tool turns on: the search
      results standing open as editable text, the edit made in that buffer, the
      write-back landing across files. Position it so the reader watches the
      state change that is the entire reason to reach for the tool.
bar:  a single listing shows the one move and lets the reader see what differs
      between before and after it. Any line that would read the same for a tool
      without that move (plugin-manager boilerplate, install steps, unrelated
      keymaps, setup that only gets the reader to the starting frame) is cut. If
      the listing reads as steps to reproduce rather than as evidence of the
      move, it has failed and is rebuilt or removed.

form: the plain cost, and the line drawn against a neighboring tool
move: the writers name a weakness as a flat declarative and pin it to the exact
      condition that triggers it. Gallant keeps an explicit anti-pitch and
      concedes where his tool is not portable; Hashimoto writes that the reader
      should not expect a polished experience and adds no cushion; Willison calls
      his own implementation a hack and then states, flat, that it works anyway.
      Each credits what the alternative genuinely does better in one clause
      before pressing his own case, which is what makes the case land. Concede in
      one clause what `:s`, `:cdo`, quickfix replace, or a direct ast-grep run
      does better, then say precisely where this tool's model breaks: which
      result-set sizes, which required or optional dependency, which unsaved or
      out-of-sync buffer state.
bar:  a cost sentence names what fails and the specific condition under which it
      fails. A qualifier that retracts the concession as it makes it ("though
      somewhat narrower", "still mostly fine", "a little slower but") fails the
      line. The concession and the bound around it are both stated and both left
      standing; the reader can tell from the sentence when the cost is paid and
      when it is not.

## Andrew Gallant (BurntSushi), "ripgrep is faster than {grep, ag, git grep, ucg, pt, sift}"
Source: https://burntsushi.net/ripgrep/
Craft:
- cadence: short declaratives set against longer technical passages; a claim
  arrives, then the mechanism under it, then the measurement.
- argument: establishes what each tool does differently before measuring
  anything, so the benchmarks cannot be dismissed as rigged; advances from
  simple patterns to hard ones the way a real user's questions would.
- evidence: numbers appear after the conceptual frame, never as the opening
  move; a code fragment is shown to prove a specific optimization exists, not to
  teach its syntax.
- stance: presses hard but fixes the scope of each win exactly ("faster for
  single files and huge directories"), and credits rivals' strengths in plain
  words.
- notice: reads other projects' source and reports the byte-level choice they
  make that no user would see from the outside.
- diction: plain, with each technical term given a short parenthetical gloss;
  assumes intelligence, not prior knowledge of the internals.
- reader: treated as an intelligent skeptic and a co-investigator, not an
  audience to be sold.
- the important move: a dedicated anti-pitch that states where the tool loses,
  which is precisely what earns belief in every claim that it wins.

## Simon Willison, "Large Language Models can run tools in your terminal with LLM 0.26"
Source: https://simonwillison.net/2025/May/27/llm-tools/
Craft:
- cadence: short and punchy against longer explanatory sentences; opens on the
  significance of the change with no throat-clearing.
- argument: shows value first and mechanism second; each demonstration escalates
  from the one before it rather than restarting.
- evidence: the command and the output it produces are themselves the proof;
  three lines, running, visible result.
- stance: confident and self-auditing at once ("this demo has been weak so
  far"); pragmatic about what is good enough.
- notice: catches the moment his own implementation is a hack and says so before
  a reader can.
- diction: conversational and precise together; functional verbs, no promotion.
- reader: a collaborator whose objection he voices and answers inside the prose.
- the important move: concede the crudeness plainly, then state the
  countervailing fact flat ("it totally works though") -- honesty that does not
  retreat from the concession it just made.

## Mitchell Hashimoto, "Libghostty is Coming"
Source: https://mitchellh.com/writing/libghostty-is-coming
Craft:
- cadence: short declaratives building momentum, a long technical passage
  relieved by a blunt short close.
- argument: moves from landscape to necessity to implementation; grounds the
  need in observable repetition ("hundreds of programs implement terminal
  emulation") so the solution reads as inevitable rather than pitched.
- evidence: a concrete catalog does the work an adjective would otherwise be
  asked to do.
- stance: calm; the structure persuades, not the intensity; claims are pressed
  only as far as the piece has built them.
- notice: names the ordinary complexity others wave past ("appears simple on the
  surface but is riddled with edge cases").
- diction: unadorned and functional; promotional words are simply absent.
- reader: a partner in an unfinished design, invited to test it and report back.
- the important move: a flat admission of immaturity ("don't expect a polished,
  stable experience") that inverts the sales pitch and buys credit for
  everything else on the page.
