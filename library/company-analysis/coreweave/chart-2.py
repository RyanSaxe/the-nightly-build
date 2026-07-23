# Chart 2: CRWV share price (monthly) against quarterly revenue.
# Price: public monthly close series for CRWV (month-open close), 2025-04 to
# 2026-07, from stockanalysis.com/stocks/crwv/history. All-time-high close was
# $183.58 on 2025-06-20 (stockanalysis.com);
# the monthly points understate that intra-month peak. Quarterly revenue owned
# by CoreWeave's 10-Q/10-K filings (CIK 0001769628). Price in US$, revenue in
# US$ millions.
import plotly.graph_objects as go

months = [
    "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09",
    "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03",
    "2026-04", "2026-05", "2026-06", "2026-07",
]
price = [41.30, 111.31, 163.06, 114.13, 103.04, 136.85,
         133.71, 73.12, 71.61, 93.19, 79.56, 77.47,
         111.60, 109.53, 99.54, 82.64]

rev_q = ["2025-03", "2025-06", "2025-09", "2025-12", "2026-03"]
rev = [982, 1213, 1365, 1572, 2078]

fig = go.Figure()
fig.add_trace(go.Bar(name="Quarterly revenue (right)", x=rev_q, y=rev, yaxis="y2",
                     opacity=0.45))
fig.add_trace(go.Scatter(name="Share price (left)", x=months, y=price,
                         mode="lines+markers"))

fig.update_layout(
    xaxis_title="Month",
    yaxis=dict(title="CRWV share price (US$)"),
    yaxis2=dict(title="Quarterly revenue (US$M)", overlaying="y", side="right",
                showgrid=False, range=[0, 2400]),
    margin=dict(r=90),
    legend_title_text="",
)
fig.add_annotation(x="2025-06", y=163.06, yref="y",
                   text="Peak: $183.58 close, 20 Jun 2025",
                   showarrow=True, arrowhead=2, ax=40, ay=-40)
fig.add_annotation(x="2025-11", y=73.12, yref="y",
                   text="~60% drawdown by Dec 2025",
                   showarrow=True, arrowhead=2, ax=0, ay=40)
