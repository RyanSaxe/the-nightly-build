# Chart 1: GB300 NVL72 over H100 SXM (FP8, 400G scale-out profile) in Epoch's
# Inference Performance Index v1, one bar per model, with the three ways of
# summarising them. Scores are the author's per-model area ratios, GB300 = 1
# (columns only_0..only_3 of docs/research/methodology-sensitivity/score_matrix.csv
# in the index author's repository; their mean equals the published H100 score
# 0.0397). Ratio = 1 / score. Arithmetic mean of scores -> 25.2x (the report's
# "about 25x"); geometric mean of scores -> 59.1x. FP8 FLOP/s ratio is
# Epoch's hardware database: 5.0e15 / 1.979e15 dense FP8 = 2.53x.
# Y axis is logarithmic.
import math
import plotly.graph_objects as go

models = ["Qwen3-Coder", "GLM-5.2", "Kimi K3", "MAI proxy"]
h100_score = [0.125202, 0.022619, 0.006303, 0.004604]
ratio = [1 / s for s in h100_score]
mean_score = sum(h100_score) / 4
arith = 1 / mean_score
geo = 1 / math.exp(sum(math.log(s) for s in h100_score) / 4)
flops = 5.0e15 / 1.979e15

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=models,
        y=ratio,
        text=[f"{r:.0f}x" if r >= 10 else f"{r:.1f}x" for r in ratio],
        textposition="outside",
        textfont=dict(size=24),
        cliponaxis=False,
        showlegend=False,
        name="GB300 over H100, one model",
    )
)
for value, label, dash, color in [
    (flops, "8-bit FLOP/s<br>ratio 2.5x", "dot", "#6b6b6b"),
    (arith, "Arithmetic mean<br>of scores (IPI) 25.2x", "solid", "#a24935"),
    (geo, "Geometric mean<br>of scores 59.1x", "dash", "#2f6f8f"),
]:
    fig.add_hline(y=value, line_width=2, line_dash=dash, line_color=color)
    fig.add_annotation(
        xref="paper",
        x=1.0,
        xanchor="left",
        y=math.log10(value),
        yref="y",
        text=label,
        showarrow=False,
        font=dict(size=22, color=color),
        align="left",
    )
fig.update_yaxes(
    type="log",
    range=[math.log10(1.5), math.log10(500)],
    title_text="GB300 over H100 per chip (log)",
    title_font=dict(size=22),
    title_standoff=20,
    tickfont=dict(size=22),
    tickvals=[2, 5, 10, 25, 50, 100, 200],
    ticktext=["2x", "5x", "10x", "25x", "50x", "100x", "200x"],
)
fig.update_xaxes(title_text="", tickfont=dict(size=22))
fig.update_layout(showlegend=False, bargap=0.45, margin=dict(r=270, l=120, b=70))
