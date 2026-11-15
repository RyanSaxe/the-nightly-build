"""Annual confirmed US measles cases, 2000-2026.

Data: CDC "Measles Cases and Outbreaks" data table as archived on CDC Stacks
(https://stacks.cdc.gov/view/cdc/157490, captured 14 June 2024) for 2000-2017,
and the current CDC page (https://www.cdc.gov/measles/data-research/index.html,
updated 13 November 2026) for 2018-2026. 2026 is a partial year, to 12 November.
"""

import plotly.graph_objects as go

cases = {
    2000: 85, 2001: 116, 2002: 44, 2003: 56, 2004: 37, 2005: 66,
    2006: 55, 2007: 43, 2008: 140, 2009: 72, 2010: 63, 2011: 220,
    2012: 55, 2013: 187, 2014: 667, 2015: 191, 2016: 86, 2017: 120,
    2018: 381, 2019: 1274, 2020: 13, 2021: 49, 2022: 121, 2023: 59,
    2024: 285, 2025: 2289, 2026: 5412,
}

years = list(cases)
values = [cases[y] for y in years]

BASE = "#8a95a5"      # ordinary years
MARK = "#96640a"      # chart-1: the years the article discusses
PARTIAL = "#1c5cab"   # chart-2: the partial year

colors = [
    PARTIAL if y == 2026 else MARK if y in (2019, 2025) else BASE for y in years
]

fig = go.Figure(
    go.Bar(
        x=years,
        y=values,
        marker_color=colors,
        marker_line_width=0,
        hovertemplate="%{x}: %{y:,} cases<extra></extra>",
        showlegend=False,
    )
)

notes = [
    (2019, 1274, "2019: 1,274<br>status kept"),
    (2025, 2289, "2025:<br>2,289"),
    (2026, 5412, "2026: 5,412<br>to 12 Nov"),
]
for x, y, text in notes:
    fig.add_annotation(
        x=x, y=y, text=text, showarrow=False, yshift=6, yanchor="bottom",
        xanchor={2026: "right", 2025: "right"}.get(x, "center"),
        xshift={2026: 10, 2025: 2}.get(x, 0),
        align="right" if x in (2025, 2026) else "center",
    )

fig.add_annotation(
    x=2000, y=420, text="2000: elimination<br>declared, 85 cases",
    showarrow=False, xanchor="left", xshift=-8, yanchor="bottom",
    align="left",
)

fig.update_layout(
    width=640,
    height=440,
    font=dict(size=16),
    bargap=0.25,
    margin=dict(l=78, r=20, t=20, b=60),
    xaxis=dict(title=dict(text="Year", font=dict(size=16)),
               tickfont=dict(size=16), tickmode="array",
               tickvals=[2000, 2010, 2020],
               range=[1999.4, 2026.6]),
    yaxis=dict(title=dict(text="Confirmed cases", font=dict(size=16)),
               tickfont=dict(size=16), range=[0, 6300], tickformat=","),
)
