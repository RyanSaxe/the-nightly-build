# Voice guide: Reinforcement Learning

## How this series should sound

Lessons in this course sound like one person explaining reinforcement learning to a colleague who
reads math and code easily and hasn't met the subject. The writer says what a step is for before
taking it. The writer can make small personal remarks, such as admitting that the hardest equation
in a lesson looks intimidating and then saying what to look at first, or that a result looked wrong
at first.

Olah's LSTM essay is the closest model for the course. His sentences average about 16 words. Each
passage below has a note on what to take from it. Copy what each writer does, and never copy their
words.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don't throw everything away and start thinking from scratch again. Your thoughts have persistence."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML), retrieved 2026-11-02
Olah opens with the reader's own experience, in short sentences with no technical words. His next paragraph says ordinary networks can't do that, so the reader understands the problem before seeing a network. A lesson's first case can start in a similar way, by showing something the course's agent can't do yet.

> "Don't worry about the details of what's going on. We'll walk through the LSTM diagram step by step later. For now, let's just try to get comfortable with the notation we'll be using."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML), retrieved 2026-11-02
He has just shown a complicated diagram. He tells the reader to ignore the details for now and learn the notation. The same help is useful when a backup diagram, a search tree, or a training loop first appears.

> "The first step in our LSTM is to decide what information we're going to throw away from the cell state. This decision is made by a sigmoid layer called the "forget gate layer.""

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML), retrieved 2026-11-02
The first sentence says what the step decides, and the second names the part that decides it. The reader already knows what the forget gate does when its name appears. Each later step follows the same order and shows the same diagram with a different part marked. Introduce a return, a target, or an update the same way, using the numbers from one move.

## Andrej Karpathy, "Hacker's guide to Neural Networks"

Source: https://karpathy.github.io/neuralnets/

> "Okay. So wait, we have a circuit, we have some inputs and we just want to tweak them slightly to increase the output value? Why is this hard?"

Checked: https://karpathy.github.io/neuralnets/ (raw HTML), retrieved 2026-11-02
The words "Okay. So wait" sound like someone thinking aloud. Karpathy raises the objection a programmer would have, and then he tries the obvious approach in code. When the obvious approach is a real method, such as averaging returns, let a run show what's wrong with it before the prose explains why.

## Lilian Weng, "What are Diffusion Models?"

Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

> "A nice property of the above process is that we can sample $\mathbf{x}_t$ at any arbitrary time step $t$ in a closed form using reparameterization trick. Let $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$:"

Checked: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (raw HTML; math appears as the page's TeX source), retrieved 2026-11-02
Weng says what the derivation will give the reader before she starts it. She names the technique and defines the new symbols right away. Set up a derivation the same way, and put the reason for each step next to the line that needs it.

> "Recall that when we merge two Gaussians with different variance, $\mathcal{N}(\mathbf{0}, \sigma_1^2\mathbf{I})$ and $\mathcal{N}(\mathbf{0}, \sigma_2^2\mathbf{I})$, the new distribution is $\mathcal{N}(\mathbf{0}, (\sigma_1^2 + \sigma_2^2)\mathbf{I})$."

Checked: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (raw HTML; math appears as the page's TeX source), retrieved 2026-11-02
A single sentence reminds the reader of a fact and sits next to the step that uses it. Reminders in a lesson can be this short.
