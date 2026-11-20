"""Newcomers per TOP500 list, June 2012 to November 2026, split by Country.

Data: TOP500 list files, entries whose "First Appearance" equals the list's own
edition number, computed by the evidence record's compute.py (series.csv columns
newcomers_cn and newcomers_noncn; "China" = Country == "China" in that list).
The November 2026 file holds 28 newcomers; the TOP500 release of 16 Nov 2026 says 27.
"""

import plotly.graph_objects as go

lists = [
    "2012-06", "2012-11", "2013-06", "2013-11", "2014-06", "2014-11",
    "2015-06", "2015-11", "2016-06", "2016-11", "2017-06", "2017-11",
    "2018-06", "2018-11", "2019-06", "2019-11", "2020-06", "2020-11",
    "2021-06", "2021-11", "2022-06", "2022-11", "2023-06", "2023-11",
    "2024-06", "2024-11", "2025-06", "2025-11", "2026-06", "2026-11",
]
newcomers_noncn = [140, 143, 140, 111, 86, 64, 84, 49, 82, 78, 74, 41, 80, 51, 49, 37,
                   25, 31, 49, 61, 39, 39, 43, 47, 46, 54, 48, 45, 42, 27]
newcomers_cn = [27, 22, 38, 18, 28, 4, 5, 87, 72, 35, 38, 96, 53, 103, 45, 65,
                33, 13, 9, 9, 0, 2, 1, 0, 0, 0, 0, 0, 1, 1]
labels = [("Jun " if l.endswith("06") else "Nov ") + l[:4] for l in lists]

fig = go.Figure()
fig.add_trace(go.Bar(name="Outside China", x=labels, y=newcomers_noncn))
fig.add_trace(go.Bar(name="China", x=labels, y=newcomers_cn))
for label, n in (("Jun 2020", 25), ("Nov 2020", 31), ("Nov 2026", 27)):
    fig.add_annotation(x=label, y=n / 2, text=str(n), showarrow=False, textangle=-90,
                       font=dict(size=30, color="white"))
fig.update_layout(
    barmode="stack",
    bargap=0.12,
    yaxis_title="New entries",
    legend=dict(orientation="h", y=0.99, x=0.99, xanchor="right", yanchor="top",
                traceorder="normal"),
    font_size=26,
    margin=dict(t=20, b=70, l=120, r=30),
)
# The renderer exports a fixed 1200x675 canvas shown about 340 px wide on a phone,
# so type is set large. Each year tick sits on that year's June list, so a year's
# two entries read from its tick rightwards.
year_ticks = [l for l in labels if l.startswith("Jun") and int(l[-4:]) % 4 == 0]
fig.update_xaxes(type="category", tickangle=0, tickvals=year_ticks,
                 ticktext=[t[-4:] for t in year_ticks])
fig.update_xaxes(tickfont_size=40, ticklabelstandoff=12)
fig.update_yaxes(ticklabelstandoff=14)
fig.update_yaxes(tickfont_size=40, title_font_size=34)
fig.update_layout(legend_font_size=36)
