"""The Global Carbon Budget's projected change in world fossil CO2 against
what the data later showed, 2015-2026.

Data: Global Carbon Budget 2026 supplement, Table S6 "Comparison of the
projection with realised fossil CO2 emissions (EFOS)", SI pp. 53-55
(projected value, projected range, and "Actual" = first estimate using actual
data, from the next year's budget; leap-year adjusted). "Current estimate" is
derived from the GCB2026 dataset (doi:10.18160/GCP-2026), sheet "Global
Carbon Budget", EFOS incl. cement carbonation, leap-year adjusted, as recorded
in the evidence record. 2020 (projected -6.7%, no range given; first actual
-5.4%) is left off so the scale stays readable.
"""

import plotly.graph_objects as go

years = [2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025, 2026]
projected = [-0.6, -0.2, 2.0, 2.7, 0.5, 4.8, 1.1, 1.1, 0.8, 1.0, -0.4]
low = [-1.6, -1.0, 0.8, 1.8, -0.3, 4.2, 0.0, 0.0, -0.2, 0.2, -1.5]
high = [0.5, 1.8, 3.0, 3.7, 1.4, 5.4, 1.7, 2.1, 1.7, 1.7, 0.6]
first_years = years[:-1]
first_actual = [0.06, 0.20, 1.6, 2.1, 0.1, 5.1, 0.9, 1.3, 1.1, 1.2]
current = [-0.13, -0.29, 1.92, 2.18, 0.48, 5.41, 1.61, 1.77, 1.04, 1.21]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Projected change and range",
        x=years,
        y=projected,
        mode="markers",
        marker=dict(symbol="line-ew-open", size=26, line=dict(width=4), color="#3f6f8f"),
        error_y=dict(
            type="data",
            symmetric=False,
            array=[h - p for h, p in zip(high, projected)],
            arrayminus=[p - l for p, l in zip(projected, low)],
            thickness=10,
            width=0,
            color="rgba(63,111,143,0.35)",
        ),
    )
)
fig.add_trace(
    go.Scatter(
        name="First estimate, a year later",
        x=first_years,
        y=first_actual,
        mode="markers",
        marker=dict(symbol="circle", size=16, color="#a24935"),
    )
)
fig.add_trace(
    go.Scatter(
        name="Estimate in the 2026 dataset",
        x=first_years,
        y=current,
        mode="markers",
        marker=dict(symbol="diamond-open", size=16, line=dict(width=2), color="#4a4f57"),
    )
)
fig.add_hline(y=0, line_width=1.5, line_color="#4a4f57")
fig.add_annotation(
    x=2015, y=0.5, text="2015: projected fall,<br>first estimate a rise",
    showarrow=True, arrowhead=0, ax=95, ay=-190, font=dict(size=28), align="left",
)
fig.update_layout(
    yaxis_title="Growth on previous year, %",
    xaxis=dict(tickfont=dict(size=26), tickmode="array", tickvals=years, ticktext=["’" + str(y)[2:] for y in years]),
    yaxis=dict(range=[-2.2, 8.4], dtick=2, tickfont=dict(size=26), title=dict(font=dict(size=26))),
    legend=dict(orientation="v", yanchor="top", y=0.99, x=0.36, font=dict(size=26), bgcolor="rgba(255,255,255,0.85)"),
    font=dict(size=26),
    margin=dict(t=20, b=60, l=110, r=10),
)
