# Chart 2: what moved Epoch's agentic inference capacity per H100-equivalent of
# peak 8-bit compute between Q2 2025 and Q2 2026. Source: Epoch AI's
# agentic_inference_capacity_by_chip_family_quarterly.csv (Data Insight of
# 18 Nov 2026, CC BY), cumulative chips sold to date. Capacity per H100e =
# total inference capacity (GB300e) / total peak 8-bit compute (H100e):
# 1,454,225 / 12,203,971 = 0.11916 in Q2 2025 and 6,665,192 / 31,654,723 =
# 0.21056 in Q2 2026. The change is split by family with a midpoint rule:
# mix term = (change in the family's share of peak compute) x (mean of its
# Q2 2025 and Q2 2026 score per H100e); drift term = (mean share) x (change in
# the family's score). A family with no chips in Q2 2025 enters at its own
# Q2 2026 score, so all of its effect is mix. Terms below are from that split.
# "Other families, mix" sums TPU v8i +0.00074, earlier TPUs -0.00246, other
# Nvidia -0.00135, AMD -0.00074, Trainium -0.00019, other chips -0.00003.
# "Score drift" sums AMD +0.00254, Trainium +0.00103, other chips +0.00059,
# Hopper +0.00027 (families that pool several chips). Axis starts at zero.
import plotly.graph_objects as go

start = 0.11916
end = 0.21056
steps = [
    ("Blackwell<br>Ultra mix", 0.08431),
    ("TPU v7<br>mix", 0.02859),
    ("Blackwell<br>mix", -0.01114),
    ("Hopper<br>mix", -0.01075),
    ("Other<br>mix", -0.00403),
    ("Score<br>drift", 0.00443),
]

labels = ["Q2 2025"] + [s[0] for s in steps] + ["Q2 2026"]
bases, heights, colors, texts = [0.0], [start], ["#6b6b6b"], ["0.119"]
running = start
for _, delta in steps:
    bases.append(min(running, running + delta))
    heights.append(abs(delta))
    colors.append("#2f6f8f" if delta > 0 else "#a24935")
    texts.append(f"{delta:+.3f}")
    running += delta
bases.append(0.0)
heights.append(end)
colors.append("#6b6b6b")
texts.append("0.211")

fig = go.Figure(
    go.Bar(
        x=labels,
        y=heights,
        base=bases,
        marker_color=colors,
        text=texts,
        textposition="outside",
        textfont=dict(size=24),
        cliponaxis=False,
    )
)
fig.update_yaxes(
    title_text="GB300 units per H100 of 8-bit compute",
    title_font=dict(size=22),
    title_standoff=20,
    tickfont=dict(size=22),
    range=[0, 0.25],
)
fig.update_xaxes(tickfont=dict(size=22))
fig.update_layout(showlegend=False, margin=dict(l=120, b=100))
