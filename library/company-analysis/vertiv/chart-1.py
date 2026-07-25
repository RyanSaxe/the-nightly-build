# Chart 1: VRT share price against Vertiv's order backlog, mid-2025 to
# mid-2026. Price points are the five dated closes confirmed against
# stockanalysis.com's VRT price history (the article's source 3), the
# named source still live after Yahoo Finance's own history page went
# dead; the dashed line joins them as a coarse visual guide only; no
# intermediate close is invented. Backlog is Vertiv's own year-end figure
# from its FY2025 Form 10-K, the only two dates the company discloses.
# Price in US$, backlog in US$ billions.
import plotly.graph_objects as go

price_dates = ["2025-07-02", "2025-10-10", "2026-05-14", "2026-06-26", "2026-07-22"]
price = [124.33, 169.09, 376.15, 303.95, 301.16]

backlog_dates = ["2024-12-31", "2025-12-31"]
backlog = [7.2, 15.0]

fig = go.Figure()
fig.add_trace(go.Bar(name="Order backlog, year-end (right)", x=backlog_dates,
                     y=backlog, yaxis="y2", opacity=0.45, width=60 * 24 * 3600 * 1000))
fig.add_trace(go.Scatter(name="VRT share price, confirmed closes (left)",
                         x=price_dates, y=price, mode="lines+markers",
                         line=dict(dash="dash")))

fig.update_layout(
    xaxis_title="Date",
    yaxis=dict(title="VRT share price (US$)"),
    yaxis2=dict(title="Order backlog (US$ billions)", overlaying="y",
                side="right", showgrid=False, range=[0, 18]),
    margin=dict(r=90),
    legend_title_text="",
)
fig.add_annotation(x="2026-05-14", y=376.15, yref="y",
                   text="All-time-high close: $376.15",
                   showarrow=True, arrowhead=2, ax=30, ay=-40)
fig.add_annotation(x="2026-07-22", y=301.16, yref="y",
                   text="-20% from the peak",
                   showarrow=True, arrowhead=2, ax=40, ay=30)
fig.add_annotation(x="2025-12-31", y=15.0, yref="y2",
                   text="Backlog +109% YoY",
                   showarrow=True, arrowhead=2, ax=-50, ay=-30)
