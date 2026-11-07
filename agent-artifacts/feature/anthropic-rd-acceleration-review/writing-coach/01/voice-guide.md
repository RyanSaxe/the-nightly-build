# Voice guide: feature/anthropic-rd-acceleration-review (01)

## How this piece should sound

This is a feature for readers who have trained and shipped models and who know what a benchmark, an interval and a threshold are. It reads as a measurement person checking a number in public: calm, exact, and willing to say plainly where a figure lands against the 2x line. Hold the register Narayanan and Kapoor hold when they quote OpenAI's contamination method word for word and only then say what it misses. Anthropic's report, the Responsible Scaling Policy and METR's review are documents with exact wording, and the reader is best served by seeing that wording before any judgment about it.

The piece's work is arithmetic about definitions. Luu's Armstrong passage shows what that looks like in prose: he names the scoring scale, the aggregation rule and the resulting fraction, and shows how a different reasonable rule gives a different answer. Where the acceleration estimates differ because one counts research progress and another counts a speed-up of engineering work, or because the windows differ, say which definition and which window produced each number, in the same sentence as the number. Use one term for each quantity ("acceleration", "early-warning threshold", "Full Substitution") and keep it; a synonym here reads as a second measurement.

Steinhardt states his verdicts as findings, gives the figure beside the forecast it beat, and puts his own wrong prediction on the page. The material may call for the same plainness about what the estimates do and do not settle: where an estimate is private, redacted or reported only through METR, say so once and attribute it, and where the evidence does not decide whether the threshold is crossed, say that as a fact about the evidence. Do not perform caution around it.

Five minutes and a few visuals is the budget. Each prose stretch tells the reader how to read the figure beside it and what follows, the way Steinhardt's "here are the actual results" list does, and then stops. Treat Anthropic's case with the same exactness as METR's, in Anthropic's words, before setting METR's reading beside it.

## Jacob Steinhardt, "AI Forecasting: One Year In"

Source: https://bounded-regret.ghost.io/ai-forecasting-one-year-in/

> "Here are the actual results, as of today:
> MATH: 50.3% (vs. 12.7% predicted)
> MMLU: 67.5% (vs. 57.1% predicted)
> Adversarial CIFAR-10: 66.6% (vs. 70.4% predicted)
> Something Something v2: 75.3% (vs. 73.0% predicted)
> MATH and MMLU progressed much faster than predicted. Something Something v2 progressed somewhat faster than predicted. In contrast, Adversarial CIFAR-10 progressed somewhat slower than predicted."

Checked: https://bounded-regret.ghost.io/ai-forecasting-one-year-in/ (raw HTML via curl), retrieved 2026-11-07
Every measured value sits next to the value it is being judged against, and the prose after the list grades each one with a calibrated adverb ("much", "somewhat") that matches the gap. He is visible in the choice to keep the one benchmark that went the other way in the same list.

> "To assess forecast accuracy, we need to look not just at the point estimate, but at the forecasters' actual probability distribution. Even though 68% on MMLU seems far off from 57%, perhaps it was well within the credible interval of the forecasts. However, that turns out not to be the case, for either MATH or MMLU"

Checked: https://bounded-regret.ghost.io/ai-forecasting-one-year-in/ (raw HTML via curl), retrieved 2026-11-07
He raises the strongest objection to his own reading, that a point estimate can look wrong while sitting inside its interval, and answers it with the data. The reader is treated as someone who would think of that objection.

> "So, while I didn't register a specific prediction, I clearly thought the forecasts on MATH were aggressive in terms of how much progress they predicted, whereas it turned out they weren't aggressive enough."

Checked: https://bounded-regret.ghost.io/ai-forecasting-one-year-in/ (raw HTML via curl), retrieved 2026-11-07
The writer reports his own error in one plain sentence, with the qualification about what he did and did not preregister stated first. The candour comes from the record he quotes, not from an announcement of honesty.

## Dan Luu, "Futurist prediction methods and accuracy"

Source: https://danluu.com/futurist-predictions/

> "I checked the accuracy rate of the wikipedia list Diamandis cited myself (using archive.org to get the list from when his article was published) and found a somewhat lower accuracy of 7%."

Checked: https://danluu.com/futurist-predictions/ (raw HTML via curl), retrieved 2026-11-07
The sentence says what he checked, which version of the source he used and how he got it, then gives the result. "Somewhat lower" set against a claimed 86% is his dry understatement; the figure does the work.

> "Karnofsky then compares the number of true + weakly true to false + weakly false, which is one level of rounding up to get an optimistic result; another way to look at it is that any level other than "true" is false when read as written."

Checked: https://danluu.com/futurist-predictions/ (raw HTML via curl), retrieved 2026-11-07
He names the exact aggregation rule someone used and shows that a second, equally literal rule gives a different answer. The person is visible in the refusal to accept a headline number without opening the scoring.

> "Although Armstrong doesn't note this in the post, if you look at the data, you'll see that the third "most true" prediction had a mean score of 1.45 and the fourth had a mean score of 1.6, i.e., if you round to the nearest prediction score, only 3 out of 105 predictions score "true" and 32 are >= 4.5 and score "false"."

Checked: https://danluu.com/futurist-predictions/ (raw HTML via curl), retrieved 2026-11-07
He goes from the summary to the underlying data and reports counts with their denominators. The long sentence holds because each clause adds one number in order.

## Arvind Narayanan and Sayash Kapoor, "GPT-4 and professional benchmarks: the wrong answer to the wrong question"

Source: https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks

> "To benchmark GPT-4's coding ability, OpenAI evaluated it on problems from Codeforces, a website that hosts coding competitions. Surprisingly, Horace He pointed out that GPT-4 solved 10/10 pre-2021 problems and 0/10 recent problems in the easy category. The training data cutoff for GPT-4 is September 2021."

Checked: https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks (raw HTML via curl), retrieved 2026-11-07
Three short sentences: what was measured, who found the anomaly and the counts, and the one date that explains it. They credit the person who found it by name and let the reader draw the inference before they state it.

> "This is a brittle method. If a test problem were present in the training set with names and numbers changed, it wouldn't be detected. Less flaky methods are readily available, such as embedding distances.
> If OpenAI were to use a distance-based method, how similar is too similar? There is no objective answer to this question."

Checked: https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks (raw HTML via curl), retrieved 2026-11-07
This follows a verbatim quotation of the lab's own method, so the judgment comes after the reader has seen the text it judges. The question is answered in the next sentence, and the answer concedes a limit on their own critique.

> "To be clear, we're not saying that Copilot is useless, just that metrics are meaningless without a qualitative understanding of how professionals use AI."

Checked: https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks (raw HTML via curl), retrieved 2026-11-07
They mark the boundary of their claim against a reading a practitioner might reasonably make. The authors are visible as people who expect to be argued with by engineers and want to be argued with about the right thing.

## Questions for the orchestrator

- None blocking. Provisional choice: the Luu piece discusses exponential-growth predictions, so I quoted only its passages about checking and aggregating scores, not its framing of accelerating growth.
