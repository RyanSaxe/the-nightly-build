import plotly.graph_objects as go

# Pooled maternal-vaccination efficacy against PCR-confirmed influenza in the
# infant, by infant age band. Omer SB, Clark DR, Madhi SA, et al. Lancet Respir
# Med 2020;8(6):597-608 (three RCTs; 10,002 women, 9,800 liveborn infants).
bands = ["0 to <2 months", "2 to <4 months", "4 to 6 months"]
point = [56, 39, 19]
ci_low = [28, 11, -9]
ci_high = [73, 58, 40]

upper = [hi - p for p, hi in zip(point, ci_high)]
lower = [p - lo for p, lo in zip(point, ci_low)]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Infant efficacy",
        x=bands,
        y=point,
        mode="markers",
        error_y=dict(type="data", array=upper, arrayminus=lower, thickness=1.5, width=8),
    )
)
fig.add_hline(y=0, line_dash="dot", line_width=1)
fig.update_layout(
    yaxis_title="Vaccine efficacy (%)",
    xaxis_title="Infant age",
    showlegend=False,
)
fig.update_yaxes(range=[-20, 90], zeroline=False)
