import plotly.graph_objects as go

# Source: Hoffmann et al. 2022, "Training Compute-Optimal Large Language Models"
# (arXiv:2203.15556), Table 3, "Estimated optimal training FLOPs and training
# tokens for various model sizes" (Section 3.4). Every point below is a published
# value from that table. No point is fitted or invented.
params = [4.0e8, 1.0e9, 1.0e10, 6.7e10, 1.75e11, 2.8e11, 5.2e11, 1.0e12, 1.0e13]
tokens = [8.0e9, 20.2e9, 205.1e9, 1.5e12, 3.7e12, 5.9e12, 11.0e12, 21.2e12, 216.2e12]

# Reference line: exactly 20 training tokens per parameter. This is the paper's
# stated rule of thumb, drawn as a guide, not a fit to the points.
line_x = [3.0e8, 1.3e13]
line_y = [20.0 * x for x in line_x]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="20 tokens / parameter",
        x=line_x,
        y=line_y,
        mode="lines",
    )
)
fig.add_trace(
    go.Scatter(
        name="Chinchilla Table 3 optimum",
        x=params,
        y=tokens,
        mode="markers",
    )
)
fig.update_layout(
    xaxis_title="Model parameters (N)",
    yaxis_title="Optimal training tokens (D)",
)
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
