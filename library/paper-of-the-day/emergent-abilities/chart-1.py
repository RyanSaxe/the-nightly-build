import plotly.graph_objects as go

# GPT-3 few-shot exact-match accuracy on integer arithmetic, by model size.
# Source: Brown et al. 2020, "Language Models are Few-Shot Learners",
# Appendix H, Table H.1, p.63 (few-shot columns, K=50 in-context examples).
# The eight GPT-3 sizes, in parameters (Table 2.1).
labels = ["125M", "350M", "760M", "1.3B", "2.7B", "6.7B", "13B", "175B"]
params = [0.125, 0.35, 0.76, 1.3, 2.7, 6.7, 13, 175]  # billions, log x-axis

# Exact-match accuracy (%), Table H.1 few-shot rows.
addition_3d = [0.15, 0.45, 0.30, 0.55, 0.75, 0.90, 8.40, 80.4]   # 3D+
multiply_2d = [1.35, 2.90, 2.70, 2.85, 4.25, 6.10, 7.05, 29.2]   # 2Dx

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="3-digit addition",
        x=params,
        y=addition_3d,
        mode="lines+markers",
        text=labels,
    )
)
fig.add_trace(
    go.Scatter(
        name="2-digit multiplication",
        x=params,
        y=multiply_2d,
        mode="lines+markers",
        text=labels,
    )
)
fig.update_layout(
    xaxis_title="GPT-3 model size (billions of parameters, log scale)",
    yaxis_title="Exact-match accuracy (%)",
)
fig.update_xaxes(type="log", tickvals=params, ticktext=labels)
fig.update_yaxes(range=[-3, 90])
