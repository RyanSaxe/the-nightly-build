import plotly.graph_objects as go

# Swartz et al. 2019, J Asthma, pooled odds ratios vs no child care.
# Each row: outcome, age band at diagnosis, OR, 95% CI low, CI high.
rows = [
    ("Wheeze, under age 2", 1.80, 1.38, 2.36),
    ("Asthma, ages 3-5", 0.66, 0.50, 0.87),
    ("Asthma, ages 6-18", 0.98, 0.66, 1.47),
    ("Wheeze, ages 6-18", 0.43, 0.27, 0.68),
]

labels = [r[0] for r in rows]
ors = [r[1] for r in rows]
lo = [r[1] - r[2] for r in rows]     # lower whisker length
hi = [r[3] - r[1] for r in rows]     # upper whisker length

# Plot top-to-bottom in listed order.
y = list(range(len(rows), 0, -1))

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=ors,
        y=y,
        mode="markers",
        marker=dict(size=11),
        error_x=dict(
            type="data",
            symmetric=False,
            array=hi,
            arrayminus=lo,
            thickness=1.6,
            width=6,
        ),
        showlegend=False,
    )
)

fig.add_vline(x=1.0, line_width=1.2, line_dash="dot")

fig.update_xaxes(
    title_text="Pooled odds ratio vs no child care (log scale)",
    type="log",
    tickvals=[0.25, 0.5, 1, 2],
    ticktext=["0.25", "0.5", "1.0", "2.0"],
    range=[-0.68, 0.42],
)
fig.update_yaxes(
    tickvals=y,
    ticktext=labels,
    range=[0.4, len(rows) + 0.6],
)
fig.update_layout(
    margin=dict(l=200, r=40, t=40, b=70),
    annotations=[
        dict(x=0.0, y=len(rows) + 0.45, xref="x", yref="y",
             text="fewer", showarrow=False, font=dict(size=13)),
        dict(x=0.30, y=len(rows) + 0.45, xref="x", yref="y",
             text="more", showarrow=False, font=dict(size=13)),
    ]
)
