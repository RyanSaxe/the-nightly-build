import plotly.graph_objects as go

# Source: Vaswani et al., "Attention Is All You Need" (arXiv:1706.03762),
# Table 1 (self-attention's per-layer complexity O(n^2 . d) in sequence
# length n); Gu, Goel & Re, "Efficiently Modeling Long Sequences with
# Structured State Spaces" (arXiv:2111.00396), which reports O(n log n);
# Gu & Dao, "Mamba: Linear-Time Sequence Modeling with Selective State
# Spaces" (arXiv:2312.00752), which reports linear scaling in n and
# sequences up to 1,000,000 tokens. Curves are the named complexity
# classes as a function of sequence length alone (model width d held
# fixed), each indexed to 1x at n = 128 tokens; they show how the
# classes diverge, not a measured wall-clock benchmark.

n = [128, 512, 2048, 8192, 32768, 131072, 524288, 1048576]
n0 = n[0]

quadratic = [(x / n0) ** 2 for x in n]
linearithmic = [
    (x * (x.bit_length() - 1)) / (n0 * (n0.bit_length() - 1)) for x in n
]
linear = [x / n0 for x in n]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Self-attention, O(n²)",
        x=n,
        y=quadratic,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="S4, O(n log n)",
        x=n,
        y=linearithmic,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Mamba, O(n)",
        x=n,
        y=linear,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="Sequence length, tokens (log scale)",
    yaxis_title="Compute relative to 128 tokens (log scale)",
    xaxis=dict(
        type="log",
        tickvals=[128, 2048, 32768, 524288],
        ticktext=["128", "2K", "32K", "512K"],
    ),
    yaxis=dict(type="log"),
)
