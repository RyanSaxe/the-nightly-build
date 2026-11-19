# editor brief: reinforcement-learning/specification-gaming (03)

Inputs:
- every input of editor/01/review-brief.md, plus your editor/01 and editor/02 reviews
- The second reader check report below (new reader, same inputs as the first: rendered page
  with collapsed sections closed, the five linked lessons, press/editorial.md)
Output: editor/03/editorial-review.md beside this brief
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/library/reinforcement-learning/specification-gaming.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

This is the second and last reader check. Per the lesson template, answer it by cutting or
correcting text only. You may rerun the lesson's code but start no new experiments, and cut any
explanation the existing runs cannot support. Place (a) is a correctness question, not a
clarity one: verify with value iteration (race.py as printed, or a throwaway check) what the
whole greedy policy does at low discounts such as 0.3 and 0.5, cell by cell, and make the
section title, the derivation's statement, Fig. 1/Fig. 2 captions and the takeaway say exactly
what is true (from cell 2, or for the start state, as the facts show). Record the action on
each place. Re-stamp and re-prove; recheck the page at 390 and 1280 px in both themes if
anything visual changed.

## Second reader check report (verbatim)

READER REPORT: "Looping through a checkpoint worth 1 beats a finish worth 10 at a discount of 0.99"

1. MAIN IDEA (in my words)
An optimal policy maximizes the return of the reward as written, not the task the designer meant. On an eight-cell race, a checkpoint that pays every time it is crossed makes a back-and-forth loop worth γr/(1−γ²). Two geometric sums show the loop beats the finish (γ⁴F from cell 2) unless γ is inside a window, about 0.514 to 0.937 for r=1, F=10. At γ=0.99, value iteration's exact optimum loops forever, and Q-learning learns the same loop. So the agent is working correctly by its return and failing by the task. You need a separate task measure to see the gaming. Paying the checkpoint only once removes the loop.

2. PLACES I GOT LOST (worst first)

a) The window is for one cell, but the takeaway states it for the whole policy, and the lesson never says why cell 2 decides the outcome.
- "Start in cell 2, just past the checkpoint." No reason is given for choosing cell 2. I worked out on my own that an agent from cell 0 must pass cell 2, so cell 2's move decides whether it finishes. The lesson should say so.
- "As γ approaches 0, the factor γ^(D−2) goes to 0 instead, so the loop wins there too." This is only true from cell 2. From cell 6, a myopic agent grabs the 10 at once. At γ=0.3, cell 2 would point back while cell 6 points forward. That doesn't match how Fig. 1 trains my eye (all of cells 2–6 flip together).
- The takeaway then says "finishing is optimal only for discounts between 0.514 and 0.937" without "from cell 2". I could not tell whether "the optimal policy" means the whole arrow row or the start-state outcome. The section title "The finish wins inside a window of discounts" has the same ambiguity.

b) A forward reference to the "pays once" flag comes before I knew why it exists.
- "A state is the cell plus 8 times a flag that records whether a checkpoint that pays only once has paid. The flag stays 0 until the last row of learn.py tests that checkpoint."
- At this point I don't know what learn.py is, and I don't know a once-paying checkpoint will appear. The explanation for the doubled state space only arrives three sections later, in the Race(once=True) paragraph. On first read I couldn't say why this sentence was there.

c) Reducing the comparison to "loop vs finish" is compressed, and the case list is incomplete.
- "Policy iteration searches only policies that pick one move per cell and still ends at an optimal one, so comparing those policies is enough." I can rebuild this from the earlier lesson (policy iteration halts at a policy that cannot be bettered). But the step "therefore a deterministic policy is optimal" is left to me.
- "So from cell 2 a policy either loops, finishes, or cycles in cells 2 to 6 without crossing anything, which earns 0." This misses the case where cell 2 moves back and cell 1 also moves back: the agent sits in cell 0 or cycles 0–1, which also earns 0. That's harmless, but the "either…or" made me stop and check whether a case was missing.

d) The constant step size is justified by an assertion, and a later result partly contradicts it.
- "That condition is there to average out noise in the targets, and here the targets have none… So a constant step size of 0.1 lets the estimates settle."
- The earlier lessons state the finite-sum-of-squares condition but never say what it is for. No earlier result covers a constant step size, so "lets the estimates settle" rests only on the run.
- The third row then reports an error of 0.116 that has not settled, on a rarely visited pair. That fits "only random moves have updated since," but it sits awkwardly next to "lets the estimates settle."

e) "a move the greedy policy stopped choosing within a few hundred episodes". "Stopped choosing" implies the greedy policy once chose to move back in cell 0 after the payment. The reason (ties at 0 broken toward index 0 = BACK) is never stated, and learn.py is collapsed. I couldn't see why it ever chose that move.

f) Minor: "In both rows cell 1 is worth more than cells 0 and 2, because its forward move collects the checkpoint." I can see it is true, but not what it is for. At γ=0.9, cell 1 is not the interesting cell, since cells 3–6 are worth more. If it is there to explain the dip at cell 2, it should say so.

3. SECTIONS I COULD SKIP AND STILL EXPLAIN THE MAIN IDEA
- "A boat in CoastRunners circled through targets that kept reappearing". This is the real-world anchor, already summarized in "Why this matters". The DeepMind/OpenAI sourcing caveat in it doesn't feed the argument.
- The window.py paragraph and its output. It only confirms that the formula matches value iteration, which Fig. 2's caption already claims.
- The step-size paragraph in the Q-learning section (the convergence-proof aside).
- The race.py code listing itself. Fig. 1 and the printed output carry the result.

4. RESULTS REPORTED WITHOUT SAYING WHAT THEY MEAN
- The window.py output line "value iteration finishes from cell 2 at 42 of 99 discounts". The text explains the agreement but not the 42. I could infer it is just the grid points inside 0.514–0.937.
- "largest ratio 1.86 at gamma 0.775". This is explained in the prose (peak of the curve), so it's fine. But the text never states that 1.86 > 1 is what makes a window exist at all. That only becomes clear from the checkpoint-2 contrast.
- The learn.py header "eps 0.5, step size 0.1, 2000 episodes of at most 100 moves". The 100-move cap is what makes the looping agent score exactly 50. The text gives the 50 but doesn't tie it back to the cap. The 50 is set by the time limit, not by anything about the race.
- In the CoastRunners section: "DeepMind's account says the targets changed the optimal policy, but OpenAI's post reports scores and computes no optimal policy." The lesson reports this difference between sources but only half says what follows from it (that the race fills the gap). I had to infer that this is the point.
