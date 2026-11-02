# Voice guide: reinforcement-learning/learning-values-from-samples (01)

## How this piece should sound

The register is a teacher who has the code open next to the derivation and moves between them. The reader holds CS or math degrees and has shipped ML systems, so nothing is explained twice and nothing is hurried. The reader is new to RL, so every RL term is defined where the lesson first needs it, in the words a practitioner would use. Karpathy's passage on the chain rule (second Karpathy passage below) shows the level: it names the quantities by their real symbols and says what each step is for in one plain sentence.

Set up a derivation by saying what is already known and what is being asked, the way Karpathy does when he lists what the gate case gives and then what the chain rule combines. Weng does it with the forward process: she states the setup in full symbols, names the property she is about to use, defines the new symbols in the same sentence, and puts the justification for a skipped step directly after the equation. For the incremental mean, the TD error, and the return, define each symbol where it enters, state what the step needs, and justify any step that is not obvious beside it. Math and code are at full difficulty, and the prose around them can stay short.

When a quantity is first introduced, let the reader meet a version small enough to hold. Colah describes the cell state by what it does to information moving along it, then walks the gates one at a time, each with what it decides. A backup, an update, or a target on the 4x4 grid can be introduced the same way: what comes in, what the step does to it, what goes out, with a cell's actual numbers. Karpathy opens a section by asking the question a sceptical reader would ask and then trying the obvious thing in code before the better method. Where the obvious approach is a real one, such as a plain average of returns, the lesson may do the same, and the contrast with the better estimator then comes from a run and not from assertion.

A person is visible in these passages through small, specific choices: a stated preference about how much math is needed, a plain admission that a sentence is dense, a sentence that says what the step is for. Allow that where the material calls for it. The press standard rules out performed carefulness, lecturing openers, and lines built to be quoted, and none of the three passages below needs them. Direct address belongs to the two bookend cards only. In the body, keep the second person out and let the grid, the estimates and the errors carry the subject.

Report only what the runs produced. The exemplars show writers who put code next to a claim; here, the number on the page is the number the run printed, with the exact solve named as the score and not as part of any estimator.

## Andrej Karpathy, "Hacker's guide to Neural Networks"

Source: https://karpathy.github.io/neuralnets/

> "Okay. So wait, we have a circuit, we have some inputs and we just want to tweak them slightly to increase the output value? Why is this hard? We can easily “forward” the circuit to compute the output for any given x and y. So isn’t this trivial? Why don’t we tweak x and y randomly and keep track of the tweak that works best:"

Checked: https://karpathy.github.io/neuralnets/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
The section asks the reader's likely objection in the reader's own terms, then runs the naive approach in code that follows directly. The person is visible in the "Okay. So wait" start, which reads as someone thinking alongside the reader.

> "You may have seen other people who teach Neural Networks derive the gradient in huge and, frankly, scary and confusing mathematical equations (if you’re not well-versed in maths). But it’s unnecessary. I’ve written plenty of Neural Nets code and I rarely have to do mathematical derivation longer than two lines, and 95% of the time it can be done without writing anything at all."

Checked: https://karpathy.github.io/neuralnets/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
He states what the math requires and gives his own working experience as the evidence. The first person is used here for a claim the reader can weigh. This blog-post stance is his; a lesson with full derivations would not copy the dismissal of math, only the habit of saying how much of it a step needs.

> "We know how to compute the gradient of q with respect to x and y (that’s a single gate case with + as the gate). And we know how to compute the gradient of our final output with respect to q. The chain rule tells us how to combine these to get the gradient of the final output with respect to x and y, which is what we’re ultimately interested in."

Checked: https://karpathy.github.io/neuralnets/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
Two known pieces are listed, then the rule that joins them, then what the join produces. The symbols are the ones the code uses, so the sentence maps straight onto the lines below it.

## Lilian Weng, "What are Diffusion Models?"

Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

> "Given a data point sampled from a real data distribution $\mathbf{x}_0 \sim q(\mathbf{x})$, let us define a forward diffusion process in which we add small amount of Gaussian noise to the sample in $T$ steps, producing a sequence of noisy samples $\mathbf{x}_1, \dots, \mathbf{x}_T$. The step sizes are controlled by a variance schedule $\{\beta_t \in (0, 1)\}_{t=1}^T$."

Checked: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (raw HTML fetched with curl, tags stripped; math appears as the page's TeX source), retrieved 2026-11-02
A definition in one pass: the input, the process, the sequence it produces, and the parameter that controls it, each with its symbol and its range. A reader with a math degree can write the next equation from it.

> "A nice property of the above process is that we can sample $\mathbf{x}_t$ at any arbitrary time step $t$ in a closed form using reparameterization trick. Let $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$:"

Checked: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
She says what the derivation that follows will buy before she starts it, names the technique by its field name, and defines the new symbols in the same breath. The colon hands off to the equation.

> "Recall that when we merge two Gaussians with different variance, $\mathcal{N}(\mathbf{0}, \sigma_1^2\mathbf{I})$ and $\mathcal{N}(\mathbf{0}, \sigma_2^2\mathbf{I})$, the new distribution is $\mathcal{N}(\mathbf{0}, (\sigma_1^2 + \sigma_2^2)\mathbf{I})$. Here the merged standard deviation is $\sqrt{(1 - \alpha_t) + \alpha_t (1-\alpha_{t-1})} = \sqrt{1 - \alpha_t\alpha_{t-1}}$."

Checked: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
A footnote that justifies the one step the main derivation skipped, by stating the fact used and then plugging in this derivation's numbers. The justification sits beside the line that needs it.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "The key to LSTMs is the cell state, the horizontal line running through the top of the diagram. The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
The key object is pointed at in the figure, then described by what it does, with one analogy used and then dropped for plain statements. Sentences are short and each adds a property.

> "The first step in our LSTM is to decide what information we’re going to throw away from the cell state. This decision is made by a sigmoid layer called the “forget gate layer.”"

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl, tags stripped), retrieved 2026-11-02
Each step of the walkthrough opens by saying what the step decides, and only then names the component that does it. The term enters when it is needed, with its job already stated.

> "It’s now time to update the old cell state, \(C_{t-1}\), into the new cell state \(C_t\). The previous steps already decided what to do, we just need to actually do it."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl, tags stripped; math appears as the page's TeX source), retrieved 2026-11-02
The step is placed relative to the earlier ones, so the reader knows what has been settled and what remains. The plain second sentence is the author talking the reader through the order of operations.
