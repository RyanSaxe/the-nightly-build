import plotly.graph_objects as go

# The swing from an operating loss in FY2025 to operating income in FY2026,
# decomposed. Figures from Peloton's FY2026 SEC-filed earnings release
# (Exhibit 99.1), statement of operations. US$ millions.
# FY2025 operating loss -36.2; gross profit rose ~18.4; operating expenses
# fell 178.5 (1,304.5 -> 1,126.0); FY2026 operating income 160.7.
labels = [
    "FY2025<br>operating loss",
    "Gross profit<br>change",
    "Operating cost<br>reduction",
    "FY2026<br>operating income",
]
measures = ["absolute", "relative", "relative", "total"]
values = [-36.2, 18.4, 178.5, 160.7]
text = ["-36.2", "+18.4", "+178.5", "160.7"]

fig = go.Figure(
    go.Waterfall(
        measure=measures,
        x=labels,
        y=values,
        text=text,
        textposition="outside",
        connector={"line": {"color": "rgba(120,120,120,0.5)"}},
    )
)
fig.update_layout(
    yaxis_title="Operating income (US$ millions)",
    showlegend=False,
)
