# Draft handoff: expert-tools/verifiers-rl-environments (writer 01)

## Original work

The article sets out each route by which a point-in-time payrolls nowcasting task can hand the agent its answer. For each one it names the verifiers 0.4.0 setting or the environment design that closes it, with an executed instance where the record has one. It then sets the PAYEMS revision size (97.7k) against the naive forecast error (104.3k) and uses the comparison to choose the scoring vintage and to argue about group size and the reward's shape.

## Proof

`nb stamp`: words 2981, sources 22, reading 13 min.
`nb check ... --series expert-tools --repo /home/user/the-nightly-build` with links checked: BLOCK 0, WARN 0, PUBLISHABLE.

Owner punctuation rule: the rendered text, title and nb-meta contain zero em-dashes and zero semicolons. A raw grep of the file finds 4 semicolons, and all of them are inside the template's Google Fonts stylesheet URL in `<head>`, which is not rendered text. The file has no HTML entities, so code arrows are written as a literal `->`.

Every code-listing line was checked by script and appears verbatim in the nowcast_alfred package or in eval.toml. The captions say what each excerpt leaves out.

## Things the editor should know

- The article is 19 words under the 3000-word cap. Any addition needs a matching cut.
- Model names: no writer-model id appears beyond meta `"model": "claude"`. DeepSeek-R1 and R1-Zero are named because the commission chose them as the warm-start counter-case. No Qwen or vf-eval default model id appears.
- Batch size counts rollouts. This is inferred from the Wordle README (32 x 16 rollouts = batch 512). The "8 tasks per step, 800 over 100 steps" arithmetic depends on it. The 100-step run and the ten-minute box are labelled as illustration and assumption.
- Reward-shape judgment: the claim that a clipped, scale-normalized gain ties fewer groups than a threshold would is labelled as a design judgment that Prime does not state. The warm-start recommendation is labelled as a judgment for nowcast_alfred.
- Cut for length: the Philadelphia Fed RTDSM source, the recipes page, and the Hub page's dead migration-guide link. vf-init is mentioned only as removed after 0.4.0, with no listing. The taskset view methods (include, exclude, shuffle and so on) and INFINITE were also cut.
- No chart and no source assets. The PAYEMS noise figures are in a stat strip next to the prose that cites them.

## Open questions

None blocking.
