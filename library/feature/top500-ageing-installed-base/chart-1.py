"""Age structure of the TOP500, June 2012 to November 2026.

Data: TOP500 list files (TOP500_YYYYMM.xlsx/.xls), "First Appearance" column,
computed by the evidence record's compute.py (series.csv columns n_3y_fa and
n_5y_fa). Age = edition - First Appearance; one edition is six months.
  n_3y_fa: entries with age >= 6 editions (first listed three or more years earlier)
  n_5y_fa: entries with age >= 10 editions (first listed five or more years earlier)
"""

import plotly.graph_objects as go

lists = [
    "2012-06", "2012-11", "2013-06", "2013-11", "2014-06", "2014-11",
    "2015-06", "2015-11", "2016-06", "2016-11", "2017-06", "2017-11",
    "2018-06", "2018-11", "2019-06", "2019-11", "2020-06", "2020-11",
    "2021-06", "2021-11", "2022-06", "2022-11", "2023-06", "2023-11",
    "2024-06", "2024-11", "2025-06", "2025-11", "2026-06", "2026-11",
]
n_3y_fa = [36, 47, 42, 44, 52, 71, 96, 108, 95, 91, 87, 79, 91, 91, 83, 86,
           84, 77, 121, 153, 172, 204, 221, 220, 239, 261, 254, 243, 240, 256]
n_5y_fa = [5, 2, 5, 4, 5, 9, 12, 16, 16, 20, 32, 36, 33, 34, 34, 34,
           43, 42, 38, 45, 52, 50, 70, 74, 90, 92, 113, 106, 117, 138]

# Category labels so plotly does not read the list months as dates.
labels = [("Jun " if l.endswith("06") else "Nov ") + l[:4] for l in lists]
five_plus = n_5y_fa
three_to_five = [a - b for a, b in zip(n_3y_fa, n_5y_fa)]

fig = go.Figure()
fig.add_trace(go.Bar(name="Five years or more", x=labels, y=five_plus))
fig.add_trace(go.Bar(name="Three to five years", x=labels, y=three_to_five))
fig.add_hline(
    y=250,
    line_dash="dot",
    line_width=2,
    line_color="#444",
    annotation_text="250: median entry 3+ years old",
    annotation_position="top left",
    annotation_font_size=34,
)
for label, n in (("Nov 2021", 45), ("Nov 2026", 138)):
    fig.add_annotation(x=label, y=n / 2, text=str(n), showarrow=False, textangle=-90,
                       font=dict(size=30, color="white"))
fig.update_layout(
    barmode="stack",
    bargap=0.12,
    yaxis_title="Entries (of 500)",
    yaxis_range=[0, 290],
    legend=dict(orientation="h", y=1.02, yanchor="bottom", x=0, traceorder="normal"),
    font_size=26,
    margin=dict(t=70, b=70, l=120, r=30),
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
