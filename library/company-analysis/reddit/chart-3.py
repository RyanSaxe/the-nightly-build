import plotly.graph_objects as go

# Revenue guidance issued the prior quarter vs the actual result, $M.
# Guidance ranges and actuals from Reddit quarterly press releases.
# Q3'26 actual is not yet reported.
quarters = ["Q4'25", "Q1'26", "Q2'26", "Q3'26"]
guide_low = [655, 595, 715, 860]
guide_high = [665, 605, 725, 870]
actual = [726.0, 663.0, 804.9, None]

guide_mid = [(lo + hi) / 2 for lo, hi in zip(guide_low, guide_high)]
err_up = [hi - mid for hi, mid in zip(guide_high, guide_mid)]
err_dn = [mid - lo for mid, lo in zip(guide_mid, guide_low)]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Guidance range issued",
        x=quarters,
        y=guide_mid,
        mode="markers",
        error_y=dict(
            type="data",
            symmetric=False,
            array=err_up,
            arrayminus=err_dn,
            width=10,
        ),
    )
)
fig.add_trace(
    go.Scatter(
        name="Actual revenue reported",
        x=quarters[:3],
        y=actual[:3],
        mode="markers+text",
        text=[f"${v:.0f}M" for v in actual[:3]],
        textposition="middle right",
    )
)

fig.add_annotation(
    x="Q3'26",
    y=865,
    xref="x",
    yref="y",
    showarrow=False,
    text="not yet<br>reported",
    font=dict(size=12),
    xshift=45,
)

fig.update_layout(
    yaxis=dict(title="Quarterly revenue ($M)", range=[560, 900]),
    xaxis_title="Fiscal quarter (guidance issued the prior quarter)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
