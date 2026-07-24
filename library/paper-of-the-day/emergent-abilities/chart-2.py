import plotly.graph_objects as go

# The same exact-match metric, one fixed model (GPT-3 175B), as the answer
# lengthens. Scale is held constant, so any fall is a property of the metric,
# not of model size.
# Source: Brown et al. 2020, "Language Models are Few-Shot Learners",
# Appendix H, Table H.1, p.63 (few-shot columns, 175B rows).
digits = [2, 3, 4, 5]  # digits in the addition operands

addition = [100.0, 80.4, 25.5, 9.3]     # 2D+, 3D+, 4D+, 5D+ at 175B
subtraction = [98.9, 94.2, 26.8, 9.9]   # 2D-, 3D-, 4D-, 5D- at 175B

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Addition",
        x=digits,
        y=addition,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Subtraction",
        x=digits,
        y=subtraction,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="Digits in the operands (GPT-3 175B, few-shot)",
    yaxis_title="Exact-match accuracy (%)",
)
fig.update_xaxes(tickvals=digits)
fig.update_yaxes(range=[0, 105])
