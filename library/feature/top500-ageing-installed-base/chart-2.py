"""The TOP500 entry bar (Rmax of the No. 500 entry), June 2012 to November 2026.

Data: TOP500 list files, Rmax of the entry ranked 500, in PFlop/s, computed by the
evidence record's compute.py (series.csv column rmax_500_pf).

The two dashed lines are arithmetic on that series, not TOP500 data: a machine that
enters at twice the bar and keeps its Rmax leaves once the bar rises past it.
  Nov 2016 bar 0.3493 PF/s -> entry at 0.6986; the bar passes it in June 2018 (0.7156).
  Nov 2021 bar 1.6491 PF/s -> entry at 3.2982; the bar is 2.8676 in Nov 2026, still below.
"""

import math

import plotly.graph_objects as go

lists = [
    "2012-06", "2012-11", "2013-06", "2013-11", "2014-06", "2014-11",
    "2015-06", "2015-11", "2016-06", "2016-11", "2017-06", "2017-11",
    "2018-06", "2018-11", "2019-06", "2019-11", "2020-06", "2020-11",
    "2021-06", "2021-11", "2022-06", "2022-11", "2023-06", "2023-11",
    "2024-06", "2024-11", "2025-06", "2025-11", "2026-06", "2026-11",
]
rmax_500_pf = [
    0.0608, 0.0764, 0.0966, 0.1178, 0.1337, 0.1534,
    0.1648, 0.2063, 0.2861, 0.3493, 0.4305, 0.5487,
    0.7156, 0.8748, 1.021, 1.142, 1.228, 1.3168,
    1.511, 1.6491, 1.6491, 1.729, 1.872, 2.015,
    2.1299, 2.3102, 2.435, 2.574, 2.6615, 2.8676,
]
labels = [("Jun " if l.endswith("06") else "Nov ") + l[:4] for l in lists]
bar = dict(zip(labels, rmax_500_pf))

entry_2016 = 2 * bar["Nov 2016"]
entry_2021 = 2 * bar["Nov 2021"]

fig = go.Figure()
fig.add_trace(go.Scatter(name="Entry bar: Rmax of No. 500", x=labels, y=rmax_500_pf,
                         mode="lines+markers"))
fig.add_trace(go.Scatter(name="Enters at 2x the bar, Nov 2016",
                         x=["Nov 2016", "Nov 2017", "Jun 2018"],
                         y=[entry_2016] * 3, mode="lines", line=dict(dash="dash", width=4)))
fig.add_trace(go.Scatter(name="Enters at 2x the bar, Nov 2021",
                         x=labels[labels.index("Nov 2021"):],
                         y=[entry_2021] * (len(labels) - labels.index("Nov 2021")),
                         mode="lines", line=dict(dash="dash", width=4)))
# Annotation y on a log axis is given in log10 units.
fig.add_annotation(x="Jun 2018", y=math.log10(0.7156), text="off in Jun 2018",
                   showarrow=True, arrowhead=0, ax=90, ay=90, font_size=34,
                   bgcolor="rgba(255,255,255,0.85)")
fig.add_annotation(x="Nov 2026", y=math.log10(entry_2021), text="still on in Nov 2026",
                   showarrow=False, yshift=30, xanchor="right", font_size=34)
fig.update_layout(
    yaxis_title="Rmax, PFlop/s (log)",
    yaxis_type="log",
    yaxis_range=[-1.3, 0.75],
    legend=dict(orientation="v", y=0.99, x=0.01, bgcolor="rgba(255,255,255,0.85)",
                font_size=34),
    font_size=26,
    margin=dict(t=20, b=70, l=130, r=30),
)
fig.update_yaxes(tickvals=[0.1, 0.2, 0.5, 1, 2, 5], ticktext=["0.1", "0.2", "0.5", "1", "2", "5"])
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
